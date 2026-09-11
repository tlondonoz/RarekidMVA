# Rare Disease, Real Kid — MVA Hackathon 2026, Track 2

**Team:** checkpoint-in-trans
**Proband:** PROBAND01
**Variants under consideration:** *BUB1B* chr15:40209701 T>G (c.2210T>G, p.Leu737Ter) and
chr15:40220612 T>G (c.3006T>G, p.Asn1002Lys), the compound heterozygous pair submitted and confirmed
in Track 1.

**These are hypotheses for follow-up investigation. They are not evidence that any medicine works,
and nothing here is a treatment recommendation.** See section 8.

---

## 1. Summary

The lesion is **dosage insufficiency of a scaffolding protein**, not a druggable gain of function.
That single fact determines the shape of every candidate below: there is no target to inhibit, so the
pharmacology has to act on the *consequences* of BubR1 insufficiency or on *restoring the protein*.

We propose three candidate axes, rank them by the strength of the mechanistic chain, and argue
explicitly against a fourth that the literature would otherwise suggest.

| | Candidate | Mechanistic basis | Approved? |
|---|---|---|---|
| 1 | **Dasatinib ± quercetin** (senolytic) | BubR1 insufficiency is the founding progeroid/senolytic model; progeroid severity tracks with SASP complexity in the mouse whose allelic architecture matches this proband | Dasatinib: yes, pediatric from age 1, including in combination with chemotherapy |
| 2 | **Sirolimus or everolimus** (mTORC1) | mTORC1 hyperactivity documented in BubR1-mutant mice; mTOR inhibition postpones ageing phenotypes in independent progeroid models | Yes, both, with pediatric use |
| 3 | **Translational readthrough** | The premature stop is TGA-A, the most readthrough-permissive stop class | **No** — see section 5 |
| ✗ | SAC-directed synthetic lethality | Aneuploid tumours depend on residual checkpoint | Argued **against** — section 7 |

---

## 2. Mechanism: what is actually broken

**BubR1 is a pseudokinase.** Of the retrieved abstracts that take a position on the catalytic activity
of the C-terminal domain, 13 of 16 conclude that the vertebrate protein is catalytically inactive.
Two of the three dissenting reports are *Drosophila*, where the enzyme is genuinely active — the
crystallised fly kinase domain adopts a catalytically competent fold (PMID 31201382). The third
(PMID 24431077) is human, but it does not measure catalysis: it infers BubR1 "kinase activity" from
the fact that synuclein-γ binding compromises checkpoint function, which the scaffolding model
explains equally well. So the contrary evidence is two studies in an organism where the enzyme is
active, plus one human study whose readout does not distinguish catalysis from scaffolding. In vertebrates the catalytic motifs are evolutionarily degenerate and the putative
catalysis is dispensable for error-free chromosome segregation (PMID 22698286); the domain binds
nucleotides but cannot deliver catalysis (PMID 26658523). UniProt still annotates EC 2.7.11.1 and an
active site at Asp882; the primary literature does not support it.

**The domain is nonetheless essential — as a scaffold.** It is required to promote KARD
phosphorylation and kinetochore recruitment (PMID 33207204) and to maintain the kinase–phosphatase
balance at the outer kinetochore (PMID 33860079). A missense lesion here is therefore a structural
failure of a scaffolding module, not a loss of enzyme activity.

**Allele 1, p.Leu737Ter, removes the entire pseudokinase domain.** Mapping the UniProt features onto
the truncation point, everything N-terminal is retained — the BUB1 N-terminal domain (62–226), the
KNL1 interaction region (152–185), the nuclear localisation signal and the D-box — and only the
766–1050 pseudokinase domain is lost. The stop lies 314 codons upstream of the natural stop, so the
transcript is NMD-competent and little or no protein is expected.

