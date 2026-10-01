# A fixed two-defect certificate permits arbitrary normalization in three stable regions

## Statement

Let pi=(v_1,...,v_n) have c(pi)=3 and fix two disjoint defect-line edges coming from defect centers i<j. While keeping the six local positions belonging to the two defect triples fixed, the vertices in each of the three position intervals [1,i-2], [i+2,j-2], and [j+2,n] may be permuted arbitrarily by adjacent transpositions without ever destroying either chosen defect center. Thus every fixed two-edge defect certificate has a canonical normalization in which all far-away vertices are ordered arbitrarily within these three stable regions; only the bounded neighborhoods of the two matched defects obstruct further permutation.

## Body

The defect at center i depends only on positions i-1,i,i+1, and the defect at center j only on j-1,j,j+1. By be245d868595, a swap at positions k,k+1 can affect the i-defect only for k in {i-2,i-1,i,i+1}, and similarly for j. Any adjacent swap wholly inside [1,i-2] has k<=i-3 and is therefore safe for both defects. Any swap wholly inside [i+2,j-2] has i+2<=k<=j-3 and is likewise outside both sensitive sets; any swap wholly inside [j+2,n] has k>=j+2 and is safe. Adjacent transpositions generate the full symmetric group on each interval, so arbitrary independent permutations of the three regions are realizable through certificate-preserving swaps. Every intermediate ordering still contains the same two defect-line edges, hence has contiguous-path number at least three.
