# Six-vertex boundary one-switch theorem from Coxeter spectra

# The six-vertex boundary one-switch theorem from Coxeter spectra

We prove the ordinary reversal-odd boundary 3-tournament conjecture on six vertices, using the self-adjoint transition operator from the preceding subsection. The proof retains all six original vertices in the Hamilton witness and imposes no global order or representability condition on the tournament.

**Theorem 1 (six-vertex boundary closure).** Let \(V\) have six vertices and let \(b(a,h,c)\in\mathbb F_2\) be defined for all ordered distinct triples, subject only to
\[
b(c,h,a)=1-b(a,h,c).
\]
There exists a permutation \((v_1,\ldots,v_6)\) of \(V\) such that
\[
\boxed{\quad
\operatorname{sw}\bigl(
b(v_1,v_2,v_3),b(v_2,v_3,v_4),
b(v_3,v_4,v_5),b(v_4,v_5,v_6)
\bigr)\le1.
\quad}
\tag{1}
\]

*Proof.* Let \(s(a,h,c)=(-1)^{b(a,h,c)}\), so \(s(c,h,a)=-s(a,h,c)\). Fix a uniformly random permutation \(\pi=(v_1,\ldots,v_6)\) and put \(q_i=s(v_i,v_{i+1},v_{i+2})\) for \(i=1,2,3,4\). A four-bit word has at most one switch precisely when a majority of its three adjacent comparisons have equal signs. The elementary identity for \(q_i\in\{-1,1\}\) is
\[
\boxed{\quad
\mathbf1_{\{\operatorname{sw}(q_1,q_2,q_3,q_4)\le1\}}
=\frac12+\frac14(q_1q_2+q_2q_3+q_3q_4-q_1q_4).
\quad}
\tag{2}
\]
Uniformity under cyclic relabeling makes the three adjacent correlations equal:
\[
C_1=\mathbb E_\pi q_1q_2
=\mathbb E_\pi q_2q_3
=\mathbb E_\pi q_3q_4.
\]
Moreover
\[
\mathbb E_\pi q_1q_4
=\mathbb E_\pi s(v_1,v_2,v_3)s(v_4,v_5,v_6)=0,
\tag{3}
\]
since exchanging \(v_1,v_3\) changes the sign of the first factor and leaves the second unchanged. Averaging (2) therefore yields
\[
\Pr_\pi(\operatorname{sw}\le1)=\frac12+\frac34 C_1.
\tag{4}
\]

Let \(H_6\) be the 60-dimensional space of real fields \(s(a,b,c)=-s(c,b,a)\), with the independent-entry inner product, and define
\[
(A_6s)(a,b,c)
=\sum_{d\notin\{a,b,c\}}
\bigl[s(b,c,d)-s(b,a,d)\bigr].
\tag{5}
\]
The preceding spectral subsection proves that \(A_6\) is symmetric and satisfies the polynomial
\[
A_6(A_6+2I)(A_6-I)(A_6^2-16I)=0.
\tag{6}
\]
Its smallest eigenvalue is therefore at least \(-4\). The correlation identity from that subsection reads
\[
C_1=\frac{\langle s,A_6s\rangle}{6\langle s,s\rangle}
\ge-\frac23.
\tag{7}
\]
Consequently (4) is nonnegative. To obtain a successful Hamilton path we prove that equality in (7) is impossible for a sign field.

**Lemma 2 (negative extremal eigenspace).** The \(-4\)-eigenspace of \(A_6\) consists precisely of fields of the form
\[
s(a,b,c)=M_{ab}-M_{bc},
\tag{8}
\]
where \(M\) is a real symmetric \(6\times6\) matrix with zero diagonal and zero row sums. Its dimension is nine.

