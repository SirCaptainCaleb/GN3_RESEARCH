# Odd-k rigid zero-slack no-switch state must contain an A-to-B connector

## Statement

In the rigid zero-slack no-switch normal form fb4fc1ee4179 with odd k, let A,B partition {1,...,c-1} as in 4468081d47b0 and let S be the union of the triples T_j with j∈A. Then the DXX graph contains an edge joining S to the union B_X of the triples indexed by B.

## Body

By 6894769a092f, if there is no S-B_X connector then all three ports x,y,z of the target triple e=T_c have common neighborhood S.

But the original alternating witness is
  T_1,C_1,T_2,...,T_{c-2},C_{c-2},T_{c-1},C_{c-1},T_c=e.
The connector C_{c-2} joins T_{c-2} to T_{c-1}. By the definition
  B={j∈{2,...,c-1}: some DXX connector joins T_{j-1} to T_{c-1}},
this implies c-1∈B.

On the other hand C_{c-1} joins a vertex of T_{c-1} to x∈e. Thus x has a DXX neighbor in T_{c-1}, a triple belonging to B_X. This contradicts N_G(x)=S, since S contains only A-indexed triples and A∩B=∅.

Therefore the no-S-B_X alternative is impossible, and an S-B_X connector must exist.