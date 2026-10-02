# Cyclic-transient decomposition for the transfer digraph

## Statement

Split the nonspecial-edge transfer digraph into its vertices lying on directed cycles and the remaining transient vertices. Use the Minty-type closed-walk inequality on the cyclic part and blocker/rotation arguments on the transient part. It would suffice to prove A_cyclic<=H_2+O(n) and A_transient=O(n); together with the refined ascending-edge accounting this gives m<=(2ell/3+O(1))n.

## Body

Closed-walk potentials naturally control only recurrent transfer structure. This limitation is genuine: the three-center one-factorization examples have many ascending edges but essentially source-to-sink transfer structure, so a circulation argument cannot see all ascending edges. The proposed division therefore treats the cyclic part by the Minty-type inequality and the transient part by repeated-blocker and path-rotation arguments. The concurrent repeated-blocker program for four ascending edges through one common last vertex is a natural candidate for the transient estimate. The remaining cyclic obligation is to construct a circulation or cycle packing whose positive contribution detects ascending edges while its negative contribution can be charged to the strongly decreasing nonascending edges counted by H_2.