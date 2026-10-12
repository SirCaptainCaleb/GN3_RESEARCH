## Codimension-two face induction and corresponding endpoints

### Inductive low-switch endpoint coincidence in adjacent codimension-two faces

#### Objective

Let \(c:E(Q_n)\to\{0,1\}\) satisfy \(c(\bar e)=1-c(e)\). Let \(\sigma(P)\) count the switches on a geodesic \(P\), and put
\[
\mu(c)=\min\{\sigma(P):P\text{ is a long geodesic in }Q_n\}.
\]
A long geodesic in a face traverses all of that face's free coordinate directions. The proposed program aims to prove \(\mu(c)\le 2\) in every dimension by induction.

Fix exterior directions \(a,b\), an \((n-2)\)-face \(F\), and its adjacent face \(F^a\). Seek long low-switch geodesics \(P\subset F\), \(Q\subset F^a\) terminating at *corresponding vertices* \(x,x^a\). The required structural advance is to **produce corresponding endpoints**; the final step follows from Article VIII.

#### Proven gluing input

Theorem 10 in Article VIII (*Penultimate-Length Extension and Parallel-Face Endpoint Exclusion*) gives, if \(P,Q\) have respectively \(r,s\) switches,
\[
\mu(c)\le \max\{r,2\lceil s/2\rceil\}.
\]
By interchanging the faces,
\[
\mu(c)\le \min\left\{\max(r,2\lceil s/2\rceil),\max(s,2\lceil r/2\rceil)\right\}. \tag{X.1}
\]
Thus two long geodesics with at most two switches in adjacent codimension-two faces and corresponding terminal vertices force \(\mu(c)\le 2\). The terminal-square proof is preserved in Article VIII.

#### Induction problem

**Candidate inductive step.** Starting with a single antipodally odd coloring of \(Q_n\), find adjacent codimension-two faces \(F,F^a\) carrying long geodesics of at most two switches with corresponding terminal vertices. Combining this assertion with (X.1) establishes the global two-switch bound.

Induction requires care: the restriction of an antipodally odd coloring to an individual face can be an arbitrary edge coloring and need not inherit antipodal oddness relative to that face. A successful induction should therefore strengthen the maintained hypothesis or work simultaneously with a family of parallel face restrictions. One may organize potential long-path endpoints by their minimum switch count and seek a corresponding pair through a geometric or topological intersection argument.

The endpoint-alignment claim is an open research target. No assertion about independently colored arbitrary faces is assumed here. The principal task is to exploit the coupled constraints inherited from the common ambient antipodally odd coloring.

#### Status

**Established:** the dimension-independent parallel-face switch bound (X.1), with proof in Article VIII. **Open:** a mechanism furnishing low-switch long geodesics terminating at corresponding vertices in adjacent codimension-two faces. This is the proposed route to the universal estimate \(\mu(c)\le2\).

### Corresponding-switch crossover and odd-defect cancellation

Let \(c:E(Q_n)\to\{0,1\}\) be an antipodally odd coloring of undirected cube edges, \(n\ge4\). Fix exterior directions \(a,b\) and adjacent codimension-two faces \(F,F^a\) with common free-coordinate set \(D=[n]\setminus\{a,b\}\). Let \(P\subset F\), \(Q\subset F^a\) span their faces and terminate at corresponding vertices \(x,x^a\). Both paths start at corresponding vertices \(u,u^a\), since each uses every coordinate in \(D\). For any edge-colored geodesic \(T\), denote its number of changes by \(\sigma(T)\). Put \(\mu(c)=\min\{\sigma(R):R\text{ is a full antipodal geodesic}\}\).

**Lemma 1 (penultimate completion).** Every \((n-1)\)-edge geodesic \(T\) with \(t\) changes gives
\[
\mu(c)\le 2\lceil t/2\rceil. \tag{1}
\]

*Proof.* Its unused-direction edges at the initial and final vertices are antipodal, so their colors differ. When \(t\) is even, the initial and final colors of \(T\) agree and one of prepending or appending the unused edge preserves \(t\). When \(t\) is odd, either extension has at most \(t+1\) changes. Each extension is a full antipodal geodesic. \(\square\)

**Theorem 2 (interior crossover).** Suppose \(w\) is interior to \(P\) and the corresponding vertex \(w^a\) is interior to \(Q\). Decompose \(P=P_-P_+\) at \(w\) and \(Q=Q_-Q_+\) at \(w^a\). Set \(h=c(ww^a)\). Denote the last colors of \(P_-,Q_-\) by \(\lambda_P,\lambda_Q\), and the first colors of \(P_+,Q_+\) by \(\rho_P,\rho_Q\). Then both inequalities hold:
\[
\begin{aligned}
\mu(c)&\le 2\left\lceil
\frac{\sigma(P_-)+\sigma(Q_+)+[\lambda_P\ne h]+[h\ne\rho_Q]}{2}
\right\rceil,\\
\mu(c)&\le 2\left\lceil
\frac{\sigma(Q_-)+\sigma(P_+)+[\lambda_Q\ne h]+[h\ne\rho_P]}{2}
\right\rceil.
\end{aligned}\tag{2}
\]

