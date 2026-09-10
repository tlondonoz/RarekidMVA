# Rare Disease, Real Kid — MVA Hackathon 2026, Track 1

**Team:** checkpoint-in-trans
**Model / approach:** `tiered-panel-biallelic` — phenotype-driven tiered panel with genome-wide
exonic scan, biallelic prioritisation, ACMG/AMP classification, and orthogonal exclusion analyses
**Proband:** WGS_EX2312012
**Predictions file:** `checkpoint-in-trans_tiered-panel-biallelic.csv`

---

## 1. Prediction

**Primary candidate — compound heterozygous pair in *BUB1B* (MVA type 1, autosomal recessive):**

| | Allele 1 | Allele 2 |
|---|---|---|
| GRCh38 | chr15:40209701 T>G | chr15:40220612 T>G |
| Transcript | ENST00000287598.11 (MANE Select) | ENST00000287598.11 (MANE Select) |
| HGVS | c.2210T>G, p.Leu737Ter | c.3006T>G, p.Asn1002Lys |
| Consequence | nonsense, exon 17/23 | missense, exon 23/23 |
| gnomAD r4 | popmax 9.98e-05 | AC=1 / 1,461,878; 0 homozygotes |
| ClinVar | Pathogenic/Likely pathogenic, 2 stars, multiple submitters, no conflict (VCV533901) | not recorded for this nucleotide change |
| Call quality | DP 46, GQ 99, AB 0.54, PASS | DP 28, GQ 99, AB 0.46, PASS |
| ACMG class | **Pathogenic** (PVS1, PM2_Supporting, PP4) | **VUS** (PM2_Supporting, PP3_Supporting, PP4) |

EPCR 0.85. **Phase is not demonstrated** — see Limitations.

Two secondary findings are also submitted (*LZTR1*, *SLC34A1*); rationale in section 7.

---

## 2. Design rationale

Three considerations fixed the strategy before the data were examined.

The scoring rule granting half credit for identifying one variant of a heterozygous pair implies the
expected answer is **biallelic**, consistent with MVA being autosomal recessive. The search was
therefore framed as a per-gene biallelic problem — rare homozygote, or two rare variants in the same
gene — rather than a search for a single de novo variant.

F-max penalises burying a correct call in noise, so the target is a **short, ranked list** rather
than an exhaustive one.

The gene panel is built from **curated sources queried at runtime**, so that panel membership is
traceable to a source rather than to recall.

---

## 3. Data and environment

- Input: `WGS_EX2312012_HGWCNDSX7.vcf.gz` (315 MB), GATK HaplotypeCaller, GRCh38, hard-filtered,
  contigs without `chr` prefix; 5,183,806 records, 3,765,246 PASS SNVs.
- Also used: one lane of paired FASTQ (`S16_L001_R1/R2`, 149 bp, Q30 91.5%, ~13x), verified
  byte-identical to the repository and read-pair synchronous before use.
- Compute: 8 CPU cores, ~3 GiB RAM, no GPU. This bounds the design: the `bwa` index for whole GRCh38
  does not fit in 3 GiB, so all whole-genome work is done from the VCF and read-level work is
  restricted to targeted references.
- Phenotype: 8 HPO terms extracted from the supplied clinical document with a DOCX parser.

---

## 4. Method

**Panel construction (693 genes, 69.7 Mb).** Four tiers assembled from live curated queries:
(A) the four curated MVA genes; (B) mitotic and chromosome-segregation genes from GO;
(C) tumour-predisposition genes; (D) ClinGen pediatric actionability genes. Two of the four MVA genes
appear in no GO set, which is why tier A is maintained explicitly rather than relying on ontology
membership. Gene symbols are resolved through alias and UniProt-accession lookup before coordinate
retrieval, which recovers 82 entries that arrive under deprecated identifiers — including *KNL1* (as
CASC5) and *NDC80* (as KNTC2), both core kinetochore components. Coverage of 36 key segregation genes
is verified as a build-time check: 35 of 36 present.

**Genome-wide exonic scan.** 238,109 exonic intervals of protein-coding genes (±20 bp to capture
splice sites), 119.3 Mb, yielding 141,559 variants — 134,547 beyond the panel. This is the
hypothesis-free arm, testing whether any gene outside the panel competes with the panel result.

