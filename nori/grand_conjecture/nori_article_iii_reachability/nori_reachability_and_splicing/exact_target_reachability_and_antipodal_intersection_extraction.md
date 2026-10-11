# Exact target reachability and antipodal intersection extraction

# Exact target reachability and antipodal intersection extraction

For a fixed root, monochromatic geodesic reachability records genuine terminal vertices together with the path support. Antipodal overlap of this color-free set has a direct gluing meaning in the classical edge setting, and analogous target-pair criteria exist for physical ordered faces only when sufficient terminal-memory data is kept.

## Antipodal reachable-target labels: exact support/face intersection formulation (edge analogue)

Fix an antipodally odd undirected binary edge coloring c of Q_n. For q in {0,1}, let R_q(x) be the set of physical cube vertices z connected to x by a monochromatic q-geodesic (including the empty path); let F_q(x)={S subseteq [n] : x XOR S in R_q(x)}.

**Theorem 1: exact target coincidence.** The following are equivalent:
(1) There exists a monochromatic antipodal geodesic.
(2) There exist x, q,r, and an actual cube vertex z in R_q(x) intersect R_r(bar x).
(3) There exist x,q,r and exact reachable direction supports S in F_q(x), T in F_r(bar x) satisfying T=[n]\S.
(4) For some x and q, R_q(x) contains an antipodal pair z,bar z.
(5) For some x and q, F_q(x) contains complementary subsets S,[n]\S.

Proof: For (2), concatenate the q-geodesic x->z with the reverse of the r-geodesic bar x->z. For each coordinate exactly one branch uses it, so the concatenation is a full antipodal geodesic with zero/one change. If r!=q, cyclically rotate the path at z by appending the antipodal image of its first monochromatic block after the second; oddness makes both resulting blocks color r, giving a monochromatic antipodal geodesic. The converse picks z=x on an existing monochromatic antipodal geodesic. (3) is the exact equation x XOR S=bar x XOR T. For (4), reverse a q-geodesic x->z and follow a q-geodesic x->bar z; their direction supports are complementary, producing a q-geodesic z->bar z. Conversely any monochromatic antipodal geodesic witnesses (4) at its starting root. (5) translates (4) into supports. Moreover F_q(bar x)=F_(1-q)(x), R_q(bar x)=overline{R_(1-q)(x)}.

**Theorem 2: honest convex target labels.** Let V=Q_n, and let Delta^V be the simplex with one affinely independent basis vertex e_z for each *actual physical target* z in V. Associate to a root/color pair its reachable-target FACE
P_q(x)=conv{e_z : z in R_q(x)}.
Then P_q(x) intersects P_r(bar x) if and only if R_q(x) intersects R_r(bar x): two faces of an ordinary simplex intersect in exactly the face on their shared vertex labels. In particular, a BU/KKM/Sperner mechanism forcing intersection of these actual target faces gives an immediate monochromatic antipodal geodesic.

**Why this does not yet prove closure.** The honest simplex has dimension 2^n-1, much larger than the dimension n-1 of the local antipodal link spheres. Replacing e_z by the physical cube vectors z in R^n destroys the exact intersection property: in Q_2, conv{00,11} and conv{01,10} meet at (1/2,1/2) although the underlying vertex sets are disjoint. Thus equality of low-dimensional barycentric averages / coordinatewise reachability is not enough. One needs a coloring-sensitive carrier, a restricted face-Helly property, or a topological index argument respecting the full combinatorial target support.

**Labeling research program (not a proved topological theorem).** Give a state with antipodal root label x an *actual realizable witness* (q,S), meaning a q-monochromatic geodesic from x to x XOR S. Under the antipodal root involution the companion root is bar x. A successful topological coincidence must force labels S and [n]\S, or equivalently the same actual target z, and it must ensure both certificates refer to the same antipodal root pair. Construct local transition/carrier rules respecting jointly realizable entire geodesics; prove a specific antipodal-label/coincidence theorem from them. Arbitrary selections including the always-reachable empty support S=empty can avoid the desired coincidence, so ordinary equivariance alone cannot force it. The required additional hypothesis must come from growth, maximality, or color-consistent repairs. For ordered-three-face NORI, retain the user's shared physical-target idea as the outer target while adding a separate two-window seam certificate before final extraction.



*The exact scoped proof is preserved in research note* note_terminal_basins_and_root_profile_nerve_extraction_limits.

## Near-complementary monochromatic branches: the one-coordinate completion law

Let \(Q_n\) have an antipodally odd binary UNDIRECTED edge coloring \(c(\bar e)=1-c(e)\). Let x be a root. Suppose two monochromatic geodesics \(P_S:x\to x\oplus S\) and \(P_T:x\to x\oplus T\) use DISJOINT coordinate supports, and
\[
S\cap T=\varnothing,\qquad S\cup T=[n]\setminus\{i\}.
\]
Thus the two paths form a geodesic from \(x\oplus S\) to \(x\oplus T\) of length n-1 through x, with a single missing direction i. Denote its two end-edges toward antipodal completion by
\[
e_S=\{x\oplus S,\overline{x\oplus T}\},\qquad
e_T=\{x\oplus T,\overline{x\oplus S}\}.
\]
They are antipodal edges and have complementary colors.

**Theorem (same-color case).** If \(P_S\) and \(P_T\) have the SAME monochromatic edge color q, then a monochromatic full antipodal geodesic exists. Precisely one of the two completion edges has color q. Appending that edge to its corresponding monochromatic branch from x reaches the antipode of the other branch's endpoint. Thus the uncolored region R(x) contains an antipodal pair and yields closure.

**Theorem (opposite-color case).** If the branch colors are q and \(1-q\), then the \((n-1)\)-geodesic through x has exactly one switch (assuming both paths have positive length). Its two full antipodal completions either BOTH have at most one switch or BOTH have two switches. The former occurs iff \(c(e_S)=q\), equivalently \(c(e_T)=1-q\). In the latter case \(c(e_S)=1-q\) and \(c(e_T)=q\). This isolates a SINGLE binary obstruction at the exposed coordinate i.

**Proof.** The disjointness of supports makes the two-arm concatenation a geodesic, and omission of only i makes both e_S and e_T legitimate geodesic endpoint extensions. The edges are antipodes because \(\overline{x\oplus S}=(x\oplus T)\oplus e_i\) and \(\overline{x\oplus T}=(x\oplus S)\oplus e_i\), so their colors are opposite. When branch colors match, precisely one edge extends the corresponding branch monochromatically; the new endpoint is antipodal to the other reachable branch endpoint. When colors differ, adding e_S before the q-block preserves one switch exactly when it has color q; adding e_T after the (1-q)-block preserves one switch exactly when it has color 1-q. The antipodal oddness makes these conditions equivalent. QED.

**Interpretation respecting COLOR-FREE R.** The main reachability set remains \(R(x)=R_0(x)\cup R_1(x)\), with no color specified in its topological labels. If two representatives of R(x) have disjoint supports covering n-1 coordinates, examining the EXISTENCE of same-color witnesses or the unique exposed bridge bit provides an exact extraction. Any reachability-label coincidence that forces same-color witnesses for such a near-partition immediately proves grand closure in the edge case. The full antipodal-support partition (covering n coordinates) already yields closure for arbitrary witness colors.

The distinction between a genuine reachable antipodal pair and an intersection of convex or simplicial relaxations is indispensable. Only the former supplies the compatible geodesic witnesses needed for extraction.
