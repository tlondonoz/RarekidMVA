# Rare Disease, Real Kid — MVA Hackathon 2026, Track 2

**Team:** checkpoint-in-trans
**Proband:** PROBAND01
**Variants:** *BUB1B* chr15:40209701 T>G (c.2210T>G, p.Leu737Ter) and chr15:40220612 T>G
(c.3006T>G, p.Asn1002Lys) — the compound heterozygous pair submitted in Track 1, which matched the
scorer's key.

**These are hypotheses for follow-up investigation. They are not evidence that any medicine works,
and nothing here is a treatment recommendation.** See section 11.

---

## 1. Summary

The lesion is **dosage insufficiency of a scaffolding protein**, not a druggable gain of function.
There is no target to inhibit, so pharmacology must act on the *consequences* of BubR1 insufficiency
or *restore* the protein.

Ordered by what we would actually propose first:

| | Proposal | Mechanistic basis | Status |
|---|---|---|---|
| **0** | **Renal ultrasound surveillance for Wilms tumour** | MVA predisposes to Wilms tumour, including bilateral; the proband is already under renal follow-up for nephrocalcinosis | Not a drug. Highest benefit-to-risk ratio available, and it **precedes** everything below |
| 1 | **mTOR inhibition (temsirolimus; sirolimus/everolimus)** | Two convergent and independent justifications: randomised trial data in this exact histology and age group, and mTORC1 hyperactivity in BubR1-mutant mice | Approved; randomised evidence in pediatric rhabdomyosarcoma |
| 2 | **Dasatinib ± quercetin** (senolytic) | Senescence is causally — not incidentally — responsible for the BubR1-insufficiency phenotype | Dasatinib approved, pediatric from age 1. Proof of concept in BubR1 is **genetic, not pharmacological** |
| 3 | **Translational readthrough** | The premature stop is TGA-A, the most readthrough-permissive class | **No approved medicine available** |
| ✗ | Checkpoint-directed synthetic lethality (KIF18A) | Argued **against** — section 8 |

---

## 2. Mechanism: what is broken

### 2.1 BubR1 is a pseudokinase in vertebrates

The vertebrate C-terminal domain is catalytically inactive. The primary structural and biochemical
literature is the basis for this: the catalytic motifs are evolutionarily degenerate and the putative
catalysis is dispensable for error-free chromosome segregation (PMID 22698286), and the domain binds
nucleotides but cannot deliver catalysis (PMID 26658523). The domain is nonetheless **essential as a
scaffold** — required to promote KARD phosphorylation and kinetochore recruitment (PMID 33207204) and
to maintain the kinase–phosphatase balance at the outer kinetochore (PMID 33860079).

Our literature survey is consistent with this and we report it as a description of the retrieved
corpus rather than as the evidence itself: of 16 retrieved abstracts taking a position, 13 report
catalytic inactivity. Two of the three dissenting reports are *Drosophila*, where the enzyme **is**
genuinely active — the crystallised fly kinase domain adopts a catalytically competent fold
(PMID 31201382) — so they do not speak to the vertebrate protein. **Restricted to vertebrates the
count is 13 to 1**, and that single dissenting report (PMID 24431077) does not measure catalysis: it
infers kinase activity from synuclein-γ binding compromising checkpoint function, which the
scaffolding model explains equally well.

**Consequence:** p.Asn1002Lys is a structural lesion in a scaffolding module, not a loss of enzyme
activity. ATP-competitive pharmacology against BubR1 would be conceptually misdirected.

**Database discrepancy, declared:** UniProt O60566 still annotates `EC 2.7.11.1` and an active site
at Asp882. We follow the primary literature. Note also that PMID 31201382 reports *bubristatin* as a
selective BubR1 kinase antagonist targeting helices αN1 and αC — in *Drosophila*, as a tool compound,
and in the wrong therapeutic direction, but a reader should know it exists.

### 2.2 What each allele does

