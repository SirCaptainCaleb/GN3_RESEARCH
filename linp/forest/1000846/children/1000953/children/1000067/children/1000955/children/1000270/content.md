# Why the P7 two-subspace grid obstruction is dimension-four exceptional

## Statement

Let P be a hypothetical spanning linear path in the Boolean projective Steiner triple system PG(r-1,2) on F_2^r\{0}, and let J be its joint set. Then |J|=2^{r-1}-2 and XOR(J)=0. More generally, if |J|>=r+2, J contains a nonempty proper zero-sum subset S with 3<=|S|<=floor(|J|/2). For r=4, |J|=6, so necessarily |S|=3 and J\S is also a zero-sum triple; these are the two complementary 2-spaces used in the P7 grid proof. Moreover this exact architecture cannot recur for r!=4: if J=(U\{0}) union (W\{0}) for complementary nonzero subspaces U,W, then the spanning-path joint count forces r=4 and dim U=dim W=2.

## Body

For a spanning path in PG(r-1,2), summing its edge vectors shows XOR(J)=0, as in d593f8024a92. Regard the elements of J as columns of an r by |J| binary matrix. The all-ones coefficient vector is a dependence because XOR(J)=0. If |J|>=r+2, the relation space has dimension at least |J|-r>=2, so there is another nonzero relation distinct from the all-ones relation. Its support S is a nonempty proper zero-sum subset of J. Since J also sums to zero, the complement J\S is zero-sum. Replacing S by its complement if necessary gives |S|<=floor(|J|/2). Distinct nonzero vectors admit no zero-sum subset of size 1 or 2, so |S|>=3.

For r=4 a spanning path has |J|=2^{3}-2=6, hence 3<=|S|<=3. Thus S and J\S are both zero-sum triples, i.e. punctured 2-dimensional subspaces. Their nonzero parts are disjoint, so the two subspaces intersect only in 0 and, because their dimensions sum to 4, are complementary. This is exactly the 3-by-3 grid decomposition in d593f8024a92.

To test whether the same two-subspace architecture can occur in general, suppose J=(U\{0}) union (W\{0}) with F_2^r=U direct_sum W. Put a=dim U and b=dim W, so a+b=r. The spanning joint count gives
(2^a-1)+(2^b-1)=2^{r-1}-2,
hence 2^a+2^b=2^{r-1}. A sum of two powers of two is itself a power of two only when a=b; then a+1=r-1, so a=b=r-2. Together with a+b=r this yields 2r-4=r, hence r=4 and a=b=2.

Thus the dependence step generalizes, but the balanced complementary-subspace/grid collapse is uniquely dimension four. This matches the set-sequential Hamiltonicity theorem recorded in 00a89cf51ecd, which gives spanning paths in the full projective systems for every r>=5.