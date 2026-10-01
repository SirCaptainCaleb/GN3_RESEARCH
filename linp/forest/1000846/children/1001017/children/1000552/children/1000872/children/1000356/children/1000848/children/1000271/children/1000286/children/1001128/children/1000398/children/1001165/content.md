# Distinguished agreements and offending cross-edges are complementary

## Statement

Fix two source rails Q_i,Q_j in a four-edge source-clean 0-1-1 block. For each offending edge e_k={x_k,v,u_k}, each rail contains exactly one of x_k,u_k. If the two rails choose the same member, that vertex is a distinguished common vertex of Q_i,Q_j. If they choose different members, e_k itself has one non-v vertex on each rail and is an offending cross-edge between them. Consequently, if a_ij is the number of shared distinguished vertices, exactly 4-a_ij of the four offending edges cross Q_i and Q_j at two distinct distinguished contacts.

## Body

For every k, source-clean transversality gives |V(Q_i) intersect {x_k,u_k}|=|V(Q_j) intersect {x_k,u_k}|=1. There are only two cases. If the chosen vertices agree, the common choice belongs to both rails and contributes one to a_ij. If they disagree, one rail contains x_k and the other contains u_k; since e_k={x_k,v,u_k}, the hyperedge e_k has one contact on each host rail. The four coordinates are disjoint source-terminal pairs, so these cases partition the four offending edges and the number of disagreement cross-edges is 4-a_ij. Thus a double-overlap pair has at most two offending cross-edges, while a triple-overlap pair has at most one.
