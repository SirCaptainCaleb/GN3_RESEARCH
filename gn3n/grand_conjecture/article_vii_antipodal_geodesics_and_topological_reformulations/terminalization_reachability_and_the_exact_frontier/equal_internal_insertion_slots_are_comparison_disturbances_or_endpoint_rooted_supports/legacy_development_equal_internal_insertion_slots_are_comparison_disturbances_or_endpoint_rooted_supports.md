# Equal internal insertion slots give disturbance or rail shortening — preserved pre-item development

## Development

Let F_a,F_b be compatible deletion covers. On H-{a,b}, let their common ordered supports be
P=(p_1,...,p_m) and Q.
Assume a,b are both inserted into the same internal gap between consecutive vertices
u=p_i, v=p_{i+1}.
Thus the two varying paths have the forms
(p_1,...,u,b,v,...,p_m)
and
(p_1,...,u,a,v,...,p_m).

The compatible-extension lemma gives a Hamiltonian four-support
K={u,v,a,b}.

Write
L=(p_1,...,p_{i-1}), R=(p_{i+2},...,p_m),
omitting empty intervals. Then H-K has the inherited cover
L | R | Q.

If both L and R are nonempty, any two-cover of H-K must contain an ordinary path edge joining two distinct inherited classes among L,R,Q: without such an edge, two path components cannot cover three nonempty classes. Hence this branch immediately enters the mixed-edge / split / leave-and-return comparison-disturbance interface.

If exactly one of L,R is empty, then uv is a displayed end-edge of P and
H-K = P^o | Q
is already an inherited two-cover, where P^o is P with that end-edge removed. Thus K is not merely a bounded support: it gives an explicit rail-shortening step deleting two consecutive vertices from one displayed rail while preserving the other rail exactly.

If both L,R are empty, then P={u,v}; K and Q are disjoint Hamiltonian supports covering H, contradiction.

Therefore an equal internal insertion slot yields exactly: direct comparison disturbance, inherited rail shortening by two, or a spanning two-cover. No bare bounded-support terminal branch remains.
