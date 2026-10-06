# Hamiltonian prefix chains force every closed deletion subfamily to be the whole monotone interface

## Metadata

- ID: hamiltonian_prefix_chains_force_every_closed_deletion_subfamily_to_be_the_whole_monotone_interface
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 272
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

Let H be any boundary 3-tournament with no spanning two-path cover. Let D be the family of ALL actual one-hole deletion-cover edges in the Boolean cube. An edge A -> A-x belongs to D precisely when A-x and V-A are nonempty Hamiltonian supports. In particular its tail has Hamiltonian complement and its head is Hamiltonian. No minimum-order hypothesis is used in this theorem.

THE PREFIX-CHAIN OBSERVATION.
Call a cube vertex left if its subset A is Hamiltonian, and right if V-A is Hamiltonian. Extend this terminology only at the two extremes: empty is left and V is right. Since H has no two-cover, no vertex is both left and right.
Every left vertex is connected to empty by a cube path consisting of Hamiltonian prefixes of one Hamilton order of A. Every right vertex is connected to V by the complementary prefix path of one Hamilton order of V-A.
These paths avoid every edge of D. Indeed each D-edge joins a right tail to a left head; two left endpoints or two right endpoints cannot form such an edge. The last step to an extreme cannot be a D-edge because deletion covers here have two nonempty supports.

THEOREM.
If C is a nonempty cubical mod-two 1-cocycle contained in D, then C=D. Moreover D is the cut of a monotone self-dual Boolean function f, normalized by f(empty)=0 and f(V)=1. Antipodal invariance of C need not be assumed.

Proof.
Contractibility of the cube gives C=delta f. An edge outside C has equal f-values at its two endpoints.
The prefix paths therefore imply f(A)=f(empty) at every left vertex and f(A)=f(V) at every right vertex.
Choose an edge in C. Its right tail and left head have different values, so f(empty) and f(V) differ. Normalize them to 0 and 1.
Now every edge in D has a right tail of value 1 and a left head of value 0, hence belongs to delta f=C. This proves C=D.
On a downward cube edge A -> A-x, either it is in D and f decreases from 1 to 0, or it is outside D and f is unchanged. Thus f is monotone under inclusion.
The full actual family D is antipodally invariant. Consequently f(A)+f(V-A) is constant over the cube. Its value at empty is 1, proving self-duality. QED.

This repairs the previously invalid global-monotonicity inference (261/263): purity ALONE remains insufficient. The additional hypothesis that every selected edge is an actual Hamiltonian deletion cover supplies the prefix paths which synchronize all components.

THE DOWNWARD CLOSURE IS EXACT.
Let K={A: A is contained in some Hamiltonian support}, allowing the empty subset. Then K={A:f(A)=0}.
One inclusion follows from f=0 on Hamiltonian supports and monotonicity.
Conversely, extend any f=0 set A to an inclusion-maximal f=0 set M. Since f(V)=1, choose x outside M. The cut edge M+x -> M lies in D and therefore certifies M Hamiltonian. Thus A belongs to K.
Self-duality gives K=K*, where K*={A:V-A notin K} is the Alexander dual.

Consequently E(H) is exactly the deleted join K *_Delta K (the Bier complex of K).
The forward containment follows from the definition of downward closure.
For the reverse containment, take disjoint A,B in K. Enlarge A to a maximal member M of K inside V-B. Self-duality rules out M=V-B, so choose x outside M union B. Maximality gives M+x notin K, and self-duality gives N=V-(M+x) in K with B subseteq N. The corresponding cut edge is in D, so M and N are actual disjoint Hamiltonian supports. They witness A+ union B- in E(H).

COMPLEMENT CONNECTIVITY.
In the cube graph with D removed, all left vertices belong to one component and all right vertices to one component. Every removed edge joins these two classes. Any additional component containing neither class would have no incident removed edge and hence no incident cube edge leaving it, impossible because the cube graph is connected.
Thus the remaining cube graph has either one component or exactly two. If it has two, D is their full edge cut and is a cocycle. Conversely a nonempty cocycle D separates them.
This gives a concrete alternative: either the cube graph with deletion-cover edges removed is connected, or the entire interface is already a globally monotone cut.

TOP COLLAPSES AND MINIMUM COUNTEREXAMPLES.
Any nonempty collection of top deletion facets with no uniquely incident codimension-one face gives a nonempty cubical cocycle contained in D. Therefore it must be the whole family D. Hence no proper nonempty closed top subfamily exists, even without minimality.
For a minimum-order counterexample, apply 269 to this automatically antipodal whole family. If any closed collection exists, n=2r+1, every r-set is Hamiltonian, every (r+1)-set is non-Hamiltonian, and D is the complete middle layer. Otherwise every nonempty surviving top collection has a free codimension-one face and all top facets can be removed.

Limits. These statements still do not construct a spanning two-cover. Connectedness of the cube with D removed is the unresolved all-collapsed branch, while the monotone branch still needs a Hamiltonian augmentation contradicting its odd middle layer. The prefix argument closes the global coorientation gap and identifies the full obstruction, without asserting that either remaining branch is impossible.
