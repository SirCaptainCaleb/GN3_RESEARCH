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

### A connected support path already closes the theorem

**Lemma 6 (connected support path closure).** Let one deletion cover (F_x) be selected for every vertex (xin V(H)), and let (J) be the resulting support graph. If (J) is a connected path, then (H) has a two-cover.

**Proof.** Put
[
n=|V(H)|.
]
There is exactly one selected edge (e_x) for each label (x), so (J) has exactly (n) edges. Since it is a connected path, write
[
S_0-S_1-cdots-S_n
]
for its support vertices, with the edge (S_{i-1}S_i) labeled (x_i).

For any vertex label (z
e x_i), exactly one of (S_{i-1},S_i) contains (z), because the two endpoint supports of (e_{x_i}) partition
[
V(H)-{x_i}.
]
For (z=x_i), neither endpoint contains (z).

Fix (j). The label (x_j) is absent from both
[
S_{j-1},S_j.
]
Moving left from (S_{j-1}), membership of (x_j) alternates across each preceding edge, since none of those edges is labeled (x_j). Therefore
[
x_jin S_0
quadLongleftrightarrowquad
j 	ext{is even}.
]
Likewise, moving right from (S_j),
[
x_jin S_n
quadLongleftrightarrowquad
n-j 	ext{is odd}.
]

If (n) is even, the second condition is equivalent to (j) odd. Hence
[
S_0={x_j:j 	ext{even}},
qquad
S_n={x_j:j 	ext{odd}}.
]
The two supports are disjoint and their union is (V(H)). Every support vertex of (J) is the support of a tight path in a selected deletion cover, so both (S_0) and (S_n) are Hamiltonian. They therefore form a two-cover of (H).

If (n) is odd, then
[
n-j 	ext{odd}
quadLongleftrightarrowquad
j 	ext{even},
]
so
[
S_n=S_0.
]
But the support vertices on a path are distinct. Equivalently, identifying the equal endpoints closes the displayed walk into a cycle, contradicting the assumption that (J) is a path in a forest.

Thus a connected support path cannot occur in a counterexample. (square)

**Corollary 7 (global no-reversal support residue).** In a counterexample, after excluding the reversal/order-disagreement outcome of Corollary 5, the selected support graph cannot be a connected forest. Hence the only remaining support-graph geometries are

1. a disconnected union of support paths; or
2. the unique spanning odd cycle from the support-graph dichotomy.

Thus the connected forest case is closed at arbitrary order. The remaining forest issue is precisely the already-identified **component escape** between distinct support-path components, not any internal tree or branching geometry.

### Compatible pairs have no quiet endpoint-slot residue

The insertion-slot lemma can be sharpened at an endpoint.

**Proposition (compatible-pair trichotomy).** Let \(F_a,F_b\) be deletion covers of \(H-a,H-b\) that are support-compatible. Then at least one of the following holds:

1. their common-support orders disagree, hence a displayed-edge reversal is forced by the order-disagreement machinery;
2. \(H\) has a two-cover;
3. \(H\) contains a Hamiltonian four-support with non-Hamiltonian path-cover-two complement;
4. the two insertion slots are adjacent, hence Lemma 3 gives a reversing tight triple.

In particular, a compatible pair has no purely neutral equal-endpoint-slot residue.

**Proof.** If the common-support orders disagree, outcome 1 holds. Otherwise \(F_a,F_b\) are compatible, so Lemma 3 puts the omitted labels \(a,b\) into the same common support in equal or adjacent insertion slots.

Adjacent slots give outcome 4.

Suppose the slots are equal and internal, between consecutive common vertices \(u,v\). Then both
\[
(u,a,v),\qquad (u,b,v)
\]
are tight. The compatible one-vertex extension lemma makes
\[
\{u,v,a,b\}
\]
Hamiltonian. In a minimum counterexample its complement has path-cover number two and is non-Hamiltonian, giving outcome 3.

It remains that the common slot is an endpoint gap. Write the common ordered support as
\[
P=(p_1,\ldots,p_m)
\]
and, after reversing if necessary,
\[
F_a=(b,p_1,\ldots,p_m)\mid Q,
\qquad
F_b=(a,p_1,\ldots,p_m)\mid Q.
\]
Exactly one of the two boundary orientations
\[
(a,b,p_1),\qquad (b,a,p_1)
\]
is tight. In the first case
\[
(a,b,p_1,\ldots,p_m)
\]
is a tight path; in the second
\[
(b,a,p_1,\ldots,p_m)
\]
is. Together with \(Q\), either order gives a spanning two-cover of \(H\). This is outcome 2. \(\square\)

Consequently, in the spanning odd-cycle support geometry, every adjacent pair of selected support edges immediately yields a reversal, a bounded Hamiltonian four-support, or a two-cover. Thus the odd-cycle geometry cannot support an additional quiet neutral omission-swap recurrence.


## Metadata

- ID: deletion_covers_and_the_support_graph_compatibility_of_deletion_covers
- Kind: section
- Version: 6
- Math version: 5
- Audit: unaudited
- Refutation: unrefuted

## Authoring state

- Subsection 1 — crystallized, version 2: (untitled)
- Subsection 2 — HOT, version 5: Three compatible covers force a reversal
