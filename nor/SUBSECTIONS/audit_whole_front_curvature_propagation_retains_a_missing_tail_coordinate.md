# Audit whole-front curvature propagation retains a missing tail coordinate

## Metadata

- ID: audit_whole_front_curvature_propagation_retains_a_missing_tail_coordinate
- Parent Section: directed_nor_union_closed_bridge
- Position: 92
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

Audit: the claimed propagation of a pure size-three front circuit along an entire monochromatic tail dropped the original tail coordinate f1. The edge-flip witness was only an order of V minus {f1}, so counterexamplehood does not forbid it. Only the original front circuit and one-step singleton propagation are proved. If an edge flip occurs, the valid deletion witness has word tau^3 sigma^(m-3); appending the omitted f1 closes unless a specific rear wrap color is forced. All full-tube conclusions depending on pair-cycle persistence are conditional.

## Development

Audit of pure_orientation_three_circuits_propagate_unchanged_along_the_whole_monochromatic_tail and its dependent tube statements. Step 2 constructs (x,z,y,f2,f3,...,fm), which omits f1. It is therefore a NOR order on V minus {f1}, not a spanning order, even when {x,y,z} is the entire set omitted by P. Counterexamplehood does not exclude this order. Consequently the no-edge-flip conclusion, the shifted-circuit induction, and the full-tube conclusions depending on that induction have not been proved.

Step 1 at the original front survives: (x,y,f1,z,f2,...,fm) is spanning, and its displayed window calculation forces alpha(z,f2,f3)=tau for all z in the original circuit when f3 exists. This gives one-step singleton propagation. Iteration would require a new full-support argument accounting for the consumed coordinates.

A valid replacement for the dropped-vertex witness is to retain it as a deletion order D=(x,z,y,f2,...,fm) with word tau^3 sigma^{m-3}. If m=3, D is monochromatic and prepending f1 already closes NOR. For m>=4, appending f1 gives a spanning one-change order unless alpha(f_{m-1},fm,f1)=tau. Thus a flipped edge forces that rear wrap color in a counterexample. Prepending f1 yields the word sigma,tau^3,sigma^{m-3}, because alpha(f1,x,z)=sigma; this has two changes and does not close. These statements preserve every coordinate and identify the additional endpoint condition needed to repair the proof.

Related scope audit of a_fully_curved_cross_tetrahedron_closes_a_maximal_monochromatic_tail: its local extension P union {a,b} is correct. However the stated counterexample consequence for arbitrary omitted set X does not follow from that one-change extension unless X={a,b}. A separate direct argument does exclude full curvature for an inclusion-maximal monochromatic path: maximality forces alpha(a,f1,f2)=alpha(b,f1,f2)=tau, whereas full curvature makes these two values opposite. This direct argument repairs the consequence without using a nonspanning NOR witness.

The local curvature identities remain usable. The global persistence claims should be treated as conditional until the missing-coordinate repair is supplied.
