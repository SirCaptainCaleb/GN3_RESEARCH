# Unused colors at a reachable endpoint avoid every outgoing forest port

## Statement

In a zero-slack maximum witness for a nonspecial forest triple, fix either opposite endpoint a and an unused connector color d. Unless the d-mate of a is one of the three vertices of the terminal triple e, that mate must be an incoming or private port of an internal forest triple; it cannot be an outgoing port. Consequently each opposite endpoint has at least c/2-2 distinct unused-color mates on incoming/private ports and none on outgoing ports.

## Body

Work in the zero-slack critical-core model, and let
  P=T_1,C_1,T_2,C_2,...,T_{c-1},C_{c-1},T_c=e
be a maximum witness for a nonspecial forest triple e={x,y,z}, entered through x. Put
  Q=P-e,
so Q is a (q-1)-edge path ending at x, avoids y,z, and q=2c-1.

Let a be either free opposite endpoint of T_1. Let d be a threshold color not used by the connectors C_1,...,C_{c-1}. In the d-perfect matching on X, let w=M_d(a), so f={d,a,w} is the corresponding DXX hyperedge.

The mate w cannot lie in T_1: otherwise f and T_1 would share the two X-vertices a,w, violating linearity. If w is one of x,y,z, call d exceptional. Since the colored graph is simple, at most one color has mate x, at most one has mate y, and at most one has mate z.

Assume now w notin {x,y,z}. Then w lies on Q, while d lies outside Q. Thus f is a single-blocking edge at the opposite endpoint a of Q, with unique blocker w. It avoids y,z and w!=x, so 174f0763685b gives a length-preserving rotation Q' ending at x and still avoiding y,z. Appending e gives another q-edge maximum witness P'=Q',e ending in the same nonspecial edge through the same entrance x.

By b93769ee6fab, every maximum witness for a nonspecial edge in zero slack contains every forest triple T_1,...,T_c. Therefore the single-blocker rotation Q->Q' is not allowed to delete any forest triple.

Inspect the explicit rotation formula of 174f0763685b.

For each internal forest triple T_i (2<=i<=c-1), its three ports relative to the orientation of Q are:
- the incoming port T_i∩C_{i-1};
- the outgoing port T_i∩C_i (for i=c-1, C_i means C_{c-1});
- the private port, lying in no connector of Q.

If w is the incoming port of T_i, then w is the joint of C_{i-1},T_i and the rotation deletes C_{i-1}; this is compatible with the universal-core requirement.

If w is the private port of T_i, the private-blocker rotation deletes the preceding path edge C_{i-1}; again compatible.

If w is the outgoing port of T_i, then w is the joint of T_i,C_i, and the joint-blocker rotation deletes T_i itself. This contradicts the fact that every rotated bad witness contains every forest triple.

Hence, for every nonexceptional unused color d, M_d(a) is either the incoming or the private port of some T_i with 2<=i<=c-1. It is never an outgoing port.

Since exactly c/2+1 colors are unused by P and at most three are exceptional, each opposite endpoint has at least
  c/2-2
distinct unused-color mates lying on incoming/private ports and no outgoing ports.
