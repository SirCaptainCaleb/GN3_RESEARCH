# The alternating rectangle forces an inner hook or four simultaneous reverse bridges

## Statement

Assume the all-nonsingleton alternating-rectangle conclusion of astra004recrect. Write the two source blocks as S_i=(...,s_i^-,s_i), i=1,2, and the two sink blocks as T_j=(t_j,t_j^+,...), j=1,2, so all four concatenations S_iT_j are tight and have order lambda. Let x be the common omitted vertex. Then either at least one inner outer-attachment reverse hook is tight, namely one of (x,s_i,s_i^-) or (t_j^+,t_j,x), or all four central reverse bridges (t_j,x,s_i) are tight for i,j in {1,2}. Equivalently, if every source-tail triple (s_i^-,s_i,x) and every sink-head triple (x,t_j,t_j^+) is tight, then every central triple (s_i,x,t_j) is non-tight and hence every (t_j,x,s_i) is tight.

## Body

# Proof

For each pair (i,j), consider the vertex sequence S_i,x,T_j. It has order |S_i|+1+|T_j|=lambda+1. Every consecutive triple is inherited from S_i or T_j except the three join triples
alpha_i=(s_i^-,s_i,x), beta_ij=(s_i,x,t_j), gamma_j=(x,t_j,t_j^+).
Since lambda is the maximum tight-path order, these three triples cannot all be tight. Thus for each (i,j), at least one of alpha_i,beta_ij,gamma_j is non-tight.

If some alpha_i is non-tight, boundary antisymmetry gives its reverse (x,s_i,s_i^-) tight. If some gamma_j is non-tight, its reverse (t_j^+,t_j,x) is tight. These are the asserted inner hooks.

Otherwise every alpha_i and every gamma_j is tight. The preceding three-clause obstruction then forces beta_ij non-tight for every one of the four pairs (i,j). Boundary antisymmetry gives (t_j,x,s_i) tight for all i,j. ∎