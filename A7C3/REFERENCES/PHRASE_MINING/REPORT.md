# A7C3 Phrase-Mining Report

Corpus documents: **1276**. Phrases are 2-6 token exact normalized n-grams.

The **raw ubiquity ranking** is sorted by number of distinct source files containing the phrase, then by total occurrences. The **promotion-candidate ranking** uses the same counts but suppresses near-duplicate subphrases and lightly rewards longer, strongly associated, phrase-complete expressions. Phrase completeness is estimated with left/right branching entropy. Frequency is a discovery signal, **not** evidence that a result is true, audited, reusable, or suitable for `SPARE_PARTS/`.

## Most ubiquitous phrases

| Rank | Phrase | Files | Uses | File % |
|---:|---|---:|---:|---:|
| 1 | `strong level-1` | 504 | 776 | 39.5% |
| 2 | `spanning two-cover` | 456 | 812 | 35.7% |
| 3 | `exact two-cover` | 448 | 1082 | 35.1% |
| 4 | `hypothetical smallest` | 388 | 541 | 30.4% |
| 5 | `tight path` | 380 | 745 | 29.8% |
| 6 | `hamilton path` | 326 | 829 | 25.5% |
| 7 | `smallest strong` | 320 | 454 | 25.1% |
| 8 | `smallest strong level-1` | 319 | 444 | 25.0% |
| 9 | `smallest strong level-1 counterexample` | 317 | 441 | 24.8% |
| 10 | `strong level-1 counterexample` | 317 | 441 | 24.8% |
| 11 | `level-1 counterexample` | 317 | 441 | 24.8% |
| 12 | `tight trimer` | 311 | 634 | 24.4% |
| 13 | `hypothetical smallest strong level-1` | 292 | 394 | 22.9% |
| 14 | `hypothetical smallest strong` | 292 | 394 | 22.9% |
| 15 | `hypothetical smallest strong level-1 counterexample` | 290 | 391 | 22.7% |
| 16 | `boundary antisymmetry` | 281 | 384 | 22.0% |
| 17 | `two-cover of h` | 247 | 352 | 19.4% |
| 18 | `h is a hypothetical` | 223 | 234 | 17.5% |
| 19 | `h is a hypothetical smallest` | 221 | 231 | 17.3% |
| 20 | `h is a hypothetical smallest strong` | 203 | 208 | 15.9% |
| 21 | `smallest counterexample` | 199 | 261 | 15.6% |
| 22 | `proper tight` | 187 | 351 | 14.7% |
| 23 | `tight hamilton` | 187 | 349 | 14.7% |
| 24 | `closes h` | 187 | 222 | 14.7% |
| 25 | `exact cover` | 185 | 297 | 14.5% |
| 26 | `boundary tournament` | 180 | 254 | 14.1% |
| 27 | `h be a hypothetical smallest` | 176 | 184 | 13.8% |
| 28 | `h be a hypothetical` | 176 | 184 | 13.8% |
| 29 | `spanning two-cover of h` | 174 | 221 | 13.6% |
| 30 | `literal exact` | 165 | 235 | 12.9% |
| 31 | `hamilton p4` | 157 | 383 | 12.3% |
| 32 | `literal tight` | 156 | 233 | 12.2% |
| 33 | `normal form` | 149 | 265 | 11.7% |
| 34 | `level-1 boundary` | 146 | 205 | 11.4% |
| 35 | `hamilton tight` | 144 | 201 | 11.3% |
| 36 | `strong level-1 boundary` | 142 | 199 | 11.1% |
| 37 | `tight paths` | 141 | 215 | 11.1% |
| 38 | `reverse trimer` | 138 | 264 | 10.8% |
| 39 | `hamilton p5` | 136 | 338 | 10.7% |
| 40 | `terminal dimer` | 136 | 258 | 10.7% |
| 41 | `h be a hypothetical smallest strong` | 134 | 140 | 10.5% |
| 42 | `literal hamilton` | 132 | 202 | 10.3% |
| 43 | `selected state` | 130 | 231 | 10.2% |
| 44 | `physical dimer` | 130 | 190 | 10.2% |
| 45 | `distinct vertices` | 128 | 160 | 10.0% |
| 46 | `level-1 boundary tournament` | 127 | 157 | 10.0% |
| 47 | `union v` | 126 | 236 | 9.9% |
| 48 | `strong level-1 boundary tournament` | 126 | 155 | 9.9% |
| 49 | `two-cover t` | 119 | 180 | 9.3% |
| 50 | `hypothetical smallest counterexample` | 119 | 141 | 9.3% |
| 51 | `balanced pair` | 118 | 226 | 9.2% |
| 52 | `two-cover h` | 118 | 192 | 9.2% |
| 53 | `physical endpoint` | 118 | 185 | 9.2% |
| 54 | `tight p4` | 116 | 211 | 9.1% |
| 55 | `tight cycle` | 116 | 207 | 9.1% |
| 56 | `actual hamilton` | 115 | 215 | 9.0% |
| 57 | `q m-1` | 113 | 315 | 8.9% |
| 58 | `vertex-simple tight` | 111 | 179 | 8.7% |
| 59 | `literal spanning` | 110 | 167 | 8.6% |
| 60 | `exact two-cover t` | 110 | 161 | 8.6% |
| 61 | `x union` | 108 | 246 | 8.5% |
| 62 | `hamilton order` | 108 | 177 | 8.5% |
| 63 | `path p` | 108 | 158 | 8.5% |
| 64 | `exact covers` | 107 | 162 | 8.4% |
| 65 | `retain the accepted` | 105 | 108 | 8.2% |
| 66 | `q m-2` | 104 | 346 | 8.2% |
| 67 | `tight p5` | 104 | 179 | 8.2% |
| 68 | `hamilton tight path` | 104 | 145 | 8.2% |
| 69 | `dimer d` | 103 | 175 | 8.1% |
| 70 | `accepted crossed` | 101 | 178 | 7.9% |
| 71 | `reverse terminal` | 99 | 171 | 7.8% |
| 72 | `literal exact two-cover` | 96 | 129 | 7.5% |
| 73 | `selected crossing` | 94 | 173 | 7.4% |
| 74 | `complete reversal` | 94 | 124 | 7.4% |
| 75 | `hamilton paths` | 93 | 152 | 7.3% |
| 76 | `cover t` | 92 | 141 | 7.2% |
| 77 | `gives an exact` | 92 | 123 | 7.2% |
| 78 | `smallest-counterexample minimality` | 92 | 102 | 7.2% |
| 79 | `disjoint union` | 91 | 132 | 7.1% |
| 80 | `tight turn` | 91 | 124 | 7.1% |
| 81 | `physical vertices` | 90 | 111 | 7.1% |
| 82 | `exact pair-deletion` | 89 | 141 | 7.0% |
| 83 | `balanced opposite-sign` | 89 | 137 | 7.0% |
| 84 | `opposite-sign pair` | 89 | 130 | 7.0% |
| 85 | `capture payment` | 89 | 106 | 7.0% |
| 86 | `independently accepted` | 84 | 149 | 6.6% |
| 87 | `physical vertex` | 84 | 126 | 6.6% |
| 88 | `exterior vertices` | 83 | 135 | 6.5% |
| 89 | `exact two-cover of h` | 83 | 112 | 6.5% |
| 90 | `sqcup q` | 82 | 242 | 6.4% |
| 91 | `union x` | 82 | 228 | 6.4% |
| 92 | `balanced opposite-sign pair` | 82 | 120 | 6.4% |
| 93 | `boundary dimer` | 81 | 183 | 6.3% |
| 94 | `literal three-cover` | 81 | 125 | 6.3% |
| 95 | `graph-intrinsic tight` | 80 | 93 | 6.3% |
| 96 | `tested dimer` | 79 | 152 | 6.2% |
| 97 | `exact singleton-deletion` | 79 | 112 | 6.2% |
| 98 | `spanning three-forest` | 78 | 113 | 6.1% |
| 99 | `selected edge` | 77 | 138 | 6.0% |
| 100 | `retained source` | 77 | 130 | 6.0% |

