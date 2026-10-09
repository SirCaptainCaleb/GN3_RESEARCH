# Tucker-common-vertex root connector has two genuine hub windows; bichromatic selector makes splice defect additive

# A genuine two-seam splicing law at a common physical hub; locally rigid bichromatic hubs automatically repair both seams

Let n>=6, and let c be ANY binary coloring of physical ORDERED three-faces of Q_n. Let P and Q be two genuine full directed antipodal cube geodesics rooted at SAME physical vertex x, with direction words
\[
P=(a_1,\ldots,a_\ell,b_1,\ldots,b_{n-\ell}),\qquad
Q=(a'_1,\ldots,a'_\ell,b'_1,\ldots,b'_{n-\ell}),
\]
for some 3<=ell<=n-3, and suppose their first-ell used-direction sets coincide:
\[
\{a_1,\ldots,a_\ell\}=\{a'_1,\ldots,a'_\ell\}=S.
\]
Thus BOTH pass at time ell through the SAME physical cube vertex y=x⊕S. ALL FOUR paths obtained by choosing either prefix and either suffix are genuine full antipodal geodesics, because the first block uses S and second block uses its coordinate complement.

**THEOREM 1 (exact physical two-window splice).** Given any prefix A with last directions (u,v) and any suffix B with first directions (w,t), the ordered-three-face color word of their full splice A B is
\[
\boxed{\operatorname{Int}_3(A),\
c(F(y;\{u,v,w\}),(u,v,w)),\
c(F(y;\{v,w,t\}),(v,w,t)),\
\operatorname{Int}_3(B).}
\]
Here \operatorname{Int}_3(A) is the actual color word of the ell-2 ordered three-face windows entirely inside A, and \operatorname{Int}_3(B) is the actual color word of the n-ell-2 windows entirely inside B, preserving each branch's physical face identities. In particular BOTH NEW splice windows are actual ordered physical three-faces THROUGH THE SAME PHYSICAL INTERMEDIATE VERTEX y; they are not virtual/interpolated colors.

**Proof.** All windows wholly before/after the cut preserve precisely the same physical exterior bits, because both choices of prefix reach the same y. There are exactly two crossing windows of ordered directions (u,v,w) and (v,w,t). Their physical first vertices lie respectively at y⊕u⊕v and y⊕v, so each corresponding free-face contains y. This is the displayed formula. QED.

**THEOREM 2 (automatic seam compatibility at a locally rigid bichromatic hub).** Assume additionally that y is a bichromatic hub in the LOCAL UNIQUE-CERTIFIED-COLOR case of Item nori_every_bichromatic_hub_local_shared_edge_or_uniform_mixed_cap_dichotomy_20261008. Let A_y,B_y be its genuine certified incident direction color classes, with assigned bits h(i)∈{0,1}. Suppose the LAST prefix direction v belongs to A_y∪B_y, the FIRST suffix direction w belongs to A_y∪B_y, and their certified bits differ:
\[
h(v)\ne h(w).
\]
Then regardless of the neighboring directions u,t, the two actual crossing window colors are
\[
\boxed{c(F(y;\{u,v,w\}),(u,v,w))=h(v),\quad
c(F(y;\{v,w,t\}),(v,w,t))=h(w).}
\]
This follows DIRECTLY from the proved local mixed-middle selector at y: in each ordered triple, the MIDDLE direction has a neighboring free direction in the opposite certified color class.

**COROLLARY 3 (actual full one-switch extraction from compatible monochromatic branches).** Under Theorem2, suppose A is a genuinely MONOCHROMATIC ell-edge geodesic from x to y of ordered-window color h(v), and B is a genuinely MONOCHROMATIC (n−ell)-edge geodesic from y to bar x of ordered-window color h(w). Then their full concatenation P=A B is a full antipodal directed geodesic with ordered-face window-color word
\[
h(v)^{\ell-1}\ h(w)^{n-\ell-1},
\]
and hence has EXACTLY ONE change. It works regardless of the direction order in the rest of A or B.

**COROLLARY 4 (exact additive defect formula for nonmonochromatic branches).** Under Theorem2, suppose the LAST internal ordered window of A has color h(v), and the FIRST internal ordered window of B has color h(w), but their other windows may change. Let d_A,d_B be the number of changes in their respective internal window-color words. Then the full spliced word has
\[
\boxed{D(A B)=d_A+d_B+1.}
\]
Indeed the two new splice windows match their adjacent internal side colors and differ exactly once from one another. Thus local hub certification supplies a ZERO-EXCESS connector: there are NO uncontrolled seam changes. In particular, if d_A=d_B=0, grand closure is immediate.

**RELATION TO THE TOPOLOGICAL TUCKER PAIR.** Item nori_odd_dimension_permutohedral_tucker_common_vertex_opposite_mirror_switch_pair_20261008 proves unconditionally, in EVERY odd n>=7 and at EVERY root x, TWO actual endpoint-opposed full paths P,Q sharing some proper interior vertex y and carrying opposite mirrored switch labels. Theorem1 now turns this topologically forced common vertex into an ACTUAL two-seam geodesic rectangle, with both seam colors lying in physical faces through y. If y is a locally rigid bichromatic hub and the boundary directions of one of the four splice combinations cross the certified A_y/B_y cut with matching adjacent window colors, then Corollaries3-4 give exact switch-controlled extraction/defect bookkeeping. Such additional properties of y or the splice do not follow automatically from the Tucker pair theorem and remain the outstanding GLOBAL COMBINATORIAL task.

**Scope.** Theorem1 uses no NORI antipodal law; Theorem2 uses physical hub rigidity proved under ACTIVE NORI. The topological pairing and the one-switch extraction are both rigorous but their unconditional conjunction is NOT proved. No claim of unrestricted grand closure is made.
