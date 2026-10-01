# Complete reciprocal transversality forces repeated intersections among opposite-terminal paths

## Statement


Let H be a finite linear 3-graph, let v be a vertex, and let
  e_i={x_i,v,u_i},  i=1,...,k,
be distinct ascending nonspecial edges, with unique entrance x_i and terminals v,u_i. For each i let P_i be a maximum endpoint path ending at u_i, and assume e_i is terminal-single on P_i.

Assume complete reciprocal transversality: for every ordered pair i!=j, the path P_i contains at least one non-v vertex of e_j.

Partition the indices according to the unique off-u_i contact of e_i on P_i:
  X={i: x_i lies on P_i},
  V={i: v lies on P_i}.
Then:

(1) every pair of indices in X has paths with at least two common vertices;

(2) among the indices in V, the graph whose edges are pairs {i,j} with V(P_i) intersect V(P_j)={v} is triangle-free.

Consequently, if m=|X| and n=|V|, the number of pairs {i,j} for which P_i,P_j have at least two common vertices is at least
  binom(m,2)+binom(n,2)-floor(n^2/4).

In particular, for k>=4 at least one pair P_i,P_j has at least two common vertices.

If, moreover, the hypotheses of c9bb03cb2b41 hold for every owner edge e_i and its chosen P_i, and
  phi(e_i)+phi(e_j) <= phi(u_i)+3
for every ordered pair i!=j, then complete reciprocal transversality is automatic, so the conclusions above apply.


## Body


Terminal-singleness says that exactly one of x_i,v occurs in the precursor of P_i. In every case P_i contains its last vertex u_i.

If i is in X, then P_i contains both x_i and u_i. We do not need to assert that v is absent from the whole path in the general statement. (In the intended strict-gap application phi(u_i)>phi(e_i), e_i cannot be the last edge of P_i, and then linearity does make v absent.)

If i is in V, then P_i contains v and u_i, while x_i is absent from the whole path. Indeed x_i is not in the precursor by terminal-singleness. If x_i lay in the last edge, then either that last edge is distinct from e_i and would share both x_i and u_i with e_i, contradicting linearity, or the last edge is e_i; in the latter case a maximum e_i-ending path would have to enter e_i through its unique entrance x_i, putting x_i in the precursor, again a contradiction.

First take distinct i,j in X. By complete reciprocal transversality, P_i contains a vertex of {x_j,u_j}; both x_j and u_j lie on P_j. Similarly P_j contains a vertex of {x_i,u_i}, both of which lie on P_i. These two common vertices are distinct because e_i and e_j already meet at v, so linearity makes their off-v pairs disjoint. Hence P_i and P_j have at least two common vertices. This proves (1).

Now take distinct i,j in V and suppose
  V(P_i) intersect V(P_j)={v}.
The foreign hit of P_i on e_j cannot be u_j, because u_j lies on P_j and would then be a second common vertex. Since the only non-v vertices of e_j are x_j,u_j, P_i must contain x_j. Symmetrically P_j must contain x_i.

Suppose three indices i,j,l in V formed a triangle of such single-intersection pairs. Applying the preceding conclusion to the pairs {i,l} and {j,l}, both P_i and P_j contain x_l. But they also both contain v, contradicting
  V(P_i) intersect V(P_j)={v}.
Therefore the single-intersection graph on V is triangle-free, proving (2).

By Mantel's theorem, a triangle-free graph on n vertices has at most floor(n^2/4) edges. Thus at least
  binom(n,2)-floor(n^2/4)
pairs inside V have two or more common vertices. Adding all binom(m,2) pairs inside X proves the quantitative bound. If k=m+n>=4, either m>=2, giving an X-pair immediately, or n>=3; among any three V-indices not all three pairs can be single-intersection, so again a double-intersection pair exists.

For the final assertion, c9bb03cb2b41 applied with owner e_i, terminal u_i, and foreign edge e_j gives a non-v e_j-contact on P_i whenever
  phi(e_i)+phi(e_j)<=phi(u_i)+3.
Thus the ordered inequalities supply complete reciprocal transversality.
