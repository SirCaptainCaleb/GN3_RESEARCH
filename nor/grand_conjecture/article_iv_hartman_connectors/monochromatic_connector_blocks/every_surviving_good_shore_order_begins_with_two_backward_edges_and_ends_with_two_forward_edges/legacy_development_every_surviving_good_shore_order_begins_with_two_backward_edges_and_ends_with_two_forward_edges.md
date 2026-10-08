# Every surviving good shore order begins with two backward edges and ends with two forward edges — preserved pre-item development

## Composition

(none yet)

## Development

## Every surviving good shore order begins with two backward edges and ends with two forward edges

Continue in the switching-normalized split
\[
B\to z\to A\to x.
\]

Let
\[
O=(a_1,\ldots,a_k)
\]
be NOR-good on \(A\), with normalized word \(0^p1^q\).

The endpoint theorem gives
\[
e_1=0,\qquad e_{k-1}=1,
\]
where \(e_i=1\iff a_i\to a_{i+1}\).

We strengthen this by one edge on each side.

### Left side

Assume for contradiction
\[
e_2=1.
\]
Consider
\[
C=(z,a_1,x,a_2,a_3,\ldots,a_k).
\]

The three new initial windows are
\[
\alpha(z,a_1,x)=0,
\]
because \(z\to a_1\to x\) and \(z\to x\);

\[
\alpha(a_1,x,a_2)=0,
\]
because \(e_1=0\), so \(a_2\to a_1\), while both shore vertices dominate \(x\);

and
\[
\alpha(x,a_2,a_3)
=
1\oplus e_2
=
0.
\]

Every later window is an old window of \(O\), beginning at old rank \(2\). Deleting the first old status from a one-change word leaves a one-change word. Hence \(C\) is spanning NOR-good, contradiction.

Therefore
\[
\boxed{e_2=0.}
\]

### Right side

Apply the same left-side argument to the reversed good order
\[
O^{\mathrm{rev}}.
\]
Its second edge bit is
\[
e'_2=1-e_{k-2}.
\]
Since every surviving good shore order has \(e'_2=0\),
\[
\boxed{e_{k-2}=1.}
\]

### Conclusion

Every surviving good shore order satisfies
\[
\boxed{e_1=e_2=0,\qquad e_{k-2}=e_{k-1}=1.}
\]

Thus the universal residual endpoint seed
\[
(a_2,a_1,x,z,a_{k-1},a_k)
\]
is backed by two-edge orientation runs, not merely by its exposed endpoint pairs.

This gives a stronger boundary condition for collective connector growth and for the outward adjacent-gap transport: any obstruction reaching either end meets a fixed two-edge \(00\) or \(11\) collar.

Elevation audit: the endpoint constructions yield NOR-good orders on U=A∪{x,z}. Therefore the 00/11 endpoint constraint is conditional on U-counterexamplehood, or on a proved full-instance extension theorem. It is not forced by counterexamplehood on larger V with nonempty B. Reversal preserves that scope limitation.
