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

### Independent direction recolorings preserve low-switch terminal alignment

Let \(m\ge2\). Fix partitions \(\mathcal P,\mathcal Q\) of \([m]\), shifts \(t,s\in\mathbb F_2^m\), and functions
\[
h_B:\{0,\ldots,|B|-1\}\to\mathbb F_2\quad(B\in\mathcal P),\qquad
g_C:\{0,\ldots,|C|-1\}\to\mathbb F_2\quad(C\in\mathcal Q).
\]
Define two undirected-edge colorings of \(Q_m\):
\[
d_i^0(x)=h_{B(i)}\left(\sum_{j\in B(i)\setminus\{i\}}(x_j\oplus t_j)\right),\qquad
e_i^0(x)=g_{C(i)}\left(\sum_{j\in C(i)\setminus\{i\}}(x_j\oplus s_j)\right).
\tag{1}
\]
Here \(B(i)\) and \(C(i)\) are the blocks containing \(i\). No relation between the two partitions, shifts, or functions is assumed. For an edge coloring \(f\), let \(E_r(f)\) denote the set of vertices terminating a spanning antipodal geodesic with at most \(r\) color changes.

**Theorem (two independent direction recolorings).** Choose any directions \(p,q\in[m]\), possibly equal. Let \(d,e\) be arbitrary undirected-edge colorings satisfying
\[
d_i(x)=d_i^0(x)\quad(i\ne p),\qquad
e_i(x)=e_i^0(x)\quad(i\ne q).
\tag{2}
\]
In the exceptional directions \(p,q\), the edge colors may be arbitrary functions of all other coordinates and unrelated to (1). Then
\[
\boxed{E_2(d)\cap E_3(e)\ne\varnothing,\qquad
E_3(d)\cap E_2(e)\ne\varnothing.}\tag{3}
\]
In particular, the direction exceptions need not agree.

**Proof.** Apply one-sided signed equitable balancing to the bipartite incidence multigraph of \(\mathcal P,\mathcal Q\), with one edge \(i\) for each coordinate and incidence signs \((-1)^{t_i}\), \((-1)^{s_i}\). Designate the \(\mathcal Q\)-side as the side on which discrepancy two is allowed. This yields \(x\in Q_m\) with the following properties:

* Each \(\mathcal P\)-block has signed imbalance at most one. Its directions therefore admit a monochromatic spanning traversal from \(x\) under \(d^0\).
* Each \(\mathcal Q\)-block has signed imbalance at most one, apart from at most one even-sized block in each connected all-even-degree component; an exceptional block has imbalance at most two. Its directions admit a traversal under \(e^0\) with at most one change, while ordinary blocks admit monochromatic traversals. Complementing every bit indexed by a connected all-even-degree component reverses the two phases of that component's exceptional traversal without changing any imbalance magnitude. Choose these complements so that all nonconstant exceptional traversals have phase order \(0\) followed by \(1\).

The first bullet follows from alternating initially zero and one shifted bits within a balanced block. For an even block of imbalance two, the alternating traversal ends with the two remaining majority bits, giving at most one change; complementation exchanges the phase order. Thus the second bullet permits interleaving all \(\mathcal Q\)-block traversals into one spanning \(e^0\)-geodesic with color word \(0^*1^*\). The first bullet permits monochromatic, possibly differently colored, \(\mathcal P\)-block traversals, all rooted at the same \(x\). These are the one-sided balancing and radial-block constructions established in the preceding Subsection.

Let \(B_*\) be the \(\mathcal P\)-block containing \(p\). Choose a monochromatic \(d^0\)-traversal of \(B_*\), of color \(\gamma\), and split it into the prefix before its \(p\)-edge, that edge, and the suffix afterward. Under \(d\), the prefix and suffix still have color \(\gamma\); the single exceptional edge has some color \(\delta\in\{0,1\}\). Traverse first all other \(\mathcal P\)-blocks whose chosen monochromatic color is \(\gamma\), then the prefix of \(B_*\), then its \(p\)-edge, then all other blocks of color \(1-\gamma\), and finally the suffix of \(B_*\). This is a spanning geodesic rooted at \(x\). Every nonexceptional block color is unchanged by the interleaving, since its edge colors depend only on coordinates in that block. Its color word has the form
\[
\gamma^*\,\delta\,(1-\gamma)^*\,\gamma^*,
\]
which has at most two changes for either value of \(\delta\).

Take the spanning \(e^0\)-geodesic rooted at \(x\) constructed above. It traverses \(q\) once. Passing from \(e^0\) to \(e\) changes the color of at most that one edge, thereby changing at most the two adjacent comparisons in the edge-color word. The resulting \(e\)-geodesic has at most three changes. The two constructed paths have the same root \(x\), hence the same antipodal terminal vertex; reversing them proves the first intersection in (3).

Interchange the two partitions and designate the \(\mathcal P\)-side for discrepancy two. The identical argument gives a two-change \(e\)-geodesic and a three-change \(d\)-geodesic with a common terminal vertex. This proves the second intersection. \(\square\)

**Corollary (ambient antipodally odd colorings).** Suppose an antipodally odd undirected-edge coloring \(c\) of \(Q_{m+2}\) restricts to two adjacent codimension-two faces, under the common free-coordinate identification, as colorings \(d,e\) satisfying (1)–(2). Then
\[
\boxed{\mu(c)\le2.}\tag{4}
\]

*Proof.* The first intersection in (3) supplies long face geodesics with corresponding terminal vertices and switch counts at most two and three. The symmetric parallel-face bound of Article VIII, Theorem 10, gives
\[
\mu(c)\le\min\{\max(2,4),\max(3,2)\}=3.
\]
Antipodal oddness makes the minimum switch count on full antipodal geodesics even, so \(\mu(c)\le2\). \(\square\)

The hypotheses impose no restriction on the two exceptional-direction edge functions, including dependence on coordinates outside their respective partition blocks. In particular, distinct exceptional directions are permitted, so deleting a single common direction from the two face colorings need not recover the structured class (1). The theorem supplies a dimension-independent endpoint-alignment certificate for this class. The unrestricted two-coloring endpoint-intersection problem remains open.

#### Two globally dependent exceptional directions

The blockwise perturbation theorem permits many exceptional directions whose colors depend only on coordinates in their blocks. The following complementary extension permits two exceptional directions with completely unrestricted dependence on the other cube coordinates.

**Theorem (two-direction global perturbation).** Let \(d^0,e^0\) be shifted block-radial edge colorings defined by two arbitrary partitions, shifts, and radial functions as in (1). Choose two distinct directions \(p,q\) lying in different blocks of the \(d^0\)-partition. Form \(d\) by recoloring the edges of directions \(p,q\) arbitrarily, leaving every other direction's edge colors unchanged. Then
\[
\boxed{E_3(d)\cap E_1(e^0)\ne\varnothing.}\tag{5}
\]
Consequently, any antipodally odd ambient coloring restricting to \(d,e^0\) on adjacent codimension-two faces satisfies \(\mu(c)\le2\).

