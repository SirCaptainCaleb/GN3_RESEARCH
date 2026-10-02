# Critical Boolean additive constructions reduce to projective families, with only lengths 3 and 7 surviving through 15

## Statement


Let A⊂F_2^d\{0} have |A|=2ell+1, and let H(A) be the induced Boolean Schur triple system. If H(A) is P_ell-free and has density greater than (ell-1)/3, then A is either a punctured subspace or a punctured subspace with two additional points deleted; equivalently ell=2^{r-1}-1 or ell=2^{r-1}-2. For 2<=ell<=15, the only strict-density-improving P_ell-free cases in these two families are the Fano example at ell=3 and PG(3,2) at ell=7.


## Body


Put n=|A|=2ell+1 and let M be the number of unordered pairs {x,y}⊂A with x+y∉A. Since every Schur triple accounts for exactly three good pairs,
  3|E(H(A))| = binom(n,2)-M.
The strict inequality |E(H(A))|/n>(ell-1)/3=(n-3)/6 is equivalent to M<n. The near-Steiner classification therefore forces either A=W\{0}, giving n=2^r-1 and ell=2^{r-1}-1, or A=W\{0,a,b}, giving n=2^r-3 and ell=2^{r-1}-2. Thus every critical-size Boolean candidate beating the generic coefficient belongs to one of these projective families.

For ell<=15 the remaining cases can be decided exactly. Full projective systems occur at ell=3,7,15. The Fano plane is P_3-free, PG(3,2) is P_7-free, while PG(4,2) contains a spanning P_15. Two-point deletions occur at ell=2,6,14. At ell=2 the five-point deletion contains P_2. At ell=6, a C_7 in PG(3,2) loses one edge to give a P_6 omitting exactly two points, and 2-transitivity carries those omitted points to any prescribed deleted pair. At ell=14, remove one endpoint edge from a spanning P_15 in PG(4,2); again 2-transitivity carries the two omitted private vertices to any deleted pair. Hence only ell=3 and ell=7 survive through 15.