**Allele 2, p.Asn1002Lys, destabilises that same domain from the inside.** No experimental structure
resolves it: the two cryo-EM structures of the APC/C–MCC complex that align to this region (6TLJ at
3.8 Å, 5KHU at 4.8 Å) model 0 of the 285 pseudokinase-domain residues. On the AlphaFold model, where
the local confidence is high (pLDDT 91.1 against a domain mean of 81.9), Asn1002 is **20% solvent
accessible** and packs against an aromatic cluster — Trp973, Phe977, Trp978, Phe997 — in the C-lobe.
It lies 19.8 Å from the degenerate catalytic aspartate and **34.7 Å from the nucleotide-binding
lysine**: it is not a pocket residue. Asparagine is present at this position in 226 of 247 vertebrate
orthologs; lysine occurs in none. Substituting a long positively charged side chain into a partially
buried aromatic environment is a destabilising change.

**Net effect: reduced functional BubR1 dosage.** One allele contributes nothing; the other contributes
a destabilised scaffold.

**A mouse reproduces exactly this architecture.** PMID 31738183 engineered `BubR1^L1002P` to mimic the
human MVA allele *BUBR1*^L1012P and crossed it with a hypomorphic low-protein allele.
`BubR1^H/L1002P` mice are viable and display the MVA phenotype — cancer predisposition, short
lifespan, dwarfism, lipodystrophy, sarcopenia, low cardiac stress tolerance. Human residue 1012 is
leucine and fully buried (0% accessibility, pLDDT 95.3) but lies 10.3 Å from Asn1002 with no shared
contacts, so the parallel is at the level of **allelic architecture** — a reduced-protein allele plus
a C-lobe pseudokinase missense — not of structural micro-environment. That is nonetheless the closest
animal model of this proband's genotype that exists, and it supplies the two mechanistic handles
below.

---

## 3. Why there is no drug against BubR1 itself

Open Targets evaluates 28 tractability buckets for *BUB1B*. Five are positive and none is usable:

- **Small molecule:** no approved drug, no clinical-phase compound, no structure with a ligand, and —
  decisively — **no high-quality pocket and no medium-quality pocket**. The two positive buckets are
  "High-Quality Ligand" and "Druggable Family", the latter an artefact of kinase-family annotation
  that the pseudokinase finding above explains away.
- **Antibody:** every bucket negative (intracellular target).
- **Degrader:** three positive buckets (literature and two ubiquitination records) — but degradation
  is the opposite of what a dosage insufficiency needs.

This is an independent, database-derived confirmation of the structural argument, and it is why no
docking was performed against BubR1: there is no pocket to dock into, and the therapeutic direction
required is restoration, not inhibition. Docking was also not applied to the candidates below,
because each acts on a target whose drug–target affinities are already measured experimentally;
re-deriving them computationally would add no evidence.

---

## 4. Candidate 1 — senolytic clearance (dasatinib ± quercetin)

**The chain.** BubR1 insufficiency causes progeroid disease in mice and drives cellular senescence
across tissues — endothelium and blood–brain barrier (PMID 26883501), skeletal muscle
(PMID 26464273), heart (PMID 40607964), neural progenitors (PMID 28383136) — with accelerated
senescence demonstrable in BubR1-haploinsufficient fibroblasts (PMID 26847209). In the mouse whose
allelic architecture matches this proband, `BubR1^H/L1002P`, several progeroid pathologies were
*attenuated* relative to `BubR1^H/H`, and in skeletal muscle this **coincided with reduced complexity
of the senescence-associated secretory phenotype** (PMID 31738183). Senescent burden is therefore not
an incidental correlate of BubR1 insufficiency; its magnitude tracks disease severity within the
model system closest to this patient.

Pharmacological clearance follows. A senolytic cocktail including dasatinib and quercetin prolonged
survival and reduced senescence markers in a hypomorphic mouse model (PMID 42098153); dasatinib plus
quercetin improved renal function and reduced p16^Ink4a, fibrosis and inflammation (PMID 41564845);
and human data exist, including skeletal responses stratified by p16 expression in T cells
(PMID 39823170) and ex vivo reduction of the secretory phenotype (PMID 39510246).

