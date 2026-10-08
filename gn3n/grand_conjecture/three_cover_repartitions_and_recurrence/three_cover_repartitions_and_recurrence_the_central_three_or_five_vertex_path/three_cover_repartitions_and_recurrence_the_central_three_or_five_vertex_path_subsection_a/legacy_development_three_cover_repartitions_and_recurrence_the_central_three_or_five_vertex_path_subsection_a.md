#  — preserved pre-item development

Write
\[
P=(p_0,\ldots ,p_m),\qquad
Q=(q_0,\ldots ,q_s).
\]
Neither
\[
(p_{m-1},p_m,x)
\quad\text{nor}\quad
(x,q_0,q_1)
\]
is tight, since either would absorb \(x\) into one path of the deletion cover. Hence
\[
(x,p_m,p_{m-1}),
\qquad
(q_1,q_0,x)
\]
are tight.

**Lemma 1.** The singleton lift and a three-cover having a central path of order three or five lie in the same component of \(\mathcal R(H)\). More precisely:
- if \((p_m,x,q_0)\) is tight, two pairwise repartitions give
\[
(p_0,\ldots ,p_{m-1})
\mid(p_m,x,q_0)
\mid(q_1,\ldots ,q_s);
\]
- if \((p_m,x,q_0)\) is non-tight, two pairwise repartitions give
\[
(p_0,\ldots ,p_{m-2})
\mid(q_1,q_0,x,p_m,p_{m-1})
\mid(q_2,\ldots ,q_s).
\]

**Proof.** In the first case, repartition
\[
Q\mid\{x\}
\]
as
\[
(x,q_0)\mid(q_1,\ldots ,q_s),
\]
then repartition \(P\mid(x,q_0)\) as the two paths displayed above.

In the second case, boundary reversal gives \((q_0,x,p_m)\) tight. First repartition
\[
Q\mid\{x\}
\]
as
\[
(q_1,q_0,x)\mid(q_2,\ldots ,q_s).
\]
Then
\[
(q_1,q_0,x,p_m,p_{m-1})
\]
is tight because its three consecutive triples are
\[
(q_1,q_0,x),\quad(q_0,x,p_m),\quad(x,p_m,p_{m-1}).
\]
Repartitioning \(P\) with the three-vertex path gives the stated five-vertex central path. \(\square\)

Thus every deleted label has a canonical bounded representative in the same component of \(\mathcal R(H)\).
