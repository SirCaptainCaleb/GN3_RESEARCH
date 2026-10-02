# The witness-free unique-small equitable residue forces four synchronized endpoint reversals

## Statement

Let H be a minimum counterexample and let K be a trapped pairwise-repartition component at minimum quadratic potential in which every three-cover has path-order multiset {r+1,r+1,r}, r>=3. Assume none of the canonical terminal-frontier witnesses excluded in unique_small_transport_recomp02 occurs. Then there are distinct vertices x,y and an exact two-cover T=R|S of H-{x,y} such that, after possibly reversing the global displayed orientation, either one extender z in {x,y} reverses both endpoint edges of both R and S, or one residual component U in {R,S} has both endpoint edges reversed through both x and y. In all four instances the reversed endpoint edge is cross-core relative to the three order-r displayed cores.

## Body

The witness-free unique-small theorem unique_small_transport_recomp02 provides three disjoint order-r core paths A,B,C and distinct exterior vertices x,y which both extend the same end of every core. Reverse the global displayed orientation if necessary so that both are initial extenders.

By minimum-counterexample minimality, H-{x,y} has path-cover number at most two. It cannot be Hamiltonian, since a Hamilton path on H-{x,y} together with the two-vertex path (x,y) would two-cover H. Hence choose an exact two-cover T=R|S. The witness-free hypothesis excludes relative-order disagreement between T and the displayed cores.

Apply same_end_extenders_four_endpoint_reversal01. Its first Hall alternative gives one extender z which is unattached at either end of either residual component, and hence four reverse cross-core endpoint triples through z. Its second alternative gives one residual component U to which neither x nor y attaches at either end, and hence four reverse cross-core endpoint triples, through both extenders at both ends of U. This proves the stated normal form.