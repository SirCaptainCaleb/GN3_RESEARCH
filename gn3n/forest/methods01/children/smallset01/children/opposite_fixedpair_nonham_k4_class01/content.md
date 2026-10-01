# An opposite-oriented fixed pair classifies every non-Hamiltonian four-set

## Statement

Let H be a boundary tournament on four distinct vertices a,b,y,z. Suppose (a,y,b) and (b,z,a) are tight and H[{a,b,y,z}] is non-Hamiltonian. Then (y,a,z) and (z,b,y) are tight. Moreover exactly one of the following holds: (i) the four-set is the exceptional cyclic non-Hamiltonian configuration from smallset01; (ii) it is edge-orderable and, writing M0={ay,bz}, M2={az,by}, M1={ab,yz}, every representing edge order has the whole block M0 strictly before the whole block M2, with M1 occurring before M0, between M0 and M2, or after M2.

## Body

The word (b,z,a,y) has first triple (b,z,a) tight. If its second triple (z,a,y) were tight, then because (a,y,b) is tight the cyclicly shifted four-word (z,a,y,b) would be Hamiltonian; equivalently, non-Hamiltonicity of (b,z,a,y) forces the reversal (y,a,z) tight. Similarly, from (a,y,b,z) and the tight triples (a,y,b),(b,z,a), non-Hamiltonicity forces (z,b,y) tight. Thus the comparison digraph contains ay->yb, bz->za, ya->az, zb->by, which is the same local pattern as compatkernelclass27 after relabelling x=a, y=b, r=z, s=y. Hence every edge of M0={ay,bz} precedes every edge of M2={az,by}. If the comparison digraph is cyclic, smallset01 gives the exceptional cyclic non-Hamiltonian K4. If it is acyclic, smallset01 gives an edge-order representation; non-Hamiltonicity forces the three opposite-edge matchings to be strict blocks, and the forced M0<M2 relation leaves exactly the three placements of M1 stated above.
