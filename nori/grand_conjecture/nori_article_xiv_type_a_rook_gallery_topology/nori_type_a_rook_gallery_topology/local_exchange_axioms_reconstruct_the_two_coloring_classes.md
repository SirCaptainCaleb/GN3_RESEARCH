# Local exchange axioms reconstruct the two coloring classes

# Coxeter chambers and reconstruction from local color-word identities

Let \(V=[n]\), \(n\ge3\). The open chambers of the type-\(A_{n-1}\) arrangement in \(W=\{z\in\mathbb R^n:\sum_i z_i=0\}\) are
\[
A(\pi)=\{z:z_{\pi_1}<\cdots<z_{\pi_n}\}\quad(\pi\in S_n).
\]
These chambers parameterize Hamilton vertex orderings, triangulate \(S^{n-2}\), and obey \(-A(\pi)=A(\pi^{\mathrm{rev}})\).

The open chambers of the type-\(B_n\) arrangement \(z_i=0,\ z_i=\pm z_j\) are
\[
B(x,\pi)=\{z:0<|z_{\pi_1}|<\cdots<|z_{\pi_n}|,
\ \operatorname{sgn}(z_i)=(-1)^{x_i}\},
\quad x\in\mathbb F_2^n,\ \pi\in S_n.
\]
They parameterize all rooted antipodal cube geodesics \(P(x,\pi)\), triangulate \(S^{n-1}\), and obey \(-B(x,\pi)=B(\bar x,\pi)\). Thus the cube's freely chosen root is the sign part of a signed permutation. Each chamber in either model certifies a full path: distinct cube dimensions in type \(B\), and distinct original vertices in type \(A\).

Write \(s_i\pi\) for exchanging entries at positions \(i,i+1\), and \(R\pi=(\pi_2,\ldots,\pi_n,\pi_1)\).

**Theorem 1 (NORI1 word reconstruction).** A family of binary words \(w(x,\pi)=(w_1,\ldots,w_n)\), indexed by \(x\in\mathbb F_2^n,\pi\in S_n\), is induced by a unique antipodally odd coloring of the undirected cube edges if and only if it satisfies
\[
w_j(x,s_i\pi)=w_j(x,\pi)\quad(j\notin\{i,i+1\}),\tag{C1}
\]
\[
w(x\oplus e_{\pi_1},R\pi)
=(w_2(x,\pi),\ldots,w_n(x,\pi),1-w_1(x,\pi)),\tag{C2}
\]
and
\[
w(x,\pi^{\mathrm{rev}})
=\mathbf1-\operatorname{rev}(w(x,\pi)).\tag{C3}
\]

*Proof.* Given an undirected antipodally odd edge coloring, swapping neighboring dimensions changes only the two edges traversed within their square. Rotating the first dimension to the end after traversing it preserves the remaining \(n-1\) edges and appends the antipodal image of the first edge. Reversing the dimension order while retaining the root gives the antipodal image of the reversed path. These observations yield (C1)–(C3).

Conversely, for \(i\in[n]\) and \(y\in\mathbb F_2^n\), set
\[
a_i(y)=w_1(y,\pi)\quad\text{where }\pi_1=i.\tag{1}
\]
Adjacent swaps among positions \(2,\ldots,n\) connect all such orders and preserve their first word entry by (C1); hence \(a_i\) is well defined. Applying (C2) successively \(j-1\) times moves the \(j\)-th letter to the first position without crossing the final complemented seam. Thus
\[
w_j(x,\pi)=a_{\pi_j}\!\left(x\oplus\sum_{k<j}e_{\pi_k}\right).\tag{2}
\]
Applying (C2) \(n\) times returns to the original permutation at the complementary root and complements all word entries, proving
\[
a_i(\bar y)=1-a_i(y).\tag{3}
\]
Take an order \(\pi\) with \(\pi_n=i\). Its reversal begins with \(i\). Equations (C3) and (2) give
\[
a_i(y)=1-a_i(\bar y\oplus e_i)=a_i(y\oplus e_i),\tag{4}
\]
where (3) gives the final equality. Therefore \(a_i(y)\) is independent of which endpoint of \(\{y,y\oplus e_i\}\) is selected. Define the color of that edge to be \(a_i(y)\). Equation (3) gives antipodal oddness, (2) reconstructs every word, and (1) proves uniqueness. \(\square\)

**Theorem 2 (boundary-tournament word reconstruction).** A family \(u:S_n\to\mathbb F_2^{n-2}\) is induced by a unique ordinary reversal-odd boundary 3-tournament through
\[
u_j(\pi)=b(\pi_j,\pi_{j+1},\pi_{j+2})\tag{5}
\]
if and only if
\[
u_j(s_i\pi)=u_j(\pi)
\quad\text{whenever }\{j,j+1,j+2\}\cap\{i,i+1\}=\varnothing,\tag{T1}
\]
\[
u_j(R\pi)=u_{j+1}(\pi)\quad(1\le j\le n-3),\tag{T2}
\]
and
\[
u(\pi^{\mathrm{rev}})=\mathbf1-\operatorname{rev}(u(\pi)).\tag{T3}
\]

*Proof.* A tournament \(b\) makes (T1) immediate, since the selected ordered triple remains unchanged. Cyclic transport preserves overlapping triples and proves (T2), while reversal oddness proves (T3).

Conversely, for pairwise distinct \(a,h,c\), set \(b(a,h,c)=u_1(\pi)\) for any permutation beginning with \((a,h,c)\). All such permutations are connected by adjacent swaps in positions \(4,\ldots,n\); these preserve \(u_1\) by (T1). This defines \(b\) independently of the unspecified suffix. Iterating (T2) brings the triple at positions \(j,j+1,j+2\) to the beginning while retaining its bit; hence (5) holds. If \(\pi\) begins with \((a,h,c)\), then \(\pi^{\mathrm{rev}}\) ends in \((c,h,a)\). Using (T3) and (5),
\[
b(c,h,a)=u_{n-2}(\pi^{\mathrm{rev}})
=1-u_1(\pi)=1-b(a,h,c).
\]
Thus \(b\) is reversal odd, and its uniqueness follows from its defining first-window values. \(\square\)

**Scope of the reconstruction.** The three axioms in each theorem impose the shared-incidence compatibility of the underlying coloring, in addition to antipodal word symmetry. The hypotheses of Theorem 1 preserve every possible NORI1 root and place no restrictions on the independent antipodal edge orbits. The hypotheses of Theorem 2 preserve all ordinary boundary-tournament reversal orbits and every Hamilton ordering. All maximal certificates are full rank: the cube's move vectors are distinct standard basis vectors, while the consecutive type-\(A\) incidence roots of a Hamilton ordering form a basis of \(W\).

These two sets of intrinsic axioms provide a verifiable starting point for a common color-sensitive selection theorem. The missing assertion is an equivariant or homological principle that, using such incidence-compatible exchange data, selects a maximal certificate whose word has at most one switch.