**Annotation.** Ensembl VEP REST (release 116), MANE Select preferred, with gnomAD r4 frequencies,
SIFT/PolyPhen, and ClinVar co-located variants. Implemented as a batched, resumable parallel
annotator with per-batch checkpointing.

**Zygosity context.** A runs-of-homozygosity scan establishes the proband as male with no autosomal
ROH tracts, i.e. no detectable consanguinity. This sets the prior toward compound heterozygosity
rather than rare homozygosity, and bears on the phase question in section 8.

**Prioritisation.** Rare (gnomAD popmax <1%), functionally impactful, quality-passing (DP≥10, GQ≥20),
then a per-gene biallelic model. Four genes carry a compatible genotype; one is phenotype-coherent.
*SERPINA1* accumulates 23 rare heterozygotes in a single gene, the signature of alignment noise
rather than biology. *MYO15A* and *CBS* have all alleles benign or likely benign in ClinVar at
frequencies up to 0.9%, with clinical pictures unlike the proband's.

**Ranking.** Five evidence axes — gene–disease validity, inheritance fit, variant effect, phenotype
fit, call quality — combined as a **geometric** mean, because diagnostic evidence is conjunctive: a
candidate failing on any single axis should not be rescued by strength on the others. The resulting
score is **elicited expert judgement, not calibrated** against a truth set.

**Classification.** ACMG/AMP (Richards et al. 2015), with PVS1 applied according to the ClinGen SVI
decision tree (Abou Tayoun et al. 2018).

---

## 5. Mechanistic basis

Per UniProt O60566, BubR1 is 1,050 residues with the kinase domain at **766–1050**. Both residues
were verified against the canonical sequence (737 = leucine, 1002 = asparagine). The premature stop
at 737 falls **immediately before the kinase domain and removes it entirely**; the missense falls
**inside** it. This is a null allele combined with a potentially catalytically-compromised allele.

The literature establishes this specific architecture for the disease. PMID 18932004 reports that a
null allele combined with a hypomorphic allele produces MVA, and that BubR1 checkpoint function is
markedly dose-dependent. PMID 40555658 documents compound heterozygosity in *BUB1B* in two MVA
fetuses.

