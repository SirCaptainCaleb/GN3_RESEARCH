# Overlap-maximal same-endpoint deficiency-d path pairs have at most d internal lenses

## Statement

Let Q be an a-edge path ending at v, let phi(v)=a+d, and let P be a maximum (a+d)-edge path ending at v. Choose P, among maximum v-paths, to maximize the number of Q-edges it contains. For any family of clean internal elementary Q/P lenses that is simultaneously switchable (in particular, their replacement interiors are pairwise vertex-disjoint), with Q-side lengths A_i and P-side lengths B_i, one has A_i<=B_i and sum_i(B_i-A_i)<=d. Moreover no balanced lens B_i=A_i can occur. Hence such a family contains at most d internal elementary lenses.

## Body

For each clean internal lens, replacing its P-side by its Q-side preserves a path ending at v. Since P is maximum, (a+d)-B_i+A_i<=a+d, so A_i<=B_i. For a simultaneously switchable family, perform all Q-to-P-side replacements inside Q at once. The resulting path still ends at v and has length a+sum_i(B_i-A_i), which is at most phi(v)=a+d. Hence sum_i(B_i-A_i)<=d. If some lens were balanced, replacing its P-side by the equal-length Q-side would preserve length a+d and endpoint v while strictly increasing the number of Q-edges in P, contradicting overlap maximality. Therefore every surviving lens in a simultaneously switchable family has integer imbalance at least one, so there are at most d of them.