*Proof.* The prefixes \(P_-\) and \(Q_-\) use the same coordinate set \(S\subset D\), because their starting vertices correspond and their endpoints correspond. Each suffix uses \(D\setminus S\). The paths
\[
P_-\, (ww^a)\, Q_+,\qquad
Q_-\, (w^aw)\, P_+
\]
therefore traverse every direction in \(D\cup\{a\}\) once and omit only direction \(b\). Their change counts are the expressions inside the ceiling operations in (2), prior to division by two. Apply Lemma 1. \(\square\)

**Corollary 3 (balanced opposite-phase switches).** Suppose both paths switch at \(w,w^a\), in opposite phases:
\[
(\lambda_P,\rho_P)=(z,1-z),\qquad
(\lambda_Q,\rho_Q)=(1-z,z). \tag{3}
\]
Let \(r=\sigma(P)\), \(s=\sigma(Q)\), \(i=\sigma(P_-)\), \(j=\sigma(Q_-)\). Then
\[
\mu(c)\le
\begin{cases}
2\lceil(s-1+i-j)/2\rceil,&h=z,\\
2\lceil(r-1+j-i)/2\rceil,&h=1-z.
\end{cases}\tag{4}
\]
When \(i=j\),
\[
\boxed{\mu(c)\le 2\left\lceil\frac{\max\{r,s\}-1}{2}\right\rceil.}\tag{5}
\]
In particular, when \(r=s=k\) is odd and the two opposite-phase switches have equal numbers of preceding changes,
\[
\boxed{\mu(c)\le k-1.}\tag{6}
\]
Thus matched opposite-phase three-switch geodesics force \(\mu(c)\le2\), while the one-switch case forces \(\mu(c)=0\). The two direction orders may differ on both sides of \(w\); the common intermediate vertex and the balanced change counts are sufficient.

*Proof.* If \(h=z\), the first crossover in Theorem 2 introduces no change at either junction. Since \(Q\) switches at \(w^a\), its suffix has \(s-j-1\) internal changes, giving the first branch of (4). If \(h=1-z\), the second crossover introduces no junction changes and its suffix has \(r-i-1\) changes. If \(i=j\), either branch implies (5); for odd \(k\), the latter becomes \(k-1\). \(\square\)

An improvement for odd switch counts is also available without a corresponding interior vertex.

**Proposition 4 (terminal-square alternative).** Suppose \(P,Q\) each have an odd number \(k\) of changes, and their final colors \(p,q\) differ. Label the four edges of the square at \(x\) by
\[
A=c(xx^a),\quad B=c(xx^b),\quad
C=c(x^ax^{ab}),\quad H=c(x^bx^{ab}).
\]
Then either \(\mu(c)\le k-1\), or the square colors alternate:
\[
\boxed{A=H\ne B=C.}\tag{7}
\]
Moreover, (7) is the sole square coloring that prevents the terminal-square completion argument itself from reducing the bound to \(k-1\).

*Proof.* Apply antipodal reversal to \(P\) and \(Q\): reverse their antipodal images. These geodesics terminate at \(x^{ab},x^b\), respectively. Because their switch count \(k\) is odd, their last colors are \(p,q\), respectively. Thus there are four face-spanning paths terminating at the four corners, with last colors \(p,q,p,q\) in cyclic order. If any of
\[
A=C=p,\qquad B=H=p,\qquad A=B=q,\qquad C=H=q \tag{8}
\]
holds, append the indicated monochromatic two-edge square route to its compatible face path. The resulting full geodesic has \(k\) changes. Since \(k\) is odd, root rotation across any change gives a full geodesic with \(k-1\) changes.

For the remaining case, swap color names so that \(p=0,q=1\), and suppose none of (8) holds. Necessarily \(A\ne B\): if both are 1, the third equality in (8) holds; if both are 0, avoiding \(B=H=0\) forces \(H=1\), avoiding \(C=H=1\) forces \(C=0\), and then \(A=C=0\). The symmetric argument gives \(C\ne H\). Also \(A\ne C\), since \(A=C=0\) is forbidden, while \(A=C=1\), together with \(A\ne B\) and \(C\ne H\), would force \(B=H=0\). These inequalities give \(A=H\) and \(B=C=1-A\), establishing (7). Conversely, an alternating square satisfies none of (8). \(\square\)

Theorem 2 exploits a common intermediate vertex, Corollary 3 cancels a synchronized opposite-phase switch, and Proposition 4 characterizes the remaining terminal-square pattern when two odd-switch paths have different final colors. No endpoint-coincidence or synchronized-interior-switch existence claim is assumed.

### Extremal exterior-cube rigidity and terminal phase separation

Let \(c:E(Q_n)\to\mathbb F_2\) be an undirected-edge coloring satisfying \(c(\bar e)=1\oplus c(e)\). Let \(F\) be a \(k\)-face, \(1\le k<n\), and let \(T\) be its set of \(t=n-k\) fixed coordinate directions. A geodesic spanning \(F\) traverses all its free directions once. Write \(\sigma(P)\) for the number of changes in the edge-color word of \(P\), and \(\mu(c)\) for the least number of changes on a full antipodal geodesic in \(Q_n\). If \(x\in F\) and \(S\subseteq T\), write \(x^S\) for the vertex obtained by flipping precisely the coordinates of \(S\).

**Lemma 1 (parity reduction).** The number \(\mu(c)\) is even.

