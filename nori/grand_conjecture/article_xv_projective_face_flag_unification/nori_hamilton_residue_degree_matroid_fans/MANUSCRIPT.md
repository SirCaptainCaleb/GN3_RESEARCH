## Degree Theory on Hamilton Residues and Matroid Fans

##### Degree-one obstruction on a Hamilton two-block cell

**Theorem.** A reversal-odd coloring of triples on six vertices admits a four-dimensional dual Coxeter cell D all of whose 36 Hamilton orders have two or more switches, while the extreme-switch bivector labels have a piecewise-linear boundary realization of nonzero degree in S^3.

*Proof.* Partition the six symbols into triples A and B. Each flag in the two-block cell D has order (a,b,c,d,e,f) with abc permuting A and def permuting B. Choose any reversal-odd bit functions t(abc), s(def) on permutations of these respective triples. Prescribe consecutive colors t,1-t,1-s,s. This defines legal triple colors: the second bit uses b(b,c,d) with a determined by b,c, and the third uses b(c,d,e) with f determined by d,e. Their reverses do not conflict with the prescribed types. Every word switches at positions 1 and 3.

Put T=sum_{a in A} e_a - 1/2 1, xi_c=e_c-(sum_A e)/3, eta_d=e_d-(sum_B e)/3. Centered prefix vectors satisfy Z_2=(2/3)T-xi_c and Z_4=(2/3)T+eta_d. Since ||T||^2=3/2, contracting the bivector Z_2 wedge Z_4 by T gives xi_c+eta_d in the four-dimensional orthogonal sum W_A+W_B. The cell D is the product of two hexagons. On their boundary vertices, the last A symbol and first B symbol each run around the three corresponding centered triangle vertices once, with repetitions. Cone both hexagon boundary maps to zero at their centers. Their product agrees with all 36 contracted flag labels, is nowhere zero on the boundary of D, and has an isolated interior zero of Brouwer degree plus or minus one. Normalizing the boundary map gives degree plus or minus one in S^3. QED.

The individual-cell degree depends on lower-cell filling choices. This refutes a proposed local automatic degree-zero mechanism; global compatibility between two-block residues remains open.

##### Transport of top obstruction degrees along three-block residues

Let \(n\ge5\), \(d=n-2\), and let \(X\cong S^d\) be the dual type-A Coxeter cell complex of Hamilton orders on \(n\) symbols, with free order-reversal involution \(J\). Put \(Y=X/J\cong\mathbb RP^d\). Consider an odd map from \(X^{(d-1)}\) to the unit sphere \(S^{d-1}\) of the sign representation. Each orbit of top cells carries a modulo-two attaching degree.

**Theorem 1 (connected degree-transfer graph).** The top-cell orbits are indexed by unordered bipartitions \(\{A,V\setminus A\}\), with \(\varnothing\ne A\subsetneq V\). The codimension-one cell orbits are indexed by ordered three-block partitions, modulo reversal. A three-block residue \(A|B|C\) joins the two top-cell orbits represented by \(A|(B\cup C)\) and \((A\cup B)|C\). The resulting graph on top-cell orbits is connected.

