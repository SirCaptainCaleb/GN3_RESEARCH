# A tight path concentrates deletion averaging to fractional mass 2+1/lambda

## Statement

Let H be a minimum-order counterexample and let A be any tight path of order lambda. Then tau*(H) <= 2+1/lambda. In particular, for a globally longest path of order lambda and using lambda>=ceil((n-1)/2), tau*(H) <= 2+1/floor(n/2).

## Body

# Concentrated deletion averaging

Let H be a minimum-order counterexample and let A be a tight path with |A|=lambda. For every v in V(A), choose an exact two-path cover P_v|Q_v of H-v.

Assign fractional weight 1/lambda to each of the 2lambda path occurrences P_v,Q_v, and also assign weight 1/lambda to the path A itself.

Fix a vertex u outside A. It is present in exactly one member of P_v,Q_v for every v in A, so its coverage from the deletion-cover paths is lambda*(1/lambda)=1.

Fix u in A. It is present in exactly one member of P_v,Q_v for every v in A-{u}, giving deletion-cover coverage (lambda-1)/lambda. The additional copy of A contributes 1/lambda, so the total coverage is again exactly one.

Thus this is a feasible fractional path cover. Its total mass is

2lambda*(1/lambda)+1/lambda=2+1/lambda.

Taking A globally longest gives tau*(H)<=2+1/lambda. The certified half-order bound lambda>=ceil((n-1)/2) therefore yields tau*(H)<=2+1/floor(n/2): for n=2k or 2k+1 the right side is 2+1/k. Compared with uniform averaging over all one-vertex deletions, this is strictly better when n is even, and agrees in the sharp odd half-order shell n=2lambda+1.

The construction also shows why the sharp half-order shell is naturally persistent in the fractional route: when lambda=(n-1)/2, concentrating on a longest path and averaging all deletions give the same mass.
