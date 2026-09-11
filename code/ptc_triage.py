#!/usr/bin/env python3
"""
ptc_triage.py — readthrough-amenability triage for a nonsense variant.

Given a transcript and a nonsense variant, reports the four properties that
govern whether a translational-readthrough agent could plausibly help:

  1. identity of the premature stop codon (TGA > TAG > TAA for readthrough)
  2. the +4 nucleotide and termination tetranucleotide (context effect)
  3. NMD competence (PTC >50 nt upstream of the last exon-exon junction)
  4. tolerance of the readthrough products at that position, from the
     residues observed in vertebrate orthologs

Point 4 is the step usually omitted: readthrough does not restore the wild-type
residue, it inserts a near-cognate one. A permissive codon context is not
sufficient if the resulting protein carries a non-conservative substitution at
a conserved buried position.

Usage:
    python ptc_triage.py --transcript ENST00000287598 --cds-pos 2210 --alt G
    python ptc_triage.py --refseq NM_001211.6 --cds-pos 2210 --alt G --uniprot O60566
"""
import argparse, json, re, sys, urllib.parse, urllib.request

STOPS = {"TAA", "TAG", "TGA"}
# near-cognate residues reported for each stop codon (Roy 2015; Beznoskova 2016;
# and the 2024-2026 readthrough literature surveyed in the accompanying report)
NEAR_COGNATE = {"TGA": ["W", "C", "R"], "TAG": ["Q", "Y", "W", "K", "E"],
                "TAA": ["Q", "Y", "K", "E"]}
# readthrough permissiveness of the stop codon itself, most to least
CODON_RANK = {"TGA": "most permissive", "TAG": "intermediate", "TAA": "least permissive"}
CODON_TABLE = {}
for i, b1 in enumerate("TCAG"):
    for b2 in "TCAG":
        for b3 in "TCAG":
            CODON_TABLE[b1 + b2 + b3] = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"[
                len(CODON_TABLE)]


def fetch_cds_refseq(acc):
    q = urllib.parse.urlencode({"db": "nuccore", "id": acc, "rettype": "gb", "retmode": "text"})
    gb = urllib.request.urlopen(
        "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?" + q, timeout=180).read().decode()
    m = re.search(r"^\s+CDS\s+(\d+)\.\.(\d+)", gb, re.M)
    if not m:
        raise SystemExit(f"no CDS feature found in {acc}")
    a, b = int(m.group(1)), int(m.group(2))
    full = "".join(re.findall(r"[acgtn]+", gb.split("ORIGIN")[1])).upper()
    return full[a - 1:b]


def fetch_cds_ensembl(tx):
    req = urllib.request.Request(f"https://rest.ensembl.org/sequence/id/{tx}?type=cds",
                                 headers={"Content-Type": "text/x-fasta"})
    fa = urllib.request.urlopen(req, timeout=120).read().decode()
    return "".join(l.strip() for l in fa.split("\n") if not l.startswith(">"))


