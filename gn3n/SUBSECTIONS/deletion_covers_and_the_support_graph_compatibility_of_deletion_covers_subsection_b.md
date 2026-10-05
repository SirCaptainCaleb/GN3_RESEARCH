# Three compatible covers force a reversal

## Metadata

- ID: deletion_covers_and_the_support_graph_compatibility_of_deletion_covers_subsection_b
- Parent Section: deletion_covers_and_the_support_graph_compatibility_of_deletion_covers
- Position: 2
- Row version: 5
- Development version: 5
- Composition version: None
- Composition stale: True

## Cold composition

(none yet)

## Development

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
