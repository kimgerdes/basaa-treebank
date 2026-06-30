# Aligned Basaa sentences (sound + transcription)

**Yes — we have a sound file with transcribed, aligned sentences, and they are extracted here.**

Source: the supplementary **sound files of Makasso & Lee (2015), "Basaá", *JIPA* 45(1)** — recorded by
the author (E.-M. Makasso, your contact), licensed by the IPA/CUP for personal/research use,
downloaded from Cambridge's static CDN (`static.cambridge.org/…/Basaa.zip`). Full set is in
`../IPA_Makasso_Lee_2015/` (226 word clips + sentences + the connected passage).

## What's aligned here

| set | files | alignment | transcription |
|---|---|---|---|
| **10 single sentences** (`bas_s01`–`bas_s10`) | one WAV each, 1.2–2.4 s | **already sentence-level** (each clip *is* one sentence) | `manifest.tsv` (IPA + segmentation + gloss + EN/FR) |
| **North Wind & Sun** (`bas_NWS`) | one 52 s WAV | passage-level; 9 internal sentences not yet time-stamped | transcription in `../../treebank/` + `docs/basaa.pdf` |

`manifest.tsv` is the alignment table: `id · file · dur_s · basaa_ipa · segmentation · gloss · english · french`.

## Could we extract sound + transcription? — done, and how to go further

- **Done:** the 10 child-sentences are paired with their published transcriptions/glosses in
  `manifest.tsv`. This is a ready, if tiny, **speech+text+gloss** corpus.
- **The IPA is OCR-recovered** from the PDF (its tone diacritics scatter on extraction) — treat
  `basaa_ipa` as *to be verified against `docs/basaa.pdf`* and against the audio. Confirm with Makasso.
- **To segment the NWS passage** into its 9 sentences: run a forced aligner. With a known transcript,
  the practical options are **Montreal Forced Aligner** (needs a Basaa pronunciation dict — derivable
  from the 226 IPA word clips here) or a **CTC-segmentation / whisperX**-style aligner. Output →
  Praat `TextGrid` / ELAN `.eaf`. Then each NWS clause becomes an aligned unit like `bas_s01`–`s10`.
- **Build a pronunciation lexicon for free:** the 226 word clips in `../IPA_Makasso_Lee_2015/` are each
  a single word with its meaning in the filename and its IPA in `docs/basaa.pdf` → a seed grapheme→
  phoneme / word→IPA dictionary for the aligner and for the gloss lexicon.

## Then analyze morphologically?

Yes — see **`../../glossary/morphology_child_paradigm.md`**. The 10 sentences share one frame and vary
only the verb + tense, so they isolate Basaa verb morphology cleanly: class-1 subject concord *a*, a
**homorganic nasal tense-prefix** (place assimilates to the verb stem), and **grammatical tone on that
nasal** marking present (H) vs past/perfect (L).
