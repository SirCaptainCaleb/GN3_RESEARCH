# Physical root-order prisms and balanced two-cap packets

# Physical root-order prisms and balanced two-cap packets

Adjacent transpositions of full coordinate orders and single-coordinate root slides form small permutohedral–cubical prisms. Their vertices are actual paths, and some crossing ordered faces remain literally identical across the prism. Combined with balanced two-cap selection, this yields opposite central colors on verifiable physical witnesses.

## A simultaneous permutohedral Borsuk–Ulam zero with NO jointly balanced actual vertex in its own face

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

NORI ROOT/ORDER SWAP PRISM (proved, all dimensions n>=5). Let p be a full distinct direction order, x a root, and k satisfy 2<=k<=n-2. Write t=p_(k-1), a=p_k, b=p_(k+1), d=p_(k+2). Let p' swap a,b. Before the swapped pair both words reach y=x XOR {p_1,...,p_(k-1)}. Their central ordered-three-face windows indexed k-1,k use the SAME TWO PHYSICAL 3-faces: F_minus=the {t,a,b}-face through y and F_plus=the {a,b,d}-face through y, intersecting in the PHYSICAL {a,b}-square through y. For p the two colors are [c(F_minus,(t,a,b)), c(F_plus,(a,b,d))]; for p' they are [c(F_minus,(t,b,a)), c(F_plus,(b,a,d))]. For each T subset {a,b}, translating the starting root x to x XOR T changes only FREE COORDINATE bits in both central faces, hence preserves both actual physical faces and the respective ordered central color pair. Therefore the eight real full geodesic states (root x XOR T, choice p or p') form a certified combinatorial 3-prism (two independent root axes plus one order-swap axis). Under active NORI reversal oddness, full-path antipodal reversal fixes each starting root, reverses p, and maps the central ordered color pair (u,v) to (1-v,1-u), at mirrored swap position n-k. All eight vertices are actual full paths, but only the TWO CENTRAL WINDOWS are certified constant on the root-square fibers. Other windows can change, and the prism need NOT be a cell in a monochromatic or one-switch path subcomplex. Proof: the two central face triples share middle free directions a,b; toggling their starting root bits changes no fixed exterior coordinate. Reversal and the color law give the displayed mirrored complement. This is a literal geometry-preserving building block for an equivariant root/order carrier; global compatible witness filling and grand extraction remain open.

THEOREM (TWO-COLOR CORRELATED POSITION FORCING, ODD n). Fix any odd n>=7, any active NORI coloring, any full path root x, a distinguished coordinate i and two others a,b. Let T=[n] minus {i,a,b}, k=|T|=n−3. The already-proved full permutohedral Borsuk–Ulam packet theorem nori_odd_full_permutohedron_two_cap_actual_opposite_central_face_colors_20261008 yields ACTUAL full x-rooted direction orders pi_r in ONE COMMON PROPER permutohedron face, with weights alpha_r>0 summing1. Let q_r be the GENUINE central ordered-3-face color of pi_r, and b_r in {0,1}^T its actual before-i order bits b_rj=1 iff j precedes i along pi_r. The packet satisfies P_alpha(q=0)=P_alpha(q=1)=1/2 and E_alpha[b_j]=1/2 for every j∈T.
Define the TWO COLOR-CONDITIONAL mean positions u=E[b|q=0] and v=E[b|q=1] in [0,1]^k. The exact balance identities imply
  u+v=mathbf1,
coordinatewise. Equivalently the convex hulls of the two genuinely witnessed coordinate-position sets have COMPLEMENTARY points u and 1−u, represented with the packet's actual conditional weights. This is a COLOR-RESOLVED strengthening of mere mixed-color/position neutrality, though it need not furnish one pair of exactly complementary {0,1}^k positions.
Let Pi_0 and Pi_1 be independent random ACTUAL packet paths sampled conditionally on central face colors q=0 and q=1, respectively. For coordinate j, the two before-i bits differ with probability
  u_j(1−v_j)+(1−u_j)v_j = u_j^2+(1−u_j)^2 = 1/2+2(u_j−1/2)^2.
Therefore
 E[d_H(b(Pi_0),b(Pi_1))] = k/2+2sum_(j∈T)(u_j−1/2)^2 >=k/2.
Hence there exist TWO ACTUAL full x-rooted endpoint-cap-coherent paths P0,P1 among the packet, with central physical ordered-three-face colors 0 and1 and their physical projected i-edge locations separated by at least CEIL((n−3)/2) Hamming coordinates in T. Their direction orders are in the SAME PROPER PERMUTOHEDRAL FACE, and the packet's common fixed prefix support is contained in {a,b} or has complement contained in {a,b}. The bound refines automatically when the color-conditional means are polarized, using the displayed correction term.
This gives a genuine opposite-color, macroscopic, same-root two-cap witness pair. It does NOT claim that their central physical faces overlap, that their two-direction tails are reversed, or that either full path has <=1 switch. In particular, the convex complementarity u+(1−u)=1 is NOT the exact bitwise complementarity required by the grand reversed-tail extraction theorem; achieving compatible paths rather than just complementary convex mixtures is the next missing step.

These configurations provide a concrete local substrate for a topological repair scheme. The unresolved step is to choose a sequence of prisms on which boundary-window defects decrease rather than move between incompatible facets.
