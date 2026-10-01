# Many common higher-rank edges force cycle-bearing edges or common unique-entrance traversal

## Statement

Let A and B be maximum endpoint paths of lengths L_A,L_B, and let p>max{L_A,L_B}. Let H be a set of T distinct hyperedges such that every h in H belongs to both A and B and has edge rank at least p.

Discard the at most two members of H that are the last edge of A or the last edge of B. For every remaining h, at least one of the following holds:

(C) h lies on a linear cycle;

(E) h is nonspecial and both A and B leave h toward their respective last vertices through the unique entrance of h.

Consequently at least one of the following holds:

(1) at least (T-2)/2 distinct edges of H lie on linear cycles;

(2) at least (T-2)/2 distinct edges of H satisfy (E).

Applied to the type-U non-cycle outcome of 20cdd04e92ca, where T>=M/6, this gives either at least M/12-1 distinct common edges lying on linear cycles, or at least M/12-1 common nonspecial edges that both higher-rank source paths leave through their unique entrances.

## Body

After discarding the last edges of A and B, each h in H is internal to both paths. Since phi(h)>=p>L_A,L_B, apply 0000bd602854.

Suppose first that, on at least one host, the forward path joint z is terminal at h. Let Q be a maximum phi(h)-edge path with last edge h and last vertex z. By 0000bd602854, Q has a second common vertex with the suffix of that host after h.

Apply 41100a9882dd to Q and this host suffix, taking z as the last vertex of Q. The last edge h of Q is not an edge of the suffix, because h precedes the suffix on the host. Therefore the shared-last-edge alternative of 41100a9882dd is impossible, and the two paths contain a linear cycle. More precisely, the cycle is formed by the terminal Q-segment ending at z and the corresponding suffix segment. Its Q-segment contains h: any second common vertex lies strictly beyond h on the host and hence is not a vertex of h other than z. Thus h lies on the resulting cycle. This is (C).

If (C) is not obtained from either host, then on neither host is the forward joint terminal at h. A special edge is terminal at each of its vertices, so h cannot be special. For a nonspecial edge, the only vertex not terminal at h is its unique entrance. Hence both hosts leave h through that same unique entrance. This is (E).

Thus every remaining edge lies in C or E. One of the two classes has size at least (T-2)/2.

For the final specialization, use T>=M/6 from the type-U non-cycle outcome of 20cdd04e92ca.
