# A c=3 ordering has at most eight adjacent swaps that can destroy a fixed defect matching

## Statement

Let pi be an ordering with c(pi)=3, and fix a size-two matching in its defect line with edges corresponding to defect centers i and j. If pi' is obtained by swapping positions k,k+1 and k is not in {i-2,i-1,i,i+1,j-2,j-1,j,j+1} (within valid swap positions), then both matched defect edges survive unchanged in L_{pi'}. Hence nu(L_{pi'})>=2 and c(pi')>=3. Thus, relative to any fixed two-edge defect certificate of a c=3 ordering, at most eight adjacent transpositions can possibly destroy that certificate in one step.

## Body

By 631ea39d7eb0, the swap at k can change only defect centers in {k-1,k,k+1,k+2}. The matched defect at center i can therefore change only when i belongs to this set, equivalently k belongs to {i-2,i-1,i,i+1}; likewise for j. If k lies outside the union of these two four-element sets, neither matched defect center changes, so the same two disjoint defect-line edges remain present after the swap. Therefore the new defect-line matching number is still at least two. This reduces the first adjacent-swap neighborhood of a minimal c=3 ordering to O(1) genuinely critical transpositions, independent of ambient order.