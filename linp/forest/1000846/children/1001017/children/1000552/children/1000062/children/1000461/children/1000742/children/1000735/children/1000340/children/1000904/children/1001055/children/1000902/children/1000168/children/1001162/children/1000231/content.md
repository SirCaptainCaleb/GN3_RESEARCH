# Deficiency-one path pairs have at most one unbalanced elementary lens

## Statement

Let Q and P be linear paths ending at the same vertex v, with |Q|=q and |P|=q+1=phi(v). Suppose a collection of pairwise edge-disjoint clean elementary lenses between Q and P is chosen, with Q-side lengths a_i and P-side lengths b_i. Then for every lens, 0<=b_i-a_i<=1, and at most one lens satisfies b_i-a_i=1. Consequently all but at most one elementary lens in any disjoint lens decomposition of the Q/P overlap are balanced.

## Body

For one clean elementary lens, replacing its P-side by the Q-side preserves a path ending at v. Since P is maximum, (q+1)-b_i+a_i<=q+1, so a_i<=b_i. Conversely replacing the Q-side by the P-side gives a path ending at v of length q-a_i+b_i, which cannot exceed phi(v)=q+1; hence b_i-a_i<=1. Thus each imbalance is 0 or 1. Now take any pairwise edge-disjoint collection of clean lenses. Because the replacements occur on disjoint path segments, they can be performed simultaneously in Q. Replacing all Q-sides by their P-sides gives a linear path ending at v of length q+sum_i(b_i-a_i), again at most q+1. Therefore sum_i(b_i-a_i)<=1. Since each summand is 0 or 1, at most one is 1.