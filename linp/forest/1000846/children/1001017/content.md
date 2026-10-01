# General-length attack: special-edge density and incidence rank

## Statement

For the 3-uniform general-length upper bound, pursue two complementary routes. Primary snake route: prove s>=epsilon*m-O(n) for some absolute epsilon>0, where s is the number of special edges; this already improves the leading coefficient below 1. Stronger b=O(n) is only the saturation target of that scheme and yields coefficient 2/3. Parallel graph/rank route: exploit the induced-P_ell-free intersection graph, its exact 3-fold clique cover, and rank(3I+A) to seek bounds capable of passing the 2/3 snake ceiling.

## Body

The proved identity 2m+s <= (2ell-3)n shows that a fixed positive special-edge density s>=epsilon*m-Cn implies m<=((2ell-3+C)/(2+epsilon))n, whose leading coefficient 2/(2+epsilon) is strictly below 1. Thus b=O(n), equivalently s=m-O(n), is much stronger than necessary; it asymptotically saturates the unchanged unweighted snake count at coefficient 2/3, and that count cannot go below 2/3 because s<=m. Pathmaker gives an exact graph translation: P_ell^(3)-free means the intersection graph is induced-P_ell-free, with an indexed clique family in which every graph vertex lies in exactly three cliques and every graph edge lies in exactly one. Nonspecial hyperedges are exactly graph vertices whose longest induced paths all enter through one clique label. This is the primary structural formulation for the special-density route. Independently, if N is the incidence matrix and A the intersection-graph adjacency matrix, then N^T N=3I+A and rank N=m-mult(-3)<=n. A lower bound on rank(3I+A) for these realizable induced-P_ell-free graphs gives an upper Turan bound; a rank scale about 3m/ell would reach the conjectural ell*n/3 scale and is not subject to the 2/3 snake ceiling.
