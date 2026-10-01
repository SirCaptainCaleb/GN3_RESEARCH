# The central-reverse-triple rectangle has eight strict quadratic descents

## Statement

Assume the all-nonsingleton alternating rectangle of astra004recrect, with source blocks S_1,S_2 of order r and sink blocks T_1,T_2 of order lambda-r, and assume the branch of astra004rectbridge in which all source-tail and sink-head outer attachment triples are tight and all four central reverse triples are tight. Then for every i,j the tight maximum path S_iT_j together with the singleton (x) admits both legal pairwise repartitions (S_i x)|T_j and S_i|(x T_j). Consequently each of the two balanced deletion states (S_1T_1)|(S_2T_2)|(x) and (S_1T_2)|(S_2T_1)|(x) has four explicit strict Phi-decreasing repartitions, two on each lambda-component. Repartitioning S_iT_j|(x) as (S_i x)|T_j decreases Phi by 2r(lambda-r-1)>0, while repartitioning it as S_i|(x T_j) decreases Phi by 2(lambda-r)(r-1)>0. Thus the rigid reciprocal-equality residue is not a quadratic plateau: it carries eight synchronized strict descents.

## Body

# Proof

Assume the branch of astra004rectbridge in which none of the source-tail or sink-head outer attachment triples fails and all four central reverse triples are tight. Hence for each source S_i=(...,s_i^-,s_i), the triple (s_i^-,s_i,x) is tight, so appending x gives the tight path S_i x. Likewise, for each sink T_j=(t_j,t_j^+,...), the triple (x,t_j,t_j^+) is tight, so prepending x gives the tight path x T_j.

Fix i,j. Since S_iT_j is one component of one of the two lambda|lambda covers of H-x, the pair of components S_iT_j and (x) in the corresponding spanning three-cover may be repartitioned on their union either as (S_i x)|T_j or as S_i|(x T_j). These are two-path covers of that union because the displayed paths are tight and their supports partition V(S_iT_j) union {x}. Hence both are legal pairwise repartitions.

For the first repartition, the affected component orders lambda,1 are replaced by r+1,lambda-r. Therefore
Phi_old-Phi_new=lambda^2+1-(r+1)^2-(lambda-r)^2=2r(lambda-r-1),
which is positive because 2<=r<=lambda-2. For the second repartition the replacement orders are r,lambda-r+1, and
Phi_old-Phi_new=lambda^2+1-r^2-(lambda-r+1)^2=2(lambda-r)(r-1)>0.

Each balanced cover has two lambda-components, and each component admits both repartitions, giving four strict descents per balanced state and eight across the reciprocal pair. ∎