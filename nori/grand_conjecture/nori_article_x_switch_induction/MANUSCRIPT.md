# Article X — Low-switch induction through parallel codimension-two faces

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

### Simultaneous low-switch terminals from signed coordinate partitions

Let \(\mathcal P\) be a partition of \([m]\), choose \(\varepsilon_B\in\mathbb F_2\) for each \(B\in\mathcal P\), and choose an arbitrary vector \(u\in\mathbb F_2^m\). Define the binary coloring of undirected edges of \(Q_m\) by
\[
d_i(x)=\varepsilon_{B(i)}\oplus\bigoplus_{j\in B(i)\setminus\{i\}}(x_j\oplus u_j),\qquad i\in[m], \tag{1}
\]
where \(B(i)\) is the block containing \(i\). The right side is invariant under changing \(x_i\).

**Theorem (signed-partition simultaneous endpoints).** For any two colorings \(d,e\) of the form (1), allowing independent partitions, block constants, and vectors \(u,v\), there exists \(x\in Q_m\) supporting a spanning antipodal geodesic with at most two switches for \(d\) and one with at most one switch for \(e\), both terminating at \(x\). Another (possibly different) common terminal supports the reversed pair of switch bounds. In symbols,
\[
E_2(d)\cap E_1(e)\ne\varnothing,\qquad
E_1(d)\cap E_2(e)\ne\varnothing. \tag{2}
\]
If the coordinate shifts coincide, \(u=v\), then \(E_1(d)\cap E_1(e)\ne\varnothing\). In that case, if the partition of \(d\) has only even-sized blocks, \(E_0(d)\cap E_1(e)\ne\varnothing\); if both partitions have only even-sized blocks, \(E_0(d)\cap E_0(e)\ne\varnothing\).

**Lemma 1 (signed incidence balancing).** Let \(G=(L,R;E)\) be any finite bipartite multigraph and let \(a_{v,e}\in\{-1,+1\}\) be specified for every incidence \(v\in e\). There exist signs \(y_e\in\{-1,+1\}\) such that
\[
\left|\sum_{e\ni v} a_{v,e}y_e\right|\le1\quad(v\in R),
\qquad
\left|\sum_{e\ni v} a_{v,e}y_e\right|\le2\quad(v\in L),\tag{3}
\]
and every odd-degree vertex has absolute sum at most one. Moreover each even-degree vertex in \(R\) has sum zero. The two sides can be interchanged.

*Proof.* Treat each connected component separately. If the component has odd-degree vertices, introduce an auxiliary vertex joined to each of them by one new edge. Assign arbitrary signs to the two incidences of every auxiliary edge. The number of odd-degree vertices is even, so the augmented multigraph is Eulerian. Traverse an Euler circuit beginning at the auxiliary vertex. Choose the sign of its first edge freely. Whenever an edge \(f\) follows an edge \(e\) at vertex \(w\), choose \(y_f\) so that \(a_{w,e}y_e+a_{w,f}y_f=0\). This cancels each consecutive arrival-departure pair. All original vertices have signed sum zero in the augmented graph, because the only potentially unmatched pair occurs at the auxiliary starting vertex. Removing the auxiliary edges leaves sum zero at original even-degree vertices and sum of absolute value one at original odd-degree vertices.

If every vertex of a component has even degree, choose a starting vertex \(w\in L\) for its Euler circuit and use the same cancellation rule. Every vertex other than \(w\) has sum zero; the two boundary incidences at \(w\) contribute a sum of magnitude at most two. Isolated vertices have sum zero. This proves (3) and the stronger assertions. Starting the even-degree components on the other side interchanges \(L,R\). \(\square\)

**Lemma 2 (balanced-block traversals).** In a block \(B\) of size \(\ell\), put \(z_j=x_j\oplus u_j\) and \(k=\sum_{j\in B}z_j\). If \(\ell\) is odd and \(|2k-\ell|\le1\), the directions of \(B\) admit a monochromatic spanning traversal from \(x\). The same holds if \(\ell\) is even and \(2k=\ell\); in that case either color may be chosen. If \(\ell\) is even and \(|2k-\ell|=2\), there is a spanning traversal with at most one switch.

