# Upload the Basaa treebank to Arborator-Grew (with working audio)

Everything is prepared. Audio is hosted and CORS-enabled; the CoNLL-U files already carry
`# sound_url` + per-token `AlignBegin/AlignEnd`. Just create a project and import.

## Browse page

A landing page is live at **https://elizia.net/basaa/** — it lists every sentence with an in-browser
audio player (child sentences play the whole clip; NWS clauses play their span via media fragments) and
download links for all CoNLL-U files. Useful for sanity-checking the audio before importing.

## What to upload

| File | Sentences | Audio | Use |
|---|---|---|---|
| **`basaa_audio.arborator.conllu`** | 21 | ✅ playable | **main** — 10 isolated "child" sentences (clean) + 11 *North Wind & the Sun* clause units (draft) |
| `basaa_sample.sud.conllu` | 5 | — | literature examples (grandfather/children, connective NP, copula) — clean SUD, no audio |

Both are in this folder, and also hosted at:
- `https://elizia.net/basaa/basaa_audio.arborator.conllu`
- `https://elizia.net/basaa/basaa_aligned.arborator.sud.conllu` (child sentences only)
- `https://elizia.net/basaa/basaa_nws.arborator.sud.conllu` (NWS only)

## Steps

1. Go to **https://arborator.grew.fr** and sign in (GitHub/Google or local account).
2. **Create a new project** — e.g. name `Basaa_A43`. Set it to your preferred visibility. Choose the
   **SUD** annotation scheme (the trees use SUD relations: `subj`, `comp:obj`, `comp:obl`, `comp:pred`,
   `mod`, `dep`, `case`, `mark`, `cc`, `conj`, `det`).
3. **Import / Add data → upload CoNLL-U** and select `basaa_audio.arborator.conllu`
   (and optionally `basaa_sample.sud.conllu`). Keep the existing `sent_id`s.
4. Open a sentence. A **play button** appears (from `# sound_url`); each token is clickable to hear its
   slice (from `AlignBegin/AlignEnd`). Try `bas_s06` ("the child is going to market") — short and clean.

That's it — no audio configuration needed inside Arborator; it's all in the CoNLL-U.

## Why the audio works (already done for you)

- MP3s live at `https://elizia.net/basaa/bas_*.mp3` (nginx `location ^~ /basaa/` on the elizia.net
  vhost, `root /home/elizia/www`).
- That location sends **`Access-Control-Allow-Origin: *`** and supports HTTP **range requests**
  (`Accept-Ranges: bytes`), so the cross-origin player on arborator.grew.fr can fetch and seek.
- Each CoNLL-U sentence points at its MP3 with `# sound_url = https://elizia.net/basaa/<file>.mp3`.
  The 10 child sentences use one short file each (offsets start at 0). The 11 NWS units **share one
  52 s file** and index into it with absolute-ms `AlignBegin/AlignEnd` (Naija-NSC style).
- Verified: all 11 referenced URLs return HTTP 200 / `audio/mpeg`.

## Quality notes

- **Child sentences (bas_s01–s10):** transcription, gloss (Hamlaoui-style: `1.AGR`, `1-child`, `CONN`),
  SUD parse, and **word-level** forced alignment (torchaudio MMS) are all in good shape. Tones are
  provisional (verify by ear — now possible in-tool).
- **NWS units (bas_nws01–11):** **sentence-level timing is reliable** (boundaries match the speaker's
  pauses), so each clause plays correctly. The **Basaa word forms and the parse are DRAFT** — the PDF's
  IPA tier was mangled on extraction, so re-transcribe against the audio (ideally with Makasso) and fix
  the trees by dragging in Arborator. Gloss + French/English translations per unit are clean.

## To add more later

Re-run `align.py` (per-file sentences) or `align_nws.py` (one shared recording) to regenerate offsets,
then re-deploy MP3s with:
```
scp recordings/aligned/mp3/*.mp3 root@elizia.net:/home/elizia/www/basaa/
ssh root@elizia.net 'chown www-data:www-data /home/elizia/www/basaa/*'
```
