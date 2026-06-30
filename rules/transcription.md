# Stage 1 — Transcription rules

Apply these when turning **audio or a raw spelling into the canonical Basaa string** that the rest of
the pipeline consumes. Get this layer right first: tone and segmentation here determine whether
glossing (Stage 2) and TAM analysis are even possible.

---

## TR-1 — Maintain a tone-marked canonical layer; keep the practical orthography separate
**Confidence: high · Source: Makasso & Lee 2015; Nikitin et al. 2022; Hamlaoui et al. 2018**

Tone in Basaa is **lexical and grammatical**, so the canonical treebank string must be **tone-marked**.
Keep two aligned layers per token:

- `form` — **tone-marked** canonical string (IPA-based, as in Makasso & Lee / Hyman).
- a practical/source layer in `MISC` (e.g. `Orig=`) for text that arrives toneless (Common Voice, GRN,
  missionary spellings).

Toneless corpus text must have tone **restored before TAM is trusted** — use the tone-prediction model
of Nikitin et al. 2022 (seq2seq missionary→official-orthography conversion), then verify by ear against
audio where available. ⚠️ **The choice of *which* canonical orthography is unsettled — see FLAG-1.**

---

## TR-2 — Mark all four tones + downstep; low is the only safely-omittable tone
**Confidence: high · Source: Makasso & Lee 2015 (Tone); Hamlaoui et al. 2018 §2; Nikitin et al. 2022 §1.1**

Inventory: **2 register tones** H, L; **2 contour tones** rising (LH), falling (HL); plus **downstep** (ꜜH).
That is the 5-way *surface* set (H, L, Rising, Falling, ꜜH) the BULBasaa team kept after cleanup.