*Proof.* If a full geodesic has direction order \(i_1,\ldots,i_n\) and color word \(w_1,\ldots,w_n\), rotate its first direction to the end and move its root across the first edge. The new word is \(w_2,\ldots,w_n,1\oplus w_1\): all intermediate edges are unchanged, and the new last edge is antipodal to the old first edge. If the original word has an odd number of changes, then \(w_n=1\oplus w_1\). The rotation removes the comparison between \(w_1,w_2\) and introduces no change at the new last comparison. Rotate past an initial constant run and then past its first change. This decreases the switch count by one, contradicting minimality if \(\mu(c)\) were odd. \(\square\)

**Theorem 2 (exterior completion and phase separation).** Let \(P\subset F\) span \(F\), terminate at \(x\), have \(r=\sigma(P)\) changes, and have last edge color \(p\).

1. One has
   \[
   \mu(c)\le 2\left\lfloor\frac{r+t}{2}\right\rfloor. \tag{1}
   \]
2. Suppose another geodesic \(Q\subset F\) spans \(F\), terminates at the same \(x\), has at most \(r\) changes, and has last edge color \(1\oplus p\). Then
   \[
   \mu(c)\le 2\left\lfloor\frac{r+t-1}{2}\right\rfloor. \tag{2}
   \]
3. If \(\mu(c)\ge r+t\), the entire \(t\)-cube generated by \(T\) at \(x\) has the following edge coloring:
   \[
   c\bigl(\{x^S,x^{S\cup\{i\}}\}\bigr)
      =1\oplus p\oplus (|S|\bmod 2),
   \quad S\subsetneq T,\ i\in T\setminus S. \tag{3}
   \]
   In particular, every exterior edge whose nearer endpoint is at distance \(j\) from \(x\) has color \(1\oplus p\oplus(j\bmod2)\). This conclusion does not require any symmetry condition on the restriction of \(c\) to \(F\).

*Proof.* Append to \(P\) any permutation of the \(t\) exterior directions. The result is a full antipodal geodesic with at most \(r+t\) changes, proving (1) by Lemma 1. For part 2, choose one exterior geodesic \(W\) from \(x\) using \(T\). The first color of \(W\) agrees with the last color of either \(P\) or \(Q\). Append \(W\) to that path: the seam contributes zero changes, \(W\) contributes at most \(t-1\), and the face path contributes at most \(r\). Lemma 1 yields (2).

For part 3, every completion of \(P\) has at most \(r+t\) changes and, by the hypothesis on \(\mu(c)\), has at least \(r+t\). Each of the \(t\) new comparisons, including the seam after \(P\), must therefore be a change. Consequently every exterior geodesic starting at \(x\) has color word
\[
(1\oplus p),p,(1\oplus p),p,\ldots
\]
in its traversal order. Given any \(S\subsetneq T\) and \(i\in T\setminus S\), choose an exterior direction order that first traverses \(S\) and then \(i\). The edge in direction \(i\) appears in position \(|S|+1\) and so has the color asserted in (3). Every edge of the exterior cube occurs this way. \(\square\)

**Corollary 3 (two sufficient terminal-phase certificates).** Each of the following configurations forces \(\mu(c)\le2\):

(a) A codimension-two face contains two spanning geodesics with at most two changes each, terminating at the same vertex and with different final edge colors.

(b) A codimension-three face contains two spanning geodesics with at most one change each, terminating at the same vertex and with different final edge colors.

*Proof.* Apply (2) with \((r,t)=(2,2)\) or \((1,3)\), respectively. In both cases the upper bound is \(2\). \(\square\)

**Corollary 4 (local rigidity under a four-switch obstruction).** Suppose \(\mu(c)\ge4\).

(a) Every codimension-two face has no spanning geodesic with fewer than two changes. If a spanning geodesic with two changes terminates at \(x\) with final color \(p\), its exterior square has both edges incident with \(x\) colored \(1\oplus p\) and both edges incident with \(x^T\) colored \(p\). At each such terminal vertex, the final color of all spanning geodesics with at most two changes is uniquely determined.

(b) Every codimension-three face has no monochromatic spanning geodesic. If a one-change spanning geodesic terminates at \(x\) with final color \(p\), its exterior three-cube is rank-alternating, with colors \(1\oplus p,p,1\oplus p\) on edges leaving ranks \(0,1,2\) from \(x\). At each such terminal vertex, the final color of all spanning geodesics with at most one change is uniquely determined.

*Proof.* For part (a), a face path with at most one change would give \(\mu(c)\le2\) by (1), and a two-change path satisfies \(r+t=4\), so (3) applies. Different terminal phases would contradict Corollary 3(a). The same argument with \(t=3\) proves (b): a monochromatic face path extends to at most three changes, while a one-change path satisfies \(r+t=4\). The uniqueness follows from Corollary 3(b). \(\square\)

**Corollary 5 (dimension reduction for a hypothetical counterexample).** If an antipodally odd coloring of \(Q_n\) has \(\mu(c)\ge4\), then the restriction to **every** codimension-two face is an arbitrary edge coloring of \(Q_{n-2}\) with no spanning antipodal geodesic having at most one change. Consequently, whenever every arbitrary edge coloring of \(Q_m\) has a spanning antipodal geodesic with at most one change, all antipodally odd colorings of \(Q_{m+2}\) satisfy \(\mu(c)\le2\).