*Proof.* A dual cell indexed by an ordered partition of \(V\) into \(k\) nonempty blocks has dimension \(n-k\). Its codimension-one incidences arise by merging two neighboring blocks. This gives the claimed description. In the graph, the bipartitions represented by proper sets \(A\subsetneq A'\) are adjacent: use the three blocks \(A|(A'\setminus A)|(V\setminus A')\). From any proper set repeatedly delete an element until a singleton remains. Singleton partitions are connected using a two-element union. Hence the graph is connected. \(\square\)

**Theorem 2 (arbitrary redistribution of the unavoidable odd obstruction).** Keeping the equivariant map fixed through dimension \(d-2\), changes of its fillings on the \((d-1)\)-cells can produce every modulo-two top-cell degree vector with odd total sum. In particular, all nonzero obstruction degrees can be concentrated in any prescribed top-cell orbit.

*Proof.* The first equivariant obstruction is the mod-two Euler class of \(d\) copies of the tautological line bundle on \(Y=\mathbb RP^d\), namely \(\alpha^d\). Its evaluation on the fundamental class is one, so the sum of top-cell degrees is odd for every choice of fillings.

Let \(C\) be a codimension-one cell of \(Y\). Modify its map to \(S^{d-1}\) in the interior by inserting a sphere map of degree one, leaving its boundary fixed. Such a modification exists because \(\pi_{d-1}(S^{d-1})=\mathbb Z\). The two top cells incident with \(C\) each have their attaching degree changed by one modulo two; no other top-cell degree changes. Thus each edge of the graph from Theorem 1 permits toggling its two endpoint entries. In a connected graph, these edge-toggle vectors span the subspace of even-sum vectors over \(\mathbb F_2\), as follows by using a spanning tree to move units between vertices. The starting degree vector has odd sum; adding every even-sum vector realizes every odd-sum vector. Lift each cell modification to its opposite partner in \(X\) to retain equivariance. \(\square\)

**Consequence.** For the critically compressed switch-bivector labeling, individual top-cell obstruction degrees depend on choices of intermediate fillings; only their global cohomology class is forced. A color-sensitive proof of the boundary one-switch conjecture must therefore supply a coherent normalization of those fillings and derive a contradiction for the resulting global obstruction. No argument based solely on vanishing degrees for separately chosen two-block cells establishes such a normalization.

##### Universal prefix degrees on two-block Coxeter cells

**Lemma 1 (prefix map of a permutahedron).** Let \(m\ge2\) and \(1\le k\le m-1\). In \(W_m=\{z:\sum z_i=0\}\), assign each vertex \(\pi\) of the \((m-1)\)-permutahedron \(P_m\) the centered prefix label
\[
z_k(\pi)=\sum_{j\le k}e_{\pi_j}-\frac{k}{m}\mathbf1.
\]
After affine interpolation on a triangulation of each boundary face, these labels define a zero-free map \(f_k:\partial P_m\to W_m\setminus\{0\}\). Its radial normalization has degree \(\pm1\).

*Proof.* Use the centered permutahedron vertices \(u_\pi=\sum_j((m+1)/2-j)e_{\pi_j}\). A proper boundary face is represented by an ordered partition with first block \(S\) of size \(h\), where \(1\le h<m\). On every vertex \(\pi\) of that face,
\[
\sum_{i\in S}(u_\pi)_i=h(m-h)/2>0,\qquad
\sum_{i\in S}(z_k(\pi))_i=\min(k,h)-kh/m>0.
\]
Consequently every convex combination of the prescribed prefix labels on this face, and every straight-line interpolation from the identity embedding \(u_\pi\), stays in a common strict halfspace avoiding zero. The normalized boundary prefix map is therefore homotopic to the radial boundary map of the centered permutahedron, which has degree \(\pm1\). QED.

**Theorem 2 (product degree for a fixed straddling switch pair).** Partition \([n]=A\sqcup B\), \(|A|=a\ge2\), \(|B|=b\ge2\), and consider the top dual type-A cell \(D=P_a\times P_b\) consisting of Hamilton words listing \(A\) before \(B\). Fix \(1\le k<a\) and \(1\le\ell<b\). For each such word \(\pi\), let \(Z_j(\pi)\) be its centered length-\(j\) prefix vector and put
\[
T=\sum_{i\in A}e_i-\frac an\mathbf1,\quad
E(\pi)=Z_k(\pi)\wedge Z_{a+\ell}(\pi).
\]
The contracted vertex labels \(\iota_T E(\pi)\) extend to a map \(\partial D\to W\cap T^\perp\setminus\{0\}\) of degree \(\pm1\), with \(\dim(W\cap T^\perp)=n-2=\dim D\).

*Proof.* Write \(u_k\in W_A\) for the centered prefix indicator of the first \(k\) members of \(A\), and \(v_\ell\in W_B\) for the first \(\ell\) members of \(B\). One has
\[
Z_k=(k/a)T+u_k,\quad
Z_{a+\ell}=((b-\ell)/b)T+v_\ell,\quad \|T\|^2=ab/n.
\]
Therefore
\[
\iota_T E=\|T\|^2\big((k/a)v_\ell-((b-\ell)/b)u_k\big).
\]
The two summands belong to orthogonal complementary spaces \(W_B\) and \(W_A\) of respective dimensions \(b-1,a-1\). By Lemma 1, the corresponding prefix maps on each permutahedron boundary have degree \(\pm1\). Coning each to zero in the interior gives maps of each ball with a unique zero of degree \(\pm1\). Their weighted direct sum on \(D\) has a single zero, with product degree \(\pm1\), and is nonzero on \(\partial D\). QED.

**Corollary 3 (all switch pairs, six-vertex product example).** For the earlier reversal-odd \(3+3\) coloring, the color word is \((t,1-t,1-s,s)\). Its switch indicators are \((1,\epsilon,1)\), where \(\epsilon=t\mathbin{\mathrm{xor}}s\). Besides the extreme pair, the full quadratic switch bivector is
\[
\mathcal B_1=Z_2\wedge Z_4+\epsilon(Z_2\wedge Z_3+Z_3\wedge Z_4).
\]
With \(T=Z_3\), \(\xi_c=e_c-\frac13\sum_Ae\), and \(\eta_d=e_d-\frac13\sum_Be\),
\[
\boxed{\iota_T\mathcal B_1=(1+\tfrac32\epsilon)(\xi_c+\eta_d).}
\]
Thus its normalized contracted labels agree at every flag with those from the extreme switch pair; the same degree-one boundary extension applies even when the middle switch occurs.

**Qualification.** Theorem 2 is geometric and conditional. For boundary triple colors, the switch ranks \(k-1\) and \(a+\ell-1\) must lie among the legal internal ranks. The theorem does not claim that arbitrary partitions admit reversal-odd colorings imposing these fixed first/last switch positions on all flags. Its conclusion is the persistence of the degree-one obstruction whenever the indicated fixed-pair configuration occurs.

##### The four-symbol threshold for uniformly fixed switches

Let \(b(x,y,z)\in\mathbb F_2\) color ordered distinct triples, with \(b(z,y,x)=1-b(x,y,z)\). For a Hamilton order \(\pi\), the consecutive triple-color word has switches at the comparisons of successive triples. For a two-block cell \(D(A|B)\), all permutations within \(A\) and within \(B\) are present.

**Lemma 1 (no universal homogeneous comparison on five symbols).** If \(U\) has at least five elements, there is no reversal-odd triple coloring such that
\[
b(x,y,z)+b(y,z,w)=\varepsilon\pmod2
\]
for every ordered quadruple of distinct symbols from \(U\), for either fixed \(\varepsilon\in\{0,1\}\).

*Proof.* Fix distinct \(y,z\). For any distinct \(x,x'\notin\{y,z\}\), choose \(w\) distinct from all four; applying the identity with \(x\) and \(x'\), and the same \(y,z,w\), gives \(b(x,y,z)=b(x',y,z)\). Therefore \(b(x,y,z)=f(y,z)\) is independent of \(x\). Reversal oddness gives \(f(y,x)=1-f(y,z)\) for every distinct \(x,z\ne y\). Three distinct choices of \(x,z\) make these pairwise complement equations inconsistent. QED.

**Lemma 2 (mixed seam rigidity).** Let \(|A|\ge4\). It is impossible that, for every order of \(A|B\), the last all-\(A\) triple and the following \(AAB\) triple have opposite colors. Dually, if \(|B|\ge4\), the first \(ABB\) triple and following all-\(B\) triple cannot have opposite colors for every order.

*Proof.* The first alleged condition says \(b(x,y,z)=1-b(y,z,d)\) for every distinct \(x,y,z\in A\), \(d\in B\). Holding \(y,z,d\) fixed shows \(b(x,y,z)=f(y,z)\), independent of \(x\). Reversal oddness then gives \(f(y,x)=1-f(y,z)\) for all distinct \(x,z\ne y\). As \(|A|\ge4\), there are at least three such symbols, contradiction. The second statement follows by the symmetric final-block argument. QED.

**Theorem 3 (global fixed-switch cutoff).** Suppose every flag of \(D(A|B)\) has a first switch and the index of this first switch is the same for all flags. Then \(|A|\le4\). If every flag has a last switch at a common index, then \(|B|\le4\). In particular, for \(n\ge9\), no two-block cell of the type-A Hamilton Coxeter complex supports a reversal-odd coloring for which all flags have the same first and last switch positions.

*Proof.* Put \(a=|A|\ge5\). If the common first switch occurs among the successive all-\(A\) triple windows (indices \(j\le a-3\)), all ordered quadruples of \(A\) would give an opposite-color comparison, contrary to Lemma 1 with \(\varepsilon=1\). If it occurs between the last all-\(A\) and first \(AAB\) windows (\(j=a-2\)), Lemma 2 applies. If it occurs later (\(j\ge a-1\)), the first two all-\(A\) windows would have equal colors for every order, contrary to Lemma 1 with \(\varepsilon=0\). The last-switch argument reverses the roles of initial and final blocks: a common last switch within \(BBB\) windows contradicts Lemma 1, one on the \(ABB/BBB\) seam contradicts Lemma 2, and an earlier last switch forces equality throughout \(BBB\). At least one block has size at least five when \(n\ge9\). QED.

**Theorem 4 (sharpness; color-realizable degree-one cells in dimensions 6, 7, 8).** For every pair \(a,b\in\{3,4\}\) there exists an unrestricted reversal-odd triple coloring on \(A\sqcup B\), with \(|A|=a,|B|=b\), such that every Hamilton order in \(D(A|B)\) has first switch at position \(1\) and last switch at position \(n-3\). Consequently every one of its \(a!b!\) complete orders has at least two switches, and its extreme-switch bivectors induce a degree-\(\pm1\) map on the boundary of \(D\) after contraction against the centered block vector.

*Proof.* On a four-element block \(U\), define the color of the ordered triple \((x,y,z)\) to be the parity of the unique permutation \((x,y,z,w)\) of \(U\), where \(w\) is the omitted symbol and a reference orientation of \(U\) is fixed. This is reversal odd, and shifting the four-symbol order cyclically from \((x,y,z,w)\) to \((y,z,w,x)\) changes permutation parity. Hence the two consecutive triple colors in every four-symbol order are opposite.

For an initial three-element block \(A\), prescribe \(b(y,z,d)=1-b(x,y,z)\), where \(x\) is the third member of \(A\), \(y,z\) are its two final members, and \(d\in B\) is the first member of \(B\). This forces the first switch for every order; this assignment concerns only \(AAB\) triples. For an initial four-element block, the parity construction already forces the first switch between its first two \(AAA\) windows.

For a final three-element block \(B\), prescribe \(b(c,d,e)=1-b(d,e,f)\), where \(d,e\) are its first two members, \(f\) is its third, and \(c\in A\) is the preceding last member of \(A\). This forces the last switch and concerns only \(ABB\) triples. For a final four-element block, the parity construction forces the last switch between its final two \(BBB\) windows. The assigned triple types are disjoint and their reverses either match the required oddness within a single block or lie in unassigned types. Thus extend arbitrarily on remaining reversal pairs. The first and last switch prefix ranks are \(2\) and \(n-2\), strictly inside their respective blocks for \(a,b\in\{3,4\}\). Apply the product-degree theorem for centered permutahedral prefix maps to obtain degree \(\pm1\). QED.

**Scope.** This sharp cutoff is specific to *uniformly fixed first and last switch indices across an entire two-block cell*. It does not limit top-cell obstruction degrees for arbitrary colorings with variable switch ranks.

##### Unit degree survives arbitrary variation of the two switch ranks

Let \(P_m\) denote the centered permutahedron of full orders on \(m\) symbols, and let \(Z_k(\pi)=\sum_{j\le k}e_{\pi_j}-(k/m)\mathbf1\) for \(1\le k<m\).

**Lemma 1 (variable-prefix sphere degree).** For every function \(k:S_m\to\{1,\ldots,m-1\}\), the boundary vertex labeling \(\pi\mapsto Z_{k(\pi)}(\pi)\) has a zero-free simplicial affine extension over \(\partial P_m\). Its radial normalization has degree \(\pm1\), independently of the function \(k\).

*Proof.* On any proper face of \(P_m\), all orders begin with the elements of a fixed nonempty proper first block \(S\), in some order. For every \(1\le k<m\) and every order on this face,
\[
\sum_{i\in S}(Z_k(\pi))_i=\min(k,|S|)-\frac{k|S|}{m}>0.
\tag{1}
\]
Thus convex hulls of the labels of any boundary face avoid zero. Moreover the straight-line homotopy at vertices from the variable labels to the centered permutahedron vertex vectors stays in this same strict halfspace on each face. The latter radial boundary map has degree one up to orientation. QED.

**Theorem 2 (variable-rank straddling unit degree).** Let \(V=A\sqcup B\), with \(a=|A|\ge2\), \(b=|B|\ge2\), and let \(D=P_a\times P_b\) be the top dual Coxeter cell of Hamilton orders listing \(A\) before \(B\). For each \(\pi\in D^{(0)}\), independently select integers
\[
1\le k(\pi)\le a-1,\qquad 1\le\ell(\pi)\le b-1.
\]
Put \(T=\sum_{i\in A}e_i-(a/(a+b))\mathbf1\), and let
\[
F(\pi)=\iota_T\left(Z_{k(\pi)}(\pi)\wedge Z_{a+\ell(\pi)}(\pi)\right)
\in W\cap T^\perp\cong\mathbb R^{a+b-2}.
\]
For any vertex triangulation of \(\partial D\), the affine extension of \(F\) is nowhere zero and its radial normalization has degree \(\pm1\), *regardless of the chosen functions \(k,\ell\)*.

*Proof.* Decompose \(W\cap T^\perp=W_A\oplus W_B\), with dimensions \(a-1,b-1\), and write \(u_k(\pi)\in W_A\) and \(v_\ell(\pi)\in W_B\) for the centered prefix indicators inside their blocks. Then
\[
F(\pi)=\|T\|^2\left(\frac{k(\pi)}a v_{\ell(\pi)}(\pi)
-\frac{b-\ell(\pi)}b u_{k(\pi)}(\pi)\right).
\tag{2}
\]
Each boundary facet of \(D\) is either \(H_A\times P_b\) or \(P_a\times H_B\), where \(H_A,H_B\) are permutahedral facets. In the first case, if \(S\subsetneq A\) is the first block defining \(H_A\), then for every flag of that facet,
\[
\sum_{i\in S}F_i
=-\|T\|^2\frac{b-\ell(\pi)}b
\left(\min(k(\pi),|S|)-\frac{k(\pi)|S|}{a}\right)<0.
\tag{3}
\]
In the second case, the corresponding sum on the first block \(R\subsetneq B\) is
\[
\sum_{i\in R}F_i
=\|T\|^2\frac{k(\pi)}a
\left(\min(\ell(\pi),|R|)-\frac{\ell(\pi)|R|}{b}\right)>0.
\tag{4}
\]
Every boundary simplex lies in a facet, so (3) or (4) places its vertex labels in a common strict halfspace. Affine interpolation therefore never vanishes. These same inequalities persist through a straight-line homotopy from the variable-rank labels to labels with fixed arbitrary ranks \(k_0,\ell_0\). The fixed-rank product map has degree \(\pm1\) by the permutahedral prefix degree theorem and multiplicativity of Brouwer degree. Hence so does the variable-rank map. QED.

**Corollary 3 (color-sensitive formulation).** In an unrestricted reversal-odd boundary 3-tournament, suppose every Hamilton ordering in one two-block cell \(D(A|B)\) has at least one color switch whose centered prefix rank lies strictly inside \(A\) and at least one color switch whose prefix rank lies strictly inside \(B\). Then the extreme-switch bivector labeling on that cell, after contraction by its centered block vector, has canonical boundary degree \(\pm1\), even when the first and last switch ranks vary from order to order.

**Scope.** The hypotheses involve only where color switches occur relative to a bipartition, not their positions within either block. Unlike the fixed-rank construction, the theorem applies in all dimensions. It does not claim that every globally all-bad coloring possesses such a straddling top cell, and it does not itself provide a globally compatible selection of fillings on different cells.

##### Connected matroid greedy fans carry degree one

Fix an \(m\)-element ground set \(E\), \(m\ge2\), and \(W=\{z\in\mathbb R^E:\sum z_i=0\}\). Let \(P_m\subset W\) be the centered permutahedron with vertices indexed by all orders \(\pi\) of \(E\).

**Theorem 1 (matroidal prefix degree).** Let \(M\) be any connected matroid on \(E\). Put \(p_M=|\mathcal B(M)|^{-1}\sum_{B\in\mathcal B(M)}\mathbf1_B\), the barycenter of its basis polytope. Let \(B_M(\pi)\) be the greedy basis obtained by scanning the order \(\pi\) and accepting an element precisely when it increases rank. At each permutahedral vertex define
\[
g_M(\pi)=\mathbf1_{B_M(\pi)}-p_M\in W.
\]
This vertex labeling admits a zero-free piecewise-affine extension to \(\partial P_m\). After radial normalization, its degree is \(\pm1\).

*Proof.* A proper face of \(P_m\) is indexed by an ordered partition with first block \(S\), a nonempty proper subset of \(E\). Every order compatible with that face begins with precisely the elements of \(S\). Greedy selection accepts a basis of \(S\) before any other element, so
\[
\sum_{e\in S}g_M(\pi)_e=r_M(S)-p_M(S).
\tag{1}
\]
Connectivity of \(M\) implies \(r_M(S)+r_M(E\setminus S)>r_M(E)\). Extend a basis of \(E\setminus S\) to a basis of \(M\); this basis meets \(S\) in only \(r_M(E)-r_M(E\setminus S)<r_M(S)\) elements. All bases meet \(S\) in at most \(r_M(S)\) elements. Therefore their average satisfies \(p_M(S)<r_M(S)\), so (1) is strictly positive at all vertices of the face. Affine interpolation on any triangulation of that boundary face stays in this halfspace and avoids zero.

The centered permutahedron vertex \(u_\pi=\sum_{j=1}^m((m+1)/2-j)e_{\pi_j}\) satisfies \(\sum_{e\in S}(u_\pi)_e=|S|(m-|S|)/2>0\) on this face. Consequently the straight-line homotopy from \(g_M\) to \(u_\pi\), extended affinely over boundary simplices, avoids zero throughout. The radial map from the centered permutahedron boundary has degree \(\pm1\). QED.

**Theorem 2 (arbitrary connected matroid selection).** Even if a different connected matroid \(M_\pi\) is selected independently at every permutation \(\pi\), the labels \(g_{M_\pi}(\pi)\) still induce a zero-free boundary map of degree \(\pm1\).

*Proof.* The inequality (1) holds for every connected matroid on the same ground set, with the same positive side of the supporting hyperplane associated with \(S\). Both the zero-avoidance and the homotopy to \(u_\pi\) therefore hold vertexwise on each proper permutahedral face, regardless of the choice of \(M_\pi\). QED.

**Theorem 3 (dual complement and reversal).** Let \(M^*\) be the dual matroid and \(\pi^R\) the reversed total order. Then
\[
B_{M^*}(\pi^R)=E\setminus B_M(\pi),\qquad
p_{M^*}=\mathbf1-p_M,\qquad
\boxed{g_{M^*}(\pi^R)=-g_M(\pi).}
\tag{2}
\]

*Proof.* A basis of \(M^*\) is the complement of a basis of \(M\). A greedy basis is the unique maximum-weight basis for any strictly decreasing order-compatible generic weights; reversing the order is equivalent to negating the weights. Maximizing reversed weights among dual bases is thus equivalent to maximizing the original weights among primal bases and taking complements. Averaging the bijection of bases gives the barycenter identity, and subtracting barycenters gives (2). QED.

**Specialization to the switch-bivector program.** The greedy basis of the uniform matroid \(U_{k,m}\) is the first \(k\) symbols of \(\pi\), with barycenter \((k/m)\mathbf1\). Thus Theorems 1 and 2 generalize the variable-length centered prefix degree theorem. Equation (2) explains why complement reversal of ordered flags acts antipodally on these carrier vectors. This is an intrinsic matroidal degree carrier shared by the dimension-order structures underlying the cube and boundary Hamilton order problems, not a proof of either coloring conjecture; the necessary color-sensitive global extension remains unresolved.

##### Greedy matroid degree: connectivity is the sharp zero-free threshold

Let \(E\) have \(m\ge2\) elements, \(W_E=\{x\in\mathbb R^E:\sum x_e=0\}\), and \(P_E\subset W_E\) the centered permutahedron, with vertices \(\pi\) indexed by orders of \(E\). For any matroid \(M\) on \(E\), write \(B_M(\pi)\) for its lexicographic greedy basis, \(p_M=|\mathcal B(M)|^{-1}\sum_{B\in\mathcal B(M)}\mathbf1_B\), and \(g_M(\pi)=\mathbf1_{B_M(\pi)}-p_M\).

**Theorem 1 (connectivity criterion).** For any triangulation of the permutahedral boundary using its vertices, extend the vertex labels \(g_M\) affinely over simplices. The resulting boundary map avoids zero if and only if \(M\) is connected. When connected, its normalized map has degree \(\pm1\). When disconnected, for *every* such triangulation the map vanishes on the ordered-component face of \(P_E\).

*Proof.* If \(M\) is connected, then for every nonempty proper \(S\subset E\) the matroid inequality
\[
r_M(S)+r_M(E\setminus S)>r_M(E)
\]
implies \(p_M(S)<r_M(S)\): extend a basis of the complement to a basis of \(M\), obtaining one whose intersection with \(S\) has fewer than \(r_M(S)\) members, while no basis exceeds \(r_M(S)\). On a face indexed by an ordered partition whose first block is \(S\), greedily scanning any compatible permutation selects \(r_M(S)\) elements of \(S\). Hence the linear functional \(\sum_{e\in S}x_e\) takes the strictly positive value \(r_M(S)-p_M(S)\) on every prescribed vertex label of that face. Affine extension is zero-free there. The same halfspace contains the standard centered permutahedron vertices. Straight-line interpolation to the identity embedding is therefore zero-free on the entire boundary and preserves degree \(\pm1\).

Conversely suppose \(M=\bigoplus_{i=1}^q M_i\), \(q\ge2\), is the direct sum of its connected matroid components \(C_1,\ldots,C_q\). Consider the proper face \(F=C_1|\cdots|C_q\) of the permutahedron. Geometrically \(F\cong\prod_{i=1}^q P_{C_i}\), a ball of dimension \(m-q\). Greedy basis selection and basis barycenters split componentwise. Therefore the vertex labels on \(F\) lie in
\[
L=\bigoplus_{i=1}^q W_{C_i},\qquad\dim L=m-q=\dim F.
\]
On any proper boundary face \(H\) of \(F\), at least one component permutahedron has a proper first block \(S\subsetneq C_i\), so that component contributes the positive supporting functional \(r_{M_i}(S)-p_{M_i}(S)>0\). The affine boundary map on \(\partial F\) avoids zero and is straight-line homotopic there to the centered product-polytope embedding \(F\hookrightarrow L\). It consequently has degree \(\pm1\). Any continuous extension from \(F\) to \(L\) must attain zero, else its normalized boundary map would extend over the ball. In particular every affine triangulation extension of \(g_M\) has a zero on the proper face \(F\subset\partial P_E\). Singleton components cause no difficulty: their factors have dimension zero and their summands are zero. QED.

**Theorem 2 (equivariant rigidity of variable connected-matroid assignments).** Assign an independently chosen connected matroid \(M_\pi\) on \(E\) to every full order \(\pi\), subject only to
\[
M_{\pi^R}=M_\pi^*.
\]
Then the greedy labeling \(g(\pi)=g_{M_\pi}(\pi)\) extends to a zero-free, reversal-odd map on \(\partial P_E\). More strongly, every such labeling is *equivariantly homotopic* to the standard centered permutahedron boundary embedding. Thus its ordinary degree is odd, and its equivariant homotopy class is independent of all matroid choices.

*Proof.* Greedy duality gives \(g_{M^*}(\pi^R)=-g_M(\pi)\). The centrally inverted standard permutahedral vertex vector \(u_\pi\) also satisfies \(u_{\pi^R}=-u_\pi\). For each face with first block \(S\), the connectedness argument above places \(g_{M_\pi}(\pi)\) and \(u_\pi\) in one strict positive halfspace simultaneously, for every vertex \(\pi\) of that face. Thus the affine straight-line homotopy \((1-t)g+t u\) is zero-free on every boundary simplex and is reversal-equivariant throughout. Its endpoint is the identity boundary embedding, proving the assertion. QED.

**Consequence for the unification program.** Duality and connected greedy-basis carriers supply the correct antipodal behavior automatically, but carry no color-sensitive homotopy information when connectivity is retained at every flag. A useful contradiction via this carrier must force a loss of matroid connectivity, a change in target dimension, or additional cross-face constraints not reducible to independent greedy selections. Theorem 1 gives a precise geometric signature of a connectivity failure: a zero already on the ordered-component face, rather than a mysterious high-dimensional top-cell obstruction.

##### The full Grassmannian homotopy obstruction of straddling switch planes

Let \(n=a+b\ge6\), with \(a,b\ge2\), \(A\sqcup B=[n]\), \(W=\{z\in\mathbb R^n:\sum z_i=0\}\), and \(D=P_a\times P_b\) the type-A dual top cell of Hamilton orders listing \(A\) before \(B\). Its dimension is \(d=n-2\), and \(W\cong\mathbb R^{d+1}\).

At every vertex \(\pi\in D\) choose ranks \(1\le k(\pi)<a\) and \(1\le\ell(\pi)<b\). Let
\[
x_\pi=Z_{k(\pi)}(\pi),\qquad
y_\pi=Z_{a+\ell(\pi)}(\pi).
\]
Interpolate the two vector assignments separately and affinely on any triangulation of \(D\) using its permutahedral vertices.

**Theorem 1 (canonical boundary plane obstruction).** The vectors \(x,y\) are independent on \(\partial D\). They therefore define an oriented 2-plane map
\[
\Psi:\partial D\cong S^{d-1}\longrightarrow\widetilde{\mathrm{Gr}}_2(W)
\]
and an orthonormal frame lift to \(V_2(W)\). The class of this map is a generator of
\[
\boxed{
\pi_{d-1}\bigl(\widetilde{\mathrm{Gr}}_2(\mathbb R^{d+1})\bigr)
\cong
\pi_{d-1}\bigl(V_2(\mathbb R^{d+1})\bigr)
\cong
\mathbb Z/\chi(S^d)\mathbb Z.
}
\tag{1}
\]
In particular this group is \(\mathbb Z\) for odd \(n\), and \(\mathbb Z/2\) for even \(n\); the class is nonzero in either case, and \(\Psi\) does not extend across \(D\). Its class is independent of the two rank-selection functions.

*Proof.* Set
\[
T=\sum_{i\in A}e_i-\frac an\mathbf1,\qquad
W\cap T^\perp=W_A\oplus W_B.
\]
At every vertex,
\[
x_\pi=\frac{k(\pi)}a T+u_\pi,\qquad
y_\pi=\frac{b-\ell(\pi)}b T+v_\pi,
\tag{2}
\]
where \(u_\pi\in W_A\) is the centered \(k(\pi)\)-prefix in \(A\) and \(v_\pi\in W_B\) is the centered \(\ell(\pi)\)-prefix in \(B\). The interpolated functions retain (2), with positive scalar coefficients \(\alpha,\beta\) and interpolated \(u,v\). On a boundary facet arising from a proper initial block \(S\subsetneq A\), the linear functional \(\sum_{i\in S}u_i\) is strictly positive on every vertex and therefore throughout that facet. Hence \(u\ne0\) there. On a facet arising from a proper initial block of \(B\), similarly \(v\ne0\). Since \(x=\alpha T+u\), \(y=\beta T+v\), with \(\alpha,\beta>0\), a dependence relation would force \(u=v=0\); this is impossible on \(\partial D\). Thus the boundary frame exists.

The first vector \(x\) is nowhere zero on the entire ball \(D\): \(\langle T,x\rangle>0\). It consequently extends into one open hemisphere of \(S(W)\), so the orthogonal complement bundle \(x^\perp\) on \(D\) has a trivialization canonically homotopic to the one obtained by projecting along \(x\) onto \(T^\perp\). The second-vector class in the fiber sphere can be represented by the nonzero boundary vector
\[
H=\iota_T(x\wedge y)
=\|T\|^2(\alpha v-\beta u)\in T^\perp.
\tag{3}
\]
On \(A\)-type facets the \(W_A\)-component of \(H\) has a strictly negative supporting sum, and on \(B\)-type facets the \(W_B\)-component has a strictly positive supporting sum. The radial boundary degree of \(H\) is therefore unchanged if all variable ranks are deformed linearly to any fixed interior ranks \(k_0,\ell_0\). For fixed ranks, (3) is a positive-weighted direct sum of the permutahedral prefix maps on \(P_a\) and \(P_b\), each of degree \(\pm1\) on its factor boundary. Their product has one zero with degree \(\pm1\), and hence the map \(H/\|H\|:\partial D\to S^{d-1}\) has degree \(\pm1\).

Finally consider the standard sphere fibration
\[
S^{d-1}\longrightarrow V_2(\mathbb R^{d+1})\longrightarrow S^d.
\]
Its long homotopy sequence gives
\[
\pi_d(S^d)\cong\mathbb Z
\xrightarrow{\ \partial\ }
\pi_{d-1}(S^{d-1})\cong\mathbb Z
\longrightarrow\pi_{d-1}(V_2)
\longrightarrow\pi_{d-1}(S^d)=0.
\]
The connecting map is multiplication by the Euler number of \(TS^d\), namely \(\chi(S^d)=1+(-1)^d\). Thus the image of the boundary fiber map of degree \(\pm1\) is a generator of the quotient group in (1). Since \(d\ge4\), the principal \(SO(2)\)-bundle \(V_2(W)\to\widetilde{\mathrm{Gr}}_2(W)\) induces an isomorphism on \(\pi_{d-1}\). The plane class is nonzero, proving nonextendibility. QED.

**Corollary 2 (unrestricted coloring application).** Suppose an unrestricted reversal-odd boundary 3-tournament has the property that, for every Hamilton order in the cell \(D(A|B)\), its first switch-prefix rank lies strictly inside \(A\), while its last switch-prefix rank lies strictly inside \(B\). The associated extreme-switch oriented plane labels possess the boundary interpolation of Theorem 1 and represent its nonzero homotopy class. This remains true when the switch ranks vary arbitrarily among the flags.

**Limitations and relation to the global obstruction.** This is a nonextendibility statement for a specified natural interpolation over one cell's boundary; other lower-dimensional fillings could alter its attaching class. It neither shows that every globally all-bad coloring has a straddling top cell nor rules out coherent alternative fillings over the full Coxeter sphere. The theorem upgrades the earlier contraction-degree obstruction: that degree is the integral fiber obstruction, whereas passage to the full oriented Grassmannian reduces it modulo the Euler number of the sphere tangent bundle.

##### Universal face signs for the complete quadratic switch bivector

Let \(n=a+b\), with \(a,b\ge2\), and let \(A\sqcup B=[n]\). The top dual Coxeter cell \(D=P_a\times P_b\) consists of the Hamilton orders \(\pi\) listing \(A\) before \(B\). Write \(Z_p(\pi)=\sum_{h\le p}e_{\pi_h}-(p/n)\mathbf1\in W\) and \(T=\mathbf1_A-(a/n)\mathbf1\).

**Lemma 1 (sign cone for every prefix wedge).** For any \(1\le p<q<n\), put \(H_{pq}=\iota_T(Z_p\wedge Z_q)\in T^\perp\). Let \(S\subsetneq A\) and \(R\subsetneq B\) be nonempty. On every order whose \(A\)-suborder begins with \(S\),
\[
\sum_{i\in S}(H_{pq})_i\le0.
\tag{1}
\]
On every order whose \(B\)-suborder begins with \(R\),
\[
\sum_{i\in R}(H_{pq})_i\ge0.
\tag{2}
\]
If \(p<a<q\), both inequalities are strict.

*Proof.* Decompose \(W=\mathbb RT\oplus W_A\oplus W_B\). For \(p<a\) write \(Z_p=(p/a)T+u_p\), with \(u_p\in W_A\) the centered first-\(p\)-subset indicator; for \(q>a\) write \(Z_q=((n-q)/b)T+v_{q-a}\), with \(v\in W_B\), and note \(Z_a=T\).

Fix \(S\subsetneq A\) of size \(s\), and define \(h_s(j)=\min(j,s)-js/a>0\) for \(1\le j<a\). If \(p<q<a\), then the sum over \(S\) in \(H_{pq}/\|T\|^2\) is
\[
\frac pa h_s(q)-\frac qa h_s(p)
=\frac{p\min(q,s)-q\min(p,s)}a\le0
\]
because \(\min(j,s)/j\) is nonincreasing. If \(p<a\le q\), the same sum is \(-((n-q)/b)h_s(p)<0\). If \(a\le p\), it vanishes. This proves (1).

Similarly fix \(R\subsetneq B\) of size \(t\), and put \(g_t(j)=\min(j,t)-jt/b\). For \(a<p<q\), write \(r=p-a\), \(s=q-a\). The sum over \(R\) in \(H_{pq}/\|T\|^2\) equals
\[
\frac{b-r}{b}g_t(s)-\frac{b-s}{b}g_t(r)\ge0,
\]
since \(g_t(j)/(b-j)\) is nondecreasing: it increases for \(j\le t\) and is constant thereafter. If \(p\le a<q\), that sum is \((p/a)g_t(q-a)>0\). Otherwise it vanishes. QED.

**Theorem 2 (unit degree of the full quadratic switch map).** For each vertex \(\pi\) of \(D\), select a set of ranks \(S_\pi\subseteq\{1,\ldots,n-1\}\) having at least one member below \(a\) and at least one above \(a\). Form
\[
\mathcal B(\pi)=\sum_{p<q,\ p,q\in S_\pi}Z_p(\pi)\wedge Z_q(\pi).
\]
The piecewise-affine interpolation of \(\iota_T\mathcal B(\pi)\) on \(\partial D\) never vanishes, and its radial normalization has degree \(\pm1\).

*Proof.* On a boundary facet from the \(A\)-factor, every pair contributes a nonpositive value to the supporting functional from Lemma 1; at least one selected pair crosses the cut and contributes strictly negatively. On a facet from the \(B\)-factor, every pair contributes nonnegatively and a crossing pair contributes strictly positively. Hence every boundary facet has all its vertex labels in a common strict open halfspace, proving zero-avoidance after affine interpolation.

Let \(E(\pi)=Z_{\min S_\pi}\wedge Z_{\max S_\pi}\). Its contracted labels satisfy the same strict inequalities, and by the variable-rank permutahedral product theorem their normalized boundary map has degree \(\pm1\). The straight-line homotopy between the contracted \(\mathcal B\) and \(E\) labels remains in the corresponding strict halfspace on every facet. Thus their degrees agree. QED.

**Corollary 3 (nonnegative pair weights).** The same conclusion holds for \(\sum_{p<q}w_{pq}Z_p\wedge Z_q\), with arbitrary nonnegative weights, provided at least one pair \(p<a<q\) has positive weight at each vertex.

This gives a color-sensitive degree theorem for the *entire* reversal-odd quadratic switch bivector, not merely its first-and-last-switch summand, whenever all flags of a two-block cell have switches on opposite sides of the block cut. It does not assert existence of a straddling cell for every coloring, nor supply coherent fillings across different top cells.