**p.Leu737Ter** removes the entire pseudokinase domain (766–1050). Everything N-terminal is retained:
the BUB1 N-terminal domain (62–226), the KNL1 interaction region (152–185), the nuclear localisation
signal and the D-box. The premature termination codon lies in **exon 17 of 23** — far more than 50 nt
upstream of the final exon–exon junction — so the transcript is NMD-competent by the canonical
50–55 nt rule and little or no protein is expected. (For reference, the stop is also 313 residues
before the natural termination codon at position 1051; the exon position, not that distance, is what
determines NMD competence.)

**p.Asn1002Lys** destabilises that same domain from the inside. No experimental structure resolves
it: the two cryo-EM structures of the APC/C–MCC complex that align to this region (6TLJ, 5KHU) model
**0 of the 285 pseudokinase-domain residues**. On the AlphaFold model, where local confidence is high
(pLDDT 91.1 against a domain mean of 81.9), Asn1002 is **20.1% solvent accessible** and packs against
an aromatic cluster — Trp973, Phe977, Trp978, Phe997 — in the C-lobe. It lies 19.8 Å from the
degenerate catalytic aspartate and **34.7 Å from the nucleotide-binding lysine**: not a pocket
residue. Asparagine occupies this position in 226 of 247 vertebrate orthologs; lysine in none.

**Net effect: reduced functional BubR1 dosage.** One allele contributes nothing; the other a
destabilised scaffold.

### 2.3 A mouse carries this allelic architecture

PMID 31738183 engineered `BubR1^L1002P` to mimic the human MVA allele *BUBR1*^L1012P and crossed it
with a hypomorphic low-protein allele. `BubR1^H/L1002P` mice are viable and display the MVA
phenotype — cancer predisposition, short lifespan, dwarfism, lipodystrophy, sarcopenia, low cardiac
stress tolerance. Human residue 1012 is leucine and fully buried (0% accessibility, pLDDT 95.3) but
lies 10.3 Å from Asn1002 with no shared contacts, so the parallel is at the level of **allelic
architecture** — a reduced-protein allele plus a C-lobe pseudokinase missense — not of structural
micro-environment. It is nonetheless the closest animal model of this proband's genotype, and it
supplies both mechanistic handles used below: progeroid severity tracking with SASP complexity, and
sarcopenia predisposition correlating with mTORC1 hyperactivity.

---

## 3. There is no direct pharmacology against BubR1

Three lines converge, and we are explicit about what each does and does not establish.

**Established:** the vertebrate domain is a pseudokinase (2.1), so there is no catalytic activity to
inhibit; and the therapeutic direction required is *restoration*, not inhibition — a ligand that
binds the protein you need more of does not help.

**Not established — and we flag this rather than claim it:** Open Targets evaluates 28 tractability
buckets for *BUB1B* and returns no high-quality or medium-quality pocket. That bucket is derived from
**ligand and cavity annotation over experimental structures**, and section 2.2 establishes that no
experimental structure covers the pseudokinase domain at all. An annotator with no structure cannot
report a pocket. So "no pocket" here is **absence of evaluation, not a negative result**, and we do
not use it as evidence. What the Open Targets result does show legitimately: no approved drug, no
clinical-phase compound, all antibody buckets negative (intracellular target), and three positive
degrader buckets — degradation being the opposite of what a dosage insufficiency needs.

**Why we performed no docking.** The two established reasons above are sufficient on their own. A
cavity-detection run over the AlphaFold model would convert the pocket question from unevaluated to
evaluated and is the obvious next step, but it would not change the direction argument: even a
well-formed pocket would give an inhibitor, which is not what this lesion needs. Docking was likewise
not applied to the candidates below, because each acts on a target whose drug–target affinities are
already measured experimentally.

**A protein–protein interface stabiliser** was considered as the one strategy that points the right
way (increase function rather than decrease it) and set aside on structural grounds: the interfaces
that govern mitotic-checkpoint-complex assembly — the KEN boxes, the N-terminal TPR region, CDC20
binding — all lie in the N-terminal module that **both alleles retain**, whereas the p.Asn1002Lys
lesion is in the C-lobe. Stabilising BubR1–CDC20 would not correct the lesion this proband has.

---

## 4. Proposal 0 — surveillance, which precedes every drug

