# Exact ordered-physical-window geodesic incidence test and unique-root full-endpoint residual permutohedron

# Exact physical compatibility of two ordered three-face windows

Work in \(Q_n=\{0,1\}^n\), \(n\ge5\), with ACTUAL ordered three-face windows \(u=(F,(a,b,c))\), \(v=(G,(d,e,f))\). For a physical coordinate three-face \(F\), write \(A=\mathrm{free}(F)\) and \(F_i\in\{0,1\}\) for every fixed exterior coordinate \(i\notin A\). Likewise \(B=\mathrm{free}(G)\), \(G_i\) for \(i\notin B\). Say \(u\prec v\) if they occur, in this order, as two distinct windows along ONE genuine direction-distinct cube geodesic, allowing any starting root and any additional moves before/after them. No coloring assumption is made.

**Theorem (complete necessary-and-sufficient two-window incidence test).** The relation \(u\prec v\) holds if and only if exactly one of the following conditions holds.

**Distance one:** the ordered free-direction triples have the literal de Bruijn overlap
\[
(d,e)=(b,c),\quad f\notin\{a,b,c\},
\]
and \(F_i=G_i\) on every coordinate \(i\notin A\cup B\).

**Distance two:** \(d=c\), the five coordinates \(a,b,c,e,f\) are pairwise distinct, and \(F_i=G_i\) for every \(i\notin A\cup B\).

**Distance at least three:** \(A\cap B=\varnothing\). In this case no further physical-face constraint is necessary. Define the **intermediate support**
\[
C(F,G)=\{i\notin A\cup B:F_i\ne G_i\}.
\]
Then necessarily the direction word from the first window to the last has precisely the set \(C(F,G)\) strictly between the two ordered free triples, in arbitrary order, and the window-index separation is
\[
k=3+|C(F,G)|.
\]

In all three cases the geometric \(\ell^1\) distance between physical face centers is EXACTLY the window-index separation:
\[
d_1(m(F),m(G))=k.
\]
Explicitly for arbitrary physical three-faces
\[
d_1(m(F),m(G))
=3-|A\cap B|+|\{i\notin A\cup B:F_i\ne G_i\}|.
\]
But the NUMERICAL metric equality alone is NOT a sufficiency test for a given pair: the free triple ordering and fixed exterior incidence above are essential.

**Proof of necessity.** Write the full direction word of a containing geodesic as \(p\) and let the window indices be \(i\) and \(i+k\). When \(k=1\), the ordered triples are \((p_i,p_{i+1},p_{i+2})\) and \((p_{i+1},p_{i+2},p_{i+3})\), giving the first overlap; when \(k=2\) they share exactly \(p_{i+2}\), in the specified last/first positions. No coordinate outside their union can have been traversed strictly between those two windows, so all common fixed exterior bits are identical. When \(k\ge3\), their ordered triples are disjoint. Every coordinate outside \(A\cup B\) with differing exterior fixed bit must have been flipped strictly between the two windows, and conversely a coordinate used there differs on the two faces. Precisely \(k-3\) moves lie between the two free triples; hence they are the set \(C(F,G)\). The formula for physical-center distance counts \(\frac12\) for each direction free in exactly one face (there are twice \(3-|A\cap B|\) of these), and 1 for each differing common fixed exterior coordinate.

**Proof of sufficiency (literal path construction).** In the distance-one case take the four-edge direction word \((a,b,c,f)\); in the distance-two case take \((a,b,c,e,f)\). For every coordinate in the first free triple but NOT the second, set its initial root bit to \(1-G_i\); for every coordinate in the second free triple but NOT the first, set its initial root bit to \(F_i\); for shared free coordinates assign arbitrary starting bits; for all common fixed exterior coordinates set the initial root bit to the shared value \(F_i=G_i\). This constructs a genuine directed geodesic whose first and later windows have EXACTLY the physical faces \(F,G\), in the requested ordered orientations.

For disjoint triples, use the direction word \((a,b,c,\text{any order of }C,d,e,f)\). Set initial root bits on \(A\) to \(1-G_i\), on \(B\) to \(F_i\), on \(C\) to \(F_i\), and on the remaining exterior coordinates \(E=[n]\setminus(A\cup B\cup C)\) to their common fixed value \(F_i=G_i\). The first window has the required exterior bits \(F_i\); after A and C are traversed the later B window has exactly \(G_i\). All prescribed physical faces therefore occur in the asserted order. If desired, append all unused E directions after the second window, giving a FULL antipodal geodesic containing both. Thus all conditions are sufficient. \(\square\)

