# Support-splitting reseeds have at least two interclass transitions — preserved pre-item development

## Development

## Genuine support-splitting reseeds have at least two interclass comparison edges

Retain the setup of [[support_splitting_seam_reseeds_are_exactly_comparison_disturbances]]:
\[
S\mid P'\mid Q'
\]
is a spanning three-cover with all three displayed classes nonempty, and
\[
H-K=A\mid B
\]
is a two-cover for a disjoint Hamiltonian seam support \(K\).

Assume \(A\mid B\) genuinely splits \(S\): both
\[
A\cap S\ne\varnothing,\qquad B\cap S\ne\varnothing.
\]

Cut every ordinary edge of the displayed paths \(A,B\) whose endpoints lie in different classes among
\[
S,\qquad P',\qquad Q'.
\]
Let \(t\) be the number of such interclass edges. Cutting them decomposes the two comparison paths into exactly
\[
t+2
\]
nonempty monochromatic blocks.

Because \(A\mid B\) splits \(S\), there is at least one \(S\)-block in \(A\) and at least one \(S\)-block in \(B\). Thus the class \(S\) alone contributes at least two blocks.

Since \(P'\) and \(Q'\) are both nonempty and are distinct displayed classes, each contributes at least one additional monochromatic block.

Hence there are at least four blocks in total:
\[
t+2\ge4.
\]
Therefore
\[
\boxed{t\ge2.}
\]

Consequently the \(t=1\) branch considered in [[support_splitting_seam_reseeds_are_exactly_comparison_disturbances]] cannot occur under genuine support splitting.

Now use the block-count argument from its \(t\ge2\) case. At least one displayed class occurs in at least two comparison blocks.

- If two such blocks lie in different comparison paths, then that displayed Hamilton path has an ordinary displayed edge whose endpoints lie in different paths of \(A\mid B\).
- If two such blocks lie in the same comparison path, that path leaves the displayed class through a nonempty segment of another class and later returns.

Thus:

> **Strong support-splitting theorem.** Every genuine support-splitting seam reseed immediately yields either a split displayed edge or a leave-and-return comparison disturbance. There is no quiet one-interclass-edge normal form.

Hamilton-order disagreement, when present, remains an additional disturbance, but is not needed to prove nonquietness.

Therefore seam reseeding has only two structural modes:
1. support-preserving, already reduced to a short order-four complementary rail;
2. support-splitting, which is automatically a comparison disturbance with at least two interclass transitions.

No minimum-counterexample hypothesis, cyclic rotation, path reversal, or finite computation is used.
