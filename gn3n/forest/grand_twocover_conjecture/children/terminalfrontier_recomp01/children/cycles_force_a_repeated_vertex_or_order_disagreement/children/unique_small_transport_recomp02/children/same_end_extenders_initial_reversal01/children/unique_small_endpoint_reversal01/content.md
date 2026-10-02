# The witness-free unique-small quadratic residue enters endpoint reversal

## Statement

Let H be a minimum counterexample and let K be a trapped pairwise-repartition component at minimum quadratic potential in which every three-cover has path-order multiset {r+1,r+1,r}, r>=3. Assume none of the canonical terminal-frontier witnesses listed in unique_small_transport_recomp02 occurs. Then H contains a tight path R=(u,v,...) and a vertex z outside R such that (v,u,z) is tight. Thus the unique-small neutral residue contains a literal initial-edge reversal and enters the certified endpoint-reversal machinery directly.

## Body

By unique_small_transport_recomp02, the witness-free hypotheses yield disjoint tight paths A,B,C of order r and distinct vertices x,y outside them such that x and y both extend the same endpoint of all three cores. Reverse the global notation if needed and assume they both initial-extend A,B,C.

Because H is a minimum counterexample, the proper induced subtournament H-{x,y} has path-cover number at most two. If it were Hamiltonian, a Hamilton path on H-{x,y} together with the two-vertex path (x,y) would be a spanning two-cover of H, impossible. Hence choose a two-cover T of H-{x,y}; it has two nonempty components.

Apply same_end_extenders_initial_reversal01 to A,B,C,x,y and T. That theorem gives either order disagreement between T and one displayed core, or a component R=(u,v,...) of T whose first two vertices lie in different cores and a label z in {x,y} for which (v,u,z) is tight.

The first alternative is excluded by the witness-free hypothesis of unique_small_transport_recomp02. Therefore the second alternative holds. Since R is a tight path and z is outside R, the tight triple (v,u,z) reverses the displayed initial edge (u,v) of R in the literal sense used by the endpoint-reversal classification. No crossing-count case analysis is required.

Consequently the former unique-small four-way comparison-cover residue can be replaced, for theorem-facing purposes, by direct entry into endpoint_reversal_obstruction_recomp01 and its descendants. This does not by itself close the grand theorem: the endpoint-reversal chain can still return bounded order disagreement or other canonical local disturbances. It does, however, eliminate crossing multiplicity, inherited-core separation, and leave-and-return as necessary terminal descriptions of this particular neutral branch.