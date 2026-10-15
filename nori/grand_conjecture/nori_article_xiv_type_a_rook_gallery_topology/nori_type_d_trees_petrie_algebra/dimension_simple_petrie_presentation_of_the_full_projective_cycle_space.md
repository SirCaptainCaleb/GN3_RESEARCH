# Dimension-simple Petrie presentation of the full projective cycle space

# Dimension-simple Petrie presentation of the full projective cycle space

The full mod-two cycle space of the projective cube admits a presentation whose generators are all complete dimension-simple antipodal geodesics and whose basic exchanges are the boundaries of ordinary cubical squares. This removes repeated-dimension paths from the *unfiltered* chain-level generation problem. It does not preserve the switch grading and therefore does not prove unrestricted NORI1. The result extends the previously observed adjacent-square pivot law from individual type-D chamber books to every projective cubical one-cycle.

Let \(n\ge3\), let \(Y_n=\partial I^n/A\cong\mathbb RP^{n-1}\), and write \(G_n=Y_n^{(1)}=Q_n/A\) for its projective cube graph. Let \(\mathcal P_n\) be the set of \(2^{n-2}(n-1)!\) undirected Petrie cycles of \(Q_n\), viewed also as projective length-\(n\) loops. Every \(C\in\mathcal P_n\) is obtained by choosing a cube root \(x\), a permutation \(\pi\) of all \(n\) directions, and a full cube geodesic from \(x\) to \(\bar x\) following \(\pi\), then identifying antipodal endpoints and opposing halves. Its projective loop chain is denoted \([C]\in Z_1(G_n;\mathbb F_2)\).

