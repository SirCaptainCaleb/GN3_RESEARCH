# Cyclic color variation and unavoidable root selection

# Cyclic variation and root selection

## Boundary one-switch Hamilton paths

Let \(b(a,b,c)\in\{0,1\}\) be a reversal-odd coloring of distinct ordered triples on \([n]\), \(n\ge4\). For a cyclic order \(\pi=(v_1,\ldots,v_n)\), index cyclically and define
\[
t_i=b(v_i,v_{i+1},v_{i+2}),\qquad
d_i=t_i\oplus t_{i+1},\qquad D(\pi)=\sum_{i=1}^n d_i.
\]
The cyclic switch count \(D\) is even.

**Theorem 1 (circular-switch criterion).** Of the \(n\) Hamilton paths obtained by cutting the cyclic order, the minimum binary switch count is
\[
\boxed{D(\pi)-\max_i(d_i+d_{i+1}+d_{i+2}).}
\]
Consequently a reversal-odd boundary tournament has a one-switch Hamilton path if and only if some cyclic order satisfies either \(D\le2\), or \(D=4\) with three consecutive \(d_i\)'s equal to one.

**Proof.** Cutting the cycle retains \(n-2\) consecutive triple bits, hence \(n-3\) consecutive comparisons \(d_i\). The omitted comparisons occupy three consecutive positions, so minimizing the retained sum gives the formula. As \(D\) is even, the minimum is at most one precisely in the two stated cases. \(\square\)

The \(D=4\) case cannot be discarded. When \(n=4\), let \(b(a,b,c)\) be the inversion parity of the four-letter ordering \((a,b,c,d)\), with \(d\) the omitted letter. Reversing \((a,b,c)\) changes parity; rotating a four-letter cyclic ordering changes parity too. Thus every circular triple word alternates, with \(D=4\), but a Hamilton path has only two triple labels and automatically at most one switch.

## Rooted spectrum in NORI1

For even \(n=2m\ge4\), define an undirected cube-edge coloring by
\[
c_i(x)=\sum_{j\ne i}x_j\pmod2,\qquad \{x,x\oplus e_i\}\in E(Q_n).
\]
This is well defined because it ignores bit \(x_i\), and \(c_i(\bar x)=1-c_i(x)\) because \(n-1\) is odd.

**Theorem 2 (root-fiber minimum).** If the starting cube vertex \(x\) has Hamming weight \(w\), then
\[
\boxed{\min_{\pi\in S_n}\operatorname{sw}(P(x,\pi))
=\max\{0,|n-2w|-1\}.}
\]

**Proof.** Put \(r=\sum_jx_j\pmod2\). The \(k\)-th edge in direction order \(\pi\) has bit
\[
b_k=r+x_{\pi_k}+k-1\pmod2.
\]
Therefore \(b_k\ne b_{k+1}\) precisely when the two corresponding bits of \(x\) are equal. A permutation minimizing switches alternates the zero and one entries of \(x\) as long as possible; the surplus of the majority bit forces exactly \(\max\{0,|n-2w|-1\}\) neighboring equal pairs. \(\square\)

In this coloring, roots admitting a one-switch full geodesic have weights \(m-1,m,m+1\), while roots admitting a monochromatic full geodesic have weight \(m\). In particular every full geodesic from \(0^n\), regardless of direction order, has \(n-1\) switches. Root selection from \(0^n\) requires changing at least \(m-1\) root bits to find a one-switch path; bounded-radius root repair is insufficient.

## Shared interpretation and limits

Article IX already establishes the antipodal cyclic-rotation identity for NORI1. Extend its \(n\)-bit geodesic word antiperiodically by \(w_{i+n}=1-w_i\). The \(n\) cyclic comparison bits have odd total \(D\), invariant under a root slide; the minimum ordinary switch count within that rotation orbit is \(D-1\). For the boundary problem the triple-bit word is periodic, its \(D\) is even, and cutting discards three comparisons rather than one.

Thus both full-strength targets can be formulated as **small cyclic variation of overlapping complete paths**. Adjacent exchanges alter only bounded intervals of the cyclic label word. Nevertheless strict local descent fails: at cube root \(0^n\), adjacent direction swaps and single root slides preserve the high variation \(n-1\), although elsewhere \(D=1\). A successful common selection theorem needs global root and ordering compatibility.

The NORI1 cyclic identity is already proved in Article IX; Theorems 1 and 2 and the plateau obstruction are detailed in research notes note_a31f3ced5651f1da607b547c, note_52fd24abbc3549954285b0a5, and note_4faa19538adf3c3d215f274d, all attached to Article IX. No unified long-path theorem is asserted.
