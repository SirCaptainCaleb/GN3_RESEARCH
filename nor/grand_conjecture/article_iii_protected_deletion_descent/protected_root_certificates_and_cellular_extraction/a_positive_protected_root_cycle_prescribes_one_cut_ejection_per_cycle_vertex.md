# A positive protected root cycle prescribes one cut ejection per cycle vertex

## Composition

(none yet)

## Development

## A positive protected-root cycle prescribes one cut ejection per cycle vertex

Let
[
ho_i=e_{x_{i+1}}-e_{x_i},
qquad iinmathbb Z/kmathbb Z,
]
be a directed physical root cycle, so
[
ho_0+cdots+ho_{k-1}=0.
]

Assume each (ho_i) is a canonical protected root carried by a normalized deletion state with physical protected cut (L_i), where (L_i) is the set of coordinates on the first-phase side of the cut.

Canonical protected roots always point inward across their own cut:
[
e_a-e_c
quadLongrightarrowquad
ain L,; c
otin L.
]
Therefore for the cycle root (ho_i=e_{x_{i+1}}-e_{x_i}),
[
x_{i+1}in L_i,
qquad
x_i
otin L_i.
	ag{1}
]

But the preceding root is
[
ho_{i-1}=e_{x_i}-e_{x_{i-1}},
]
so its cut satisfies
[
x_iin L_{i-1}.
	ag{2}
]

Combining (1)-(2),
[
oxed{x_iin L_{i-1}setminus L_i}
]
for every cycle vertex (x_i).

### Consequences

1. Consecutive root states on a sign-compatible directed cycle can never have the same physical cut.

2. Any path in the chamber/cut carrier joining the state carrying (ho_{i-1}) to the state carrying (ho_i) must cross at least one Johnson-graph edge at which the physical coordinate (x_i) leaves the first-phase set.

3. Hence a length-k positive root circuit forces at least k prescribed cut-ejection events, one for each physical cycle coordinate. This is stronger than the generic theorem that a Radon carrier contains some cut-changing wall.

4. For a two-cycle
[
e_x-e_y,quad e_y-e_x,
]
the two states force x and y to exchange cut membership in opposite directions, matching the antipodal protected-pair geometry.

5. For a directed A2 triangle, each of the three residual coordinates is forced to leave the protected cut between the two root states incident with it. Thus any compatible realization of the triangle circulation necessarily traverses all three physical cut changes; it cannot remain inside a same-cut A2 recurrence, consistent with the common-cut coorientation theorem.

### Extraction target

Let paths between consecutive root states be chosen inside a minimal carrier. Since (x_i) must leave along each path, choose the first cut-changing wall that ejects (x_i). The remaining desired lemma is:

> in a support-minimal protected-root carrier, the coordinate entering at this first ejection can be chosen to be (x_{i+1}), or else the intervening wall yields a smaller sign-compatible root circuit / threshold-band improvement.

Proving this would convert an abstract positive Radon cycle into a sequence of actual protected exchanges following the same physical coordinate cycle.
