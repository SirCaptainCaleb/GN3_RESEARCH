# An internal clean detour yields edge reversal, a Hamiltonian five-window, or a doubled reverse barrier

## Statement

In the setting of 0227c4505eec, suppose the replaced inherited edge xy is internal in its displayed path R, with predecessor p and successor q. Then at least one of the following holds: (1) a tight path on the detour support contains the reversed consecutive pair y,x; (2) a Hamiltonian five-set is supported on {p,x,y,q,w}, where w is one endpoint of the exterior detour; (3) one side of xy carries a doubled reverse barrier, namely either both (w,q,y),(q,w,y) or both (x,p,w),(x,w,p) are tight.

## Body

Write the clean detour as D=(x,u_1,...,u_k,y). By 214a634b4fd9, either its cycle branch gives outcome (1), or one of the wrap triples (x,y,u_k) and (u_1,x,y) is tight. Because xy is internal in the displayed inherited path R, its neighboring inherited triples (p,x,y) and (x,y,q) are tight. If (x,y,u_k) is tight, apply edge_extender_five with u=u_k to obtain a Hamiltonian five-set on {p,x,y,q,u_k} or the doubled right reverse barrier (u_k,q,y),(q,u_k,y). If (u_1,x,y) is tight, apply the symmetric half with u=u_1 to obtain a Hamiltonian five-set on {p,x,y,q,u_1} or the doubled left reverse barrier (x,p,u_1),(x,u_1,p).