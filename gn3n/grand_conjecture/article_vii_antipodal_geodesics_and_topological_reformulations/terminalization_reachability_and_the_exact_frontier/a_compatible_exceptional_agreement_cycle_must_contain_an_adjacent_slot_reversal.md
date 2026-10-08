# A compatible exceptional agreement cycle must contain an adjacent slot reversal

## Composition

(none yet)

## Development

## A compatible exceptional agreement cycle must contain an adjacent-slot reversal

Let H have no spanning two-cover, |V(H)|>=5. Choose deletion covers whose support-agreement graph is 2-connected. Suppose additionally that the path orders agree on every agreement edge after restricting to its common domain.

Then at least one cycle edge has adjacent insertion slots, and hence supplies a positioned boundary reversal across its unique intervening common vertex.

Proof. The support graph is the negatively signed odd cycle in [[negative_spanning_support_agreement_cycles_have_an_odd_single_switch_normal_form]], with two path supports of equal order r=(n-1)/2>=2. Name the two ordered paths consistently along all cycle edges except the final edge, where the names are exchanged.

For consecutive holes a,b, compatibility represents the two paths by inserting a or b into the same common ordered support. Different supports or insertion slots separated by at least two give a spanning two-cover by simultaneous insertion, so the slots are equal or adjacent.

Assume for contradiction that all these slots are equal. Equality means replacing the vertex b by a at the same ordered position in the same named path; all other positions are unchanged. Thus one may regard the 2r ordered path positions as fixed slots and the hole as an additional position.

Traverse the cycle of holes x_1,x_2,...,x_n,x_1. Before x_j first becomes the hole, it remains in its initial slot, because equal-slot replacements move only the next hole label. The slot initially occupied by x_2 first receives x_1, each later visited slot receives the preceding hole, and the final step removes x_1 from the first visited slot and replaces it by x_n. Hence on the 2r path slots the complete traversal induces one cycle of length 2r.

But the final negative identification, together with order compatibility on the last edge, says that the two named ordered paths have exchanged as entire ordered lists. The induced permutation of fixed slots is therefore the product of r disjoint transpositions, each exchanging corresponding positions of the two paths. For r>=2 this is not one 2r-cycle. Contradiction.

Consequently some edge has adjacent slots. Write its common varying support as L,z,R, with its two extensions (L,a,z,R) and (L,z,b,R). All consecutive triples of (L,a,z,b,R) are inherited from those extensions except (a,z,b). If that triple were tight, the resulting path and the unchanged common second path would two-cover H. Therefore h(a,z,b)=0 and h(b,z,a)=1.

Thus a 2-connected agreement family does not leave an unstructured coherent loop: either some agreement edge already has order disagreement, or full compatibility forces an adjacent-slot positioned reversal. The theorem retains an actual reversing triple and the two deletion orders that locate it. Closing that reversal still requires a valid conversion; no bare four-support is being treated as terminal.
