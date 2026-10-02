# Saturated boundary fans force a nonlocal blocker

## Statement

Let H have minimum degree delta=q>=5, let e={x,y,z} be an ascending nonspecial edge of rank q, and let Q=(g_1,...,g_t), t=q-1, be a canonical maximum x-ending path avoiding y,z. For a double blocker through an opposite endpoint a with blockers in A_i,A_j, the exact splice loss is j-i-1 when the later blocker is private and j-i when it is the forward joint; length is preserved exactly for consecutive private-private blockers {a,b_i,b_{i+1}}. If a saturated endpoint fan has only consecutive double blockers and no safe single rotation or length-preserving double splice, then S=2 is impossible and S=3 has one rigid ladder with only the final adjacency missing. Consequently, if both opposite endpoints a,a' are sinks of this kind, at least one fan contains a nonlocal double blocker.

## Body


Write A_i={b_i,c_i} for i=2,...,t, where b_i is private to g_i along Q, c_i=g_i∩g_{i+1} for i<t, and c_t=x.

First consider a double-blocking edge h through an opposite last vertex a with blockers u∈A_i and v∈A_j, 2<=i<j<=t. If v=b_j, the splice
(g_{i-1},g_{i-2},...,g_1,h,g_j,g_{j+1},...,g_t)
is linear, ends at x, and has length t-(j-i-1). If v=c_j with j<t, omitting g_j instead gives
(g_{i-1},...,g_1,h,g_{j+1},...,g_t)
of length t-(j-i). For j=t and v=x, the truncated splice (g_{i-1},...,g_1,h) has the same loss j-i. Hence a double-blocker splice preserves full length exactly when j=i+1 and the blockers are the consecutive private vertices b_i,b_{i+1}; linearity rules out c_i in that case.

Now assume a saturated fan has no safe single-blocker rotation and no length-preserving double-blocker splice, and every edge of its index graph joins consecutive indices. For a consecutive pair i,i+1, linearity forces the A_i blocker to be b_i. The private-private choice b_i,b_{i+1} is forbidden by the length-preserving splice just proved, so every consecutive double blocker must instead use b_i and c_{i+1}.

If S=2, the saturated index graph has t-1 vertices and t-2 edges, so it is the full chain 2-3-...-t. Its only defect vertices are c_2 and b_t. The two singleton blockers are the y- and z-types, hence one uses b_t. If h={a,b_t,y}, then
(g_{t-1},g_{t-2},...,g_1,h,e)
is a q-edge path ending in e through y, contradicting nonspeciality; the z-case is identical. Thus S=2 is impossible.

If S=3, the consecutive index graph is the full chain with one adjacency r,r+1 deleted. The x-type singleton must use x=c_t, forcing r=t-1. Therefore the defect vertices are c_2,b_{t-1},c_t=x,b_t. The same alternative-entrance splice shows b_t cannot be a y- or z-singleton, and it is not the x-singleton. Hence b_t is the unique uncovered blocker vertex; c_t is the x-type singleton; and c_2,b_{t-1} are the y- and z-singletons in some order. This is the unique rigid nearest-neighbor ladder.

Finally suppose both opposite last vertices a,a'' are sinks and every double blocker in both fans is local. The S=2 case is impossible, so both fans are the rigid S=3 ladder. Since q>=5, choose 2<=i<=t-2. The rigid ladder at a contains {a,b_i,c_{i+1}}, while the ladder at a'' contains {a'',b_i,c_{i+1}}. These distinct hyperedges share two vertices, contradicting linearity. Therefore at least one endpoint fan has a nonlocal double blocker.
