# At least one third of a minimal counterexample lies at threshold degree

## Statement

In the setting of 324fa959c567, write X=V(H)\D. Then (k-1)|X|<=2k|D|. Consequently |D|>=(k-1)|V(H)|/(3k-1). Thus at least an asymptotic one-third fraction of the vertices of any edge-minimal dense-core counterexample have degree exactly k=floor(2ell/3)+1.

## Body

For x∈X, 324fa959c567 gives d_{H-D}(x)<=2, while d_H(x)>=k+1. Hence x lies in at least k-1 edges meeting D.

Each such edge contains at least one vertex d∈D. By linearity, for a fixed pair (x,d) there is at most one hyperedge containing both. Thus these at least k-1 cross edges certify at least k-1 distinct D-X incidence pairs at x. Summing over x∈X gives at least
(k-1)|X|
distinct incidence pairs (d,x) that occur together in a hyperedge.

For d∈D, d_H(d)=k. Each of its k incident hyperedges contains at most two vertices of X, so d participates in at most 2k D-X incidence pairs. Summing over d∈D gives at most
2k|D|
such pairs.

Therefore
(k-1)|X|<=2k|D|.
Since |V(H)|=|D|+|X|, rearrangement gives
(k-1)(n-|D|)<=2k|D|,
so
(k-1)n<=(3k-1)|D|,
as claimed.