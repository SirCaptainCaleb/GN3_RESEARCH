# At lambda equals 3c minus 3 the maximin parameter is minimal and the two larger quadratic-minimum components are nearly equal

## Statement

Let H be a minimum counterexample in the sharp half-order shell |V(H)|=2lambda+1. Choose, among all globally Phi-minimal spanning three-covers, one with maximum minimum component order c, and write its component orders m>=r>=c with d=m-r. Suppose lambda=3c-3. Then rho=ceil(lambda/2), where rho is the maximin minimum-component parameter. Moreover, if c=2k>=4 then d^2<4k-3=2c-3. If c=2k+1>=5 then d^2<4k=2(c-1), and a maximin-lex cover has component-order profile (6k,3k+1,3k)=(lambda,rho+1,rho). In particular |m-r|<sqrt(2c) throughout this boundary regime.

## Body

Let rho be the maximin parameter. Maximin compression gives a tight path with non-Hamiltonian complement of order at most 2rho+1. Since every tight path has order at most lambda in the sharp half-order shell, every path complement has order at least lambda+1. Hence rho>=ceil(lambda/2).

On the other hand, the universal quadratic/maximin inequality bd7998713cd1 gives
 6rho<=n+3c=2lambda+1+3c.
Substituting lambda=3c-3 yields
 6rho<=9c-5.
If c=2k, then lambda=6k-3 and the lower bound is rho>=3k-1, while the displayed upper bound gives rho<=floor((18k-5)/6)=3k-1. If c=2k+1, then lambda=6k and the lower bound is rho>=3k, while the upper bound gives rho<=floor((18k+4)/6)=3k. Thus in both parities
 rho=ceil(lambda/2).

Now assume c>=4, so rho>c. Because the chosen global Phi-minimum is secondary-maximal in its minimum component order, every maximin cover has strictly larger Phi: equality would produce another global Phi-minimum with minimum component rho>c.

First let c=2k. Then lambda=6k-3, n=12k-5, rho=3k-1, and m+r=10k-5. Since d=m-r, the normalized quadratic minimum has
 Phi_0=(2k)^2+((10k-5)^2+d^2)/2.
Any maximin cover has all three component orders at least rho. Its Phi is therefore at most the extreme value
 M=(6k-3)^2+2(3k-1)^2.
As just noted Phi_0<M. Direct subtraction gives
 2(M-Phi_0)=4k-3-d^2>0,
so d^2<4k-3=2c-3.

Now let c=2k+1>=5. Then lambda=6k is even and rho=3k, so 2rho=lambda. Since every path complement has order at least lambda+1, no path has non-Hamiltonian complement of order at most 2rho. The sharp-residue alternative of maximin01 therefore applies: a maximin-lex cover has profile
 (lambda,rho+1,rho)=(6k,3k+1,3k).
The normalized quadratic minimum has m+r=10k and
 Phi_0=(2k+1)^2+((10k)^2+d^2)/2.
The displayed maximin-lex cover has
 Phi_*=(6k)^2+(3k+1)^2+(3k)^2.
Again Phi_0<Phi_* because its minimum component rho exceeds c. Subtracting gives
 2(Phi_*-Phi_0)=4k-d^2>0,
so d^2<4k=2(c-1).

Both parity bounds imply d^2<2c, hence |m-r|<sqrt(2c). ∎