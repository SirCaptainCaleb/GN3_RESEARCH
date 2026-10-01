# A singleton companion separates every nonadjacent pair in an edge-ordered two-cover

## Statement

Let G be an edge-orderable boundary tournament, represented by a strict total order on E(K_n). Suppose G has a spanning two-cover A|(q), where A=(a_0,...,a_m) is increasing and q is a singleton. If two vertices s=a_i and t=a_j of A satisfy j-i>=2, then G has a spanning two-cover separating s and t. Consequently, with respect to the inseparability relation defined by membership in the same component of every spanning two-cover, every inseparability class has size at most two whenever G admits a singleton-side two-cover; any inseparable pair must occur as consecutive vertices of A.

## Body

Put e_k=a_k a_{k+1}; since A is increasing, e_k<e_{k+1} for every applicable k. Let s=a_i and t=a_j with j-i>=2. Choose any k with i<=k<=j-2 and write a=a_k, b=a_{k+1}, c=a_{k+2}. Thus s lies in the prefix A[0,k], t lies in the suffix A[k+2,m], and ab<bc.

Compare the single edge bq with ab and bc. Because the edge order is strict and ab<bc, at least one of the inequalities bq<bc or ab<bq holds.

If bq<bc, then (q,b,c,a_{k+3},...,a_m) is an increasing path: its first edge is qb=bq, followed by bc and then the inherited increasing suffix edges. Together with the inherited prefix (a_0,...,a_k), this is a spanning two-cover separating s and t.

If ab<bq, then (a_0,...,a_k,b,q) is an increasing path: its final two edges are ab<bq, and all earlier edges are inherited from A. Together with the inherited suffix (c,a_{k+3},...,a_m), this is again a spanning two-cover separating s and t.

Thus every nonadjacent pair on A is separable. Now suppose G admits A|(q) and let C be an inseparability class. Any two vertices of C must lie on A, since q is alone in its component in this cover, and the preceding paragraph says any inseparable pair on A must be consecutive in the displayed linear order. Three distinct vertices cannot be pairwise consecutive in one linear order, while inseparability is an equivalence relation. Hence |C|<=2. ∎