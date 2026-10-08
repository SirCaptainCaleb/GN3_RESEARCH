# Minimum holes carry uniform cross-end five-path tests — preserved pre-item development

## Absolute nonaugmentability forces two additional cross-end relations

Let
\[
X
\]
be a minimum two-cover deletion hole and
\[
H-X=P\mid Q,
\qquad
P=(p_1,\ldots,p_s),\quad Q=(q_1,\ldots,q_t),
\]
with \(s,t\ge2\).

By the four-end synchronization theorem, every \(x\in X\) satisfies
\[
h(p_2,p_1,x)=1,\qquad h(x,p_s,p_{s-1})=1,
\]
\[
h(q_2,q_1,x)=1,\qquad h(x,q_t,q_{t-1})=1.
\]

Fix \(x\in X\). Consider the concatenation
\[
P^{\rm rev},\,x,\,Q^{\rm rev}
=
(p_s,\ldots,p_1,x,q_t,\ldots,q_1).
\]
Every consecutive triple internal to the two reversed displayed paths is tight after using their displayed tight orientations in reverse only through the boundary-tournament status convention? No: we do **not** assume path reversal preserves tightness. Therefore use instead the two endpoint-rooted tight paths supplied by the four-end relations only locally.

The valid conclusion is the following local obstruction.

The three-vertex path
\[
(p_2,p_1,x)
\]
is tight and the three-vertex path
\[
(x,q_t,q_{t-1})
\]
is tight. If additionally
\[
h(p_1,x,q_t)=1,
\]
then
\[
(p_2,p_1,x,q_t,q_{t-1})
\]
is a tight five-path.

Likewise
\[
(q_2,q_1,x,p_s,p_{s-1})
\]
would be a tight five-path if
\[
h(q_1,x,p_s)=1.
\]

Thus minimum-hole nonaugmentability does **not** by itself force these middle triples to be zero, because the resulting five-path need not cover the interiors of \(P,Q\). The tempting whole-path concatenation would incorrectly reverse the displayed paths.

### Correct elevation

What absolute nonaugmentability *does* give is a uniform pair of **cross-end five-path tests**:

for every \(x\in X\),
\[
h(p_1,x,q_t)=1
\Longrightarrow
(p_2,p_1,x,q_t,q_{t-1})
\text{ is tight},
\]
and
\[
h(q_1,x,p_s)=1
\Longrightarrow
(q_2,q_1,x,p_s,p_{s-1})
\text{ is tight}.
\]

If either implication fires, one hole label simultaneously consumes one endpoint edge from each base component, producing a rooted five-support spanning opposite ends of the two-cover.

If it fails, boundary antisymmetry gives the reverse cross hook:
\[
h(q_t,x,p_1)=1
\quad\text{or}\quad
h(p_s,x,q_1)=1.
\]

Hence each hole vertex carries two independent cross-end transport bits. Together with the four guaranteed end reversals, every minimum hole has a six-relation endpoint signature. These cross-end tests can be combined with the fixed-pair signature classes and the finite root-advance theorem; they are not merely arbitrary orientation data.

This addendum records the corrected local consequence and explicitly rejects the invalid inference that a displayed tight path may be reversed wholesale.
