# Endpoint-pair Hamiltonicity graphs have independence number at most two

## Statement

Let G be edge-orderable and fix distinct vertices u,v. On any set W disjoint from {u,v}, define a graph J on W by xy in E(J) exactly when G[{u,v,x,y}] is Hamiltonian. Then every three vertices of W span an edge of J. Equivalently, alpha(J)<=2, or the complement of J is triangle-free.

## Body

Take any three distinct x,y,z in W and consider the induced edge-ordered K5 on {u,v,x,y,z}. By smallset01, Section 4, at least three of its five four-vertex deletions are Hamiltonian.

Suppose none of xy,xz,yz is an edge of J. Then each of the three four-sets
{u,v,x,y}, {u,v,x,z}, {u,v,y,z}
is non-Hamiltonian. These are exactly the three four-subsets obtained by deleting respectively z,y,x from the K5. Therefore only the two remaining four-subsets, obtained by deleting u or v, could be Hamiltonian. This gives at most two Hamiltonian four-subsets, contradicting the certified K5 theorem.

Hence every triple in W contains at least one edge of J, so J has no independent set of order three. ∎