**The tumour discriminates between MVA genes.** PMID 28553959 establishes that biallelic *BUB1B* or
*TRIP13* mutations carry high risk of embryonal tumours with severe checkpoint deficiency, whereas
MVA from biallelic *CEP57* or unknown cause is **not** associated with embryonal tumours. The
proband's rhabdomyosarcoma is therefore evidence for *BUB1B* and against *CEP57* that is independent
of the genetics. Rhabdomyosarcoma in MVA/*BUB1B* is documented across 9 retrieved articles.

A cross-check on the second allele: ClinVar has no record of chr15:40220612 T>G, but does record T>A
at the same position producing the **same p.Asn1002Lys**, classified VUS (VCV4600147). The protein
change is catalogued; this allele reaches it by a different nucleotide route.

The other three MVA genes are clean: *CEP57* carries 7 variants at its locus, *TRIP13* 3, *CENATAC*
20, none simultaneously rare and functionally impactful.

---

## 6. Exclusion analyses

**6.1 Mosaic aneuploidy — negative, with a quantified detection floor.** MVA is defined by mosaic
aneuploidy, so it is tested directly. Depth from 3,765,246 PASS sites — drawn from all four lanes,
i.e. full ~45x — is combined with allele balance.

Two methodological choices are load-bearing. Chromosome-level **means** are dominated by a small
number of very-high-coverage windows and would place chr21 at 57.7x and chr22 at 54.1x against a 44x
baseline; **medians per 1 Mb window** are the appropriate statistic and place chr21 at 44.0x, ratio
1.0000. Because integer medians quantise in 2.3% steps, fine resolution uses a 10% trimmed mean over
the per-window medians.

An **internal artefact calibrator** anchors the interpretation. In a male, real heterozygosity on
chrX is impossible, so the 4,650 heterozygous chrX calls with |BAF−0.5| excess of 0.0268 quantify
this sample's own mismapping noise — and chr20/21/22 show that same magnitude (0.029–0.031). The chrX
coverage ratio of 0.4875 independently confirms the method measures copy number correctly.

The decisive test is joint: a true mosaic trisomy of fraction *f* moves coverage **and** allele
balance in a fixed relationship. No chromosome satisfies it. chr16 and chr19 show elevated coverage
without the corresponding balance shift; chr20, chr21 and chr22 show the balance shift without the
corresponding coverage. GC bias is **measured**: Spearman ρ = 0.458 (p = 5.4e-29) per window and
**ρ = 0.764 at chromosome level**, with depth running 43.0x in the low-GC decile against 45.0x in the
high-GC decile — a 4.7% swing that spans the entire observed between-chromosome range.

Detection floor ≈ **6% cell fraction** for well-behaved chromosomes, ~20–25% for chr21 and chr22,
whose acrocentric short arms give them ten-fold larger sampling error. **This negative does not
exclude the diagnosis**, for three reasons fixed in advance of the test: MVA aneuploidy is
*variegated*, so no single chromosome need reach a detectable fraction; the DNA is peripheral blood,
where aneuploid cells may be counter-selected; and hard filtering removes precisely the
pericentromeric regions. Karyotype with premature chromatid separation counting remains the reference
test for this trait.

**6.2 The intronic candidate at chr15:40216470 — excluded on two independent grounds.** This variant
(A>G, absent from gnomAD) is the strongest positional candidate for a second hypomorphic allele.
SpliceAI 1.3 (TensorFlow 2.15, GRCh38) returns max delta 0.00 for it; all 16 scored variants at the
locus are ≤0.03 against a 0.20 threshold. Because raw-score analysis places the maximum gain site
outside the default window, the locus was rescored at the maximum distance the version accepts
(`-D 4999`); max delta remains 0.030, so the conclusion does not depend on the parameter.
Independently, read-level analysis places the position **3 bp from a (TA)n microsatellite**
(chr15:40216473–40216514); its apparent depth inflates to 124x against ~13x real lane depth through
microsatellite read recruitment, and only 3 reads with a single mismatch support the alternate
allele. The original heterozygous call is of questionable reliability.

**6.3 PM1 tested empirically and not applied.** ClinVar missense variants in *BUB1B* were partitioned
by residue position to test whether the kinase domain is depleted of benign variation. It is not
(OR 1.03, p = 1.0). PM1 was therefore not applied.

**6.4 PVS1 verified against the ClinGen SVI decision tree.** The tree requires establishing whether
the PTC-containing exon can be skipped in the relevant transcript. *BUB1B* has 31 transcripts, 12
coding, and 11 of the 12 contain the exon carrying chr15:40209701; the one that does not is a 4-exon,
138-aa fragment. PVS1 holds at Very Strong. PM4 is not co-applied, as the document prohibits.

**6.5 Recessive Noonan via biallelic *LZTR1* — competing hypothesis excluded.** PMID 30481304
establishes three distinct genotype–phenotype relationships for *LZTR1*: monoallelic inactivating
causes schwannomatosis, monoallelic missense causes dominant Noonan, and **biallelic** causes
autosomal recessive Noonan. This hypothesis carries real weight: recessive Noonan would explain short
stature, failure to thrive and small-for-gestational-age, and RASopathies predispose to embryonal
rhabdomyosarcoma — with a second allele, **five of the eight HPO terms would have a single-gene
explanation** and MVA would be unnecessary. It is excluded on four independent grounds: of 62
annotated variants at the locus only the truncating one is functionally impactful; depth is uniform
with no deletion; there are no non-PASS calls; and the only above-threshold splice candidate is
**rs178294, AF 0.766 with 421,582 homozygotes** — a common splice-modulating polymorphism, removed by
BA1.

**6.6 Mitochondrial genome — negative on four independent criteria.** The supplied VCF contains zero
calls on the MT contig, so this is assessed from reads at 1,490x mean coverage, against a reference
built with **NUMT decoys** drawn from a published catalogue rather than the isolated mitochondrial
genome. The decoy design is validated by the distribution of alignments, the overwhelming majority of
which land on decoys; the inverse risk of decoys depleting legitimate coverage was checked and does
not occur. All 13 classical pathogenic positions are reference. Sixteen heteroplasmy candidates are
excluded by two complementary tests, the decisive one being **edit distance**, which separates
genuine heteroplasmy from divergent uncatalogued NUMT segments.

**6.7 Mobile element insertion in *BUB1B* — NOT ASSESSED at adequate sensitivity.** This is a ceiling
statement, not a negative result, and it matters because published MVA1 cases carry intronic
Alu/transposon insertions as the second allele and such variants are invisible to a short-variant
caller by construction.

A targeted reference without the rest of the genome acts as a magnet: the 120 kb *BUB1B* locus
attracts **17,736,494 raw reads**, equivalent to 22,000x. Filtering (MAPQ≥30, proper pair, NM≤3)
leaves 1,261,572 reads at a **median** depth of 18x; the mean of 410x is not the right statistic
here, with a 95th percentile of 1,947x at residual mismapping foci. A positive control validates the
filter chain for point variants: both candidate variants recover at depth 13 with allele fractions
0.538 and 0.385, consistent with heterozygosity at the lane's own depth.

Both insertion evidence classes, however, are swamped. The locus is 34.9% covered by 138 pre-existing
Alu/L1/SVA elements, and **88.7% of soft clips and 90.3% of discordant pairs fall on those
pre-existing elements** against ~35% expected from their coverage. The only two high-support
positions outside an annotated element are explained by composition: one sits in an MSTB LTR with
clipped sequences that all differ from one another, whereas a real insertion yields clips sharing the
inserted element's sequence; the other sits between two (TA)n microsatellites with clips full of
ATATAT and GTGTGT tracts. Base composition of the clipped segments is AT-rich at 62–67%, incompatible
with both the Alu consensus (~52% GC) and a poly-A tail.

Resolving this requires whole-genome alignment, whose `bwa` index needs ~5.5 GiB against ~3 GiB
available. **A machine limitation, not a data limitation.**

---

## 7. Secondary findings

**Genotype-first screen.** 12,219 ClinVar records across 36 pharmacogenomic, malignant-hyperthermia
and cardiac genes were intersected with the proband's genotypes by exact coordinate — closer to
clinical practice than filtering on predicted impact. The screen returns **zero pathogenic or likely
pathogenic variants**, including none in *RYR1*/*CACNA1S*/*STAC3* (no genetic evidence of malignant
hyperthermia susceptibility, relevant given repeated anaesthesia) and none in the twelve
cardiomyopathy and arrhythmia genes (no identifiable predisposition amplifying anthracycline
cardiotoxicity risk).

**Submitted — *LZTR1* chr22:20996720 C>G**, c.2244C>G p.Tyr748Ter, heterozygous, AC=2 / 1,461,378.
Per section 6.5 this is monoallelic inactivating *LZTR1*, i.e. schwannomatosis, and **does not explain
the proband's phenotype**; it is a secondary finding in the strict sense. PVS1 verified against splice
rescue: the variant creates a strong cryptic acceptor (raw 0.001→0.910) and weakens the natural
acceptor 31 bp away (0.680→0.382), but the resulting 25-nt shift is not a multiple of 3, so both
splicing routes end in frameshift and no in-frame rescue exists. Published surveillance protocol:
PMID 29448935.

**Submitted — *SLC34A1* chr5:177386432 C>T**, retained only for the nephrocalcinosis overlap. gnomAD
AF 0.0041 with 21 homozygotes is incompatible with severe recessive disease, and no second allele
exists. Probable benign carrier; EPCR 0.04.

**Not submitted.** A homozygous 45-bp splice-donor deletion call in *PEX5* is excluded as
unclassifiable on quality grounds (DP 10, GQ 37), with a Zellweger-spectrum phenotype that does not
match. A *CTU2* variant is excluded for absent gene-disease curation. Either would likely have been a
false positive under F-max.

---

## 8. Limitations

1. **Phase is not demonstrated.** The two *BUB1B* variants lie 10,911 bp apart, HaplotypeCaller
   assigned no physical phase group (`PGT`/`PID` empty for both), and no intervening heterozygotes lie
   close enough to chain phase. This is **not resolvable with short reads** at that distance, nor by
   statistical phasing, since one variant is a singleton in 1.46 M alleles. The genotype is
   *compatible* with compound heterozygosity, not *proven* as such. The absence of autosomal ROH
   argues against a single-haplotype origin.
2. **p.Asn1002Lys remains VUS.** PM3 requires phase; PS3 requires a functional assay; PM1 was tested
   and not met. No calibrated metapredictor was applied.
3. **Mobile element insertions not assessed** (section 6.7) — a memory limitation.
4. **Structural and copy-number variants** not assessed beyond depth-based analysis; the VCF does not
   contain them.
5. **Methylation not assessed.** Silver-Russell and Temple syndrome would fit the prematurity, growth
   restriction and short stature, and are **not detectable by sequencing at all** — they require a
   methylation array. This is the most valuable orthogonal test still outstanding.
6. **Confidence scores are elicited expert judgement, not calibrated** against a truth set. The
   phenotype-fit axis is assigned by hand rather than computed by HPO semantic similarity in the
   manner of Exomiser.
7. **Phenotype discordance.** Microcephaly appears in 18 of 40 retrieved MVA abstracts, and
   PMID 31053147 places it among the principal features of MVA1. It is **not** present in the
   proband's phenotype. This is the weakest point of phenotypic concordance.
8. **SpliceAI thresholds** derive from established practice and the SpliceAI-visual paper rather than
   from the original publication (Jaganathan et al. 2019 is closed access and unobtainable through
   open routes). The 0.20 threshold is used permissively, i.e. to **exclude**, which is the
   conservative direction.
9. ***TRIP13* is not excluded.** It carries 3 heterozygous calls in 36.5 kb, with 2,278 zero-coverage
   positions and 27.7% of the gene body under 10x in the analysed lane. Since biallelic *TRIP13* also
   predisposes to embryonal tumours (PMID 28553959), it is the one phenotype-compatible alternative
   that remains open.

---

## 9. What would resolve the open questions

| Test | What it answers |
|---|---|
| Sanger on both positions | that the variants exist — prerequisite to everything else |
| **Parental samples** | phase → PM3 → p.Asn1002Lys ceases to be VUS; 25% recurrence risk; and with abnormal-metaphase counting, possibly the recurrent miscarriages (PMID 40555658 found excess abnormal metaphases in the carrier parent) |
| Karyotype + premature chromatid separation | the defining trait, which sequencing cannot establish (PMID 11746029) |
| Skin fibroblasts + colcemid challenge | whether p.Asn1002Lys is hypomorphic → PS3 (PMID 10877982) |
| Targeted *TRIP13* sequencing | closes the one open alternative |
| Methylation array | covers a mechanism no sequencing test reaches |

---

## 10. Reproducibility

All code, the tiered panel with its provenance, and every intermediate table are in the repository.
Sections 3 through 6.5 run from the VCF alone; sections 6.6 and 6.7 additionally use one FASTQ lane. Wall-clock span 56 hours across 253 executed cells on 8 cores with
no GPU; the dominant single cost is 3.5 hours for the targeted alignment, followed by VEP REST
annotation of 141,559 variants. No proprietary data were used.

External resources: Ensembl (REST, VEP 116, FTP), gnomAD r4, ClinVar, ClinGen (gene validity,
dosage, actionability), GO/QuickGO, UniProt, MyGene, UCSC (rmsk, NUMT catalogue), PubMed E-utilities,
SpliceAI 1.3.

**Generative AI disclosure.** Anthropic, Claude Opus 5, accessed through a Team/Enterprise plan on
the Claude Science platform, under commercial terms with no training on customer content.

**Submission provenance.** The predictions file is the **automated output** of the pipeline for
variant discovery, annotation, filtering, the biallelic model and ranking. The final EPCR values, the
primary/secondary assignment and the ACMG criterion assignments involve **expert curation**; details
in the methods description form.

---

## 11. Key references

- Richards S, et al. Standards and guidelines for the interpretation of sequence variants. Genet Med
  2015. PMC4544753
- Abou Tayoun A, et al. Recommendations for interpreting the loss of function PVS1 ACMG/AMP variant
  criterion. Hum Mutat 2018. PMID 30192042
- PMID 28553959 — checkpoint deficiency and embryonal tumour risk across MVA genes
- PMID 18932004 — null + hypomorphic architecture; BubR1 dose dependence
- PMID 40555658 — compound heterozygous *BUB1B* in MVA fetuses; parental abnormal metaphases
- PMID 30481304 — three genotype–phenotype relationships for *LZTR1*
- PMID 29448935 — schwannomatosis surveillance
- PMID 10877982 — colcemid challenge assay in fibroblasts
- PMID 11746029 — MVA cytogenetic diagnosis with premature chromatid separation
- PMID 31053147 — MVA1 clinical features