In particular, the established arbitrary-color one-change geodesic theorem for \(Q_7\) gives
\[
\boxed{\mu(c)\le2\quad\text{for every antipodally odd coloring of }Q_9.} \tag{4}
\]
The \(Q_7\) theorem follows from the verified geodesic antipodal-color theorem in \(Q_8\) by Leader and Long's dimension-reduction implication (Kirchweger, Peitl, Subercaseaux and Szeider, 2025; Leader and Long, 2014).

*Proof.* The first assertion is Corollary 4(a), applied to every codimension-two face. Its contrapositive gives the dimension-reduction implication. Apply it with \(m=7\) for (4). \(\square\)

The phase certificates concern two paths in the **same** face, whereas the terminal-coincidence program considers paths in adjacent faces. In a hypothetical coloring with \(\mu(c)\ge4\), both mechanisms impose additional compatible constraints: low-switch terminal phases are unique inside each face, and their prescribed exterior squares or three-cubes must agree on every shared edge. Obtaining a contradiction from these constraints across varying faces remains open.

### Quadratic independence of antipodal-geodesic color profiles

Let \(n\ge2\), and write \(x^i=x\oplus e_i\) and \(\bar x=x\oplus\mathbf1\) for vertices of \(Q_n\). Let \(c_i(x)\in\mathbb F_2\) be the color of the undirected edge \(\{x,x^i\}\), with
\[
c_i(x^i)=c_i(x),\qquad c_i(\bar x)=1+c_i(x).
\tag{1}
\]
For a long geodesic \(P\), define \(w(P)\in\mathbb F_2^n\) by letting \(w_i(P)\) be the color of its unique edge in direction \(i\). Thus the coordinates of \(w(P)\) are indexed by directions, regardless of traversal order. Put
\[
\mathcal W(c)=\{w(P):P\text{ is a long geodesic in }Q_n\}.
\]

**Theorem 1 (quadratic independence).** Suppose a multilinear polynomial
\[
q(Y)=a_0+\sum_{i=1}^n b_iY_i+
       \sum_{1\le i<j\le n}a_{ij}Y_iY_j
\quad\text{over }\mathbb F_2
\tag{2}
\]
vanishes at every \(w\in\mathcal W(c)\). Then every coefficient in (2) is zero.

Equivalently, every nonconstant Boolean polynomial of degree at most two assumes both values on \(\mathcal W(c)\). The coloring in (1) may have arbitrary nonlinear dependence on its exterior coordinates.

We use a consequence of constant geodesic integrals which requires no antipodal condition on the edge weights.

**Lemma 2 (constant antipodal integrals).** Let \(D\) be a nonempty coordinate set, and give each undirected edge of \(Q_D\) a weight \(\omega(e)\in\mathbb F_2\). Suppose the sum of the edge weights on every long geodesic is the same constant \(\kappa\), independently of its root and coordinate order. Then every square has weight sum zero, and
\[
\omega(e)=\omega(e^{*}),
\tag{3}
\]
where \(e^{*}\) is the antipodal edge within \(Q_D\).

*Proof.* Compare two long geodesics which start at the same vertex, traverse two directions in opposite orders, and then follow the same remaining order. Their later edges coincide, so the sum of the four square-edge weights is zero. This holds for every square.

Choose a vertex potential \(\phi\) by integrating \(\omega\) from a fixed vertex. The integral is independent of the chosen path: a cube walk is encoded by coordinate flips, and adjacent exchanges and cancellations of repeated consecutive flips reduce any closed walk to the empty walk. Square sums and the weights of backtracks vanish. Thus
\[
\omega(\{x,x^j\})=\phi(x)+\phi(x^j).
\]
Writing \(x^D\) for the complement within \(Q_D\), the hypothesis implies
\[
\phi(x)+\phi(x^D)=\kappa.
\]
Adding this equation at \(x\) and \(x^j\) proves (3). The same argument applies when \(|D|=1\), with no square condition needed. \(\square\)

*Proof of Theorem 1.* Put \(a_{ji}=a_{ij}\) and \(a_{ii}=0\). Consider a long geodesic whose first direction is \(i\), with profile \(w\). Move its root across its first edge and rotate that direction to the end of the order. All other edges are unchanged, and the new last edge is antipodal to the old first edge. By (1), the new profile is \(w+e_i\). Therefore
\[
0=q(w+e_i)+q(w)=b_i+\sum_{j\ne i}a_{ij}w_j.
\tag{4}
\]

Fix either facet perpendicular to \(i\). Every long geodesic in that facet can be preceded by an \(i\)-edge to obtain a long geodesic of the full cube beginning in direction \(i\). Consequently (4) says that the weights
\[
\omega_j(x)=a_{ij}c_j(x)\qquad(j\ne i)
\tag{5}
\]
have constant long-geodesic integral \(b_i\) on each of the two facets.

There are three consequences.

First, complementing every vertex of a full geodesic complements every entry of its profile and preserves its first direction. Adding (4) for a path and its antipodal image gives
\[
\sum_{j\ne i}a_{ij}=0\qquad(i\in[n]).
\tag{6}
\]

Second, apply (3) to (5) within an \(i\)-facet. Its antipodal map is \(x\mapsto\bar x^i\), so
\[
a_{ij}c_j(x)=a_{ij}c_j(\bar x^i)
           =a_{ij}\bigl(1+c_j(x^i)\bigr).
\]
For the Boolean difference \(\Delta_i c_j(x)=c_j(x^i)+c_j(x)\), this gives
\[
a_{ij}=1\quad\Longrightarrow\quad
\Delta_i c_j(x)=1\text{ for every }x.
\tag{7}
\]

