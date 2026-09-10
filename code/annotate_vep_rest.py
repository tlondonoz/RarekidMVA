"""Annotate a variant list with the Ensembl VEP REST API, in parallel, resumable.

Input : TSV with CHROM POS REF ALT ... (from bcftools query)
Output: JSONL, one VEP result object per line (plus batch bookkeeping)
"""
import json, sys, time, urllib.request, urllib.error, os
from concurrent.futures import ThreadPoolExecutor, as_completed

IN_TSV   = sys.argv[1]
OUT_JSONL = sys.argv[2]
BATCH    = 200
WORKERS  = 3
WAVE     = 12          # futures in flight at once — caps peak memory on small hosts

URL = ("https://rest.ensembl.org/vep/homo_sapiens/region?"
       "af_gnomade=1&af_gnomadg=1&canonical=1&mane=1&hgvs=1&numbers=1&symbol=1&"
       "sift=1&polyphen=1&domains=1&variant_class=1&vcf_string=1")
HDRS = {"Content-Type": "application/json", "Accept": "application/json"}


def load_variants(path):
    out = []
    with open(path) as fh:
        for line in fh:
            f = line.rstrip("\n").split("\t")
            if len(f) < 4:
                continue
            chrom, pos, ref, alt = f[0], f[1], f[2], f[3]
            if alt in (".", "*"):
                continue
            out.append(f"{chrom} {pos} . {ref} {alt} . . .")
    return out


def post(batch, attempt=0):
    data = json.dumps({"variants": batch}).encode()
    req = urllib.request.Request(URL, data=data, method="POST", headers=HDRS)
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        if e.code in (429, 500, 502, 503, 504) and attempt < 6:
            wait = float(e.headers.get("Retry-After", 2 ** attempt))
            time.sleep(min(wait, 60))
            return post(batch, attempt + 1)
        raise
    except Exception:
        if attempt < 6:
            time.sleep(2 ** attempt)
            return post(batch, attempt + 1)
        raise


def main():
    variants = load_variants(IN_TSV)
    batches = [variants[i:i + BATCH] for i in range(0, len(variants), BATCH)]

    done = set()
    if os.path.exists(OUT_JSONL + ".done"):
        done = {int(x) for x in open(OUT_JSONL + ".done").read().split()}
    todo = [(i, b) for i, b in enumerate(batches) if i not in done]
    print(f"variants={len(variants)} batches={len(batches)} todo={len(todo)}", flush=True)

    mode = "a" if done else "w"
    with open(OUT_JSONL, mode) as out, open(OUT_JSONL + ".done", "a") as dn, \
            ThreadPoolExecutor(max_workers=WORKERS) as ex:
        n_ok = 0
        for w in range(0, len(todo), WAVE):
            futs = {ex.submit(post, b): i for i, b in todo[w:w + WAVE]}
            for fut in as_completed(futs):
                i = futs[fut]
                try:
                    res = fut.result()
                except Exception as e:
                    print(f"batch {i} FAILED {type(e).__name__} {str(e)[:120]}", flush=True)
                    continue
                for rec in res:
                    out.write(json.dumps(rec) + "\n")
                del res
                out.flush()
                dn.write(f"{i}\n")
                dn.flush()
                n_ok += 1
                if n_ok % 25 == 0:
                    print(f"  {n_ok}/{len(todo)} batches done", flush=True)
            futs.clear()
    print("finished", flush=True)


if __name__ == "__main__":
    main()
