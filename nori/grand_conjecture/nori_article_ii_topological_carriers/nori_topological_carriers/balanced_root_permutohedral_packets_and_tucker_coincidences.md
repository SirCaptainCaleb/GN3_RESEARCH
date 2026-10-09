# Balanced-root permutohedral packets and Tucker coincidences

# Balanced-root permutohedral packets and Tucker coincidences

At a given root, reversing a full direction order is central antipodality of the permutohedron. Actual first/last color functions and position coordinates become odd labels, so the full sphere forces balanced packets of genuine geodesics. Tucker coincidences locate two path witnesses within this parameter space, but the witnesses may still have different physical middle windows.

## A canonical HIGH-INDEX permutohedral sphere for EVERY physical root: topological endpoint-opposition forcing in NORI

Fix n>=7 and a binary active NORI coloring of ordered physical 3-faces satisfying
  c(bar F,rev(i,j,k)) = 1-c(F,(i,j,k)).
Fix ANY cube root x∈Q_n. Every full n-edge cube geodesic from x is specified by a coordinate permutation pi=(p1,...,pn). Its L=n−2 consecutive actual ordered-three-face window colors are
  w_j(x,pi)∈{0,1}, j=1,...,L.
Let alpha(pi)=w_1(x,pi), beta(pi)=w_L(x,pi), and define the integral ENDPOINT IMBALANCE
  q_x(pi)=alpha(pi)+beta(pi)−1 ∈ {−1,0,+1}.
Thus q=0 iff the FIRST and LAST physical ordered-three-face colors are OPPOSITE.

**THEOREM 1 (literal NORI antipodality on the permutohedron).** Let P_n be the STANDARD (n−1)-dimensional permutohedron in the affine hyperplane sum_i t_i=n(n+1)/2, whose vertex indexed by pi has coordinates
  v_pi(i)=position of direction i in pi.
Its center is o=((n+1)/2,...,(n+1)/2), and reversing a permutation gives
  v_(rev pi)=2o−v_pi.
Therefore ∂P_n is an (n−2)-sphere with a FREE CENTRAL-ANTIPODAL action pi↦rev pi on its vertices.

For a FULL antipodal geodesic from root x, physical complement followed by path reversal has starting root
  bar(x xor [n])=x.
Its direction order is rev pi, and by ACTIVE NORI oddness the COMPLETE color word becomes complemented-reversed:
  w_j(x,rev pi)=1−w_(L+1−j)(x,pi).
Consequently
  q_x(rev pi)=−q_x(pi).
This uses actual physical ordered faces and does not assume a fictitious complement action on direction supports.