Define the *Petrie exchange multigraph* \(\mathcal E_n\). Its vertices are \(\mathcal P_n\). An edge is any rooted adjacent-transposition event: choose a representative \((x,\pi)\), choose two consecutive entries \(i,j\) of \(\pi\), and compare the Petrie cycles \(C,C'\) obtained from \(\pi\) and from \(\pi\) with \(i,j\) exchanged. Label the event by the projective cube square \(\bar F\) based at the prefix vertex reached just before traversing \(i,j\). Multiple events giving the same pair of Petrie cycles are retained as separate multiedges, so their square labels are unambiguous.

**Theorem 1 (square-exchange identity).** Every edge \(a=(C,C';\bar F)\) of \(\mathcal E_n\) satisfies
\[
\boxed{[C]+[C']=\partial_2[\bar F]\quad\text{in }C_1(Y_n;\mathbb F_2).}
\tag{1}
\]
Conversely, for every projective cubical square \(\bar F\) there exists an exchange edge labeled by \(\bar F\). In particular every projective square boundary is the sum of **two complete dimension-simple Petrie loops**.

*Proof.* A rooted adjacent swap replaces the two-edge route across the cubical square \(F\) in directions \(i,j\) by its other two-edge route. All preceding and following full-geodesic edges coincide. Completing the two full paths antipodally replaces their opposite two-edge routes across \(AF\) as well. Therefore, upstairs in \(Q_n\), the symmetric difference of the two \(2n\)-cycle edge sets is \(\partial F+\partial(AF)\); after passage to the antipodal quotient this is \(\partial\bar F\), proving (1).

Conversely, choose a lift \(F\) of any projective square and one of its corners \(x\). Let its two free directions be \(i,j\), and choose any permutation \(\sigma\) of the remaining directions. The full geodesics from \(x\) with dimension words \((i,j,\sigma)\) and \((j,i,\sigma)\) differ by the required square swap, giving the desired labeled exchange edge. \(\square\)

**Theorem 2 (connectivity of the complete-geodesic exchange graph).** The Petrie exchange multigraph \(\mathcal E_n\) is connected for every \(n\ge3\). Thus any two undirected antipodal Petrie cycles can be joined by a finite sequence of adjacent dimension exchanges, all of whose intermediate cycles remain complete dimension-simple geodesic completions.

*Proof.* Fix a projective vertex \([v]\). Every Petrie loop containing \([v]\) has a full rooted-geodesic representative beginning at the chosen lift \(v\), in one of its two traversal orientations. Hence the Petrie cycles through \([v]\) are images of the set \(S_n\) of all dimension permutations under the map \(\pi\mapsto C(v;\pi)\). The adjacent transpositions generate \(S_n\), and each such transposition is an edge of \(\mathcal E_n\). Therefore the subgraph induced by the cycles through \([v]\) is connected.

If \([v],[w]\) are adjacent vertices of the connected graph \(G_n\), choose a lift of their edge and extend it by the remaining \(n-1\) distinct directions to a full geodesic. Its Petrie cycle contains both \([v]\) and \([w]\). Consequently the connected subgraphs formed by cycles through neighboring projective vertices intersect. Connectivity of \(G_n\) implies that the union of these subgraphs, which contains every Petrie cycle, is connected. \(\square\)

Let
\[
V_P=\mathbb F_2^{\mathcal P_n},\qquad
V_E=\mathbb F_2^{E(\mathcal E_n)}
\]
be the free spaces on Petrie cycles and labeled exchanges. Define
\[
\varepsilon:V_P\to Z_1(G_n;\mathbb F_2),\quad
\varepsilon(C)=[C],
\]
\[
d:V_E\to V_P,\quad d(C,C';\bar F)=C+C',
\qquad
q:V_E\to C_2(Y_n;\mathbb F_2),\quad q(C,C';\bar F)=[\bar F].
\tag{2}
\]

**Theorem 3 (surjective dimension-simple chain presentation).** The maps in (2) satisfy
\[
\boxed{\varepsilon d=\partial_2q,\qquad q(V_E)=C_2(Y_n;\mathbb F_2),}
\tag{3}
\]
and
\[
\boxed{\varepsilon(V_P)=Z_1(G_n;\mathbb F_2).}
\tag{4}
\]
Thus **every mod-two projective cube one-cycle is a sum of complete dimension-simple Petrie loops**, and the cubical boundary of every projective two-cell is lifted by a single adjacent-swap event.

*Proof.* Equation (3) follows from Theorem 1, including the surjectivity of \(q\) because every projective square arises from an exchange event. Hence the image of \(\varepsilon\) contains the entire boundary subspace
\(B_1(Y_n)=\operatorname{im}\partial_2\).

On the other hand, \(Y_n\cong\mathbb RP^{n-1}\) and \(H_1(Y_n;\mathbb F_2)\cong\mathbb F_2\). Every Petrie loop lifts to a geodesic beginning at \(x\) and ending at \(\bar x\), so its projection represents the nonzero homology class. Therefore the image of \(\varepsilon\) contains a representative of the unique nonzero homology class as well as every boundary. This proves (4). \(\square\)

**Corollary 4 (rank and relation module).** The projective cube graph has \(2^{n-1}\) vertices and \(n2^{n-2}\) edges. Therefore
\[
\boxed{
\operatorname{rank}\varepsilon
=\dim Z_1(G_n;\mathbb F_2)
=(n-2)2^{n-2}+1,
}
\tag{5}
\]
and
\[
\boxed{
\dim\ker\varepsilon
=2^{n-2}(n-1)!-(n-2)2^{n-2}-1.
}
\tag{6}
\]
Moreover,
\[
\boxed{
\ker\varepsilon
=d\bigl(q^{-1}(Z_2(Y_n;\mathbb F_2))\bigr).
}
\tag{7}
\]
In words, **every linear relation among complete Petrie loops can be realized by a family of adjacent-square exchanges whose total labeled square two-chain is a two-cycle**.

*Proof.* A connected graph with \(V\) vertices and \(E\) edges has cycle-space dimension \(E-V+1\), giving (5). The dimension of \(V_P\) gives (6). For (7), note that every Petrie loop has nonzero projective homology class, so a vector in \(\ker\varepsilon\) has even coefficient sum. Since \(\mathcal E_n\) is connected by Theorem 2, its incidence map \(d\) has image precisely the even-parity subspace of \(V_P\). Consequently any \(z\in\ker\varepsilon\) can be written \(z=d\alpha\). Then \(0=\varepsilon z=\partial_2q\alpha\), so \(q\alpha\in Z_2(Y_n)\). Conversely every \(\alpha\) with \(q\alpha\in Z_2(Y_n)\) has \(\varepsilon d\alpha=\partial_2q\alpha=0\) by (3). \(\square\)

**Corollary 5 (homologically trivial combinations admit square-exchange decompositions).** A mod-two sum of projective Petrie loops is nullhomologous precisely when it contains an even number of summands. For such a sum \(z\in V_P\), there exists a finite set of adjacent-square exchange events whose Petrie endpoints sum to \(z\). The sum of their projective square labels is a cubical two-chain bounding \(\varepsilon(z)\).

*Proof.* The homology class of the sum is the parity of its Petrie-loop summands times the nonzero class of \(H_1(Y_n)\). An even vector lies in \(\operatorname{im}d\) because the exchange graph is connected. If \(d\alpha=z\), then \(\partial_2q\alpha=\varepsilon z\) by Theorem 3. \(\square\)

**Significance for Wu--Yang and the remaining obstruction.** This is a constructive unfiltered chain framework whose one-dimensional generators are **all complete dimension-simple antipodal paths** and whose elementary differentials use only two distinct directions at a time. Its exchange multigraph connects every such witness, and the diagram (3) lifts the entire projective cubical two-cell boundary operation.

For a legal coloring \(c\), however, assigning each Petrie cycle its twisted switch grade defines a nontrivial filtration on the vertices of the exchange multigraph. Along an exchange event, the grade changes by at most one, but the exchange sequence in Theorem 2 need not remain below a prescribed grade. The rank-one wall example and grade-separated nonfillability in the preceding subsections show that this restriction matters: the surjective unfiltered diagram (3) need not admit an analogous filtered lift.

A potential next theorem would identify the homology or equivariant obstruction of the subgraph of exchanges among cycles of switch grade at most \(r\), particularly at \(r=0\). Establishing the requisite filtered connectivity or a support-sensitive chain homotopy would advance unrestricted NORI1 without ever introducing a repeated cube direction along an intermediate complete witness.


## Local-to-global integrability of cubical turn signatures

Let \(n\ge3\), \(G_n=Q_n/A\) be the folded cube, and \(d_v(i,j)\) a candidate binary switch at projective vertex \(v\) between the two incident edges in distinct directions \(i,j\).

**Theorem 6 (complete switch reconstruction).** The pattern \(d\) comes from an antipodally odd coloring of the original undirected cube edges if and only if:
\[
\begin{array}{ll}
\text{Triangle:}&d_v(i,j)+d_v(j,k)+d_v(k,i)=0
\quad\text{for all }v,\ i,j,k,\\
\text{Square:}&\displaystyle\sum_{v\in V(F)}d_v(i,j)=0
\quad\text{for every projective }ij\text{-square }F,\\
\text{Antipodal:}&\displaystyle\sum_{\tau\in T(C_0)}d(\tau)=1
\quad\text{for one fixed projective Petrie loop }C_0.
\end{array}
\tag{8}
\]
When these conditions hold, the coloring is unique up to global complementation. Every projective Petrie loop then contains an odd number of prescribed switches.

*Proof.* Fix one cube lift \(\widetilde v\) of each folded-cube vertex \(v\), and let \(\eta\) be the associated sheet-transition one-cochain on \(G_n\). It represents the nonzero class in \(H^1(\mathbb RP^{n-1};\mathbb F_2)\).

By the triangle conditions, choose local bits \(a_{v,i}\), unique up to adding a common bit at each \(v\), such that \(d_v(i,j)=a_{v,i}+a_{v,j}\). On each folded-cube edge \(e=vw\) in direction \(i\), put \(\mu(e)=a_{v,i}+a_{w,i}\). Changing the local reference bits modifies \(\mu\) by a coboundary. For a closed edge walk in \(G_n\), the sum of its turn bits is the evaluation of \(\mu\) on that walk, since each incident edge value occurs at both endpoints and the contributions regroup into \(\mu(e)\).

Thus each square equation is the cocycle equation \(\mu(\partial F)=0\). These square faces form the two-skeleton of \(Y_n=\partial I^n/A\cong\mathbb RP^{n-1}\). Their vanishing makes \(\mu\) a cocycle on \(Y_n\). Its first cohomology has order two, and any projective Petrie loop generates \(H_1(Y_n;\mathbb F_2)\). The one odd Petrie evaluation therefore yields \([\mu]=[\eta]\). Choose a function \(t\) on folded-cube vertices with \(\mu+\eta=\delta t\), and put \(b_{v,i}=a_{v,i}+t_v\). Then \(b_{v,i}+b_{w,i}=\eta(vw)\) on every direction-\(i\) edge \(vw\).

Define the color of the cube edge leaving lift \(\widetilde v\) in direction \(i\) as \(b_{v,i}\) and the color of its antipodal mate as \(1+b_{v,i}\). The last displayed identity makes the prescription consistent when the same edge is considered from its opposite endpoint. This gives a legal coloring inducing all the prescribed turns. Conversely, for any legal coloring the incident edge bits at chosen lifts provide such local \(a_{v,i}\), and their mismatch is \(\eta\), yielding all three conditions.

If two legal colorings have the same turn switches, at each projective vertex their incident edge colors differ by a common bit. Consistency along every folded-cube edge forces those bits equal on the connected graph \(G_n\), giving global complementation and no further ambiguity. \(\square\)

**Corollary 7 (Petrie-only global parity tests).** A turn pattern comes from a legal odd coloring if and only if it obeys the vertex triangle equations and its sum over **every** projective Petrie loop is one.

*Proof.* Under the triangle equations, projective turn sums along closed cube walks are evaluations of \(\mu\). The preceding Petrie-cycle presentation proves these loops span the full cycle space of \(G_n\). Agreement with the sheet cochain \(\eta\) on every spanning Petrie loop therefore implies \([\mu]=[\eta]\), giving the square and one-loop tests of Theorem 6. \(\square\)

**Theorem 8 (dimension of the realizable turn-code affine space).** There are \(2^{n-1}\binom n2\) projective turn variables, and the realizable switch signatures form an affine space of dimension
\[
\boxed{n2^{n-2}-1.}
\tag{9}
\]
Hence there are \(2^{n2^{n-2}-1}\) realizable turn signatures; each comes from two antipodally odd cube-edge colorings. The ranks of the independent homogeneous constraints are
\[
\boxed{
\mathrm{rk}(\text{vertex triangles})=2^{n-1}\binom{n-1}{2},
\qquad
\mathrm{rk}(\text{squares modulo triangles})=(n-2)2^{n-2}.
}
\tag{10}
\]
The remaining projective parity supplies one independent inhomogeneous constraint.

*Proof.* Each of the \(E=n2^{n-2}\) antipodal cube-edge orbits can be colored independently. Theorem 6 identifies only the pair of globally complementary choices, leaving dimension \(E-1\). At each folded-cube vertex, \(\binom n2\) local turns have \(n-1\) free bits after the triangle equations, giving the first rank. The folded-cube graph has \(V=2^{n-1}\) vertices and cycle-space dimension \(E-V+1\). Square boundaries span the nullhomologous subspace of dimension \(E-V\), since \(H_1(Y_n;\mathbb F_2)\) has dimension one. This gives the second rank and the final odd parity test. \(\square\)

**Theorem 9 (fundamental group of the turn two-complex).** Construct a two-dimensional CW complex \(X_n\) with one vertex for each projective cube edge; one edge for each projective turn; a triangular two-cell for every three incident cube edges at a projective vertex; and a square two-cell along the sequence of turns around every projective cube square. Then
\[
\boxed{\pi_1(X_n)\cong\mathbb Z/2,\qquad
H^1(X_n;\mathbb F_2)\cong\mathbb F_2.}
\tag{11}
\]
Its unique nonzero degree-one cohomology class is the realizable turn signature class.

*Proof.* With only vertex-star triangles attached, each projective cube vertex contributes the two-skeleton of a simplex on its incident edges. This complex is simply connected for \(n\ge3\). Distinct such complexes intersect at the vertices corresponding to shared projective cube edges; by van Kampen, replacing each one by an incidence star preserves the fundamental group. The resulting graph is a subdivision of \(G_n\). The remaining square two-cells impose the relations of the cubical projective square boundaries. Thus the new fundamental group is the fundamental group of the two-skeleton of \(Y_n\cong\mathbb RP^{n-1}\), namely \(\mathbb Z/2\). The cohomology and signature statement follow from Theorem 6. \(\square\)

**Research implication.** The switch variables are fully intrinsic. Local triangle and square compatibilities plus one antipodal parity test reconstruct every unrestricted legal coloring. The two-complex carries the prescribed projective first-cohomology class, but cannot by itself express the higher covering-index powers needed in the Smith-transfer route. That route requires higher turn-incidence cells respecting full dimension-simple Petrie witnesses, not further low-dimensional integrability conditions.



## A canonical one-switch signature and the cut-robust NORI1 formulation

The reconstruction theorem admits a particularly simple base point in its affine signature space. It gives a normalized switch-only problem involving cuts of the projective turn graph rather than arbitrary edge-color bits.

Choose distinct dimensions \(a,b\in[n]\). Define the cubical edge coloring
\[
\boxed{
c^0_d(x)=
\begin{cases}
x_b,&d=a,\\
x_a,&d\ne a,
\end{cases}}
\tag{12}
\]
where \(c^0_d(x)\) denotes the color of the undirected edge \(\{x,x\oplus e_d\}\). Each selected bit is different from \(x_d\), so the edge color is independent of the chosen endpoint; and all selected bits complement under \(x\mapsto\bar x\), proving antipodal oddness.

Write \(S_0\) for its switch signature on the projective turn graph \(\Lambda_n=L(Q_n/A)\). At a projective cube vertex \([x]\),
\[
\boxed{
S_0([x];i,j)=
\begin{cases}
x_a+x_b,&|\{i,j\}\cap\{a\}|=1,\\
0,&\text{otherwise},
\end{cases}}
\tag{13}
\]
with binary values interpreted modulo two. The expression \(x_a+x_b\) is invariant under antipodal inversion, so the rule is well defined.

**Theorem 10 (sharp minimum frustration and universal one-switch loops).** Every projective Petrie loop \(C\) contains precisely one active turn of \(S_0\). Consequently
\[
\boxed{
\min_{\text{legal }c}N_c=2^{n-2}(n-1),
}
\tag{14}
\]
where \(N_c=\sum_{[x]}s_x(n-s_x)\) counts all active projective turns. Equality in (14) holds for a legal coloring \(c\) if and only if **every** projective Petrie loop has precisely one active turn, or equivalently every projective Petrie loop contains a monochromatic antipodal half-geodesic.

*Proof.* In (13) an active turn must contain direction \(a\). Any Petrie loop uses a single edge in each dimension, and therefore has two turns incident with its unique direction-\(a\) edge. Their projective cube vertices differ by toggling \(a\), so \(x_a+x_b\) takes complementary values at the two endpoints, as \(a\ne b\). One of the two turns is active and the other inactive; every turn not incident with \(a\) is inactive. Hence every loop has one active turn.

For any legal coloring, the antipodal covering class forces every projective Petrie loop to have a positive odd number of active turns. Each projective turn belongs to \((n-2)!\) Petrie loops, and there are \(M_n=2^{n-2}(n-1)!\) loops. Counting loop--active-turn incidences gives
\((n-2)!N_c\ge M_n\), or \(N_c\ge2^{n-2}(n-1)\). The preceding construction attains this bound. Equality means the positive odd turn count is one on every loop. By the root-slide criterion, this is equivalent to a monochromatic antipodal half-geodesic within every loop. \(\square\)

**Theorem 11 (cut-robust one-switch form of unrestricted NORI1).** Let \(\Lambda_n=L(Q_n/A)\). For any \(U\subseteq V(\Lambda_n)\), write \(\partial U\subseteq E(\Lambda_n)\) for its binary graph cut. Every legal switch pattern is of the form
\[
\boxed{S_U=S_0\mathbin{\triangle}\partial U,}
\tag{15}
\]
where \(U\) is unique modulo complementation (the turn graph is connected). The unrestricted NORI1 conjecture is equivalent to
\[
\boxed{
\text{For every }U\subseteq V(\Lambda_n)
\text{ there is a Petrie loop }C\text{ with }
|T(C)\cap(S_0\triangle\partial U)|=1.}
\tag{16}
\]
No original edge-color variables occur in (16).

*Proof.* Theorem 6 identifies every legal switch pattern with the same nonzero class \(\alpha\in H^1(\Lambda_n;\mathbb F_2)\). In particular it differs from \(S_0\) by a one-coboundary, which is the cut of a vertex subset \(U\). The line graph of the connected cube is connected, and so is its antipodal quotient; its only zero cuts are \(U=\varnothing\) and \(U=V(\Lambda_n)\), giving uniqueness modulo complementation. The switch-one Petrie criterion is equivalent to NORI1, proving (16). \(\square\)

**Corollary 12 (cut-blocker necessary condition).** If a subset \(U\) violated the assertion (16), then for every Petrie loop \(C\), its cut \(\partial U\) would meet \(T(C)\) in at least two turns. If the cut met a particular \(C\) in precisely two turns, neither could be the distinguished unique \(S_0\)-turn on \(C\). More generally, letting
\[
t_0(C)=\text{the unique turn in }T(C)\cap S_0,\qquad
k_U(C)=|T(C)\cap\partial U|,
\]
one has
\[
\boxed{
|T(C)\cap S_U|=
\begin{cases}
k_U(C)+1,&t_0(C)\notin\partial U,\\
k_U(C)-1,&t_0(C)\in\partial U.
\end{cases}}
\tag{17}
\]
Here \(k_U(C)\) is even. A potential counterexample therefore requires \(k_U(C)\ge2\) on every Petrie loop and \(k_U(C)\ge4\) whenever \(t_0(C)\in\partial U\).

*Proof.* Every projective Petrie loop is a closed walk in \(\Lambda_n\), so it crosses every vertex cut an even number of times. The signature \(S_0\) contains one of its turns. Symmetric difference with the cut adds every other cut turn, but cancels the distinguished turn if that turn is included, yielding (17). Avoiding one-switch loops forces the displayed restrictions. \(\square\)

**Interpretation.** Formula (16) isolates the remaining existence problem from the construction of realizable switch signatures. All such signatures arise by cuts from an explicit perfect one-switch reference signature. The obstruction is now a cut \(U\) that crosses **every** special Petrie loop sufficiently often and in the correct positions to destroy its unique reference switch. This gives a direct structural replacement for deletion-based switch criticality: investigate subsets of projective cube edge-states under cut changes, with the three-turn Petrie square exchanges supplying the higher compatibility constraints.



## Rigidity of minimum Petrie transversals and a cut-distance obstruction

A set \(U\subseteq E(G_n)\) of projective cube edges is a *Petrie transversal* if it contains at least one edge of every projective dimension-simple Petrie loop. The vertices of the quotient turn graph \(\Lambda_n=L(G_n)\) are these same projective cube edges.

**Theorem 13 (sharp Petrie transversal size, with equality classification).** For every \(n\ge3\),
\[
\boxed{\min\{|U|:U\text{ meets every Petrie loop}\}=2^{n-2}.}
\tag{18}
\]
The only transversals attaining this cardinality are the \(n\) dimension classes
\[
\boxed{D_i=\{e\in E(G_n):\dim(e)=i\},\quad i\in[n].}
\tag{19}
\]
Thus the minimum hitting sets of all dimension-simple Petrie loops are rigid.

*Proof.* There are \(M_n=2^{n-2}(n-1)!\) projective Petrie loops, and each projective cube edge belongs to \((n-1)!\) loops, by symmetry or by counting \(M_n n\) loop--edge incidences. Hence a set meeting them all has cardinality at least \(M_n/(n-1)!=2^{n-2}\). Every dimension class \(D_i\) attains this bound because each loop traverses every dimension once.

Suppose equality holds. Every Petrie loop must meet \(U\) in precisely one edge. Therefore the incidence cochain \(u=\mathbf1_U\in C^1(G_n;\mathbb F_2)\) evaluates to one on every Petrie loop. These loops span the projective cube cycle space by Theorem 3, so \(u\) represents the nonzero covering class \(\alpha\). Fix one dimension \(a\) and let \(\mathbf1_{D_a}\) denote its direction-class cochain, which also represents \(\alpha\) because every Petrie loop uses direction \(a\) once. Thus
\[
u=\mathbf1_{D_a}+\delta f
\tag{20}
\]
for a binary vertex function \(f:V(G_n)\to\mathbb F_2\).

Lift \(f\) antipodally evenly to \(Q_n\), and define the binary Boolean function \(g(x)=x_a+f([x])\) on cube vertices. It is antipodally odd: \(g(\bar x)=1+g(x)\). On an edge in direction \(i\),
\[
g(x)+g(x\oplus e_i)=\mathbf1_{\{i=a\}}+f([x])+f([x\oplus e_i])
=u([x,x\oplus e_i]).
\tag{21}
\]
Consequently the number of cube edges on which \(g\) changes is \(2|U|=2^{n-1}\).

Put \(F(x)=(-1)^{g(x)}\), and expand it in Walsh characters
\(F=\sum_{S\subseteq[n]}\widehat F(S)\chi_S\).
Antipodal oddness removes the even-degree Fourier characters, including the constant. Parseval gives \(\sum_S\widehat F(S)^2=1\), while the total influence equals
\[
\sum_{i=1}^n\Pr_x(g(x)\ne g(x\oplus e_i))
=\sum_{S}|S|\widehat F(S)^2\ge1.
\tag{22}
\]
The edge-change cardinality \(2^{n-1}\) makes this an equality. Hence all Fourier weight lies in degree one:
\(F(x)=\sum_i a_i(-1)^{x_i}\).
As \(F(x)^2=1\) identically, the coefficient of every character \(\chi_{\{i,j\}}\) in its square vanishes, giving \(2a_i a_j=0\) whenever \(i\ne j\). Thus at most one \(a_i\) is nonzero, and Parseval makes that coefficient \(+1\) or \(-1\). Therefore \(g(x)=x_b+\text{constant}\) for some dimension \(b\). Equation (21) now says \(u(e)=1\) precisely on direction-\(b\) edges, proving \(U=D_b\). \(\square\)

**Theorem 14 (strict cut-distance barrier for hypothetical NORI1 counterexamples).** Fix distinct dimensions \(a,b\), and let \(c^0\) be the perfect one-switch reference coloring (12). Let \(c\) be any legal antipodally odd coloring, and let \(U\subseteq E(G_n)\) be the projective edge orbits on which \(c\) and \(c^0\) differ. If \(c\) has no monochromatic antipodal geodesic, then
\[
\boxed{2^{n-2}<|U|<n2^{n-2}-2^{n-2}.}
\tag{23}
\]
Equivalently every potential counterexample is at Hamming distance at least \(2^{n-2}+1\), modulo global complementation, from **every** canonical perfect one-switch coloring \(c^0\) of form (12).

*Proof.* Flipping the colors on edge orbits in \(U\) changes the projective turn signature by the graph cut \(\partial U\) in \(\Lambda_n\). If some Petrie loop contains no edge-state of \(U\), none of its turn switches changes, so it retains the unique switch of \(c^0\), giving a monochromatic antipodal half-geodesic after root sliding. Thus any hypothetical counterexample requires \(U\) to meet every Petrie loop. Theorem 13 implies \(|U|\ge2^{n-2}\).

If equality holds, Theorem 13 gives \(U=D_d\) for some dimension \(d\). When \(d=a\), every Petrie loop still has one active switch, since changing the color of all \(a\)-edges merely exchanges which endpoint of its unique \(a\)-edge carries the active turn. When \(d\ne a\), choose a projective Petrie loop whose dimensions \(a,d\) are consecutive and whose common vertex \(y\) satisfies \(y_a+y_b=1\) (possible by choosing a suitable root and placing the two dimensions first). If the unique original switch occurs at this shared turn, toggling all \(d\)-edges removes that switch and inserts one at the other endpoint of the \(d\)-edge, leaving one active turn. If instead \(d=b\), the same choice \(y_a+y_b=1\) is available. Thus equality always leaves a favorable loop and cannot occur in a counterexample.

Finally, complementing all colors globally replaces \(U\) by \(E(G_n)\setminus U\) and does not change any switch or monochromatic-path existence property. Apply the same lower bound to that complementary difference set to obtain the strict upper bound. \(\square\)

**Interpretation.** A minimum transversal of full dimension-simple Petrie loops is forced to be one complete direction class. This is a rigid equality theorem, not merely a counting lower bound. The cut formulation then places any hypothetical NORI1 counterexample strictly outside the Hamming neighborhoods of radius \(2^{n-2}\) surrounding all the perfect reference colorings. The obstruction is global and valid for arbitrary legal colorings, but does not rule out more distant cut perturbations.


Even-dimensional Petrie partition theorem. For even n, the projective cube group F2^n/<1> has an even-parity subgroup H of size 2^(n-2). Every Petrie cycle C has one edge of each direction, and the translates C+h over h in H partition the projective edge set. Proof: the translation stabilizer of a direction-i edge is {0,g_i}, disjoint from H. Therefore its H-orbit contains all 2^(n-2) direction-i edges without duplication. Since this holds for every direction, the translated cycles form an edge partition. For odd n, the projective cube has odd degree, so no cycle partition exists.

**Theorem (alternating perfect-matching model).** For even \(n\), let \(M_0,M_1\) be perfect matchings on the \(n\) dimension symbols, with their union one alternating Hamilton cycle. At every projective vertex of parity \(p\), pair incident cube edges as prescribed by \(M_p\). The resulting transition system partitions all graph edges into \(2^{n-2}\) length-\(n\) Petrie cycles. Conversely, every even-parity translation partition above has this form.

*Proof.* Moving along an edge reverses vertex parity. Thus successive direction symbols follow alternately \(M_0\) and \(M_1\), and traverse all \(n\) symbols once before repeating. Their sum in the projective vertex group is zero; no nonempty proper subset sums to zero. Hence each trajectory closes after \(n\) steps and is dimension-simple. The transition system covers all edges once by construction. For the converse, the incident dimension pairs at even and odd vertices of a given Petrie loop are alternating perfect matchings; even-parity translations propagate these pairings across each parity class. \(\square\)

For a legal edge coloring, let \(s_v(i,j)\) mark the switch at projective vertex \(v\). Put \(A_p(i,j)=\sum_{v:\,\mathrm{parity}(v)=p}s_v(i,j)\) and
\[
W(M_0,M_1)=\sum_{\{i,j\}\in M_0}A_0(i,j)+
\sum_{\{i,j\}\in M_1}A_1(i,j).
\]
**Corollary (Hamilton-matching certificate).** For the resulting Petrie partition \(\mathcal D\),
\[
W(M_0,M_1)=\sum_{C\in\mathcal D}(2h_c(C)+1).
\]
Therefore \(W<3\cdot2^{n-2}\) forces a monochromatic full geodesic. A hypothetical NORI1 counterexample must satisfy the reverse inequality for *every* alternating Hamilton matching pair. Averaging uniformly over these pairs gives
\[
\mathbb E W=\frac{N_c}{n-1},
\]
where \(N_c\) is the total number of active projective turns. This follows because each dimension pair is matched with probability \(1/(n-1)\) in each parity class. Thus at the old first-moment boundary \(N_c=3\cdot2^{n-2}(n-1)\), NORI1 follows unless all these matching weights are equal.

**Proposition (sharp limitation of the matching certificate already in \(Q_6\)).** Define the direction-\(d\) edge bit by \(c_d(x)=x_{r_d}+a_d\), where
\[
(r_0,\ldots,r_5)=(2,2,1,0,0,1),\qquad
(a_0,\ldots,a_5)=(0,1,0,0,1,1).
\]
This is a legal antipodally odd undirected edge coloring. It admits a monochromatic full geodesic from \(0\) with dimension word \((3,0,2,1,4,5)\). Nevertheless, **every** alternating Hamilton matching pair satisfies
\[
W_c(M_0,M_1)\ge48=3\cdot2^{6-2},
\]
so the preceding matching certificate cannot detect this favorable path.

*Proof.* Every reader direction \(r_d\) differs from \(d\), making each edge label independent of its chosen endpoint. Complementing all vertex bits complements the label, proving legality. Reading the displayed dimension word from \(0\) gives color word \(000000\).

The six direction-color signs at every vertex occur in three complementary pairs: the pair \((0,1)\) reads \(x_2\) and \(x_2+1\); the pair \((3,4)\) reads \(x_0\) and \(x_0+1\); and the pair \((2,5)\) reads \(x_1\) and \(x_1+1\). On each parity class of the projective cube there are 16 vertices. The two bits in each complementary pair disagree at all 16 vertices, while any two bits belonging to different reader pairs disagree at 8 vertices, since distinct input bits remain uniformly independent when the total six-bit parity is fixed. Thus each cost \(A_p(i,j)\) is either 8 or 16. Each Hamilton matching pair uses six matched pairs in all, so \(W_c\ge6\cdot8=48\). An alternating Hamilton matching pair avoiding all three complementary reader pairs exists, so the lower bound is attained. \(\square\)

The obstruction is methodological: the local matching sum can meet the bad-coloring threshold even when some constituent Petrie cycles have grade zero. Higher turn correlations or the equivariant chain index are needed to distinguish these cases.