*Proof.* When \(\ell=2r\) and \(k=r\), alternate flips of initially one- and zero-valued \(z\)-bits. Beginning with a one-bit gives constant color \(\varepsilon_B\oplus(r-1\bmod2)\); beginning with a zero-bit gives the complementary color. When \(k=r+1\), alternate a one-bit then a zero-bit for \(r-1\) pairs, followed by the two remaining one-bits. The first \(2r-1\) edges all have color \(\varepsilon_B\oplus(r\bmod2)\), while the last has the opposite color. For \(k=r-1\), alternate a zero-bit then a one-bit for \(r-1\) pairs, followed by two remaining zero-bits. Again only the final edge differs in color. If \(\ell=2r+1\) and \(k=r\) or \(r+1\), alternate flips beginning and ending with a bit of the initially more numerous value. Throughout this traversal the parity of the number of other one-valued \(z\)-bits is \(r\bmod2\); the word is monochromatic. \(\square\)

**Lemma 3 (three-phase assembly).** Suppose the directions are partitioned into disjoint blocks, and each block has a spanning traversal with at most one color change, with each block-edge color depending only on coordinates in that block. Then all block traversals can be interleaved to give a spanning geodesic with at most two changes. If every block admits a monochromatic traversal, a spanning geodesic with at most one change exists; if every block admits either monochromatic color, a monochromatic spanning geodesic exists.

*Proof.* Regard a block path with one change as either \(0^a1^b\) or \(1^a0^b\). In the first phase traverse the zero-prefixes of all \(0^a1^b\) paths. In the second phase traverse their one-suffixes, the one-prefixes of all \(1^a0^b\) paths, and all constant-one blocks. In the third phase traverse the zero-suffixes of the \(1^a0^b\) paths and all constant-zero blocks. The within-block edge order is preserved, so every specified edge color remains valid. The resulting word has form \(0^*1^*0^*\). The monochromatic-block claims follow by grouping the blocks according to their colors, or choosing the same color for all. \(\square\)

*Proof of the theorem.* Construct the bipartite incidence graph between the partition blocks defining \(d\) and \(e\), with one edge for each coordinate \(i\). At its \(d\)-end give edge \(i\) incidence sign \((-1)^{u_i}\), and at its \(e\)-end use \((-1)^{v_i}\). Choose \(y_i\) by Lemma 1, taking the \(e\)-blocks to be the right vertices, and select \(x_i\) through \(y_i=(-1)^{x_i}\). The signed sum at a block is then
\[
\sum_{i\in B}(-1)^{x_i\oplus u_i}
=|B|-2\sum_{i\in B}(x_i\oplus u_i)
\tag{4}
\]
for \(d\), with \(v\) in place of \(u\) for \(e\). Every \(e\)-block has discrepancy at most one, so Lemmas 2 and 3 give a spanning geodesic with at most one change under \(e\). Every \(d\)-block has discrepancy at most two, and the odd blocks have discrepancy at most one; Lemmas 2 and 3 give a spanning geodesic with at most two changes under \(d\). Both may start at \(x\), so their reversals terminate at \(x\). Interchanging sides proves the other intersection in (2).

If \(u=v\), replace \(x\) throughout by \(x\oplus u\), reducing to two unshifted block partitions. Their incidence multigraph admits an equitable two-coloring of its edges: attach one auxiliary vertex to each side, join each odd-degree original vertex to the auxiliary vertex on the opposite side, and join the auxiliary vertices to each other when their degrees are odd. The augmented graph is bipartite and Eulerian. Alternating 0/1 around each even-length Euler circuit gives each original block equal color counts when its size is even and counts differing by one when its size is odd. Thus every block in both partitions satisfies the stronger hypotheses of Lemma 2 for a monochromatic traversal. Lemma 3 gives one-switch paths in both colorings, and monochromatic paths whenever all blocks of the corresponding partition have even size. \(\square\)

**Corollary (ambient NORI1).** Let \(c\) be an antipodally odd coloring of \(Q_{m+2}\). Suppose its restrictions to two adjacent codimension-two faces are of form (1), with independent partitions, block constants, and shifts. Then \(\mu(c)\le2\). If the two shifts coincide and one partition has only even-sized blocks, then \(\mu(c)=0\).

*Proof.* The theorem gives corresponding terminal vertices with switch counts \(r\le2,s\le1\). Theorem 10 of Article VIII yields \(\mu(c)\le2\). Under the final hypotheses, the theorem gives \(r=0,s\le1\) after possibly interchanging faces. The symmetric bound gives \(\mu(c)\le1\); evenness of the minimum full-path switch count under antipodal oddness forces \(\mu(c)=0\). \(\square\)

##### Signed partition balancing and simultaneous one-switch endpoints

