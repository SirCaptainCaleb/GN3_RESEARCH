# Folded-cube line graphs and local generation of binary dependencies

# Direction-deleted graphic restrictions and a binary contraction normal form

Let \(n\ge3\), and let \(G_n=Q_n/\langle\tau\rangle\) be the folded cube under antipodal complementation. Put \(H_n=L(G_n)\), with \(V_i\subseteq V(H_n)\) the vertices corresponding to cube-edge pairs of direction \(i\). Let \(M_n\) be the binary matroid on \(E(H_n)\) represented by the vertex-edge incidence matrix \(B\) of \(H_n\), augmented by a row \(a\) recording the monodromy of the cover \(L(Q_n)\to H_n\). In particular, the cycles of \(M_n\) are the even-degree subgraphs of \(H_n\) having zero covering monodromy.

Fix a direction \(s\), set \(U_s=V(H_n)\setminus V_s\), and write \(m=2^{n-2}=|V_s|\).

**Theorem 1 (direction-deleted graphic flat).** There is a canonical isomorphism, after choosing the coordinate-\(s\) zero layer,
\[
H_n[U_s]\cong L(Q_{n-1}).
\tag{1}
\]
The restriction of \(M_n\) to \(E(H_n[U_s])\) is the graphic cycle matroid of \(L(Q_{n-1})\), of rank
\[
(n-1)2^{n-2}-1.
\tag{2}
\]
Moreover, \(E(H_n[U_s])\) is a flat of \(M_n\). Its complement consists of \(2(n-1)m\) turns, partitioned into \(2m\) families of \(n-1\) turns according to the two endpoints of each direction-\(s\) edge of \(G_n\).

*Proof.* Every antipodal vertex pair of \(Q_n\) has a unique representative with coordinate \(s\) equal to zero. Deleting the direction-\(s\) edges from \(G_n\) identifies its remaining graph with \(Q_{n-1}\) on those representatives. Taking line graphs gives (1).

Every closed walk in this direction-deleted graph lifts to a closed walk in the layer \(x_s=0\) of \(Q_n\). Its covering monodromy is zero. Thus the extra row \(a\) of a matrix representing \(M_n\), restricted to \(E(H_n[U_s])\), lies in the cut space of the connected graph \(H_n[U_s]\). The matroid restriction is graphic, with rank \(|U_s|-1=(n-1)2^{n-2}-1\). Every turn outside this restriction has one endpoint in \(V_s\), so its incidence column has a nonzero entry in the corresponding \(V_s\)-row; all columns of the restriction vanish on that row. Such an outside column lies outside their span, proving flatness.

Each vertex \(v\in V_s\) represents an edge \(e_v\) of \(G_n\) in direction \(s\). At each endpoint of \(e_v\), there are \(n-1\) other incident edges, producing \(n-1\) distinct turns incident with \(v\). Since the direction-\(s\) edges of \(G_n\) form a matching, these are all turns outside the restriction. \(\square\)

**Theorem 2 (paired-column contraction).** Let \(T\) be any spanning tree of \(H_n[U_s]\). Contract \(T\) in \(M_n\) and delete the loops arising from \(E(H_n[U_s])\setminus T\). The remaining matroid has rank \(m+1\) and admits over \(\mathbb F_2\) the representation
\[
\boxed{\quad
\{\,e_v^{\,n-1},\ (e_v+z)^{\,n-1}:v\in V_s\,\}
\subseteq\mathbb F_2^{\,V_s}\oplus\mathbb F_2 z .
\quad}
\tag{3}
\]
Here \(e_v^{\,n-1}\) means \(n-1\) parallel copies of the standard vector \(e_v\). The first family represents turns at the endpoint of a selected cube-edge lift with \(s\)-coordinate zero; the second represents turns at its endpoint with \(s\)-coordinate one.

*Proof.* Choose a representative of each antipodal cube-edge pair: for any direction other than \(s\), take its unique edge lying in \(x_s=0\); for every direction-\(s\) pair, choose either one of its two cube edges. Define the reference coloring \(c_0\) to be zero on all selected representatives and one on their antipodes, and let \(a\) be its induced turn cochain on \(H_n\).

