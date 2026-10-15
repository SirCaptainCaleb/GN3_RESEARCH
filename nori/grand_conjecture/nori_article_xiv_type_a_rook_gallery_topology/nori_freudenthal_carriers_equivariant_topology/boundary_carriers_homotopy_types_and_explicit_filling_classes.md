# Boundary carriers: homotopy types and explicit filling classes

# Boundary carriers: homotopy types and explicit filling classes

Let \(V=A\sqcup B\sqcup C\), where \(A,B,C\) are nonempty, and put
\[
p=|A|,\quad r=|B|,\quad q=|C|,\quad n=p+r+q\ge5,\qquad
W=\{z\in\mathbb R^V:\sum_{v\in V}z_v=0\}.
\]
For \(H\subseteq B\) and signs \(\sigma_h\in\{-1,1\}\), define
\[
\mathcal C(A,B,C;H,\sigma)=
\bigcup_{a\in A,\ c\in C}
\{z\in S(W):z_a=z_c=0,\ \sigma_hz_h\ge0\ (h\in H)\}.
\tag{1}
\]
These are the carriers used by the affine-dependence labels on Hamilton middle vertices. The sets \(A,C\) specify possible first and last vertices; \(B\) consists of vertices that are always middle vertices; \(H\) records their invariant colors.

## A complete carrier classification

**Theorem 1.** Carrier (1) has the following homotopy type.
\[
\begin{array}{c|c}
\text{condition}&\text{homotopy type}\\ \hline
H=\varnothing&
\displaystyle\bigvee^{(2^p-1)(2^q-1)}S^{n-4}\\
\varnothing\ne H\subsetneq B&\text{contractible}\\
H=B\text{ and both signs occur}&\text{contractible}\\
H=B\text{ and all signs agree},\ p+q>2&S^{p+q-3}\\
H=B\text{ and all signs agree},\ p=q=1&\varnothing.
\end{array}
\tag{2}
\]
In particular, the uncolored boundary carrier is \((n-5)\)-connected.

*Proof of the contractible cases.* Choose \(h\in H\). If \(B\setminus H\ne\varnothing\), choose \(k\) in that set; otherwise choose \(k\in H\) with \(\sigma_k=-\sigma_h\). The vector
\[
v=\sigma_h(e_h-e_k)/\sqrt2
\]
lies in every member of the union (1). Its prescribed entry at \(h\) is strictly positive, so \(-v\) lies in none of them. Normalized interpolation toward \(v\) contracts each member and the union simultaneously. All sign inequalities and both required zero entries persist along this interpolation.

*Proof when \(H=\varnothing\).* Fix \(b_0\in B\), and eliminate \(z_{b_0}\) using the equation defining \(W\). This gives a linear isomorphism
\[
W\cong\mathbb R^A\oplus\mathbb R^C\oplus\mathbb R^{B\setminus\{b_0\}}.
\]
Under it, the cone over (1) becomes
\[
U_p\times U_q\times\mathbb R^{r-1},
\qquad U_t=\{u\in\mathbb R^t:\text{some entry of }u\text{ is zero}\}.
\tag{3}
\]
An invertible linear map induces a homeomorphism of links by radial normalization. The link of a product of cones is the join of their links.

For \(t\ge2\), radial projection in the \(\ell^1\) norm identifies the link of \(U_t\) with the \((t-2)\)-skeleton of the boundary of the \(t\)-crosspolytope. This skeleton is \((t-3)\)-connected, and its reduced integral homology is concentrated in degree \(t-2\), with rank \(2^t-1\). Indeed, the relative cellular chains of the sphere and its skeleton have \(2^t\) generators in degree \(t-1\), and the sphere's fundamental class maps to a rank-one subgroup. The long homology sequence gives the stated rank and vanishing. For \(t=2\) the link consists of four points; for \(t=3\) it is a connected graph. In higher dimensions, the Hurewicz and Whitehead theorems identify the link with a wedge of \(2^t-1\) spheres of dimension \(t-2\). For \(t=1\), the factor \(U_1=\{0\}\) contributes no nonzero direction and is omitted from the join.

The free factor in (3), when nonzero, contributes \(S^{r-2}\). Joining the two crosspolytope skeletons and this sphere gives the first row of (2); joining wedges of spheres multiplies their multiplicities and adds their dimensions plus the join increments. The resulting dimension is \(n-4\). The same computation covers factors of dimension zero by omission.

*Proof when all of \(B\) has one sign.* By negation assume that sign is positive. Cover (1) by the subsets specified by the pair of required zero entries \((a,c)\). An intersection is determined by nonempty sets \(A_0\subseteq A,C_0\subseteq C\) of entries forced to vanish. If \(A_0=A\) and \(C_0=C\), all remaining entries lie in \(B\), are nonnegative, and sum to zero; the spherical intersection is empty. Otherwise choose \(k\in(A\setminus A_0)\cup(C\setminus C_0)\) and \(h\in B\). Normalized interpolation to \((e_h-e_k)/\sqrt2\) contracts the intersection. The finite polyhedral nerve lemma therefore identifies the carrier with the simplicial complex on \(A\times C\) whose simplices omit at least one row or at least one column.

Cover this nerve by the full simplices obtained by omitting a given row or column, discarding empty members. Their intersections are again simplices, and are nonempty precisely when the set of omitted rows is a proper subset of \(A\) and the omitted columns form a proper subset of \(C\). Their nerve is
\[
\partial\Delta_A*\partial\Delta_C\cong S^{p+q-3},
\]
with the empty boundary factor omitted when its set has one element. If \(p=q=1\), the original carrier is empty. This proves the remaining rows. The closed polyhedral covers used here admit common triangulations, so the polyhedral form of the nerve lemma applies. \(\square\)

## The complement is a complete bipartite graph

