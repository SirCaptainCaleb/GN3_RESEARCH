# Active NORI: first and last directions of every near-spanning monochromatic geodesic cross a canonical physical-face two-color cut

# Active NORI: every near-spanning monochromatic core crosses a canonical two-color direction cut

Let n>=5 and let c be any binary coloring of physical ordered three-faces satisfying the ACTIVE antipodal-reversal-odd NORI law. Fix a set U⊂[n] of size n-2 and its two missing directions {a,b}, with one fixed order (a,b). Fix ANY root x of Q_n and put y=x⊕U. These are antipodal endpoints INSIDE their physical U-facet.

For every i∈U define the **geometric cap label**
\[
A_i=A_i(x,U;a,b)=c\big(F(x;\{a,b,i\}),(a,b,i)\big)\in\mathbb F_2.
\]
This is an actual ordered-three-face color at the fixed root x, and is defined independently of any path. Construct an UNCOLORED graph H_{x,U} on vertex set U by joining i≠j whenever there exists a directed MONOCHROMATIC (n-2)-edge geodesic P from x to y with first(P)=i and last(P)=j; either monochromatic color is permitted and is NOT part of the graph label.

**THEOREM (canonical bipartite-cap obstruction; directly active NORI).** If the full one-switch antipodal NORI conjecture fails for c, then EVERY edge {i,j} of H_{x,U} satisfies
\[
\boxed{A_i\oplus A_j=1.}
\]
Therefore H_{x,U} is bipartite, with its two vertex classes given by the ACTUAL physical cap colors A_i. In particular, if for ANY x,U the uncolored graph H_{x,U} has an ODD cycle, or if any single monochromatic (n-2)-edge geodesic begins in direction i and ends in direction j with A_i=A_j, then c HAS a full antipodal geodesic with at most one ordered-three-face color change. The theorem holds for ALL n>=5, with no restriction on the internal coordinate order of P.

**Proof.** Suppose no full good NORI geodesic exists. Let P be any monochromatic U-spanning geodesic from x to y, let q be its common three-face window color, and put i=first(P), j=last(P). Append or prepend any ONE missing direction t∈{a,b} to P. If its new terminal three-face window had color q, the result would be a monochromatic length-(n-1) geodesic; inserting the final unused direction at the opposite end (or just appending at the same end) would produce a full n-edge antipodal geodesic with at most one new window color, contrary to the no-closure assumption. Thus every one-coordinate terminal extension window has color 1-q.

Now PREPEND the two missing directions in the order a,b to P. Its first three window colors are
\[
(c(F(x;\{a,b,i\}),(a,b,i)),\ 1-q,\ q).
\]
Any full path of this form has at most one change unless the first displayed color equals q: the middle two symbols are opposite, so to have at least two changes the first must be q. The no-closure assumption forces
\[
A_i=q. \tag{1}
\]

Likewise APPEND the two missing directions to P in order b,a. Its last three window colors are
\[
(q,\ 1-q,\ c(F(y;\{j,b,a\}),(j,b,a))).
\]
The no-closure assumption forces the final color to equal q. Because \bar x=y⊕e_a⊕e_b and both a,b are FREE directions of F(x;{a,b,j}), the face F(y;{a,b,j}) equals the antipodal physical face of F(x;{a,b,j}). The ordered triple (j,b,a) is the reversal of (a,b,j). Thus active NORI oddness gives
\[
q=c(F(y;\{a,b,j\}),(j,b,a))=1-A_j. \tag{2}
\]
Combining (1),(2), A_i=1-A_j. This holds for every witnessed edge of H_{x,U}, yielding the claimed proper two-coloring and all extraction corollaries. QED.

**Sharp root-mobile strengthening.** The same cap potential A_i is unchanged when the root x is replaced by x⊕e_i, since the physical face F(x;{a,b,i}) is free in i. Consequently a monochromatic U-spanning geodesic P rooted at x with first direction i and another such geodesic Q rooted at x or x⊕e_i with LAST direction i must have opposite colors under no closure, recovering and strengthening the earlier first–last pivot theorem. This lets one build a richer signed graph over root states and endpoint-memory coordinates.

**Relation to the color-free reversed-tail grand equivalence.** This theorem supplies a NEW same-facet, rank-(n-2) extraction mechanism that requires only the geometric FIRST and LAST direction of a monochromatic reachability witness, without recording its monochromatic color. Its graph H_{x,U} is a shadow of genuine terminal-memory reachability but has only n-2 direction labels. An ideal topological/Hartman/Kneser strategy would force a nonbipartite H_{x,U} (or incompatible root-mobile cap partitions) from the entire coupled family of actual reachability profiles.

