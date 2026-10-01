# A mixed singleton pair either pays rank sum or forms a host triangle

## Statement

Let P=(g_1,...,g_p) be a maximum p-edge path with last vertex v and last edge h=g_p. Let
  e={x,v,u},  f={y,v,z}
be distinct ascending nonspecial edges, neither equal to h, that are terminal at v and each have exactly one off-v contact with V(P)\h.

Assume at least one of the two contacts is the opposite terminal of its edge rather than its unique entrance. Then at least one of the following holds:
(1) phi(e)+phi(f) >= p+4;
(2) there is a path edge g_i such that g_i,e,f form a linear 3-cycle.

Equivalently, a mixed entrance/terminal-only singleton pair with rank sum at most p+3 necessarily forms a linear 3-cycle with the host path.

## Body

Let c_e,c_f be the two distinct off-v contact vertices. Distinctness follows from linearity, since e and f already share v.

If the path-edge occurrence intervals I(c_e),I(c_f) are disjoint, order them from left to right. The separated mixed-singleton rank-sum lemma e9fc907b07c9 applies and gives
  phi(e)+phi(f)>=p+4.

Otherwise the two occurrence intervals overlap. Hence some path edge g_i contains both c_e and c_f. Because e and f are distinct edges through v, linearity gives
  e∩f={v}.
Also g_i∩e={c_e} and g_i∩f={c_f}; these intersections are distinct, and v is not in g_i because v is the last vertex of P and i<p. Thus g_i,e,f are three edges with three distinct pairwise intersection vertices and no other pairwise intersections. They form a linear 3-cycle.

No source-clean hypothesis, opposite-terminal single-contact hypothesis, minimum-terminal orientation, paid certificate, or near-extremal assumption is used.
