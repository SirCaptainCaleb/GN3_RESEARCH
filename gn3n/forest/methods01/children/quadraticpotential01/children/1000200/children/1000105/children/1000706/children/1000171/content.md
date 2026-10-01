# Secondary quadratic normalization raises the sharp half-order shell minimum component above the equality line

## Statement

Let H be a minimum counterexample in the sharp half-order shell |V(H)|=2lambda+1, where lambda is the maximum tight-path order. Among all spanning three-covers minimizing Phi=sum |C_i|^2, choose one whose minimum component order c is as large as possible. Then lambda<=3c-3. Equivalently c>=ceil((lambda+3)/3).

## Body

By 23d0bf612df7, every globally Phi-minimal spanning three-cover with minimum component order c satisfies lambda<=3c-2. It remains only to rule out equality lambda=3c-2 for the secondary choice. Assume equality. The equality-shell theorem d7b3880e6944 gives the exact global profile. We show in both parities that another spanning three-cover has the same Phi and strictly larger minimum component order.

Let rho be the maximin parameter: the maximum possible minimum component order of a spanning three-cover. The general maximin-compression theorem maximin01 gives a tight path with non-Hamiltonian complement of order at most 2rho+1. In the sharp half-order shell every tight path has order at most lambda, so every path complement has order at least lambda+1. Hence rho>=ceil(lambda/2).

First let c=2k. Then lambda=6k-2, n=12k-3, and d7b3880e6944 gives the global Phi-minimum profile
(5k-1,5k-2,2k),
whose potential is
Phi_0=54k^2-30k+5.
The preceding lower bound gives rho>=3k-1. If rho>=3k, take a maximin cover. Since all three component orders are at least 3k and sum to 12k-3, convexity of the square function bounds its potential above by the extreme profile
(6k-3,3k,3k),
whose potential is 54k^2-36k+9<Phi_0. This contradicts global Phi-minimality. Therefore rho=3k-1.

Now 2rho=6k-2=lambda. No tight path can have complement of order at most 2rho, since every path complement has order at least lambda+1. Thus the sharp alternative of maximin01 applies: a maximin-lex cover has profile
(lambda,rho+1,rho)=(6k-2,3k,3k-1).
Its potential is exactly
(6k-2)^2+(3k)^2+(3k-1)^2=54k^2-30k+5=Phi_0.
Hence it is another global Phi-minimum, but its minimum component order 3k-1 exceeds 2k provided k>=2. The remaining k=1 case would give n=9, impossible for a minimum counterexample. This contradicts the secondary maximality of c.

Now let c=2k+1. Then lambda=6k+1, n=12k+3, and d7b3880e6944 gives the global profile
(5k+1,5k+1,2k+1),
with
Phi_0=54k^2+24k+3.
Here rho>=ceil(lambda/2)=3k+1. If rho>=3k+2, any maximin cover has all three orders at least 3k+2 and total 12k+3. Its potential is at most the extreme value at
(6k-1,3k+2,3k+2),
which is strictly below Phi_0; contradiction. Hence rho=3k+1.

Take a maximin cover. Its three component orders are all at least rho and sum to n. Therefore its potential is at most the extreme value
(6k+1,3k+1,3k+1),
which equals
(6k+1)^2+2(3k+1)^2=54k^2+24k+3=Phi_0.
Global Phi-minimality gives the reverse inequality, so equality holds. Thus this maximin cover is itself a global Phi-minimum and, by equality in the convex extremal bound, has exactly the displayed profile. Its minimum component order 3k+1 is strictly larger than 2k+1, again contradicting the secondary choice.

Equality lambda=3c-2 is therefore impossible. Since lambda and c are integers and lambda<=3c-2, we conclude lambda<=3c-3, equivalently c>=ceil((lambda+3)/3). ∎
