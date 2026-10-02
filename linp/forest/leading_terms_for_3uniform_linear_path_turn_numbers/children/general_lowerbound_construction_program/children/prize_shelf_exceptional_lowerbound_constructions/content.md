# Prize shelf: exceptional lower-bound constructions

## Statement

Curated shelf of especially strong, reusable, or potentially novel lower-bound results for linear-path Turán numbers. First prize: the PG(3,2) construction proving ex_L(n,P_7^(3)) >= (7/3)n-O(1).

## Body

PRIZE 1 — PG(3,2) gives the 7n/3 lower bound for P7.

Result. Let H be the 3-uniform hypergraph whose 15 vertices are the nonzero vectors of F_2^4 and whose 35 edges are the projective lines {x,y,x+y}. Then H contains no 7-edge linear path. Consequently,
ex_L(n,P_7^(3)) >= 35 floor(n/15) = (7/3)n-O(1),
with equality to (7/3)n in the construction when 15 divides n.

Proof. Suppose a spanning P7 exists and let J be its six joints. Hyperplane incidence counting gives |J∩Pi| even for every projective hyperplane Pi, hence XOR(J)=0.

Now J must contain a line. If it were line-free, every one of its 15 pair-sums x+y would lie outside J∪{0}. These pair-sums are distinct: equality x+y=u+v for disjoint pairs would, using XOR(J)=0, force the two remaining joints to be equal. But only 9 vectors lie outside J∪{0}, contradiction.

So J contains a line L={u1,u2,u3}; XOR(J)=0 forces the remaining three joints to form a second disjoint line M={w1,w2,w3}. Consecutive joints cannot lie on the same line, so they alternate u1,w1,u2,w2,u3,w3.

The nine non-joint points form the 3x3 grid u_i+w_j. The five internal path edges consume
u1+w1, u2+w1, u2+w2, u3+w2, u3+w3,
leaving
u1+w2, u1+w3, u2+w3, u3+w1.
An endpoint line through u1 other than L requires two unused grid points in one W-column, both in rows other than u1. No remaining column has such a pair. Therefore the first endpoint edge cannot exist, contradiction.