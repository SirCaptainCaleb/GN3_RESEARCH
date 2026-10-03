# Compatibility of deletion covers

## Body

Two path covers of the same vertex set are support-compatible if they induce the same partition into path supports. They are compatible if they are support-compatible and every two vertices lying in one common support occur in the same relative order in the two path orders. When two deletion covers omit different vertices, these definitions are applied after restricting both covers to their common vertex set.

**Lemma 2 (compatibility gluing).** Let \(D\subseteq V(H)\), \(|D|\ge4\), and for every \(d\in D\) let \(F_d\) be a cover of \(H-d\) by at most two tight paths. If the covers are pairwise compatible on their common domains, then \(H\) has a two-cover.

**Proof.** For distinct \(u,v\), choose \(d\in D-\{u,v\}\). The relation saying that \(u,v\) lie in the same path of \(F_d\), together with their relative order when they do, is independent of \(d\) by compatibility. Any three vertices survive in some \(F_d\), so the same-path relation is transitive. It therefore partitions \(V(H)\) into at most two classes; otherwise three representatives from distinct classes survive in one cover.

Each class inherits a total order. Take three consecutive vertices in one class. A deletion label can be chosen outside them, and in the corresponding \(F_d\) these three vertices occur consecutively in the inherited order. Their ordered triple is tight. Hence every class is a tight path. These one or two paths cover \(H\). \(\square\)

The next lemma gives the local form of a compatible pair.

**Lemma 3 (insertion slots).** Let \(F_a\) and \(F_b\) be compatible deletion covers. Then the omitted vertices \(a\) and \(b\) are inserted into the same common support. Their insertion slots in the common order are equal or adjacent. If the slots are adjacent, there is a tight triple reversing the two inserted labels across the unique common vertex between the slots.

**Proof.** On \(V(H)-\{a,b\}\), compatibility gives two ordered supports, say \(P,Q\). In \(F_a\), the vertex \(b\) is inserted into one of them; in \(F_b\), the vertex \(a\) is inserted into one of them. If they are inserted into different supports, augmenting both supports simultaneously gives a two-cover of \(H\), a contradiction. Thus both are inserted into the same support, say
\[
P=(p_1,\ldots ,p_m).
\]

If the two slots are separated by at least one entire slot, insert both vertices into \(P\) at their respective positions. No new consecutive triple contains both inserted vertices; each consecutive triple is inherited from \(P\), \(F_a\), or \(F_b\). This again gives a two-cover with \(Q\). Hence the slots are equal or adjacent.

In the adjacent case write the common order as \(L,z,R\), with
\[
F_b=(L,a,z,R)\mid Q,\qquad F_a=(L,z,b,R)\mid Q.
\]
Every consecutive triple of \((L,a,z,b,R)\) is known to be tight except possibly \((a,z,b)\). If this triple were tight, the displayed path together with \(Q\) would cover \(H\) by two paths. Hence \((a,z,b)\) is non-tight, so its boundary flip
\[
(b,z,a)
\]
is tight. \(\square\)

## Three compatible covers force a reversal

### Three pairwise compatible deletion covers cannot remain featureless

**Lemma 4 (three compatible covers force a reversal).** Let (a,b,c) be distinct vertices of a boundary tournament (H) with (operatorname{pc}(H)>2). Suppose deletion covers
[
F_a,qquad F_b,qquad F_c
]
are pairwise compatible on their common domains. Then at least one pair has adjacent insertion slots in the sense of Lemma 3. Consequently (H) contains a tight triple reversing the two corresponding omitted labels across the unique common vertex between those slots.

Equivalently: three pairwise compatible deletion covers cannot have equal insertion slots for all three pairs.

**Proof.** By Lemma 3, for each pair the two omitted labels are inserted into the same common support, and their slots are equal or adjacent. If any pair uses adjacent slots, Lemma 3 already gives the asserted reversing triple.

Assume therefore that all three pairs use equal slots. Pairwise support compatibility, or equivalently the localization lemma for three support-compatible covers, places (a,b,c) in one varying support. The three compatible orders induce a common relative order on every pair of surviving vertices.

Write
[
alpha=[a<b],qquad
eta=[a<c],qquad
gamma=[b<c],
]
where each comparison is read in any deletion-cover order containing the displayed pair; compatibility makes it well-defined.

Because (a) and (b) occupy the same insertion slot relative to the common order in (F_a,F_b), they lie on the same side of every surviving common vertex, in particular of (c). Hence
[
eta=gamma.
]

Likewise, equal slots for (a,c), viewed relative to the surviving vertex (b), give
[
[a<b]=[c<b]=
eg[b<c],
]
so
[
alpha=
eggamma.
]

Finally, equal slots for (b,c), viewed relative to the surviving vertex (a), give
[
[a<b]=[a<c],
]
so
[
alpha=eta.
]

Combining
[
eta=gamma,qquad
alpha=
eggamma,qquad
alpha=eta
]
gives (gamma=
eggamma), a contradiction. Therefore some pair has adjacent slots, and Lemma 3 supplies the reversing tight triple. (square)

This strengthens the four-cover compatibility gluing threshold in the direction needed for recurrence arguments. Four pairwise compatible covers glue outright to a two-cover; already three pairwise compatible covers force a positional reversal.

### Branching in the support graph forces a reversal

**Corollary 5 (degree-three support obstruction).** Choose one deletion cover (F_x) for each label (x), and let (J) be their support graph. If a support vertex of (J) has degree at least three, then two selected path orders have an order disagreement on their common domain, or (H) contains a tight triple reversing an edge of one of the selected paths.

Consequently, in any reduction branch in which order disagreement and external reversal have already been excluded as successful disturbances,
[
Delta(J)le2.
]
By the support-graph dichotomy, (J) is then either a disjoint union of paths or the unique spanning odd cycle.

**Proof.** Let a support (S) be incident with three distinct selected edges
[
e_a, e_b, e_c.
]
The corresponding covers (F_a,F_b,F_c) are pairwise support-compatible, because adjacent support-graph edges are exactly support-compatible deletion covers.

Consider any pair, say (F_a,F_b). On their common domain the two support classes agree. If the induced path orders disagree on either common support, the path-order disagreement lemma gives a tight triple reversing an edge of one of the two paths. Thus, if no such reversal occurs, (F_a,F_b) are fully compatible. The same argument applies to the other two pairs.

Hence absence of an order-disagreement reversal makes (F_a,F_b,F_c) pairwise compatible. Lemma 4 then forces an adjacent-slot reversal, contradiction. Therefore degree at least three always produces one of the asserted reversal disturbances.

The final statement follows from the support-graph dichotomy: a forest of maximum degree at most two is a disjoint union of paths, while the only cyclic support graph is already one spanning odd cycle. (square)

Thus neutral omission-swap recurrence cannot hide in a branching support tree once reversals are treated as progress. Its only global geometries are one-dimensional: path recurrence in the forest case, or cyclic recurrence in the spanning odd-cycle case.

## Metadata

- ID: deletion_covers_and_the_support_graph_compatibility_of_deletion_covers
- Kind: section
- Version: 4
- Math version: 3
- Audit: unaudited
- Refutation: unrefuted

## Authoring state

- Subsection 1 — crystallized, version 2: (untitled)
- Subsection 2 — HOT, version 3: Three compatible covers force a reversal