A turn between two directions other than \(s\) occurs in the layer \(x_s=0\), giving \(a=0\). A turn involving a direction-\(s\) edge has \(a=0\) when the two incident edges meet at the selected direction-\(s\) representative's endpoint in \(x_s=0\), and \(a=1\) at its endpoint in \(x_s=1\). Indeed, every non-\(s\) edge in the latter layer is antipodal to its selected representative. For the quotient turn, choosing the antipodal lift of both edges leaves their color difference unchanged.

Hence the matrix \(\left(\begin{smallmatrix}B\\a\end{smallmatrix}\right)\) has zero last entry on every edge of \(H_n[U_s]\). Contracting \(T\) identifies all its vertices into one incidence vertex. Deleting the redundant incidence row leaves the \(m\) rows indexed by \(V_s\), together with the monodromy row \(z\). A turn incident with \(v\in V_s\) has incidence vector \(e_v\), with monodromy entry zero or one according to the endpoint family. This gives (3). Every other edge of \(H_n[U_s]\) becomes a loop, since its incidence column belongs to the span of the tree columns and its monodromy entry is zero.

The \(m\) columns \(e_v\), together with any column \(e_v+z\), span \(\mathbb F_2^{m+1}\), proving the rank assertion. \(\square\)

**Corollary 3 (independence and four-element circuits).** Delete parallel copies in (3), and put \(P_v=\{e_v,e_v+z\}\) for every \(v\in V_s\). A set of columns is independent if and only if it contains both members of at most one \(P_v\). For distinct \(v,w\), the four columns of \(P_v\cup P_w\) form a circuit. Consequently \(M_n\) has, for each direction \(s\), a rank-\((2^{n-2}+1)\) minor on \(2^{n-1}\) elements represented by
\[
\begin{pmatrix}
I_m&I_m\\
0&\mathbf1^T
\end{pmatrix}.
\tag{4}
\]

*Proof.* In a linear relation among the columns in (3), the \(e_v\)-coordinate forces the two coefficients from each \(P_v\) to be equal. The \(z\)-coordinate then forces the number of fully selected pairs to be even. A nonzero relation therefore exists if and only if at least two complete pairs occur; any two complete pairs form a minimal relation. Deleting duplicate columns gives (4). \(\square\)

The contraction exhibits the covering monodromy as one shared binary degree of freedom across all direction-\(s\) pairs. The normal form holds for every antipodally odd edge coloring because \(M_n\) is independent of the coloring within its prescribed switching class. Direction-rainbow witnesses and integer turn weights remain additional data in applications to switch minimization.

## Hamilton direction-order theorem for universal pairwise turn compatibility

For legal antipodally odd edge coloring c_i(x) of Q_n define graph G on directions i in [n]. Distinct i,j are adjacent iff some cube vertex x has c_i(x)=c_j(x)=0, equivalently a red two-edge cube path uses i and j. Because antipodal translation exchanges all-red with all-blue incident pairs, ij is NOT adjacent iff c_i(x)=1-c_j(x) for all x. The pairwise compatibility graphs for red and blue coincide.

THEOREM. G has a Hamiltonian path for every n>=2, with no restrictions on nonlinear dependence and no need for balance. Proof: partition the direction functions into equivalence classes under c_i=c_j or c_i=1-c_j pointwise. Every class has one or two sign blocks; directions within each sign block are adjacent, directions in opposite blocks of the same class are not, and directions from different classes are adjacent. There are at least TWO equivalence classes, since if all c_i are sign variants of one common function f, then edge consistency forces f to ignore each bit i (one direction i occurs for every bit), contradicting oddness under complementation. List the equivalence classes with all two-block classes first. List their first sign blocks in this class order, then list their second sign blocks, if present, in the same order. Successive blocks are from distinct classes because at least two classes are present. Ordering members arbitrarily within each block produces a Hamiltonian path. Every consecutive direction pair in this order supports both a red two-edge geodesic and an antipodally translated blue two-edge geodesic; these local witnesses may have different roots.

HAMILTON-CYCLE BARRIER. For n>=4 choose nonempty disjoint A,B and a singleton t with A union B union {t}=[n] and |A|>=2. Fix a in A. Let c_i(x)=x_t for i in A, c_j(x)=1-x_t for j in B, and c_t(x)=x_a. This is legal and odd. G consists of cliques A and B linked through the universal vertex t; it has a cut vertex, so no Hamilton cycle. The Hamilton-path conclusion is appropriately sharp.

