# Cut obstruction for inseparable pairs needs no minimality

## Statement

Let H be a boundary tournament with a two-cover, and let s,t be distinct vertices that lie in the same component of every two-cover of H. Fix any two-cover A|B with A=(a_1,...,a_m), s=a_i, t=a_j, i<j. For every k with i<=k<j, put L=(a_1,...,a_k) and R=(a_{k+1},...,a_m). Then H[V(L) union V(B)] and H[V(R) union V(B)] are both non-Hamiltonian. In particular H itself is non-Hamiltonian.

## Body

No minimal-counterexample hypothesis is needed.

If H were Hamiltonian, choose a Hamilton path C containing s and t. Cutting C at any ordinary edge strictly between the positions of s and t produces two nonempty contiguous tight subpaths whose supports partition V(H), with s and t in different components. This is a two-cover separating s and t, contrary to hypothesis. Hence H is non-Hamiltonian.

Now fix A|B as in the statement and k with i<=k<j. The contiguous subpaths L and R are nonempty and tight, with s in L and t in R. If H[V(L) union V(B)] were Hamiltonian, a Hamilton path on V(L) union V(B), together with R, would form a two-cover of H separating s from t. This contradicts inseparability. The same argument with L and R interchanged shows H[V(R) union V(B)] is non-Hamiltonian.

Thus the simultaneous cut obstruction is a property of any inseparable pair inside any two-coverable boundary tournament; order-minimality plays no role.