# A flag-compatible outermost-root cycle is a strict ordered transversal of the finest face — preserved pre-item development

## A flag-compatible outermost-root cycle is a strict ordered transversal of the finest face

Continue with the directed cycle supplied by §244/§245:
\[
x_0\to x_1\to\cdots\to x_m\to x_0,
\]
where the apex edge \(x_0\to x_1\) comes from an arbitrary bad full order and every return edge
\[
x_i\to x_{i+1}\qquad(1\le i\le m)
\]
is the outermost-change root of a canonical proper-face witness \(\pi_{F_j}\) from one nested flag
\[
F_1< F_2<\cdots<F_k.
\]

Let
\[
F_1=B_1|\cdots|B_s
\]
be the finest face in the flag.

### Common strict orientation

Every later face \(F_j\) is obtained from \(F_1\) by merging consecutive blocks. For its canonical witness \(\pi_{F_j}\), §243 shows that the source and target of its outermost root lie in two distinct \(F_j\)-blocks, with the source block earlier than the target block.

Distinct \(F_j\)-blocks are unions of disjoint consecutive intervals of \(F_1\)-blocks. Therefore the source coordinate lies in a strictly earlier \(F_1\)-block than the target coordinate.

Hence, for the \(F_1\)-block-rank functional \(\beta\),
\[
\boxed{\langle\beta,r\rangle<0}
\]
for every boundary root \(r\) occurring in the flag-compatible cycle.

This is stronger than the weak largest-face orientation used in the two-shore extraction: all return edges are simultaneously strictly forward in one common ordered partition.

### Ordered-transversal consequence

Along the boundary return path
\[
x_1\to x_2\to\cdots\to x_0
\]
the \(F_1\)-block index strictly increases at every step.

Therefore:

1. the path meets each \(F_1\)-block in at most one cycle vertex;
2. its vertices form a strictly increasing transversal through a subsequence of the ordered blocks \(B_1,\ldots,B_s\);
3. the path length is at most \(s-1\);
4. the apex edge is strictly backward in the same block order, joining the last visited block back to the first.

Thus the support-minimal degree obstruction has the form
\[
x_0\to x_1\to x_2\to\cdots\to x_m\to x_0
\]
with
\[
\operatorname{blk}(x_1)<\operatorname{blk}(x_2)<\cdots<\operatorname{blk}(x_m)<\operatorname{blk}(x_0).
\]

### Proper-block structure

Each block \(B_j\) is a proper coordinate subset and carries its fixed NOR-good order \(g(B_j)\). The cycle selects at most one distinguished physical coordinate from each visited block. Therefore no compatibility problem remains inside a visited block between two different cycle vertices: all nontrivial cycle motion is between distinct proper good blocks.

This converts the topological output into an ordered block-transversal splice problem.

### Closure target

It is enough to prove the following relative transversal theorem:

> Given proper good blocks \(B_1|\cdots|B_s\) and distinct selected coordinates
> \[
> y_1\in B_{i_1},\ldots,y_\ell\in B_{i_\ell},
> \qquad i_1<\cdots<i_\ell,
> \]
> whose successive physical roots are witnessed as outermost-change roots by canonical coarsenings of the same block flag, together with one bad apex witness whose outermost root closes \(y_\ell\to y_1\), produce a spanning NOR-good order or a strict admissible improvement.

The key simplification is that the return path is monotone through the fixed block order and never revisits a block. Any failed realization can therefore be assigned to its first block junction without later recurrence to that block.
