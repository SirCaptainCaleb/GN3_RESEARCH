# Every edge of a minimum signature shore lies in a directed triangle, hence the shore tournament is strongly connected

## Composition

(none yet)

## Development

## Every edge of a minimum signature shore lies in a directed triangle, hence the shore tournament is strongly connected

Continue with the minimum shortcut-free split
\[
B\to z\to A\to x
\]
and the protected-clique theorem §341.

Fix a directed edge
\[
u\to v
\]
of the induced tournament \(T[A]\). Let
\[
h(w)=\alpha(u,v,w).
\]

In the switching-normalized representative, every vertex outside \(A\) has the same \(u,v\)-signature. Since \(u\to v\), that common value is \(0\).

By §341 the pair \(u,v\) is protected and therefore nonclone, so \(h\) is nonconstant. Hence some
\[
w\in A\setminus\{u,v\}
\]
has
\[
\alpha(u,v,w)=1.
\]

For a tournament triple containing the directed edge \(u\to v\), ternary value \(1\) means the triple is cyclic. Therefore necessarily
\[
v\to w\to u,
\]
and
\[
u\to v\to w\to u
\]
is a directed triangle contained in \(A\).

Thus
\[
\boxed{\text{every directed edge of }T[A]\text{ lies in a directed triangle inside }A.}
\]

Now suppose \(T[A]\) had at least two strongly connected components. The condensation of a tournament is a transitive tournament, so for two consecutive components every cross-edge is oriented in the same forward direction. Such a cross-edge cannot lie in a directed triangle: a directed triangle using it would provide a return path from the later component to the earlier component.

Contradiction.

Hence
\[
\boxed{T[A]\text{ is strongly connected}.}
\]

This strengthens §§337,342: the minimum shore is not merely source/sink-free and does not merely contain one protected triangle. Its entire edge set is covered by internal directed triangles. Every shore edge therefore supplies a five-coordinate monochromatic connector seed with \(x,z\) after choosing one of its triangle completions as in §344.
