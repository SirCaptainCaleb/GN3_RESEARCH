# Flag-compatible outermost-root paths admit a recursive two-shore decomposition

## Composition

A return path of outermost roots drawn from one nested face flag admits a recursive two-shore decomposition. In any contiguous subpath, the root from the coarsest occurring face is strictly forward across any block boundary it crosses, while every other edge is weakly forward there; hence that pivot is the unique crossing and splits the subpath into opposite shores. Recursing gives a binary tree with strictly decreasing face rank down branches. The flag-cycle realization problem therefore reduces recursively to one relative merge at a time.

## Development

## Flag-compatible outermost-root paths admit a recursive two-shore decomposition

Consider a directed path of physical roots
\[
P:x_0\to x_1\to\cdots\to x_m
\]
whose edges are outermost-change roots of witnesses attached to distinct faces from one nested flag
\[
F_1<\cdots<F_k.
\]
Take any nonempty contiguous subpath \(Q\) of \(P\). Let \(G\) be the largest face in the flag whose root occurs on \(Q\), and write its pivot edge as
\[
r_G=a\to b.
\]

Every other edge of \(Q\) comes from a face refining \(G\). Therefore, with respect to the ordered blocks of \(G\), every edge of \(Q\) is weakly forward, while \(r_G\) is strictly forward.

Choose any boundary between consecutive \(G\)-blocks crossed by \(a\to b\), and coarsen there to two shores
\[
H=L|R.
\]
All edges of \(Q\) are weakly forward across \(H\), and \(r_G\) crosses from \(L\) to \(R\). Hence no other edge of \(Q\) can cross this boundary: after the path enters \(R\), weak forwardness forbids a return to \(L\).

Consequently \(Q\) factors uniquely at the pivot edge as
\[
Q=Q_L\,(a\to b)\,Q_R,
\]
where every vertex of \(Q_L\) lies in \(L\) and every vertex of \(Q_R\) lies in \(R\).

### Recursive theorem

Apply the same argument to each nonempty child subpath. Its edge labels are still drawn from a chain, and its largest remaining face is a valid new pivot. Induction on the number of edges gives a binary decomposition tree with the following properties:

1. each internal node is one actual outermost root from the path;
2. the node's face is the coarsest face appearing in that path segment;
3. its two children lie entirely on opposite shores of a block boundary crossed by that root;
4. face ranks strictly decrease down every branch;
5. leaves are single vertices.

Thus every flag-compatible closing path has a canonical hierarchical shore structure obtained by repeatedly cutting at the coarsest remaining witness.

### Application to the degree closing cycle

For the cycle of §245,
\[
s\to t=x_0\to x_1\to\cdots\to x_m=s,
\]
delete the backward apex edge \(s\to t\). The boundary return path from \(t\) to \(s\) therefore admits the recursive decomposition above.

This sharpens the realization problem. One does not need to realize an arbitrary directed root circuit or glue an arbitrary family of incomparable witness sheets. The entire return path is assembled recursively from nested proper-subinstance shores, with one coarsest transverse outermost root at each merge.

Hence the remaining flag-cycle splice theorem may be attacked inductively: realize one relative merge at a tree node while preserving the two child shores, or obtain a spanning NOR-good order / strict admissible improvement. A successful relative splice rule at one node propagates up the whole tree and ultimately confronts the apex root.