*Proof.* Let \(M\) be as stated. The field (8) is odd under interchange of its outer arguments. Since
\[
s(b,c,d)-s(b,a,d)
=M_{bc}-M_{ab}+M_{ad}-M_{cd},
\]
the zero row sums give
\[
\sum_{d\notin\{a,b,c\}}(M_{ad}-M_{cd})
=-M_{ab}+M_{bc}.
\]
There are three permitted values of \(d\), so (5) yields
\[
(A_6s)(a,b,c)=-3s(a,b,c)-s(a,b,c)=-4s(a,b,c).
\tag{9}
\]
The space of symmetric zero-diagonal matrices has 15 entries. Its six row-sum constraints are independent over \(\mathbb R\): any linear dependence would give scalars \(\lambda_a\) with \(\lambda_a+\lambda_b=0\) for all \(a\ne b\), forcing every \(\lambda_a=0\). Hence this space has dimension \(15-6=9\). The map \(M\mapsto s\) is injective: if every difference \(M_{ab}-M_{bc}\) vanishes, each row has constant off-diagonal entries, symmetry makes all those constants equal, and zero row sums make them zero.

It remains to show that the \(-4\)-eigenspace has dimension nine. In the independent-triple basis the integer matrix (5) has size 60, and direct finite walk enumeration gives
\[
\operatorname{tr}(I,A_6,A_6^2,A_6^3,A_6^4)
=(60,0,360,0,5040).
\tag{10}
\]
These five integer identities can be checked using the matrix construction in the preceding subsection, or by the following standalone checker:

\`\`\`python
from itertools import permutations
import numpy as np
from scipy.sparse import coo_matrix

n = 6
R = [(a,b,c) for a,b,c in permutations(range(n),3) if a<c]
index = {t:(i,1) for i,t in enumerate(R)}
index.update({t[::-1]:(i,-1) for i,t in enumerate(R)})
rows, cols, vals = [], [], []
for i,(a,b,c) in enumerate(R):
    for d in range(n):
        if d in (a,b,c):
            continue
        for t,sgn in (((b,c,d),1),((b,a,d),-1)):
            j,orient = index[t]
            rows.append(i); cols.append(j); vals.append(sgn*orient)
A = coo_matrix(
    (np.array(vals,dtype=np.int64),(rows,cols)),
    shape=(len(R),len(R))
).tocsr()
B = A.copy()
traces = [len(R)]
for k in range(1,5):
    traces.append(int(B.diagonal().sum()))
    B = B @ A
assert traces == [60,0,360,0,5040]
\`\`\`

By (6) and symmetry, the eigenvalues belong to \(\{-4,-2,0,1,4\}\). Let their multiplicities be \(m_\lambda\). Equation (10) gives the five linear equations
\[
\sum_\lambda m_\lambda\lambda^k
=(60,0,360,0,5040)_k,\qquad 0\le k\le4.
\]
The coefficient matrix is Vandermonde with distinct values \(-4,-2,0,1,4\), so the solution is unique:
\[
(m_{-4},m_{-2},m_0,m_1,m_4)=(9,10,15,16,10).
\]
Thus the nine-dimensional family (8) fills the entire \(-4\)-eigenspace. \(\square\)

Returning to Theorem 1, equality in (7) would force the sign vector \(s\) into the \(-4\)-eigenspace. By Lemma 2, there would be a symmetric matrix \(M\) with
\[
|M_{ab}-M_{bc}|=1
\qquad\text{for every three distinct }a,b,c.
\tag{11}
\]
Fix any middle vertex \(b\), and choose three distinct neighbors \(a,c,d\). Equation (11) would make the three real numbers \(M_{ab},M_{cb},M_{db}\) pairwise separated by absolute difference one. Three points on the real line cannot have all three pairwise distances equal to one. This contradiction proves
\[
C_1>-\frac23.
\]
Equation (4) then gives \(\Pr_\pi(\operatorname{sw}\le1)>0\). Therefore at least one permutation of all six vertices satisfies (1). \(\square\)

**Scope and significance.** The theorem proves the original six-vertex boundary conclusion for every reversal-odd coloring of ordered distinct triples. It does not require a prescribed initial vertex: a separate seven-vertex research note demonstrates that a fixed-root strengthening can fail. The proof is common to the Coxeter framework at the level of its local-incidence transition operator and positive-probability extraction, although the vanishing three-step correlation and extremal eigenspace analysis are specific to the type-A six-vertex instance. Larger dimensions remain open.
