# Density improvement forces an almost-period and binary carrier reduction

## Statement

Let A subset F_2^d\{0}, let n=|A|=2ell+1+t with t>=0, and let H(A) consist of all triples {x,y,x+y} contained in A. If |E(H(A))|/n>(ell-1)/3, then there is x in A such that at most t translation pairs {y,y+x} cross S=A union {0}. Equivalently b_S(x)<=t, and d_H(x)>=(n-1-t)/2=ell. Deleting one S-vertex from each crossing pair produces S0 subset S with |S\S0|<=t and S0+x=S0. Thus, after at most t vertex deletions, A has an exact 2-point carrier decomposition over the quotient F_2^d/<x>.

## Body

Let M be the number of unordered pairs {u,v} subset A for which u+v is not in A. Since every hyperedge accounts for its three unordered pairs,
3|E(H(A))| = C(n,2)-M.
The density hypothesis gives
C(n,2)-M > n(ell-1),
hence, using n=2ell+1+t,
M < n(t+2)/2.

Put S=A union {0}. For x in A define
b_S(x)=|{y in S:x+y notin S}|.
As usual, every bad unordered pair in A contributes two ordered failures and no pair involving 0 or a diagonal pair fails, so
sum_{x in A} b_S(x)=2M<n(t+2).
Therefore some x in A has b_S(x)<t+2.

Translation by x partitions the ambient vector space into 2-cycles {y,y+x}. The number b_S(x) is the number of these cycles crossing S, so
b_S(x) == |S| = n+1 == t (mod 2).
Because b_S(x)<t+2 and has the same parity as t, we obtain
b_S(x)<=t.

The internal x-translation pairs in S number (|S|-b_S(x))/2. One of them is {0,x}; every other internal pair {y,y+x} gives the hyperedge {x,y,y+x}. Hence
d_H(x)=(n+1-b_S(x))/2-1=(n-1-b_S(x))/2>=ell.

Finally, for each crossing x-pair delete its unique member lying in S. This deletes exactly b_S(x)<=t points and leaves a set S0 satisfying S0+x=S0. The pair {0,x} is internal, so 0,x remain in S0. Let pi:F_2^d -> F_2^d/<x>. Then S0=pi^{-1}(T) for some quotient domain T containing 0.

Writing each nonzero quotient fiber as G_q={(q,0),(q,1)}, the induced additive triple system on A0=S0\{0} has the exact binary carrier form:
(1) for each q in T\{0}, a vertical block {x,(q,0),(q,1)};
(2) for every quotient Schur triple {q,r,q+r} in T\{0}, the four lifted triples with bit parity epsilon_q+epsilon_r+epsilon_{q+r}=0.
Thus any density-beating induced Boolean domain at excess t is at vertex distance at most t from an exact unsigned t=1 carrier/doubling over a smaller induced Boolean domain.