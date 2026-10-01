# The opposite-orientation residue is cyclic or has a forced matching-block precedence

## Statement

Assume the opposite-orientation residue of compatdualorient26: r in R, s in S, and distinct special labels x,y satisfy (y,r,x) and (x,s,y) tight. If X={x,y,r,s} is non-Hamiltonian, then exactly one of the following holds. (i) X is the exceptional cyclic non-Hamiltonian four-vertex boundary tournament from smallset01. (ii) X is edge-orderable and, in every representing edge order, the opposite-edge matching M0={yr,xs} occurs strictly before M2={xr,ys}. Since a non-Hamiltonian edge-ordered K4 has its three opposite-edge matchings as strict consecutive blocks, the remaining matching M1={xy,rs} may occur before M0, between M0 and M2, or after M2. Thus the possible block orders are M1<M0<M2, M0<M1<M2, or M0<M2<M1.

## Body

Assume X={x,y,r,s} is non-Hamiltonian. The two given tight triples are
(y,r,x) and (x,s,y).

Because (y,r,x,s) is not a Hamilton tight path, its second consecutive triple (r,x,s) is non-tight. Boundary antisymmetry therefore gives (s,x,r) tight. Likewise, because (x,s,y,r) is not Hamiltonian, (s,y,r) is non-tight, so (r,y,s) is tight.

Hence the comparison digraph on the six ordinary edges of K_X contains
yr -> rx,
xs -> xr,
xs -> sy,
yr -> ys.
Therefore every edge of M0={yr,xs} precedes every edge of M2={xr,ys} in the comparison relation.

If the comparison digraph Gamma(H[X]) is cyclic, smallset01's four-vertex classification gives the exceptional cyclic non-Hamiltonian four-vertex boundary tournament, yielding (i).

Otherwise Gamma(H[X]) is acyclic, so smallset01 gives an edge-order representation of H[X]. Since X is non-Hamiltonian, the matching-block classification says that its three opposite-edge perfect matchings form three strict consecutive blocks in every representing edge order. The four forced comparison arcs above imply that the whole M0 block precedes the whole M2 block. The third matching M1={xy,rs} is unconstrained by those four comparisons beyond being a separate strict block, so it may lie before M0, between M0 and M2, or after M2. These are exactly the three block orders M1<M0<M2, M0<M1<M2, M0<M2<M1.

The cyclic and edge-orderable alternatives are exclusive because the latter has acyclic comparison digraph. ∎