**Regulatory fit is the strongest of any candidate here.** Dasatinib has 12 FDA applications in
prescription status, and its label carries an explicit pediatric indication from 1 year of age —
including newly diagnosed Ph+ ALL **in combination with chemotherapy**. Pediatric dosing,
pharmacokinetics and safety in a child receiving concurrent cytotoxic therapy are therefore already
characterised, which is precisely this proband's situation.

**Against it.** Quercetin is a dietary supplement with no FDA drug application, so the classical D+Q
pair is not two approved medicines. No senolytic trial has been conducted in MVA or in children for
this indication. Dasatinib carries myelosuppression and pleural-effusion risk that compounds
chemotherapy toxicity. Most importantly, **senescence is itself a tumour-suppressive program**, and
clearing it in a child with a cancer-predisposition syndrome and an existing rhabdomyosarcoma is not
a risk-free manoeuvre; this is the single largest objection and would need to be addressed before any
trial.

---

## 5. Candidate 2 — mTORC1 inhibition (sirolimus, everolimus)

The same mouse paper reports that predisposition to sarcopenia in *BubR1*-mutant animals correlates
with **mTORC1 hyperactivity** (PMID 31738183). mTOR inhibition postpones premature ageing in
independent progeroid models: prelamin A accumulation drives ageing through mTOR overactivation and
mTOR inhibition delays it (PMID 32282093); rapamycin rescued differentiation defects in senescent
progenitors from Zmpste24-deficient mice (PMID 31312666); everolimus increases autophagy and reduces
progerin in laminopathies (PMID 29581305). Both drugs are approved with established pediatric use.

**Against it.** The BubR1–mTOR relationship is **not directionally consistent**: in hepatocellular
carcinoma, high BUB1B *upregulates* mTORC1 signalling (PMID 32977361), the opposite of the progeroid
finding. No rapamycin or everolimus experiment in a BubR1 model was retrieved, so the pharmacological
step is an inference across progeroid syndromes rather than a direct result. And immunosuppression in
a child on cytotoxic chemotherapy is a substantial cost.

---

## 6. Candidate 3 — translational readthrough, and the triage that downgrades it

This is the only axis that addresses the causal lesion. It is ranked third, and the reason is a piece
of analysis that is usually skipped.

**The codon context is favourable.** c.2210T>G converts the Leu737 codon TTA to **TGA**, with adenine
at +4 — termination tetranucleotide **TGA-A**. TGA is the most readthrough-permissive stop class, the
consensus of the abstracts that state a hierarchy and of direct comparison (PMID 41015699). The exact
context is characterised in the recent literature: TCP-306 is potent against TGA-A sequences whereas
G418 preferentially reads through TGA-C (PMID 41730613), and other compounds are reported
particularly effective on UGAA (PMID 42034525). A generic class recommendation would stop here and
conclude the axis is promising.

**The product is not.** Readthrough does not restore leucine; at UGA it inserts a near-cognate residue
— tryptophan, cysteine or arginine, consistently across independent 2024–2026 reports. We therefore
asked whether BubR1 tolerates any of them at position 737, by reading the residue aligned to human
737 in **247 vertebrate orthologs**. Leucine occupies it in 236 (95.5%; the remainder are Ser 5,
Phe 2, Ile 1, Pro 1, with 2 alignment gaps). **None of tryptophan, cysteine or arginine appears at
this position in any vertebrate.** The position is also 90% buried in the AlphaFold model and packs
against Pro802, Phe805, Tyr806 and Leu809 — residues of the pseudokinase domain itself. The
physicochemical cost matches: Leu→Trp adds 61 Å³ to a buried pocket, Leu→Cys removes 58 Å³ and leaves
a cavity, and Leu→Arg buries a positive charge at a hydrophobicity cost of 8.3 Kyte–Doolittle units.

**And the substrate is scarce.** The PTC lies 314 codons upstream of the natural stop, so the
transcript is NMD-competent, and NMD-mediated transcript reduction is documented to limit readthrough
efficacy (PMID 34828417).

