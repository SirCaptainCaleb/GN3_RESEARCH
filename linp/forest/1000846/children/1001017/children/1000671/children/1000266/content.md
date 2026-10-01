# Refuted: terminal-pair cycle rank is controlled by special edges

## Statement

Refuted. It is not true that beta(T)<=s for the terminal-pair graph T of nonspecial edges and the number s of special hyperedges. The family c3e95f4ce77d has s=0 while its terminal-pair graph is t disjoint copies of K_{3,3}, so beta(T)=4t.

## Body

The conjecture is refuted by c3e95f4ce77d. In that family every hyperedge is ascending and hence nonspecial, so the number of special edges is s=0. The terminal-pair graph is a disjoint union of t copies of K_{3,3}; each component has cycle rank 9-6+1=4, hence beta(T)=4t. Thus terminal cycles do not require special edges. The useful surviving lesson is that cycle rank must be controlled by terminal support rather than by special-edge count. The sharp replacement suggested by the same family is beta(T_↑)<=|V(T_↑)|/2+c(T_↑), equivalent to the maximum-average-degree-three conjecture 933f2e734c5d.
