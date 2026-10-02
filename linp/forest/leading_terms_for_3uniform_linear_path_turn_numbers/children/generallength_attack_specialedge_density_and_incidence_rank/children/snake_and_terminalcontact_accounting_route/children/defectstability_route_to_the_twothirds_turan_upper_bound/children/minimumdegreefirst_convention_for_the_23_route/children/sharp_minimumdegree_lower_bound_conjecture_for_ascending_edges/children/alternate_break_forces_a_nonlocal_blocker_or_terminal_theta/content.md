# Type-B alternate break forces a nonlocal blocker or terminal theta

## Statement


In loss-one sink case (B), let P=(p_1,...,p_s), s=q-2, end at x with opposite last vertex a, and let h_x be the mandatory x-type singleton blocker. Then C=(p_1,...,p_s,h_x) is a linear cycle of length q-1. Deleting p_s yields a canonical second x-ending path P^*=(p_{s-1},...,p_1,h_x).

Write A_s={b_s,x} and A_{s-1}={b_{s-1},c_{s-1}} with c_{s-1}=p_{s-1}∩p_s. If neither last vertex of A_{s-1} admits a safe single-blocker rotation on P^*, then the unique double blocker through a containing b_s pairs b_s with a blocker in some cell A_j with j<=s-2.

Moreover, at c=c_{s-1}, the deleted edge p_s={c,b_s,x} is itself an x-type single blocker relative to P^*. Hence if c is a safe sink, its deficiency-two normal form cannot be the perfect-double-matching type. In that case c has a clean edge f through one of the terminals y,z of e={x,y,z}, and P^*, p_s, and f,e form three internally disjoint c-to-x branches of lengths q-2,1,2. Thus their union is a theta containing linear cycles of lengths q-1, q, and 3.


## Body


The loss-one Type-B normal form provides an x-type single blocker h_x through the opposite endpoint a and x. Relative to the deficiency-two path P=(p_1,...,p_s), h_x meets p_1 at a, meets p_s at x, and is disjoint from the internal edges, so C=(p_1,...,p_s,h_x) is a linear (q-1)-cycle. Deleting h_x recovers P. Deleting p_s instead leaves the path
P^*=(p_{s-1},p_{s-2},...,p_1,h_x),
which still ends at x because x is now free in the end edge h_x. This is the canonical alternate Type-B break.

Exact Type-B saturation partitions the blocker vertices outside p_1 between the two singleton blockers and the double blockers. The x-type singleton uses x, while the terminal-type singleton cannot use the final cell. Thus the private final-cell vertex b_s belongs to a unique double blocker d={a,b_s,u}. Suppose u lay in A_{s-1}. Since b_s is precisely the vertex omitted when p_s is deleted, while a remains on P^* as p_1∩h_x, the same edge d would become a safe single blocker at the opposite endpoint u of P^*: it has only the additional blocker a on P^*, avoids the terminals, and is distinct from the prescribed singletons. Therefore, if both new far endpoints in A_{s-1} are trapped, u must instead lie in some A_j with j<=s-2. This is the forced nonlocal final-cell blocker.

At the joint endpoint c=c_{s-1}, the deleted edge p_s={c,b_s,x} meets P^* exactly in its two last vertices c and x, with b_s outside P^*. Hence p_s is an x-type single blocker at c. The exact deficiency-two sink classification therefore excludes its perfect-double-matching case, the only type with no singleton blockers. In each remaining safe-sink type there is a clean edge f through c and one of the terminals y,z of e={x,y,z}.

Now f meets P^* only at c, e meets P^* only at x, and p_s meets P^* only at c and x. By linearity, p_s∩f={c}, f∩e is the chosen terminal, and e∩p_s={x}. Consequently the three c-to-x branches P^*, p_s, and f,e are internally disjoint. Their lengths are q-2,1,2, respectively. The theta therefore contains the cycles P^*∪{p_s} of length q-1, P^*∪{f,e} of length q, and {p_s,f,e} of length 3.