**Exact open forcing obligation.** A valid NORI coloring need not furnish any monochromatic (n-2)-edge geodesic in a given facet/root chart; thus H_{x,U} may be empty or bipartite. The theorem proves the extraction conditional on the demonstrated uncolored memory obstruction, NOT the universal existence of such an obstruction.

## Four-facet transfer: one common cap potential for all parallel U-facets

Let U be fixed of size n-2, with missing directions a,b, and let r∈Q_U be any **projected starting root**. There are four U-parallel physical facets indexed by the exterior (a,b) bits t∈{0,1}²; let x_t be the unique cube vertex with U-coordinate vector r and exterior vector t, and y_t=x_t⊕U.

**THEOREM (simultaneous four-facet bipartiteness).** The canonical cap label
\[
A_i(r)=c(F(x_t;\{a,b,i\}),(a,b,i)),\quad i∈U,
\]
is INDEPENDENT of t. Let \(\mathcal H_U(r)\) be the undirected simple graph on U joining i≠j whenever, in ANY of the four U-parallel facets, there exists a monochromatic directed U-geodesic from x_t to y_t whose first and last directions are i,j in either order. The monochromatic color and exterior facet t are omitted from the graph labels. If active NORI grand closure FAILS, then every edge {i,j} of this UNION graph obeys
\[
A_i(r)\oplus A_j(r)=1.
\]
Thus \(\mathcal H_U(r)\) is bipartite. An ODD cycle assembled from monochromatic near-spanning geodesics in DIFFERENT parallel facets forces a full one-switch antipodal geodesic.

**Proof.** The physical three-face F(x_t;{a,b,i}) has exterior coordinates U\{i}, with fixed values inherited from r; varying t changes only free a,b bits and leaves this face literally unchanged. Hence A_i(r) is a common label across all four facets. Apply the canonical cap theorem to each actual U-spanning path in its own facet: its first/last directions lie in opposite common A-classes. Thus all edges of the union graph cross the SAME binary cut and the graph is bipartite in a hypothetical counterexample. Any odd cycle contradicts this property, proving closure. QED.

**Antipodal-reversal edge reversal.** If a monochromatic path from x_t starts in i and ends in j, then its global antipodal-reversal ΘP starts at \bar y_t=x_{t⊕(1,1)} (same projected U-root r), uses the reverse direction word, and is monochromatic of the complementary color. Thus every oriented first–last edge i→j present in exterior facet t has a conjugate edge j→i present in the opposite facet t⊕(1,1). The unoriented four-facet graph \(\mathcal H_U(r)\) automatically captures this conjugate pair. This is precisely the color-free, root-mobile/facet-coupled incidence pattern suggested by the Hartman connector analogy.

**Improved closure target.** Force nonbipartiteness of the UNION graph \(\mathcal H_U(r)\) for some U and projected root r, instead of demanding an odd cycle from one single prescribed endpoint pair and facet. Its edges are honest monochromatic \((n-2)\)-geodesic reachability witnesses, and its bipartition under no closure comes from actual physical ordered-face cap colors which do not depend on exterior facet bits.

## Extremal/Turán quantitative corollaries

Write m=|U|=n-2. In a hypothetical counterexample the four-facet union graph \(\mathcal H_U(r)\) lies inside the complete bipartite graph between the canonical direction classes \(U_0=\{i:A_i(r)=0\}\) and \(U_1=\{i:A_i(r)=1\}\). Hence
\[
|E(\mathcal H_U(r))|\le |U_0||U_1|\le\lfloor m^2/4\rfloor.
\]
Therefore, if for some U and projected root r the four-facet color-free reachability graph realizes MORE THAN \(\lfloor(n-2)^2/4\rfloor\) distinct unordered first/last coordinate pairs, grand closure follows. Likewise minimum graph degree \(>\lfloor m/2\rfloor\) forces closure.

**Path-density version.** Fix U,r and consider all 4m! directed U-spanning geodesics beginning at the projected root r, across the four exterior (a,b)-facet assignments. For each exterior choice and each ordered pair i≠j of first and last directions, there are exactly (m-2)! choices of the interior coordinate order. In a hypothetical counterexample, monochromatic geodesics only occur when A_i(r)≠A_j(r), giving at most
\[
4\cdot 2|U_0||U_1|(m-2)!
\le 8\lfloor m^2/4\rfloor(m-2)!
\]
monochromatic directed U-geodesics in that four-facet bundle. Thus their density is at most
\[
\boxed{\frac{2\lfloor (n-2)^2/4\rfloor}{(n-2)(n-3)}}.
\]
For even m this is \(m/[2(m-1)]\), and for odd m it is \((m+1)/(2m)\); both tend to 1/2. A universal lower bound exceeding this explicit ceiling for even ONE bundle (U,r) would close active NORI. The bound uses no color-indexed reachability labels: it counts paths meeting the canonical first–last cut.
