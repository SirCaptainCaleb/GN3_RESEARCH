# 43/48 near-extremizers carry five-sixteenths top-potential rotation mass

## Statement

Let (H_j) be a sequence of finite linear 3-uniform hypergraphs. Write
S_j=sum_v phi(v), m_j=|E(H_j)|, and n_j^+=|{v:d(v)>0}|.
Assume S_j/n_j^+ tends to infinity and
m_j >= (43/48)S_j-o(S_j).

Choose the maximum endpoint paths and switching families from d287da5967d5. For every active misaligned center v, let R(v) be a set of distinct vertices produced by single-blocker rotations of its chosen maximum phi(v)-edge path, each vertex in R(v) having endpoint potential at least phi(v). Then the choices may be made so that
sum_v |R(v)| >= (5/16-o(1))S_j.

Thus every asymptotic 43/48 near-extremizer carries center-indexed top-potential rotation-endpoint mass of asymptotic size at least 5S/16.

## Body

For each active misaligned vertex v, let F_v be the switching family supplied in d287da5967d5, and write s(v)=|F_v|. Every member of F_v is a single blocker on the chosen maximum p_v-edge path P_v, where p_v=phi(v).

Apply 5f8d96bf566a to P_v and F_v. Its cell-rotation argument gives an absolute constant C such that one can choose a set R(v) of distinct rotation endpoints satisfying
|R(v)| >= s(v)/2-C,
and every w in R(v) satisfies phi(w)>=p_v=phi(v).

Summing over active misaligned centers gives
sum_v |R(v)| >= (1/2)sum_v s(v)-C n_j^+.
By d287da5967d5,
sum_v s(v) >= (5/8-o(1))S_j.
Since n_j^+=o(S_j) by hypothesis, the last two displays yield
sum_v |R(v)| >= (5/16-o(1))S_j.

The count is center-indexed: a vertex may occur in R(v) for several centers. Controlling precisely that reuse is therefore the remaining global packing problem.
