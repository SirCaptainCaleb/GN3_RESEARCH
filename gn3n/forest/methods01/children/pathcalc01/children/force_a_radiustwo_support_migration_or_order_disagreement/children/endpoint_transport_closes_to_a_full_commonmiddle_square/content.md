# Neutral opposite-end endpoint transport closes to a full common-middle square

## Statement

In the no-order-disagreement branch of 7e9f89b85786, write A=(a,M,c), where M=(a_2,...,a_{r-1}), and let ell be the vertex immediately preceding M in the deletion cover of H-a while r be the vertex immediately following M in the deletion cover of H-c. Then a,ell,c,r are distinct and all four paths (a,M,c), (ell,M,c), (a,M,r), and (ell,M,r) are tight. The first two new corners are same-order Hamiltonian supports at Johnson distance one from A and the fourth is at Johnson distance two.

## Body

The original path is (a,M,c). In the deletion cover of H-a, the surviving A-block is (M,c) and has immediate predecessor ell, so the contiguous segment (ell,M,c) is tight. In the deletion cover of H-c, the surviving A-block is (a,M) and has immediate successor r, so (a,M,r) is tight. By 7e9f89b85786, if ell=r then the two deletion-cover orders disagree on their common vertices; hence in the no-disagreement branch ell and r are distinct. Both are outside A, so all four corner labels a,ell,c,r are distinct. The certified common-middle rectangle theorem commonmiddle01 applied to (a,M,c) and (ell,M,r), or directly to the two endpoint joins, gives the remaining mixed corner (ell,M,r); equivalently the four corners form a complete 2-by-2 common-middle square. Their supports are respectively M+{a,c}, M+{ell,c}, M+{a,r}, and M+{ell,r}, so the two adjacent new supports differ from A by one vertex and the diagonal support by two.