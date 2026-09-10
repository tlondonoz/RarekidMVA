"""Raw-score SpliceAI analysis, following de Sainte Agathe et al. 2023 (SpliceAI-visual).

Rationale: SpliceAI's published delta scores are differences between variant and reference
predictions. A modest delta added to an already-high reference raw score can still produce a
functional splice site, so a DS below the 0.2 threshold does not by itself exclude a splicing
effect. This script reports the RAW acceptor/donor probabilities for the reference and variant
alleles so that case can be assessed directly.

Usage: python spliceai_rawscores.py <fasta> <chrom> <out.tsv> pos:ref:alt [pos:ref:alt ...]
"""
import sys, os, json
import numpy as np

os.environ.setdefault("TF_CPP_MIN_LOG_LEVEL", "3")
os.environ.setdefault("CUDA_VISIBLE_DEVICES", "")

from pyfaidx import Fasta
from keras.models import load_model
from pkg_resources import resource_filename
from spliceai.utils import one_hot_encode

CONTEXT = 10000        # SpliceAI's receptive field
FLANK = 5000           # sequence reported either side of the variant

fasta_path, chrom, out_tsv = sys.argv[1], sys.argv[2], sys.argv[3]
variants = [v.split(":") for v in sys.argv[4:]]

fa = Fasta(fasta_path)
models = [load_model(resource_filename("spliceai", f"models/spliceai{i}.h5")) for i in range(1, 6)]


def raw_scores(seq):
    """Mean acceptor/donor probability per position across the 5 SpliceAI models."""
    x = one_hot_encode("N" * (CONTEXT // 2) + seq + "N" * (CONTEXT // 2))[None, :]
    y = np.mean([m.predict(x, verbose=0) for m in models], axis=0)
    return y[0, :, 1], y[0, :, 2]          # acceptor, donor


rows = []
for pos, ref, alt in variants:
    pos = int(pos)
    start = pos - FLANK
    end = pos + FLANK
    ref_seq = str(fa[chrom][start - 1:end]).upper()
    off = pos - start                       # 0-based index of the variant within ref_seq
    assert ref_seq[off:off + len(ref)] == ref.upper(), (
        f"reference mismatch at {chrom}:{pos}: fasta has "
        f"{ref_seq[off:off+len(ref)]!r}, variant says {ref!r}")
    var_seq = ref_seq[:off] + alt.upper() + ref_seq[off + len(ref):]

    a_ref, d_ref = raw_scores(ref_seq)
    a_var, d_var = raw_scores(var_seq)

    # align the two coordinate systems on the variant position, then compare
    n = min(len(a_ref), len(a_var))
    for label, r, v in (("acceptor", a_ref[:n], a_var[:n]), ("donor", d_ref[:n], d_var[:n])):
        delta = v - r
        i_gain = int(np.argmax(delta))
        i_loss = int(np.argmin(delta))
        rows.append(dict(chrom=chrom, pos=pos, ref=ref, alt=alt, site=label,
                         rs_ref_at_variant=float(r[off]), rs_var_at_variant=float(v[off]),
                         max_gain=float(delta[i_gain]),
                         rs_ref_at_gain=float(r[i_gain]), rs_var_at_gain=float(v[i_gain]),
                         offset_gain=i_gain - off,
                         max_loss=float(delta[i_loss]),
                         rs_ref_at_loss=float(r[i_loss]), rs_var_at_loss=float(v[i_loss]),
                         offset_loss=i_loss - off,
                         max_rs_ref_window=float(r.max()), max_rs_var_window=float(v.max())))

with open(out_tsv, "w") as fh:
    keys = list(rows[0])
    fh.write("\t".join(keys) + "\n")
    for r in rows:
        fh.write("\t".join(str(r[k]) for k in keys) + "\n")
print(f"wrote {len(rows)} rows to {out_tsv}")
