# Transcription & gloss review — can we do better, and is it like Fatima's papers?

Review of the 10 *maàŋgɛ́* sentences (`../recordings/aligned/`, `../treebank/basaa_aligned.sud.conllu`)
against (a) the source PDF `../docs/basaa.pdf` and (b) Hamlaoui & Makasso's own glossing conventions
in `../docs/Hamlaoui_Makasso_2014_HighTone_PhonPhrases_Basaa.pdf`. Includes corrections I'm applying.

## TL;DR

- **Transcription can be improved** (segmentation + tone), and we now have the **aligned audio** to
  verify it by ear, token by token, in Arborator.
- **The glosses were close but not in Fatima's house style.** I'm applying three fixes: `1.SBJ → 1.AGR`,
  `CL1.child → 1-child` (recognising the class-1 *m-* prefix), and a correction to the tense/tone claim.
- **One analysis to revisit:** the *i* in "going to market" is probably the noun's **augment**, not a
  preposition.
- **Good news:** my SUD treatment of the connective (head-initial) **matches Hamlaoui & Makasso's own
  constituency** (their ex. 10), so the syntax layer is on solid ground.

---

## 1. Can we improve the transcription?

### Segmentation — yes, and it's now audio-verifiable
The forced alignment (`forced_align_offsets.tsv`) gives per-word time spans. Two payoffs:
- Each token is now **clickable audio** in Arborator → tones and vowel length can be checked against
  the speaker directly (the best possible source: Makasso himself).
- The proclitic **concord *a*** aligns to a ~20 ms slice fused to the verb onset (e.g. bas_s06
  `a[686–707]` immediately before `ngke[787–989]`) — acoustic confirmation that *a* is a clitic, not a
  prosodically independent word (bears on the tokenisation decision below).

### Tone — partially; flag the rest
The PDF's IPA tier scatters its tone diacritics on text extraction, so the tone marks in `manifest.tsv`
are **OCR-recovered and provisional**. Best-effort reconstruction of the frame (verify against audio):

| id | reconstructed IPA | nasal (place ← stem) |
|---|---|---|
| s01 | m-aːŋgɛ́ á **m̀-**pɔ́rɔ́ ɓasǎː | bilabial ← p |
| s03 | m-aːŋgɛ́ á **ǹ-**sɔ́mb ma-kálà | alveolar ← s |
| s04 | m-aːŋgɛ́ á **ń-**ʤɛ́ ma-kálà | palato-alv. (→n) ← ʤ |
| s06 | m-aːŋgɛ́ á **ŋ́-**kɛ̀ í-ɓòm | velar ← k |
| s10 | m-aːŋgɛ́ á **ŋ̀-**áŋ kâːr | velar ← vowel-initial |

The **place** of the nasal is robust (it assimilates to the stem onset — see §2). The **tone** of the
nasal is where I over-reached; see §4.

## 2. Morphological decomposition (improved)

Three segmentable pieces per finite verb word, plus a decomposable subject noun:

```
m-aːŋgɛ́     á          {m̀,ǹ,ŋ̀}-STEM
m-          a          N-           V
CL1-        1.AGR      TAM(homorganic nasal)  verb
'child'     subj.concord
```

- **`m-aːŋgɛ́` = `m-` (class-1 prefix) + `aːŋgɛ́` 'child'.** Confirmed by Hamlaoui & Makasso (2014) ex.
  (11): they write *m-ààngɛ́* glossed **`1-child`**. So 'child' is *not* unanalysable — I now gloss it
  `1-child`, matching them. (The same *m-* class-1 nasal prefix appears on *ǹ-sàŋ* `CL1-father`.)
