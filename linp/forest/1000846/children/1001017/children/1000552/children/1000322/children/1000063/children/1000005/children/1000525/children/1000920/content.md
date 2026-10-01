# Opposite-end degree bound proves the maximum-rank-nonspecial branch of 3δ≤2L+2

## Statement

Assume the opposite-end degree conjecture. If H has minimum degree δ, global maximum path length L, and contains a nonspecial edge e with φ(e)=L, then 3δ<=2L+2.

## Body

Choose a globally longest L-edge path P ending in the maximum-rank nonspecial edge e. By the opposite-end conjecture, one of the two physical endpoints a of the first edge opposite e has d_H(a)<=floor(2(L+1)/3). Since δ<=d_H(a), we get δ<=floor(2(L+1)/3), hence 3δ<=2L+2. This handles only the branch in which a nonspecial edge has global maximum rank. The full conjecture 76ef6efb21e7 still requires a dense-minimum-degree propagation theorem or a corresponding opposite-end statement starting from a lower-rank nonspecial edge; unrestricted propagation is false in low-degree systems by 61e82a9b70f5.
