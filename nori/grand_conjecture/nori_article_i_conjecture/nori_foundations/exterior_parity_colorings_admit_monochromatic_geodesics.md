# Exterior parity colorings admit monochromatic geodesics

**Theorem (exterior-parity twist, arbitrary window length).** Fix integers 1≤k≤n, a coordinate order p=(p_1,…,p_n), and any binary function f of ordered k-tuples of distinct coordinates. For each ordered k-face (F,σ), let
c(F,σ)=f(σ) ⊕ (⊕_{u∉free(F)} b_u(F)),
where b_u(F) is the constant bit of coordinate u on F and ⊕ denotes addition in F_2. Then **exactly 2^k starting vertices** yield a monochromatic sequence of all n−k+1 ordered k-face windows along the antipodal geodesic with direction order p. In particular, for k=3 exactly eight starts work for **every fixed permutation**, for all n≥3, regardless of f.

**Proof.** Identify starting vertex bits in p-order by x_1,…,x_n and let X=⊕_{j=1}^n x_j. At window i, the first i−1 directions have been toggled. Its color is
w_i=f(p_i,…,p_{i+k−1}) ⊕ X ⊕ (⊕_{j=i}^{i+k−1}x_j) ⊕ ((i−1) mod 2).
We seek w_i=t for a single t∈F_2. Put q=X⊕t. Choose q and x_1,…,x_{k−1} freely, and successively define
x_{i+k−1}=f(p_i,…,p_{i+k−1}) ⊕ ((i−1) mod2) ⊕ q ⊕ (⊕_{j=i}^{i+k−2}x_j)
for i=1,…,n−k+1. Every x_k,…,x_n is determined, and setting t=X⊕q verifies w_i=t at every window. Conversely, any monochromatic starting vertex has its unique t and q=X⊕t and therefore appears exactly once in this construction. The choices are injective, since the first k−1 bits are freely specified and x_k determines q. Hence exactly 2^k starting vertices work. □

**Antipodal compatibility.** The coloring satisfies c(bar F,rev σ)=1⊕c(F,σ) exactly when f(rev σ)=f(σ)⊕(1+(n−k) mod2). Thus for k=3 this supplies a substantial NORI subclass, with reversal-even f in even n and reversal-odd f in odd n. The theorem also works without antipodal symmetry.

**Affine rank criterion (generalization).** Suppose more generally every ordered k-face color is affine over F_2 in the outside face bits. For a fixed coordinate order p the n−k+1 window colors form w(x)=A_p x⊕b_p. If the augmented matrix [A_p | 1] has full row rank n−k+1, a monochromatic window sequence exists: solve A_px⊕t1=b_p. The exterior-parity theorem above gives a constructive proof of this rank criterion for its special coefficient matrix, and proves the stronger exact count 2^k.

**Scope.** General Boolean dependence on outside face bits, and rank-deficient affine colorings, remain untreated. The grand NORI conjecture remains open.
