# Reversals are unavoidable

## Body

**Lemma 1.** If two tight paths of order at least three have an order disagreement on their common vertices, then \(H\) contains a tight triple reversing an edge of one of the paths.

**Proof.** Choose a disagreeing pair with minimum union and then minimum total order. If a common edge is traversed in opposite directions, a consecutive tight triple containing that edge reverses the corresponding edge of the other path.

Otherwise the first change of relative order yields a reversing triple unless the two paths close into a vertex-simple tight cycle. Open such a cycle at any edge. Its complement is non-Hamiltonian and has a two-cover \(A\mid B\). Let \((a_{m-1},a_m)\) be an end edge of a nontrivial component \(A\). If both triples needed to concatenate \(A\) to the opened cycle were tight, the concatenation together with \(B\) would two-cover \(H\). Hence one of those triples is non-tight. Boundary reversal then gives a tight triple reversing either \((a_{m-1},a_m)\) or an edge of the opened cycle. \(\square\)

Deletion covers at different vertices cannot all induce one common support partition and one common relative order, since those orders would glue to a two-cover. Hence:

**Corollary 2.** Every minimum counterexample contains a tight triple reversing an edge of a tight path.

The remaining question is where such a reversal can be placed.

## Metadata

- ID: longest_paths_and_reversal_structure_reversals_are_unavoidable
- Kind: line
- Version: 1
- Math version: 1
- Audit: passed
- Refutation: unrefuted

## Authoring state

- Chunk 1 — HOT, version 1: (untitled)
