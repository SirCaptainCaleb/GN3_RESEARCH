# Near-Steiner classification for induced Boolean Schur triple systems

## Statement

Let A be a finite subset of an elementary abelian 2-group G with 0 not in A and n=|A| odd. Let H(A) have edges {x,y,x+y} contained in A, and let M be the number of unordered pairs {x,y} in A with x+y not in A. If M<n, then for some subgroup W<=G either A=W\{0}, or A=W\{0,a,b} for two distinct nonzero a,b in W. Equivalently, among odd-order induced Boolean Schur systems, being within fewer than n missing pairs of a Steiner triple system forces a projective system or a two-point deletion of one.

## Body

Put S=A union {0}, so |S|=n+1 is even. For x in S define
b_S(x)=|{y in S : x+y notin S}|.
Every bad unordered pair {x,y} subset A with x+y notin A contributes the two ordered failures (x,y),(y,x), while pairs involving 0 and diagonal pairs x=x never fail. Hence
sum_{x in S} b_S(x)=2M.

For nonzero x, translation by x partitions G into 2-cycles {y,y+x}. The number b_S(x) is exactly the number of those 2-cycles crossing S, so
b_S(x) == |S| (mod 2).
Since |S| is even, every b_S(x) is even.

Assume M<n. Then
sum_{x in A} b_S(x)=2M<2n.
There are n nonzero elements of S, and every positive b_S(x) is at least 2. Therefore some nonzero k in S has b_S(k)=0. Thus S+k=S.

Let K=Stab(S)={g in G:S+g=S}. Then K is a nontrivial subgroup. Let q=|K|, let pi:G->G/K, and write S=pi^{-1}(T), where 0 in T. Take K to be the full translation stabilizer, so T has trivial translation stabilizer.

For t in T define b_T(t)=|{u in T:t+u notin T}|. Every x in the K-coset t has
b_S(x)=q b_T(t),
and there are q such x. Therefore
2M=q^2 F_T,  where F_T=sum_{t in T} b_T(t).
Write s=|T|. Since T has trivial stabilizer, b_T(t)>=1 for every nonzero t in T, hence F_T>=s-1. Also |S|=qs, so M<n gives
q^2 F_T<2(qs-1).

If q>=4 and s>1, then q^2(s-1)<2qs, i.e. q(s-1)<2s, impossible for q>=4 and s>=2. Thus either s=1, in which case S=K is a subgroup and A=K\{0}, or q=2.

Assume q=2 and s>1. Then
4F_T<4s-2,
so F_T<=s-1. Together with F_T>=s-1 this gives equality, and hence
b_T(t)=1
for every nonzero t in T. (In particular s is odd, by the same 2-cycle parity observation.)

Now form a graph on T\{0} by joining distinct t,u when t+u notin T. The condition b_T(t)=1 says this graph is 1-regular: every nonzero t has a unique bad partner.

All bad pairs have the same sum. Indeed, let {a,b} and {c,d} be two distinct bad pairs. Every cross pair between the two matching edges is good, so
x=a+c, y=b+c, z=a+d
all lie in T. But x+y=a+b notin T, so y is the unique bad partner of x; and x+z=c+d notin T, so z is also the unique bad partner of x. Hence y=z, giving a+b=c+d. Call the common bad-pair sum h. Necessarily h notin T.

For every nonzero t in T, its unique bad partner is t+h, so t+h in T. Also for t,u in T, either t+u in T or {t,u} is a bad pair and t+u=h. It follows that Ubar=T union {h} is closed under addition; hence Ubar is a subgroup of G/K and T=Ubar\{h}.

Let W=pi^{-1}(Ubar), a subgroup of G. Since q=2, the missing coset pi^{-1}(h) has exactly two elements, say {a,b}; it does not contain 0. Thus
S=W\{a,b},
and therefore
A=W\{0,a,b}.
This proves the classification.