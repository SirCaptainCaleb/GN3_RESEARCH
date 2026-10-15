# Antipodal prefix complements and dimension drop

Alexander duality of two opposed disjoint contractible red prefix cones in the cube boundary yields the mod-two homology of S^(n-2) for the antipodal complement. Under the absence of red-then-blue full geodesics at a root, the two cones are disjoint and both lie in the boundary. A PL regular neighborhood of the image cone in projective space is a ball, so the antipodal quotient of the complement has the homotopy type of RP^(n-2). The missing result is compatibility between these root-dependent complements along colored cube edges; no global chain map is established.

**Theorem (equivariant dimension-drop).** Let \(n\ge3\) and \(K_x\) be the red geodesic-prefix Freudenthal complex rooted at \(x\). If no full geodesic from \(x\) has a red run followed by a blue run, permitting empty runs, then
\[
Y_x=\partial[0,1]^n\setminus(K_x\cup A K_x)
\]
is equivariantly homotopy equivalent to the antipodal sphere \(S^{n-2}\). Consequently
\[
H^*(Y_x/A;\mathbb F_2)=\mathbb F_2[u]/(u^{n-1}),
\]
where \(u\) is the first Stiefel–Whitney class of the restricted antipodal cover.

*Proof.* The earlier gluing theorem makes \(K_x\) and its antipodal image disjoint. Every red prefix has length at most \(n-1\), since one of length \(n\) would be a red full antipodal geodesic. Each simplex of \(K_x\) therefore lies in a proper cubical face. Thus both complexes lie in \(\partial[0,1]^n\cong S^{n-1}\) and are simplicial cones, hence collapsible. Alexander duality applied to their disjoint union gives
\[
\widetilde H_i(Y_x;\mathbb F_2)
=\widetilde H^{n-2-i}(K_x\sqcup AK_x;\mathbb F_2),
\]
which is \(\mathbb F_2\) when \(i=n-2\) and zero otherwise.

For the equivariant assertion put \(m=n-1\). Quotienting the boundary sphere by antipodality yields \(\mathbb RP^m\), and the image \(C\) of \(K_x\) is a PL embedded collapsible cone, since \(K_x\cap AK_x=\varnothing\). A small regular neighborhood \(N\) of \(C\) in \(\mathbb RP^m\) is a PL \(m\)-ball. Its punctured neighborhood deformation retracts to \(\partial N\), so
\(Y_x/A=\mathbb RP^m\setminus C\simeq\mathbb RP^m\setminus\operatorname{int}N\simeq\mathbb RP^{m-1}\).
The restricted antipodal covering class maps to the nonzero \(H^1\) generator. The homotopy equivalence of quotients therefore lifts, by double-cover classification, to an equivariant homotopy equivalence \(Y_x\simeq_{\mathbb Z_2}S^{m-1}\). \(\square\)

**Unproved step.** The target \(Y_x\) changes with \(x\). Independent equivariant sphere models do not form a global chain map. A root-change construction must use the contractible common bridges of monochromatic prefix complexes and supply coherent higher-dimensional fillings.
