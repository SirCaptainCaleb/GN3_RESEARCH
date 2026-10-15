# Coxeter-window switch moments and a boundary spectral polynomial

# Coxeter-window switch moments and a boundary spectral polynomial

We work with the Coxeter-coset representations of Article XIV. A general averaging identity permits direct comparison of the canonical type-A and type-B models without losing full-path admissibility.

**Lemma 1 (uniform Coxeter-window moment).** Let \(G\) be a finite group, \(t\in G\), \(q:G\to\{-1,1\}\), and \(m\ge2\). For each \(g\in G\), let \(\mathsf w_g=(q(g),q(gt),\ldots,q(gt^{m-1}))\), with a switch whenever consecutive signs differ. Then
\[
\boxed{\quad
\mathbb E_{g\in G}\operatorname{sw}(\mathsf w_g)
=\frac{m-1}{2}\left(
1-\mathbb E_{g\in G}q(g)q(gt)
\right).
\quad}
\tag{1}
\]

*Proof.* The switch indicator between consecutive signs \(u,v\in\{-1,1\}\) is \((1-uv)/2\). For each fixed window position \(j\), uniformity of \(g\) makes \(gt^j\) uniform in \(G\), giving the same correlation \(\mathbb E_g q(g)q(gt)\). Summing over \(m-1\) comparisons proves (1). \(\square\)

## A cubical sum-of-squares identity

For any binary undirected-edge coloring of \(Q_n\), define
\[
s_i(x)=(-1)^{c(\{x,x\oplus e_i\})},
\qquad
M(x)=\sum_{i=1}^n s_i(x).
\tag{2}
\]
In particular, \(s_i(x\oplus e_i)=s_i(x)\).

**Theorem 2 (cubical switch moment).** If \(x\) is a uniform cube root and \(\pi\) a uniform permutation of all dimensions, the full antipodal geodesic \(P(x,\pi)\) satisfies
\[
\boxed{\quad
\mathbb E_{x,\pi}\operatorname{sw}(P(x,\pi))
=\frac n2-\frac1{2n\,2^n}\sum_{x\in Q_n} M(x)^2
\le\frac n2.
\quad}
\tag{3}
\]
For odd \(n\), the right-hand side is at most \(n/2-1/(2n)\). Consequently every cube-edge coloring admits a full antipodal geodesic with at most \(\lfloor n/2\rfloor\) switches. For antipodally odd colorings, the parity reduction of Article IX permits the smallest switch count to be chosen even.

*Proof.* At each of the \(n-1\) comparisons of successive edges, their dimensions are a uniformly selected ordered pair \(i\ne j\), and the tail \(y\) of the first edge is uniform over \(Q_n\). The edge signs are \(s_i(y)\) and \(s_j(y\oplus e_i)\). By translation invariance of uniform \(y\) and \(s_i(y\oplus e_i)=s_i(y)\),
\[
\mathbb E_y[s_i(y)s_j(y\oplus e_i)]
=\mathbb E_y[s_i(y)s_j(y)].
\]
Averaging over \(i\ne j\) yields
\[
\mathbb E\operatorname{sw}
=\frac{n-1}{2}
-\frac1{2n}\mathbb E_y\sum_{i\ne j}s_i(y)s_j(y).
\]
Since \(\sum_{i\ne j}s_i s_j=M(y)^2-n\), (3) follows. For odd \(n\), the sum of \(n\) signs is odd, hence \(M(y)^2\ge1\). Integer rounding and the earlier antipodal rotation lemma give the consequences. \(\square\)

This nonnegative quadratic defect is available even without antipodal oddness; its positivity comes from undirected-edge incidence compatibility.

## The boundary-tournament transition operator

Let \(n\ge4\). On ordered distinct triples define a real field \(s(a,b,c)\) satisfying
\[
s(c,b,a)=-s(a,b,c).
\tag{4}
\]
The sign field of any ordinary reversal-odd boundary tournament belongs to this space and takes values in \(\{-1,1\}\). Let \(H_n\) be the real vector space of such fields, represented by the independent entries \(s(a,b,c)\) with \(a<c\) and their standard Euclidean inner product. Define
\[
\boxed{\quad
(A_n s)(a,b,c)
=\sum_{d\notin\{a,b,c\}}
\bigl[s(b,c,d)-s(b,a,d)\bigr].
\quad}
\tag{5}
\]
The right-hand side is odd under interchange of \(a,c\), so \(A_n\) maps \(H_n\) to itself.

**Lemma 3 (boundary correlation).** The operator \(A_n\) is self-adjoint, and for any binary boundary tournament with sign field \(s\),
\[
\boxed{\quad
\mathbb E_{\pi\in S_n}\operatorname{sw}
=\frac{n-3}{2}
\left(1-\frac{\langle s,A_n s\rangle}
{2(n-3)\langle s,s\rangle}\right).
\quad}
\tag{6}
\]