Suppose additionally that some \(\gamma\in\{0,1\}\) satisfies
\[
h_B(r)=\gamma\quad(|B|=2r+1),\qquad
\gamma\in\{h_B(r-1),h_B(r)\}\quad(|B|=2r)
\tag{6}
\]
for every \(d^0\)-block \(B\). Form \(e\) by arbitrarily recoloring every edge of **one** coordinate direction of \(e^0\). Then
\[
\boxed{E_2(d)\cap E_3(e)\ne\varnothing,}\tag{7}
\]
and again \(\mu(c)\le2\) for the corresponding ambient coloring.

*Proof.* Apply the one-sided signed equitable balancing lemma to the incidence graph of the partitions with the \(d^0\)-side as the side without discrepancy-two exceptions. It gives a vertex \(x\) at which every \(d^0\)-block admits a monochromatic spanning traversal. By complementing coordinates independently within the all-even-degree incidence components, the \(e^0\)-block traversals can be chosen with color words \(0^*1^*\). As explained in the signed-partition proof, interleaving those block traversals yields a long \(e^0\)-geodesic rooted at \(x\) with at most one switch.

Let \(\alpha,\beta\) be the colors of chosen monochromatic \(d^0\)-traversals in the blocks containing \(p,q\). Split each of these traversals into its prefix, distinguished direction, and suffix. The unmodified edges retain their original colors under any interleaving of different blocks, since their reference colors depend only on their own block coordinates.

If \(\alpha=\beta=\eta\), execute the two exceptional-block prefixes and all other monochromatic blocks of color \(\eta\), then the \(p\)-edge, the \(q\)-edge, both exceptional-block suffixes, and finally all remaining blocks, which have color \(1-\eta\). The resulting color word has the form
\[
\eta^*\,\delta_p\,\delta_q\,\eta^*\,(1-\eta)^*.
\tag{8}
\]
The subword \(\eta^*\delta_p\delta_q\eta^*\) has at most two switches, since its nonempty first and last constant phases agree and only two letters intervene; the final phase adds at most one switch. Thus the whole path has at most three switches.

If \(\alpha\ne\beta\), relabel the two distinguished directions so that \(\alpha=0\), \(\beta=1\). Execute the zero-block prefix, its exceptional edge, the one-block prefix, its exceptional edge, the zero-block suffix, and the one-block suffix. Place all other constant-zero blocks into a zero phase and all other constant-one blocks into a one phase. The color word is
\[
0^*\,\delta_p\,1^*\,\delta_q\,0^*\,1^*.
\tag{9}
\]
For every choice of \(\delta_p,\delta_q\), the six-letter template \(0,\delta_p,1,\delta_q,0,1\) has three switches. Empty phases can only reduce that number. Therefore the \(d\)-path has at most three switches. Reversing the two constructed paths gives (5).

Under (6), every balanced \(d^0\)-block admits a monochromatic traversal with the same color \(\gamma\). Interleave all prefixes, then the two exceptional edges, then all suffixes and remaining blocks. The color word is
\[
\gamma^*\,\delta_p\,\delta_q\,\gamma^*,
\]
which has at most two switches. For the adjacent-face coloring \(e\), the change from \(e^0\) affects just one entry in the previously constructed \(0^*1^*\) geodesic's edge-color word. The new word therefore has at most three switches. Both paths are rooted at \(x\), so their reversals terminate at the common vertex \(x\). This proves (7).

Finally, Article VIII's parallel-face switch inequality and the evenness of \(\mu(c)\) yield \(\mu(c)\le2\) from either switch-budget pair \((3,1)\) or \((2,3)\). \(\square\)

The two directions \(p,q\) may carry arbitrarily complicated edge-color functions, involving coordinates of every block. Their membership in separate reference blocks is what permits the requisite ordering of the unmodified monochromatic portions.

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

### Blockwise perturbation and dimension-free phase synchronization

Let \(Q_m=\{0,1\}^m\), \(m\ge2\), and let \(\mathcal P,\mathcal Q\) be partitions of \([m]\). An undirected-edge coloring \(d\) is **separable over** \(\mathcal P\) if, for \(i\in B\in\mathcal P\), its direction-\(i\) edge color depends only on the coordinates in \(B\setminus\{i\}\). Analogously define separability over \(\mathcal Q\). Fix two separable binary colorings \(d^0,e^0\).

For an integer \(t\ge0\), a **blockwise \(t\)-direction perturbation** of \(d^0\) means a coloring \(d\), still separable over \(\mathcal P\), such that, in each block \(B\), the functions \(d_i\) and \(d_i^0\) agree for all but at most \(t\) directions \(i\in B\). In the exceptional directions, \(d_i\) may be an arbitrary function of the other coordinates of \(B\). Apply the analogous definition to \(e^0\) and \(\mathcal Q\). The exceptional directions and the perturbation functions are independent in the two colorings.

For a binary word \(w=w_1\cdots w_\ell\), \(\ell\ge1\), let \(\sigma(w)=\sum_{j<\ell}[w_j\ne w_{j+1}]\) and define
\[
A_\gamma(w)=\sigma(w)+[w_1\ne\gamma],\qquad \gamma\in\{0,1\}.
\tag{1}
\]
For the empty word set \(A_\gamma(\varnothing)=0\).

