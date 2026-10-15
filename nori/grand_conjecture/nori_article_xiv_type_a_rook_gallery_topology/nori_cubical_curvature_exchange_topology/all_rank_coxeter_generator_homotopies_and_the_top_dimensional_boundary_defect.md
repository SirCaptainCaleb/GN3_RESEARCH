# All-rank Coxeter generator homotopies and the top-dimensional boundary defect

# All-rank Coxeter-generator homotopies and the top boundary defect

This extends the all-rank antipodal cubical resolution of Article XIV, Subsection 33, from a collection of chains indexed by full geodesics to an explicit **chain homotopy under every type-\(B_n\) simple Coxeter generator**, in every rank. The existing three-cube adjacent-swap theorem (Subsection 32) is the rank-two case of one uniform formula. The root-flip generator admits a parallel formula. No edge coloring is restricted.

Work over \(\mathbb F_2\). A complete geodesic flag is \(g=(x,\pi)\), where \(\pi=(d_0,\ldots,d_{n-1})\) is an ordered list of all dimensions. The type-\(B_n\) generators are \(s_0\), which flips the initial-root bit in dimension \(d_0\) without changing \(\pi\), and \(s_i\) for \(1\le i<n\), which transposes dimensions in positions \(i-1,i\), keeping the root fixed. Put \(N=1+\tau\), where \(\tau\) is central cube antipodality.

For any set \(U\subseteq\{0,\ldots,n-1\}\) and any bit function \(q\) on its complement, denote by \([U;q]_x\) the cubical face whose free dimensions are \(d_j\), \(j\in U\), and whose remaining bit in dimension \(d_j\) is \(x_{d_j}+q(j)\). The all-rank chain \(E_k(g)\) has one face for each \(k\)-subset \(U\), with
\[
E_k(g)=\sum_{|U|=k}[U;q_U]_x,\qquad
q_U(j)=|\{r\in U:r>j\}|\pmod2\quad(j\notin U).
\tag{1}
\]
It obeys \(\partial E_k(g)=NE_{k-1}(g)\).

## Theorem 1 (homotopy for every adjacent-swap generator)

For \(s_i\), \(1\le i<n\), write \(A_i=\{i-1,i\}\). Define \(H_0(g,s_i)=0\), and for \(1\le k\le n-1\) put
\[
\boxed{
H_k(g,s_i)=
\sum_{\substack{R\subseteq[n]_0\setminus A_i\\|R|=k-1}}
[A_i\cup R;q_{i,R}]_x,\qquad
q_{i,R}(j)=
|\{r\in R:r>j\}|+\mathbf1_{\{j<i-1\}}\pmod2,
}
\tag{2}
\]
where \([n]_0=\{0,\ldots,n-1\}\). Then \(H_k(g,s_i)\) contains precisely
\(\binom{n-2}{k-1}\) faces of dimension \(k+1\), and
\[
\boxed{
E_k(g)+E_k(gs_i)
=\partial H_k(g,s_i)+NH_{k-1}(g,s_i),
\qquad 1\le k\le n-1.
}
\tag{3}
\]
At \(k=1\), \(H_1\) is the local square exchanged by the two full geodesics. At \(k=2\), \(H_2\) is the sum of the \(n-2\) three-cubes of Subsection 32.

*Proof.* Compare the face indexed by a fixed \(k\)-subset \(U\) in (1) before and after swapping positions \(i-1,i\). If \(U\) contains both swapped positions, or neither, the face is unchanged, and the two copies cancel. Otherwise \(U\) contains one position of \(A_i\) and some \((k-1)\)-subset \(R\) of the other positions. As \(U\) runs over the two choices of its member in \(A_i\), the four resulting faces (two from each chain) are the four side facets of the single \((k+1)\)-face \([A_i\cup R;q_{i,R}]_x\), with the two exchanged dimensions left free.