Write \(\mathcal C_0=\mathcal C(A,B,C;\varnothing,\varnothing)\), and let
\[
P_A=\{-1,1\}^A,\qquad P_C=\{-1,1\}^C.
\]

**Theorem 2.** There is an antipodally equivariant homotopy equivalence
\[
S(W)\setminus\mathcal C_0\simeq K_{P_A,P_C}=K_{2^p,2^q}.
\tag{4}
\]
The graph involution negates every sign in each of its two vertex classes.

*Proof.* A point lies outside \(\mathcal C_0\) precisely when every entry in \(A\) is nonzero or every entry in \(C\) is nonzero. Cover this complement by
\[
U_\alpha=\{z\in S(W):\operatorname{sgn}(z|_A)=\alpha\},
\qquad
T_\beta=\{z\in S(W):\operatorname{sgn}(z|_C)=\beta\}.
\]
Sets of the same kind with distinct sign vectors are disjoint. Every \(U_\alpha\cap T_\beta\) is nonempty: prescribe the signs and magnitudes on \(A\cup C\), and use an entry of the nonempty set \(B\) to make the total sum zero. Each set and each nonempty intersection is the spherical part of a convex cone with strict sign constraints. Choosing a point in the intersection and using normalized interpolation proves contractibility. The cover nerve is consequently the complete bipartite graph in (4).

Negation permutes the cover by \(\alpha\mapsto-\alpha,\beta\mapsto-\beta\). An invariant partition of unity and the equivariant good-cover construction give the equivariant equivalence. No graph vertex or edge is fixed by this involution. \(\square\)

For a finite set \(P\), let
\[
I_P=\ker\bigl(\mathbb Z^P\xrightarrow{\sum}\mathbb Z\bigr).
\]
Orient every graph edge from \(P_A\) to \(P_C\). A graph one-chain is an integer matrix \((t_{\alpha\beta})\); it is a cycle precisely when every row and every column sum is zero. Thus
\[
H_1(K_{P_A,P_C};\mathbb Z)=I_{P_A}\otimes I_{P_C}.
\tag{5}
\]
Choose \(\alpha_0\in P_A,\beta_0\in P_C\). A basis consists of the rectangle cycles
\[
R_{\alpha\beta}
=E_{\alpha\beta}-E_{\alpha\beta_0}
-E_{\alpha_0\beta}+E_{\alpha_0\beta_0},
\qquad \alpha\ne\alpha_0,\ \beta\ne\beta_0.
\tag{6}
\]
Alexander duality gives
\[
\widetilde H^{n-4}(\mathcal C_0;\mathbb Z)
\cong H_1(S(W)\setminus\mathcal C_0;\mathbb Z)
\cong I_{P_A}\otimes I_{P_C}.
\tag{7}
\]
The carrier is a finite polyhedral complex, so the compactness and local contractibility hypotheses of duality hold. Over \(\mathbb F_2\), this identification commutes with antipodality. Over the integers, naturality includes the ambient orientation sign \((-1)^{n-1}\). The duality used is the ordinary Alexander duality theorem, for example Hatcher, *Algebraic Topology*, Corollary 3.45, https://pi.math.cornell.edu/~Hatcher/AT/ATch3.pdf.

## Filling classes on full Hamilton residues

A closed dual type-A cell is specified by an ordered partition of \(V\) into consecutive nonempty blocks. Its flags independently permute the entries within each block. If the first and last blocks are \(A,C\), all other vertices form \(B\). The invariant middle-vertex colors give \(H,\sigma\), and the affine-dependence vertex labels lie in carrier (1). Passing to a face shrinks the endpoint sets and adds invariant middle-vertex constraints, so the corresponding carriers are nested.

**Proposition 3 (forced variation in a middle block).** If an interior position block has at least three vertices, none of its vertices belongs to \(H\). In particular, for a primary \((n-3)\)-cell with its three blocks \(A|B|C\), if \(|B|\ge3\), then \(H=\varnothing\).

*Proof.* For a specified \(h\) in such a block, choose distinct \(u,v\) in the same block. Two permissible internal orders contain the consecutive words \(u,h,v\) and \(v,h,u\). Their triples centered at \(h\) have complementary colors by reversal oddness. Thus \(h\)'s color is not invariant. A primary cell has three blocks because a residue with \(k\) blocks has dimension \(n-k\). \(\square\)

Let \(D\) be a primary cell with \(H=\varnothing\), and suppose a color-sensitive boundary assignment has already given
\[
f:\partial D\cong S^{n-4}\longrightarrow\mathcal C_0.
\tag{8}
\]
Let \(\xi_{\alpha\beta}\) be the cohomology classes corresponding to the rectangle basis (6) under (7).

**Corollary 4 (complete integral and chain filling tests).** For \(n\ge7\), map (8) extends continuously over \(D\) inside \(\mathcal C_0\) if and only if
\[
\left\langle f^*\xi_{\alpha\beta},[\,\partial D\,]\right\rangle=0
\quad\text{for every }\alpha\ne\alpha_0,\ \beta\ne\beta_0.
\tag{9}
\]
With coefficients in \(\mathbb F_2\), the corresponding vanishing conditions are necessary and sufficient for the image of the fundamental boundary cycle to bound a chain in \(\mathcal C_0\).

*Proof.* By Theorem 1 the carrier is \((n-5)\)-connected and homotopy equivalent to a wedge of \((n-4)\)-spheres. Hurewicz identifies \(\pi_{n-4}(\mathcal C_0)\) with \(H_{n-4}(\mathcal C_0;\mathbb Z)\). Consequently \(f\) is nullhomotopic precisely when its fundamental homology class vanishes. The integral cohomology basis in (7) detects this class, giving (9). A nullhomotopy is equivalent to a disk extension. Over \(\mathbb F_2\), a cycle bounds precisely when its homology class vanishes, and the reduced cohomology basis detects that class. Modulo-two vanishing alone does not imply continuous extendibility. \(\square\)