**Corollary (complete full-endpoint fiber; UNIQUE physical starting root).** For \(n\ge6\), u and v can be the FIRST and LAST ordered three-face windows of a full n-edge geodesic if and only if
\[
A\cap B=\varnothing,\quad F_i\ne G_i\ \text{for EVERY }i\notin A\cup B.
\]
When this holds, the physical starting root \(x\) is UNIQUE:
\[
x_i=\begin{cases}
1-G_i,&i\in A,\\
F_i,&i\notin A,
\end{cases}
\]
where on \(i\notin A\) the value \(F_i\) is defined because the first window has these coordinates fixed. Its direction orders are EXACTLY
\[
(a,b,c,\ \text{any permutation of }[n]\setminus(A\cup B),\ d,e,f),
\]
a full residual middle permutohedral chamber of \((n-6)!\) actual geodesics (one for \(n=6\)). Every such geodesic has the exact same physical FIRST and LAST ordered windows.

**Proof.** Full endpoint windows are n−3 positions apart. A pair with overlapping triples has window separation 1 or 2, so cannot be full endpoints once n≥6 (when n=6 the first and last windows are at separation 3). In the disjoint case \(k=3+|C|\), so \(k=n-3\) requires \(|C|=n-6\), i.e. every common fixed exterior coordinate differs. The construction then has no unused E directions, and its root bits are forced as displayed. The middle coordinate order is arbitrary. \(\square\)

**Antipodal-pair metric counterexample.** For a physical window u and its physical antipodal reverse \(\tau u=(\bar F,\mathrm{rev}(a,b,c))\), the center distance is \(n-3\): every fixed exterior bit differs. Nevertheless u and \(\tau u\) CANNOT occur together on any direction-distinct path, since their free-coordinate sets coincide, whereas distinct windows of such a path always have different free-coordinate sets. Thus a raw metric-\((n-3)\) edge would be spurious: the good-window complex MUST carry actual ordered-direction and physical-face witness incidence.

**Research implication.** The compatibility test gives a COLOR-INDEPENDENT ambient directed window graph in which each admitted good-window edge is accompanied by a literal root and a precise middle support. Maximal-distance edges have particularly rigid unique-root, full-path residual permutohedral fibers. One may therefore formulate the missing high-index transfer problem as producing a good one-switch window path inside one such **real physical endpoint fiber**, rather than interpreting an interpolated fixed point as a false pair of endpoint windows.

## Elevation: full-endpoint fibers are antipodally paired, never individually invariant

Let \(\Theta\) be the active **physical antipodal path reversal**: reverse the sequence of vertices and complement each physical vertex. For every FULL antipodal geodesic it FIXES the initial root \(x\), reverses the entire direction order, and sends the first/last actual ordered-face windows
\[
(u,v)\longmapsto(\tau v,\tau u),
\quad \tau(F,\pi)=(\bar F,\operatorname{rev}\pi).
\]
The ordered middle direction word is reversed.

**Theorem (dual residual permutohedra and local index-zero obstruction).** For EVERY compatible full-endpoint pair \((u,v)\), its fiber \(\mathcal P_{u,v}\) of exactly \((n-6)!\) genuine full paths (with one fixed physical root and fixed first/last ordered triples) is exchanged by \(\Theta\) with a DISTINCT fiber
\[
\mathcal P_{\tau v,\tau u}.
\]
The two fibers are disjoint because the free direction set of \(\tau v\) is \(B\), disjoint from the free direction set \(A\) of \(u\); in particular \(u\ne\tau v\). Each fiber's middle-order adjacency complex is a copy of the \((n-7)\)-dimensional residual permutohedron (a point for n=6). The union of **one fiber and its antipodal mate** is therefore a disjoint involutively exchanged pair of contractible permutohedral chambers: its double cover over the orbit quotient is TRIVIAL and has cohomological antipodal index zero.

**Proof.** If \(P\) has first ordered window u and last v, the actual NORI oddness transformation under \(\Theta\) gives first ordered window \(\tau v\) and last \(\tau u\), and reverses the direction word. Because the original full word uses each direction once, the transformed path starts at the SAME root. The earlier full-endpoint uniqueness shows that each fiber has precisely all permutations of the middle coordinate set C of size n−6, giving the residual permutohedron. The free sets A,B of the two original terminal windows are disjoint, so u cannot equal \(\tau v\), and hence the two paired fibers are distinct. Reversal identifies their residual permutohedra; neither alone is invariant. A free involution on a DISJOINT union of two homeomorphic contractible chambers, exchanged by the involution, gives a trivial two-sheeted cover of their common quotient chamber. \(\square\)

**Research implication.** The Kneser antipodal-root synchronization theorem produces many genuine endpoint-opposed full-path FIBERS, but no isolated such fiber can carry the high-index antipodal class. Building the global fixed-point argument requires GLUING DIFFERENT endpoint fibers through ACTUAL shared-window/order/root incidence so that their separate dual-pair sheets form a nontrivial connected cover. This is the precise global topology which the good-window complex, as opposed to disconnected residual middle permutohedra, is designed to retain.
