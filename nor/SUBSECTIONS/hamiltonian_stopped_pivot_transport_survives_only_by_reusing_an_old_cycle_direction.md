# Hamiltonian stopped-pivot transport survives only by reusing an old cycle direction

## Metadata

- ID: hamiltonian_stopped_pivot_transport_survives_only_by_reusing_an_old_cycle_direction
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 120
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Hamiltonian stopped-pivot transport can survive only by reusing an old cycle direction

Assume the endpoint CORNER-LIFT theorem of Subsection 93 and choose a physical endpoint-root cycle of minimum length among all actual protected endpoint-root cycles in the minimum-counterexample class.

Suppose its physical support is Hamiltonian: it contains every ambient coordinate.

By Subsections 114 and 117, after corner-lift normalization every partner-change junction is a pinned endpoint triangle, and a completed pivot triangle is impossible because it would shortcut two consecutive cycle edges.

By Subsection 119, every remaining stopped pivot either:
1. emits an immediate farther protected root;
2. enters audited one-sided flat transport, which terminates in a one-change state or at a fully-curved boundary emitting an actual protected physical root.

The immediate farther-root branch is already excluded in a minimum Hamiltonian cycle unless that root is an existing cycle edge: there is no exterior coordinate.

The same statement holds for the terminal root of the flat-transport branch.

### Directed-chord shortening lemma

Let the minimum physical cycle be
x_0 -> x_1 -> ... -> x_{k-1} -> x_0.

Let an actual protected root
e_u-e_v
be emitted by the stopped-pivot/transport process, with u=x_i and v=x_j.

Because the cycle is Hamiltonian, u and v are cycle vertices.

If v is not x_{i+1}, then the emitted edge u->v together with the directed segment of the old cycle from v back to u forms a directed protected-root cycle strictly shorter than k.

Indeed, if the old directed distance from v to u is d in {1,...,k-2}, the new cycle has d+1<=k-1 edges.

This includes the case v=x_{i-1}, which gives a two-edge cycle with the old edge x_{i-1}->x_i.

Therefore minimum length forces
v=x_{i+1}
for every emitted protected root whose source is x_i.

More generally, every emitted root must coincide, with orientation, with one of the existing cycle edges.

### Consequence

In a minimum Hamiltonian endpoint cycle, a stopped-pivot branch cannot survive by producing a genuinely new physical root direction.

If flat transport does not solve the instance, its terminal fully-curved root must REUSE an already present cycle direction
e_{x_i}-e_{x_{i+1}}.

But one-sided flat transport carries a strict central-cut flag (Subsections 82 and 104): its terminal root is realized at a graded central cut reached after strict cut motion from the stopped-pivot state.

Hence any unresolved Hamiltonian stopped-pivot branch produces the same physical protected root direction at a second provenance state / graded cut.

So, conditional on corner lifting, the Hamiltonian endpoint frontier has reduced to pure provenance multiplicity:

- either a pivot triangle shortens the physical cycle;
- or a farther/terminal root shortens the physical cycle;
- or the process realizes an existing physical cycle edge again at a different compatible cut/state.

The remaining theorem is no longer root production. It is an extraction theorem for two realizations of the same oriented physical root at distinct compatible provenance states. This is precisely the setting in which realized repair squares, braid cells, or a same-root cut-comparison potential may be able to force a legal witness improvement.

## Frontier

- Development version when composed: None
- Development version now: 1
