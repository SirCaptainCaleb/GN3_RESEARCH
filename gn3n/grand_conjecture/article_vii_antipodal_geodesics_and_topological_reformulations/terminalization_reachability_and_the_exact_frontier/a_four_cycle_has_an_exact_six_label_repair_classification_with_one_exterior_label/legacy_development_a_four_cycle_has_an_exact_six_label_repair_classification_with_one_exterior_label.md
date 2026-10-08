# A four-cycle has an exact six-label repair classification with one exterior label — preserved pre-item development

## Exact six-label repair with one exterior label

Let B={a,b,c,d} have mutual terminal-pair graph the chordless cycle a-b-c-d-a before z. Add one distinct label y to the free reservoir, keeping the same tight-triple relation. The old pair locus is embedded by placing y in a fixed prefix before B.

Let T=B union {y,z}. On P(T) use the allowed-chamber rule
delta(last label)=0 or the last ordered triple is tight,
where delta(z)=1. Let D be the resulting chamber-defined subcomplex. This is the enlarged outward locus in the separated-window model whenever the fixed subsequent statuses are all zero. The full six-label enlargement must actually be an available protected ambient face; merely finding y elsewhere in the ordering does not supply that hypothesis.

Write N subset B for the labels mutually admissible with y before z:
u in N iff h(u,y,z)=h(y,u,z)=1.
Let r be the number of labels u in B with delta(u)=1.

**Theorem.** The inclusion of the original four-cycle pair locus into D is null-homotopic exactly in the following cases:
1. r=0;
2. N=B;
3. r=1, with unique nonzero-exit label a after cyclic relabeling, delta(y)=0, and N={d,a,b}.

In case 3, y is mutually admissible with the exceptional label and its two cycle neighbors, but not with the opposite label c. If y is also adjacent to c, case 2 applies. Thus a single exterior label need not be universal once movement of z is allowed.

In every other case the original circle survives in first homology with coefficients in F_2 and hence cannot be filled in D.

**Sufficiency.** If r=0, keep y fixed in the prefix and apply the five-label contraction theorem to B union {z}.

If N=B, the mutual graph after adding y is a cone on the old four-cycle. The pair locus with z still fixed is already contractible, by [[one_exterior_label_fills_a_four_cycle_only_by_mutual_adjacency_to_every_boundary_label]]. It is contained in D.

In case 3, the enlarged mutual clique complex contains the triangles {a,b,y} and {a,d,y}. Their union supplies a homotopy replacing the old cycle segment b-a-d by b-y-d. The old four-cycle is therefore homotopic to the cycle b-c-d-y-b. Every label of this new cycle has zero exit status.

Use the natural terminal-pair equivalence, including its compatibility with reservoir enlargement, to realize this homotopy in the pair locus with z fixed. The subcomplex of that locus whose terminal label always belongs to {b,c,d,y} maps null-homotopically into D: merge its last free block with z and contract toward the endpoint-subset locus on those zero-exit labels, as in the first inclusion of [[moving_the_following_label_has_an_exact_first_homology_kernel]]. Thus the new cycle, and hence the old cycle, is null-homotopic in D. This argument supplies an actual null-homotopy, not just vanishing first homology.

**Necessity.** Assume r>0 and N is a proper subset of B. Let K' be the enlarged mutual clique complex on B and the active label y, if any. The old cycle is nonzero in H_1(K';F_2): adding the cone from y over a proper induced subgraph of C_4 cannot kill the original class, as proved in [[one_exterior_label_fills_a_four_cycle_only_by_mutual_adjacency_to_every_boundary_label]].

By [[moving_the_following_label_has_an_exact_first_homology_kernel]], this class can die in H_1(D) only if it belongs to the image of first homology of the induced subcomplex K'_S on labels with zero exit status.

If r>=2, S has at most three labels, even if y belongs to S. A clique complex on at most three vertices has zero first homology. Thus the old class survives.

Suppose r=1, with exceptional label a. If delta(y)=1, S={b,c,d} induces a path, again with zero first homology.

It remains that delta(y)=0. The induced graph on S={b,c,d,y} consists of the path b-c-d and whichever edges from y meet that path. Its clique complex has nonzero first homology only when y is adjacent to b and d but not c. Indeed these are exactly the conditions for the unique possible chordless four-cycle on S; all other choices give a forest or a complex with its triangular cycles filled.

Under those conditions, N is either {b,d} or {a,b,d}. If N={b,d}, the full enlarged graph is the theta graph consisting of the three length-two paths b-a-d, b-c-d, and b-y-d, with no triangles. The original cycle and the zero-exit cycle are linearly independent in its first homology: the original one uses edge ab and the latter does not, and there are no two-boundaries. Hence the original class is not in the image from K'_S and survives in D.

The only remaining case is N={a,b,d}, precisely case 3. This proves necessity. QED.

### What this repairs

With z fixed, one exterior label must be adjacent to all four cycle labels to fill the loop. Allowing z to move adds exactly one nonuniversal possibility: replace a single label having nonzero exit status by an exterior label having zero exit status and three specified mutual adjacencies.

If two or more original exit statuses are nonzero, one nonuniversal exterior label cannot suffice in this six-label model. Further labels, different boundary data, or another global argument are then genuinely needed.

The theorem classifies this local extension and gives a concrete six-label repair test. It does not assert that an appropriate exterior label exists in every boundary tournament, nor does a null-homotopy of this one cycle imply contractibility of the full enlarged locus or compatibility of independent ambient enlargements.
