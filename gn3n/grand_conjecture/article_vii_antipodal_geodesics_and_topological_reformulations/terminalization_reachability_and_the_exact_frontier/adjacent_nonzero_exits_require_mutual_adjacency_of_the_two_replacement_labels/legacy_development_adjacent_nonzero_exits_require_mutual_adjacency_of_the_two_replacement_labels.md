# Adjacent nonzero exits require mutual adjacency of the two replacement labels — preserved pre-item development

## Composition

(none yet)

## Development

## Adjacent nonzero exits require a relation between the two replacement labels

Let B={a,b,c,d} have mutual terminal-pair graph the chordless cycle a-b-c-d-a before z. Assume
delta(a)=delta(b)=delta(z)=1,
delta(c)=delta(d)=0.

Add distinct labels x,y with delta(x)=delta(y)=0. Suppose their mutual neighborhoods among B are exactly
N_B(x)={d,a,b},
N_B(y)={a,b,c}.
One-way extra pair relations are allowed; the displayed conditions concern mutual adjacency. Allow the mutual relation xy to be either present or absent.

Let D be the chamber-defined outward subcomplex of P(B union {x,y,z}) using the usual rule: zero exit status or a tight final triple. The old pair locus embeds with x,y fixed in a prefix before B. As always, applying this to the protected filtration requires this full seven-label face to be an available protected enlargement with the specified fixed suffix.

**Theorem.** The original four-cycle is null-homotopic in D if and only if x and y are mutually adjacent before z.

**Sufficiency.** With z fixed, the triangles {d,a,x} and {a,b,x} replace segment d-a-b by d-x-b. The original cycle becomes x-b-c-d-x. If xy is mutual, the triangles {x,b,y} and {b,c,y} replace segment x-b-c by x-y-c. The old cycle is therefore homotopic in the terminal-pair locus to
x-y-c-d-x.
Every label on this new cycle has zero exit status. The merging and endpoint-subset construction contracts it inside D. Naturality of the terminal-pair equivalence supplies the actual homotopy of the old pair locus. QED for sufficiency.

**Necessity.** Suppose xy is not mutual. Let K' be the mutual clique complex on B union {x,y}. Its restriction to the labels with zero exit status {c,d,x,y} is just the path
x-d-c-y.
Thus it has no first homology.

The original four-cycle remains nonzero in H_1(K';F_2). To see this, attach x first: it cones off the proper induced path d-a-b of the old cycle. That path has zero first homology, so the original cycle injects into the enlarged complex. Then attach y. Because xy is absent, y's link is exactly the old induced path a-b-c, also with zero first homology. The same homology argument again preserves the old cycle. This is the cone-attachment argument of [[one_exterior_label_fills_a_four_cycle_only_by_mutual_adjacency_to_every_boundary_label]], applied sequentially.

The first-homology kernel theorem says that passing from this pair locus with z fixed to D can kill only the image of homology supported on zero-exit labels. That image is zero here. The original cycle therefore survives in H_1(D;F_2) and cannot be null-homotopic. QED.

### Relation to the opposite-exit repair

The concurrent result [[two_opposite_nonzero_exits_admit_independent_two_label_repair]] handles opposite exceptional vertices a,c: their zero-exit replacements can form a new cycle through the two unchanged labels b,d, without needing mutual adjacency between the replacements.

For adjacent exceptional vertices, under the stated three-neighbor patterns, the replacements themselves must be consecutive on the new zero-exit cycle. Their mutual relation is consequently necessary, not just convenient for the proposed disk.

This completes both placements of two nonzero exits for the basic two-replacement pattern. It remains conditional on the actual mutual neighborhoods, exit statuses, and availability of a protected ambient enlargement.
