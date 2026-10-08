# Deletion distance one has root advance or a complete reverse rectangle — preserved pre-item development

## Deletion distance one has an opposite-boundary five-path or a complete reverse rectangle

Assume
\[
\kappa_2(H)=1,\qquad \operatorname{pc}(H)>2,
\]
and fix a minimum-hole deletion cover
\[
H-x=P\mid Q,
\]
with
\[
P=(p_1,\ldots,p_r),\qquad Q=(q_1,\ldots,q_s),
\qquad r,s\ge3.
\]

By [[kappa_one_four_end_reversal]],
\[
h(p_2,p_1,x)=h(q_2,q_1,x)=1,
\]
and
\[
h(x,p_r,p_{r-1})=h(x,q_s,q_{s-1})=1.
\]

Put
\[
L=\{p_1,q_1\},\qquad R=\{p_r,q_s\}.
\]

Consider the four cross statuses
\[
h(a,x,b),\qquad a\in L,\ b\in R.
\]

### Root-advance branch

Suppose
\[
h(a,x,b)=1
\]
for some \(a\in L,b\in R\).

Let \(a'\) be the second vertex on the same displayed path as \(a\):
\[
a'=p_2\quad\text{if }a=p_1,\qquad
a'=q_2\quad\text{if }a=q_1.
\]
Let \(b'\) be the penultimate vertex on the same displayed path as \(b\):
\[
b'=p_{r-1}\quad\text{if }b=p_r,\qquad
b'=q_{s-1}\quad\text{if }b=q_s.
\]

Then
\[
h(a',a,x)=1,\qquad
h(a,x,b)=1,\qquad
h(x,b,b')=1.
\]
Therefore
\[
\boxed{(a',a,x,b,b')}
\]
is a tight Hamiltonian five-path.

Thus any positive entry of the \(2\times2\) cross matrix produces an explicitly rooted five-component joining opposite boundaries of the deletion cover.

### Complete reverse-rectangle branch

Assume no such five-path arises from the cross matrix. Then
\[
h(a,x,b)=0
\qquad
(a\in L,\ b\in R).
\]
Boundary antisymmetry, with middle vertex \(x\), gives
\[
\boxed{h(b,x,a)=1
\qquad
(a\in L,\ b\in R).}
\]

Hence the only residue is the complete reverse rectangle
\[
R \longrightarrow_x L:
\]
every terminal endpoint \(b\in\{p_r,q_s\}\) forms a tight triple
\[
(b,x,a)
\]
with every initial endpoint \(a\in\{p_1,q_1\}\).

Therefore:

> **Opposite-boundary dichotomy for \(\kappa_2=1\).** Every one-hole deletion cover has either an explicit five-path
> \[
> (a',a,x,b,b')
> \]
> bridging an initial boundary to a terminal boundary, or the four cross triples through the hole form a complete reverse \(K_{2,2}\) rectangle.

The five-path branch gives a spanning three-cover with a distinguished rooted five-component and two inherited residual path intervals. The complete reverse rectangle is the only local configuration that avoids all four such opposite-boundary root advances.

No minimum-counterexample assumption, cyclic rotation, path reversal, or computation is used.
