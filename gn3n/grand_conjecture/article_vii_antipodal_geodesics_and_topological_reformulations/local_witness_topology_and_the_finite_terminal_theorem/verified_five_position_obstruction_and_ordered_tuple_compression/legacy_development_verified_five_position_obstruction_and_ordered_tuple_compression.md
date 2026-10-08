# Verified five-position obstruction and ordered-tuple compression — preserved pre-item development

## Composition

(none yet)

## Development

## Two compression lemmas with explicit hypotheses

These lemmas repair two elementary steps without importing six-word protection. They do not certify the remaining positional reductions in [[explicit_proofs_for_finite_terminal_compression]].

**Lemma 1 (five-position obstruction).** Let five consecutive vertex positions be wholly contained in one ordered-partition block. If every chamber avoids \(001\) and \(011\) on the three consecutive status positions internal to those five positions, a contradiction follows.

**Proof.** Fix any five vertices of the block, keeping all other positions fixed. Every ordering \(a,b,c,d,e\) of those vertices is available. The forbidden patterns imply
\[
h(a,b,c)\ge h(c,d,e).
\]
Choose names \(0,1,2,3,4\) so that \(h(0,1,2)=0\), possible by boundary antisymmetry. Apply the inequality along
\[
012,\ 234,\ 401,\ 132,\ 240,\ 013,\ 342,\ 210.
\]
Each consecutive pair has the form \(abc,cde\) with five distinct vertices. Thus
\[
0=h(012)\ge h(234)\ge h(401)\ge h(132)
 \ge h(240)\ge h(013)\ge h(342)\ge h(210)=1,
\]
a contradiction. \(\square\)

Only the absence of the two indicated positive patterns at their actual starts is needed. The phrase “protected positions” may be used here only when the depth rule really excludes those starts throughout the face.

**Lemma 2 (ordered-tuple disjointness).** Let \(B\) have order \(N\), and let \(\alpha,\beta\ge1\). Form a bipartite graph whose vertices are ordered injective \(\alpha\)-tuples and ordered injective \(\beta\)-tuples from \(B\); two opposite-side tuples are adjacent when their supports are disjoint. If \(N\ge\alpha+\beta+1\), this graph is connected.

**Proof.** Two \(\alpha\)-tuples with the same support have a common neighboring \(\beta\)-tuple. If their supports differ by one element, their union has order \(\alpha+1\), leaving at least \(\beta\) elements for a common neighbor. Any two \(\alpha\)-subsets are connected by single-element replacements. Thus all left vertices lie in one connected component. Every right vertex has a neighbor, since \(N-\beta\ge\alpha\), proving connectivity. \(\square\)

**Corollary (exclusive indicators).** Suppose functions \(L,R\) on the two tuple sets take values in \(\{0,1\}\) and satisfy
\[
L(u)+R(v)=1
\]
on every compatible pair. If \(N\ge\alpha+\beta+1\), each function is constant. Hence if both reflected states occur, meaning \(L=1\) and \(R=1\) each occur somewhere in this fixed-context tuple model, then
\[
N\le\alpha+\beta.
\]
When the positions for the two tuples are disjoint and simultaneously occupied, \(N\ge\alpha+\beta\), so equality follows.

**Corollary (footprints of exclusive prescribed words).** Assume this equality, that the left and right tuple positions are consecutive portions of their respective determining windows, and that each indicator asserts a fixed forbidden word. If both states occur, then \(\alpha,\beta\le2\).

**Proof.** Choose a left tuple with \(L=1\), and let its support be \(A\). The complementary support \(B-A\) is the right support. Independent reordering of these two fixed supports is available. The exclusive-indicator identity implies that \(L\) is constant over all orders of \(A\), and its known value makes it identically one. If \(\alpha\ge3\), swap the first and third vertices in any three consecutive left tuple positions. This preserves the support and face but flips their triple status, contradicting the fixed word. Thus \(\alpha\le2\). Use an \(R=1\) tuple for the symmetric proof of \(\beta\le2\). Consequently \(N\le4\). \(\square\)

These are conditional mathematical statements with complete proofs. Applying them to a source face still requires proving: a unique common block; indicator dependence only on the displayed tuples after exterior orders are fixed; exclusive occupation on every compatible pair; and occurrence of both states in the same fixed-context model. Independence of exterior blocks can help prove those hypotheses but does not replace them.

In particular this \(N\le4\) conclusion applies to the exclusive disjoint-window model. It supplies no rank-three bound for centered or overlapping terminal faces, in agreement with [[correction_surviving_terminal_carriers_are_bounded_by_ten_not_rank_three]].
