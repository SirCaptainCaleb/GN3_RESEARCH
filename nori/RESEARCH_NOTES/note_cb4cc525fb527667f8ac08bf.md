# Two antipodally exchanged Euler tours with equal direction counts

- Stable ID: note_cb4cc525fb527667f8ac08bf
- Author: unspecified; session provenance retained
- Primary home: subsection:paired_direction_involutions_and_geodesic_endpoint_matchings
- Labels: eulerian, antipodal-involution, symmetry, direction-regular
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r10487_3
- Updated session: session_nori_r10487_3
- Disposition: none
- Successor: none

## Related references

- None

## Research note

## Antipodally paired Euler tours in balanced cubes

Let \(D\) be an Eulerian orientation of a connected graph \(G\), equipped with a fixed-point-free involution \(\tau\) on its geometric realization such that \(\tau\) takes every directed edge \(u\to v\) to a directed edge \(\tau v\to\tau u\). Assume \(\tau\) fixes no geometric edge or point.

**Theorem (two-tour decomposition).** The edge set of \(D\) admits a partition into two directed closed Euler trails \(T,\tau(T)^{\mathrm{rev}}\), each using every edge in its part once, exchanged by antipodal reversal. A \(\tau\)-equivariant local transition system cannot have a single Euler circuit, so two tours is best possible among symmetry-preserving Euler decompositions.

*Proof.* At each vertex \(v\), choose a bijection \(f_v\) from its incoming arcs to outgoing arcs. On one member of each vertex pair \(\{v,\tau v\}\) choose this bijection arbitrarily, and prescribe on the other vertex
\[
f_{\tau v}(\tau f_v(e))=\tau e
\]
for every incoming arc \(e\) of \(v\). This is consistent because \(\tau\) reverses arrow directions and \(v\ne\tau v\). The resulting local pairing decomposes the arcs into directed closed Euler trails, and \(\tau\) carries each trail, with its cyclic order reversed, onto another trail.

No trail is preserved by this involution. If a trail were preserved, the induced involution on its cyclic abstract edge-occurrence circle would reverse the cyclic orientation. Every orientation-reversing involution of a circle has a fixed point, which would correspond to a point of \(G\) fixed by \(\tau\) (at a vertex occurrence or inside an edge). This contradicts the assumption.

Thus the trails occur in disjoint antipodal pairs. If there are at least two such pairs, connectedness of \(G\) ensures some vertex \(v\) is incident with edges belonging to trails \(A,B\) from two different pairs: otherwise edge sets of distinct pairs would have disjoint vertex sets and disconnect \(G\). At \(v\), interchange the successors of an incoming arc from \(A\) and one from \(B\), merging these two directed trails into one. At \(\tau v\), make the conjugate successor interchange, merging their two antipodal mates. The two vertex locations differ, the four original trails are distinct, and the paired changes maintain the \(\tau\)-equivariance of the transition system. They replace two antipodal pairs of trails by one pair. Iterate until precisely one pair remains. Since every arc occurs in one trail, the two remaining trails partition \(E(D)\), and \(\tau\) exchanges them with reversal. \(\square\)

**Corollary (uniform direction counts in balanced NORI1 cubes).** Suppose \(N=2m\ge4\) and \(c\) is a perfectly balanced antipodally odd coloring of \(Q_N\). Orient red edges even-to-odd and blue edges odd-to-even. This is an Eulerian orientation on which \(\tau(x)=\bar x\) reverses every arrow. The theorem gives two antipodally paired directed Euler tours \(T,T^\tau\) with
\[
\boxed{|E(T)|=N2^{N-2},\quad
\#\{\text{direction }i\text{ edges in }T\}=2^{N-2}
\quad(i=1,\ldots,N).}
\]
Each tour alternates red and blue, and therefore contains \(N2^{N-3}\) edges of each color. The formulas also hold for its antipodal partner.

*Proof.* Antipodal reflection preserves edge direction classes and bijects the two tours. The full cube has \(2^{N-1}\) edges of each direction, so each tour contains half of that class. Directed edges alternate colors under the parity-defined orientation. \(\square\)

**Finite audit.** For a representative antipodally odd vertex-balanced coloring of \(Q_4\), all \(2^8\) involution-equivariant choices of local incoming-to-outgoing pairings at the eight antipodal vertex pairs were enumerated. A choice with precisely two directed tours was found. Their lengths were 16 and 16; each uses four edges in every direction, and the antipodal map exchanges the two tours. The theorem is combinatorial and does not depend on this finite check.

This is a symmetry-preserving half-Euler decomposition, not yet a NORI1 proof: its directed tours alternate colors, and the direction repetition within them is large. Any attempt to obtain a monochromatic full antipodal geodesic must extract an \(N\)-step zigzag using each direction once rather than merely a directed subtrail.
