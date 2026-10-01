# Every backward comparison admits a shorter two-coverable defect shift

## Statement

Refine the normalization by first minimizing the number of backward comparisons and then minimizing the sum of their order-spans. For every backward comparison alpha=e_j->e_i, choose a shortest all-forward return path e_i=f_0->...->f_r=e_j. Some forward arc beta=f_k->f_{k+1} on this path is unused by the fixed three-cover F. Reversing alpha and beta preserves F, preserves the number of backward comparisons, and strictly decreases the total backward-span sum. Hence the shifted tournament has path-cover number at most two.

## Body

By astra010monotonecycle the all-forward return path exists. Its forward comparisons cannot all be used by F. If they were, the shared ordinary edges force them to occur consecutively in one displayed F-path; but the first and last ordinary edges are incident because alpha is a comparison between them, so the corresponding vertex sequence would repeat a vertex. Choose an unused beta. Toggle alpha and beta. Neither changed comparison is used by F, so F survives. Alpha becomes forward and beta becomes backward, while every other comparison keeps its forward/backward status. Thus the backward count is unchanged. Since beta lies strictly inside the alpha interval along the forward return path, span(beta)<span(alpha), so the total span sum decreases. A path-cover-three shifted tournament would contradict the refined normalization; therefore it is two-coverable.