These tests apply to complete Hamilton residues in the unrestricted boundary class. They specify the color-sensitive cancellation problem by finitely many endpoint-sign rectangles. The labels on individual flags do not determine the boundary assignment (8); coherent choices over shared faces remain necessary.

The contractibility criterion in Theorem 1 is a statement about each carrier. Its condition need not be inherited by cell faces: an unconstrained middle vertex can acquire the same invariant sign as the other middle vertices. Therefore the new contractible cases may fill a cell when its prescribed boundary lies in that carrier, but do not by themselves enlarge the previously constructed global equivariant map. Likewise, a general extension into the larger sparse target need not remain inside \(\mathcal C_0\).

The affine-dependence label is common to the cube and boundary constructions. Its boundary placement identifies the higher filling groups and their complete bipartite complement. The following results determine the antipodally invariant part of those groups and its canonical chain-tower class.


## Antipodal norm classes and rectangles with opposite signs

Continue with \(\mathcal C_0\), and assume \(n\ge7\). Put \(d=n-4\), let \(Rz=-z\), and use coefficients in \(\mathbb F_2\) throughout this part. The induced involution on chains, homology and cohomology is also denoted \(R\); write \(N=1+R\). For a vector space \(M\) with involution, its quotient of invariant vectors by norm vectors is
\[
T(M)=\ker(N:M\to M)/\operatorname{im}(N:M\to M).
\tag{10}
\]
Since \(N^2=0\), the quotient is defined.

For \(\alpha\in P_A,\beta\in P_C\), let
\[
Q_{\alpha\beta}=
E_{\alpha\beta}+E_{-\alpha,\beta}
+E_{-\alpha,-\beta}+E_{\alpha,-\beta}
\tag{11}
\]
be the rectangle joining a sign pattern to its opposite in both graph parts. Denote its Alexander-dual class in \(H^d(\mathcal C_0;\mathbb F_2)\) by \(\xi_{\alpha\beta}\). Unlike the previously chosen rectangle basis, (11) is invariant under the graph involution. Modulo two, Alexander duality is equivariant, so \(R\xi_{\alpha\beta}=\xi_{\alpha\beta}\).

**Theorem 5 (one invariant class modulo norms).** The two vector spaces
\[
T\bigl(H^d(\mathcal C_0;\mathbb F_2)\bigr),
\qquad
T\bigl(H_d(\mathcal C_0;\mathbb F_2)\bigr)
\tag{12}
\]
have dimension one. Every class \(\xi_{\alpha\beta}\) from (11) represents the same nonzero element of the first space. Thus, among invariant top cohomology classes, there is one independent class after norm classes are removed.

*Proof.* For a finite set \(P\) with a fixed-point-free involution, let
\[
I_P=\ker\bigl(\mathbb F_2^P\xrightarrow{\sum}\mathbb F_2\bigr).
\]
Choose one representative \(a_j\) of each orbit, with \(a_0\) distinguished. In \(I_P\), the vector
\[
v_0=e_{a_0}+e_{Ra_0}
\]
is invariant. For every other orbit, put \(x_j=e_{a_j}+e_{a_0}\). The vectors
\[
v_0,\quad x_j,\quad Rx_j\quad(j\ne0)
\]
form a basis: entries at \(a_j,Ra_j\) give independence, and their number is \(|P|-1\). Consequently
\[
I_P\cong\mathbb F_2\oplus
\mathbb F_2[\mathbb Z_2]^{\,|P|/2-1}
\tag{13}
\]
as an involution module.

The cohomology module of the carrier is \(I_{P_A}\otimes I_{P_C}\), with the diagonal involution, by (7). A tensor product having one regular summand is regular; the tensor product of two regular two-dimensional summands is the direct sum of two regular summands, as seen by the two orbits of its four basis tensors. Hence this module has one trivial summand, generated by
\[
(e_\alpha+e_{-\alpha})\otimes(e_\beta+e_{-\beta}),
\tag{14}
\]
and all remaining summands are regular. A regular summand has equal invariant and norm subspaces, whereas the one-dimensional trivial summand has zero norm map. This proves the first dimension assertion and nonvanishing of (14).