Third, square closedness in the same facet gives, for distinct \(i,j,k\),
\[
a_{ij}\Delta_k c_j(x)=a_{ik}\Delta_j c_k(x).
\tag{8}
\]

Form a simple graph on \([n]\), placing an edge \(ij\) precisely when \(a_{ij}=1\). If \(ij\) and \(jk\) are edges with \(i,j,k\) distinct, (7) gives
\(\Delta_k c_j=\Delta_j c_k=1\). Equation (8) then forces \(a_{ik}=1\). Every connected component of this graph is therefore a clique. By (6), all its vertex degrees are even, so each clique has odd order.

Suppose a component \(B\) has at least two vertices. Fix \(j\in B\) and choose \(i\in B\setminus\{j\}\). Equation (7) gives
\[
\Delta_k c_j=1\quad(k\in B\setminus\{j\}).
\]
For \(k\notin B\), equation (8), with \(a_{ij}=1\) and \(a_{ik}=0\), gives \(\Delta_k c_j=0\). Also \(\Delta_j c_j=0\) by undirectedness. Hence, for some constant \(\gamma_j\),
\[
c_j(x)=\gamma_j+\sum_{k\in B\setminus\{j\}}x_k.
\tag{9}
\]
Indeed, subtracting the displayed coordinate sum leaves a function with zero difference in every coordinate, which is constant on the connected cube. Since \(|B|\) is odd, (9) is invariant under complementing all coordinates. This contradicts (1).

Thus the coefficient graph has no edges, and every \(a_{ij}\) vanishes. Equation (4) now gives \(b_i=0\) for every \(i\). Since at least one long geodesic exists, evaluating \(q\) on its profile gives \(a_0=0\). \(\square\)

**Corollary 3 (dimension and profile count).** The vectors
\[
\left(1,\ (w_i)_{i\in[n]},\
                (w_iw_j)_{1\le i<j\le n}\right),
\qquad w\in\mathcal W(c),
\tag{10}
\]
span \(\mathbb F_2^{\,1+n+\binom n2}\). In particular,
\[
|\mathcal W(c)|\ge 1+n+\binom n2.
\tag{11}
\]
Since \(\mathcal W(c)\) is closed under complementation, its cardinality is even; consequently (11) may be rounded up to the next even integer.

*Proof.* A proper linear span in (10) would admit a nonzero annihilating linear functional. Its coefficients would define a nonzero polynomial (2) vanishing on every profile, contrary to Theorem 1. A spanning family has at least as many vectors as the dimension. Complementation has no fixed point on \(\mathbb F_2^n\), proving the final assertion. \(\square\)

The theorem strengthens the affine-span conclusion of Article VIII by including all pair products of direction colors, even when their coefficients involve arbitrarily many directions. Its proof uses compatible edges on every coordinate square and both facets perpendicular to each direction. It provides a restriction on the full profile family of any hypothetical counterexample: every nonzero multilinear polynomial vanishing on that family must have degree at least three.

The statement concerns direction-indexed profiles over all long geodesics. It does not specify traversal orders, guarantee either constant profile, or establish a two-switch path. Those existence questions remain open.

### Common-facet terminal lifting and exterior color stability

Let \(d,e:E(Q_m)\to\{0,1\}\) be arbitrary undirected-edge colorings. For a face \(H\) of \(Q_m\), write \(E_r^H(d)\) for the vertices of \(H\) that terminate a geodesic spanning \(H\) with at most \(r\) changes in its \(d\)-edge-color word. The set \(E_r(d)\) denotes the corresponding terminals of geodesics spanning the whole cube. If \(S\subseteq[m]\), write \(x^S\) for the vertex obtained by flipping each coordinate of \(S\).

**Lemma 1 (common-subface lifting).** Let \(H\) be a codimension-\(r\) face of \(Q_m\), with fixed-coordinate set \(S\), and let \(a,b\ge0\). Then
\[
\boxed{\bigl(E_a^H(d)\cap E_b^H(e)\bigr)^S
 \subseteq E_{a+r}(d)\cap E_{b+r}(e).}\tag{1}
\]
No conditions are imposed on any edge outside \(H\). The same assertion holds simultaneously for any number of edge colorings, with separately specified switch budgets.

*Proof.* Fix \(x\in E_a^H(d)\cap E_b^H(e)\). Choose spanning geodesics \(P_d,P_e\subseteq H\) ending at \(x\) with at most \(a,b\) changes, respectively. From \(x\), traverse the directions of \(S\) in an arbitrary common order, producing a path \(R\) with \(r\) edges from \(x\) to \(x^S\). Concatenating \(P_dR\) and \(P_eR\) yields two geodesics of \(Q_m\): the paths inside \(H\) traverse every direction outside \(S\) once, and the appended paths traverse precisely the remaining directions. Their final vertex is the same \(x^S\). Appending \(r\) edges introduces at most \(r\) additional adjacent color comparisons, independently for each coloring. This proves (1). For \(r=0\), the inclusion is the identity. The argument is identical for further colorings. \(\square\)

