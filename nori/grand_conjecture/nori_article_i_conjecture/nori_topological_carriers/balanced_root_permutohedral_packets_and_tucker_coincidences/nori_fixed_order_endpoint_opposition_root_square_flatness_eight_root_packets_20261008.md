# Actual NORI endpoint-opposed paths obey a cubical root-square parity law and occur in packets of at least eight per fixed order

# Physical root-square parity and an eight-root packet for each fixed full direction order

Fix any \(n\ge6\), any binary coloring of ACTUAL ordered three-faces of \(Q_n\) (the theorem does NOT require antipodal oddness), and any full direction permutation \(\pi=(p_1,\ldots,p_n)\). Put
\[
A=\{p_1,p_2,p_3\},\quad B=\{p_{n-2},p_{n-1},p_n\},\quad M=[n]\setminus(A\cup B).
\]
The sets \(A,B\) are disjoint. For any root \(x\), write \(\alpha(x)=w_1(x,\pi)\), \(\beta(x)=w_{n-2}(x,\pi)\), and let \(e(x)=\alpha(x)\oplus\beta(x)\in\{0,1\}\). Then \(e(x)=1\) precisely when the ACTUAL full geodesic \((x,\pi)\) has **opposite first and last ordered-face colors**.

**Theorem 1 (root-square exact parity).** Fix any \(i\in A\), \(j\in B\), and fix all cube root bits outside \(\{i,j\}\). On the resulting genuine physical root square \(\{x,x\oplus e_i,x\oplus e_j,x\oplus e_i\oplus e_j\}\), the endpoint-opposition indicator has **zero mixed cubical derivative**:
\[
\boxed{e(x)\oplus e(x\oplus e_i)\oplus e(x\oplus e_j)
\oplus e(x\oplus e_i\oplus e_j)=0.}
\tag{1}
\]
More strongly, its four values comprise **0, 2, or 4** ones, never 1 or 3. The sum of the two integer endpoint-imbalance functions also has zero mixed derivative:
\[
q(x)+q(x\oplus e_i\oplus e_j)
=q(x\oplus e_i)+q(x\oplus e_j),
\quad q=\alpha+\beta-1.
\tag{2}
\]

**Proof.** The actual first ordered-three-face has all of \(A\) FREE, so \(\alpha\) is independent of every root bit in \(A\), including \(i\). The actual last ordered-three-face has all of \(B\) FREE, so \(\beta\) is independent of every root bit in \(B\), including \(j\). Their exterior physical positions depend on the other root bits and the fixed prefix-flip set, but that does not alter these two coordinate independences. On the 2-square therefore
\[
\alpha(x\oplus r e_i\oplus s e_j)=f(s),\qquad
\beta(x\oplus r e_i\oplus s e_j)=g(r)
\]
for binary functions \(f,g\) of one bit. Thus \(e=f(s)\oplus g(r)\), whose XOR around the square vanishes, and \(q=f(s)+g(r)-1\), whose alternating integer sum vanishes. \(\square\)

**Theorem 2 (eight genuine endpoint-opposed ROOTS for each occupied direction order).** Fix the root bits on \(M\). Vary the three independent starting bits on \(A\) and the three independent starting bits on \(B\), obtaining a 6-dimensional physical root cube of 64 roots. Let \(a\in\{0,\ldots,8\}\) be the number of assignments to the \(B\) root bits for which \(\alpha=1\), and let \(b\in\{0,\ldots,8\}\) be the number of assignments to the \(A\) root bits for which \(\beta=1\). Then the number of roots in this 64-vertex cube supporting an endpoint-opposed full geodesic of order \(\pi\) is EXACTLY
\[
\boxed{N_{\pi,M}=a(8-b)+(8-a)b=8(a+b)-2ab.}
\tag{3}
\]
In particular:
- The count is always EVEN.
- If it is nonzero, it is **at least eight**.
- It is zero if and only if \(\alpha\) and \(\beta\) are both constant and equal on this root 6-cube; it equals 64 if and only if both are constant and opposite.
- If **both** endpoint bits \(\alpha,\beta\) vary with their respective opposite root triples, then \(N_{\pi,M}\ge14\).

**Proof.** After fixing \(M\), \(\alpha\) depends solely on the 8 possible \(B\)-bit assignments, and \(\beta\) solely on the independent 8 possible \(A\)-bit assignments. Opposite endpoint colors mean either \((\alpha,\beta)=(1,0)\) or \((0,1)\); elementary product counting gives (3). The parity is immediate from its form. For fixed \(a\) the expression is affine in \(b\); minimizing over the rectangle \([0,8]^2\) subject to positivity shows the least possible positive value is 8, obtained when one endpoint function is constant and the other differs from it on exactly one of its eight assignments. If both functions are nonconstant, \(1\le a,b\le7\), and the minimum on that rectangle is 14 at \((a,b)=(1,1)\) or \((7,7)\). The zero and full cases require the functions to be equal or opposite constants, respectively. \(\square\)

**Corollary 3 (a genuine same-order moving-root packet).** If the actual fixed-order full geodesic \((x,\pi)\) has opposite endpoint colors at ANY root \(x\), then at least EIGHT distinct physical roots, including \(x\) possibly, support an endpoint-opposed FULL geodesic with the **same direction permutation** \(\pi\). The accompanying root-square parity identity is valid on every first-triple/last-triple mixed coordinate square. These are *physical face-certified paths*, not interpolation artifacts.

**Topological significance.** The first and last ordered-three-face bits form a separable two-block Boolean map on every 6-coordinate root packet. The endpoint-opposition indicator is the XOR of these two blocks, so it defines a flat cubical 0/1 field across every root square whose two axes come one from the first and one from the last free triples. This exact source of **root mobility with fixed direction order** can be combined with the multi-root permutohedral Borsuk–Ulam face carrier: one yields high-index common *order faces* across prescribed roots, the other gives nontrivial same-order *root packets* whenever an endpoint balance occurs. The unresolved compatibility problem is to make the two kinds of packet intersect with ordered three-face **internal switch** and exact reversed-tail witness constraints.

**No claim of grand closure.** Opposite first/last colors guarantee an odd number of changes, which may be three or more; eight such rooted paths need not contain a one-change path. The root-square identity only couples endpoint colors, not the entire interior face-window sequence.
