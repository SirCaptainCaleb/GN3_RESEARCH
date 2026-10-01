# An anchor neighborhood has complete cross-path incompatibility

## Statement

Let F_d=P|Q be a chosen deletion cover of H-d, and let N_P,N_Q partition the compatibility neighbors of d according to whether their labels lie on P or Q. Then every pair y in N_P, z in N_Q is incompatible. Moreover that incompatibility is support-incompatible solely because the restored label d lies in the P-support of F_y and in the Q-support of F_z. Within N_P and within N_Q, compatibility edges can occur only between consecutive neighbor labels in the corresponding displayed anchor order. Hence G[N(d)] is a subgraph of the disjoint union of the two path graphs on N_P and N_Q, while the complement of G[N(d)] contains the complete bipartite graph K_{|N_P|,|N_Q|}.

## Body

# Proof

Take y in N_P and z in N_Q. If F_y and F_z were compatible, then y,z would be adjacent in G[N(d)]. By 47d4a615286a, any such compatible pair must lie in the same displayed path of F_d. But y lies on P and z lies on Q, contradiction. Thus every cross-path pair is incompatible.

For the stronger support statement, apply compatanchorclass05. Compatibility of F_y with F_d forces the restored label d in F_y to lie in the same anchor support class as y, namely P. Likewise d lies in the Q-support of F_z. After deleting d the two covers agree, by compatanchorlocal03. Therefore their support incompatibility is carried exactly by d switching between the two anchor support classes.

Finally, 47d4a615286a already proves that an edge inside G[N(d)] can only join consecutive neighbor labels lying on one common anchor path. This gives the stated path-graph containment within N_P and N_Q and the complete cross-path incompatibility between them.
