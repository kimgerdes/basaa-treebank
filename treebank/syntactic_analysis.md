# Basaa — first syntactic analyses (SUD)

Worked **SUD** (Surface-syntactic Universal Dependencies) analyses of Basaa sentences, built from the
gloss lexicon (`../glossary/`) and glossed sources in `../docs`. Machine-readable:

- [`basaa_sample.sud.conllu`](basaa_sample.sud.conllu) — 5 sentences from the literature.
- [`basaa_aligned.sud.conllu`](basaa_aligned.sud.conllu) — **10 sentences aligned to audio** in
  `../recordings/aligned/` (Makasso & Lee 2015 sound files). This makes the treebank *speech-grounded*.
- [`basaa_sample.ud.conllu`](basaa_sample.ud.conllu) — the original **UD** version, kept for comparison.

Method: **gloss first, then attach.** Each token carries its Leipzig gloss in `MISC Gloss=`, so every
file is simultaneously interlinear glossed text **and** a dependency treebank.

## Why SUD here

SUD is a better fit than UD for a *first* Basaa treebank, for two concrete reasons:

1. **Function words are heads in SUD.** Basaa packs grammar into adposition-like linkers — the
   **connective** ('of'), locative/prepositional particles, and copulas. SUD makes each of these the
   head of its phrase, so a constituent's distribution is read directly off the head. That keeps the
   highly productive **connective construction** (possessor, attributive adjective, relative — all
   linked the same way) under one uniform head-initial analysis instead of UD's `case`/`nmod` split.
2. **Surface criteria for headedness** match what we can actually observe (agreement, prosodic
   phrasing from Hamlaoui & Makasso 2014) better than UD's content-word-head convention.

Throughout, the systematic SUD↔UD mapping used: `nsubj→subj`, `obj→comp:obj`, `xcomp/ccomp→comp:obj`,
`obl(arg)→comp:obl`, `obl(adjunct)/nmod/amod/advmod→mod`; UD `cop`,`case`,`mark` **disappear** because
the copula / adposition / subordinator becomes the head.

---

## 1–2. Transitive clause + concord minimal pair (Hamlaoui & Makasso 2014)

```
Sógól          à-ǹ-téhé        á-ɓóóngé
CL1.grandfather 1.AGR-PST-see   CL2-children
'The grandfather saw the children.'
```
```
        ┌──subj────┐        ┌──comp:obj──┐
      Sógól     à-ǹ-téhé    á-ɓóóngé
       NOUN     VERB(root)    NOUN
```
- Basic order **SVO**; the verb is the root.
- The verb word carries `à-` **subject concord (class 1)** + `-ǹ-` **past** + `-téhé` 'see'
  (`Morph=a-n-tehe`). Swapping a class-2 subject (ex. 2, *á-ór* 'people') flips the concord to `áá-`:
  the **concord, not order, identifies the subject.**
- *SUD vs UD here:* identical tree shape; only the labels change (`subj`, `comp:obj`).

## 3. Possessive NP — the connective (where SUD and UD diverge)

```
bi-bóx   bi       ɓóóngé
CL8-boxes 8.CONN   CL2-children
'the children's boxes'
```
```
   SUD:                              UD (for contrast):
   bibóx (root)                      bibóx (root)
     └─mod─▶ bi                        └─nmod:poss─▶ ɓóóngé
               └─comp:obj─▶ ɓóóngé              └─case─▶ bi
```
- **SUD:** the connective **`bi` is the head** of the possessor phrase (`bi → ɓóóngé` = `comp:obj`),
  and the whole linker phrase attaches to *bibóx* as `mod`. `bi` agrees with the **head** noun (class
  8 → `bi`), which the head-initial SUD analysis makes visually obvious.
- **UD:** *bibóx* governs *ɓóóngé* directly (`nmod:poss`); `bi` is a `case` dependent.
- This is the single most consequential Basaa decision: the connective links possessors **and**
  attributive adjectives **and** relatives. SUD handles all three with one head-initial pattern.

## 4. Identificational question — copula as head (Common Voice)

```
Bés bo  njé ?
1PL COP who
'Who are we?'
```
```
   SUD:  bo (root, AUX)             UD:  njé (root, PRON)
         ├─subj──▶ Bés                   ├─nsubj──▶ Bés
         ├─comp:pred──▶ njé              ├─cop──▶ bo
         └─punct──▶ ?                    └─punct──▶ ?
```
- **SUD:** the copula **`bo` is the root**; *Bés* is `subj`, the predicate *njé* 'who' is `comp:pred`.
- **UD:** the nominal predicate *njé* is the root and *bo* is a `cop` dependent.
- Drawn from real running text — shows the analysis generalizes past elicited examples.

