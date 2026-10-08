# Audit: the five-step weave is conditional on pair-cycle propagation

## Composition

(none yet)

## Development


## Audit: the five-step weave is conditional on pair-cycle propagation

The subsection titled "The pure-orientation size-three curvature tube closes by a five-step weave" used the order

(a,f_1,f_2,b,c,f_3,f_4,...,f_m)

and asserted that its first statuses are all tau.

The identities

alpha(a,f_1,f_2)=tau,
alpha(f_1,f_2,b)=tau

are valid from the original front circuit.

However the next two identities

alpha(f_2,b,c)=tau,
alpha(b,c,f_3)=tau

require the circuit edge b->c to persist from pivot f_1 to pivots f_2 and f_3.

The global pair-cycle propagation theorem was audited in Subsection 92: its edge-flip witness omitted f_1, so counterexamplehood did not forbid the flip. Consequently persistence at f_2,f_3 is not currently proved.

Therefore the five-step weave is a correct conditional construction:

if one circuit edge, say b->c, persists at both f_2 and f_3, then the displayed spanning order has word tau* sigma* and closes NOR.

It is not an unconditional closure of the size-three branch.

### Correct dichotomy

For a whole-front size-three circuit, either:

1. some circuit edge persists through the first two shifted pivots, in which case the five-step weave closes; or
2. every choice of circuit edge suitable for the weave flips at f_2 or f_3.

Any early flip must then be handled using the full-support endpoint condition from the propagation audit: the deletion witness produced by the flip becomes spanning after restoring f_1, and counterexamplehood forces a specific rear wrap color.

Thus the repaired closure target is to combine the three possible early edge flips with that common rear wrap constraint.

This audit supersedes the unconditional conclusion of the five-step-weave subsection while retaining the weave as a valid branch-closing lemma.