SPECTRAL FORM. Write sigma_i(x)=(-1)^(c_i(x)) and K_ij=E_x sigma_i(x)sigma_j(x). Oddness gives E sigma_i=0 and Pr[c_i=c_j=0]=(1+K_ij)/4. Hence the number of red common-incidence vertices is 2^(n-2)(1+K_ij). Missing ij corresponds to K_ij=-1. The matrix K is a PSD Gram matrix. For balanced colorings, K times the all-one vector vanishes, and G has minimum degree at least n/2-1 because a red i-edge at every vertex coexists with n/2-1 further red directions.

SCOPE. This is a full-dimensional pairwise direction-ordering theorem for every legal cube coloring. It does NOT prove a full monochromatic geodesic because the red two-edge path witnessing one adjacent pair may be incompatible with the path witnessing the next pair. Transferring complete-graph increasing paths or rainbow paths must enforce simultaneous intermediate cube states rather than merely pairwise direction adjacency.

## Balanced Hamilton cycle of locally monochromatic turns

For n>=4 even let c be any vertex-balanced antipodally odd edge coloring of Q_n, and let G be the graph on the n directions, with i,j adjacent if some cube vertex has simultaneous red incident i,j edges. Antipodal oddness proves that ij is missing precisely when the signed edge functions s_i(x)=(-1)^c_i(x), s_j(x) obey s_i=-s_j identically. Grouping rules up to global sign yields classes with one or two sign blocks, complete cliques within sign blocks and complete joins between distinct classes; the only missing edges join opposing blocks of the same class.

THEOREM. G has a Hamilton cycle for every such coloring, irrespective of nonlinear rule count. Indeed alpha(G)<=2: three pairwise missing edges would require three signed functions pairwise opposite, impossible. Also G is two-connected. If removing t disconnects it, all other n-1 vertices must belong to a single equivalence class with both sign blocks nonempty; otherwise complete joins between different classes retain connectivity after deletion. Let f denote their common signed rule, with a rules equal to f and b rules equal to -f, a+b=n-1. The pointwise balance identity reads (a-b)f+s_t=0, so a-b=+1 or -1 and s_t=-(a-b)f. Thus t also belongs to the same equivalence class. Consequently all direction rules are sign multiples of f. Since each direction's rule ignores its own bit, f ignores every bit and is constant, contradicting its antipodal oddness. This also excludes the case where G was disconnected initially. We conclude kappa(G)>=2. The Chvatal--Erdos Hamiltonicity criterion kappa>=alpha proves the statement.

The analogous blue-pair compatibility graph is the same G by antipodal translation, so this Hamilton cycle works simultaneously for red and blue local turns. The result improves the previous universal Hamilton-path theorem in the balanced counterexample-preserving class, but still does not certify one cube path realizing every consecutive pair: different local pairs can have inconsistent root states. It identifies rooted state synchronization as the obstruction left beyond the complete cyclic direction ordering.

## Polynomial-density Hamilton cycles from antipodal signs and Boolean Poincare

QUANTITATIVE HAMILTON CYCLE THEOREM. Let n>=4 even, and c be any vertex-balanced antipodally odd undirected edge coloring of Q_n. Write s_i(x)=(-1)^(c_i(x)) and for distinct directions i,j let p_ij=Pr_(uniform x)[s_i(x)=s_j(x)=+1]. Define G_theta on [n] by ij present if p_ij>=theta, where theta=1/(32n). Then G_theta has a Hamilton cycle. Consequently the n directions can be arranged cyclically so that EACH adjacent pair admits a red two-edge cube path at no fewer than 2^n/(32n) starting center vertices. The blue analogue follows by antipodal reflection. No bound on nonlinear rule complexity is assumed.

Proof. Antipodal oddness implies Pr[s_i=+1]=1/2 for every i. If three distinct directions i,j,k were pairwise nonadjacent in G_theta, the union bound with first two inclusion-exclusion terms would give
1>=Pr[any of i,j,k is red]>=3/2-p_ij-p_ik-p_jk>3/2-3theta>1,
a contradiction. Hence alpha(G_theta)<=2.

We prove G_theta has no articulation vertex. Suppose for some v the deletion G_theta-v is disconnected, and partition the remaining directions into two nonempty sets A,B with no cross edge. Then p_ij<theta for all i in A,j in B. Since antipodal inversion interchanges red-red with blue-blue, one has Pr[s_i=s_j]=2p_ij<2theta for all cross pairs. Choose i0 in A, j0 in B and set f=s_i0, an odd mean-zero sign function.