**Theorem 2 (one common block-radial facet).** Suppose \(m\ge2\) and there exist a direction \(p\in[m]\) and a bit \(\eta\in\{0,1\}\) such that, under identification of the facet \(H=\{x:x_p=\eta\}\) with \(Q_{m-1}\), both restrictions \(d|_H,e|_H\) are shifted block-radial edge colorings. Explicitly, for each coloring independently, partition \(D=[m]\setminus\{p\}\) into blocks, choose a shift \(t\in\{0,1\}^D\), and assign an arbitrary binary function \(h_B\) on \(\{0,\ldots,|B|-1\}\) to every block. Its edge colors within \(H\) have the form
\[
d_i(x)=h_{B(i)}\left(\sum_{j\in B(i)\setminus\{i\}}(x_j\oplus t_j)\right)
\qquad(i\in D,\ x\in H),\tag{2}
\]
and analogously for \(e\), with independent data. Then
\[
\boxed{E_2(d)\cap E_2(e)\ne\varnothing.}\tag{3}
\]
The coloring of **every** edge outside \(H\), including all edges in the opposite facet and all edges in direction \(p\), may be prescribed independently and arbitrarily for \(d\) and \(e\).

*Proof.* The simultaneous one-switch terminal theorem for two shifted block-radial colorings, proved above in this Article, applies to the restrictions on \(H\). It yields
\[
E_1^H(d)\cap E_1^H(e)\ne\varnothing.
\]
Apply Lemma 1 with \(S=\{p\}\) and \(a=b=1\). The proof consults the colors outside \(H\) only to count at most one extra change on the appended edge. \(\square\)

**Corollary 3 (several unrestricted exterior coordinates).** Let \(S\subseteq[m]\) have cardinality \(r\) and let \(H\) be any corresponding codimension-\(r\) face with \(m-r\ge1\). If \(d|_H\) and \(e|_H\) are independently shifted block-radial, then
\[
\boxed{E_{r+1}(d)\cap E_{r+1}(e)\ne\varnothing.}\tag{4}
\]
Consequently, for \(r=1\) the common-terminal two-switch assertion survives arbitrary and independent recoloring of all edges outside one common facet, a class wider than perturbations confined to one edge direction.

*Proof.* Apply the simultaneous one-switch theorem on \(H\) and then Lemma 1 with \(a=b=1\). \(\square\)

**Corollary 4 (NORI1 completion from matched codimension-three subfaces).** Let \(n=m+2\ge4\), and let \(c\) color the undirected edges of \(Q_n\) subject to \(c(\bar f)=1-c(f)\) for every edge \(f\). Fix adjacent parallel codimension-two faces \(F,F^a\) with common free directions \(D\) of size \(m\). Suppose that for some \(p\in D\), the restrictions of \(c\) to the two corresponding codimension-three faces obtained by fixing \(p=\eta\) in \(F\) and \(F^a\) are shifted block-radial under their common free-coordinate identification. Then
\[
\boxed{\mu(c)\le2.}\tag{5}
\]

*Proof.* Identify \(F,F^a\) with \(Q_m\), giving unrestricted colorings \(d,e\). Theorem 2 supplies geodesics spanning \(F,F^a\), each with at most two changes and terminating at corresponding vertices. The parallel-face switch bound of Article VIII yields \(\mu(c)\le2\). The antipodal relation on \(c\) is used in the final gluing theorem; no antipodal condition is required in the two subfaces. \(\square\)

The statements are conditional on one common face of controlled structure. In particular, no claim that an arbitrary pair \(d,e\) has such a face is needed.

### Antipodal diagonal compression and local face certificates

Let \(n\ge3\), let \(c:E(Q_n)\to\mathbb F_2\) satisfy \(c(\bar e)=1+c(e)\), and fix distinct directions \(a,b\). Put \(D=[n]\setminus\{a,b\}\), with \(|D|=m\). After translating coordinates, let \(F\) fix \(a=b=0\). Identify \(F\) with \(Q_D\), and write \(x^*=x^D\) for complementation within \(F\). For \(x\in F\), label its exterior square by
\[
A(x)=c(xx^a),\quad B(x)=c(xx^b),\quad
C(x)=c(x^ax^{ab}),\quad E(x)=c(x^bx^{ab}).
\tag{1}
\]
Thus the routes from \(x\) to its corresponding vertex \(x^{ab}\) have color words \(A(x)C(x)\) and \(B(x)E(x)\). Antipodal oddness gives
\[
A(x^*)=1+E(x),\quad B(x^*)=1+C(x),\quad
C(x^*)=1+B(x),\quad E(x^*)=1+A(x).
\tag{2}
\]

##### Odd compressed cubes

Keep the edges of \(F\) and \(F^{ab}\), and join every pair \(x,x^{ab}\) by a new edge of color \(h(x)\). The resulting graph is \(Q_D\times Q_1\). If \(d\) denotes the restriction to \(F\), its two facet colorings are
\[
g_i(x,0)=d_i(x),\qquad g_i(x,1)=1+d_i(x^*),\qquad i\in D.
\tag{3}
\]
The joining-direction edge has color \(g_t(x,z)=h(x)\). This coloring is antipodally odd if and only if
\[
h(x^*)=1+h(x).
\tag{4}
\]

