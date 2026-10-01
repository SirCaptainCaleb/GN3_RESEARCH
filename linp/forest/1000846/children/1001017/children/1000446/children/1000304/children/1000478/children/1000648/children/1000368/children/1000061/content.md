# A potential-oriented charged ascending edge can have rank below both terminal potentials

## Statement

There is a six-edge linear 3-graph containing an ascending nonspecial edge e={1,5,6} with φ(e)=3, unique entrance 1, and vertex ranks φ(5)=φ(6)=4. Thus the potential-oriented condition φ(u)≥φ(v) does not force φ(e)=φ(v), even when the two terminal vertex ranks are equal.

## Body

Take edges A={1,5,6}, B={6,7,9}, C={1,2,9}, D={2,3,8}, E={0,1,3}, F={0,4,5}. This is linear. Its intersection graph has adjacencies A-B,A-C,A-E,A-F; B-C; C-D,C-E; D-E; E-F. The longest induced paths ending at A have length 3 and all enter A through vertex 1: for example D,C,A and D,E,A; any route attempting to enter A through 5 or 6 is blocked by the extra A-E or A-C adjacency, respectively. Hence φ(A)=3 and A is nonspecial with unique entrance 1. The vertex rank φ(1)=2, for example B,A ends with last vertex 1 and no 3-edge path can end there; thus A is ascending. On the other hand B,C,E,F is a 4-edge linear path with last vertex 5, so φ(5)≥4, and F,E,C,B is a 4-edge path with last vertex 6, so φ(6)≥4. Exact induced-path inspection gives φ(5)=φ(6)=4. Therefore A satisfies the potential-oriented condition at either terminal but φ(A)=3<4.