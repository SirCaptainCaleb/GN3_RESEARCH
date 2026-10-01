# The neutral endpoint-attachment move is a fully compatible omission swap

## Statement

In the neutral t=1 branch of 295ead2879dc, let z be the unique vertex split off as the new singleton. The old deletion cover F_y of H-y and the new deletion cover F_z of H-z are fully compatible on H-{y,z}: they have one identical unchanged path D, and their other paths restrict to the same displayed tight path after deleting z from F_y and y from F_z. Hence every Phi-neutral one-block endpoint-restoration move is exactly a clean omission swap along an edge of the full deletion-cover compatibility graph. The same holds for the symmetric terminal-end branch.

## Body

Use the notation of 295ead2879dc. In the terminal-attachment case with |L|=1, write L=(z). The old deletion cover is F_y=(z,B,K)|D, while the restored spanning three-cover is (z)|(y,B,K)|D, so deleting the new singleton z gives the deletion cover F_z=(y,B,K)|D. On the common domain H-{y,z}, both covers restrict to (B,K)|D with exactly the same displayed orders.

In the initial-attachment case, neutral means |A|=1; write A=(z), so the old path is (z,a,B,K) and the new deletion path after omitting z is (a,y,B,K). Deleting z from the old cover and y from the new one leaves the identical ordered path (a,B,K), again with D unchanged. Thus the two deletion covers are fully compatible. The terminal-end version is symmetric.
