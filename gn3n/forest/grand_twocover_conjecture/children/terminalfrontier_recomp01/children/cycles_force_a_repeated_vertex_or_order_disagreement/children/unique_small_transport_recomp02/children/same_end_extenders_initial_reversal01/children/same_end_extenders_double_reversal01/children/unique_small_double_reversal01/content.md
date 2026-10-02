# The witness-free unique-small equitable residue forces synchronized double endpoint reversal

## Statement

Let H be a minimum counterexample and let K be a trapped pairwise-repartition component at minimum quadratic potential in which every three-cover has path-order multiset {r+1,r+1,r}, r>=3. Assume none of the canonical terminal-frontier witnesses excluded in unique_small_transport_recomp02 occurs. Then there are distinct vertices x,y and a two-cover T=R|S of H-{x,y} such that, after possibly reversing the global displayed orientation, either one of x,y reverses the initial edge of both R and S, or one of R,S has an initial edge whose boundary reversal is tight through both x and y. Thus the witness-free unique-small equitable residue forces a synchronized double endpoint-reversal obstruction.

## Body

By unique_small_transport_recomp02, the witness-free unique-small branch yields disjoint tight core paths A,B,C of order r and distinct exterior vertices x,y such that x and y both initial-extend each of A,B,C, after globally reversing the displayed orientations if necessary.

Because H is a minimum counterexample, the proper induced subtournament H-{x,y} has path-cover number at most two. It is not Hamiltonian: otherwise a Hamilton path on H-{x,y}, together with the two-vertex tight path (x,y), would two-cover H. Hence choose an exact two-cover T=R|S of H-{x,y}.

The witness-free hypotheses exclude relative-order disagreement with the displayed cores. Apply same_end_extenders_double_reversal01 to A,B,C,x,y and T. Its Hall obstruction gives exactly one of the following: one extender z in {x,y} cannot be prepended to either R or S, so both residual initial edges are cross-core and their boundary reversals through z are tight; or one residual component U in {R,S} cannot be prepended by either extender, so its cross-core initial edge has tight boundary reversals through both x and y.

This yields the asserted synchronized double endpoint reversal. In particular the older four-way crossing taxonomy from unique_small_transport_recomp02 is not needed as the terminal description of the witness-free unique-small branch.