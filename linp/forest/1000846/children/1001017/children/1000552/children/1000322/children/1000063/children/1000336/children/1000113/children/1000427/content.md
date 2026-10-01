# Endpoint deficiency pays for clean extensions and single rotations

## Statement

Let H be a linear 3-graph of minimum degree δ, and let P=(g_1,...,g_s) be any linear path with last vertex x. Let a be a last vertex of g_1 at the opposite end. Among edges f≠g_1 through a, let C be the number with no vertex of f\{a} in V(P)\g_1, let S be the number with exactly one such blocker vertex, and let D be the number with two. Then C+S+D=d_H(a)-1, S+2D<=2s-2, and consequently 2C+S>=2(d_H(a)-s)>=2(δ-s).

## Body

Because every edge f≠g_1 through a already meets g_1 in a, linearity forbids either other vertex of f from lying in g_1. Thus the two vertices of f\{a} contribute zero, one, or two blockers in V(P)\g_1, giving the partition C,S,D and C+S+D=d_H(a)-1. Distinct edges through a have disjoint blocker vertices outside a, so S+2D<=|V(P)\g_1|=2s-2. Hence 2C+S=2(C+S+D)-(S+2D)>=2(d_H(a)-1)-(2s-2)=2(d_H(a)-s)>=2(δ-s).
