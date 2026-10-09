# A valid NORI coloring has a simultaneous antipodal-root permutohedral zero on a facet containing no jointly balanced actual path

# A simultaneous permutohedral Borsuk–Ulam zero with NO jointly balanced actual vertex in its own face

This is a sharp **physical ordered-face no-go** for a tempting but invalid extension of the scalar endpoint-zero face lemma to a pair of physical roots. It does NOT contradict the proved global same-order synchronization theorem for n≥10, which ensures a joint actual order somewhere else in the permutohedron.

Take any \(n\ge8\), choose an arbitrary physical cube root \(x\), and partition the direction set into disjoint sets \(S,T\) with \(|S|=4\), \(|T|=n-4\ge4\). Fix a total order of direction names. Define the following colors on actual ordered 3-faces THROUGH \(x\):
- For all triples \((a,b,c)\) with \(\{a,b,c\}\subseteq S\), prescribe
\[
h_x(a,b,c)=\mathbf1_{\{b\in S_1\}},
\tag{1}
\]
where \(S_1\subset S\) is any two-element subset. This is **reversal-even** within the first block: \(h_x(a,b,c)=h_x(c,b,a)\). Among all 24 ordered triples of distinct S-elements, exactly 12 have h-value0 and 12 have h-value1.
- For all triples with \(\{a,b,c\}\subseteq T\), prescribe
\[
h_x(a,b,c)=\mathbf1_{\{a<c\}},
\tag{2}
\]
which is **reversal-odd**: \(h_x(c,b,a)=1\oplus h_x(a,b,c)\), and precisely half of all ordered triples of T have value1.
- Assign arbitrary binary colors to every other ordered physical 3-face through \(x\), including all mixed-S/T free triples.
- For every ordered physical 3-face through the ANTIPODAL root \(\bar x\), assign the NORI-required bit \(c(\bar F,\operatorname{rev}\pi)=1\oplus c(F,\pi)\). For all remaining ordered-face involution orbits, choose arbitrary bits in antipodally complementary pairs.

This defines a COMPLETE valid active NORI coloring, because \(n\ge8\) ensures a three-face cannot contain both \(x\) and \(\bar x\); the sets of faces through them are distinct, and the paired-orbit prescription never conflicts.

Let \(H_S\) be the PROPER FACET of the standard permutohedron \(P_n\) whose permutation vertices \(\pi\) have precisely S as their first four direction supports (in any order), followed by the T directions (in any order). For any \(\pi\in H_S\) let
\[
u(\pi)=h_x(p_1,p_2,p_3)\in\{0,1\},\qquad
v(\pi)=h_x(p_{n-2},p_{n-1},p_n)\in\{0,1\}.
\]
By construction \(h_x(\operatorname{rev}(p_1,p_2,p_3))=u\), while \(h_x(\operatorname{rev}(p_{n-2},p_{n-1},p_n))=1-v\).

**Theorem (literal phantom simultaneous zero).** On EVERY actual full direction permutation \(\pi\in H_S\), the two physical-root integer endpoint-imbalance functions satisfy
\[
\boxed{
(q_x(\pi),q_{\bar x}(\pi))=(u+v-1,\ v-u)
\in\{(-1,0),(0,1),(0,-1),(1,0)\}.
}
\tag{3}
\]
In particular NO original permutation vertex of the ENTIRE face \(H_S\) has \(q_x=q_{\bar x}=0\).

Nevertheless, for the canonical ODD PL extensions \(F_x,F_{\bar x}\) formed by averaging endpoint imbalance over original vertices of each face and extending on the barycentric subdivision, one has
\[
\boxed{(F_x,F_{\bar x})(b_{H_S})=(0,0)}
\tag{4}
\]
at the actual barycenter \(b_{H_S}\) of this proper permutohedral facet.

**Proof.** The active NORI endpoint formula at the two antipodal roots is
\[
q_x=h_x(\text{first triple})-h_x(\operatorname{rev}(\text{last triple})),
\quad
q_{\bar x}=h_x(\text{last triple})-h_x(\operatorname{rev}(\text{first triple})).
\]
Insert (1)-(2) to obtain (3). No binary u,v solve both \(u+v-1=0\) and \(v-u=0\) (the second forces u=v, the first would then force 2u=1). Thus no actual joint balanced path lies in H_S.

The facet's original vertices are all independent orders of S followed by independent orders of T. The first triple of a uniformly random S-order has its MIDDLE direction uniformly distributed over the four S-directions, so \(E[u]=|S_1|/|S|=1/2\). The last triple of a uniformly random T-order is symmetric under reversing its first/third directions, and the rule (2) changes bit under that reversal, so \(E[v]=1/2\). Consequently \(E[q_x]=E[u]+E[v]-1=0\) and \(E[q_{\bar x}]=E[v]-E[u]=0\). The defined barycentric extension assigns the original-vertex mean at b_H, proving (4). \(\square\)

**Interpretation for the topology-first research program.** The scalar face lemma works because a 1-Lipschitz \(\{-1,0,1\}\)-valued function on a connected polytope graph cannot average to zero in a face unless that face contains a true zero vertex. For TWO such independent physical-root functions, the vector values can wind around the origin with no common zero vertex of the face—even when the roots are ANTIPODAL and the coloring obeys the FULL active ordered-face oddness law. The example realizes the four axial signs \(\pm e_1,\pm e_2\) on genuine complete geodesics, not fictitious combinatorial colors.

The previously proved multi-root Borsuk–Ulam theorem correctly extracts a possibly DIFFERENT endpoint-opposed path at each root from the same face; it cannot be upgraded to a SAME-PERMUTATION statement by applying the single-root scalar face lemma componentwise. The separate disjoint-triple reversal-signature theorem supplies real simultaneous permutations in n≥10, but uses additional combinatorial incidence across different faces. Any further high-index **joint real-path** carrier needs a new labeled-face degree or Sperner-type extraction lemma, not just vector averaging and the existing 1-Lipschitz scalar property.
