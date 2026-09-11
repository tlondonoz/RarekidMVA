# checkpoint-in-trans — MVA Hackathon 2026

Variant prioritisation for the *Rare Disease, Real Kid* challenge (Sage Bionetworks, 2026).
Proband `WGS_EX2312012`. Approach name: `tiered-panel-biallelic`.

## Result

Primary candidate: **compound heterozygous pair in *BUB1B*** (mosaic variegated aneuploidy type 1,
autosomal recessive).

| | Allele 1 | Allele 2 |
|---|---|---|
| GRCh38 | chr15:40209701 T>G | chr15:40220612 T>G |
| HGVS (ENST00000287598.11) | c.2210T>G, p.Leu737Ter | c.3006T>G, p.Asn1002Lys |
| ACMG | Pathogenic | VUS |

The stop at residue 737 removes the 766–1050 kinase domain entirely; the missense falls inside it.
Phase is **not** demonstrated — the variants lie 10,911 bp apart, which short reads cannot resolve.

Full rationale, evidence and limitations: [`submission/checkpoint-in-trans_track1_report.md`](submission/checkpoint-in-trans_track1_report.md).

## Track 2 — drug repurposing

BubR1 is a vertebrate **pseudokinase**: catalytically dead but essential as a scaffold. Both alleles
reduce functional dosage, so there is nothing to inhibit — and Open Targets finds no pocket of high
or medium quality across 28 tractability buckets. That is why no docking was performed.

| | Candidate | Basis | Approved |
|---|---|---|---|
| 1 | Dasatinib ± quercetin | BubR1 insufficiency is the founding senolytic model; in `BubR1^H/L1002P` mice — this proband's allelic architecture — progeroid severity tracked with SASP complexity | Dasatinib: yes, pediatric from age 1, incl. with chemotherapy |
| 2 | Sirolimus / everolimus | mTORC1 hyperactivity in BubR1-mutant mice | Yes |
| 3 | Translational readthrough | PTC is TGA-A, the most permissive stop class | **No** — ataluren has 0 FDA applications and EU authorisation was not renewed on 28 Mar 2025 |
| ✗ | SAC-directed synthetic lethality | Argued **against**: its window assumes normal cells keep an intact checkpoint, untrue here |

**The analysis that reordered the ranking.** Readthrough does not restore the wild-type residue — at
UGA it inserts Trp, Cys or Arg. Across 247 vertebrate orthologs, position 737 is Leu in 236 and
**none of the three products occurs in any species**, at a site 90% buried. `code/ptc_triage.py`
packages this triage for any nonsense allele.

Full reasoning: [`track2/checkpoint-in-trans_track2_report.md`](track2/checkpoint-in-trans_track2_report.md).
**Hypotheses for laboratory follow-up, not treatment recommendations.**

## Layout

```
submission/    predictions CSV, Track 1 report, methods description form (both tracks)
code/          annotation, scoring, and the readthrough-triage tool
resources/     gene panel and reference annotation derived from public databases
literature/    structured extractions from PubMed abstracts (Track 1)
results/       aggregate statistics and the submitted candidate set
figures/       supporting figures (Track 1)
track2/        Track 2 report, candidate table, mechanism figure, pitch script
               and slides, and the Track 2 literature extractions
```

## Pipeline

1. **Phenotype** — 8 HPO terms parsed from the supplied clinical document.
2. **Panel** — 693 genes / 69.7 Mb in four tiers built from live curated queries: curated MVA genes;
   mitotic and chromosome-segregation genes from GO; tumour predisposition; ClinGen pediatric
   actionability. Symbols resolved through alias and UniProt-accession lookup before coordinate
   retrieval. See `resources/gene_panel.tsv`, which carries the tier provenance per gene.
3. **Hypothesis-free arm** — genome-wide exonic scan, 238,109 intervals (±20 bp for splice sites),
   119.3 Mb, 141,559 variants.
4. **Annotation** — Ensembl VEP REST 116, MANE Select preferred, with gnomAD r4, SIFT/PolyPhen and
   ClinVar. Batched and resumable: `code/annotate_vep_rest.py`.
5. **Zygosity context** — runs-of-homozygosity scan; no autosomal ROH, proband male.
6. **Filtering and biallelic model** — gnomAD popmax <1%, functional impact, DP≥10, GQ≥20, then a
   per-gene biallelic grouping.
7. **Ranking** — five evidence axes combined as a geometric mean.
8. **Classification** — ACMG/AMP (Richards et al. 2015), PVS1 per the ClinGen SVI decision tree
   (Abou Tayoun et al. 2018).
9. **Orthogonal exclusion** — mosaic aneuploidy by joint coverage and allele-balance testing with an
   internal chrX artefact calibrator; SpliceAI 1.3 with raw-score inspection
   (`code/spliceai_rawscores.py`); mitochondrial genome against a NUMT-decoy reference; empirical
   test of PM1.

## Reproducing

The challenge VCF is required and is **not** included here (see Data availability). With
`WGS_EX2312012_HGWCNDSX7.vcf.gz` and its index in place:

```bash
# annotation (resumable; writes one JSON line per variant)
python code/annotate_vep_rest.py input_genotypes.tsv output_vep.jsonl

# SpliceAI raw-score inspection for a locus
python code/spliceai_rawscores.py --help
```

Dependencies: `bcftools`/`samtools`/`htslib`, Python 3.11+ with `pandas`/`numpy`/`scipy`, and
SpliceAI 1.3 (TensorFlow 2.15) for the splicing analyses. Section 6.6–6.7 of the report additionally
use one FASTQ lane with `bwa`.

Wall-clock 56 hours across 253 executed cells on 8 CPU cores, no GPU. The dominant single cost is
3.5 hours for a targeted-locus alignment; the VCF-only arm that produces the primary result runs in
well under an hour.

## Data availability

See [`DATA_AVAILABILITY.md`](DATA_AVAILABILITY.md). In short: **no patient sequence data, genotype
tables or aligned reads are in this repository**, because it is public and the dataset terms prohibit
redistribution. Every excluded table is regenerable from the code here plus the challenge dataset,
which the judging panel holds.

## Generative AI disclosure

Anthropic, Claude Opus 5, accessed through a Team/Enterprise plan on the Claude Science platform,
under commercial terms with no training on customer content.

## Not a clinical report

This is research analysis for a challenge submission. Variants have no orthogonal confirmation, the
analysis was not performed under laboratory accreditation, and the ACMG classifications here are the
authors' application of the published criteria, not a diagnostic laboratory's determination. No
variant in this repository should be used for clinical decision-making without confirmation on a
fresh clinical sample in an accredited laboratory.
