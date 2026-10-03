# Reversals are unavoidable

## Body

**Lemma 1.** If two tight paths of order at least three have an order disagreement on their common vertices, then \(H\) contains a tight triple reversing an edge of one of the paths.

**Proof.** Choose a disagreeing pair with minimum union and then minimum total order. If a common edge is traversed in opposite directions, a consecutive tight triple containing that edge reverses the corresponding edge of the other path.

Otherwise the first change of relative order yields a reversing triple unless the two paths close into a vertex-simple tight cycle. Open such a cycle at any edge. Its complement is non-Hamiltonian and has a two-cover \(A\mid B\). Let \((a_{m-1},a_m)\) be an end edge of a nontrivial component \(A\). If both triples needed to concatenate \(A\) to the opened cycle were tight, the concatenation together with \(B\) would two-cover \(H\). Hence one of those triples is non-tight. Boundary reversal then gives a tight triple reversing either \((a_{m-1},a_m)\) or an edge of the opened cycle. \(\square\)

Deletion covers at different vertices cannot all induce one common support partition and one common relative order, since those orders would glue to a two-cover. Hence:

**Corollary 2.** Every minimum counterexample contains a tight triple reversing an edge of a tight path.

The remaining question is where such a reversal can be placed.

### Every prescribed pair forces an endpoint-reversal pattern

The preceding existence statement has a pairwise strengthening.

**Lemma 3.** Let \(H\) be a minimum counterexample and let \(u,v\in V(H)\) be distinct. Then
\[
\operatorname{pc}(H-\{u,v\})=2.
\]
Moreover, in every two-cover
\[
H-\{u,v\}=A\mid C,
\]
both \(A\) and \(C\) have order at least two. Writing
\[
A=(a_1,\ldots ,a_r),\qquad C=(c_1,\ldots ,c_s),
\]
one of the following holds:

1. both
\[
(u,a_r,a_{r-1}),\qquad (v,a_r,a_{r-1})
\]
are tight;

2. both
\[
(c_2,c_1,u),\qquad (c_2,c_1,v)
\]
are tight;

3. after naming one of \(u,v\) as \(z\) and the other as \(w\),
\[
(a_{r-1},a_r,z),\qquad (z,c_1,c_2)
\]
are tight, while
\[
(w,a_r,a_{r-1}),\qquad (c_2,c_1,w)
\]
are tight.

In particular, every prescribed pair \(\{u,v\}\) participates in a spanning three-cover in which an exposed end edge of one of the other two paths is reversed by a tight triple through \(u\) or \(v\).

**Proof.** Every two-vertex set is a tight path. Since \(\{u,v\}\) is a proper Hamiltonian support, minimum-counterexample calculus gives
\[
\operatorname{pc}(H-\{u,v\})\le2.
\]
If \(H-\{u,v\}\) were Hamiltonian, its Hamilton path together with the two-vertex path on \(\{u,v\}\) would give a two-cover of \(H\). Hence the path-cover number is exactly two.

Let \(A\mid C\) be any two-cover of the complement. Neither component can be a singleton. Indeed, if \(A=\{a\}\), then the three-set \(\{u,v,a\}\) has a tight Hamilton path: fixing \(v\) as the middle vertex, exactly one of
\[
(u,v,a),\qquad(a,v,u)
\]
is tight. That three-vertex path together with \(C\) would two-cover \(H\), a contradiction. Thus \(r,s\ge2\).

Now
\[
A\mid(u,v)\mid C
\]
is a spanning three-cover. Apply the two-vertex-middle endpoint classification from the rooted small-support analysis. Its three alternatives are exactly the three displayed patterns above. \(\square\)

Thus reversals in a minimum counterexample are not isolated artifacts of a particular deletion cover or longest path: every chosen vertex pair can be placed into a two-vertex middle component whose complementary two-cover exposes an endpoint reversal. The remaining issue is positional compression, not production of reversals.

## Metadata

- ID: longest_paths_and_reversal_structure_reversals_are_unavoidable
- Kind: section
- Version: 2
- Math version: 2
- Audit: unaudited
- Refutation: unrefuted

## Authoring state

- Subsection 1 — HOT, version 2: (untitled)
