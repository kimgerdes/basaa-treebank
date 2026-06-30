# Building the first glossed & translated treebank of Basaa (A43) — gap analysis & plan

Basaa (Bàsàá, A43, ISO `bas`, Glottolog `basa1284`) has **no dependency or constituency treebank**.
There is no Universal Dependencies treebank for `bas` as of mid-2026. This document states what we
have, what is missing, and a concrete path to the first glossed+translated treebank.

---

## 1. What "glossed and translated treebank" requires

A usable treebank needs, per sentence, **four aligned tiers** plus a syntactic layer:

1. **Text** — Basaa orthography (ideally tone-marked; see the orthography problem below).
2. **Morpheme segmentation + interlinear gloss** (Leipzig-style): noun-class prefixes, agreement
   markers, TAM, derivation.
3. **Free translation** (French and/or English) — the "translated" requirement.
4. **Lemma + POS** per token (UPOS for UD).
5. **Syntactic annotation** — dependency relations (UD) or constituency. This is what does *not* yet
   exist for Basaa in any form.

The CoNLL-U format holds tiers 1, 4, 5 natively and 2–3 in `MISC`/comments. So the target is
**CoNLL-U with `Gloss=` on each token and `# text_fr` / `# text_en` sentence comments.**

---

## 2. What we already have (in this folder)

| Need | Have? | Where |
|---|---|---|
| Glossed, translated example sentences | ✅ small | `docs/basaa.pdf` (NWS, fully glossed); `docs/Hamlaoui_Makasso_2014…pdf` (SVO examples) |
| Running Basaa text | ✅ ~770 sentences | `corpora/opus/Mozilla-l10n_bas.mono.txt` (Common Voice prose) |
| Parallel Basaa–French/English | ✅ tiny, UI-domain | `corpora/opus/*.xml` (~900 + ~760 links) |
| Frequency list (common words) | ✅ | `corpora/opus/Mozilla-l10n_bas.freq` → `glossary/` |
| Speech audio | ✅ 53 files / 178 MB | `recordings/` (GRN) |
| Grammar / syntactic analyses | ✅ | `docs/*.pdf` (Hamlaoui & Makasso) |
| Seed gloss lexicon | ✅ (this project) | `glossary/basaa_glosses.tsv` |
| Worked syntactic analyses → CoNLL-U (SUD + UD) | ✅ (this project, 5 + 10 sentences) | `treebank/` |
| **Speech-aligned, transcribed sentences** | ✅ 10 single sentences + NWS passage | `recordings/aligned/` (Makasso & Lee 2015 sound files) |

---

## 3. What is MISSING (the real gaps)

### A. A morphological analyzer / segmenter
Basaa is agglutinating with **noun-class concord**: every sentence threads class features through
prefixes and agreement (subject marker, augment, CONN, demonstratives). To gloss at scale we need a
segmenter that splits e.g. `á-ÓÓNgÉ` → `á-` (CL2) `-ÓÓNgÉ` (children) and tags agreement. The BULB
project shipped a `basaa` morphology module implementing Hamlaoui & Makasso (2015). **Action:**
obtain/reimplement it; otherwise glossing is fully manual.

### B. Tone-marked orthography & a tone restorer
Two orthographies circulate: a **minimal/toneless** practical orthography and a **fully tone-marked**
one (Hyman / Language Committee). Most running text (Common Voice, GRN) is toneless; the literature
is tone-marked. Tone is lexical *and* grammatical in Basaa (it distinguishes tense — see
`docs/Adda-etal_2022…pdf`: *M̀È nlÒ yani* 'I'll come tomorrow' vs *M̀È ǹlÔ yani* 'I came yesterday').
**A treebank that ignores tone will mis-analyze TAM.** Action: adopt the tone-marked standard as the
canonical layer; use the Adda et al. tone-prediction model to lift toneless corpus text.

### C. A real parallel / translated corpus
The translation tier is thin: only small Mozilla-domain parallel data; **JW300 is not actually
available for `bas`** (claim in `docs/resources.md` is unverified against the live OPUS index); the
Basaa Bible is copyrighted and not bulk-downloadable. **Action:** (i) request **BULBasaa** from ELRA
— it already pairs audio with French oral translation; (ii) harvest the **GRN narration scripts**
(Basaa text + known translation); (iii) hand-translate the elicited IGT we gloss.

### D. POS tagset + UD annotation guidelines for Basaa
No `bas` UD guidelines exist. Decisions to make and document: how to treat the **augment/initial
vowel**, **noun-class prefixes** (features vs separate tokens — recommend features on one token),
**subject markers** (`nsubj` agreement vs clitic), the **connective/associative** `CONN` (→ `case`
or `nmod` head?), **serial verbs**, and **ex-situ focus** fronting. Hamlaoui & Makasso (2015)
argues apparent ex-situ focus keeps the subject as grammatical subject — this **directly sets how
fronted constituents attach**. **Action:** write a short `bas` UD companion doc before mass annotation.

### E. Annotation tooling & a treebank corpus plan
No project file, no annotation environment. **Action:** standardize on CoNLL-U; annotate in a
dependency editor (e.g. **Arborator/UD Annotatrix/INCEpTION**); keep IGT in FLEx or plain Leipzig.

### F. Volume + a second annotator
A first release can be ~100–300 sentences (UD "sample" tier). Need at least a second annotator (or
the original linguists) for agreement scoring. **Action:** contact **Fatima Hamlaoui / E.-M. Makasso**
— authors of under-resourced corpora often share glossed ELAN/FLEx files (the BULBasaa transcription
layer), which would save enormous manual effort.

---

## 4. Recommended pipeline (bootstrap → scale)

```
            ┌─────────────────────────────────────────────────────────────┐
  Phase 0   │ Seed: hand-gloss the NWS passage + literature IGT  (DONE: 5 sents) │
  (now)     │   → glossary/basaa_glosses.tsv,  treebank/*.conllu               │
            └─────────────────────────────────────────────────────────────┘
  Phase 1   Acquire: ELRA BULBasaa request • GRN scripts • Hamlaoui Lingua 2015 PDF
            Decide orthography = tone-marked; set up tone restorer (Adda et al.)
  Phase 2   Write bas-UD companion guidelines (classes, augment, CONN, focus, SVC)
  Phase 3   Annotate 100–300 sentences in CoNLL-U (IGT → UPOS → deps), double-annotate a subset
  Phase 4   Validate with UD tools, compute IAA, release as UD_Basaa-<name>
```

**Single highest-leverage action:** email the BULBasaa authors / ELRA. Their transcribed+orally-
translated 10 h subset is 80% of a treebank's substrate; everything else here is enough to *start*
and to prove the format. The five worked sentences in `treebank/` show the target format end-to-end.
