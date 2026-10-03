# A balanced omission swap gives descent or recurrence between selected singleton lifts

**Summary:** Under minimum-imbalance deletion-cover selection, a Phi-neutral omission swap either yields strict quadratic descent or a Phi-neutral path to the selected singleton lift at the new omitted label.

## Statement

Let H be a boundary tournament, and for each vertex v choose a deletion cover F_v of H-v minimizing the sum of squares of its two component orders. Suppose a spanning singleton lift F_z|{z} admits a Phi-neutral pairwise repartition to G_w|{w}, where G_w is a deletion cover of H-w. Then Phi(F_w|{w})<=Phi(F_z|{z}). If the inequality is strict, F_z|{z} lies in the same pairwise-repartition component as a three-cover of strictly smaller Phi. If equality holds, F_z|{z} and the selected singleton lift F_w|{w} lie in the same Phi-level component, joined by at most two pairwise repartitions. In particular, the Phi-neutral omission-swap outcome of [[path_disturbance_endpoint_reversal_descent_or_an_omission_swap]] reduces to strict descent or neutral recurrence among selected singleton lifts.

## Body

Let
\[
F_z=A\mid B
\]
be the selected deletion cover of \(H-z\), and suppose a pairwise repartition of the singleton lift
\[
A\mid B\mid\{z\}
\]
is \(\Phi\)-neutral and yields
\[
G_w=C\mid D
\]
as a deletion cover of \(H-w\), so that the resulting three-cover is
\[
C\mid D\mid\{w\}.
\]
Thus
\[
\Phi(C\mid D\mid\{w\})=\Phi(A\mid B\mid\{z\}).
\]

Let the selected minimum-imbalance deletion cover of \(H-w\) be
\[
F_w=C'\mid D'.
\]
By its defining minimality,
\[
|C'|^2+|D'|^2\le |C|^2+|D|^2.
\]
After adjoining the singleton \(w\),
\[
\Phi(C'\mid D'\mid\{w\})
\le
\Phi(C\mid D\mid\{w\})
=
\Phi(A\mid B\mid\{z\}).
\]

Both \(C\mid D\mid\{w\}\) and \(C'\mid D'\mid\{w\}\) are three-covers of \(H\), and replacing \(C\mid D\) by \(C'\mid D'\) is a pairwise repartition because both are two-covers of the same induced subtournament \(H-w\). Hence the two singleton lifts are adjacent in the pairwise-repartition graph.

If the displayed inequality is strict, the selected singleton lift at \(w\) has strictly smaller quadratic potential than the original singleton lift at \(z\), and the two lie in the same pairwise-repartition component.

If equality holds, the original neutral repartition
\[
F_z\mid\{z\}\longrightarrow G_w\mid\{w\}
\]
followed by
\[
G_w\mid\{w\}\longrightarrow F_w\mid\{w\}
\]
is a path of at most two pairwise repartitions entirely on one \(\Phi\)-level. Thus a neutral omission swap can always be continued to the selected singleton lift at the new omitted label without increasing \(\Phi\).

For the neutral omission-swap outcome of [[path_disturbance_endpoint_reversal_descent_or_an_omission_swap]], the first neutral repartition and the deletion cover \(G_w\) are supplied by that result, so the preceding argument applies directly.

## Metadata

- ID: balanced_omission_swap_gives_descent_or_selected_singleton_recurrence
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