For every i in A, the triangle inequality for sign-disagreement gives Pr[s_i != f]<=Pr[s_i != -s_j0]+Pr[-s_j0 != f]<4theta, and for j in B we have Pr[s_j != -f]<2theta. Let a=|A|,b=|B|, a+b=n-1. The event E on which all these alignments hold has probability at least 1-4(n-1)theta>0. Pointwise vertex balance says sum_i s_i(x)=0. On E this becomes (a-b)f+s_v=0. Because a+b is odd, a-b is odd; since f and s_v are signs, E nonempty forces a-b=+1 or -1, and on E we have s_v=-(a-b)f. Thus for each direction i there exists a constant sign eta_i in {+1,-1} such that Pr[s_i != eta_i f]<=4theta when i !=v, and Pr[s_v != eta_v f]<=4(n-1)theta.

Each s_i is independent of bit i by edge consistency. Thus Boolean influence Inf_i(f)=Pr[f(x) != f(x xor e_i)] obeys Inf_i(f)<=2Pr[s_i != eta_i f], since the comparison at x and at its bit-i flip has the same distribution. Summing over i gives
sum_i Inf_i(f)<=2*(4(n-1)theta+4(n-1)theta)=16(n-1)theta<1.
But f is antipodally odd, hence mean zero and variance one. The Boolean Poincare inequality yields sum_i Inf_i(f)>=Var(f)=1, contradiction. Therefore G_theta-v remains connected for every v. With n>=4 this implies G_theta is 2-connected and kappa(G_theta)>=2.

Finally the Chvatal--Erdos Hamiltonicity theorem states that every graph with vertex connectivity at least its independence number is Hamiltonian. Apply kappa>=2>=alpha to G_theta.

SHARPNESS LIMIT OF CONSTANT DENSITY. In the majority-paired family recorded in note_74cf251b5aa0830cadf4d053, every cross pair between the two blocks of n/2 directions has witness density O(n^(-1/2)). Thus no replacement of theta=1/(32n) by a fixed positive constant is possible in this theorem. The bound may perhaps be improved as a function of n. The conclusion is a global cyclic order with individually many local two-step red witnesses, NOT a simultaneous root-consistent red full geodesic. A separate exchange or transport theorem is required to glue its witnesses.

## Exponential long-cycle packings and antipodal quotient circuit partitions

Let N=4h and m=N/2. In any antipodally odd balanced red-blue coloring of Q_N, both color subgraphs have even regular degree m. By Eoin Long's theorem, any cube subgraph of minimum degree d>=2 contains a simple cycle of length at least 2^d. Iteratively remove red simple cycles C_1,...,C_k, where k<=m/2. Every removal lowers each vertex degree by at most two, so before choosing C_j the red remainder has minimum degree at least m-2(j-1), giving |C_j|>=2^(m-2(j-1)). All residual degrees remain even, allowing an edge partition of the residual red graph into simple cycles. Apply the antipodal map to each red cycle to obtain a paired blue cycle decomposition. For every N>=8 divisible by four, take k=floor(N/8); then each color decomposition has k long pairwise edge-disjoint cycles of length at least 2^(N/4+2).

In the antipodally folded graph F_N=Q_N/<tau>, every quotient edge has one red and one blue lifted representative. Each red cycle projects to an edge-simple closed trail of trivial double-cover monodromy. The entire red cycle decomposition projects to an edge partition of F_N into such trails. Choosing blue cycles as antipodal red cycles makes paired red and blue cycles project to identical quotient trails. This is an intrinsic pair correspondence, whereas noncrossing/enclosure depends on an auxiliary surface embedding. Q_N is nonplanar for N>=4 because it has N*2^(N-1) edges, exceeding 2*2^N-4, the planar bipartite bound. Any orientable cellular embedding has genus at least 1+(N-4)*2^(N-3), by four-edge facial length and Euler's formula. In higher genus a simple curve need not enclose a region.

Long simple cycles do not automatically contain long direction-rainbow arcs: the standard binary-reflected Gray-code Hamiltonian cycle of Q_d has 2^d edges but uses one fixed direction every other edge, leaving no rainbow contiguous arc longer than three steps. A cycle length 2^(N/2) does imply that its direction support contains at least N/2 labels, because a t-direction subcube has 2^t vertices. These conclusions do not establish the n-o(n) monochromatic geodesic needed for NORI1.
