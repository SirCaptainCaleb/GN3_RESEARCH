# Tetrahedral parity blocks all monochromatic boundary Hamilton paths on four vertices

- Stable ID: note_tetrahedral_parity_boundary_no_spanning_tight_path
- Author: unspecified; session provenance retained
- Primary home: project:nori
- Labels: obstruction, conjecture-selection, proved
- Lifecycle: active
- Epistemic status: proved
- Current version: 3
- Retention: current and at most one previous snapshot
- Created session: session_nori_r0_3
- Updated session: session_nori_r0_3
- Disposition: none
- Successor: none

## Related references

- article:nori_article_vii_seven_coordinate
- note:note_boundary_tournament_edge_orderability_is_strict_fallback

## Research note

# Tetrahedral parity prevents a spanning monochromatic tight path

Let \(V=\{1,2,3,4\}\), with its displayed linear order. For every ordered triple of distinct vertices \(a,b,c\), let \(d\) be the unique element of \(V\setminus\{a,b,c\}\). Define
\[
h(a,b,c)=\operatorname{inv}(a,b,c,d)\pmod 2,
\]
where \(\operatorname{inv}\) is the inversion count relative to \(1<2<3<4\).

**Proposition.** The map \(h\) is an ordinary reversal-odd boundary \(3\)-tournament. Every vertex-simple tight Hamilton path on \(V\) has its two consecutive ordered-triple colors different. Its longest monochromatic vertex-simple tight path therefore uses precisely three vertices.

**Proof.** Reversing \(a,b,c\) interchanges the first and third positions in the associated four-permutation, reversing its parity. Thus
\[
h(c,b,a)=1-h(a,b,c).
\]
For any permutation \(p=(a,b,c,d)\) of \(V\), the two triple colors are
\[
h(a,b,c)=\operatorname{inv}(a,b,c,d)\pmod2,\qquad
h(b,c,d)=\operatorname{inv}(b,c,d,a)\pmod2.
\]
The second four-permutation is obtained from the first by a four-cycle, which has odd sign. Hence \(h(b,c,d)=1-h(a,b,c)\). Every three-element vertex set has a monochromatic tight path on three vertices (a single triple), proving the claimed maximum. \(\square\)

The construction belongs to the full ordinary boundary-tournament class. In fact the local comparison tournament at each fixed middle vertex is a directed triangle. For example at middle vertex \(1\), the comparisons among \(2,3,4\) form a directed \(3\)-cycle; consequently no single strict order on the edges of \(K_4\) represents these comparisons.

**Consequence for conjecture selection.** A conjecture demanding a monochromatic *spanning* tight path for every ordinary boundary tournament is already false at four original vertices, the smallest cardinality at which a two-window obstruction can arise. A common NORI1/boundary formalism must encode different guaranteed witness lengths through an intrinsic structural invariant or prove a boundary lower bound short of Hamiltonicity. Antipodal/reversal oddness of path-color signatures alone cannot imply a common spanning-color conclusion.

This is a small finite obstruction, not a refutation of a conjecture guaranteeing long nonspanning tight paths, and is recorded as a research note rather than as a manuscript theorem.
