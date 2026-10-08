# Deletion-critical complement forks only require two-cover distance at least two — preserved pre-item development

## Composition

(none yet)

## Development

## Elevation: complement deletion-criticality only needs (kappa_2(H)ge2)

Let (H) be any boundary tournament with no spanning two-cover and assume
[
kappa_2(H)ge2.
]
Let (Ssubsetneq V(H)) be a Hamiltonian support such that
[
H-S=Pmid Q
]
is a two-cover.

Put
[
G=H-S.
]

Then for every
[
vin V(G),
]
the graph
[
G-v
]
is non-Hamiltonian.

Indeed, if (G-v) were Hamiltonian, then a Hamilton path on (S) together with one on (G-v) would give a spanning two-cover of
[
H-v,
]
contradicting
[
kappa_2(H)ge2.
]

Thus
[
oxed{G-v	ext{ is non-Hamiltonian for every }vin V(G).}
]

Consequently every second-layer junction-fork argument in
[[deletion_critical_complements_force_second_layer_junction_forks]]
remains valid under the weaker hypothesis
[
kappa_2(H)ge2,
]
not merely (kappa_2(H)=2).

If (S) is maximal among Hamiltonian supports with two-coverable complement, the exposed-endpoint nonaugmentability relations are independent of deletion distance. Therefore the seam four-support theorem
[[every_deletion_critical_complement_corner_forces_a_hamiltonian_four_support]]
also extends unchanged to every saturated state with
[
kappa_2(H)ge2.
]

### Recursive consequence

Suppose a four- or eight-vertex seam descent produces a smaller induced no-two-cover graph (H') while a Hamiltonian support (S) survives and
[
H'-S
]
still has a displayed two-cover.

Then exactly one of the following happens:

1. (kappa_2(H')=1), entering the deletion-distance-one machinery; or
2. (kappa_2(H')ge2), in which case seed-preserving maximalization of (S) in (H') again yields a saturated deletion-critical complement and all second-layer seam forks are available anew.

Thus the seam mechanism can be restarted after descent without requiring the descended graph to have deletion distance exactly two.

No minimum-counterexample induction is used; this is a direct consequence of the definition of two-cover deletion distance.
