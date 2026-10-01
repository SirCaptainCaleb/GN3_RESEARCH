# Deletion-cover averaging gives a fractional path cover of mass 2n/(n-1)

## Statement

If H is a minimum-order counterexample on n vertices, then its fractional tight-path cover number satisfies tau*(H) <= 2n/(n-1)=2+2/(n-1). Equivalently, the deletion-cover family gives an explicit fractional cover whose excess over two is only 2/(n-1).

## Body

# Fractional cover from all one-vertex deletions

Let H be a minimum-order counterexample on n vertices. For each vertex v, choose an exact two-path cover P_v|Q_v of H-v, which exists by minimum-counterexample calculus.

Give each of the 2n path occurrences P_v,Q_v fractional weight 1/(n-1). (If the same path support appears more than once, combine the corresponding weights.)

Fix u in V(H). For each deletion label v != u, the vertex u belongs to exactly one of P_v,Q_v. For v=u it belongs to neither. Therefore the total fractional weight of chosen paths containing u is exactly

(n-1)/(n-1)=1.

Hence these weighted path supports form a feasible fractional cover of V(H). Their total weight is

2n/(n-1)=2+2/(n-1).

Thus tau*(H)<=2n/(n-1). By finite LP duality this is the fractional-cover form of the weighted near-half estimate under Astra's weighted-longest-path branch. In particular, any attempt to prove the grand theorem via Astra's rounding conjecture only needs to rule out a very narrow possible integrality-gap strip immediately above two in a minimum counterexample.