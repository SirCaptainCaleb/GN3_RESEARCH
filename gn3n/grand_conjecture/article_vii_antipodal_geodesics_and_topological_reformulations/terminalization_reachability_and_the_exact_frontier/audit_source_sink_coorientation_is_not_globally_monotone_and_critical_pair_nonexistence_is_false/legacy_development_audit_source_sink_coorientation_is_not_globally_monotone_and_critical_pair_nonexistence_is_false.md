# Audit: source-sink coorientation is not globally monotone and critical-pair nonexistence is false — preserved pre-item development

## Composition

(none yet)

## Development

## Audit of the monotone-separator and critical-pair closure claims

This audits subsection 261, in the context of the valid source/sink and square-cocycle statements in 258-259.

### Componentwise coorientation does not imply one global monotone potential

A cubical cut delta f whose boundary vertices are pure sources/sinks need not admit a single normalization with f=0 on ALL sources and f=1 on ALL sinks. Different connected cut components can have opposite coorientations.

Here is an explicit antipodally invariant source/sink cut on the 19-dimensional cube. For a plus-set A put
f(A)= (number of elements of {4,7,10,13,16} at most |A|) mod 2.

Then delta f consists precisely of the complete incidence layers at source ranks 4,7,10,13,16. These ranks are pairwise separated by at least three. Hence each nonisolated cube vertex is a pure source or pure sink, and every square has even cut incidence because the cut is delta f. Also
f(V-A)=1-f(A),
so the cut is antipodally invariant and self-dual.

However the f-values at sources of these five components are respectively
1,0,1,0,1.
Adding a global constant flips all five and cannot make them equal. Thus f is not monotone under the subset order, and no global additive normalization makes it so.

This is a counterexample to the pure-source/sink + cocycle + antipodal-symmetry INFERENCE used in subsection 261. It is not claimed to arise from Hamiltonian deletion covers of a counterexample. Additional Hamiltonicity hypotheses could conceivably force global coorientation, but that requires an additional proof. The componentwise statement in subsection 258 remains valid.

Subsection 262 avoids this gap: minimum imbalance excludes parallel square adjacencies except at the middle ranks and thereby proves a stronger rank classification without assuming global monotonicity.

### The proposed universal nonexistence of a critical pair is false

There is a real edge-ordered boundary tournament with a partition A|B satisfying all three local conditions in the proposed critical-pair target:
- A is non-Hamiltonian and A-x is Hamiltonian for every x in A;
- B is Hamiltonian;
- B+x is non-Hamiltonian for every x in A.

Use V={1,...,7}, A={1,2,3,4}, B={5,6,7}. Set the edge ranks
12=1, 34=2, 13=3, 24=4, 14=5, 23=6;
56=10, 57=20, 67=30;
x7=10+x, x6=20+x, x5=30+x for x in A.
All ranks are distinct, and declare (u,v,w) tight iff rank(uv)<rank(vw).

The three opposite-edge matchings of A are the consecutive blocks
{12,34} < {13,24} < {14,23},
so A is non-Hamiltonian. Each A-x has order three and is Hamiltonian; explicit words are
x=1: 342; x=2: 314; x=3: 124; x=4: 123.
B has Hamilton word 567.

For every x in A, the opposite-edge matchings of B+x are the consecutive blocks
{56,x7} < {57,x6} < {67,x5}.
Hence every B+x is non-Hamiltonian as well.

Nevertheless H has the MIXED spanning two-cover
(1,2,5) | (3,4,6,7).
The needed consecutive edge ranks are
1<31 on the first path, and 2<24<30 on the second.

The matching-block classification proves the non-Hamiltonicity claims directly; all four-/three-word cases and the displayed mixed cover were also checked using exact integer comparisons.

Therefore the three critical-pair properties are not universally impossible in boundary tournaments. A correct potential closure lemma would have to CONSTRUCT a mixed two-cover from those properties (possibly with further minimum-counterexample structure), rather than assert that the partition itself cannot exist.

This example is not a counterexample to the grand theorem. It diagnoses an overstrong intermediate target, and shows explicitly that a blocked original partition can be escaped by mixing supports.

### The empty-core branch remains separate

The unique-face collapses in subsection 258 may remove every top facet. If that happens there is no nonempty cut, no source upset, and no inclusion-minimal source from which to extract a critical pair. Thus even a correct nonempty-core-to-critical-pair theorem would not by itself reduce the entire grand conjecture to that pair. One must either prove that a relevant nonempty core survives or close the all-collapsed branch independently.

No global closure is claimed.
