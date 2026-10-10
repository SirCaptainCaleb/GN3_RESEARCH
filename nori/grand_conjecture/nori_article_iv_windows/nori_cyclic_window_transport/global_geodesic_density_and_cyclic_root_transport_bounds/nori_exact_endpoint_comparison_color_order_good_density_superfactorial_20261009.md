# Exact all-dimensional one-switch count for reversal-odd endpoint-comparison colors

# Exact one-switch counts for the endpoint-comparison coloring

**Theorem (valid reversal-odd coloring with superfactorially sparse good full paths).** For every n>=3, linearly order the coordinate alphabet [n] and color every physical ordered three-face with free directions (a,b,c) by h(a,b,c)=1[a<c], independent of its fixed exterior bits. This is a legal antipodal-reversal-odd NORI coloring because h(c,b,a)=1-h(a,b,c). For every starting cube vertex, the number of full n-direction permutations yielding at most one change in their n-2 consecutive three-face colors is exactly

  G_n = 2 binom(n,r) (binom(n-1,r-1)-1),   r=ceil(n/2).

Precisely 2 binom(n,r) of these permutations have zero changes. In particular, among all 2^n n! rooted directed antipodal geodesics, the good fraction is

  G_n/n! ~ 2*4^n / (pi*n*n!) -> 0,

faster than any fixed-base exponential.

**Proof.** On a full path with coordinate order p=(p_1,...,p_n), its color word is w_i=1[p_i<p_(i+2)], 1<=i<=n-2. Split the positions of p into the odd subsequence of length r and the even subsequence of length s=floor(n/2). The odd-indexed colors compare adjacent elements of the odd subsequence, and the even-indexed colors do likewise for the even subsequence.

For a prescribed good word 1^t 0^(n-2-t), 0<=t<=n-2, the odd subsequence has exactly ceil(t/2) initial ascents followed by descents, and the even subsequence has floor(t/2) initial ascents followed by descents. For k distinct prescribed labels, exactly binom(k-1,j) permutations have j initial ascents followed by k-1-j descents: the maximum label lies at the turn; choose the j labels to its left, arranging each side monotonically. Therefore the number of full coordinate orders realizing this word equals

  binom(n,r) binom(r-1,ceil(t/2)) binom(s-1,floor(t/2)).

The reversed-bit word 0^t 1^(n-2-t) has the same count, via reflection of the total order on [n]. Both constant-color words appear twice in these two families, each having exactly binom(n,r) realizations. By splitting t into even and odd values and applying Vandermonde's identity,

  sum_(t=0)^(n-2) binom(r-1,ceil(t/2)) binom(s-1,floor(t/2))
  = sum_j binom(r-1,j)binom(s-1,j) + sum_j binom(r-1,j+1)binom(s-1,j)
  = binom(n-1,r-1).

Double the sum, subtract the two duplicated constant words, and multiply by binom(n,r), proving G_n. Each constant word contributes binom(n,r), proving the monochromatic count. Stirling's approximation yields the asymptotic.

**Independent exact check.** Enumeration of all n! permutations for n=3,...,9 gives G_n=6,24,100,360,1330,4760,17388, matching the formula; zero-switch counts are 6,12,20,40,70,140,252.

**Use and precise limitation.** No universal lower bound by a constant fraction, or by exp(-C*n) for fixed C, can hold for the density of GOOD FULL antipodal paths, even in the coordinate-only subclass and at any fixed root. Density averaging alone must therefore accommodate superfactorially rare witnesses. The example has good full paths in every dimension and does not refute the grand conjecture. It is compatible with global topology or exact same-root complementary-tail extraction, which require a single witness rather than density.
