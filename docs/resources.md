Here is a breakdown of downloadable resources for Basaa (ISO 639-3: bas), categorized by your requirements. Because your ultimate goal is to build a Universal Dependencies (UD) treebank from interlinear glosses, this list prioritizes structured data and programmatic accessibility.

1. Sound & Transcription Data
Mozilla Common Voice (Basaa): The most accessible starting point. You can directly download an open-source archive of Basaa speech paired with aligned orthographic text transcriptions directly from the Mozilla Common Voice portal.

The BULBasaa Corpus: As discussed previously, this contains ~50 hours of audio and a 10-hour phonetically transcribed and orally translated subset. It must be requested for academic use via the ELRA (European Language Resources Association) data catalog.

2. Simple Text Data (Corpora)
OPUS Parallel Corpus (JW300): The open-source OPUS platform hosts the JW300 dataset, a massive parallel corpus mined from Jehovah's Witnesses publications. It contains thousands of aligned Basaa/French and Basaa/English sentences. This is highly valuable if you plan to use cross-lingual projection to map POS tags or dependency structures from French/English into Basaa.

The Crúbadán Project: A repository of web-crawled text for under-resourced languages. You can download the Basaa crawl—which primarily consists of word frequency lists and n-grams—as simple text and CSV files.

3. Dictionaries & Lexicons
PanLex: The PanLex project provides massive, downloadable datasets (in JSON or CSV format) of cross-lingual lexical translations, including thousands of entries for Basaa.

Dictionnaire Basaa-Francais (Lemb & de Gastines, 1973): This remains the foundational reference dictionary. While originally a physical text, digitized and structured wordlists derived from it circulate in various Bantu linguistic data archives.

4. Glossed Texts & Scientific Articles (For Treebanking)
Extracting Interlinear Glossed Text (IGT) directly from PDFs is notoriously difficult due to column and spacing alignment artifacts. To bootstrap a simple treebank, you will have much better luck targeting structured IGT databases:

TypeCraft Interlinear Glossed Text Repository: TypeCraft is a digital infrastructure built for under-resourced languages and specifically hosts annotated, glossed linguistic data for Basaa. Crucially, the platform allows you to export IGT via API in structured XML, making it significantly easier to convert into the CoNLL-U format required for UD.

ODIN (Online Database of Interlinear Text): ODIN programmatically crawls linguistic literature and extracts IGT. Searching ODIN for "Basaa" will yield a consolidated list of glossed sentences extracted from decades of African linguistics papers, alongside the citations of the original PDFs.

Specific Authors to Search: For PDFs containing high-quality manual glosses, look for typological syntax and phonology papers authored by Emmanuel-Moselly Makasso, Fatima Hamlaoui, and Larry Hyman.

Automated Glossing: If you find un-glossed Basaa parallel texts (such as the OPUS corpus) and want to generate glosses to accelerate your treebank construction, modern multi-source neural models can now automatically produce STEM and GRAM (grammatical) glosses for low-resource languages by leveraging their translations (Zhao et al., 2020).

References
Zhao, X., Ozaki, S., Anastasopoulos, A., Neubig, G., & Levin, L. (2020). Automatic Interlinear Glossing for Under-Resourced Languages Leveraging Translations. Proceedings of the 28th International Conference on Computational Linguistics, 5397–5408. https://doi.org/10.18653/v1/2020.coling-main.471
Cited by: 37 


Good leads. Fatima's Toronto faculty page has a full publication list. Let me fetch it for direct links and dates, then check the key glossed works and the Glottolog resource list.Fetched: https://www.french.utoronto.ca/people/directories/all-faculty/fatima-hamlaouiFetched: https://www.french.utoronto.ca/people/directories/all-faculty/fatima-hamlaouiThe page truncated the journal articles and proceedings sections. I have a good picture from the earlier search plus dblp/ACL. Let me confirm two things: the key glossed Basaa source articles (Hamlaoui & Makasso 2015 Lingua, and the Pronominal F-markers paper), and the open Glottolog resource inventory for Basaa to round out downloadable text/dictionary data.Searched the webSearched the webI found Hamlaoui's personal publications page (sites.google.com/site/fhaml044/publications) with direct PDF links, which is the key resource. I have enough now to assemble the list. Let me do one more check for the freely downloadable text/Bible and dictionary data, since those matter for your treebank.Searched the webSearched the webI have what I need. Here's the consolidated, download-oriented resource list for Basaa (A43, ISO bas, Glottolog basa1284), organized for your treebank goal. The single most important link is Hamlaoui's own publications page, which has direct PDFs of the glossed analyses you want to fit to.
Glossed scientific articles by Fatima Hamlaoui (your analysis target)
Her personal page has direct-download PDFs for most of these: https://sites.google.com/site/fhaml044/publications (and her Toronto page lists the rest). Makasso's page mirrors several: https://cne.cm/dr-makasso-emmanuel-m/
The core glossed works on Basaa syntax/information structure:

