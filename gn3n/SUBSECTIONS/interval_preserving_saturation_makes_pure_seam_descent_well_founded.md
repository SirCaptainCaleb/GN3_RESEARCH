# Interval-preserving saturation makes pure seam descent well-founded

## Metadata

- ID: interval_preserving_saturation_makes_pure_seam_descent_well_founded
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 183
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Interval-preserving saturation makes the pure seam branch well-founded

Let (H) be a no-two-cover boundary tournament and suppose
[
Smid Pmid Q
]
is a spanning three-cover, with (S) Hamiltonian and
[
P=(p_1,ldots,p_m),qquad Q=(q_1,ldots,q_t).
]

Fix these displayed rail orders.

Call a Hamiltonian support (Tsupseteq S) **interval-admissible** if
[
H-T=P[I]mid Q[J]
]
for two contiguous subintervals (P[I]subseteq P), (Q[J]subseteq Q), with empty intervals omitted.

Choose (T) of maximum cardinality among interval-admissible supports.

### Endpoint saturation needs only interval maximality

Write
[
H-T=P'mid Q'
]
for the surviving intervals.

For every nonempty subset (E) of the exposed endpoints of (P'|Q'),
[
H[Tcup E]
]
is non-Hamiltonian.

Indeed, deleting exposed endpoints from contiguous intervals leaves at most two contiguous intervals. Hence if (Tcup E) were Hamiltonian, it would be a strictly larger interval-admissible support, contradicting maximality.

Thus for any Hamilton order
[
T=(t_1,ldots,t_k)
]
every exposed complementary endpoint (z) satisfies
[
h(t_2,t_1,z)=1,
qquad
h(z,t_k,t_{k-1})=1.
]

So the endpoint-saturation input used by the seam four-support theorem does not require unrestricted global maximalization.

### If deletion distance is at least two, the complement is deletion-critical

If additionally
[
kappa_2(H)ge2,
]
then by
[[deletion_critical_complement_forks_only_require_two_cover_distance_at_least_two]]
every one-vertex deletion of
[
G=H-T
]
is non-Hamiltonian. Hence all second-layer junction forks are available whenever both surviving rail intervals have order at least three.

Therefore every saturated oriented seam has the same dichotomy as
[[every_deletion_critical_complement_corner_forces_a_hamiltonian_four_support]]:
a transversal Hamiltonian four-support, or the explicit pure cross-seam rail four-support.

### Iteration after pure descent

Suppose both oriented seams are pure and both seam four-supports take the descent branch. When the surviving rails have order at least five, the two opposite seam supports are disjoint and
[[opposite_pure_seams_give_two_step_reseeding_or_eight_vertex_descent]]
removes the first two and last two vertices of each rail.

The original support (T) survives in the twice-descended graph, and its complement is exactly the two shorter contiguous rail intervals.

If the descended graph has
[
kappa_2=1,
]
the process enters the deletion-distance-one machinery.

If instead
[
kappa_2ge2,
]
perform interval-preserving saturation again, starting from the surviving (T). Any enlargement only removes further exposed rail vertices. Thus the surviving rail intervals can never grow or be rearranged.

The seam theorem then applies again.

Hence every full pure-descent round decreases each rail order by at least four.

### Well-foundedness

Starting from rail orders (m,t), there are at most
[
leftlfloorrac{min(m,t)-3}{4}ightfloor
]
full opposite-seam pure-descent rounds before one rail has order at most six.

At or before that point, one of the following must occur:

1. a seam four-support has two-coverable complement, giving bounded-seed re-entry;
2. a transversal seam support/disturbance occurs;
3. the descended graph has (kappa_2=1);
4. a rail has order at most six, and the one-/two-step low-distance bounds apply;
5. a bounded equality packet or other finite seam interface occurs.

Therefore:

> **Well-founded pure-seam theorem.** There is no genuinely unbounded residue consisting solely of repeated pure cross-seam descents. Under interval-preserving saturation, that branch has a strictly decreasing rail-length potential and must reach a reseeding, disturbance, deletion-distance-one, or bounded-interface state after finitely many rounds.

This is not itself a proof that the reseeding/disturbance outputs close. It eliminates indefinite pure-descent propagation as an independent frontier.

No minimum-counterexample induction, cyclic rotation, path reversal, or finite computation is used.
