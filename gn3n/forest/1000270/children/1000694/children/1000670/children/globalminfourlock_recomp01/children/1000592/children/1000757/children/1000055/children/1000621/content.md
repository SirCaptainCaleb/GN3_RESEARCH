# From lambda ten onward a secondarily balanced global quadratic minimum has no component of order four

## Statement

Let H be a minimum counterexample in the sharp half-order shell |V(H)|=2lambda+1 with lambda>=10. Among all spanning three-covers minimizing the quadratic potential Phi, choose one whose minimum component order is as large as possible. Then every component has order at least five.

## Body

Let A|B|C be the chosen spanning three-cover, with component orders a>=b>=c.

Because H has no spanning two-cover, the connected component of the pairwise-repartition graph containing A|B|C contains no two-cover. Global Phi-minimality implies Phi-minimality in that connected component. Since lambda>=10, H has order at least 21. The certified minimum-side theorem d1e3453f5ffe therefore gives
c>=4.

Suppose for contradiction that c=4. Write the four-vertex component as X and the other two components as P,Q, with orders m>=r. Since
4+m+r=2lambda+1,
we have
m+r=2lambda-3.                                      (1)

We first note that r>=6. If r<=5, then by (1)
m>=2lambda-8>lambda
because lambda>=10. But m is the order of a tight path and lambda is the maximum tight-path order, contradiction.

Thus the certified endpoint-pair complement theorem 150f88194ce1 applies. Let E be the four displayed endpoints of P and Q. Fix x in X and a two-element set {e,f} subset E, and put
F=(X-{x}) union {e,f}.
The theorem gives that F is Hamiltonian, H-F has path-cover number two, and every two-cover U|V of H-F has imbalance
delta=||U|-|V||
satisfying
delta^2 >= d^2+2s-19,                              (2)
where
s=m+r,  d=m-r>=0.

The complement H-F has order s-1. Therefore delta has the same parity as s-1, while d=m-r has the same parity as s=m+r. Hence delta-d is odd. Equation (2), together with s>=12, gives delta>d, so delta-d is a positive odd integer.

We claim delta cannot equal d+1. Otherwise (2) would imply
(d+1)^2 >= d^2+2s-19,
hence
2d+1 >= 2s-19.
Thus
2(s-d)<=20.
But s-d=2r, so 4r<=20, contradicting r>=6. Therefore
delta>=d+3.                                         (3)

Order the complement cover so p=|U|>=q=|V|. Since p+q=s-1, (3) gives
q=(s-1-delta)/2 <= r-2,
and hence
p>=m+1.                                             (4)

No tight path has order greater than lambda, so p<=lambda. From (4),
m<=lambda-1.                                        (5)

On the other hand, m>=r and (1) give
m>=ceil((2lambda-3)/2)=lambda-1.                    (6)

Thus
m=lambda-1,  r=lambda-2.                            (7)

Now H-F has order 2lambda-4. From q<=r-2=lambda-4 and p<=lambda,
q=(2lambda-4)-p>=lambda-4.
Therefore every such two-cover has orders
p=lambda,  q=lambda-4.                              (8)

Consequently
F | U | V
is a spanning three-cover of H with component orders
5, lambda, lambda-4.

The original cover has component orders
4, lambda-1, lambda-2.
Their quadratic potentials are
Phi_old=4^2+(lambda-1)^2+(lambda-2)^2
       =2lambda^2-6lambda+21,
and
Phi_new=5^2+lambda^2+(lambda-4)^2
       =2lambda^2-8lambda+41.

If lambda>=11, then Phi_new<Phi_old, contradicting global Phi-minimality.

If lambda=10, then Phi_new=Phi_old. Hence F|U|V is also globally Phi-minimal, but its minimum component order is
min{5,10,6}=5,
strictly larger than the minimum component order 4 of the chosen cover. This contradicts the secondary choice maximizing the minimum component order among global Phi-minima.

Thus c cannot equal four. Since c>=4, we conclude c>=5. ∎