## 5. North Wind & the Sun clause — verbal complement + adjunct PP

```
haŋga    hí-ɓoroo      ɓaj    ni    ŋguy
9.sun    9.AGR-begin   shine  with  9.strength
'The sun began to shine with strength.'
```
```
        híɓoroo (root, '9.AGR-begin')   ← concord hí- bound onto the verb (NounClass=Bantu9)
        ├─subj──────▶ haŋga
        └─comp:obj──▶ ɓaj 'shine'
                        └─mod──▶ ni 'with'
                                   └─comp:obj──▶ ŋguy 'strength'
```
- *ɓoroo* 'begin' is a full inceptive verb (not in the SUD auxiliary list) → it stays the **head**;
  its verbal complement *ɓaj* 'shine' is `comp:obj` (SUD collapses UD's `xcomp`/`ccomp` into `comp:obj`).
- *ni ŋguy* 'with strength' is a manner **adjunct**: SUD makes the preposition **`ni` the head**
  (`ni → ŋguy` = `comp:obj`) and attaches it to *ɓaj* as `mod`. (UD: `case(ŋguy→ni)`, `obl(ɓaj→ŋguy)`.)

## 6–10. Audio-grounded verb paradigm ([`basaa_aligned.sud.conllu`](basaa_aligned.sud.conllu))

The 10 *maàŋgɛ́* 'child' sentences (each its own WAV) share one SUD frame and vary only the verb+tense:

```
maange         a-{m̀,ǹ,ŋ̀}-V       (OBJ)
└─subj─▶ V     root                └─comp:obj─▶ V
               (concord a- bound; NounClass on the verb)
```
e.g. **bas_s06** *maange aŋ́-kɛ̀ í ɓòm* 'the child is going to market':
```
   angke (root, 1.AGR-PRS-go)
   ├─subj──────▶ maange
   └─comp:obl──▶ i 'to'            (locative head; SUD: preposition heads its object)
                  └─comp:obj──▶ bom 'market'
```
These also expose the morphology (homorganic **nasal tense-prefix**, place-assimilating to the stem
onset). ⚠️ **Do not read tense off the nasal's tone.** An earlier draft claimed "tone = tense, H present
vs L past"; that is **not supported** — the past nasal's tone is copied from the subject marker via High
Tone Spreading, the present carries a nasal H + floating L (downstep), and syllabic nasals default to L
(three non-aligned source statements: `../rules/contradictions.md` FLAG-2). Tense is glossed from the
translation + verified melody, not the nasal tone (see `../rules/glossing.md` GL-4). Full analysis in
[`../glossary/morphology_child_paradigm.md`](../glossary/morphology_child_paradigm.md).

---

## Open annotation decisions (for the `bas` SUD companion guide)

1. **Preverbal subject concord (`a`, `hí`): RESOLVED — option (b).** When a lexical subject NP is
   present, the concord vowel doubles it. Options were: (a) separate `dep` token; (b) **verb morphology**
   (no token; feature `NounClass=` on the verb, concord written as the verb prefix `a-`/`hi-`); (c) `subj`
   with the lexical NP `dislocated`. **Adopted: (b)** — applied across all files (the spaced practical
   spelling is kept in `# text_practical`; in the audio file the verb's `AlignBegin` spans back over the
   concord's slice). §1–2 and §6–10 are now treated identically. See `../rules/parsing.md` PA-2.
2. **Connective CONN** — head-initial `mod` + `comp:obj` (chosen, §3). Confirm it scales to
   attributive adjectives and relatives.
3. **Phasal/inceptive verbs** (*ɓoroo* 'begin', §5) — full verb with `comp:obj` complement (chosen)
   vs. aux-like (`comp:aux`). They inflect for tense/concord like main verbs → keep as full verbs.
4. **Tense & tone.** TAM features come from the translation + verified melody, **not** from the nasal's
   tone (the nasal tone is not a reliable tense exponent — see FLAG-2 / GL-4). Toneless corpus tokens get
   **provisional** tense. Restore tone (Nikitin et al. 2022) before trusting TAM. See `../TREEBANK_PLAN.md` §3B.
5. **Focus / ex-situ fronting.** Not in these examples; Hamlaoui & Makasso (2015) argue apparent
   ex-situ focus keeps the subject as grammatical subject → a fronted constituent attaches high
   (`dislocated`) rather than `subj`. Get that PDF before annotating focus.

## Validation

Both `.sud.conllu` files are plain CoNLL-U. Validate with **Grew** (`grew`/Grew-match, the SUD
toolchain) and convert SUD↔UD with the published **grew grs** rule set; the UD file here is the target
of that conversion for sentences 1–5.