For compression using original \(a\)-edges, choose one edge from each antipodal pair: the edge chosen at \(x\) is incident with \(F\), and its antipodal mate at \(x^*\) is incident with \(F^{ab}\), or conversely. Its joining color satisfies
\[
h_a(x)\in\{A(x),E(x)\},\qquad h_a(x^*)=1+h_a(x).
\tag{5}
\]
Equation (2) shows that such choices always exist and can be made independently on the antipodal pairs of vertices of \(F\). The corresponding \(b\)-compression has
\[
h_b(x)\in\{B(x),C(x)\},\qquad h_b(x^*)=1+h_b(x).
\tag{6}
\]
Both compressed cubes therefore belong to NORI1 in dimension \(n-1\). They have the same facet colorings (3) and differ only in their joining edges.

A long geodesic in a compressed cube crosses its joining direction once. Reverse it if necessary so that it goes from the lower to the upper facet, and write its word as
\[
\alpha\,h(x)\,\beta.
\tag{7}
\]
Its two lifts to \(Q_n\) have words
\[
\alpha\,A(x)C(x)\,\beta,\qquad
\alpha\,B(x)E(x)\,\beta.
\tag{8}
\]
The direction sets used before and after the crossing partition \(D\). Thus each lift uses every direction of \(Q_n\) once and has antipodal endpoints.

If \(h(x)\) is chosen from any of the four square edges, one route in (8) retains that edge color and inserts one additional letter beside it. Inserting a binary letter increases the switch count by at most two. Consequently a compressed path with at most two switches lifts to at most four switches. A compressed path with at most one switch lifts to at most three; odd-change rotation in \(Q_n\) then gives \(\mu(c)\le2\).

##### Reassembly at the joining position

The following formula describes all paths through a prescribed joining edge. It depends only on the coloring \(d\) in one face.

For an arbitrary edge coloring \(d\) of \(Q_m\), a vertex \(x\in Q_m\), and \(p\in\mathbb F_2\), let \(\tau_d(x;p)\) be the least switch count of a long geodesic in the two-facet cube (3) which crosses the joining edge at \(x\), when that edge has color \(p\). Its value does not depend on the other joining-edge colors.

For a nonempty long \(d\)-geodesic \(R\) rooted at \(x\), let \(r(R)\) be its switch count and \(s(R)\) its initial edge color.

**Theorem 1 (reassembly formula).**
\[
\boxed{\tau_d(x;p)=
\min_{R:x\to x^*}
\begin{cases}
r(R),&r(R)\text{ even},\\
r(R)-1+2[s(R)\ne p],&r(R)\text{ odd}.
\end{cases}}
\tag{9}
\]

*Proof.* Split \(R=UV\) at any vertex \(u\). In the compressed cube, traverse \(U\) in reverse from \(u\) to \(x\) in the lower facet, cross the joining edge to \(x\) in the upper facet, and then traverse the reversed antipodal image of \(V\). This last segment starts at \(x\) in the upper facet and ends at \(u^*\) there. The resulting path is long.

Conversely, a compressed path crossing at \(x\) can be reassembled in the lower face: reverse its lower portion to obtain \(U\), and antipodally reverse its upper portion to obtain \(V\). The two segments concatenate into a long \(d\)-geodesic from \(x\) to \(x^*\). Thus all such compressed paths arise from the construction.

Let \(w\) be the word of \(R\), with initial color \(s\), final color \(q\), and \(r\) switches. Its compressed word is
\[
\operatorname{rev}(w(U))\,p\,
       \overline{\operatorname{rev}(w(V))}.
\tag{10}
\]
For an interior split, let \(j\in\{0,1\}\) indicate whether the cut lies at a switch. Its switch count is
\[
r-j+[s\ne p]+[1+q\ne p].
\tag{11}
\]
If \(r\) is even, \(q=s\), so the last two terms sum to one. For \(r>0\), splitting at a switch realizes the minimum \(r\). Splitting at either endpoint yields \(r+[s\ne p]\) or \(r+[1+q\ne p]\); these endpoint choices also give minimum \(r\), including \(r=0\).

If \(r\) is odd, \(q=1+s\), and the last two terms in (11) sum to \(2[s\ne p]\). A split at a switch yields \(r-1+2[s\ne p]\). Endpoint splits yield \(r+[s\ne p]\), which give no smaller value. Minimizing over \(R\) proves (9). \(\square\)

Define
\[
H_2(d,x)=\{p\in\mathbb F_2:\tau_d(x;p)\le2\}.
\tag{12}
\]

**Corollary 2 (two-switch face alternatives).** If some long \(d\)-geodesic rooted at \(x\) has at most two switches, then \(H_2(d,x)=\mathbb F_2\). Otherwise
\[
H_2(d,x)=
\{p:\text{a long }d\text{-geodesic rooted at }x
       \text{ has three switches and initial color }p\}.
\tag{13}
\]
Furthermore \(H_2(d,x^*)=1+H_2(d,x)\).

*Proof.* A path with zero or two switches gives both joining colors by (9). A one-switch path gives costs zero and two. If every face path has at least three switches, only a three-switch path whose initial color is the joining color can contribute a value at most two. Reversing a face path preserves its switch count, preserves its initial color when that count is even, and complements it when the count is odd. Applying (9) proves the final equality. \(\square\)

##### Varying all antipodal selections

**Lemma 3 (selection criterion).** Suppose nonempty sets \(S(x)\subseteq\mathbb F_2\) satisfy \(S(x^*)=1+S(x)\). The following are equivalent:

(i) Every joining coloring \(h\) satisfying (4) and \(h(x)\in S(x)\) gives a compressed cube with a long geodesic having at most two switches.

