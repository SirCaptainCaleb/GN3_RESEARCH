# 

There is a second argument that does not follow one trajectory.

Two deletion covers are compatible when, after deleting both omitted labels, they induce the same support partition and the same relative order on every common support.

**Lemma 5.** If deletion covers \(F_x\) of \(H-x\) and \(F_y\) of \(H-y\) are compatible, their singleton lifts lie on one edge of \(\mathcal R(H)\).

**Proof.** On \(H-\{x,y\}\), compatibility gives two common ordered supports, say \(A,B\). In \(F_x\), the restored vertex \(y\) is inserted into one of them; in \(F_y\), the restored vertex \(x\) must be inserted into the same support, since insertion into the other support would produce two disjoint Hamiltonian supports covering \(H\). Suppose the common support is \(A\). Then the two singleton lifts have the form
\[
(A+y)\mid B\mid\{x\},
\qquad
(A+x)\mid B\mid\{y\}.
\]
Replacing
\[
(A+y)\mid\{x\}
\]
by
\[
(A+x)\mid\{y\}
\]
is a pairwise repartition. \(\square\)

Hence every connected component of the compatibility graph of chosen deletion covers maps into one connected component of \(\mathcal R(H)\).

By Lemma 1, this component then contains, for every deleted label in the compatibility component, its singleton lift and its central three- or five-vertex representative. Thus a large compatibility component produces many differently rooted bounded states in one component of \(\mathcal R(H)\).

If the compatibility graph has no large connected component, choosing labels from different components produces a large family of pairwise incompatible deletion covers. This is the complementary structural case and belongs to the deletion-cover argument rather than the recurrence argument.
