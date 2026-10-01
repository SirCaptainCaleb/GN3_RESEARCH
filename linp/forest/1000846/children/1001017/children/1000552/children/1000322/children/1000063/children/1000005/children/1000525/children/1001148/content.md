# Every opposite-end single blocker is a safe rotation of the fixed nonspecial last edge

## Statement

Let P=(g_1,...,g_L) be a globally longest linear path whose last edge e=g_L is nonspecial with unique entrance x=g_{L-1}∩e. Let a be either vertex of g_1\g_2. If f≠g_1 is an edge through a with exactly one blocker vertex w∈V(P)\g_1, then there is another globally longest L-edge path P' whose last edge is still e. Moreover P' enters e through x. In particular w cannot be either terminal vertex of e.

## Body

Choose a terminal vertex t of e different from w; this is always possible because e has two terminal vertices. Regard P as an L-edge path with last vertex t. The endpoint-preserving single-blocker rotation 912c72c000da applies because w≠t, and produces an L-edge path P' with last vertex t using f. Inspecting its explicit construction shows that the last edge remains g_L=e. If w lies before g_{L-1}, the suffix g_{L-1},e is retained, so P' enters e through x. If w=x, then w lies in the consecutive pair g_{L-1},e and the rotation omits g_{L-1} and places f immediately before e, again entering e through x. The only remaining possibility for a blocker vertex in e is one of the two terminals y,z. If w=y, choose t=z (and symmetrically if w=z); then the same rotation yields a globally longest path ending in e whose penultimate edge is f and whose entrance label is y, contradicting nonspeciality and uniqueness of entrance x. Hence terminal blockers are impossible, and every opposite-end single blocker rotates within the state space of globally longest paths ending in e through x.