- **`á` = class-1 subject concord.** Same morpheme that appears verb-bound as *à-* in their *à-ǹ-tÉhÉ*
  `1.AGR-PST-see`. Here it's written as a separate word — the tokenisation question stands (`../treebank/
  syntactic_analysis.md` open decision #1), but its **gloss should be `1.AGR`**, their label, not `1.SBJ`.
- **Homorganic nasal TAM prefix**, place-assimilating to the stem onset: bilabial *m̀-* /p,ɓ/, alveolar
  *ǹ-* /s,t/, palato-alveolar *ń-* (realised *n*) /ʧ,ʤ,ɲ/, velar *ŋ̀-* /k, V-initial/. This is the same
  syllabic nasal that is a class prefix on nouns — disambiguated by host POS.

## 3. Are the glosses like Fatima's? — comparison

From Hamlaoui & Makasso (2014), their conventions are:

| device | their gloss | mine (before) | fix |
|---|---|---|---|
| class prefix on noun | `2-children`, `1-child`, `8-boxes` | `CL1.child` | → `1-child` ✅ |
| subject concord | `1.AGR` (in *à-ǹ-tÉhÉ* `1.AGR-PST-see`) | `1.SBJ` | → `1.AGR` ✅ |
| connective | `8.CONN`, `9.CONN` | `8.CONN` | already matches ✅ |
| augment | `AUG` (ex. 16 *í ndáp* `AUG 9.house`) | (not used) | adopt as a label when needed (not for s06 — see §5) |
| demonstrative | `9-DEM` | — | adopt when needed |
| possessive | `8-POSS` | — | adopt when needed |
| tense | `PST` (+ `PRS`, `FUT2`… in the F-markers key) | `PRS`/`PST` | keep, but see §4 |

So: same Leipzig framework, same class-number style, same `CONN`/`AGR`/`PST` labels. The two
mismatches (`1.SBJ`→`1.AGR`, `CL1.child`→`1-child`) are now fixed in the conllu. Her full abbreviation
inventory (FUT2, GEN, INF, LOC, OBL, PASS, PRS, class numerals) is the key to adopt verbatim — it's in
the "Pronominal F-markers" paper (still to obtain; `../docs/SOURCES.md`).

**Syntax bonus:** my SUD connective analysis (connective = head of NP2, the whole modifying NP1) is
*exactly* Hamlaoui & Makasso (2014) ex. (10): `[ConnP [NP Bì-kwémbé] [Conn Bí [NP á-ÓÓNgÉ]]]`
'the children's boxes'. The head-initial SUD tree mirrors their ConnP constituency — reassuring.

## 4. Correction: tense is **not** simply "tone of the nasal"

My earlier note (`morphology_child_paradigm.md`) claimed *H-nasal = present, L-nasal = past*. That
over-reads the source. The illustration explicitly states: **"syllabic nasals are assigned an L tone."**
The section is about **syllable structure** (the nasal is syllabic), not a tense paradigm. What is
robust: (i) present vs. perfect *meaning* (from the English translations), and (ii) the homorganic
nasal prefix. **How** tense is exponed (nasal tone? stem melody? a floating tone?) is **not**
establishable from this source and must be checked against Hyman (2003) / the BULB `basaa` morphology
module / Fatima. The conllu keeps `Tense=Pres|Past` (justified by translation) but the per-token
`Tone=` field is now labelled an **observation**, not the tense exponent.

## 5. One tree considered: *i* in "going to market" — kept as locative

s06 *…ŋ́-kɛ̀ **í** ɓòm* could analyse *i* either as a locative **preposition** heading *bom*, or as the
noun's **augment** (cf. Hamlaoui & Makasso 2014 ex. 16 *í ndáp* `AUG 9.house`). **Decision: keep the
locative-head analysis** (`i` = `ADP`, `comp:obl` of the verb, heading *bom*); the augment reading is
recorded but set aside pending audio verification with Makasso. Tracked as `../rules/contradictions.md`
FLAG-3.

## Applied changes
- `basaa_aligned.sud.conllu` (+ Arborator twin): concord folded into the verb as a bound prefix
  (`á-`), `NounClass=Bantu1` on the verb, tokens renumbered, verb `AlignBegin` extended over the
  concord slice; glosses `1-child`, `1.AGR-…`; verb tone kept as `NasalTone=…(obs)`; s06 *i* kept as
  `LOC` (§5). Spaced spelling preserved in `# text_practical`.
- `morphology_child_paradigm.md`: tone/tense table corrected; interlinear updated to bound concord.
- `syntactic_analysis.md` §6–10: "tone = tense" claim removed; open decision #1 resolved (bound concord).
- Arborator file regenerated; redeploy to `https://elizia.net/basaa/` when convenient.
