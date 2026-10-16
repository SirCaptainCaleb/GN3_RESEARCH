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
Therefore \(b_k\ne b_{k+1}\) precisely when the two corresponding bits of \(x\) are equal. A permutation minimizing switches alternates the zero and one entries of \(x\) as long as possible; the surplus of the majority bit forces precisely \(\max\{0,|n-2w|-1\}\) neighboring equal pairs. \(\square\)

In this coloring, roots admitting a one-switch full geodesic have weights \(m-1,m,m+1\), while roots admitting a monochromatic full geodesic have weight \(m\). In particular every full geodesic from \(0^n\), regardless of direction order, has \(n-1\) switches. Root selection from \(0^n\) requires changing at least \(m-1\) root bits to find a one-switch path; bounded-radius root repair is insufficient.

## Shared interpretation and limits

Article IX already establishes the antipodal cyclic-rotation identity for NORI1. Extend its \(n\)-bit geodesic word antiperiodically by \(w_{i+n}=1-w_i\). The \(n\) cyclic comparison bits have odd total \(D\), invariant under a root slide; the minimum ordinary switch count within that rotation orbit is \(D-1\). For the boundary problem the triple-bit word is periodic, its \(D\) is even, and cutting discards three comparisons rather than one.

Thus both full-strength targets can be formulated as **small cyclic variation of overlapping complete paths**. Adjacent exchanges alter only bounded intervals of the cyclic label word. Nevertheless strict local descent fails: at cube root \(0^n\), adjacent direction swaps and single root slides preserve the high variation \(n-1\), although elsewhere \(D=1\). A successful common selection theorem needs global root and ordering compatibility.

The NORI1 cyclic identity is already proved in Article IX; Theorems 1 and 2 and the plateau obstruction are detailed in research notes note_a31f3ced5651f1da607b547c, note_52fd24abbc3549954285b0a5, and note_4faa19538adf3c3d215f274d, all attached to Article IX. No unified long-path theorem is asserted.

## Balanced lifts preserve a linear rootwise switch obstruction

Fix even \(d\ge2\), and take the parity coloring from Theorem 2,
\(f_i(x)=\sum_{j\ne i}x_j\pmod2\).
Its complementary paired lift \(C\) on \(Q_{2d}\) is
\[
C_i(x,y)=f_i(x),\qquad
C_{d+i}(x,y)=1+f_i(x),\qquad 1\le i\le d.
\tag{CV1}
\]
This is a legal antipodally odd vertex-balanced coloring: paired incident edge colors are complementary at every vertex. Every face retaining a union of complete free-direction pairs is balanced.

**Theorem (linear rootwise switch obstruction).** For every vertex \(z=(0^d,y)\) and every direction-simple path \(P\) rooted at \(z\), if \(P\) has length \(\ell\) and \(s\) changes in its temporal color word, then
\[
\boxed{\ell\le d+s+1.}\tag{CV2}
\]
In particular, every full antipodal geodesic rooted at \(z\) has at least \(d-1\) switches; a rooted direction-simple path with at most one switch has length at most \(d+2\). Therefore paths with \(o(d)\) switches from these roots have length at most \(d+o(d)\), while the cube dimension is \(2d\).

*Proof.* Delete from \(P\) every step in a new direction \(d+i\), leaving \(r\) steps in old directions. Since each old direction is used at most once and the old vertex begins at \(0^d\), immediately before the \(k\)-th remaining step precisely \(k-1\) old bits have been flipped and the bit of the current direction is still zero. Its color is therefore
\[
f_{i_k}(x)=k-1\pmod2.
\]
Thus the subsequence of old-step colors alternates \(0101\cdots\), and has \(r-1\) switches for \(r\ge1\). Deleting entries from a binary word cannot increase the number of switches, so \(r\le s+1\); this is also true for \(r=0\). The path uses at most \(d\) new directions, yielding \(\ell\le d+r\le d+s+1\). Setting \(\ell=2d\) proves the full-geodesic claim. \(\square\)

This gives arbitrarily large balanced, paired-face-balanced legal colorings in which no path beginning at a specified root can simultaneously be near spanning and have sublinear switch count. The underlying parity coloring still has monochromatic full geodesics at other roots. Hence existential root selection is indispensable in any asymptotic low-switch route to unrestricted NORI1.


**Sharpness of the full-geodesic rooted switch bound.** In the coloring (CV1), the minimum switch count among all full antipodal geodesics starting at \((0^d,y)\) is \(d-1\) for every even \(d\ge2\) and every \(y\). Thus
\[
\boxed{\min_{\pi\in S_{2d}}\operatorname{sw}_C(P((0^d,y),\pi))=d-1.}\tag{CV3}
\]

*Proof.* The lower bound is (CV2). For the upper bound traverse dimensions in the order
\[
1,d+1,\ 2,d+2,\ \ldots,\ d-2,2d-2,\quad
d-1,\ 2d,\ 2d-1,\ d.
\tag{CV4}
\]
When \(d=2\), the initial repeated pairs are absent and (CV4) is \((1,4,3,2)\). All \(2d\) directions occur once.

The old directions occur in increasing order and their temporal colors alternate, with old step \(i\) colored \(i-1\bmod2\). For \(1\le i\le d-2\), the new direction \(d+i\) immediately follows old step \(i\), at which point \(i\) old bits have been flipped, including bit \(i\). Its color is
\(1+f_i(x)=1+(i-1)=i\bmod2\),
which equals the color of old step \(i+1\).

After old step \(d-1\), the new direction \(2d\) has color
\(1+f_d(x)=1+(d-1)=0\bmod2\),
matching old step \(d-1\). The next step \(2d-1\) has color
\(1+f_{d-1}(x)=1+(d-2)=1\bmod2\),
matching the final old step \(d\). Every inserted new-direction edge therefore belongs to one of the two neighboring constant-color runs. No additional switches are created, and the full path has the \(d-1\) switches already present in its alternating old-direction subsequence. \(\square\)
