# Pairwise-compatible anchor neighbors occupy at most four consecutive positions

## Statement

Let F_d=P|Q be an anchor deletion cover with P=(p_1,...,p_m). Let S be a set of indices such that each deletion cover F_{p_i}, i in S, is compatible with F_d, and the family {F_{p_i}: i in S} is pairwise compatible. Then max S-min S<=3. Equivalently, every such pairwise-compatible cluster on one anchor path is supported on at most four consecutive anchor positions.

## Body

Take i<j in S. Since both F_{p_i} and F_{p_j} are compatible with the anchor F_d, compatrelocationinterval07 applies. If j-i>=4, it forces F_{p_i} and F_{p_j} to have an interval of relative-order reversals and hence to be incompatible, contradicting pairwise compatibility. Therefore j-i<=3 for every pair i,j in S, so all indices lie in one interval of at most four consecutive positions. This supplies a genuinely nonlocal positional rigidity unavailable from the raw failed-insertion sign word.
