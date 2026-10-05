# Moving the auxiliary center can reverse arbitrary large nearest radii without same face escape

## Metadata

- ID: moving_the_auxiliary_center_can_reverse_arbitrary_large_nearest_radii_without_same_face_escape
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 102
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Cold composition

(none yet)

## Development

## A moving-center obstruction to the radius-three elevation

This addendum examines the use of [[separated_protected_determining_windows_force_a_persistent_witness_or_same_face_escape]] in [[elevation_exact_violations_reduce_terminal_topology_to_radius_at_most_three]]. The separated-window theorem fixes absolute determining positions throughout a face. Auxiliary-radius protection is measured from the position of r, which can change within its face block. These hypotheses are not interchangeable.

For an auxiliary order with r in position t, define x_j to detect a non-tight old triple beginning at t-j-2, and y_j to detect a tight old triple beginning at t+j, with a missing triple contributing zero. Thus x_1,y_1 test the immediate old triples on the left and right.

**Example family.** Fix any integer d>=4. Take disjoint lists
\[
L=(l_1,\ldots,l_\ell),\quad R=(q_1,\ldots,q_s),
\qquad \ell,s\ge d+2,
\]
and a further old vertex z. Prescribe the consecutive statuses of L to be all 1 except
\[
h(l_{\ell-d-1},l_{\ell-d},l_{\ell-d+1})=0.
\]
Prescribe the consecutive statuses of R to be all 0 except
\[
h(q_d,q_{d+1},q_{d+2})=1.
\]
Also prescribe
\[
h(l_{\ell-1},l_\ell,z)=1,\qquad h(z,q_1,q_2)=0.
\]
The specified reversal pairs are distinct, so these prescriptions extend to a boundary tournament H by assigning all remaining reversal pairs arbitrarily.

Adjoin the standard auxiliary vertex r with h(u,v,r)=1 and h(r,v,u)=0. Let F be the proper ordered-partition edge with singleton blocks for the vertices of L and R and central block {r,z}. Its two chambers are
\[
\pi=(L,r,z,R),\qquad \pi'=(L,z,r,R).
\]
Their complete violation profiles are
\[
\pi:\quad x_d=1,\ y_{d+1}=1,
\]
\[
\pi':\quad x_{d+1}=1,\ y_d=1,
\]
with all other x_j,y_j zero. The two displayed boundary prescriptions ensure cleanliness of the newly exposed radius-one triples.

Consequently every chamber of F is clean at all radii j<d, and the ordinary nearest labels are +d and -d. There is no chamber in F clean at radius d, for any d>=4. Its two nearest-label vectors have positive balance with equal weights.

In both chambers the positive word 011 at the left non-tight old triple and the positive word 001 ending at the right tight old triple occupy exactly the same absolute positions. Both occurrences persist. Swapping r,z changes their relative radii, not their occurrence indicators. The fixed-position separated-window theorem therefore gives its persistent-orientation alternative, not a same-face escape.

This family refutes a local implication from universal smaller-radius cleanliness and opposite ordinary nearest labels to a greater-radius chamber. It is not a counterexample to the grand conjecture. If the intended auxiliary theorem additionally assumes that H is a grand counterexample, that global assumption would have to do extra work: the cited fixed-position theorem does not supply the stated conclusion, and the local proof does not use such extra information.

A valid repair is to fix r as a singleton throughout the source face, or to prove a separate theorem synchronizing its positions before applying fixed-position window splicing. The example does not justify a uniform radius-three bound on non-singleton auxiliary carriers.