**Regulatory status removes what remains.** Ataluren has **zero FDA applications**, and the European
Commission did not renew its conditional marketing authorisation on 28 March 2025 after the CHMP
concluded effectiveness had not been confirmed; the EMA record lists it as expired. It remains
available in the UK, and EU Directive 2001/83 Articles 117(3) and 5(1) permit continued national use.
Aminoglycosides are approved antibiotics but oto- and nephrotoxic on chronic dosing — a poor fit for a
child already receiving toxic agents.

**Conclusion for this axis.** It is not dead: the alternative to a destabilised full-length protein is
no protein at all, and the disease is dose-dependent, so partial restoration could still matter. But
it is downgraded from "restores near-wild-type protein" to "produces a full-length protein of
uncertain stability, using no currently approved medicine". Stating that honestly is the point of the
triage.

---

## 7. What we argue against: SAC-directed synthetic lethality

Aneuploid cancer cells are more dependent on core spindle-assembly-checkpoint components and are
selectively sensitive to their perturbation (PMID 33505028, 33505027). This is the standard rationale
for TTK/MPS1, AURKA and CENP-E inhibitors in aneuploid tumours, and a naive reading would apply it to
this proband's rhabdomyosarcoma.

**It should not be applied here.** That therapeutic window exists because normal cells retain an
intact checkpoint while tumour cells do not. In constitutional *BUB1B* insufficiency the proband's
**normal tissue is itself checkpoint-compromised**, so the window may be narrow, absent, or inverted.
We record this explicitly so the strategy is not adopted by analogy to sporadic aneuploid cancers.

A related observation, at hypothesis level only: dexamethasone downregulates G2/M and mitotic-spindle
checkpoint genes and enables cells to override the SAC (PMID 33478100). Dexamethasone is widely used
in pediatric oncology. Whether this interacts with a constitutional checkpoint defect is unknown and
unstudied; we flag it as a question, not a finding.

On spindle poisons more broadly, the evidence does not support any recommendation. Of the retrieved
abstracts reporting a direction for checkpoint-weakened cells, 30 report increased sensitivity and 18
increased resistance. The literature is genuinely split and context-dependent, and **nothing here
justifies altering this child's chemotherapy.**

---

## 8. Limitations

1. **No candidate has clinical evidence in MVA.** None has been trialled in this disease, in this
   gene, or in this age group for this indication. Every proposal is a hypothesis for follow-up.
2. **The senolytic rationale rests on mouse genetics**, and the pharmacological step (senolytic drugs
   in a BubR1 model) is supported by one retrieved study in a hypomorphic model, not by a trial.
3. **The mTORC1 rationale is correlative** in BubR1 and directionally inconsistent across contexts.
4. **No experimental structure covers either variant position.** All structural statements derive
   from the AlphaFold model, at high local confidence but unvalidated experimentally.
5. **The readthrough near-cognate set is taken from the general literature**, not measured for this
   sequence context; relative insertion frequencies at this specific site are unknown.
6. **Ortholog tolerance is an evolutionary argument, not a functional assay.** Absence of a residue
   across 247 vertebrates is strong evidence of constraint, not proof that the substitution abolishes
   function.
7. **No docking or co-folding was performed.** Section 3 gives the reason. A GPU was not available in
   this environment, but that is not why: the analysis did not call for it.
8. **Oncological risk was not modelled.** The interaction between senolytic therapy and an active
   cancer-predisposition syndrome is the largest open question and is outside what this analysis can
   resolve.

---

## 9. Scalability: the triage generalises

The step that changed the ranking — asking what amino acid readthrough actually inserts, and whether
the protein tolerates it — is not specific to this child. It applies to **any recessive disease with a
nonsense allele**, of which there are thousands.