MVA is a tumour-predisposition syndrome and its spectrum is not limited to rhabdomyosarcoma.
Bilateral Wilms tumours arising in premature-chromatid-separation/MVA have been reported with
long-term remission after bilateral nephron-sparing surgery (PMID 31081598), and sequential Wilms
tumour and orbital rhabdomyosarcoma have been described in a child with MVA (PMID 42595739).
Biallelic *TRIP13* variants — one of the four MVA genes — specifically predispose to Wilms tumour
(PMID 28553959). Consolidated screening and surveillance recommendations for children with genomic
instability disorders are published (PMID 39264246).

**Practical consequence for this child:** serial renal ultrasound is indicated, and he is **already
under renal follow-up for nephrocalcinosis**, so the incremental cost is close to zero and the risk
is nil. No drug proposal in this report has a comparable benefit-to-risk ratio, and none of them
substitutes for this. We place it first deliberately.

---

## 5. Proposal 1 — mTOR inhibition

**This is the only proposal with randomised trial evidence in the proband's own tumour type and age
group**, and it is supported by two independent chains that converge on the same drug class.

**Oncological chain.** A randomised phase II trial compared bevacizumab versus temsirolimus added to
chemotherapy in first-relapse rhabdomyosarcoma (PMID 31513481, Children's Oncology Group), and a
randomised open-label trial tested the addition of temsirolimus to chemotherapy in children,
adolescents and young adults with intermediate-risk rhabdomyosarcoma (ARST1431, PMID 38936378). The
question of giving an mTOR inhibitor alongside cytotoxic chemotherapy in a child with
rhabdomyosarcoma has therefore already been asked in a trial setting.

**Mechanistic chain.** Sarcopenia predisposition in *BubR1*-mutant mice correlates with mTORC1
hyperactivity (PMID 31738183). mTOR inhibition postpones premature ageing in independent progeroid
models: prelamin A accumulation drives ageing through mTOR overactivation and inhibition delays it
(PMID 32282093); rapamycin rescued differentiation defects in senescent progenitors from
Zmpste24-deficient mice (PMID 31312666); everolimus increases autophagy and reduces progerin in
laminopathies (PMID 29581305).

**The convergence is the argument.** No other proposal here has both an indication-level evidence
base in this histology and a genotype-level mechanistic rationale. And the objection one would
normally raise — immunosuppression during chemotherapy — has been examined in those trials rather
than left to speculation.

**Against it.**
- **The anabolic objection, which is specific to this child and more serious than immunosuppression.**
  He has skeletal muscle atrophy, short stature and failure to thrive. mTORC1 is the central
  regulator of protein anabolism and growth; chronic inhibition acts against the axis that most
  limits his situation. The mouse rationale (mTORC1 hyperactivity correlates with sarcopenia
  predisposition) and the clinical objection (mTOR inhibition compromises muscle protein synthesis
  and linear growth) point in **opposite directions on the same tissue**. This tension is unresolved
  and we do not resolve it.
- **The BubR1–mTOR relationship is not directionally consistent:** in hepatocellular carcinoma, high
  BUB1B *upregulates* mTORC1 signalling (PMID 32977361), the opposite of the progeroid finding.
- **No rapamycin or everolimus experiment in a BubR1 model was retrieved**, so the geroprotective
  limb is an inference across progeroid syndromes, not a direct result in this genotype.

---

## 6. Proposal 2 — senolytic clearance

**The causal chain is strong where it matters most: senescence is not an incidental correlate of
BubR1 insufficiency, it is causal.** p16^Ink4a and p19^Arf play opposing roles in the senescence and
ageing caused by BubR1 insufficiency (PMID 18516091) — this is what makes senescence a target rather
than an observation. Genetic clearance of p16^Ink4a-positive senescent cells delays
ageing-associated disorders in the BubR1 progeroid mouse (PMID 22048312, the founding experiment of
the senolytics field). Senescence is demonstrable across tissues in BubR1 insufficiency — endothelium
and blood–brain barrier (PMID 26883501), skeletal muscle (PMID 26464273), heart (PMID 40607964),
neural progenitors (PMID 28383136) — and accelerated in BubR1-haploinsufficient fibroblasts
(PMID 26847209). In the mouse matching this proband's allelic architecture, progeroid severity
coincided with SASP complexity (PMID 31738183).

**Where the chain weakens, stated in the same terms we use for proposal 1.** The proof of concept in
BubR1 is **genetic** — INK-ATTAC and p16 deletion — **not pharmacological**. Searches for senolytic
drug experiments in BubR1 mice return nothing. The step from genetic clearance to dasatinib is an
**inference of class, not a result in this genotype**. The available drug evidence is in other
systems: dasatinib plus quercetin reduced p16^Ink4a, fibrosis and inflammation and improved renal
function in streptozotocin-induced diabetic nephropathy (PMID 41564845), with human data including
skeletal responses stratified by p16 expression (PMID 39823170) and ex vivo reduction of the
secretory phenotype (PMID 39510246).

**And the biology is not one-directional:** p21 both attenuates and drives senescence and ageing in
BubR1 progeroid mice (PMID 23602569), so the contribution of senescence programs to the phenotype is
tissue-dependent. "Clear senescent cells and the phenotype improves" is a simplification this model
system does not fully support.

**Regulatory fit.** Dasatinib is approved with an explicit pediatric indication from 1 year of age,
one of them *"in combination with chemotherapy"*. **But the schedules are not the same drug use:**
what is characterised in children is *continuous daily* dasatinib as a BCR-ABL-directed antileukaemic.
Senolytic use is an *intermittent pulse* schedule at a different dose with a different
pharmacodynamic rationale — hit-and-run clearance rather than sustained target inhibition. The
pediatric pharmacokinetics transfer; **the safety profile of a senolytic schedule in children does
not**, and we do not claim it does.

**The largest objection, with its mechanism.** Senescence is tumour-suppressive, and the mechanism is
specific: immune surveillance of senescent pre-malignant cells limits tumour development
(PMID 22080947). Clearing senescent cells in a child with a cancer-predisposition syndrome and an
active rhabdomyosarcoma risks removing an antitumour barrier. A further distinction the design must
make: cytotoxic chemotherapy itself induces senescence in tumour cells, so a senolytic given
**concurrently** acts on a senescent population that includes arrested tumour cells, with a net
tumour effect of unknown sign. **Concurrent and sequential administration are not the same question**,
and only an ex vivo-first, sequential design would be defensible.

---

## 7. Proposal 3 — translational readthrough, and the triage that ranks it third

**The codon context is favourable.** c.2210T>G converts the Leu737 codon TTA to **TGA**, with adenine
at +4 — termination tetranucleotide **TGA-A**, context `CCAGAG[TGA]AGTGCC`. TGA is the most
readthrough-permissive stop class (PMID 41015699). The exact context is characterised: TCP-306 is
potent against TGA-A whereas G418 preferentially reads through TGA-C (PMID 41730613), and other
compounds are reported particularly effective on UGAA (PMID 42034525). A class-level recommendation
would stop here.

**The product is the problem — but not uniformly, and we are precise about which part of the argument
holds.** Readthrough at UGA inserts a near-cognate residue: tryptophan, cysteine or arginine. We read
the residue aligned to human 737 across **247 vertebrate orthologs**: leucine in 236 (95.5%), then
Ser 5, Phe 2, Ile 1, Pro 1, with 2 alignment gaps. None of Trp, Cys or Arg appears at this position
in any vertebrate, and the position is 90% buried, packing against Pro802, Phe805, Tyr806 and Leu809.

Taking the three products separately:

| Product | Volume change vs Leu | Verdict |
|---|---|---|
| **Trp** | **+61.1 Å³** into a buried pocket | Argument holds. No vertebrate precedent and a large steric insertion at a 90%-buried site. |
| **Arg** | +6.7 Å³, hydrophobicity −8.3 | Argument holds on charge, not volume: buries a positive charge. Note Arg does occur at the *other* variant position (1002) in 2 species, so charge burial is not categorically forbidden in this domain. |
| **Cys** | −58.2 Å³ | **Argument does not exclude it.** Five orthologs carry **Ser** at this position, which is a *larger* cavity (−77.7 Å³), and Cys is near-isosteric with Ser (19.5 Å³ apart). A substitution more costly in volume than Cys is tolerated in real vertebrates here. |

**Which product dominates is unknown.** Of the 9 retrieved abstracts naming the residues inserted at
UGA, **none reports relative proportions**, so we cannot say whether the disruptive product (Trp) or
the plausibly tolerated one (Cys) predominates in this context. We declare this rather than assume
it, and it is the single measurement that would most change this proposal's ranking.

**Substrate is scarce.** The PTC is in exon 17 of 23 and NMD-competent, and NMD-mediated transcript
reduction limits readthrough efficacy (PMID 34828417).

**Regulatory status is what actually removes this option today.** Ataluren has **no approved
application in Drugs@FDA** — note that Drugs@FDA lists approved applications, so this means it was
never approved in the US, not that no submission was ever attempted — and the European Commission did
not renew its conditional marketing authorisation on 28 March 2025 after the CHMP concluded
effectiveness had not been confirmed; the EMA record lists it as expired. It remains available in the
UK, and EU Directive 2001/83 Articles 117(3) and 5(1) permit continued national use. Aminoglycosides
are approved antibiotics but oto- and nephrotoxic on chronic dosing, a poor fit for a child already
receiving toxic agents.

**Conclusion.** Mechanistically the most direct proposal — it addresses the causal lesion, and the
alternative to a destabilised full-length protein is no protein at all in a dose-dependent disease.
Ranked third because no approved medicine is available and the identity of the dominant readthrough
product is unmeasured.

---

## 8. What we argue against: checkpoint-directed synthetic lethality

Aneuploidy renders cancer cells vulnerable to mitotic checkpoint inhibition, with **KIF18A dependency
as the central finding** (PMID 33505028), and whole-genome doubling confers related vulnerabilities
(PMID 33505027). KIF18A inhibitors are in clinical development, which makes this concrete rather than
hypothetical. (These two papers support the concept; they do not themselves establish MPS1/TTK, AURKA
or CENP-E as the targets, and we do not cite them for that.)

**It should not be applied here, and the argument is stronger than a narrow-window concern.** The
therapeutic window exists because normal cells retain an intact checkpoint while tumour cells do not.
In constitutional *BUB1B* insufficiency the proband's **normal tissue is itself
checkpoint-compromised and already generating aneuploidy** — that is the mechanism of his tumour
predisposition. Perturbing the residual checkpoint would not merely narrow the window; it could
**raise the aneuploidy rate in healthy tissue and so increase tumour risk**. We record this so the
strategy is not adopted by analogy to sporadic aneuploid cancers.

At hypothesis level only: dexamethasone downregulates G2/M and mitotic-spindle checkpoint genes and
enables cells to override the SAC (PMID 33478100), and dexamethasone is widely used in pediatric
oncology. Whether this interacts with a constitutional checkpoint defect is unknown and unstudied.

On spindle poisons more broadly, the evidence does not support any recommendation: of the retrieved
abstracts reporting a direction for checkpoint-weakened cells, 30 report increased sensitivity and 18
increased resistance. **Nothing here justifies altering this child's chemotherapy.**

---

## 9. Routes considered and set aside

- **Pharmacological chaperones.** The precedent (migalastat, CFTR correctors) is small molecules that
  bind a pocket in the misfolded substrate. The pseudokinase domain has no experimental structure and
  therefore no evaluated pocket — the same obstacle that rules out structure-based design generally
  applies here, for the same reason.
- **NMD inhibition alone.** Set aside, and the reasoning is worth stating because it is not
  symmetric. *Combined* with a readthrough agent it is the standard strategy and makes sense here: it
  increases the transcript substrate that is the limiting factor (PMID 34828417). *Alone* it is
  potentially harmful: stabilising the p.Leu737Ter transcript yields a 736-residue protein retaining
  the entire N-terminal module — BUB1 N-terminal domain, KNL1 interaction region, D-box — and lacking
  only the pseudokinase domain. That is a protein which still competes for its assembly partners but
  cannot contribute C-lobe scaffolding function: the profile of a **dominant negative**.
- **Modulating aneuploidy tolerance** (proteotoxic and metabolic stress in aneuploid cells). Set
  aside for a direction problem identical to synthetic lethality: one would want to *increase*
  tolerance in healthy tissue and *decrease* it in the tumour, and a systemic agent does not
  discriminate.
- **Protein–protein interface stabiliser.** Set aside on structural grounds — see section 3.

---

## 10. Limitations

1. **No proposal has clinical evidence in MVA.** The randomised temsirolimus data are in
   rhabdomiosarcoma generally, not in MVA-associated rhabdomyosarcoma, and not in this genotype.
2. **The senolytic proof of concept in BubR1 is genetic, not pharmacological.** No senolytic drug
   experiment in a BubR1 model exists in the retrieved literature.
3. **The mTORC1 geroprotective rationale is correlative** in BubR1 and directionally inconsistent
   across contexts, and the anabolic objection is unresolved.
4. **No experimental structure covers either variant position.** All structural statements derive
   from the AlphaFold model, at high local confidence but experimentally unvalidated. The druggable
   pocket question is **unevaluated, not negative**; cavity detection over the AlphaFold model is the
   obvious next step.
5. **The dominant readthrough product at this codon is unmeasured**, and our volume argument excludes
   Trp but not Cys.
6. **Ortholog tolerance is an evolutionary argument, not a functional assay.**
7. **Abstract counts are descriptive of a corpus defined by our own queries**, not an evidence
   synthesis. They are reported as such.
8. **Oncological risk was not modelled.** The interaction between senolytic therapy and an active
   cancer-predisposition syndrome, and the concurrent-versus-sequential question, are the largest
   open issues and outside what this analysis resolves.
9. **No docking, co-folding or cavity detection was performed.** Section 3 gives the reasoning and
   names what the pocket claim does not establish.
10. **Phase of the two variants remains undemonstrated** — 10,911 bp apart, unresolvable with short
    reads.

---

## 11. Statement on clinical use

This is a computational research analysis submitted to a challenge. It was not performed under
laboratory or clinical accreditation. No variant, mechanism or candidate described here has
orthogonal confirmation. **None of these medicines should be given to this child, or to any patient
with MVA, on the basis of this document.** Each proposal is a hypothesis whose next step is a
laboratory experiment on patient-derived cells, followed — if and only if those succeed — by
institutional review, regulatory consultation and formal trial design conducted by the treating
clinical team. Proposal 0, surveillance, is the exception in kind: it is established practice for
tumour-predisposition syndromes and a matter for the treating team to apply, not a novel hypothesis.

---

## 12. Scalability: the triage generalises

The step that set the ranking of proposal 3 — asking what amino acid readthrough actually inserts,
and whether the protein tolerates it — applies to **any recessive disease with a nonsense allele**.

`ptc_triage.py` implements it. Given a transcript and a nonsense variant it returns the stop-codon
identity and permissiveness class, the +4 nucleotide and termination tetranucleotide, NMD competence,
the near-cognate residues insertable at that stop, the residue distribution at that position across
vertebrate orthologs, and and a per-product volume comparison against the residues actually observed
there — which is what separates Trp from Cys and Arg in this case. It ends in explicit lists of
favourable and unfavourable factors.

```
$ python ptc_triage.py --refseq NM_001211.6 --cds-pos 2210 --alt G \
      --uniprot O60566 --last-junction-nt 2957

  stop_codon: TGA   tetranucleotide: TGAA   permissiveness: most permissive
  nt_upstream_of_last_junction: 747   nmd_competent: true
  near_cognate_products: [W, C, R]    orthologs_aligned: 247
  wt_residue: L   wt_conservation_pct: 95.5   (gap-free: 96.3)
  products_seen_in_orthologs: {W: 0, C: 0, R: 0}
  observed_substitution_volumes: {S: -77.7, F: +23.2, I: 0.0, P: -54.0}
  product_volume_vs_observed:
      W  +61.1   no tolerated substitution of this magnitude at this position
      C  -58.2   not excluded by volume (a larger cavity is tolerated: -77.7)
      R   +6.7   not excluded by volume (a larger insertion is tolerated: +23.2)
  dominant_product: unknown - relative near-cognate insertion frequencies are
                    not measured for this sequence context
  unfavourable: PTC is NMD-competent, so transcript availability limits yield
                none of [W, C, R] occurs at this position in 247 orthologs
  caution:      C is not excluded by volume - a larger cavity (-77.7 A^3) is
                tolerated at this position
                R is not excluded by volume - a larger insertion (+23.2 A^3) is
                tolerated at this position
```

**Declared limits:** the near-cognate set comes from the general literature and is not measured for
this sequence context; relative insertion frequencies at this site are unknown; and ortholog
constraint is evolutionary evidence, not a functional assay.

---

## 13. What would test these hypotheses

| Experiment | What it tests |
|---|---|
| Serial renal ultrasound | Proposal 0 — not a test of a hypothesis but of the child; it is the one item that should start now |
| Phospho-S6 / phospho-4E-BP1 in proband fibroblasts | Whether mTORC1 is hyperactive in this genotype, as proposal 1 assumes |
| Senescence markers (p16^INK4a, SA-β-gal, SASP panel) in proband fibroblasts | Whether the senescent burden that justifies proposal 2 is present in this child |
| Dasatinib ± quercetin *ex vivo* on those fibroblasts, at a senolytic pulse schedule | Proposal 2, directly, without exposing the patient, and at the schedule actually proposed |
| Mass-spectrometric identification of the residue at position 737 after readthrough-agent exposure in proband cells | The unmeasured quantity in proposal 3 — whether Trp or Cys predominates |
| Western blot for full-length BubR1 ± readthrough agent | Proposal 3 — whether any full-length protein is recoverable |
| Colcemid-challenge spindle-checkpoint assay (PMID 10877982) before and after any intervention | The functional readout common to all three drug proposals |

The last row matters most: every drug proposal is ultimately judged by whether checkpoint function or
its downstream consequences improve, and that assay already exists for this disease.

---

## 14. Key references

- PMID 31738183 — BubR1 allelic effects in MVA progeria; `BubR1^H/L1002P`; SASP complexity and mTORC1 hyperactivity
- PMID 22698286 — putative catalysis by human BUBR1 is dispensable for chromosome segregation
- PMID 26658523 — the BubR1 kinase domain binds nucleotides but delivers no catalysis
- PMID 31201382 — *Drosophila* BubR1 kinase domain structure; bubristatin
- PMID 33207204 / PMID 33860079 — the pseudokinase domain as a scaffold
- PMID 18516091 — opposing roles for p16^Ink4a and p19^Arf in BubR1-insufficiency senescence and ageing
- PMID 22048312 — clearance of p16^Ink4a-positive senescent cells delays ageing-associated disorders
- PMID 23602569 — p21 both attenuates and drives senescence in BubR1 progeroid mice
- PMID 22080947 — senescence surveillance of pre-malignant cells limits cancer development
- PMID 41564845 / PMID 39823170 / PMID 39510246 — dasatinib + quercetin, animal and human data
- PMID 31513481 — randomised phase II, temsirolimus in first-relapse rhabdomyosarcoma (COG)
- PMID 38936378 — ARST1431, temsirolimus added to chemotherapy in intermediate-risk rhabdomyosarcoma
- PMID 32282093 / PMID 31312666 / PMID 29581305 — mTOR inhibition in progeroid models
- PMID 32977361 — BUB1B upregulates mTORC1 in hepatocellular carcinoma (opposite direction)
- PMID 39264246 — surveillance recommendations in genomic instability disorders
- PMID 31081598 / PMID 42595739 / PMID 28553959 — Wilms tumour in MVA and TRIP13
- PMID 41730613 / PMID 42034525 / PMID 41015699 — readthrough codon context and compounds
- PMID 34828417 — NMD limits readthrough efficacy
- PMID 33505028 / PMID 33505027 — aneuploidy and KIF18A dependency
- PMID 10877982 — colcemid-challenge spindle-checkpoint assay
