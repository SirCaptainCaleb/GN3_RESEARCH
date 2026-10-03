# A mixed two-vertex middle forces an endpoint-rooted Hamiltonian four-set

**Summary:** In the mixed attachment case A|(z,w)|C, either a left or right local Hamiltonian four-set gives an immediate pairwise repartition, or both local four-sets are non-Hamiltonian and their forced matching-block orders produce the cross Hamiltonian path (a_{r-1},z,w,c_1). The latter support has a two-coverable complement but its same-component realization remains separate.

## Statement

Let H be a minimum counterexample and let A|(z,w)|C be a spanning three-cover in the mixed attachment case, with r=|A|, s=|C| at least two. Put a=a_{r-1}, b=a_r, c=c_1, d=c_2. Then either L={a,b,z,w} is Hamiltonian, in which case repartitioning A|(z,w) gives the same-component cover (a_1,...,a_{r-2})|L|C; or R={z,w,c,d} is Hamiltonian, symmetrically giving a same-component repartition; or both L,R are non-Hamiltonian, in which case (a,z,w,c) is a tight Hamiltonian four-path. In the third case its complement has path-cover number two by minimality, but no same-component pairwise-repartition claim is made.

## Body

The mixed-case lemmas give tight triples (a,b,z), (w,b,a), (w,z,b) on L={a,b,z,w}, and (z,c,d), (d,c,w), (c,z,w) on R={z,w,c,d}.

If L is Hamiltonian, then L together with the inherited prefix (a_1,...,a_{r-2}) partitions A union {z,w} into two tight paths (with the empty prefix omitted when r=2). Hence replacing A|(z,w) by these paths is a legal pairwise repartition, while C is unchanged. The symmetric statement holds if R is Hamiltonian.

Assume both L and R are non-Hamiltonian. By the non-Hamiltonian four-set matching-block classification, each is edge-orderable with its three opposite-edge matchings in consecutive blocks. On L the known triples give bw<ab<bz and wz<bz. With opposite-edge matchings {bw,az}, {ab,wz}, {bz,aw}, the block order is forced to be {bw,az}<{ab,wz}<{bz,aw}. Hence az<wz, so (a,z,w) is tight.

On R the known triples give zc<cd<cw and zc<zw. With opposite-edge matchings {zc,dw}, {cd,zw}, {cw,zd}, the block order is forced in that order. Hence zw<cw, so (z,w,c) is tight. Therefore (a,z,w,c) is a tight Hamiltonian four-path.

This cross support is proper, so minimum-counterexample calculus gives path-cover number two on its complement. However, it uses vertices from A, the middle component, and C simultaneously. Thus its existence alone does not certify that the resulting three-cover lies in the original pairwise-repartition component. The precise residue is therefore the double-non-Hamiltonian local case together with this forced cross four-path.

## Metadata

- ID: toolkit_vertex_middle_forces_an_endpoint_rooted_hamiltonian_four_set
- Kind: toolkit
- Version: 2
- Math version: 2
- Audit: unaudited
- Refutation: unrefuted
