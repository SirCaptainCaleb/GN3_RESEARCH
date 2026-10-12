# Blockwise perturbation and dimension-free phase synchronization

# Blockwise perturbation and dimension-free phase synchronization

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