Hamlaoui & Makasso 2015, "Focus marking and the unavailability of inversion structures in the Bantu language Bàsàá (A43)," Lingua 154: 35–64. This is the central analysis — the morphology module named basaa in the BULB tooling explicitly "implements the morphology of Basaa (A43)... described in (Hamlaoui and Makasso, 2015)." PDF linked from both her page and Makasso's. Publisher (paywalled) version: sciencedirect.com/science/article/abs/pii/S0024384114002605
Pronominal F-markers in Basaá (Hamlaoui & Makasso) — heavily glossed, with an explicit gloss-abbreviation key (FUT2, GEN, INF, LOC, noun-class numerals, OBL, PASS, PRS…). Copy on ResearchGate: researchgate.net/publication/285875891
Makasso, Hamlaoui & Lee 2016, "Aspects of the intonational phonology of Bàsàá," in Intonation in African Tone Languages, de Gruyter, pp. 167–194. doi.org/10.1515/9783110503524-006
Hamlaoui & Makasso 2019, "Downstep and recursive phonological phrases in Bàsàa (Bantu A43)," ACAL 47 proceedings.
Makasso & Lee 2015, "Basaá," Journal of the IPA 45(1): 71–79 — the IPA illustration, with downloadable audio (word list + "North Wind and the Sun") plus transcription. Best small, clean sound+transcription pair.

Note on glosses for a treebank: published example glosses are Leipzig-style interlinear (three tiers — Basaa / morpheme gloss / translation). They're clean but not dependency-annotated, so you'd be converting IGT → dependency/constituency by hand against Hamlaoui's analysis. There's no existing Basaa treebank (no UD treebank for bas as of now), so you'd be building the first.
Sound data + transcription

BULBasaa corpus (Hamlaoui et al. 2018) — ~50h speech, ~10h phonetically transcribed, Basaa–French. Not a free open download; distributed via ELRA: catalog.elra.info (filter language = "Bantu languages"). Paper with full description (open): aclanthology.org/L18-1533 and hal.science/hal-04466108
"Bàsàa – oral spontané" (Makasso 2008), SLDR/ORTOLANG repository — spontaneous speech, OLAC id oai:sldr.org:sldr000737. Often openly accessible; this underlies his intonation work.
Interactions en basaa / Lexique en basaa (Bassong et al. 2025), CNRS Cocoon/ORTOLANG — newly deposited speech interactions plus a lexicon, via the "Structures formelles du langage" collection. Listed at language-archives.org/language/bas (Cocoon handles).
DoBeS / The Language Archive (MPI) — story-telling recordings (some catalogued under the neighboring Bakola/Bagyeli deposits). archive.mpi.nl
GRN / Faith Comes By Hearing / Jesus Film — spoken Basaa audio (religious), freely streamable/downloadable MP3: globalrecordings.net/en/language/bas. Useful as raw audio but glosses/transcriptions are limited.

Simple text data (good raw material for parsing)

Crúbadán data for Basaa (Kevin Scannell 2018) — web-crawled Basaa text corpus + word/character n-gram lists, downloadable: crubadan.org (id oai:crubadan.org:bas). This is your most directly usable plain-text corpus.
Basaa Bible / New Testament (Alliance Biblique du Cameroun; "Kaat nyambe…") — parallel-text potential against French/English. Via find.bible / Scripture Earth / the Rosetta Project (oai:rosettaproject.org:rosettaproject_bas_gen-1).

Dictionaries

Dictionnaire ɓàsàa-français-anglais-allemand (P. E. Njock, comp., 2019, SIL) — online and queryable on Webonary: webonary.org (id oai:webonary.org:33). Multilingual, the most usable digital dictionary.
Lemb & de Gastines 1973, Dictionnaire basaá-français, Collège Libermann — the standard reference, print (OLAC oai:gial.edu:24496); cited throughout the BULB work.
PHOIBLE phonemic inventory for Basaa: phoible.org (id basa1284) — downloadable phoneme data.

Aggregator pages (check these for anything new)

OLAC inventory (the master list, with live "ONLINE" flags): language-archives.org/language/bas and olac.ldc.upenn.edu/language/bas
Glottolog: glottolog.org/resource/languoid/id/basa1284 — full reference bibliography.

Practical path to your treebank
The realistic pipeline: harvest IGT examples from the Hamlaoui/Makasso PDFs (and the Hyman 2003 Bantu Languages chapter for baseline morphology), normalize them into a CoNLL-U-like format, and annotate dependencies to match Hamlaoui's syntactic claims (especially her "indirect role marking" / subject-as-grammatical-subject analysis of apparent ex-situ focus, which directly affects how you'd attach fronted constituents). For running text beyond elicited examples, the Crúbadán corpus and the Bible give you sentences to parse, and the Webonary dictionary gives lemmas/POS hooks. Contacting Hamlaoui directly is worth it — authors of under-resourced-language corpora often share glossed ELAN/FLEx files (the BULBasaa transcription layer) for academic treebank work, which would save enormous manual effort.