# Single-blocker surplus below the conjectured ascending threshold

## Statement

Let H be a linear 3-graph of minimum degree δ, let x be a vertex, and let Q=(g_1,...,g_t) be a path of length t=φ(x) with last vertex x. Let z be a last vertex of g_1 at the opposite end. For f≠g_1 containing z, call f single-blocking if exactly one vertex of f\{z} lies in V(Q)\g_1, and double-blocking if both do. If S and D are their numbers, then S+D=d_H(z)-1 and S+2D<=2t-2. Hence S>=2(δ-t). In particular, if t<=δ-1 then S>=2.

## Body

Every edge f≠g_1 containing z must meet V(Q)\g_1; otherwise f,g_1,...,g_t is a (t+1)-edge linear path with last vertex x, contradicting t=φ(x). Because f already meets g_1 at z, linearity implies neither of the other two vertices of f lies in g_1. Thus every such edge is either single-blocking or double-blocking as defined. Distinct incident edges through z have pairwise disjoint blocker vertices outside z, again by linearity. Since |V(Q)\g_1|=2t-2, the blocker count gives S+2D<=2t-2, while S+D=d_H(z)-1>=δ-1. Therefore S=2(S+D)-(S+2D)>=2(δ-1)-(2t-2)=2(δ-t).