The other boundary facets arise by fixing one of the positions \(r\in R\). For each fixed set \(R'\) of size \(k-2\), these facets assemble, as \(r\) runs through the remaining positions in ascending order, into the successive links of a monotone path between the face \([A_i\cup R';q_{i,R'}]_x\) and its antipodal face. Their total modulo-two boundary is \(N[A_i\cup R';q_{i,R'}]_x\). Summing over \(R'\) proves (3). The initial case \(k=1\) has no remaining \(R\)-facets. \(\square\)

## Theorem 2 (homotopy for the root-flip generator)

For \(s_0\) and \(0\le k\le n-1\), define
\[
\boxed{
H_k(g,s_0)=
\sum_{\substack{R\subseteq\{1,\ldots,n-1\}\\|R|=k}}
[\{0\}\cup R;q_R]_x,\qquad
q_R(j)=|\{r\in R:r>j\}|\pmod2.
}
\tag{4}
\]
This consists of \(\binom{n-1}k\) faces of dimension \(k+1\). With \(H_{-1}=0\), it satisfies
\[
\boxed{
E_k(g)+E_k(gs_0)
=\partial H_k(g,s_0)+NH_{k-1}(g,s_0),
\qquad 0\le k\le n-1.
}
\tag{5}
\]
In particular \(H_0(g,s_0)\) is the initial edge of the complete geodesic.

*Proof.* Flipping the root only in dimension \(d_0\) leaves any \(E_k\)-face whose free set contains position \(0\) unchanged. Faces whose free set omits \(0\) come in pairs at opposite \(d_0\) positions. Each such pair appears as the two boundary facets obtained by fixing dimension \(d_0\) in a unique \((k+1)\)-face of (4). The remaining boundary facets come from fixing one position in \(R\); for every common \((k-1)\)-subset they telescope, in increasing order of the remaining positions, from \(H_{k-1}(g,s_0)\) to its antipodal mate. This gives (5). For \(k=0\), the identity says that the boundary of the initial edge is the two possible initial roots. \(\square\)

## Theorem 3 (a sharp top-rank distinction)

All correction chains in (2) and (4) with \(k\le n-2\) lie in the cubical boundary sphere \(B_n=\partial[0,1]^n\). But at rank \(k=n-1\),
\[
\boxed{H_{n-1}(g,s)=Q_n}
\tag{6}
\]
for **every** simple Coxeter generator \(s\). Accordingly the preceding identities in the highest rank are
\[
\boxed{
E_{n-1}(g)+E_{n-1}(gs)+NH_{n-2}(g,s)
=\partial Q_n=[B_n].
}
\tag{7}
\]
The right-hand side is the nonzero mod-two fundamental cycle in \(H_{n-1}(B_n;\mathbb F_2)\). Thus the displayed normalized homotopies are internal to the boundary through rank \(n-2\), while their final correction necessarily uses the full ambient \(n\)-cube. This statement is about the explicit homotopies (2) and (4), not an assertion that every other choice of higher correction is impossible.

*Proof.* For \(s_i\), \(i\ge1\), the only \((n-1)\)-rank term in (2) has \(R=[n]_0\setminus A_i\), so its free dimensions are all of \([n]_0\). For \(s_0\), the only term in (4) has \(R=\{1,\ldots,n-1\}\), likewise giving the full cube. A cubical face with at most \(n-1\) free dimensions belongs to \(B_n\). Formula (7) now follows from (3) and (5); its right-hand side is the full cellular boundary of the top cube, representing the mod-two sphere fundamental class. \(\square\)

**Computational audit.** Formulas (2)–(5) were independently expanded and checked as cubical chains for all generator positions, all ranks and dimensions \(2\le n\le7\), including arbitrary initial roots and scrambled dimension orders.

**Proof-search significance.** The all-rank resolution is now compatible by explicit chain homotopies with each of the generators of the complete type-\(B_n\) flag geometry. This is stronger than the rank-two square and three-cube identities: the formulas already account for arbitrary higher dimension sets. To make a chain-valued representation of the Coxeter relations, one must next compare these generator homotopies around the braid and commuting polygons, requiring homotopies of homotopies. Those can be sought inside the same cubical face system. The principal open issue remains a color-sensitive lift of these relations under unrestricted edge coloring; the uncolored homotopies themselves do not imply the desired monochromatic full geodesic.
