# A connected dense antipodal square complex has link independence two but vanishing second cover power

# Dense antipodal certified-square geometry does not by itself force Tucker index two

This is a **combinatorial topological no-go model**, not a claim that its precise square family is realized by some active NORI coloring. It tests whether the new certified hub-square theorem's *abstract* local bounds alone suffice to force a nonzero second equivariant index.

Let \(n\ge5\) and choose two distinct coordinate directions \(i,j\). Build a cubical two-dimensional complex \(Y_{i,j}\subset[0,1]^n\) containing **all** cube vertices and edges and **all** ordinary coordinate two-faces **except** those whose two free coordinate directions are exactly \(\{i,j\}\).

**Theorem.** The complex \(Y_{i,j}\) has the following properties.

1. Every vertex's link is \(K_n\) with just the single edge \(\{i,j\}\) deleted. Thus every link has independence number \(2\le4\), there are no isolated coordinate directions, and the center-move graph is the **entire connected cube** \(Q_n\), of degree \(n\) at every vertex.
2. The cube antipodal involution acts freely on \(|Y_{i,j}|\), and \(Y_{i,j}\) has all but the \(2^{n-2}\) squares of one direction-pair class. In particular, this example is far denser and more connected than the universal \(n-3\) minimum-degree and link-independence constraints of the proved certified center-square complex.
3. **Nevertheless there is an equivariant continuous map**
\[
Y_{i,j}\longrightarrow S^1
\]
with the antipodal action on \(S^1\). Hence its cohomological antipodal-cover class \(w\in H^1(Y_{i,j}/\tau;\mathbb F_2)\) satisfies \(w^2=0\). Any attempt to force a two-dimensional Tucker/Borsuk–Ulam obstruction *merely* from cube-wide degree, \(\alpha(\operatorname{link})\le4\), dense squares, connectedness, and free antipodality is invalid.

**Proof.** At each vertex, an incident square with two free directions \(a,b\) contributes an edge \(\{a,b\}\) to the vertex's coordinate link. Precisely the pair \(\{i,j\}\) is missing; all cube edges remain. This proves (1) and the square count in (2). No cubical face of dimension at most two contains the geometric center \((\frac12,\ldots,\frac12)\) when \(n\ge3\), so the antipodal action is free.

Let \(\mathrm{pr}_{i,j}:[0,1]^n\to[0,1]^2\) be the projection to the selected coordinates. On every cell of \(Y_{i,j}\), at least one of \(i,j\) is **fixed at 0 or 1**, because the cells with both free have been deleted. Therefore the restricted projection lands in the **boundary of the square** \(\partial[0,1]^2\cong S^1\). It is continuous and respects coordinatewise complementation: \(\mathrm{pr}_{i,j}(\bar t)=\overline{\mathrm{pr}_{i,j}(t)}\). The involution on the boundary square is a half-turn, conjugate to the antipodal action on \(S^1\). This is the asserted equivariant map.

The quotient double cover of \(Y_{i,j}\) is the pullback along the quotient map of the universal antipodal cover of \(S^1\), whose first Stiefel–Whitney class generates \(H^1(S^1/\tau;\mathbb F_2)\). Therefore \(w\) is pulled back from a 1-dimensional circle and \(w^2=0\). \(\square\)

**Interpretation and repair target.** The all-dimensional *actual* certified-square complex from Item \`nori_certified_center_square_complex_high_degree_eight_components_20261008\` may carry additional global incidence restrictions not shared by this artificial model. But a proof invoking only its unconditional *link density and 2-dimensional cell count* cannot force a nonzero \(w^2\). To apply fixed-point topology, establish extra constraints on how **actual monochromatic ordered-three-face path certificates** on neighboring squares glue; or construct a compatible higher-dimensional carrier using root/terminal-memory witnesses whose topology cannot be collapsed by such a two-coordinate projection. A topological zero must still extract the precise same-root reversed-two-tail complementary-support pair (or a four-facet odd cap-memory cycle).