(ii) Some \(x\) satisfies \(S(x)\subseteq H_2(d,x)\).

*Proof.* If (ii) holds, every admissible selection assigns a color to the joining edge at \(x\) for which a two-switch path exists. Conversely, suppose (ii) fails. At one representative \(x\) of each antipodal pair, choose a color in \(S(x)\setminus H_2(d,x)\), and give the opposite vertex its complementary color. Corollary 2 ensures that this color also belongs to \(S(x^*)\setminus H_2(d,x^*)\). No joining position now supports a two-switch long path. Every long compressed path uses one joining edge, contradicting (i). \(\square\)

For the \(a\)-compression use \(S(x)=\{A(x),E(x)\}\), and for the \(b\)-compression use \(S(x)=\{B(x),C(x)\}\). Therefore, if the universal two-switch assertion holds in dimension \(n-1\), each family has a vertex at which every available joining color supports a two-switch path. The vertices supplied by the two families may differ.

Allowing all odd joining colorings yields a full-class equivalence.

**Theorem 4 (rooted face characterization).** For every \(m\ge1\), the following statements are equivalent:

(a) Every antipodally odd edge coloring of \(Q_{m+1}\) has a long geodesic with at most two switches.

(b) Every arbitrary edge coloring \(d\) of \(Q_m\) has a vertex \(x\) satisfying one of:
- a long geodesic rooted at \(x\) has at most two switches;
- two long geodesics rooted at \(x\) each have three switches and have different initial edge colors.

*Proof.* Every antipodally odd coloring of \(Q_{m+1}\) has the form (3), with an arbitrary lower-facet coloring \(d\) and an odd joining coloring \(h\). For fixed \(d\), Lemma 3 with \(S(x)=\mathbb F_2\) says that every such \(h\) admits a two-switch path if and only if some \(x\) has \(H_2(d,x)=\mathbb F_2\). By Corollary 2, this is precisely the alternative in (b). Quantifying over \(d\) proves the equivalence. \(\square\)

##### Monochromatic square routes and a hypothetical four-switch obstruction

**Corollary 5 (monochromatic diagonal completion).** Suppose a long geodesic \(R\subset F\), rooted at \(x\), has \(r\) switches and initial color \(s\). If the exterior square at \(x\) has a monochromatic route from \(x\) to \(x^{ab}\) of color \(p\), then \(Q_n\) has a long geodesic with at most
\[
\begin{cases}
r,&r\text{ even},\\
r-1+2[s\ne p],&r\text{ odd}
\end{cases}
\tag{14}
\]
switches.

*Proof.* Use the split realizing (9), with joining color \(p\), and replace the joining edge by the monochromatic square route. Duplicating its color preserves the switch count in (10). The result is a long geodesic of \(Q_n\). \(\square\)

In particular, a two-switch face path together with a monochromatic diagonal square route of either color gives \(\mu(c)\le2\). A three-switch face path rooted at \(x\) gives the same conclusion when the route color equals its initial color.

**Theorem 6 (constraints obtained from compressed induction).** Suppose the universal two-switch assertion holds in dimension \(n-1\), and \(c\) is an antipodally odd coloring of \(Q_n\) with \(\mu(c)\ge4\). For every opposing codimension-two face pair \(F,F^{ab}\), there is \(x\in F\) such that
\[
A(x)\ne C(x),\qquad B(x)\ne E(x),
\tag{15}
\]
and one of the following holds:
- \(F\) has a long two-switch geodesic rooted at \(x\);
- \(F\) has long three-switch geodesics rooted at \(x\) with both initial colors.

In the first case, if \(s\) is the initial color of the two-switch face path, then
\[
A(x)=B(x)=1+s,\qquad C(x)=E(x)=s.
\tag{16}
\]

*Proof.* Let \(M(x)\) be the set of colors of monochromatic diagonal routes in the exterior square. Equation (2) implies \(M(x^*)=1+M(x)\). Set \(S(x)=M(x)\) when this set is nonempty, and \(S(x)=\mathbb F_2\) otherwise. Every allowed color can be chosen from an original square edge; the antipodal selections give odd compressed cubes. Induction and Lemma 3 supply \(x\) with \(S(x)\subseteq H_2(d,x)\).

If \(M(x)\) were nonempty, choose \(p\in M(x)\subseteq H_2(d,x)\). A compressed two-switch path crossing there lifts along the monochromatic route without changing its switch count, contradicting \(\mu(c)\ge4\). Thus \(M(x)=\varnothing\), which is (15), and \(H_2(d,x)=\mathbb F_2\). Corollary 2 gives the asserted alternatives. A face path with at most one switch would extend by the two exterior directions to a full path with at most three switches; odd-change rotation would give \(\mu(c)\le2\). Hence the first alternative has two switches.

Finally, reverse that face path so it terminates at \(x\). Its final color remains \(s\), since its switch count is even. Appending either square route introduces at most two switches. If either route introduced fewer than two, a full path would have at most three and imply \(\mu(c)\le2\). Both new comparisons must therefore switch on both routes, giving (16). \(\square\)

The induction conclusion is a local certificate in an arbitrary face coloring, obtained by varying the antipodal selections. The remaining configurations in (15)–(16) specify where the two-edge lift can introduce its additional switches. Excluding those configurations globally, or finding a compressed witness whose square lift has at most three switches, would complete the proposed two-switch induction.
