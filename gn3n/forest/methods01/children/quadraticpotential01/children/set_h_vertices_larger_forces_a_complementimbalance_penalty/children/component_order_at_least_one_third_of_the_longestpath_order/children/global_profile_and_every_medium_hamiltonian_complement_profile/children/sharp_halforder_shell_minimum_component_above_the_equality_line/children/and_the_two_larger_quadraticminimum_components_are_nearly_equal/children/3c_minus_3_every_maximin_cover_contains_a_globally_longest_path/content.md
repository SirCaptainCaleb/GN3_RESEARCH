# At lambda equals 3c minus 3 every maximin cover contains a globally longest path

## Statement

Let H be a minimum counterexample in the sharp half-order shell |V(H)|=2lambda+1. Choose, among all globally Phi-minimal spanning three-covers, one with maximum minimum component order c, and suppose lambda=3c-3. Let rho be the maximin minimum-component parameter. Then every spanning three-cover whose minimum component order is rho contains a component of order lambda. More precisely: if c=2k>=4, every maximin cover has component-order multiset {6k-3,3k-1,3k-1}={lambda,rho,rho}; if c=2k+1>=5, every maximin cover has component-order multiset {6k,3k+1,3k}={lambda,rho+1,rho}. Thus every maximin cover consists of a globally longest tight path together with a most-balanced possible two-path cover of its complement.

## Body

By 86c6d5d44600, rho=ceil(lambda/2). Fix any maximin spanning three-cover and write its component orders x>=y>=z. By definition of rho, z=rho. Since lambda is the maximum tight-path order, x<=lambda.

Because rho>c in the stated ranges, this maximin cover cannot itself be globally Phi-minimal: otherwise it would be another global Phi-minimum whose minimum component order rho is larger than the secondary-maximal value c. Hence its quadratic potential is strictly larger than Phi_0, the potential of the chosen normalized global minimum.

First let c=2k>=4. Then lambda=6k-3, n=12k-5 and rho=3k-1. By 86c6d5d44600, if the normalized global minimum has orders m>=r>=c and d=m-r, then d^2<4k-3. For the maximin cover, x+y=n-rho=9k-4. Put e=x-y. Since x<=lambda, e<=3k-2. Moreover e has the same parity as 9k-4, so if e<3k-2 then e<=3k-4.

The two potentials satisfy
2(Phi_max-Phi_0)=e^2-d^2-9k^2+16k-7.
If e<=3k-4, the right side is at most
-8k+9-d^2<0,
contradicting Phi_max>Phi_0. Hence e=3k-2, and therefore
(x,y,z)=(6k-3,3k-1,3k-1)=(lambda,rho,rho).

Now let c=2k+1>=5. Then lambda=6k, n=12k+1 and rho=3k. By 86c6d5d44600, d^2<4k. For an arbitrary maximin cover, x+y=9k+1. Put e=x-y. The path-order cap gives e<=3k-1; parity implies that if e<3k-1 then e<=3k-3. Here
2(Phi_max-Phi_0)=e^2-d^2-9k^2+10k-1.
If e<=3k-3, the right side is at most
-8k+8-d^2<0,
again contradicting Phi_max>Phi_0. Therefore e=3k-1, and
(x,y,z)=(6k,3k+1,3k)=(lambda,rho+1,rho).

In both parities the largest maximin component has order lambda and is therefore globally longest. The other two components cover its complement of order lambda+1 and have the unique most-balanced sizes compatible with the displayed parity. ∎