*Proof.* Put \(F(s,t)=\sum_{a,b,c,d\ {\rm distinct}}s(a,b,c)t(b,c,d)\). Under reversal of the ordered quadruple, both fields acquire a minus sign, so \(F(s,t)=F(t,s)\). The skew relation (4), followed by the exchange \(a\leftrightarrow c\), gives \(\langle s,A_n t\rangle=F(s,t)\) in the independent-entry inner product. This proves self-adjointness. For sign fields, \(\langle s,s\rangle=n(n-1)(n-2)/2\). Every consecutive pair of triple bits in a uniform Hamilton order is distributed as a uniform ordered quadruple of distinct vertices. Hence its sign correlation equals \(F(s,s)/[n(n-1)(n-2)(n-3)]\). Substitute in Lemma 1 with \(m=n-2\) to obtain (6). \(\square\)

**Theorem 4 (boundary spectral polynomial; finite-algebra certificate).** For every \(n\ge4\), the symmetric operator (5) satisfies
\[
\boxed{\quad
A_n(A_n+2I)(A_n-I)
\bigl(A_n^2-(n-2)^2 I\bigr)=0.
\quad}
\tag{7}
\]
Thus every eigenvalue belongs to \(\{-(n-2),-2,0,1,n-2\}\), and in particular
\[
\boxed{\quad
\mathbb E_{\pi\in S_n}\operatorname{sw}
\le \frac{3n-8}{4}.
\quad}
\tag{8}
\]
For \(n=5\), inequality (8) gives a Hamilton tight path with at most one switch.

*Computer-assisted proof of (7), with a finite interpolation justification.* The coefficients of \(A_n\), between two ordered-triple basis vectors, depend only on the equality pattern among their symbols. The entries of \(A_n^k\) count signed \(k\)-step transitions, where each step introduces at most one new symbol. After fixing the input and output triples (together involving at most six symbols), classify the intermediate symbols by equality pattern. A pattern involving \(r\) additional distinct symbols contributes a multiple of the falling factorial \((n-h)_r\), where \(h\le6\) is the number of fixed symbols, and \(r\le k\). Consequently each matrix entry of \(A_n^k\), for every fixed input-output equality pattern and \(n\ge6\), is a polynomial in \(n\) of degree at most \(k\). Expanding the left-hand side of (7), including its coefficients polynomial in \(n\), gives degree at most five. Every possible equality pattern among two triples occurs already for \(n=6\). It therefore suffices to verify the integer matrix identity for the six values \(n=6,\ldots,11\). The remaining \(n=4,5\) are checked directly.

Here is a standalone Python 3 / SciPy verification of these finitely many integer equalities. Each matrix entry is an integer, so no floating-point eigensolver or tolerance is involved.

\`\`\`python
from itertools import permutations
import numpy as np
from scipy.sparse import coo_matrix, identity

for n in range(4, 12):
    reps = [(a,b,c) for a,b,c in permutations(range(n),3) if a<c]
    loc = {t:(i,1) for i,t in enumerate(reps)}
    for i,(a,b,c) in enumerate(reps):
        loc[c,b,a] = (i,-1)

    rows, cols, vals = [], [], []
    for i,(a,b,c) in enumerate(reps):
        for d in range(n):
            if d in (a,b,c):
                continue
            j,sgn = loc[b,c,d]
            rows.append(i); cols.append(j); vals.append(sgn)
            j,sgn = loc[b,a,d]
            rows.append(i); cols.append(j); vals.append(-sgn)

    A = coo_matrix(
        (np.array(vals, dtype=np.int64), (rows,cols)),
        shape=(len(reps),len(reps))
    ).tocsr()
    A.sum_duplicates()
    I = identity(len(reps), dtype=np.int64, format="csr")
    P = A @ (A+2*I) @ (A-I) @ (A-(n-2)*I) @ (A+(n-2)*I)
    P.eliminate_zeros()
    assert (A-A.T).nnz == 0
    assert P.nnz == 0
\`\`\`

The polynomial interpolation argument promotes this finite verification to all \(n\ge4\). Since \(A_n\) is real symmetric, (7) bounds its smallest eigenvalue below by \(-(n-2)\). Inserting this in (6) yields
\[
\frac{n-3}{2}\left(1+\frac{n-2}{2(n-3)}\right)
=\frac{3n-8}{4},
\]
proving (8). The number of switches is integral, and \((3\cdot5-8)/4=7/4<2\), giving the stated five-vertex consequence. \(\square\)

## Implication for the unified conjecture

The cubical and boundary coset models now share Lemma 1, a spectral quadratic formulation of their complete-path switch counts. Local incidence descent gives the positive sum-of-squares formula (3) in type B. In type A, the corresponding compressed Coxeter transition has the five-root polynomial (7), proved by the finite-algebra certificate above. Both guarantee complete paths with bounded switches in every dimension, while neither alone forces the desired universal one-switch conclusion in large rank. A full proof needs either higher moments or structural concentration beyond the first Coxeter correlation.