Let \(\mathcal P,\mathcal Q\) be partitions of \([m]\). Fix independently chosen shifts \(t,s\in\mathbb F_2^m\), and for each \(B\in\mathcal P\) and \(C\in\mathcal Q\) fix arbitrary functions
\[
h_B:\{0,\ldots,|B|-1\}\longrightarrow\mathbb F_2,\qquad
g_C:\{0,\ldots,|C|-1\}\longrightarrow\mathbb F_2.
\]
Define undirected-edge colorings of \(Q_m\) by
\[
\begin{aligned}
d_i(x)&=h_{B(i)}\left(\sum_{j\in B(i)\setminus\{i\}}(x_j\oplus t_j)\right),\\
e_i(x)&=g_{C(i)}\left(\sum_{j\in C(i)\setminus\{i\}}(x_j\oplus s_j)\right),
\end{aligned}\tag{1}
\]
where \(B(i)\in\mathcal P\) and \(C(i)\in\mathcal Q\) contain \(i\). The functions need not be affine, periodic, or related between different blocks. Each edge color is independent of the coordinate of that edge.

**Theorem (simultaneous terminals for two shifted block-radial colorings).** There exists \(x\in Q_m\) such that both \(d\) and \(e\) admit spanning geodesics terminating at \(x\) with at most one color change.

If every block \(B\in\mathcal P\) is even-sized, and there is a color \(\gamma\in\mathbb F_2\) such that
\[
\gamma\in\{h_B(|B|/2-1),h_B(|B|/2)\}
\quad\text{for every }B\in\mathcal P,\tag{2}
\]
the \(d\)-geodesic can be chosen monochromatic of color \(\gamma\). The analogous statement holds for \(\mathcal Q\).

**Corollary (codimension-two gluing).** Suppose an antipodally odd edge coloring \(c\) of \(Q_{m+2}\) restricts on two adjacent codimension-two faces to colorings of the form (1), under the identification of corresponding vertices with \(Q_m\). Then \(\mu(c)\le2\). If condition (2) holds for either face coloring, then \(\mu(c)=0\).

*Proof.* The theorem gives spanning face paths with corresponding terminals and at most one switch each. Article VIII, Theorem 10, yields \(\mu(c)\le2\). If one path is monochromatic, its symmetric bound yields \(\mu(c)\le1\). The minimum switch count of an antipodally odd coloring is even under cyclic root rotation, hence is zero. \(\square\)

The theorem follows from an incidence-balancing lemma and the behavior of layer-dependent edge colors along alternating coordinate orders.

**Lemma 1 (one-sided signed equitable balancing).** Let \(G\) be a finite bipartite multigraph with sides \(L,R\). Give each incidence \((v,f)\) a sign \(\sigma_{v,f}\in\{-1,1\}\); the two ends of an edge may receive unrelated signs. There exist edge signs \(z_f\in\{-1,1\}\) such that
\[
S_v=\sum_{f\ni v}\sigma_{v,f}z_f
\]
satisfies \(|S_v|\le1\) at every vertex of \(L\), and \(|S_v|\le1\) at every vertex of \(R\) except possibly one vertex per connected component, where \(|S_v|\le2\). In a component having an odd-degree vertex, all signed sums can be made of absolute value at most one. In a component with all degrees even, all sums vanish except possibly at one prescribed right-side vertex, whose signed sum belongs to \(\{0,-2,2\}\).

*Proof.* Work independently in each connected component. In an all-even-degree component, choose an Euler circuit starting at a right-side vertex \(v_0\). Assign the sign of its first edge arbitrarily, then choose each subsequent edge sign so that its contribution at the current vertex cancels that of the preceding edge. Each edge appears once, so the assignments are consistent. At every vertex other than \(v_0\), the visits pair all incidences and give signed sum zero. At \(v_0\), the initial and final incidences are unpaired and give sum \(0\) or \(\pm2\).

If the component has odd-degree vertices, pair them arbitrarily and add one auxiliary edge joining each pair, with arbitrary incidence signs. The augmented graph is connected with all degrees even. Start an Euler circuit at an odd-degree vertex \(v_0\), taking its auxiliary edge first, and assign signs by consecutive cancellation. Delete the auxiliary edges. Every original even-degree vertex retains signed sum zero. Each odd-degree vertex other than \(v_0\) loses one incidence from an augmented sum of zero, leaving signed sum \(\pm1\). At \(v_0\), the sole unpaired original incidence is the last edge of the circuit; the initial edge was auxiliary. Its signed sum is therefore \(\pm1\). \(\square\)

**Lemma 2 (radial block traversals).** Let \(B\) have size \(\ell\), let \(t|_B\) be a shift, and color its direction-\(i\) edges by
\[
d_i(x)=h\left(\sum_{j\in B\setminus\{i\}}(x_j\oplus t_j)\right)
\]
for an arbitrary \(h:\{0,\ldots,\ell-1\}\to\mathbb F_2\). Write \(b_j=x_j\oplus t_j\) and \(D_B(x)=|\sum_{j\in B}(-1)^{b_j}|\).

