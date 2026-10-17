# Crossing-flux identity and sharp linear holonomy curvature for paired-cover bigons

- Stable ID: note_a674bfdfdd23faeef04d3cb8
- Author: unspecified; session provenance retained
- Primary home: subsection:paired_direction_involutions_and_geodesic_endpoint_matchings
- Labels: NORI1, geodesic-bigon, holonomy, crossing-flux, dimension-uniform
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r10917_1
- Updated session: session_nori_r10917_1
- Disposition: none
- Successor: none

## Related references

- note:note_c944daa4c653527d2f6bf61e
- note:note_0cc55ed501605ffd6b5857ed
- subsection:paired_direction_involutions_and_geodesic_endpoint_matchings

## Research note

**Theorem (crossing-flux identity and sharp linear curvature necessity for geodesic bigons).** Let \(c\) be a legal antipodally odd binary edge coloring of \(Q_n\), with red swaps \(U_i\), and let \(W=W(\pi,A)=(\pi|_A)\pi(\pi|_{A^c})\) for an arbitrary subset \(A\). Write \(J(W)\) for the chord-interlacement graph. Between the two occurrences of each \(i\) in \(W\), the intervening word \(W_i\) consists of every neighbor \(j\in N_{J(W)}(i)\) once, and no other letters. For a trajectory of \(U_W\) from \(x\), let \(z_i\) be the state just after the first \(i\)-operation, and \(z_{ij}\) the state just before the intervening \(j\)-operation. With \(r_j=1-c_j\) and \(\partial_jc_i(v)=c_i(v)\oplus c_i(v\oplus e_j)\), the displacement of bit \(i\) obeys
\[
\boxed{[U_W(x)\oplus x]_i
=c_i(z_i)\oplus c_i(U_{W_i}(z_i))
=\bigoplus_{j\in N_{J(W)}(i)}r_j(z_{ij})\,\partial_j c_i(z_{ij}).}
\tag{1}
\]
Let the directed influence graph have arc \(j\to i\) when \(\partial_jc_i\not\equiv0\). Let \(a_c(W)\) be the number of such directed arcs crossing in \(J(W)\), and \(r_c(W)\) the number of noncommuting crossing swap pairs. Then
\[
\boxed{d_H(U_W(x),\bar x)\ge n-a_c(W)\ge n-2r_c(W).}
\tag{2}
\]
Indeed every displaced bit \(i\) has an incoming crossed directed-influence arc. Thus a successful bigon demands minimum indegree at least one in the crossed directed-influence graph, \(a_c(W)\ge n\), and
\[
\boxed{r_c(W)\ge\lceil n/2\rceil.}
\tag{3}
\]
This strengthens the source-SCC curvature lower bound for the geodesic-bigon family.

*Proof.* For \(i\in A\), the interval separating its occurrences contains each other \(A\)-letter once and each \(B\)-letter preceding \(i\) in \(\pi\) once. For \(i\in B\), it contains each other \(B\)-letter once and each \(A\)-letter following \(i\) once. These are the interlacement neighbors, with no repeated intervening directions. Both \(i\)-operations change only bit \(i\), and \(c_i\) is invariant under bit \(i\). Hence the parity of the two \(i\)-flips equals the change in \(c_i\) across the intervening trajectory. Telescoping this change across its distinct direction operations yields (1). If bit \(i\) changes, one summand of (1) is nonzero, furnishing a directed influence arc \(j\to i\) whose letters cross. Counting displaced bits against crossed arcs yields the first inequality in (2). The existing commutator-influence identity says a crossed pair carries at least one influence arc if and only if its swaps do not commute; each such pair carries at most two arcs. This proves (2) and (3).

*Sharpness.* Let \(n=2h\). For each \(0\le t<h\), set \(c_{2t}(x)=x_{2t+1}\) and \(c_{2t+1}(x)=x_{2t}\), independently of all other bits. Each two-bit factor admits a red antipodal geodesic from a root with mixed bits, and concatenating those geodesics gives a red full geodesic. The simple-bigon normal form supplies a word \(W(\pi,A)\) with antipodal return. The only noncommuting swap pairs are the \(h\) reciprocal-reader pairs, so the lower bound forces all \(h\) to cross and \(r_c(W)=h=n/2\).

*Scope.* The gap property (1) is specific to the bigon family. For arbitrary doubled words, a nested pair may lie twice between two occurrences of another label, transmitting curvature without an incident crossing. Thus (3) is a bigon-only statement. The curvature requirement is necessary and does not establish antipodal return.
