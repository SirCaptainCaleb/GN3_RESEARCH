# Every globally noninsertable vertex reverses a displayed path edge

## Statement

Let H be a boundary tournament, let B=(b_1,...,b_m), m>=2, be a displayed tight path, and let x lie outside B. If x is noninsertable into the displayed order of B, then there is an index i such that H contains a tight triple reversing the displayed edge b_i b_{i+1}.

More precisely, insert01 Section 3 yields either
(x,b_t,b_{t-1})
for some 2<=t<=m, or
(b_{t+1},b_t,x)
for some 1<=t<=m-1.
Thus global noninsertability is already a reversed-edge disturbance, not a separate terminal obstruction.

## Body

Since x is noninsertable into the displayed order of B, apply insert01 Section 3.

In alternative 1, for some 2<=t<=m-1 the comparison-digraph arc
f_t -> e_{t-1}
holds, where f_t={x,b_t} and e_{t-1}={b_{t-1},b_t}. Traversing these incident ordinary edges through their common vertex b_t, that arc is exactly the tight triple
(x,b_t,b_{t-1}).
This contains the displayed edge b_{t-1}b_t in reverse order.

In alternative 2, the arc
e_t -> f_t
holds, where e_t={b_t,b_{t+1}} and f_t={x,b_t}. Traversing through the common vertex b_t gives the tight triple
(b_{t+1},b_t,x),
which contains the displayed edge b_tb_{t+1} in reverse order.

The endpoint case t=m-1 is included in alternative 2, and m=2 causes no difficulty. Therefore one of the displayed path edges is reversed by a tight triple whenever x is noninsertable into every displayed position.

No additional hypothesis beyond noninsertability and insert01 Section 3 is used.