(i) If \(D_B(x)\le1\), the directions of \(B\) admit a monochromatic spanning traversal starting at \(x|_B\).

(ii) If \(\ell=2r\) and \(D_B(x)=0\), one can prescribe the common edge color as either \(h(r-1)\) or \(h(r)\).

(iii) If \(\ell=2r\) and \(D_B(x)=2\), there is a spanning traversal with color word
\[
h(r)^{\,2r-1}h(r-1)
\quad\text{or}\quad
h(r-1)^{\,2r-1}h(r),\tag{3}
\]
according as \(b\) initially has \(r+1\) or \(r-1\) one-bits. In particular it has at most one switch. Complementing every \(b_j\) reverses the two displayed color phases.

*Proof.* For \(\ell=2r\) with \(r\) ones and \(r\) zeros, alternate initially one and zero coordinates. Beginning with a one yields \(r-1\) one-bits among the other coordinates at each edge; beginning with a zero yields \(r\) such bits. This proves (i)–(ii) for even \(\ell\) and zero imbalance.

For \(\ell=2r+1\), a zero-or-one imbalance means that \(b\) has \(r\) or \(r+1\) ones. Alternate initial majority and minority coordinates, starting and ending with a majority coordinate. Each traversed edge then sees \(r\) ones among its other block coordinates, and therefore has color \(h(r)\). This proves (i) for odd \(\ell\), including \(\ell=1\).

If \(\ell=2r\) and there are \(r+1\) initial ones, traverse \(r-1\) alternating pairs of one and zero coordinates, followed by the two remaining one coordinates. Every edge except the last sees \(r\) other one-bits; the last sees \(r-1\). If there are \(r-1\) initial ones, use the symmetric order of alternating zero and one coordinates followed by two zeros. The other-bit counts are \(r-1\) until the last edge, where the count is \(r\). This proves (iii). \(\square\)

*Proof of the theorem.* Form the bipartite incidence multigraph whose left vertices are the blocks of \(\mathcal P\), right vertices are the blocks of \(\mathcal Q\), and whose edge labeled \(i\) joins \(B(i)\) to \(C(i)\). Put
\[
\sigma_{B(i),i}=(-1)^{t_i},\qquad
\sigma_{C(i),i}=(-1)^{s_i}.
\]
Apply Lemma 1, and define \(x_i\in\mathbb F_2\) by \(z_i=(-1)^{x_i}\). The signed sums become
\[
S_B=\sum_{i\in B}(-1)^{x_i\oplus t_i},
\qquad
S_C=\sum_{i\in C}(-1)^{x_i\oplus s_i}.
\tag{4}
\]
Every left block has imbalance \(|S_B|\le1\). Every right block has \(|S_C|\le1\), apart from at most one right block per all-even-degree component with imbalance two.

Lemma 2 gives a monochromatic traversal for every left block and every ordinary right block. Each exceptional right block has even size and admits a one-switch traversal. Within any all-even-degree component, complement all \(x_i\) indexed by its edges if necessary. The signed-sum magnitudes in (4) remain unchanged. By Lemma 2(iii), this operation exchanges the two possible phase orders of its exceptional right-block traversal. When its two layer colors differ, choose the complement so that its traversal has the phase order \(0\) followed by \(1\). When they agree, that block is monochromatic. The component choices are independent.

To form a spanning \(d\)-geodesic, concatenate the monochromatic left-block traversals in color order, first all color-zero blocks, then all color-one blocks. For \(e\), first perform the color-zero traversals of ordinary right blocks together with the color-zero prefixes of exceptional blocks; then perform the color-one traversals of ordinary blocks together with the color-one suffixes of exceptional blocks. The order within each block is preserved, and changing coordinates of another block does not affect its edge colors. Both spanning geodesics thus start at \(x\) and change color at most once. Reverse them to obtain the stated common terminal vertex.

Under condition (2), every left block has even cardinality, so \(|S_B|\le1\) implies \(S_B=0\). Lemma 2(ii) permits every left-block traversal to have common color \(\gamma\), yielding a monochromatic spanning \(d\)-geodesic. Interchanging the two sides gives the symmetric assertion. \(\square\)

The affine signed partition model \(h_B(j)=\varepsilon_B\oplus(j\bmod2)\) is a special case. Then the two central layer colors in each even block differ, so condition (2) holds whenever all blocks of one partition have even cardinality. The single-block case also includes arbitrary coordinate shifts of the rank-parity coloring.

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
