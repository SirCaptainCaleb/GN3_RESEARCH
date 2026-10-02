# Overlap-maximal gap-one path pairs have no balanced internal lens and at most one internal lens total

## Statement

Let Q be a q-edge path ending at v and let phi(v)=q+1. Among all maximum (q+1)-edge paths P ending at v, choose P to maximize the number of Q-edges it contains. Then Q and P admit no balanced clean internal elementary lens. Consequently, by the deficiency-one lens lemma 32ea928e6ffd, any pairwise edge-disjoint family of clean internal elementary Q/P lenses has size at most one; if such a lens exists, its P-side is exactly one edge longer than its Q-side.

## Body

Suppose a balanced clean internal elementary lens exists, with Q-side A and P-side B of equal edge length. Because the lens is elementary and clean, the interior of B is disjoint from Q, so B contains no Q-edge that would be lost under replacement, while every edge of A is a Q-edge. Replace B inside P by A. The clean-lens hypothesis guarantees a linear path still ending at v, and equal side lengths preserve the total length q+1. The resulting maximum endpoint path contains strictly more Q-edges than P, contradicting the defining overlap maximality. Therefore no balanced internal lens exists. By 32ea928e6ffd, every clean internal lens has imbalance b-a in {0,1}, and among any disjoint family at most one has imbalance one. Since imbalance zero has just been excluded, any pairwise edge-disjoint family contains at most one clean internal elementary lens, and if such a lens occurs its P-side exceeds its Q-side by exactly one edge.