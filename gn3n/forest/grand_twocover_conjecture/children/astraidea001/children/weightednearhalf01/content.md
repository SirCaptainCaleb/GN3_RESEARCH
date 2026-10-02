# Minimum counterexamples satisfy the weighted half principle up to one minimum vertex

## Statement

Let H be a minimum-order counterexample to the grand two-cover conjecture, with n vertices, and let w:V(H)->R_{>=0} have total weight W. Then H has a tight path P with w(V(P)) >= (W-min_v w(v))/2 >= (n-1)W/(2n). In particular Astra's weighted longest-path conjecture holds for every nonnegative weight function that vanishes at some vertex.

## Body

# Weighted near-half lemma

Let H be a minimum-order counterexample on n vertices, and let w be a nonnegative vertex weight function. Put W=sum_{v in V(H)} w(v), and choose v of minimum weight.

By minimum-counterexample calculus, H-v has an exact two-path cover P|Q. Hence

w(V(P))+w(V(Q))=W-w(v).

Therefore one of P,Q has weight at least (W-w(v))/2. Since w(v)<=W/n, this is at least

(W-W/n)/2=(n-1)W/(2n).

If min_v w(v)=0, the first bound is W/2, exactly the conclusion of the weighted longest-path principle. Thus any failure of that principle inside a minimum counterexample must use a strictly positive weight vector, and its multiplicative gap below one half is at most 1/(2n).

No path surgery is used: the estimate is an immediate global consequence of the exact two-covers of all one-vertex deletions.