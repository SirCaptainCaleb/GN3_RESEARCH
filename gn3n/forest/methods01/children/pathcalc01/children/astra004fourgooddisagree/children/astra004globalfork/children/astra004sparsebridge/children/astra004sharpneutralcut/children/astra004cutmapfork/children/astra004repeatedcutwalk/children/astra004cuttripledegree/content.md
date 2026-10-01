# Three pairwise-compatible labels at one cut force odd degree at least three

## Statement

In the neutral cut normalization, let three distinct bad labels u,v,w have the same cut k, and suppose their chosen normalized deletion covers are pairwise support-compatible after deleting the corresponding label pairs. Then the Hamiltonian-support odd graph has a vertex of degree at least three. Consequently, under maximum odd degree two, every cut value contains at most two bad labels whose normalized covers form a pairwise support-compatible family.

## Body

For each compatible pair among {u,v,w}, astra004repeatedcutwalk gives exactly one of two types: either the S-block is fixed across the pair and the R-block varies by exchanging the two omitted labels, or the R-block is fixed and the S-block varies. Color the three edges uv,vw,wu by these two types. Two edges have the same color and share a vertex; after relabelling, suppose uv and uw both have fixed-S type. Then S_u=S_v and S_u=S_w, hence S_u=S_v=S_w=:S. Therefore the Hamiltonian support Q=S A^+ is the same component in all three deletion covers. For each t in {u,v,w}, the other component P_t is disjoint from Q and P_t union Q=V(H)-{t}, so P_t-Q is an odd-graph edge labelled t. The three labels are distinct, hence the three neighboring supports P_u,P_v,P_w are distinct. Thus deg_G(Q)>=3. The fixed-R case is symmetric.