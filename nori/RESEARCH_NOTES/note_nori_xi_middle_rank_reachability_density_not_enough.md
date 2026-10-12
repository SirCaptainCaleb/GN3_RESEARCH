# Five-cube example: no root exceeds EKR middle-level density despite monochromatic geodesics

- Stable ID: note_nori_xi_middle_rank_reachability_density_not_enough
- Author: unspecified; session provenance retained
- Primary home: section:nori_matroid_generalizations_conjectures
- Labels: 
- Lifecycle: active
- Epistemic status: computational
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r6430_3
- Updated session: session_nori_r6430_3
- Disposition: none
- Successor: none

## Related references

- None

## Research note

An explicit antipodally odd edge coloring of Q5 shows that the sufficient reachability criterion max_x |R_x intersect binom([5],2)| > 4 cannot hold for every coloring. Enumerate canonical antipodal edge orbits as follows: for cube vertices x=0,...,31 and directions i=0,...,4 with bit i of x equal zero, take the sorted unoriented edge endpoints (x,x XOR 2^i), compute the sorted endpoints of its antipodal edge, choose the lexicographically smaller pair as representative, and append unseen representatives in traversal order. There are 40 orbits. Assign their representative colors from low-to-high bit positions of mask 0xb23de7cb0b, with antipodal mates complemented. Direct Boolean-lattice reachability dynamic programming over all 32 roots gives a histogram for the number of reachable size-two coordinate sets: {1:2, 2:6, 3:10, 4:14}; hence every root has at most four reachable middle sets. Nevertheless the path from root zero with directions (2,4,0,1,3) is monochromatic color zero, so NORI1 holds in this example. The example blocks the overly strong claim that every deck-odd coloring must force a root whose size-two color-zero reachability exceeds the odd EKR threshold. The cross-intersection/EKR bound remains a valid necessary condition on hypothetical counterexample colorings; the failure of the naive converse shows that reachability density alone is insufficient. Computationally enumerated certificate, not a proof of any open general conjecture.
