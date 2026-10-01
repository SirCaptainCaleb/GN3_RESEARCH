# The extremal C4 rail skeleton carries two clean length-two bridges

## Statement

In the extremal C4 simple-rail skeleton, the two nonsimple rail pairs have explicit terminal boundaries and clean two-edge bridges: after relabeling, Q_1,Q_2 share u_3,u_4 and e_3,e_4 is a u_3-u_4 path through v otherwise disjoint from both rails; symmetrically Q_3,Q_4 share u_1,u_2 with bridge e_1,e_2. Hence any clean elementary lens bounded by those terminal pairs has balanced side length at least two.

## Body

Assume the extremal simple-rail skeleton of de60628c8d58 is a 4-cycle. Relabel so the simple edges are
  13, 32, 24, 41,
and hence the nonsimple/theta pairs are
  12 and 34.

Because 13 and 23 are simple, cddeebb1b0b2 gives
  u_3 in V(Q_1) cap V(Q_2).
Because 14 and 24 are simple,
  u_4 in V(Q_1) cap V(Q_2).
Thus Q_1,Q_2 share the two distinct labeled terminals u_3,u_4.

Moreover simplicity of 13 and 23 forbids x_3 from lying on Q_1 or Q_2: any such X-hit would force the corresponding pair with Q_3 to be nonsimple. Likewise simplicity of 14 and 24 forbids x_4 from Q_1 or Q_2. The source rails Q_1,Q_2 also avoid the common terminal v of all offending edges.

Therefore the two-edge path
  e_3,e_4
connects u_3 to u_4 through v and is otherwise disjoint from Q_1 union Q_2:
  e_3={x_3,v,u_3},
  e_4={x_4,v,u_4}.

Symmetrically Q_3,Q_4 share u_1,u_2 and the two-edge path e_1,e_2 is otherwise disjoint from Q_3 union Q_4.

Consequently each of the two theta pairs in the C4 residue carries a clean third bridge of length two between its two explicitly labeled common terminal vertices.

If u_3,u_4 bound a clean elementary lens between Q_1,Q_2 with common side length t (balanced by 390e818020e1), then t>=2. Otherwise replacing either t-edge lens side by the clean 2-edge bridge e_3,e_4 would yield an endpoint-preserving path longer than the corresponding maximum source rail. The same holds for the u_1,u_2 lens on Q_3,Q_4.
