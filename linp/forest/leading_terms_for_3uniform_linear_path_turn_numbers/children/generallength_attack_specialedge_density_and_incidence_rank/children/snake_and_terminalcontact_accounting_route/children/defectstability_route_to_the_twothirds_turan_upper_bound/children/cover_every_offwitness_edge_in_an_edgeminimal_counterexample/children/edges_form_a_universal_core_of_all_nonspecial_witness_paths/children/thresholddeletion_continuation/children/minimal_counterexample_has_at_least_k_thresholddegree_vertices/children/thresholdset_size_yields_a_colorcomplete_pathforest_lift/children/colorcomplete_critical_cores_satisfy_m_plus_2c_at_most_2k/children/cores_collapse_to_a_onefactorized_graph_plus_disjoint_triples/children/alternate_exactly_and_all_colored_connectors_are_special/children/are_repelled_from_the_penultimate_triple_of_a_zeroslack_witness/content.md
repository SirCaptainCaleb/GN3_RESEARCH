# Unused terminal colors are repelled from the penultimate triple of a zero-slack witness

## Statement

Let
T_1,C_1,...,T_{c-1},T_c=e
be a zero-slack maximum witness for a nonspecial forest triple e, entered through x, and let y be another vertex of e. Let p_in be the port of T_{c-1} used by C_{c-2}, p_out the port used by C_{c-1}, and p_free the third port. If d is a connector color unused by the witness and the d-colored edge from y has its other X-endpoint w in T_{c-1}, then nonspeciality forces w=p_in. In particular at most one unused-color y-edge can meet T_{c-1}. The same holds for the other terminal z.

## Body

Let f={y,d,w}, where d is unused among the witness connectors C_1,...,C_{c-1} and w∈T_{c-1}.

Suppose first that w is p_out or p_free. Consider the sequence obtained by stopping the old witness at T_{c-1} and then appending f,e:
T_1,C_1,...,C_{c-2},T_{c-1},f,e.

It has
(2c-3)+2=2c-1
edges, equal to the rank of e from b93769ee6fab.

The new edge f meets T_{c-1} exactly at w and e exactly at y. Since d is an unused color, its D-vertex does not occur on the retained prefix. If w=p_free, no earlier retained connector contains w. If w=p_out, the only old connector using w is C_{c-1}, which has been omitted. Hence f is disjoint from every nonconsecutive edge of the displayed sequence.

Therefore the displayed sequence is a maximum path ending in e through entrance label y, contradicting that e is nonspecial with unique entrance x.

Thus w must be p_in. Since G is simple, y has at most one edge to the single vertex p_in, so at most one unused-color edge through y can meet T_{c-1}.

The argument for z is identical.