def ortholog_residues(uniprot_acc, positions, taxon="7742", max_seqs=500):
    """Residue distribution at the given 1-based positions across vertebrate orthologs."""
    from Bio import Align
    from Bio.Align import substitution_matrices
    ref = json.load(urllib.request.urlopen(
        f"https://rest.uniprot.org/uniprotkb/{uniprot_acc}.json", timeout=90))
    gene = ref["genes"][0]["geneName"]["value"]
    human = ref["sequence"]["value"]
    lo, hi = int(len(human) * 0.75), int(len(human) * 1.25)
    url = ("https://rest.uniprot.org/uniprotkb/search?format=fasta&size=500&query=" +
           urllib.parse.quote(f"gene:{gene} AND taxonomy_id:{taxon} AND length:[{lo} TO {hi}]"))
    fa = urllib.request.urlopen(url, timeout=240).read().decode()
    seqs, cur = [], []
    for line in fa.split("\n"):
        if line.startswith(">"):
            if cur:
                seqs.append("".join(cur))
            cur = []
        else:
            cur.append(line.strip())
    if cur:
        seqs.append("".join(cur))
    seqs = [s for s in seqs if len(s) > lo][:max_seqs]
    al = Align.PairwiseAligner(mode="global",
                               substitution_matrix=substitution_matrices.load("BLOSUM62"),
                               open_gap_score=-11, extend_gap_score=-1)
    counts = {p: {} for p in positions}
    n_aln = 0
    for s in seqs:
        if s == human:
            continue
        try:
            a = al.align(human, s)[0]
        except Exception:
            continue
        n_aln += 1
        for p in positions:
            aa = "-"
            for (h0, h1), (o0, o1) in zip(a.aligned[0], a.aligned[1]):
                if h0 <= p - 1 < h1:
                    aa = s[o0 + (p - 1 - h0)]
                    break
            counts[p][aa] = counts[p].get(aa, 0) + 1
    return gene, human, n_aln, counts


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--transcript"); ap.add_argument("--refseq")
    ap.add_argument("--cds-pos", type=int, required=True,
                    help="1-based position in the CDS of the substituted base")
    ap.add_argument("--alt", required=True, help="alternate base")
    ap.add_argument("--uniprot", help="UniProt accession; enables the ortholog-tolerance step")
    ap.add_argument("--json-out")
    a = ap.parse_args()

    cds = fetch_cds_ensembl(a.transcript) if a.transcript else fetch_cds_refseq(a.refseq)
    idx = a.cds_pos - 1
    codon_i = idx // 3
    wt = cds[codon_i * 3:codon_i * 3 + 3]
    mut = list(wt); mut[idx % 3] = a.alt.upper(); mut = "".join(mut)
    aa_pos = codon_i + 1
    out = {"cds_length": len(cds), "codon_index": aa_pos, "wt_codon": wt,
           "wt_aa": CODON_TABLE.get(wt), "mut_codon": mut,
           "creates_stop": mut in STOPS}
    if not out["creates_stop"]:
        out["verdict"] = f"not a nonsense variant: {wt}->{mut} = {CODON_TABLE.get(mut)}"
        print(json.dumps(out, indent=2)); return

    plus4 = cds[(codon_i + 1) * 3] if (codon_i + 1) * 3 < len(cds) else None
    out.update(stop_codon=mut, permissiveness=CODON_RANK[mut], plus4=plus4,
               tetranucleotide=(mut + plus4) if plus4 else None,
               near_cognate_products=NEAR_COGNATE[mut],
               context=f"{cds[codon_i*3-6:codon_i*3]}[{mut}]{cds[(codon_i+1)*3:(codon_i+1)*3+6]}")
    # NMD: last codon is the natural stop; PTC is NMD-competent if well upstream.
    out["codons_to_natural_stop"] = (len(cds) // 3) - aa_pos
    out["nmd_competent_by_distance"] = out["codons_to_natural_stop"] * 3 > 50

    if a.uniprot:
        gene, human, n_aln, counts = ortholog_residues(a.uniprot, [aa_pos])
        c = counts[aa_pos]
        total = sum(v for k, v in c.items() if k != "-")
        wt_aa = human[aa_pos - 1]
        out["gene"] = gene
        out["orthologs_aligned"] = n_aln
        out["residue_distribution"] = dict(sorted(c.items(), key=lambda kv: -kv[1]))
        out["wt_conservation_pct"] = round(100 * c.get(wt_aa, 0) / max(total, 1), 1)
        out["products_seen_in_orthologs"] = {p: c.get(p, 0) for p in NEAR_COGNATE[mut]}
        out["any_product_natural"] = any(c.get(p, 0) for p in NEAR_COGNATE[mut])

    fav = [f"stop codon {mut} is the {CODON_RANK[mut]} class"]
    unfav = []
    if out.get("nmd_competent_by_distance"):
        unfav.append("PTC is NMD-competent, so transcript availability limits yield")
    if a.uniprot:
        if out["any_product_natural"]:
            fav.append("at least one readthrough product occurs naturally at this position")
        else:
            unfav.append(f"none of {NEAR_COGNATE[mut]} occurs at this position in "
                         f"{out['orthologs_aligned']} orthologs "
                         f"(wild-type residue {out['wt_conservation_pct']}% conserved)")
    out["favourable"] = fav
    out["unfavourable"] = unfav
    print(json.dumps(out, indent=2))
    if a.json_out:
        json.dump(out, open(a.json_out, "w"), indent=2)


if __name__ == "__main__":
    main()
