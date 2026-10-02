# A dense reversal family contains a common-four-set star of at least three Hamiltonian five-supports

## Statement

Let H be a minimum counterexample of order n, and let T and J_T be as in reversal_dense_fivefamily01. Then some exterior vertex y belongs to at least floor((n-4)/2) edges of J_T. Equivalently, there are at least floor((n-4)/2) distinct vertices z such that V(T) union {y,z} is a Hamiltonian five-vertex support containing the same genuine reversal and having non-Hamiltonian path-cover-two complement. Since n>10, at least three such five-supports share the same four-vertex set V(T) union {y}.

## Body

Write m=n-3. By reversal_dense_fivefamily01,
|E(J_T)| >= binom(m,2)-floor(m^2/4).

If m=2k, the right side is k(k-1), so the average degree of J_T is at least k-1=floor((m-1)/2).
If m=2k+1, the right side is k^2, so the average degree is at least
2k^2/(2k+1)>k-1.
Because degrees are integers, some vertex has degree at least k=floor((m-1)/2).

Thus in all cases there is y in V(J_T) with
deg_{J_T}(y) >= floor((m-1)/2)=floor((n-4)/2).
For every neighbor z of y, reversal_dense_fivefamily01 says that V(T) union {y,z} is Hamiltonian, contains the same reversing tight triple T, and has non-Hamiltonian path-cover-two complement.

Minimum-counterexample calculus gives n>10, so floor((n-4)/2)>=3. Choosing three distinct neighbors yields the asserted common-four-set star. ∎