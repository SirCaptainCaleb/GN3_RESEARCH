# Two-cover status words avoid three local patterns

**Summary:** A binary status word satisfies q≤p+1 iff it avoids 001, 011, and 0101.

## Statement

Let p be the first 0 and q the last 1 of a binary word. Then q≤p+1 iff the word contains none of 001, 011, 0101 as consecutive subwords.

## Body

Let (epsilon_1cdotsepsilon_m) be a binary word, with (p) the first zero and (q) the last one.

The condition
[
qle p+1
]
is equivalent to there being no zero followed by a one at distance at least two. If such a pair exists, choose one with minimum span.

If the span is (2), the resulting three-bit pattern is (001) or (011). If the span is at least (3), minimality forces all positions immediately after the first zero to be (1) and all positions immediately before the last one to be (0). Span at least (4) is impossible by overlap, so the only remaining case is span (3), giving (0101).

Conversely, each of (001,011,0101) visibly contains such a nonadjacent (0	o1) inversion. Therefore
[
qle p+1
iff
	ext{the word avoids }001, 011, 0101.
]

## Metadata

- ID: two_cover_words_avoid_three_local_patterns
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
