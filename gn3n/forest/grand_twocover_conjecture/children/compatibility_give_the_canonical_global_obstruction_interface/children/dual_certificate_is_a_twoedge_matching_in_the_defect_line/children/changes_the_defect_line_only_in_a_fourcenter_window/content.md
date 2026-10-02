# An adjacent transposition changes the defect line only in a four-center window

## Statement

Let pi=(v_1,...,v_n) and let pi' be obtained by swapping the adjacent vertices in positions k,k+1. Then D(pi) and D(pi') can differ only at defect centers i in {k-1,k,k+1,k+2} (within the valid center range). Equivalently, their defect-line edge sets differ only among the four consecutive possible edges {i-1,i} for those centers, on at most five consecutive cut-position vertices. Consequently |nu(L_pi)-nu(L_pi')|<=2, and likewise |c(pi)-c(pi')|<=2.

## Body

A defect center i depends only on the ordered triple occupying positions i-1,i,i+1. Swapping positions k and k+1 leaves this triple unchanged unless its three-position window meets {k,k+1}, which occurs only for i in {k-1,k,k+1,k+2}. Thus the symmetric difference of the two defect-line edge sets is supported on at most four consecutive path edges, whose maximum matching number is at most two. For arbitrary graphs G,H, deleting the symmetric-difference edges from a maximum matching of G loses at most nu(E(G) triangle E(H)) matched edges, so |nu(G)-nu(H)| is at most the matching number of the symmetric-difference graph. Here that is at most two. The identity c=1+nu from ca8dc4ee0bde gives the same bound for contiguous-path number.