`ptc_triage.py` implements it as a reusable tool. Given a transcript and a nonsense variant it
returns the stop-codon identity and permissiveness class, the +4 nucleotide and termination
tetranucleotide, NMD competence by distance to the natural stop, the near-cognate residues insertable
at that stop, and the residue distribution at that position across vertebrate orthologs — ending in an
explicit list of favourable and unfavourable factors. Run on this proband it reproduces the section 6
analysis end to end.

```
$ python ptc_triage.py --refseq NM_001211.6 --cds-pos 2210 --alt G --uniprot O60566
  stop_codon: TGA        permissiveness: most permissive      tetranucleotide: TGAA
  near_cognate_products: [W, C, R]        orthologs_aligned: 247
  products_seen_in_orthologs: {W: 0, C: 0, R: 0}
  favourable:   stop codon TGA is the most permissive class
  unfavourable: PTC is NMD-competent, so transcript availability limits yield
                none of [W, C, R] occurs at this position in 247 orthologs
```

The same pattern — take the lesion, ask what the drug mechanism would actually produce, then test
whether the protein tolerates that product — is what separates a class-level recommendation from a
patient-level one, and it is cheap to run at scale.

---

## 10. What would test these hypotheses

| Experiment | Which candidate it tests |
|---|---|
| Senescence markers (p16^INK4a, SA-β-gal, SASP panel) in proband-derived fibroblasts | Whether the senescent burden that justifies candidate 1 is present in this child |
| Ex vivo dasatinib ± quercetin on those fibroblasts, scoring senescent-cell clearance | Candidate 1, directly, without exposing the patient |
| Phospho-S6 / phospho-4E-BP1 in proband fibroblasts | Whether mTORC1 is hyperactive in this genotype, as candidate 2 assumes |
| Western blot for full-length BubR1 ± a readthrough agent in proband cells | Candidate 3 — whether any full-length protein is recoverable at all |
| Colcemid-challenge spindle-checkpoint assay (PMID 10877982) before and after any intervention | The functional readout common to all three: does checkpoint function improve? |

The last row matters most. All three candidates are ultimately judged by whether checkpoint function
or its downstream consequences improve, and that assay already exists for this disease.

---

## 11. Statement on clinical use

This is a computational research analysis submitted to a challenge. It was not performed under
laboratory or clinical accreditation. No variant, mechanism or candidate described here has
orthogonal confirmation. **None of these medicines should be given to this child, or to any patient
with MVA, on the basis of this document.** Each candidate is a hypothesis whose next step is a
laboratory experiment on patient-derived cells, followed — if and only if those succeed — by the
normal route of institutional review, regulatory consultation and formal trial design, conducted by
the treating clinical team.

---

## 12. Key references

- PMID 31738183 — BubR1 allelic effects drive phenotypic heterogeneity in MVA progeria; `BubR1^H/L1002P` model; SASP complexity and mTORC1 hyperactivity
- PMID 22698286 — putative catalysis by human BUBR1 is dispensable for chromosome segregation
- PMID 26658523 — the BubR1 kinase domain binds nucleotides but delivers no catalysis
- PMID 33207204 — the pseudokinase domain is required to promote KARD phosphorylation
- PMID 33860079 — the pseudokinase domain maintains kinase–phosphatase balance at the kinetochore
- PMID 42098153 — senolytic cocktail including dasatinib and quercetin in a hypomorphic mouse
- PMID 41564845 — dasatinib plus quercetin reduces p16^Ink4a, fibrosis and inflammation
- PMID 39823170 — dasatinib plus quercetin, human skeletal responses
- PMID 32282093 / PMID 31312666 / PMID 29581305 — mTOR inhibition in progeroid models
- PMID 41730613 — TCP-306 potent against TGA-A; G418 prefers TGA-C
- PMID 42034525 — readthrough compounds particularly effective on UGAA
- PMID 34828417 — NMD reduces PTC transcript and limits readthrough efficacy
- PMID 33505028 / PMID 33505027 — aneuploid cells depend on residual spindle-checkpoint function
- PMID 10877982 — colcemid-challenge spindle-checkpoint assay in fibroblasts
