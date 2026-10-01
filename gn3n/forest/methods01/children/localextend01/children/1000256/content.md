# Parallel three- and four-vertex corridors with common endpoints Hamiltonize their union

## Statement

Let u,a,b,v,x be five distinct vertices of a boundary tournament. If (u,a,b,v) is a tight path and (u,x,v) is a tight path, then the induced five-vertex subtournament on {u,a,b,v,x} is Hamiltonian.

## Body

Suppose the five-set W={u,a,b,v,x} is non-Hamiltonian. By the certified non-Hamiltonian-five-set theorem in smallset01, W admits an edge-order representation in which a vertex sequence is tight exactly when its consecutive ordinary edges increase. The two displayed tight paths give ua<ab<bv and ux<xv.

If ux<ua, then x,u,a,b,v is increasing because ux<ua<ab<bv. If bv<xv, then u,a,b,v,x is increasing because ua<ab<bv<xv. Thus in a non-Hamiltonian W neither inequality can hold, so ua<ux and xv<bv. Combining these with ux<xv gives ua<ux<xv<bv, and therefore a,u,x,v,b is an increasing Hamilton path. This is again a contradiction. Hence W is Hamiltonian.