| Tone | Diacritic | Example |
|---|---|---|
| High (H) | acute `´` | `jáχ` 'to annoy' |
| Low (L) | grave ``` `` (or **unmarked** in official orthography) | `jàχ` 'also' |
| Falling (HL) | circumflex `^` | `tûː` 'shoulder' |
| Rising (LH) | caron `ˇ` | `ɓǒː` 'nine' |
| Downstep | `ꜜ` / `!` before the H | `BíꜜGá` |

- In the **official (AGLC) orthography a Low tone is left unmarked**; H and contours carry diacritics
  (Nikitin et al. 2022). In the **IPA illustration both H and L are written** (acute / grave).
- **Tone is the tense exponent's only cue in minimal pairs** — keep it even when tedious (TR-7).

---

## TR-3 — Write the syllabic nasal place-assimilated to the following segment
**Confidence: high · Source: Makasso & Lee 2015 (Syllabic nasals); Hamlaoui et al. 2014 (7)**

Basaa has a **syllabic homorganic nasal** that surfaces both as a **noun class prefix** and as a
**verb tense morpheme**. Transcribe its place from the following onset:

| Following onset | Nasal | As class prefix | As tense prefix |
|---|---|---|---|
| bilabial p, ɓ | `m̀-` | `m̀-pek` 'CL3-bag' | `m̀-pɔ́rɔ́` 'speaks' |
| alveolar t, s | `ǹ-` | `ǹ-tombá` 'CL3-goat' | `ǹ-sɔ́mb` 'bought' |
| palato-alveolar ʧ, ʤ, ɲ | `ǹ-` → realised **`n`** | `ǹ-ʤɔ̀` 'CL1-fighter' | `ń-ʤɛ́` 'eats' |
| velar k, **and vowel-initial stems** | `ŋ̀-` | `ŋ̀-kɔ̀ŋ` 'CL3-land', `ŋ̀-anɛ̀` 'CL1-chief' | `ŋ́-kɛ̀` 'goes', `ŋ̀-áŋ` 'reads' |

- **A vowel-initial stem takes a velar nasal `ŋ̀-`** (Makasso & Lee 2015).
- ⚠️ **Do not encode tense in the nasal's tone at transcription time.** The nasal's *place* is robust;
  its *tone* is not a clean tense cue (FLAG-2). Record the heard tone descriptively (e.g.
  `MISC NasalTone=L(obs)`), not as an analysis.

---

## TR-4 — Vowel length is contrastive: always transcribe it
**Confidence: high · Source: Makasso & Lee 2015 (Vowels, Syllable structure)**

Each of the 7 vowels /i e ɛ u o ɔ a/ has a short/long contrast with **no quality difference**
(`sú` 'face' vs `sùː` 'to tease'; `sɛ́` 'to grind' vs `sɛ́ː` 'to collect palm wine'). Mark length with
`ː` (or vowel doubling, consistently). **Constraint to respect:** a long vowel **cannot** be followed by
a coda consonant in the same syllable (templates are `(C)V(C)` or `(C)Vː`).

---

## TR-5 — Normalise positional lenition (the "phantom consonants") for the lemma
**Confidence: high · Source: Makasso & Lee 2015 (Consonants); Nikitin et al. 2022 §1.1**

Voiceless stops /p t k/ occur **only word/stem-initially**; elsewhere the same underlying consonant
lenites by position:

| Underlying | Intervocalic (voiced) | Pre-pausal / pre-obstruent (voiceless) |
|---|---|---|
| /p/ | `B` (β) | `ɸ` |
| /t/ | `ɾ` | `ɾ̥` |
| /k/ | `ɣ` | `χ` |

Also: implosive **/ɓ/ → fricative `B` after a vowel**; /s/~/h/ in **free variation pre-pausally**
(`móm-óh`~`móm-ós` 'to console'). **Rule:** keep the **fortis/initial** consonant in the *lemma*; record
the surface allophone in `form`. This prevents the same root being mis-split into different lexemes.

---

## TR-6 — Undo applicative vowel-raising when lemmatising
**Confidence: high · Source: Makasso & Lee 2015 (Vowel raising)**

Adding a verbal extension (e.g. applicative) **raises the stem vowel one step**: a→e, ɛ→e, e→i,
ɔ→o, o→u (high vowels unchanged). E.g. `sal` 'work' → `sel-êl` 'work with'; `hol` 'sharpen' →
`hul-ûl` 'sharpen with'. **Rule:** the **lemma is the un-raised base verb**; gloss the raised vowel as
part of the derivation, not as a different root (link to GL-9 derivation glossing).

---

## TR-7 — Tense/aspect minimal pairs differ **only** in tone — never drop it
**Confidence: high · Source: Nikitin et al. 2022 §1.1**

A documented quadruplet on one segmental string:

```
M̀È nlÒ yani   'I'll come tomorrow'      (future)
M̀È ǹlÔ yani   'I came yesterday'        (past)
M̀È nlŌ yani   "I'm gonna throw up tomorrow"
M̀È ǹlO yani   'I threw up yesterday'
```

A treebank that strips tone here **cannot recover tense**. If a token's tone is unknown, mark its
`Tense=`/`Aspect=` as **provisional** in `MISC` (e.g. `TAMconf=low`) rather than guessing.

---

## TR-8 — Flag French borrowings explicitly
**Confidence: high · Source: Hamlaoui et al. 2018 §4.1**

The BULBasaa pre-processing **added a marker symbol to words written in French orthography**
(French borrowings were transcribed the French way). **Rule:** tag borrowings (`MISC Lang=fr` or a
`Foreign=Yes` feature) so they are not fed to a Basaa morphological segmenter and don't pollute the
lexicon. Note loanword `[dolá]` 'dollar' surfaces with a true /d/ (not the tap), unlike native roots.

---

## TR-9 — Present tense carries a floating L (downstep), not just a nasal
**Confidence: med · Source: Makasso & Lee 2015 (Tone)**

> "The present tense is marked with a nasal H and a floating L tone: the H tone in `ʤɛ́` 'eat' is
> downstepped in the present `[a ńꜜʤɛ́]` 'she eats'."

So **present = homorganic nasal (H) + a floating L that downsteps a following stem H.** When you hear a
downstep on the first stem mora after the subject+nasal, that is evidence for **present**, not past.
⚠️ This coexists in tension with two other statements by the same authors about nasal tone — **FLAG-2**.
Treat downstep as *supporting* evidence, confirmed by translation/audio, not as a standalone rule.