**THEOREM 2 (discrete endpoint-balance lemma: every root has a REAL opposite-end path).** For n>=7, an edge of the 1-skeleton of P_n corresponds to swapping two ADJACENT POSITIONS in the direction permutation. Such a swap changes AT MOST ONE of alpha(pi),beta(pi):
- the first physical three-face depends on the first three ordered directions (and on root x);
- the last physical three-face depends on the final three ordered directions and the SET of previously flipped directions;
- when n>=7 these first and last three-position blocks have at least one position separating them, and swapping adjacent entries cannot alter both physical faces simultaneously.
Hence for adjacent permutohedron vertices,
  |q_x(pi)−q_x(pi')|<=1.
The graph of P_n is connected. Starting at any pi with q≠0 and following an adjacent-transposition path to rev pi, whose q-value is −q, the integer-valued 1-Lipschitz q must pass through zero at some VERTEX. If q(pi)=0 already, stop. Therefore for EVERY starting root x there exists an ACTUAL full antipodal cube geodesic with opposite first and last ordered-three-face window colors.

Under hypothetical grand failure, every such actual endpoint-opposed full geodesic necessarily has at least THREE window-color changes, because its number of changes is ODD and at most one is prohibited. This provides a physically witnessed, antipodally invariant 'middle defect' on every root's full permutation space.

**THEOREM 3 (canonical HIGH INDEX endpoint-opposition zero carrier).** Define an odd piecewise-linear function F_x:∂P_n→R as follows. Use the barycentric subdivision of the proper nonempty face poset of P_n. At the barycenter b_H of a face H, set F_x(b_H) to the arithmetic MEAN of q_x(pi) over all ORIGINAL permutation vertices v_pi of H, and extend affinely over each barycentric simplex. Central inversion sends H→−H and q→−q, so
  F_x(−z)=−F_x(z).
At the original vertices F_x(v_pi)=q_x(pi).

Let Z_x=F_x^{-1}(0), the literal PL ZERO SET. It is closed, antipodally invariant, and admits a finite antipodally symmetric triangulation as a subpolyhedron. Let w be the first Stiefel–Whitney class of its free antipodal quotient double cover. Then
  w^(n−3) !=0 in H^(n−3)(Z_x/(±1);F2).
Equivalently, the cohomological Z2 index of the endpoint-opposition carrier Z_x is AT LEAST n−3, one dimension below the full permutohedron boundary's index n−2.

**Proof of index bound (relative cup-product form of Borsuk–Ulam).** More generally let S^d carry the antipodal action and let F:S^d→R be any continuous ODD map with zero locus Z. Suppose w^(d−1) vanished on Z/(±1). For our PL Z choose a sufficiently small invariant regular neighborhood U retracting equivariantly onto Z; then w^(d−1) vanishes on U/(±1). Choose a smaller invariant neighborhood U0 whose closure lies in U, and set B=S^d\U0, a closed invariant complement avoiding zeros. On B the SIGN of F defines an equivariant map to S^0, hence the double cover over B is trivial and w|B=0. In the quotient X=RP^d, the vanishing classes lift to relative classes in
  H^(d−1)(X,U/(±1)) and H^1(X,B/(±1)).
Their relative cup product represents w^d in H^d(X,(U∪B)/(±1))=H^d(X,X)=0. But w^d is the NONZERO top generator of H^d(RP^d;F2), contradiction. Therefore w^(d−1)|Z is nonzero. Apply d=n−2. QED.

**COROLLARY 4 (an EXACT topological grand-closure target).** Since ind(Z_x)>=n−3, there is NO antipodally equivariant continuous map Z_x→S^(n−4). Thus a TOPLOGICAL proof of GRAND NORI closure would follow if, under the hypothetical assumption that EVERY full geodesic has at least two changes, one constructs an honest antipodally equivariant LOW-SPHERE MAP
  Phi_x:Z_x→S^(n−4)
from the ordered-face change pattern, with all cellwise extensions justified by physical face/coordinate-swap combinatorics. Such a map would contradict Theorem3.

Concretely, at ACTUAL endpoint-opposed permutation vertices q_x(pi)=0, the color-change vector
  s_j(pi)=w_j(x,pi) xor w_(j+1)(x,pi), j=1,...,n−3,
has ODD Hamming weight, and in a hypothetical counterexample at least THREE 1s. Physical reversal sends this change vector to its position reversal, while keeping the root x fixed. The missing extraction step is to turn this equivariant MULTI-SWITCH LABELING into a continuous sphere map on ALL of Z_x (or a combinatorial Tucker complementary-edge certificate whose physical local repair yields a good path). Merely assigning switch labels at permutation vertices does NOT automatically define such a map on higher-dimensional faces; proving the extension is the essential combinatorial obligation INSIDE the high-index topological frame.

**CRITICAL COMPARISON WITH THE OLD PATH-HISTORY INDEX-ONE BARRIER.** The earlier NORI history-poset carrier has small Z2 index because its legal-prefix topology collapses. P_n is a DIFFERENT, canonically supplied, centrally symmetric convex polytopal COMPLETION of the set of all FULL direction orders, with index n−2 on its boundary. Its higher faces encode permutations and their swaps, NOT automatically compatible monochromatic paths. Theorem2 gives a literal actual geodesic at the FIRST zero-level because endpoint imbalance is 1-Lipschitz under legitimate adjacent swaps. Higher-dimensional Tucker extraction STILL requires additional physical-cell compatibility rather than treating arbitrary PL barycenters as real geodesics. This is the sharp, topology-first direction for global closure.

**Status.** Theorem1–3 and the conditional obstruction in Corollary4 are proved. Constructing the sphere map Phi_x or a valid combinatorial carrier extraction remains open; unrestricted grand NORI closure has NOT been obtained.

## Quantitative actual-path separator: at least n−1 endpoint-opposed full permutations per root

**THEOREM 5.** For every n>=7 and EVERY fixed physical cube root x, at least n−1 DISTINCT full antipodal ordered-direction geodesics rooted at x have opposite initial and final ordered-three-face window colors.

**Proof.** Let V_+, V_0, V_- partition the vertex set of the standard (n−1)-dimensional permutohedron P_n according to q_x(pi)=+1,0,−1. Reversal of direction order interchanges V_+ and V_- and preserves V_0. If V_+ is empty, then V_- is also empty, so ALL n! permutation vertices are in V_0 and the assertion is immediate. Otherwise both V_+ and V_- are nonempty. The proved 1-Lipschitz adjacent-swap property of q says there is NO permutohedron GRAPH EDGE directly between V_+ and V_-. Thus deleting V_0 disconnects the 1-skeleton of P_n into at least the two nonempty groups V_+, V_-. Balinski's elementary d-vertex-connectivity theorem for convex d-polytopes says the graph of P_n has vertex connectivity at least d=n−1. Hence |V_0|>=n−1. Every vertex in V_0 is one genuine full rooted cube geodesic with physically opposite endpoint colors. QED.

**Topology inside combinatorics.** The count is a direct finite shadow of the high-index endpoint-zero hypersurface: the genuine zero-LABELED vertices, not merely virtual PL zeros, form an antipodally invariant vertex separator in an (n−1)-connected polytopal graph. This strengthens the nonempty actual balanced-path theorem and quantifies a minimum amount of certified endpoint diversity at EACH root.

This theorem uses the classical convex-polytope graph connectivity result. It does not assert that any of these >=n−1 paths has only one change; under hypothetical grand failure each has at least THREE, an odd number. For a universal grand proof the endpoint-balanced high-index hypersurface must additionally force a defect-removal transition among its actual adjacent-swap witnesses.


## A genuine Tucker connector: odd-dimensional NORI forces two endpoint-opposed full geodesics to meet and have opposite mirror-switch asymmetry

Let n>=7 be ODD, and let c be ANY active NORI coloring of PHYSICAL ORDERED three-faces satisfying c(bar F,rev pi)=1−c(F,pi). Fix ANY physical cube root x. For each full n-direction permutation p, let w(x,p)=(w_1,...,w_{n-2}) be the ACTUAL ordered-face color word and let D=n−3 be its number of switch positions. Because n is odd, D is EVEN. Let
\[
s_j(p)=w_j\oplus w_{j+1},\quad j=1,...,D.
\]
Call p ENDPOINT-OPPOSED if \(w_1\ne w_{n-2}\), equivalently its switch word has ODD Hamming weight.

For each endpoint-opposed p, define its CANONICAL MIRROR-SWITCH SIGNED LABEL:
\[
j(p)=\min\{1\le j\le D/2:s_j(p)\ne s_{D+1-j}(p)\},
\]
\[
\lambda(p)=
\begin{cases}
+j(p),&s_{j(p)}(p)=1,\\
-j(p),&s_{j(p)}(p)=0.
\end{cases}
\]
The label is well-defined: if all D/2 mirror pairs had matching bits, the total switch count would be EVEN, contradicting endpoint opposition. Under the actual full-geodesic NORI antipodal-reversal operation p→rev p at THE SAME root x, the entire window word transforms as \(w(rev p)=1-\operatorname{rev}w(p)\); hence the switch vector transforms as \(s(rev p)=\operatorname{rev}s(p)\), and
\[
\lambda(\operatorname{rev}p)=-\lambda(p).
\]
This is a genuine \(\mathbb Z_2\)-odd vertex labeling on all ACTUAL endpoint-opposed geodesics, with only k=D/2=(n−3)/2 coordinate labels.

**THEOREM (physical root-compatible mirror-switch Tucker pair).** For EVERY odd n>=7 and EVERY root x, there exist TWO ACTUAL full antipodal directed geodesics \(P=(x,p)\) and \(Q=(x,q)\), both endpoint-opposed, such that:
1. Their signed mirror-switch labels are COMPLEMENTARY, \(\lambda(p)=+j\), \(\lambda(q)=-j\), for some \(1\le j\le(n−3)/2\). Thus
\[
s_j(p)=1,\quad s_{n-2-j}(p)=0,\qquad
s_j(q)=0,\quad s_{n-2-j}(q)=1,
\]
where the reflected position is D+1−j=n−2−j.
2. Their direction permutations share SOME proper nonempty INITIAL COORDINATE SUPPORT:
\[
\{p_1,...,p_\ell\}=\{q_1,...,q_\ell\}
\quad\text{for some }1\le\ell\le n−1.
\]
In particular P and Q pass through the SAME genuine physical cube vertex \(y=x\oplus\{p_1,...,p_\ell\}\) at time \ell, as well as their common antipodal endpoints x and bar x.
3. The permutations q and rev p are necessarily DIFFERENT: the pair is not merely the tautological antipodal-reversed copy of one geodesic.

**PROOF.** Let P_n be the standard centered (n−1)-dimensional permutohedron whose original vertices are full direction orders, with antipodal involution p→rev p. Its boundary is a free-antipodal sphere S^(n−2). Use the genuine integer-valued endpoint imbalance \(f(v_p)=w_1(x,p)+w_{n−2}(x,p)-1\in\{-1,0,+1\}\). The NORI antipodal-reversal law makes f ODD; it is 1-Lipschitz on ACTUAL adjacent-transposition edges of the permutohedron, since swapping adjacent positions changes at most one of the first and final ordered three-face colors when n>=7. Let F be the equivariant barycentric piecewise-linear extension averaging f over original vertices of each face and interpolating over flags of faces, and put Z=F^(-1)(0).

The previously proved endpoint-zero index theorem, Item nori_permutohedral_antipodal_sphere_endpoint_color_balance_high_index_20261008, gives
\[
w_1(Z/\tau)^{n−3}\ne0,
\]
so no equivariant continuous map Z→S^(k−1) exists for k=(n−3)/2.

We now construct a GENUINELY CARRIED simplicial labeling of Z. Every point z∈Z lies in a unique relative interior of a PROPER permutohedron face H(z). This face H(z) has an ACTUAL endpoint-opposed original permutation vertex. Indeed, if H(z) had no f=0 original vertex, its connected original 1-skeleton (true for any convex-polytope face) together with the 1-Lipschitz property of f would force f to be CONSTANT +1 or CONSTANT −1 on all vertices of H(z). The barycentric extension F would then be identically that sign on H(z), contradicting F(z)=0.

Choose a finite centrally equivariant triangulation of the PL zero complex Z that refines the barycentric triangulation of ∂P_n. For each triangulation vertex z, choose an actual f=0 permutation p_z contained in the minimal P_n-face H(z). Choose the permutations in antipodal pairs so \(p_{\tau z}=\operatorname{rev}p_z\); this is consistent because proper permutohedron faces come in DISJOINT antipodal pairs, and the involution is free. Assign the signed label \lambda(p_z)∈{±1,...,±k} to z. The labels are genuinely antipodally ODD.

Suppose for contradiction that NO edge of this zero-set triangulation has opposite labels +j and -j. Then every simplex's vertex-label set contains no complementary pair (every pair of simplex vertices is an edge). Map each labeled vertex +j to the standard basis vector e_j∈R^k and -j to -e_j; interpolate linearly on simplices. Since a simplex contains no complementary pair, its positive barycentric combinations of signed basis vectors CANNOT vanish: for each coordinate index the appearing signs are either all + or all −, and at least one nonzero coordinate appears. Normalize to obtain a continuous τ-equivariant map Z→S^(k−1), contradicting the high antipodal index of Z. Therefore some genuine ZERO-SET SIMPLEX EDGE zz' has complementary labels ±j.

Because the triangulation refines the barycentric face-flag triangulation of ∂P_n, the two z,z' lie in a common flag simplex and therefore in a common PROPER polytope face H. Their selected actual f=0 permutations p_z,p_z' lie in the respective minimal faces H(z),H(z')⊆H, hence both lie in H. Every proper permutohedron face is contained in some proper FACET. A facet of the standard permutohedron is given by a nonempty proper subset S of coordinates occupying the first |S| positions of the order (or by its complementary last-block equivalent). Thus any two original vertices p,q in that facet share an exact proper prefix used-coordinate SUPPORT S. Their full geodesics from root x therefore meet at x⊕S. Moreover a proper convex face cannot contain both centrally antipodal original vertices p and rev p: their midpoint is the CENTER of P_n, an interior point. So q≠rev p. Finally their switch labels ±j give the displayed physically verified opposite reflected switch bits. QED.

**INTERPRETATION.** This is a DIMENSION-INDEPENDENT GENUINE TOPOLOGICAL FORCING THEOREM, NOT a virtual barycentric zero only: high index and Tucker's no-complement obstruction force TWO HONEST full physical geodesic witnesses at the SAME ROOT, with a common intermediate cube vertex and opposed mirror-switch patterns. The proof uses physical face locality, active NORI oddness, and the actual permutohedron face incidence. It does NOT YET force either geodesic to have <=1 switch; the remaining combinatorial obligation is to leverage the common-prefix-support connector and opposite mirror-switch orientations to exchange segments or slides while preserving a full geodesic and strictly reducing defects.

**OPEN NEXT STEP.** Strengthen this Tucker pair to a *compatible local exchange*: either force q to be obtained from p by one adjacent transposition with controlled two-window effects, or force a common intermediate vertex at a switch boundary with monochromaticly compatible ordered-two-direction tails, thereby connecting directly to the exact reversed-tail support-overlap NORI closure theorem. No such strengthening is claimed in this item.

## An exact antipodal-root switch-coboundary identity for physical ordered faces

Let \(n\ge5\) and \(c\) be any active NORI coloring of PHYSICAL ordered three-faces, satisfying
\[
c(\bar F,\operatorname{rev}\pi)=1\oplus c(F,\pi).
\]
Fix ANY full direction order \(p=(p_1,\ldots,p_n)\) and ANY physical root \(x\). Let \(L=n-2\), and let \(F_j=F_j(x,p)\) be the actual physical three-face at the jth window, with ordered free direction triple \(t_j=(p_j,p_{j+1},p_{j+2})\). Define the same-face **local triple-reversal asymmetry bit**
\[
r_j(x,p)=c(F_j,t_j)\oplus c(F_j,\operatorname{rev}t_j)\in\mathbb F_2.
\tag{1}
\]
Unlike reversal-oddness across *antipodal physical faces*, this is a comparison of two orders ON THE SAME physical face, and may be 0 or 1 independently as the coloring varies.

**Theorem (exact antipodal-root discrete gauge/coboundary identity).** Write the actual ordered-face word \(w_j(x,p)=c(F_j,t_j)\) and switch bits \(s_j(x,p)=w_j(x,p)\oplus w_{j+1}(x,p)\), \(1\le j\le L-1=n-3\). At the ANTIPODAL root \(\bar x=x\oplus[n]\), with the SAME direction order \(p\), one has:
\[
\boxed{w_j(\bar x,p)=1\oplus w_j(x,p)\oplus r_j(x,p),}
\tag{2}
\]
\[
\boxed{s_j(\bar x,p)=s_j(x,p)\oplus r_j(x,p)\oplus r_{j+1}(x,p).}
\tag{3}
\]
Thus the two full switch vectors differ by the \(\mathbb F_2\) discrete coboundary \(\delta r\) of the actual local order-reversal asymmetry 0-cochain along the window-index path:
\[
\boxed{s(\bar x,p)\oplus s(x,p)=\delta r.}
\tag{4}
\]
The reversal-asymmetry word is itself antipodally ROOT-INVARIANT and full-order-reversal covariant:
\[
r_j(\bar x,p)=r_j(x,p),\qquad
r_j(x,\operatorname{rev}p)=r_{L+1-j}(x,p).
\tag{5}
\]
The endpoints of \(r\) agree if and only if the two antipodal-root paths have the SAME switch-count parity:
\[
\bigoplus_{j=1}^{L-1}s_j(\bar x,p)
=\bigoplus_{j=1}^{L-1}s_j(x,p)
\quad\Longleftrightarrow\quad r_1=r_L.
\tag{6}
\]

**Proof.** At the same progress rank, the rooted path from \(\bar x\) has the SAME window free directions and all exterior fixed bits complemented, so its physical window face is literally \(\bar F_j\). The active axiom applied with reversed free order gives
\[
c(\bar F_j,t_j)=1\oplus c(F_j,\operatorname{rev}t_j)
=1\oplus w_j(x,p)\oplus r_j(x,p),
\]
which is (2). XOR consecutive window identities: the two constant 1s cancel, giving (3)-(4). Applying the same argument to the reversed order on \(\bar F_j\) shows
\[
r(\bar F_j,t_j)=c(\bar F_j,t_j)\oplus c(\bar F_j,\operatorname{rev}t_j)
=r(F_j,t_j),
\]
so \(r_j(\bar x,p)=r_j(x,p)\). The actual full-path antipodal reversal at the FIXED root \(x\) sends \(p\mapsto\operatorname{rev}p\) and transforms the physical color word to the reversed complement. Its corresponding reversal-asymmetry comparison therefore gives the reversed \(r\)-word, proving the second identity in (5). Finally XOR (3) across all \(j\); the interior \(r\) terms cancel in pairs, yielding (6). \(\square\)

**Corollary (antipodally synchronized endpoint-balanced paths have a closed reversal gauge).** For a full permutation \(p\) that is endpoint-opposed at BOTH \(x\) and \(\bar x\), the two switch vectors have odd parity, hence
\[
\boxed{r_1(x,p)=r_L(x,p).}
\tag{7}
\]
The synchronized full-path corridors from Item \`nori_same_order_antipodal_root_pairs_endpoint_opposition_disjoint_triple_orbits_20261008\` therefore provide, at every prescribed antipodal root pair in \(n\ge10\), an entire \((n-6)!\)-packet of actual full paths with a CLOSED reversal-asymmetry cochain (identical first/last gauge bits), while their internal switch vectors differ by its exact derivative. Moreover the endpoint-closed condition is EXACTLY the two-root equality of reversal-orbit signatures used in that theorem.

**Why this is mathematically useful.** Earlier permutohedral Tucker labels track internal switch positions but do not control how switches change when ROOT is antipodally complemented. Formula (3) supplies that missing PHYSICAL comparison without inventing an abstract sign-vector action: at any fixed complete order, the antipodal root transfer is a gauge transformation by a same-face reversal asymmetry word. It is compatible with order-reversal and is an actual 1-dimensional chain-complex coboundary identity. It suggests constructing a two-parameter root/order carrier with the switch-change 1-cochain and its cross-root gauge \(r\), then deriving a nontrivial holonomy obstruction when certified cells are glued around root-cube and permutohedral exchange cycles.

**Crucial limitation.** The cochain may be identically zero: a coloring independent of reversing local three-direction order has \(r_j=0\) everywhere, and the two antipodal-root switch vectors then coincide, even if BOTH contain many switches (as in the valid full exterior-parity coloring). Consequently the coboundary identity alone cannot reduce switches or force grand closure. A proof must combine it with genuine root mobility over MORE THAN one antipodal pair and/or with a nontrivial coupled topological class. No universal holonomy contradiction is asserted.

To turn these packets into grand closure, one needs a constructive root/order exchange that both respects the antipodal label correspondence and controls the defect of the stitched path.