## Promotion-candidate highlights

The candidate score preserves the corpus counts but adds phrase association, left/right branching entropy, and subphrase suppression. Its strongest theorem-like signals included `boundary antisymmetry`, `tight trimer`, `reverse trimer`, `terminal dimer`, `selected state`, `balanced pair`, and `reverse ear`.

## First mathematical triage

| Mechanism | Files | Uses | Initial disposition |
|---|---:|---:|---|
| `boundary antisymmetry` | 281 | 384 | Foundational axiom R3. Canonical reference material, not a Spare Part theorem. |
| `tight trimer` | 311 | 634 | R8 is an immediate corollary of boundary antisymmetry and is explicitly superseded. Do not duplicate it. |
| `balanced pair` | 118 | 226 | Important output vocabulary. The reusable theorem-level compiler is R159/R176, not the bare phrase. |
| `reverse trimer` | 138 | 264 | Common local output. Usually part of a larger comparison theorem rather than a standalone promotion target. |
| `reverse ear` | 69 | 83 | General theorem R435. Already rescued as `S9001_REVERSE_EAR_LEMMA.md`. |
| `component drop` | 46 | 74 | Points to the general R159 punctured component-drop compiler, a strong Spare-Part candidate. |
| `normal form` | 149 | 265 | A naming pattern shared by many unrelated reductions, not one reusable theorem. |
| `terminal dimer` | 136 | 258 | Common geometric noun phrase. Needs theorem-level localization before promotion. |
| `selected state` | 130 | 231 | Ambient representation vocabulary, not by itself a theorem. |

The intended workflow is: **frequency discovers the pressure points; theorem archaeology identifies the actual reusable object; mathematical review decides promotion.** The complete objective common-to-least ranking is generated by the companion script as `phrase_ranking_compact.csv`.