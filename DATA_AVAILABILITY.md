# Data availability

This repository is public. The challenge dataset terms prohibit redistribution, and the sample is a
child's genome. The following are therefore **deliberately excluded**:

| Excluded | Reason |
|---|---|
| `bub1b_clean.bam / trip13_clean.bam (+ .bai)` | aligned patient reads |
| `candidates_all.tsv` | 539 variants with patient genotypes |
| `sites_BUB1B / sites_TRIP13 / sites_SLC34A1.tsv` | per-locus patient genotypes |
| `spliceai_bub1b / spliceai_lztr1 / spliceai_rawscores_bub1b / lztr1_locus_annotated / lztr1_rawscores.tsv` | SpliceAI output tables carrying patient GT columns |
| `secondary_pgx_hits.tsv / pgx_coding_variants.tsv` | patient pharmacogenomic genotypes |
| `mt_heteroplasmy_qc.tsv / mt_depth.txt` | per-position mitochondrial data for the patient |
| `CLINICAL_HANDOFF.md` | clinical-team document containing patient pharmacogenomic findings |
| `METHODS.md / REVISION_analisis_MVA.md / FASTQ_PLAN.md` | internal working logs |
| `WGS_EX2312012*.vcf.gz / *.fastq.gz` | the challenge dataset itself — redistribution is prohibited |

**Every excluded table is regenerable** from the code in `code/` plus the challenge dataset, which
the judging panel holds. Nothing needed to verify the method is missing.

## What is included, and why it is safe to publish

- `resources/` — derived entirely from public databases (Ensembl, GO, ClinGen, ClinVar, UCSC
  RepeatMasker, UniProt). Contains no patient data.
- `literature/` — structured extractions from PubMed abstracts. No patient data.
- `results/` — aggregate statistics only: per-chromosome coverage and allele-balance summaries,
  per-window depth and GC, per-gene depth. No per-variant genotypes.
- `results/ranked_predictions.tsv` and `results/acmg_classification.tsv` — the submitted candidate
  set. These four variants are disclosed by the submission itself, which goes to the leaderboard by
  design of the challenge.
- `figures/` — variant positions appear in one panel without genotypes; all other panels are
  aggregate. Figure labels are in Spanish while the report is in English.

## A note on the excluded genotype tables

The largest excluded files are a 141,559-variant annotated table and a 3.7-million-site depth and
allele-balance table. These are not merely intermediate results: together they constitute a portion
of an identifiable individual's genome. Publishing them would be a re-identification risk
independent of the dataset licence.