**Lemma 1 (alternating-phase embedding).** If \(w'\) differs from \(w\) in at most \(t\) positions, then
\[
A_\gamma(w')\le A_\gamma(w)+2t.
\tag{2}
\]
If \(A_\gamma(w')\le L-1\), the letters of \(w'\) can be assigned in order to \(L\) consecutive monochromatic phases with prescribed colors \(\gamma,1-\gamma,\gamma,\ldots\), allowing empty phases.

*Proof.* Recoloring one letter changes at most the two adjacent comparisons; if it is the first letter, it changes at most one comparison and the initial-color penalty. Thus each recoloring increases \(A_\gamma\) by at most two, proving (2). For the embedding, assign the first letter to phase \(1+[w'_1\ne\gamma]\), and advance one phase at every subsequent switch. The last assigned phase is \(1+A_\gamma(w')\le L\). All phase assignments preserve order and match the prescribed phase colors. \(\square\)

**Lemma 2 (interleaving block paths).** Suppose an edge coloring is separable over a partition, and for every block there is a traversal using each of its directions once, starting from the prescribed block coordinates of a common vertex \(x\). If each traversal's color word admits the \(L\)-phase embedding of Lemma 1 with the same initial phase color \(\gamma\), then there is a long geodesic of the full cube starting at \(x\) with at most \(L-1\) switches.

*Proof.* Fix the within-block traversals and their phase assignments. Execute all their first-phase portions, then all their second-phase portions, and so forth. Each direction is traversed once. A block's edge colors depend only on the coordinates of that block, so interleaving other blocks changes none of its chosen edge colors. The resulting word has at most \(L\) monochromatic phases. \(\square\)

**Theorem 3 (common terminals under blockwise perturbations).** Suppose a vertex \(x\in Q_m\) has the following properties:

(a) For every \(B\in\mathcal P\), there is a monochromatic \(d^0\)-traversal of all directions of \(B\) starting at \(x|_B\).

(b) For every \(C\in\mathcal Q\), there is an \(e^0\)-traversal of all directions of \(C\) starting at \(x|_C\), with color word \(0^*1^*\).

Let \(d,e\) be independent blockwise \(t\)-direction perturbations of \(d^0,e^0\), respectively. Then
\[
\boxed{E_{2t+1}(d)\cap E_{2t+1}(e)\ne\varnothing.}
\tag{3}
\]
If in (a) all the monochromatic \(d^0\)-block traversals can be chosen with one common color \(\gamma\), then
\[
\boxed{E_{2t}(d)\cap E_{2t+1}(e)\ne\varnothing.}
\tag{4}
\]

*Proof.* Fix the block traversals from the hypotheses. A traversal uses any specified direction once, so under a blockwise \(t\)-direction perturbation its color word changes at no more than \(t\) places. By Lemma 1, each \(e\)-block traversal satisfies
\[
A_0(w_e)\le 1+2t.
\]
Every initially monochromatic \(d^0\)-block word satisfies \(A_0(w_d^0)\le1\), whatever its color, hence the same bound holds for its perturbed word. Lemma 2, with \(L=2t+2\), constructs long \(d\)- and \(e\)-geodesics starting at \(x\), each having at most \(2t+1\) switches. Their reversals terminate at \(x\), giving (3).

Under the additional assumption, each \(d^0\)-block word is the constant word \(\gamma\), so \(A_\gamma(w_d)\le2t\). Lemma 2 with \(L=2t+1\) gives a \(d\)-geodesic starting at \(x\) with at most \(2t\) switches. The preceding \(e\)-geodesic is unchanged. Reversing both gives (4). \(\square\)

**Corollary 4 (parallel codimension-two faces).** Let \(c\) be an antipodally odd binary coloring of the undirected edges of \(Q_{m+2}\). Suppose two adjacent codimension-two face restrictions, identified with \(Q_m\), are \(d,e\) as in Theorem 3. Then
\[
\mu(c)\le2t+2.
\tag{5}
\]
If the common-color assumption in (4) holds, then
\[
\boxed{\mu(c)\le2t.}
\tag{6}
\]

*Proof.* Article VIII's parallel-face switch bound, for corresponding terminals with \(r,s\) switches, is
\[
\mu(c)\le
\min\{\max(r,2\lceil s/2\rceil),
       \max(s,2\lceil r/2\rceil)\}.
\tag{7}
\]
Using (3) with \(r=s=2t+1\) gives (5). Using (4) with \(r=2t,s=2t+1\) gives \(\mu(c)\le2t+1\). The minimum switch count of a full antipodal geodesic is even, so \(\mu(c)\le2t\). This also covers \(t=0\). \(\square\)

The theorem has an explicit broad family of applications. For a partition \(\mathcal P\), choose shifts \(u\in Q_m\) and arbitrary functions \(h_B:\{0,\ldots,|B|-1\}\to\{0,1\}\), and let
\[
d_i^0(z)=h_{B(i)}\left(\sum_{j\in B(i)\setminus\{i\}}(z_j\oplus u_j)\right).
\tag{8}
\]
Define \(e^0\) independently by a partition \(\mathcal Q\), shifts \(v\), and arbitrary functions \(g_C\).

**Corollary 5 (radial block colorings with many exceptional directions).** Let \(d,e\) be blockwise \(t\)-direction perturbations of the shifted radial colorings (8) for two arbitrary partitions. If they are restrictions of an ambient antipodally odd coloring to adjacent codimension-two faces, then \(\mu(c)\le2t+2\). Suppose further there is \(\gamma\in\{0,1\}\) such that every \(B\in\mathcal P\) satisfies
\[
\begin{cases}
h_B(r)=\gamma,& |B|=2r+1,\\
\gamma\in\{h_B(r-1),h_B(r)\},& |B|=2r.
\end{cases}
\tag{9}
\]
Then \(\mu(c)\le2t\). In particular, **one arbitrarily recolored direction per block on each side**, with no bound on the number of blocks, still implies \(\mu(c)\le2\) under (9).

*Proof.* Apply the one-sided signed equitable balancing lemma of the preceding signed-partition Subsection to the bipartite incidence graph of \(\mathcal P,\mathcal Q\), with incidence shifts \(u,v\) and exceptional side \(\mathcal Q\). It produces a common vertex \(x\) at which every \(\mathcal P\)-block has imbalance at most one, and every \(\mathcal Q\)-block has imbalance at most one except for at most one block of imbalance two in each all-even-degree connected component. The radial block traversal lemma gives monochromatic traversals on every \(\mathcal P\)-block and every ordinary \(\mathcal Q\)-block. An exceptional \(\mathcal Q\)-block has a traversal with at most one change. Complementing all coordinates in its all-even-degree component switches the direction of that transition; choose such complements to make all nonconstant exceptional words \(0^*1^*\). Ordinary monochromatic words also belong to \(0^*1^*\). Thus the hypotheses (a)–(b) of Theorem 3 hold.

If (9) holds, at every balanced \(\mathcal P\)-block the radial traversal lemma permits the constant color \(\gamma\), independent of the signs of the balanced coordinates. Therefore the common-color strengthening also holds. Apply Corollary 4. \(\square\)

The restriction that perturbations remain block-separable is essential to the interleaving proof: moving an edge of one block past the traversal of another must preserve its color. A single arbitrarily dependent exceptional direction, as handled in the preceding Subsection, is covered by a different argument. The results here allow an unbounded number of exceptional directions as \(m\) grows, while keeping the switch bound dependent only on the number of exceptions **per block**.

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

### Root-uniform low-switch geodesics for affine colorings supported on forests

Let \(G\) be a simple graph on \([m]\), and let \(\varepsilon\in\mathbb F_2^m\). Color the undirected coordinate-\(i\) edges of \(Q_m\) by
\[
d_i(z)=\varepsilon_i\oplus\bigoplus_{j:ij\in E(G)}z_j. \tag{1}
\]
The formula is independent of \(z_i\). No antipodal condition is assumed on these face colorings.

**Lemma 1 (indegree parity in trees).** Let \(T\) be a tree, and prescribe \(b_v\in\mathbb F_2\) for each vertex. There is an orientation with \(\deg^-(v)\equiv b_v\pmod2\) at every vertex if and only if
\[
\bigoplus_{v\in V(T)}b_v=|E(T)|\pmod2. \tag{2}
\]
Each orientation of a tree is acyclic and thus is induced by some vertex ordering.

*Proof.* Summing indegrees proves necessity. For sufficiency, orient the edge at a leaf to realize its prescribed parity, remove the leaf, and adjust the target parity at its neighbor if that edge enters the neighbor. The parity identity persists, so induction applies. Any orientation of a tree has a topological ordering. \(\square\)

**Theorem 2 (rooted paths for a tree).** If \(G=T\) is a tree, then for every root \(x\in Q_m\) there is an antipodal spanning geodesic starting at \(x\) with at most one color change. For odd \(m\), a monochromatic path exists at every root. For even \(m\), set
\[
b_i=\varepsilon_i\oplus\bigoplus_{j:ij\in E(T)}x_j.
\]
A monochromatic path from \(x\) exists precisely when
\[
\bigoplus_i b_i=|E(T)|\pmod2. \tag{3}
\]
If (3) fails, a spanning path with its sole switch before the final edge exists.

*Proof.* Given an order \(\pi\) of the directions, orient every graph edge from its earlier to its later endpoint. The color traversed in direction \(i\) is \(b_i\oplus\deg^-_\pi(i)\pmod2\). To obtain the constant word \(\gamma^m\), apply Lemma 1 with indegree targets \(b_i\oplus\gamma\). This is possible if and only if
\[
\bigoplus_i b_i\oplus(m\gamma\bmod2)=|E(T)|\pmod2.
\]
For odd \(m\), choose \(\gamma\) accordingly; for even \(m\), this is (3). Necessity also follows because every graph edge contributes one to the parity sum of the traversed color word.

Now suppose \(m\) is even and (3) fails. Choose a leaf \(v\), set \(\gamma=b_v\), and delete \(v\). Prescribe indegree parity \(b_i\oplus\gamma\) on every vertex \(i\ne v\). The sum of these targets is
\[
\bigoplus_{i\ne v}(b_i\oplus\gamma)
=\bigoplus_i b_i
=|E(T)|\oplus1
=|E(T-v)|\pmod2.
\]
Lemma 1 supplies an orientation and a topological order of \(T-v\). Traverse these coordinates first, then \(v\). The first \(m-1\) edge colors all equal \(\gamma\). Since \(v\)'s unique neighbor has already been flipped, the final color is \(b_v\oplus1=1\oplus\gamma\). \(\square\)

**Theorem 3 (root-uniform two-switch bound for forests).** If \(G\) is a forest, then
\[
\boxed{\forall x\in Q_m\quad
\min_{P:x\to\bar x}\sigma_d(P)\le2.} \tag{4}
\]
If every component of \(G\) has odd order, the upper bound improves to one. The general bound two is sharp for prescribed roots.

*Proof.* Apply Theorem 2 to each tree component at the restriction of the prescribed root. Each component admits a spanning traversal whose word is \(0^*1^*\), \(1^*0^*\), or a constant word. Because (1) couples only coordinates within a component, these traversals may be interleaved while preserving their internal edge colors. Traverse all zero-prefixes of \(0^*1^*\) blocks first; then all one-suffixes of those blocks, all one-prefixes of \(1^*0^*\) blocks, and all constant-one blocks; finally all zero-suffixes of \(1^*0^*\) blocks and all constant-zero blocks. The resulting word has form \(0^*1^*0^*\) and at most two switches. When all components have odd order, choose monochromatic traversals by Theorem 2 and concatenate them according to color.

For sharpness let \(G\) consist of disjoint edges \(12\) and \(34\), with \(x=0000\) and \(\varepsilon=(1,1,0,0)\). The two local traversals necessarily have respective color words \(10\) and \(01\). A global traversal must contain both as subsequences, requiring at least two switches. \(\square\)

**Corollary 4 (unrestricted corresponding endpoints for two forest couplings).** Suppose \(d,e\) are two independent colorings of \(Q_m\) of the form (1), using potentially different forests and constants. Let \(E_s(d)\) be the set of terminals of spanning antipodal geodesics with at most \(s\) switches. Then
\[
\boxed{E_2(d)=E_2(e)=Q_m.} \tag{5}
\]
If one coupling graph is a tree, its rooted switch bound is one. Coordinate shifts in the two colorings are absorbed into the respective constants.

If \(d,e\) are restrictions of an antipodally odd coloring \(c\) of \(Q_{m+2}\) to adjacent parallel codimension-two faces, coordinate identification yields corresponding terminal vertices for paths with at most two switches. Article VIII's parallel-face bound therefore gives
\[
\boxed{\mu(c)\le2.} \tag{6}
\]

*Proof.* To realize a prescribed terminal \(y\), apply Theorem 3 at root \(\bar y\). Both forest colorings therefore admit paths with terminal \(y\). Apply the parallel-face switch bound. \(\square\)

**Corollary 5 (hereditary rooted closure).** For every face \(H\) of \(Q_m\), every vertex \(x\in H\) starts a geodesic spanning \(H\) with at most two switches under \(d|_H\). Indeed, fixing coordinates outside \(H\) changes only the constants in (1), and the induced graph on its free directions remains a forest. Apply Theorem 3 within \(H\).

This theorem includes arbitrary paths and branching trees as interaction graphs. For example, the four-coordinate path \(1-2-3-4\) gives \(d_1=\varepsilon_1\oplus z_2\), \(d_2=\varepsilon_2\oplus z_1\oplus z_3\), \(d_3=\varepsilon_3\oplus z_2\oplus z_4\), and \(d_4=\varepsilon_4\oplus z_3\), which is beyond disjoint block-radial couplings.

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

##### Sharp square-derivative deficits and terminal holes

Let \(n\ge3\) be odd. For an antipodally odd coloring \(c\) of undirected edges of \(Q_n\), write \(c_i(x)\) for the color of \(\{x,x^i\}\). Then
\[
c_i(x^i)=c_i(x),\qquad c_i(\bar x)=1+c_i(x).
\tag{1}
\]
All color arithmetic is in \(\mathbb F_2\). Write \(\mu(c)\) for the minimum switch count on a long geodesic of \(Q_n\).

For distinct directions \(i,j\), each \((i,j)\)-square is indexed by a projected vertex \(z\in Q_{[n]\setminus\{i,j\}}\). Its cross-derivatives
\[
d_{ij}(z)=c_i(x)+c_i(x^j),\qquad
d_{ji}(z)=c_j(x)+c_j(x^i)
\tag{2}
\]
are independent of the omitted bits of \(x\). Set
\[
B_{ij}=\{z:(d_{ij}(z),d_{ji}(z))\ne(1,1)\},\quad
D=\sum_{i<j}|B_{ij}|,
\tag{3}
\]
\[
Z_i=\sum_{j\ne i}|\{z:d_{ij}(z)=0\}|,\qquad
K=\sum_{i<j}|\{z:d_{ij}(z)+d_{ji}(z)=1\}|.
\tag{4}
\]

**Theorem 1 (sharp bound and rigidity).** Every coloring satisfying (1) in odd dimension has
\[
Z_i\ge2^{n-2}\ (i\in[n]),\qquad K\ge2^{n-2},\qquad
\boxed{D\ge(n+1)2^{n-3}.}
\tag{5}
\]
The final bound is sharp for every odd \(n\ge3\). Equality holds precisely for colorings
\[
\boxed{c_i(x)=a_i+\sum_{j\notin\{i,p(i)\}}x_j,}
\tag{6}
\]
where \(a_i\in\mathbb F_2\) and the directed partner map \(p\) pairs \(n-1\) coordinates into reciprocal pairs, with the remaining coordinate \(w\) pointing to a member of one pair. Every coloring of form (6) admits a monochromatic long geodesic. Consequently,
\[
\boxed{\mu(c)\ge4\ \Longrightarrow\ D\ge(n+1)2^{n-3}+2.}
\tag{7}
\]

*Proof.* Fix direction \(i\), and regard \(c_i\) as a function of the \(d=n-1\) other bits \(y\), where \(d\) is even. Put
\[
f_i(y)=(-1)^{c_i(y)+\sum_{j\ne i}y_j}.
\tag{8}
\]
Antipodal oddness gives \(f_i(\bar y)=-f_i(y)\), so its mean is zero. The value of \(f_i\) changes along a \(j\)-edge precisely when \(d_{ij}=0\). In the Walsh expansion \(f_i=\sum_S\widehat f_i(S)\chi_S\), Parseval and the elementary directional-edge count give
\[
Z_i=2^{d-1}\sum_{S\ne\varnothing}|S|\widehat f_i(S)^2
\ge2^{d-1}\sum_{S\ne\varnothing}\widehat f_i(S)^2
=2^{n-2}.
\tag{9}
\]
Equality forces Fourier degree one. Since \(f_i^2=1\), writing \(f_i=\sum_j b_j\chi_{\{j\}}\) and comparing the coefficients of \(\chi_{\{j,k\}}\) gives \(b_jb_k=0\) for distinct \(j,k\). Thus \(f_i\) is a signed coordinate character. Reversing (8), equality in (9) is equivalent to
\[
c_i(x)=a_i+\sum_{j\notin\{i,p(i)\}}x_j
\quad\text{for some }p(i)\ne i.
\tag{10}
\]

For the curvature count, fix a direction ordering \(\pi\), and reverse it through \(\binom n2\) adjacent swaps, each unordered pair of directions crossing once. At any root \(x\), the color word for the reversed order is the complemented reversal of the original word, by (1). Their color sums therefore differ by \(n=1\pmod2\). Each adjacent swap changes that sum by \(d_{ij}+d_{ji}\) at the intervening square. Hence an odd number of the squares in the swap sequence have nonzero curvature at every root. Summing over \(2^n\) roots, each square is counted four times: its swapped directions and earlier direction set are fixed, while the two square-coordinate bits of the root vary freely. Therefore \(4K\ge2^n\), proving the middle bound in (5).

A square with derivative pair \((1,1)\) contributes \(0,0,0\) to the counts \((D,\sum_iZ_i,K)\). A square with \((0,0)\) contributes \((1,2,0)\); a square with \((1,0)\) or \((0,1)\) contributes \((1,1,1)\). Thus
\[
2D=\sum_iZ_i+K\ge(n+1)2^{n-2},
\tag{11}
\]
proving the last bound in (5).

Equality in (11) forces equality in (9) for every \(i\) and equality in the curvature bound. Hence (10) holds for every direction. In that case,
\[
d_{ij}+d_{ji}=[p(i)=j]+[p(j)=i]
\tag{12}
\]
is constant over all \((i,j)\)-squares. Since \(K=2^{n-2}\), there is precisely one unordered direction pair with a nonreciprocal partner relation. The directed graph of \(p\) has one outgoing arc at each vertex; all but one arcs belong to reciprocal pairs. Its structure is therefore the paired map with one unmatched vertex described in the theorem. Conversely, that map has \(Z_i=2^{n-2}\) for all \(i\), and one direction pair of nonzero curvature, so it attains (5).

We prove monochromaticity for every equality coloring, allowing arbitrary constants \(a_i\). Write the reciprocal pairs as \(\{u_r,v_r\}\), \(1\le r\le m=(n-1)/2\), with unmatched vertex \(w\). Choose a permutation of directions, with position \(t_i\) for direction \(i\), such that
\[
t_{u_r}+t_{v_r}=1+a_{u_r}+a_{v_r}\pmod2.
\tag{13}
\]
This permutation exists by assigning the pairs successively to positions of the required parities. Among any odd number of unused positions, one parity class has one more position than the other. For a required same-parity pair, use two positions of the larger class; for a required opposite-parity pair, use one position of each class. The remaining classes again differ by one, and the final unused position is assigned to \(w\).

Let \(S_i\) be the directions preceding \(i\) in this permutation and set
\[
\eta_i=a_i+(t_i-1)+[p(i)\in S_i].
\tag{14}
\]
Equation (13) ensures \(\eta_{u_r}=\eta_{v_r}=:\eta_r\). Choose arbitrary bits \(T,q\). Prescribe the root-coordinate pair sums
\[
s_r=x_{u_r}+x_{v_r}=T+q+\eta_r,
\tag{15}
\]
set \(x_w=T+\sum_rs_r\), and set \(x_{p(w)}=T+q+\eta_w+x_w\). Complete the remaining root bits so that all prescribed pair sums hold; the conditions are compatible since \(p(w)\) belongs to one reciprocal pair. These assignments give \(\sum_i x_i=T\). At the step traversing direction \(i\), equation (6) now yields
\[
c_i(x^{S_i})
=T+x_i+x_{p(i)}+\eta_i=q
\tag{16}
\]
for each paired direction by (15), and also for \(w\) by its prescribed coordinate. Thus the full path is monochromatic.

Antipodal complementation preserves both cross-derivatives of every square, and pairs the projected vertices \(z,\bar z\). Since \(n-2\ge1\), those vertices differ, and \(D\) is even. Any coloring with \(\mu(c)\ge4\) lies outside the equality family by the preceding construction, giving the strict even-integer bound (7). \(\square\)

**Theorem 2 (global terminal-hole obstruction).** Assume \(n\ge5\) odd. For each pair \(i<j\), consider the four codimension-two faces obtained by fixing bits \(i,j\), and project their long-geodesic terminals with at most two switches onto the common \(Q_{n-2}\). Let \(H_{ij}\) be the complement of the union of these four projected terminal sets. If \(\mu(c)\ge4\), then
\[
\boxed{B_{ij}\subseteq H_{ij}\quad(i<j),}
\tag{17}
\]
\[
\boxed{\sum_{i<j}|H_{ij}|\ge(n+1)2^{n-3}+2,\qquad
\sum_{j\ne i}|H_{ij}|\ge2^{n-2}\quad(i\in[n]).}
\tag{18}
\]
Furthermore, fix a direction \(i\) and identify the direction-\(i\) edges of \(Q_n\) with vertices of \(Q_{n-1}\). Along every long geodesic of this edge-position cube, an odd number of crossed edges have \(d_{ij}=0\), where \(j\) is the crossed direction. Each corresponding \((i,j)\)-square belongs to \(H_{ij}\) under projection.

*Proof.* Suppose a projection \(z\) is the terminal of a long geodesic \(P\) with at most two switches in one of the four \((n-2)\)-faces. Write \(x\) for its terminal corner and \(q\) for its last color. When \(\mu(c)\ge4\), \(P\) must have two switches: appending both exterior directions to a path with at most one switch would produce at most three switches, implying \(\mu(c)\le2\) by the evenness of \(\mu(c)\). Append the two exterior directions to \(P\) in either order. Each full geodesic has at most four switches and therefore must have four. Both added comparisons must be switches. The two square edges leaving \(x\) have color \(1+q\), and the two entering its opposite corner have color \(q\). It follows that \(d_{ij}(z)=d_{ji}(z)=1\). This proves (17). The bounds (18) follow from (17), (5), (7), and the definition of \(Z_i\).

For the last assertion, a long geodesic in the edge-position cube joins \(y\) to \(\bar y\) and has \(n-1\) edges. The sum of its crossed derivatives is \(c_i(y)+c_i(\bar y)=1\). Since \(n-1\) is even, an odd number of these derivatives vanish. Each vanishing derivative marks a square belonging to \(B_{ij}\subseteq H_{ij}\). \(\square\)

**Corollary (a two-switch certificate).** In odd dimension \(n\ge5\), the inequality
\[
\sum_{i<j}|H_{ij}|\le(n+1)2^{n-3}+1
\tag{19}
\]
implies \(\mu(c)\le2\).

The directional constraint applies to every antipodal geodesic in each edge-position cube and couples the four-face terminal sets across all exterior direction pairs. No antipodal symmetry is assumed for the edge coloring restricted to an individual face.

##### Simultaneous square defects and antipodal facet exchanges

Let \(n\ge5\) be odd. Color the undirected edges of \(Q_n=\{0,1\}^n\) by bits \(c_i(x)\), where \(c_i(x)\) denotes the edge incident with \(x\) in direction \(i\), and assume
\[
c_i(x^i)=c_i(x),\qquad c_i(\bar x)=1+c_i(x).
\tag{1}
\]
Arithmetic of colors is in \(\mathbb F_2\). For \(i\ne j\), put
\[
d_{ij}(x)=c_i(x)+c_i(x^j).
\tag{2}
\]
This depends only on the \((i,j)\)-square containing \(x\).

Triangulate each facet of the geometric cube \([0,1]^n\) by its Freudenthal (monotone-chain) simplices, consistently on intersecting facets. The resulting complex \(\mathcal T\) triangulates \(\partial[0,1]^n\cong S^{n-1}\). Its maximal simplices have as vertices the \(n\) successive corners of a geodesic traversing every free direction of one coordinate facet, starting with all its free bits zero. Call these *facet chains*. Two facet chains are adjacent if their maximal simplices share a codimension-one simplex, equivalently if their sets of \(n\) vertices share \(n-1\) vertices. Cube complementation sends each facet chain, with its order reversed, to another facet chain.

For a nonempty \(I\subseteq[n]\), call a facet chain \(P=(v_0,\ldots,v_{n-1})\) **\(I\)-defect-complete** when, for every \(i\in I\), there is a step \(v_t\to v_{t+1}=v_t^j\) with \(j\ne i\) and
\[
d_{ij}(v_t)=0.
\tag{3}
\]
Let \(\Gamma_I\) be the graph induced by these chains under the preceding adjacency.

**Theorem 1 (simultaneous defect carriers).** For every nonempty \(I\subseteq[n]\) with \(|I|\le n-1\), the graph \(\Gamma_I\) has a vertex. If
\[
1\le |I|\le n-2,
\tag{4}
\]
then \(\Gamma_I\) has a connected component preserved by cube complementation. In particular, there is a sequence
\[
P_0,P_1,\ldots,P_s=\bar P_0
\tag{5}
\]
of \(I\)-defect-complete facet chains such that successive chains share \(n-1\) vertices. All conclusions hold for arbitrary colorings satisfying (1).

*Proof.* For \(i\in[n]\) define at each cube vertex
\[
a_i(x)=(-1)^{\,c_i(x)+\sum_{h\ne i}x_h}.
\tag{6}
\]
Since \(n-1\) is even, (1) gives \(a_i(\bar x)=-a_i(x)\). Moreover, \(a_i(x^i)=a_i(x)\), whereas for \(j\ne i\),
\[
a_i(x^j)=-a_i(x)\quad\Longleftrightarrow\quad d_{ij}(x)=0.
\tag{7}
\]
For \(I=\{i_1,\ldots,i_r\}\), assign the vector
\(a_I(x)=(a_{i_1}(x),\ldots,a_{i_r}(x))\in\{-1,1\}^r\)
to the vertices of \(\mathcal T\), and extend affinely over every simplex. This defines a continuous map
\[
A_I:|\mathcal T|\longrightarrow\mathbb R^r,\qquad
A_I(\bar z)=-A_I(z),
\tag{8}
\]
because the Freudenthal triangulation of the cubical boundary is preserved by complementation.

When \(r\le n-1\), Borsuk–Ulam applied to
\(|\mathcal T|\cong S^{n-1}\) gives \(z\) with \(A_I(z)=0\). Choose a maximal simplex \(\sigma\) containing \(z\), and let \(P\) be its facet chain. The zero vector is a convex combination of the vectors \(a_I(v)\) at vertices of \(P\). For each \(i\in I\), both signs therefore occur among the \(a_i\)-values along \(P\). Some consecutive vertices of \(P\) have opposite \(a_i\)-values; equation (7) shows that this step has direction \(j\ne i\) and satisfies (3). Thus \(P\) belongs to \(\Gamma_I\).

Assume next that \(r\le n-2\), and let \(Z=A_I^{-1}(0)\). It is a nonempty finite polyhedron with finitely many connected components, preserved as a collection by complementation. We show that some component \(W\) satisfies \(\bar W=W\). Otherwise, the components can be divided into two disjoint closed unions \(Z_+\), \(Z_-\) interchanged by complementation. With distance measured in the ambient Euclidean space, define
\[
g(z)=\operatorname{dist}(z,Z_-)-\operatorname{dist}(z,Z_+)
\quad(z\in|\mathcal T|).
\tag{9}
\]
Then \(g\) is continuous and odd, and \(g\ne0\) on \(Z\). The map \((A_I,g):S^{n-1}\to\mathbb R^{r+1}\) is consequently odd and nowhere zero, contrary to Borsuk–Ulam because \(r+1\le n-1\). This proves the existence of \(W\).

Let \(\mathcal D\) be the graph of maximal simplices meeting \(Z\), joined across codimension-one faces. All such simplices give \(I\)-defect-complete chains by the first part of the proof. The maximal simplices containing any one point \(z\in Z\) are ridge-connected: they constitute the maximal simplices of the star of the minimal face supporting \(z\), whose link in the triangulated sphere is connected in its facet-adjacency graph. Consequently two components of \(\mathcal D\) cannot have closed unions meeting at a point of \(Z\). The connected set \(W\) therefore meets maximal simplices in a single component \(D\) of \(\mathcal D\). Since \(\bar W=W\), this component is preserved by complementation. It lies in \(\Gamma_I\); the component of \(\Gamma_I\) containing \(D\) is also preserved by complementation. Choosing any chain in it and connecting it by graph edges to its complement proves (5). \(\square\)

For each \(i<j\), project the four codimension-two faces with fixed directions \(i,j\) onto the common \(Q_{n-2}\), and let \(H_{ij}\) be the complement of the union of the projected terminals of their spanning geodesics with at most two color changes.

**Corollary 2 (simultaneous terminal-hole exchanges).** Suppose \(\mu(c)\ge4\). For any \(I\subseteq[n]\), \(|I|\le n-1\), there exists a facet chain \(P\) such that for every \(i\in I\), one of its steps in a direction \(j\ne i\) lies on an \((i,j)\)-square whose projection belongs to \(H_{\min(i,j),\max(i,j)}\). For \(1\le |I|\le n-2\), the graph of facet chains with this property has a complementation-invariant connected component, and consequently contains an antipodal exchange sequence as in (5).

*Proof.* The terminal-hole theorem for odd-dimensional cubes gives
\[
d_{ij}(x)=0\quad\Longrightarrow\quad
x|_{[n]\setminus\{i,j\}}\in H_{\min(i,j),\max(i,j)}
\tag{10}
\]
under \(\mu(c)\ge4\): a square with \(d_{ij}=0\) cannot have both cross-derivatives equal to one. Each step certified by (3) therefore certifies the required terminal hole. The asserted graph contains \(\Gamma_I\), is preserved by complementation, and consequently has an invariant connected component whenever \(\Gamma_I\) does. \(\square\)

The conclusion couples terminal holes for as many as \(n-1\) selected directions along one facet chain, and for \(n-2\) directions along an antipodally connected exchange family. A terminal-hole certificate specifies an excluded endpoint of a short face geodesic; it does not provide a short geodesic through that point. In particular, the theorem supplies a global connectivity constraint on the holes of a hypothetical four-switch coloring, while the corresponding-low-switch-terminal intersection required for the Article X induction remains open.

##### Antipodally connected galleries of simultaneous square defects

Let \(n\ge3\) be odd, and let \(c\) be a binary coloring of the undirected edges of \(Q_n\) satisfying \(c(\bar e)=1-c(e)\). Write \(c_i(x)\) for the color of the direction-\(i\) edge at \(x\), so that
\[
c_i(x^i)=c_i(x),\qquad c_i(\bar x)=1-c_i(x).
\]
For distinct \(i,j\), put \(d_{ij}(x)=c_i(x)+c_i(x^j)\) in \(\mathbb F_2\). This derivative depends only on the \((i,j)\)-square containing \(x\).

Let \(T\) be the restriction to \(\partial[0,1]^n\) of the Freudenthal triangulation of the cube. Its vertices are those of \(Q_n\); its maximal simplices are the chains in coordinate facets, each encoding a geodesic traversing the \(n-1\) free directions of that facet. Complementation \(\tau(x)=\bar x\) is a simplicial involution of \(T\).

Define vertex signs
\[
g_i(x)=(-1)^{\,c_i(x)+\sum_{j\ne i}x_j},\qquad i\in[n]. \tag{1}
\]
Since \(n-1\) is even,
\[
g_i(\bar x)=-g_i(x),\qquad g_i(x^i)=g_i(x),\qquad
g_i(x^j)=-g_i(x)\ \Longleftrightarrow\ d_{ij}(x)=0
\quad(j\ne i). \tag{2}
\]
Fix a nonempty \(I\subseteq[n]\). Call a simplex of \(T\) *\(I\)-mixed* when, for each \(i\in I\), both signs of \(g_i\) occur among its vertices. Define a graph \(\mathcal G_I\) whose vertices are the maximal \(I\)-mixed simplices of \(T\), with two joined when they share an \(I\)-mixed codimension-one face. The involution \(\tau\) acts on this graph.

**Theorem 1 (connected antipodal square-defect gallery).** For every \(I\subseteq[n]\) with \(1\le |I|\le n-2\), the graph \(\mathcal G_I\) has a connected component invariant under \(\tau\). Every simplex represented by a vertex of \(\mathcal G_I\) encodes a geodesic \(P\) in a coordinate facet such that for each \(i\in I\) some step of \(P\), in a direction \(j\ne i\), lies on an \((i,j)\)-square satisfying
\[
d_{ij}=0. \tag{3}
\]
The threshold \(n-2\) cannot be replaced by \(n-1\) for arbitrary antipodally odd edge colorings.

We first record the connectivity principle underlying the theorem.

**Lemma 2 (connected zero component).** Let \(S^d\) have a finite antipodally invariant triangulation, and let \(F:S^d\to\mathbb R^k\) be an odd piecewise-linear map, where \(1\le k\le d-1\). Then \(F^{-1}(0)\) has a connected component invariant under the antipodal involution.

*Proof.* Borsuk–Ulam makes \(Z=F^{-1}(0)\) nonempty. As the zero set of a map affine on finitely many simplices, \(Z\) is a finite polyhedron and has finitely many connected components. Suppose the involution exchanges the components in disjoint pairs. Assign the constants \(+1\) and \(-1\) to the two components in each pair. This defines a continuous odd map \(h:Z\to\{-1,1\}\). Extend \(h\) to a continuous real function \(h_0\) on \(S^d\), and replace the extension with \((h_0(x)-h_0(-x))/2\). The resulting function \(H\) is odd and agrees with \(h\) on \(Z\). The map
\[
x\longmapsto(F(x),H(x))\in\mathbb R^{k+1}
\]
is odd and nowhere zero: \(F\ne0\) off \(Z\), while \(H=\pm1\) on \(Z\). Since \(k+1\le d\), this contradicts Borsuk–Ulam. Thus some component of \(Z\) is invariant. \(\square\)

*Proof of Theorem 1.* Extend the vertex functions \(g_i\), \(i\in I\), affinely across the simplices of \(T\), obtaining \(F_I:|T|\to\mathbb R^{|I|}\). Equation (2) and antipodal invariance of \(T\) make \(F_I\) continuous and odd. Since \(|T|\cong S^{n-1}\) and \(|I|\le n-2\), Lemma 2 gives a connected \(\tau\)-invariant component \(Z_0\) of \(F_I^{-1}(0)\).

If \(z\in Z_0\) and \(\rho\) is the smallest simplex containing \(z\), then \(0=F_I(z)\) is a convex combination of the vectors \((g_i(v))_{i\in I}\) at vertices \(v\) of \(\rho\). Because each coordinate of each vertex vector is \(\pm1\), both signs occur on \(\rho\) for every \(i\in I\). Thus \(\rho\) and all its containing simplices are \(I\)-mixed.

Consider the maximal simplices meeting \(Z_0\). The finite closed cover of the connected space \(Z_0\) by their intersections with \(Z_0\) has connected intersection graph. Whenever two of these maximal simplices share a point \(z\in Z_0\), their common face contains the smallest simplex \(\rho\) containing \(z\). The maximal simplices containing \(\rho\) form a ridge-connected gallery in the triangulated sphere. Each intermediate ridge contains \(\rho\), hence is \(I\)-mixed. Therefore the maximal simplices meeting \(Z_0\) belong to one connected component of \(\mathcal G_I\). Their collection is invariant under \(\tau\), so that component is invariant as well.

For the path assertion, write the vertices of a maximal simplex as a chain \(v_0,\ldots,v_{n-1}\) with successive cube edges in the free directions of its facet. For each \(i\in I\), the signs \(g_i(v_s)\) cannot be constant. At some successive pair they differ. The traversed direction \(j\) differs from \(i\), since \(g_i\) is unchanged across direction-\(i\) edges. Equation (2) then gives \(d_{ij}=0\) on the square through that step. This proves (3).

To see sharpness, for \(1\le i<n\) define
\[
c_i(x)=x_{i+1}+\sum_{j\ne i}x_j\pmod2,
\]
and put \(c_n(x)=x_1\). Each function is independent of its own direction bit and is antipodally odd because \(n\) is odd. For \(I=[n-1]\), equation (1) yields \(g_i(x)=(-1)^{x_{i+1}}\). A maximal boundary simplex is \(I\)-mixed precisely when it lies in one of the two facets \(x_1=0\) or \(x_1=1\): in these facets its vertex chain traverses every direction \(2,\ldots,n\), whereas any other facet fixes some \(x_{i+1}\). The two families have no adjacency in \(\mathcal G_I\), and complementation exchanges them. Hence no connected component is invariant. \(\square\)

**Proposition 4 (one simultaneous facet chain at the next threshold).** For any \(I\subseteq[n]\) with \(|I|=n-1\), there exists a geodesic spanning a coordinate facet such that, for every \(i\in I\), one of its steps lies in a direction \(j\ne i\) on a square with \(d_{ij}=0\).

*Proof.* The vertex signs \(g_i\) of (1), for \(i\in I\), extend to the odd piecewise-linear map \(F_I:S^{n-1}\to\mathbb R^{n-1}\) used above. Borsuk–Ulam supplies a zero in some maximal simplex of \(T\). On the vertex chain of that simplex, each \(g_i\) takes both signs, so (2) provides the required step. The sharpness construction in Theorem 1 shows why existence here cannot be strengthened to a connected antipodally invariant mixed-ridge gallery. \(\square\)

**Corollary 3 (connected terminal-hole galleries under a four-switch obstruction).** Suppose \(n\ge5\) is odd and \(\mu(c)\ge4\). For \(i<j\), let \(H_{ij}\subseteq Q_{n-2}\) be the complement of the union of the projected terminal sets of spanning geodesics having at most two switches in the four codimension-two faces perpendicular to \(i,j\). For every \(I\subseteq[n]\) with \(|I|\le n-2\), there is a connected, antipodally invariant gallery of coordinate-facet geodesics such that every geodesic in the gallery, for each \(i\in I\), crosses some edge in direction \(j\ne i\) whose associated \((i,j)\)-square projects to a point of \(H_{ij}\).

*Proof.* Under \(\mu(c)\ge4\), every square with \(d_{ij}=0\) projects into \(H_{ij}\). Indeed, if its projection were the terminal of a spanning face geodesic with at most two switches, appending the exterior directions \(i,j\) in either order would produce a full geodesic with at most four switches. The evenness of \(\mu(c)\) forces the face path to have two switches and both full completions to have four, which in turn forces both derivatives of the terminal square to equal one, a contradiction. Apply Theorem 1. \(\square\)

The corollary supplies a connected antipodal carrier of simultaneously witnessed square defects. The witnesses are facet geodesics along which zero derivatives occur; their edge-color words may have arbitrarily many switches. An endpoint-coincidence conclusion would additionally require a theorem relating the connected defect gallery to the terminal sets of low-switch paths. Neither connectedness nor the zero-set theorem supplies that extraction.

###### Even-character simultaneous square witnesses

The preceding gallery construction extends to arbitrary even coordinate masks and to either parity of the cube dimension. Let \(n\ge3\), and let \(c_i(v)\) be the colors of an antipodally odd undirected-edge coloring of \(Q_n\). For \(i\ne j\), write \(d_{ij}(v)=c_i(v)+c_i(v^j)\) in \(\mathbb F_2\).

Fix an indexed family \(\mathcal A=((i_\alpha,S_\alpha))_{\alpha=1}^r\), where \(i_\alpha\in[n]\) and \(S_\alpha\subseteq[n]\setminus\{i_\alpha\}\) has even cardinality. Repeated directions are permitted. Call a facet chain \(P=(v_0,\ldots,v_{n-1})\) a witness for \(\mathcal A\) if, for each \(\alpha\), some step \(v_t\to v_{t+1}=v_t^{j}\), with \(j\ne i_\alpha\), satisfies
\[
d_{i_\alpha j}(v_t)\ne \mathbf1_{\{j\in S_\alpha\}}. \tag{4}
\]

**Theorem 5 (simultaneous even-character galleries).** If \(r\le n-1\), some facet chain witnesses \(\mathcal A\). If \(r\le n-2\), the graph of witnessing facet chains, adjacent when their simplices share a codimension-one face in the Freudenthal triangulation of \(\partial[0,1]^n\), contains a connected component invariant under complementation. The bound \(r\le n-2\) for invariant connectivity is sharp, in every dimension \(n\ge3\).

*Proof.* For each \(\alpha\), assign the sign
\[
g_\alpha(v)=(-1)^{\,c_{i_\alpha}(v)+
                       \sum_{j\in S_\alpha}v_j}. \tag{5}
\]
The exponent is modulo two. Since \(c_{i_\alpha}(\bar v)=1+c_{i_\alpha}(v)\) and \(|S_\alpha|\) is even, \(g_\alpha(\bar v)=-g_\alpha(v)\). Because \(i_\alpha\notin S_\alpha\), the sign is constant along direction-\(i_\alpha\) edges. Along a direction-\(j\) edge, its sign changes precisely when
\[
d_{i_\alpha j}(v)+\mathbf1_{\{j\in S_\alpha\}}=1, \tag{6}
\]
equivalently when (4) holds.

Affinely extend the \(r\) vertex signs to a map \(G:|\mathcal T|\to\mathbb R^r\) on the antipodally invariant Freudenthal triangulation \(\mathcal T\) of the cubical boundary. The map is continuous and odd. When \(r\le n-1\), Borsuk--Ulam gives \(z\in G^{-1}(0)\). Each coordinate of the vertex images is a sign. Thus every maximal simplex containing \(z\) has both signs in each coordinate. Its ordered vertex chain has a sign-changing step for each \(\alpha\), which witnesses (4) by (6).

When \(r\le n-2\), Lemma 2 (connected zero component) above gives an antipodally invariant connected component of \(G^{-1}(0)\). The star-and-ridge argument in the proof of Theorem 1 carries this component into a single connected component of witnessing maximal simplices, preserved by complementation. This proves the first two assertions.

For sharpness, set \(c_i(v)=v_{i+1}\) for \(i<n\), and \(c_n(v)=v_1\). This coloring is undirected-edge well defined and antipodally odd. Choose \(r=n-1\) and \((i_\alpha,S_\alpha)=(\alpha,\varnothing)\), \(\alpha=1,\ldots,n-1\). For every \(i<n\), the sole direction \(j\) in which \(d_{ij}=1\) is \(j=i+1\). A witnessing facet chain must therefore traverse every direction \(2,\ldots,n\), forcing its fixed direction to be \(1\). Witnessing chains occur in the two opposite facets \(v_1=0\) and \(v_1=1\). These facets are disjoint, so no adjacency component contains chains from both; complementation exchanges the two collections. Hence no component is invariant. \(\square\)

**Corollary 6 (simultaneous derivatives of both values).** Let \(n\ge5\) be odd and \(I\subseteq[n]\) satisfy \(2|I|\le n-2\). There is an antipodally invariant connected gallery of facet-spanning geodesics in which every geodesic, for each \(i\in I\), crosses both (possibly distinct) squares with
\[
d_{ij}=0\quad\text{and}\quad d_{ik}=1,
\qquad j,k\ne i. \tag{7}
\]
The two derivative witnesses may use different directions and positions.

*Proof.* For each \(i\in I\), insert the two constraints \((i,\varnothing)\) and \((i,[n]\setminus\{i\})\) into \(\mathcal A\). Both masks have even size because \(n\) is odd. Equation (4) for the empty mask forces derivative one, while (4) for the full exterior mask forces derivative zero. Apply Theorem 5 with \(r=2|I|\). \(\square\)

These simultaneous witnesses hold without restrictions on the dependence of individual edge colors. They refine the square-defect carrier theorem by including both derivative signs and repeated coordinate constraints. The gallery certifies square crossings; a low-switch geodesic still requires an additional extraction argument.
