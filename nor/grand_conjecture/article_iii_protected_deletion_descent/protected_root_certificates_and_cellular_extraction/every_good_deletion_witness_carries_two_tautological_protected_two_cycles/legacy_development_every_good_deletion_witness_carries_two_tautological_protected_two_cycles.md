# Every good deletion witness carries two tautological protected two-cycles — preserved pre-item development

## Every good deletion witness carries two tautological protected two-cycles

Assume a minimum counterexample and let
\[
O_x=(v_1,\ldots,v_m)
\]
be any NOR-good deletion order of \(V\setminus\{x\}\). By §287 its word is genuinely one-change; after normalization write
\[
0^p1^q,\qquad p,q\ge3.
\]

### Left endpoint

Prepending \(x\) gives the bad full word
\[
1,0^p1^q.
\]
Its initial transition on
\[
(x,v_1,v_2,v_3)
\]
is fully curved, since a flat endpoint repair would give a spanning one-change order. Therefore it carries the actual protected root
\[
\boxed{x\to v_3}.
\]

Now reverse the deletion order. The good order
\[
O_x^{\rm rev}=(v_m,\ldots,v_1)
\]
again has one change. Appending \(x\) gives a bad full order whose final transition is the reversed four-packet
\[
(v_3,v_2,v_1,x).
\]
By the same endpoint-blocking argument it is fully curved and carries
\[
\boxed{v_3\to x}.
\]

Thus
\[
x\leftrightarrow v_3
\]
is an actual protected two-cycle.

### Right endpoint

Appending \(x\) to \(O_x\) gives a fully-curved final barrier on
\[
(v_{m-2},v_{m-1},v_m,x)
\]
and hence
\[
\boxed{v_{m-2}\to x}.
\]

Prepending \(x\) to \(O_x^{\rm rev}\) gives the reversed barrier and hence
\[
\boxed{x\to v_{m-2}}.
\]

Therefore
\[
x\leftrightarrow v_{m-2}
\]
is a second actual protected two-cycle.

### Consequence

Every good deletion witness in a minimum counterexample already contains two opposite-root protected pairs:
\[
\boxed{x\leftrightarrow v_3,\qquad x\leftrightarrow v_{m-2}.}
\]

The two directions in each pair are the same fully-curved four-coordinate endpoint packet viewed from opposite global orientations.

Hence existence of a positive protected-root cycle, even a two-cycle, is not by itself a meaningful closure certificate. Such cycles are forced locally by endpoint blockedness.

The genuine Article III obligation is compatibility: combine protected roots whose witness orders share enough outside provenance to support a full-order splice. This explains why purely algebraic root-cancellation and arbitrary cycle minimization repeatedly stall, and it sharpens the target toward same-outside-order exchange, certified-shortcut realization, or common-cell extraction.
