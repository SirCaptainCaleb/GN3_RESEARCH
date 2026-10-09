# Exact parity reachability counts: all roots below half-cube from dimension 20

# Exact reachable-target density for exterior-parity edge coloring: collisions below half the cube

Let n=2m be even and color each undirected edge in direction i by c_i(v)=sum_{j neq i}v_j modulo 2. The edge is well defined because c_i is independent of v_i, and c_i(bar v)=1-c_i(v) since n-1 is odd. For root x let U(x)=F_0(x) union F_1(x), where F_q(x) consists of supports S of q-monochromatic geodesics starting at x.

**Theorem 1 (exact support shape).** A support S belongs to U(x) if and only if the numbers of x-ones and x-zeros within S differ by at most one:
U(x) = {S subseteq [n] : | |S intersect Ones(x)| - |S intersect Zeros(x)| | <= 1}.

Proof. Along a permutation p of S, the color of the k-th edge is P(x) XOR (k-1 mod2) XOR x_(p_k), with P(x)=sum_i x_i mod2. Thus all edge colors are equal exactly when x_(p_1),x_(p_2),... alternate in parity. Such an order exists exactly when the two bit counts within S differ by <=1. The assertion includes the empty path.

**Theorem 2 (exact cardinality and global maximum).** If x has t ones, then
|U(x)| = C(n,n-t-1)+C(n,n-t)+C(n,n-t+1),
where binomial coefficients outside 0..n are zero. Indeed write a for the number of selected one-positions and b for selected zero-positions; by selecting unchosen zero-positions instead, the total number of pairs (a,b) with a-b=k is C(n,(n-t)+k). Sum over k=-1,0,1. The consecutive-binomial sum is symmetric and unimodal in n-t, hence its maximum over all roots occurs at t=m. In particular,
max_x |U(x)| = C(2m,m)+2 C(2m,m-1)
= ((3m+1)/(m+1)) C(2m,m).

**Corollary (the half-cube cardinality criterion fails even for positive instances).** At m=10,
max_x |U(x)|= C(20,10)+2 C(20,9) = 520676 < 524288=2^19.
The ratio
p_m = max_x |U(x)|/4^m
decreases strictly in m>=1, because
p_(m+1)/p_m = ((3m+4)(2m+1))/(2(m+2)(3m+1)) < 1.
Therefore for every EVEN n>=20 and EVERY root x,
|U(x)| < 2^(n-1),
although the coloring possesses monochromatic antipodal geodesics: take any root x with exactly m one-bits and an order alternating 0- and 1-root-bits. The color formula shows its full length-n geodesic is monochromatic.

Thus a pigeonhole argument proving a complementary pair from |U(x)|>2^(n-1) cannot establish the conjecture in full generality: positive instances can have every reachability star strictly smaller than half the Boolean lattice. Complementary reachable labels must be forced via structure/incidence/topology, not cardinality alone. In the balanced roots, the empty and full support are already a complementary reachable pair, despite low cardinality.

This lemma addresses the antipodally odd EDGE proving ground. The ordered-three-face NORI extraction additionally needs two seam-window compatibility conditions.