Replacing \(\alpha\) by \(\alpha'\) changes its first factor by
\(N(e_\alpha+e_{\alpha'})\), where \(e_\alpha+e_{\alpha'}\in I_{P_A}\). Tensoring with the invariant second factor turns this change into a norm for the diagonal action. The same holds for \(\beta\). Formula (14) corresponds to (11), proving independence of the representatives. The homology module is dual to this finite-dimensional cohomology module. Duals of trivial and regular summands have the same types, giving the second dimension assertion. \(\square\)

## A fixed odd pairing on every antipodal sphere map

**Theorem 6 (the opposite-sign rectangle has unit parity).** For every odd continuous map
\[
f:S^d\longrightarrow\mathcal C_0,
\qquad f(-x)=-f(x),
\]
one has
\[
\boxed{\langle f^*\xi_{\alpha\beta},[S^d]\rangle=1}
\quad\text{for every }\alpha\in P_A,\ \beta\in P_C.
\tag{15}
\]

*Proof.* Choose \(a\in A,c\in C\), and consider the invariant sphere
\[
L=\{z\in S(W):z_a=z_c=0\}\cong S^d
\subseteq\mathcal C_0.
\tag{16}
\]
First compute the pairing for its inclusion \(i\). The complement of \(L\) has a four-sector good cover recording the sign of \(z_a\) or \(z_c\); its nerve is \(K_{2,2}\cong S^1\). The inclusion
\(S(W)\setminus\mathcal C_0\hookrightarrow S(W)\setminus L\)
induces the graph map
\[
P_A\ni\alpha\longmapsto\alpha_a,\qquad
P_C\ni\beta\longmapsto\beta_c.
\]
This follows directly from the sign-sector covers used in Theorem 2. It takes (11) to the four-edge fundamental cycle of \(K_{2,2}\). Naturality of Alexander duality therefore gives
\[
\langle i^*\xi_{\alpha\beta},[L]\rangle=1.
\tag{17}
\]

By Theorem 1, \(\mathcal C_0\) is \((d-1)\)-connected. The restrictions of \(f\) and \(i\) to an antipodal equatorial \(S^{d-1}\) are consequently equivariantly homotopic: construct a homotopy over a free cellular decomposition, extending through cells using the vanishing of homotopy groups through degree \(d-1\). The equivariant homotopy extension property allows us to modify \(f\) equivariantly so that it agrees with \(i\) on that equator.

Glue the two upper-hemisphere maps along their common boundary. They determine a class \(h\in H_d(\mathcal C_0;\mathbb F_2)\). The corresponding lower-hemisphere difference is \(Rh\). Thus
\[
f_*[S^d]+i_*[S^d]=Nh.
\tag{18}
\]
Since \(\xi_{\alpha\beta}\) is invariant, it pairs trivially with \(Nh\). Equations (17)--(18) yield (15). \(\square\)

This fixes the antipodal parity without selecting arbitrary lower-dimensional fillings. It does not reduce the integral single-cell tests (9) to one test: those tests concern ordinary disk fillings. The one-dimensional quotient (12) describes the invariant part that survives changes by antipodal norms.

## The final equation of a carrier chain tower

An antipodal chain tower of height \(d\) in \(\mathcal C_0\) consists of mod-two chains \(z_j\), \(0\le j\le d\), satisfying
\[
\varepsilon z_0=1,\qquad
\partial z_j=Nz_{j-1}\quad(1\le j\le d).
\tag{19}
\]
Use a finite invariant triangulation of the carrier. The sphere (16) supplies such a tower, for example by the fundamental chains of successive antipodal hemispheres in that sphere.

**Theorem 7 (a canonical final tower obstruction).** For every tower (19), the cycle \(Nz_d\) defines a class
\[
\Theta(\mathcal C_0)=[Nz_d]\pmod{N H_d(\mathcal C_0;\mathbb F_2)}
\in T\bigl(H_d(\mathcal C_0;\mathbb F_2)\bigr).
\tag{20}
\]
This class is independent of every chain choice in the tower, is the nonzero element of the one-dimensional space in (12), and satisfies
\[
\boxed{\langle\xi_{\alpha\beta},[Nz_d]\rangle=1.}
\tag{21}
\]
In particular, no choice of a height-\(d\) tower can be extended through degree \(d+1\).

*Proof.* The chain \(Nz_d\) is invariant and
\[
\partial Nz_d=N\partial z_d=N^2z_{d-1}=0.
\]
Take two towers \(z,z'\), and write \(\delta z_j=z_j+z'_j\). Since their zero-chains have the same odd augmentation and the carrier is connected, choose \(a_1\) with \(\partial a_1=\delta z_0\), and put \(a_0=0\). Inductively choose \(a_{j+1}\), for \(j<d\), with
\[
\delta z_j=\partial a_{j+1}+Na_j.
\tag{22}
\]
The chain \(\delta z_j+Na_j\) is a cycle, since its boundary is
\(N\delta z_{j-1}+N\partial a_j=0\) by the preceding instance of (22). Its class vanishes by the reduced homology vanishing through degree \(d-1\), proving the inductive choice.

At degree \(d\), the chain \(\eta=\delta z_d+Na_d\) is a cycle. Therefore
\[
N\delta z_d=N\eta,
\]
so the two classes in (20) differ by a norm homology class. This proves independence.

For the tower carried by (16), \(Nz_d\) is its fundamental sphere cycle. Equation (17) gives pairing one with every \(\xi_{\alpha\beta}\). Those invariant cohomology classes pair trivially with norms of homology classes, so independence yields (21) for every tower. Thus (20) is nonzero and, by Theorem 5, generates the quotient. A degree-\((d+1)\) chain whose boundary is \(Nz_d\) would make all the pairings zero, contradicting (21). \(\square\)

Theorem 7 gives an explicit higher-dimensional counterpart of the canonical second-stage obstruction in the Smith-transfer analysis: here the lower homology vanishes, every lower chain choice can be absorbed, and the surviving class is detected by the four-edge rectangle (11).


## Compatibility under changes of endpoint sets

Let \(A'\subseteq A,C'\subseteq C\) be nonempty, and put
\(B'=V\setminus(A'\cup C')\). The uncolored carriers have a natural invariant inclusion
\[
j:\mathcal C_0(A',B',C')\hookrightarrow\mathcal C_0(A,B,C).
\tag{23}
\]

**Theorem 8 (natural transport of the invariant class).** Under the cohomology identifications (7), the restriction \(j^*\) is induced by restricting endpoint sign patterns:
\[
\alpha\longmapsto\alpha|_{A'},\qquad
\beta\longmapsto\beta|_{C'}.
\tag{24}
\]
More explicitly, a cycle matrix is sent to the matrix obtained by summing its entries over fibers of these two restriction maps. In particular,
\[
j^*\xi_{\alpha\beta}
=\xi_{\alpha|_{A'},\,\beta|_{C'}}.
\tag{25}
\]
The maps on both top homology and top cohomology induce isomorphisms of the one-dimensional invariant quotients (12), and
\[
j_*\Theta\bigl(\mathcal C_0(A',B',C')\bigr)
=\Theta\bigl(\mathcal C_0(A,B,C)\bigr).
\tag{26}
\]

*Proof.* Requiring a zero entry in \(A'\) and in \(C'\) implies the corresponding requirements in \(A,C\), proving (23). Its complementary inclusion goes from the complement of the larger carrier to the complement of the smaller one. The sign-sector cover of the former refines that of the latter by (24). The induced nerve map is the complete bipartite graph map given by restriction of signs. Its map on one-chains sums cycle-matrix entries over the indicated fibers; all row and column sums remain zero.

Naturality of Alexander duality identifies that graph map with \(j^*\). Restriction on a nonempty set commutes with sign negation and keeps a sign pattern distinct from its negative. Thus (11) maps to the corresponding four-edge rectangle without collapse, giving (25). It induces a nonzero map, hence an isomorphism, between the one-dimensional cohomology quotients of Theorem 5.

The evaluation pairing between homology and cohomology descends to a perfect pairing on the invariant quotients. This can be checked on the module decomposition in Theorem 5: regular summands have zero quotient, and the remaining trivial summands pair perfectly. Naturality of evaluation and the cohomology isomorphism therefore give the homology isomorphism. Finally, (21) characterizes the nonzero homology quotient class by its pairing with the opposite-sign rectangle. Equations (21) and (25) yield (26). \(\square\)

**Corollary 9 (transport along endpoint rook moves).** For distinct \(a,c\in V\), let \(L_{a,c}\) be the sphere defined in (16). The nonzero invariant quotient classes of all these spheres, and of all uncolored carriers (1), are canonically identified through carrier inclusions. Changing either endpoint to a third vertex preserves the identified class; swapping the endpoint roles also preserves it. The resulting identification is independent of the chosen sequence of such changes.

*Proof.* If \(a'\notin\{a,c\}\), both \(L_{a,c}\) and \(L_{a',c}\) are subspaces of
\[
\mathcal C_0(\{a,a'\},\,V\setminus\{a,a',c\},\,\{c\}).
\]
Each inclusion induces an isomorphism by Theorem 8, giving the identification for a change of first endpoint. The analogous carrier handles changes of the last endpoint. Swapping \(A,C\) leaves the carrier unchanged and interchanges the two graph parts; modulo two this preserves (11). The graph of ordered distinct endpoint pairs under changes of one entry is connected: an unused third vertex permits exchanging the endpoint roles, and changing entries successively connects arbitrary pairs. Every general carrier contains \(L_{a,c}\) for \(a\in A,c\in C\). All the quotient spaces have dimension one over \(\mathbb F_2\), with the distinguished nonzero classes specified by Theorems 5 and 7. Every inclusion preserves these classes, and the only automorphism of such a one-dimensional space is the identity. Hence identifications along different walks agree. \(\square\)

The transport in Theorem 8 concerns the uncolored endpoint-zero conditions. A colored face carrier may have extra invariant-sign constraints and a different homotopy type, as shown in (2). No assertion that its homology quotient is the same is needed or made. Thus the theorem resolves transport of the distinguished class across the raw endpoint carriers while leaving the color-sensitive shared-face chains as a separate proof obligation.

For a primary Hamilton residue \(A|B|C\) and its reversed residue \(C|B|A\), the carrier \(\mathcal C_0\) is the same on both sides and opposition acts by negation. This provides the native setting for paired-face corrections. However, the two residues alone do not form the antipodal sphere required in Theorem 6; their shared-face assignments and their attachments to other residues still have to be constructed. The results identify the forced invariant class once an antipodal sphere or tower is carried by this common target. They do not assert that the coloring already supplies that sphere or tower, or that carriers for different endpoint partitions can be identified.

The next results incorporate fixed colors into this transport and identify the resulting relative classes.


## Opposed fixed-color carriers

Assume \(n\ge7\). Fix a nonempty \(H\subseteq B\), signs \(\sigma\), and write \(h=|H|\), \(d=n-4\). The carrier belonging to an opposed pair of Hamilton residues is
\[
U(H,\sigma)=
\mathcal C(A,B,C;H,\sigma)
\cup\mathcal C(A,B,C;H,-\sigma).
\tag{27}
\]
It is antipodally invariant. Its points have all their signed entries
\(\sigma_h z_h\), \(h\in H\), nonnegative, or all nonpositive. The intersection of the two pieces has every entry of \(H\) zero.

**Theorem 10 (homotopy type after paired color constraints).** Put \(M=(2^p-1)(2^q-1)\). The homotopy types are
\[
\begin{array}{c|c}
\text{condition}&U(H,\sigma)\\ \hline
H\subsetneq B&
\displaystyle\bigvee^{M}S^{n-h-3}\\
H=B,\ \sigma\text{ constant},\ p+q\ge3&
\displaystyle\bigvee^{M}S^{p+q-3}\\
H=B,\ \sigma\text{ constant},\ p=q=1&\varnothing\\
H=B,\ \sigma\text{ mixed},\ p+q\ge3&
\displaystyle\bigvee^{M-2}S^{p+q-3}\\
H=B,\ \sigma\text{ mixed},\ p=q=1&S^0.
\end{array}
\tag{28}
\]
A wedge of \(M\) zero-spheres denotes \(M+1\) points.

*Proof when \(H\subsetneq B\).* Choose \(b_0\in B\setminus H\). Define a linear projection \(P:W\to W\) by putting
\[
\lambda(z)=\frac1h\sum_{j\in H}\sigma_j z_j,\qquad
(Pz)_j=\lambda(z)\sigma_j\quad(j\in H),
\]
\[
(Pz)_{b_0}=z_{b_0}
+\sum_{j\in H}\bigl(z_j-\lambda(z)\sigma_j\bigr),
\tag{29}
\]
and retaining every other entry. This preserves the total sum and every entry in \(A\cup C\). On either of the two sign cones in (27), interpolation from \(z\) to \(Pz\) retains the same sign inequalities. If an entry of \(H\) is nonzero, \(\lambda\) has the strict sign of that cone, so no interpolation vector is zero. If every entry of \(H\) is zero, \(Pz=z\). Radial normalization therefore gives an odd strong deformation retraction onto the subspace where the \(H\)-entries are proportional to \(\sigma\).

After eliminating \(b_0\), the cone over this retracted space has the form
\[
U_p\times U_q\times\mathbb R^{\,|B\setminus H|},
\]
where \(U_p,U_q\) are the unions of entry hyperplanes in (3). Its link is an uncolored carrier with effective middle-set size \(|B\setminus H|+1\). The cone-link computation in Theorem 1 gives the first row of (28), including its zero-dimensional instances.

*Proof when \(H=B\) and \(\sigma\) is constant.* Negation of the common sign does not change (27). All entries of \(B\) are therefore either nonnegative or nonpositive. Choose \(b_0\in B\), replace its entry by \(\sum_{j\in B}z_j\), and replace the other \(B\)-entries by zero. This is a sum-preserving linear projection. The same normalized interpolation gives an odd strong deformation retraction onto the uncolored carrier with one middle entry. Its cone is \(U_p\times U_q\), giving the second row. If \(p=q=1\), the two endpoint entries must both vanish, and the same-sign middle entries sum to zero; the carrier is empty.

*Proof when \(H=B\) and \(\sigma\) is mixed.* Both constituent carriers are contractible by Theorem 1. Their intersection is
\[
J_{A,C}=\{z\in S(W_{A\cup C}):
\text{some entry in }A\text{ and some entry in }C\text{ vanish}\},
\]
where \(W_{A\cup C}\) imposes total sum zero. Since the inclusions are polyhedral cofibrations, their union is homotopy equivalent to the suspension of \(J_{A,C}\) when that intersection is nonempty; if it is empty, the union has two contractible components.

For \(p+q\ge4\), compute the reduced cohomology of \(J_{A,C}\) by Alexander duality in \(S(W_{A\cup C})\cong S^{p+q-2}\). Its complement has the sign-sector cover of Theorem 2, except that there is no unused entry to compensate the total sum. A sector pair is feasible precisely when its combined signs include a positive and a negative entry. Thus the nerve is
\[
G=K_{2^p,2^q}\setminus
\{E_{+,+},E_{-,-}\}.
\tag{30}
\]
Here \(+\) and \(-\) mean constant sign patterns in the respective sets. Every feasible intersection is contractible by normalized interpolation. The graph is connected for \(p+q\ge3\) and has cycle rank \(M-2\). Duality gives reduced integral homology of \(J_{A,C}\), concentrated in degree \(p+q-4\), free of rank \(M-2\). The homology assertion follows also from the cohomology form of duality and the universal coefficient theorem, since the finite complex has no other cohomology or torsion.

If \(p+q=4\), the intersection consists of \(M-1\) points, and its suspension is a wedge of \(M-2\) circles. If \(p+q\ge5\), the intersection is connected; its suspension is simply connected and has reduced homology only in degree \(p+q-3\). Hurewicz and Whitehead identify that suspension with the stated wedge of spheres. For \(p+q\le3\), the intersection is empty. The union then has the homotopy type \(S^0\), agreeing with the remaining rows of (28). \(\square\)

**Theorem 11 (index and the two-sign vanishing threshold).** Every nonempty space in (28) admits an odd map to \(S^m\) and contains an odd embedded \(S^m\), where
\[
m=
\begin{cases}
n-h-3,&H\subsetneq B,\\
p+q-3,&H=B,\ \sigma\text{ constant},\ p+q\ge3,\\
\max(0,p+q-3),&H=B,\ \sigma\text{ mixed}.
\end{cases}
\tag{31}
\]
Its least possible odd-sphere target dimension is therefore \(m\), and its covering class has nonzero \(m\)-th power and zero \((m+1)\)-st power.

For \(h=1\), one has \(U(H,\sigma)=\mathcal C_0\). For \(h\ge2\), the opposite-sign rectangle class satisfies
\[
\boxed{\xi_{\alpha\beta}|_{U(H,\sigma)}=0
\quad\text{in }H^d(U(H,\sigma);\mathbb F_2).}
\tag{32}
\]

*Proof.* In the first two cases, the odd deformation retractions above land in effective uncolored carriers of dimension \(m\). Their invariant polyhedral structures admit odd maps to \(S^m\): assign to a face of dimension \(j\) an arbitrarily chosen sign times the \((j+1)\)-st crosspolytope vertex, with opposite signs on opposite faces, and extend over the barycentric subdivision. Distinct faces in a chain have distinct dimensions. Setting one specified \(A\)-entry and one specified \(C\)-entry to zero in the effective ambient subspace gives an odd embedded \(S^m\).

In the mixed case with \(p+q\ge4\), the intersection \(J_{A,C}\) has an invariant cell structure of dimension \(m-1\), hence an odd map to \(S^{m-1}\) by the same face-dimension labeling. Extend this map over the positive-sign carrier into the contractible upper hemisphere of \(S^m\). Extend over its opposite by negation. The prescriptions agree on the intersection, giving an odd map on the union. When the intersection is empty, mapping the two pieces to opposite points gives an odd map to \(S^0\).

For the matching embedded sphere, choose a nonzero vector \(v\) supported in \(B\), with total sum zero and strict signs \(\sigma\); such a vector exists since both signs occur. For fixed \(a\in A,c\in C\), the subspace
\[
\{z\in\mathbb R^{A\cup C}:
\sum z_j=0,\ z_a=z_c=0\}\oplus\mathbb Rv
\]
has its unit sphere inside (27). Its dimension is \(m\) when \(p+q\ge3\); when \(p=q=1\), the two points \(\pm v/\|v\|\) give \(S^0\). The embedded antipodal sphere supplies the lower bound on the covering power; the odd map supplies the upper bound.

A single real entry always has one of its two weak signs, proving \(U(H,\sigma)=\mathcal C_0\) when \(h=1\). For \(h\ge2\), every nonempty row of (28) has homotopy dimension at most \(d-1\), because \(n\ge7\). Thus \(H^d(U;\mathbb F_2)=0\), proving (32). The empty case gives the same vanishing. \(\square\)

## Two fixed signs transgress the rectangle class

The vanishing in (32) has a distinction at \(h=2\): the absolute rectangle class has relative lifts, but none of those lifts is antipodally invariant.

**Theorem 12 (the relative norm extension at two signs).** Suppose \(h=2\), set \(U=U(H,\sigma)\), and use mod-two coefficients. There is an equivariant sequence with each kernel equal to the preceding image
\[
0\longrightarrow H^{d-1}(U)
\xrightarrow{\delta}H^d(\mathcal C_0,U)
\xrightarrow{\rho}H^d(\mathcal C_0)
\longrightarrow0.
\tag{33}
\]
The module \(H^d(\mathcal C_0,U)\) is a direct sum of regular involution modules. Its regular rank is \(M\), except when \(H=B\) and \(\sigma\) is mixed, when its regular rank is \(M-1\). In particular its invariant quotient modulo norms is zero.

For every opposite-sign rectangle class \(\xi=\xi_{\alpha\beta}\), and every lift \(\widetilde\xi\) through \(\rho\), define
\[
\kappa(\xi)=
\delta^{-1}(N\widetilde\xi)
\pmod{N H^{d-1}(U)}.
\tag{34}
\]
This is well-defined, independent of the lift and of \(\alpha,\beta\), and generates
\[
T(H^{d-1}(U))\cong\mathbb F_2.
\tag{35}
\]
Consequently \(\xi\) has no invariant relative lift.

*Proof.* The carrier \(\mathcal C_0\) has zero degree-\((d-1)\) cohomology. Theorem 10 gives zero degree-\(d\) cohomology for \(U\). The cohomology sequence of the pair yields (33).

We first show that no invariant lift of \(\xi\) exists. Restrict the pair to the invariant sphere \(L_{a,c}\cong S^d\) of (16). The two linear entries specified by \(H\) are independent on its ambient subspace: at least one other entry remains available to enforce total sum zero. After a linear change of variables and radial normalization,
\[
L_{a,c}\cap U=\{x\in S^d:x_1x_2\ge0\},
\]
where multiplying the two entries by their prescribed signs is included in the change of variables. Its complement has two open spherical sectors, each an open \(d\)-ball, exchanged by antipodality. Collapsing the intersection gives a wedge of two \(d\)-spheres with those spheres exchanged. Therefore the relative group
\[
H^d(L_{a,c},L_{a,c}\cap U)
\]
is a regular two-dimensional module; its map to \(H^d(L_{a,c})\cong\mathbb F_2\) sums the two entries. Every invariant vector has zero image. But Theorem 6 gives \(\xi|_{L_{a,c}}\ne0\). Naturality of relative restriction therefore rules out an invariant lift in (33).

For the first two cases of (28) at \(h=2\), the equivariant projection identifies \(H^{d-1}(U)\) with the top cohomology of an effective uncolored carrier. Its module has one trivial summand and regular remaining summands, by the proof of Theorem 5. In the mixed case \(H=B\), Mayer–Vietoris identifies it equivariantly, modulo two, with the top cohomology of \(J_{A,C}\), and duality identifies that group with \(H_1(G;\mathbb F_2)\) for the graph (30).

For completeness, the first homology of any connected free involution graph has one trivial summand and regular remaining summands. Its augmented cellular chain sequence
\[
0\to H_1(G)\to C_1(G)\to C_0(G)\to\mathbb F_2\to0
\]
has regular middle modules. Applying the two-periodic complex with differential \(N\) to its two short sequences identifies \(T(H_1(G))\) with \(T(\mathbb F_2)\cong\mathbb F_2\), since regular modules have zero \(N\)-homology. Every finite involution module in characteristic two splits into trivial blocks and regular blocks, by the Jordan form of \(N\), where \(N^2=0\). Thus there is one trivial block. This proves (35) in all cases.

Since \(\xi\) is invariant, \(N\widetilde\xi\) belongs to \(\ker\rho=\operatorname{im}\delta\). Its preimage is invariant because \(\delta\) is injective. Changing the lift by \(\delta a\) changes that preimage by \(Na\), so (34) is independent of the lift. If (34) were zero, changing the lift by such a \(\delta a\) would make it invariant, contrary to the restriction argument. Thus it generates (35). Changing \(\xi\) by a norm \(Nb\) changes a lift by \(N\widetilde b\), whose norm is zero. Theorem 5 therefore makes (34) independent of the rectangle representatives.

Finally write the left and right modules of (33) as a trivial summand plus regular summands. A regular summand in the quotient can be lifted as a regular pair \(x,Nx\), splitting it off. For the remaining trivial quotient, choose its lift \(u\). The nonzero class (34) allows a change of \(u\) by an element of the kernel so that \(Nu\) is its distinguished trivial generator. These two vectors form one regular summand, and the remaining kernel summands are regular. Thus the middle module is entirely regular. Its dimension is \(2M\) in the first two cases of (28) and \(2M-2\) in the mixed case, giving the asserted ranks. \(\square\)

This is a color-sensitive transgression: two fixed middle signs annihilate the absolute top class on the paired carrier, while its relative lift acquires the nonzero degree-\((d-1)\) norm obstruction (34). Selecting opposite fillings independently cannot remove this class.

## Three fixed signs give natural relative lifts

**Theorem 13 (unique relative transport with at least three signs).** If \(h\ge3\), then
\[
\boxed{H^d(\mathcal C_0,U(H,\sigma))
\xrightarrow{\ \rho\ }H^d(\mathcal C_0)}
\tag{36}
\]
is an equivariant isomorphism. Each opposite-sign rectangle class has a unique relative lift, which is invariant and represents the nonzero invariant quotient modulo norms.

These lifts commute with shared-face inclusions. More precisely, suppose
\(A'\subseteq A,C'\subseteq C\), \(H\subseteq H'\subseteq B'\), the signs agree on \(H\), and both \(h,|H'|\ge3\). Then the carrier inclusion from Theorem 8 is an inclusion of pairs, and its relative pullback sends the unique lift of \(\xi_{\alpha\beta}\) to the unique lift of
\(\xi_{\alpha|_{A'},\,\beta|_{C'}}\).

*Proof.* By (28), \(U(H,\sigma)\) has zero cohomology in degrees \(d-1,d\) when \(h\ge3\), including the empty and zero-dimensional cases. The sequence of the pair gives (36). Equivariance and uniqueness make the lift invariant and identify its invariant quotient with that in Theorem 5.

Stronger endpoint-zero conditions and stronger consistent sign constraints give
\[
U(H',\sigma')\subseteq U(H,\sigma)
\]
under the inclusion of the raw carriers. Thus there is a map of pairs. The ordinary and relative restriction maps commute. Theorem 8 identifies the absolute class after restriction, and the isomorphism (36) on the smaller carrier identifies its relative lift uniquely. \(\square\)

For Hamilton residues these hypotheses come directly from face incidence: possible endpoint sets shrink, invariant middle-vertex sets grow, and their signs persist. Hence Theorem 13 supplies compatible colored relative cohomology classes on every face chain having at least three invariant middle vertices. At two vertices, Theorem 12 specifies the missing lower-degree correction.

## The same threshold for cube affine-word labels

Let
\[
L_n=\{z\in\mathbb R^n:\sum_i z_i=0,\ \sum_i iz_i=0\},
\qquad D=n-3,
\]
and consider the affine-dependence cube labels in \(S(L_n)\cong S^D\). Fix \(H\subseteq[n]\), \(1\le h=|H|\le n-2\), and prescribed signs \(\sigma\). Define
\[
V(H,\sigma)=
S(L_n)\cap\left(
\{\sigma_i z_i\ge0\ (i\in H)\}
\cup
\{\sigma_i z_i\le0\ (i\in H)\}
\right).
\tag{37}
\]

**Theorem 14 (paired positional constraints).** The space (37) has an odd strong deformation retraction onto a linear sphere
\[
\boxed{S^{D-h+1}=S^{n-h-2}.}
\tag{38}
\]
For \(h=1\) it is the entire sphere \(S(L_n)\). For \(h\ge2\) the fundamental degree-\(D\) cohomology class restricts to zero on it. At \(h=2\), its relative lift has the nonzero norm transgression of Theorem 12, with one regular two-dimensional relative module. At \(h\ge3\), the relative lift is unique and invariant.

*Proof.* Choose distinct \(a,b\notin H\). Replace \(z_i\), \(i\in H\), by
\(\lambda(z)\sigma_i\), where \(\lambda=h^{-1}\sum_{i\in H}\sigma_i z_i\). Adjust only the entries \(a,b\) to restore the two defining equations of \(L_n\). There is a unique linear adjustment, since
\[
\begin{pmatrix}1&1\\a&b\end{pmatrix}
\]
is nonsingular. Retain every other entry. This gives a linear projection onto the subspace of \(L_n\) where the \(H\)-entries lie on the line \(\mathbb R\sigma\). On either sign cone, normalized interpolation to the projection never vanishes: if any \(H\)-entry is nonzero, its signed sum has the strict cone sign and the projected \(H\)-vector is nonzero; otherwise the projection fixes the point.

Prescribing arbitrary entries on \(H\) is possible in \(L_n\) by solving for \(a,b\). Therefore the projected subspace has dimension
\((n-2)-(h-1)=n-h-1\), and its unit sphere gives (38). The one-sign equality and the cohomology vanishing follow.

For two signs, their entry functionals are independent on \(L_n\). The complement of (37) has the same two opposite open sectors used in Theorem 12. Its relative top cohomology is a regular two-dimensional module, whose invariant part maps to zero in the absolute top class. The cohomology sequence
\[
0\to H^{D-1}(V)\to H^D(S(L_n),V)
\to H^D(S(L_n))\to0
\]
therefore has the nonzero norm transgression between its one-dimensional trivial end modules. For at least three signs, (38) has dimension at most \(D-2\), and the relative-to-absolute map in degree \(D\) is an equivariant isomorphism. \(\square\)

For \(h=n-1\) or \(h=n\), assume the first sign cone contains a vector with every prescribed signed entry strictly positive. Each sign cone then contracts by normalized interpolation to that vector or its negative. Their intersection has all \(H\)-entries zero and at most one remaining entry, so both moment equations force it to be empty. Consequently \(V(H,\sigma)\simeq S^0\), and its degree-\(D\) relative lift is again unique and invariant. In the complete-path application, strict feasibility is supplied by any affine-dependence label of a flag in the cell. Thus the same one-, two-, and three-sign distinctions cover all nonempty constant-position families of bad words.

If a cube source cell has \(h\) constant color positions, its affine-dependence labels lie in the first sign cone of (37), and the antipodal cell's labels lie in the other. For boundary residues, the same statement holds after placing the coefficients on the invariant middle vertices, giving (27). Thus the two-sign transgression and the three-sign relative normalization apply to both original complete-path constructions through their existing labels.

These statements concern relative cohomology and the paired color carriers. They preserve every source flag's dimension-simple cube geodesic or vertex-simple Hamilton path. Constructing compatible chain representatives, particularly the lower-degree corrections at two fixed signs and the attachments of cells with no fixed signs, remains necessary for a full color-sensitive Wu–Yang transfer.

Both full existence conjectures remain open.
