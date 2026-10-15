# Projective face incidences and intrinsic flag rotation

# Projective face windows and intrinsic flag monodromy

Let \(P\subset\mathbb R^d\) be a simple convex polytope. For a nonbacktracking two-edge graph walk \(u,v,w\), the two incident edges at \(v\) lie in a unique two-dimensional face \(F(u,v,w)\). Let \([a]=\mathbb Ra\) be the unoriented line of a nonzero vector \(a\). Define the intrinsic incidence sets
\[
\mathscr I_1(P)=\{(E,[v-u]):E=uv\text{ an edge of }P\},
\tag{1}
\]
\[
\mathscr I_2(P)=\{
(F(u,v,w),[v-u],[w-v]):u,v,w\text{ nonbacktracking graph walk}
\}.
\tag{2}
\]
The order of the two direction lines in (2) is retained. Multiple two-edge walks can give one member of \(\mathscr I_2(P)\). For a maximal face flag \(\mathcal F\), its canonical complete basis walk \(v_0,\ldots,v_d\) supplies the color word
\[
\mathsf w_k(\mathcal F)=
\bigl(c(\Xi_k(v_j,\ldots,v_{j+k}))\bigr)_{j=0}^{d-k},
\qquad c:\mathscr I_k(P)\to\mathbb F_2,\quad k\in\{1,2\}.
\tag{3}
\]

**Theorem 1 (faithful local-incidence realization).**
(a) For the \(d\)-cube \(P=[0,1]^d\) and \(k=1\), (1) is canonically the undirected edge set, and (3) runs through all full antipodal geodesic edge-color words as the maximal flag varies. Under central inversion, \((E,[v-u])\) maps to its opposite edge with the same direction line. Thus all odd incidence colorings are the unrestricted NORI1 colorings.

(b) For a \(d\)-simplex with vertices \(e_a\), \(a\in V\), \(|V|=d+1\), and \(k=2\), the correspondence
\[
\boxed{(a,h,c)\longmapsto
(\operatorname{conv}\{e_a,e_h,e_c\},[e_h-e_a],[e_c-e_h])}
\tag{4}
\]
is a bijection between ordered triples of distinct vertices and \(\mathscr I_2(P)\). The words (3) are all Hamilton tight-path triple words. The natural incidence involution
\[
\rho(F,L_1,L_2)=(F,L_2,L_1)
\tag{5}
\]
corresponds to triple reversal. Thus every binary coloring odd under (5) is an arbitrary ordinary reversal-odd boundary 3-tournament.

*Proof.* For the cube, an edge and its direction line determine an undirected edge, and a maximal face flag selects every dimension once from an arbitrary root. For the simplex, distinct edges have distinct unoriented direction lines. Two edges of one triangular face share a unique middle vertex, and the order of their lines specifies the first and last vertex. This reconstructs the triple from (4); reversing the triple interchanges its two lines. Every Hamilton vertex ordering is the canonical walk of a maximal face flag. \(\square\)

**Theorem 2 (intrinsic flag rotation).** For every simple \(d\)-polytope, let \(r_j\), \(0\le j<d\), change only the \(j\)-face of a maximal flag to the other \(j\)-face between its adjacent ranks, using the bottom and top elements as usual. These operations are involutions satisfying
\[
r_ir_j=r_jr_i\quad(|i-j|\ge2).
\tag{6}
\]
Their product \(T=r_0r_1\cdots r_{d-1}\), acting successively on the right, has the following effects:
\[
\begin{aligned}
\text{simplex: }&(v_0,\ldots,v_d)\longmapsto(v_1,\ldots,v_d,v_0),\\
\text{cube: }&(x;i_1,\ldots,i_d)\longmapsto
(x\oplus e_{i_1};i_2,\ldots,i_d,i_1).
\end{aligned}
\tag{7}
\]

*Proof.* Thinness of rank-two intervals in a convex face lattice gives a unique alternative intermediate face at each rank, and changes at nonadjacent ranks commute. For a simplex, \(r_j\) exchanges the entries in positions \(j,j+1\) of its vertex order, hence the product rotates the first entry to the end. For the cube, \(r_0\) moves the root across the first edge, while \(r_j\) for \(j\ge1\) swaps the \(j\)-th and \((j+1)\)-st freed dimensions. Their successive application gives (7). \(\square\)

The previously specified Coxeter-parabolic stabilizers now arise from the incidence definitions: a simplex's first oriented two-edge observation is invariant under \(r_j\) for \(j\ge3\), while a cube's first undirected edge observation is invariant under \(r_0\) and \(r_j\) for \(j\ge2\). The common flag rotation is a product of canonical rank exchanges, independent of the reflection type.

**Opposition covariance and the proposed extension.** On the simplex's proper-face flag sphere, the complement involution reverses each maximal flag order and turns (4) into its reverse; the color word becomes complemented and reversed. On the cube's flag sphere, central inversion preserves the dimension order while complementing every edge color. More generally, call \((P,k,J,\rho)\) an *opposed projective-window system* when \(P\) is simple, \(k\in\{1,2\}\), \(J\) is a free involution of its flag sphere, \(\rho\) a free involution on \(\mathscr I_k(P)\), and applying \(J\) to a flag transforms its ordered windows by \(\rho\) with a fixed identity or reversed position order.

**Original unified assertion (refuted by the permutahedral construction below).** In every opposed projective-window system, every binary coloring \(c:\mathscr I_k(P)\to\mathbb F_2\) satisfying \(c(\rho I)=1-c(I)\) has a maximal face flag \(\mathcal F\) with
\[
\operatorname{sw}(\mathsf w_k(\mathcal F))\le1.
\tag{8}
\]
Theorem 1 shows that (8) would imply both unrestricted motivating conjectures, with no specific reflection group in its hypotheses. It also contains other simple polytopes, including centrally symmetric products and permutahedra when their incidence opposition is free. Theorem 2 gives a common exchange structure. The universal assertion (8) is false: the subsequent permutahedral counterexample theorem constructs opposed systems in arbitrarily large dimensions whose every complete path has an alternating observation word. The face-flag geometry and the two faithful specializations remain valid. A revised universal theorem requires an additional intrinsic condition.
