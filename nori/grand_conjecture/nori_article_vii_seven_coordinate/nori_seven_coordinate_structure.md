# Seven-coordinate endpoint constraints and tournament structure

# Seven-coordinate endpoint constraints and tournament orders

A directed geodesic with direction word \(p_1,\ldots,p_m\) produces a binary word \(w_1,\ldots,w_{m-2}\) of colors of its consecutive physical ordered three-faces. The dependence of \(w_i\) on the initial cube vertex is confined to the coordinates exterior to that face. We exploit this locality to separate endpoint choices from an invariant middle block.

**Lemma 1 (shared-pivot formula).** For a seven-move order \(p=(a,b,c,d,e,f,g)\), fixing all initial bits other than \(t=x_d\) makes its five colors have the form
\[
(A(t),M_1,M_2,M_3,E(t)).
\]
For the analogous six-move order, two independent root bits vary the two endpoint colors, giving \((A(u),M_1,M_2,E(v))\).

**Proof.** In the seven-move order the coordinate \(d\) belongs to each of the three interior free triples \(bcd,cde,def\), while it is exterior to the first \(abc\) and last \(efg\). Hence all three middle colors are independent of \(x_d\). In the six-move order, the intersections of free sets of interior windows contain the two central directions, whereas the first and last faces omit exactly one of those directions each. \(\square\)

If the fixed middle block \(M\) has \(q\) changes, a one-switch choice of root exists exactly when some pivot satisfies
\[
q+[A(t)\ne M_1]+[E(t)\ne M_{\rm last}]\le1.
\]
For an invariant middle block with \(q=0\), failure for both values of \(t\) forces both endpoints always to disagree with its common color. For \(q=1\) and endpoints that each toggle, existence is governed by whether their XOR matches the XOR of the middle endpoints. These are exact finite-memory conditions on the two physical end windows.

**Lemma 2 (independent seven-coordinate wings).** Fix the initial bits in directions \(a,b,d,f,g\) and vary \(u=x_e\), \(v=x_c\). Then
\[
(w_1,\ldots,w_5)=(A(u),B(u),M,D(v),E(v)).
\]
Writing \(\ell(u)=[A(u)\ne B(u)]+[B(u)\ne M]\) and \(r(v)=[M\ne D(v)]+[D(v)\ne E(v)]\), a successful root exists among the four choices exactly when
\[
\min_u\ell(u)+\min_v r(v)\le1.
\]
**Proof.** The direction \(e\) is exterior exactly to the first two ordered windows and free in the middle; the direction \(c\) is exterior exactly to the last two and free in the middle. Their effects on the left and right wing colors are independent. Every switch is internal to one wing, so the count is exactly \(\ell(u)+r(v)\), which minimizes separately. \(\square\)

An additional bit \(t=x_d\) affects only the first and last windows, refining the pattern to
\[
(P(u,t),L(u),M,R(v),S(v,t)).
\]
When \(L\) and \(R\) each toggle, choose their unique inputs \(u_*,v_*\) making the three central windows equal to \(M\). If either \(P(u_*,t)\) or \(S(v_*,t)\) can equal \(M\), the full path has at most one change. Thus failure at both values of \(t\) forces
\[
P(u_*,0)=P(u_*,1)=S(v_*,0)=S(v_*,1)=1-M.
\]
This rigid endpoint obstruction is local to the seven-direction order.

**Theorem 3 (tournament-factorized monochromatic subclass).** Let \(T\) be a tournament on the \(n\) directions, let \(t(a,c)=0\) if \(a\to c\) and \(1\) otherwise, and let \(s:V\to\mathbb F_2\) be constant outside one distinguished vertex \(v\). The position-independent ordered-face coloring
\[
c(F,(a,b,c'))=t(a,c')+s(b)
\]
is antipodal-reversal odd and admits a monochromatic full antipodal geodesic.

**Proof.** Reverse the free order: the tournament orientation bit changes by one, while the middle bit is unchanged. This is exactly NORI oddness. Every tournament admits a directed Hamilton path, obtained inductively by inserting a new vertex immediately before the first path vertex it dominates. Choose such a path through the distinguished direction \(v\), and extract from one side of \(v\) a directed subpath of length \(\lceil n/2\rceil\) (one side is long enough). Put its directions into every other position of the desired permutation, with \(v\) at the corresponding endpoint; put a directed Hamilton path on the remaining directions into the other parity positions. Thus \(p_i\to p_{i+2}\) for every \(i\) and \(v\) is an endpoint. Along this full order, every window has color \(s(p_{i+1})\), the same constant since no interior \(p_{i+1}\) equals \(v\). \(\square\)

The local pivot and wing theorems are exact necessary restrictions for bad seven-coordinate orders. The tournament theorem gives an independent all-dimensional positive subclass. Synchronizing the local restrictions between different orders and roots remains open for arbitrary NORI colorings.

## Seven-coordinate absorption as a compatibility problem

The factorization \(w=(P(u,t),L(u),M,R(v),S(v,t))\) exhibits three genuinely independent roles: a central physical window \(M\), the two separately adjustable wing bits \(u,v\), and a common endpoint pivot \(t\). When \(L\) and \(R\) are sensitive, choose \(u,v\) to force the central three-window block to be monochromatic. A bad order then requires *both* endpoints to remain opposite to \(M\) for every pivot value, producing the rigid bit pattern from the wing subsection.

The one-flipper and flat-bridge lemmas handle special ways to carry this block into larger cubes. They are not a general seven-dimensional closure theorem, since the exterior-bit colors on the two newly formed seam windows can still obstruct extension. The separate tournament-factorization construction is all-dimensional, but assumes its explicit coordinate-only outer-tournament plus middle-bit representation.
