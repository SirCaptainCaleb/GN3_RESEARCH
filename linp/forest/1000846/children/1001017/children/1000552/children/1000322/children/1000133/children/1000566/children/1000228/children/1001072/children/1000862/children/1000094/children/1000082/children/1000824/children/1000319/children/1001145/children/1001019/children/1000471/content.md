# Odd-k rigid zero-slack branch either crosses into B or all three target ports share the same half-neighborhood

## Statement

Assume the rigid zero-slack no-switch normal form fb4fc1ee4179 and let k be odd. Let S=N_G(y)=N_G(z), |S|=k, and write R=X\S=B_X union e, where B_X is the union of the forest triples indexed by B and e={x,y,z}.

Then either:

(A) some DXX edge joins S to B_X; or

(B) N_G(x)=S as well. In case (B), all three vertices x,y,z of e are adjacent to every vertex of S and to no vertex of B_X.

## Body

Fix a color d. By e3c7e513d6ec, the d-perfect matching M_d has at least three S-R crossing edges. Two are the edges incident with y and z, whose partners lie in S.

Consider any further crossing edge of M_d. Its R-endpoint lies either at x or in B_X. If for some color a further crossing has its R-endpoint in B_X, then (A) holds.

Suppose (A) never occurs. Then for every color d, every S-R crossing beyond the y- and z-edges must use x. Because M_d is a matching, at most one crossing edge can use x. Since k is odd, the total number c_d of crossing edges is odd; after the two y,z crossings, at least one further crossing is required. Therefore for every d the x-edge of M_d crosses into S.

Thus x has one neighbor in S in every one of the k colors. These k neighbors are distinct because G is simple/proper at x, so d_G(x)=k gives N_G(x)=S. Since x has degree exactly k in the zero-slack DXX graph, it has no neighbor in B_X. Together with the already known N_G(y)=N_G(z)=S, this proves (B).
