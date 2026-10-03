# Main Line VI — three-cover repartitions and recurrence

---

## Research Line — Introduction

<!-- research_line_id: three_cover_repartitions_and_recurrence_introduction -->

Let \(H\) be a minimum counterexample to \(\operatorname{pc}(H)\le2\).

Let \(\mathcal R(H)\) be the graph whose vertices are spanning three-covers of \(H\). Two vertices of \(\mathcal R(H)\) are adjacent when one is obtained from the other by a pairwise repartition. For
\[
C=P_1\mid P_2\mid P_3
\]
define
\[
\Phi(C)=|P_1|^2+|P_2|^2+|P_3|^2.
\]

For every \(x\in V(H)\), minimality gives a deletion cover
\[
H-x=P\mid Q.
\]
Its singleton lift
\[
P\mid Q\mid\{x\}
\]
is a vertex of \(\mathcal R(H)\).

---

## Research Line — The central three- or five-vertex path

<!-- research_line_id: three_cover_repartitions_and_recurrence_the_central_three_or_five_vertex_path -->

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

---

## Research Line — Minimum potential inside a component

<!-- research_line_id: three_cover_repartitions_and_recurrence_minimum_potential_inside_a_component -->

Fix a component \(\mathcal C\) of \(\mathcal R(H)\) containing a singleton lift, and choose \(C=P_1\mid P_2\mid P_3\in\mathcal C\) minimizing \(\Phi\).

**Lemma 2.** For \(i\ne j\), every two-cover \(R\mid S\) of
\[
H[V(P_i)\cup V(P_j)]
\]
satisfies
\[
\bigl||R|-|S|\bigr|
\ge
\bigl||P_i|-|P_j|\bigr|.
\]

**Proof.** The replacement \(P_i\mid P_j\mapsto R\mid S\) is an edge of \(\mathcal R(H)\). With fixed sum \(a+b\),
\[
a^2+b^2=\frac{(a+b)^2+(a-b)^2}{2},
\]
so a smaller size difference would decrease \(\Phi\), contrary to the choice of \(C\). \(\square\)

Thus every displayed pair is a minimum-imbalance two-cover of its union.

Among triples of positive integers with fixed sum, the minimum of the sum of squares occurs exactly when the largest and smallest entries differ by at most one. Therefore the absolute minimum size multisets are
\[
\{r,r,r\},\qquad
\{r+1,r,r\},\qquad
\{r+1,r+1,r\}.
\]
Strict decrease of \(\Phi\) must eventually stop, and it can stop at one of these profiles.

---

## Research Line — Moving away from a three-vertex side

<!-- research_line_id: three_cover_repartitions_and_recurrence_moving_away_from_a_three_vertex_side -->

Suppose a state in \(\mathcal C\) has the form
\[
X\mid P\mid Q,
\qquad |X|=3,
\qquad
P=(p_1,\ldots ,p_m).
\]

If \(X\cup\{p_1\}\) is Hamiltonian, repartition \(X\mid P\) as
\[
(X\cup\{p_1\})\mid(p_2,\ldots ,p_m).
\]
The two affected orders change from \((3,m)\) to \((4,m-1)\), and
\[
16+(m-1)^2-(9+m^2)=8-2m.
\]
Hence the move strictly decreases \(\Phi\) for \(m\ge5\). The same holds at the other endpoint.

Assume neither endpoint extends \(X\). Boundary reversal then supplies reversed triples at both ends of \(P\). Comparing the six- and seven-vertex sets formed from \(X\), the two endpoints of \(P\), and one further path vertex gives one of two possibilities: a Hamiltonian four-set whose complement has a two-cover, or a Hamiltonian five-set containing both displayed endpoints of a long inherited interval. In either case the new three-cover lies in \(\mathcal C\), because it is obtained by repartitioning \(X\mid P\).

Consequently:

**Lemma 3.** From a three-vertex side adjacent to a path of order at least five, one obtains inside the same component of \(\mathcal R(H)\) either
1. a strict decrease of \(\Phi\);
2. a Hamiltonian four-vertex component with two-coverable complement; or
3. a Hamiltonian five-vertex component tied to displayed endpoints of a complementary path.

Repeated application either decreases \(\Phi\) or reaches a bounded Hamiltonian component carrying endpoint information.

---

## Research Line — Four- and five-vertex components

<!-- research_line_id: three_cover_repartitions_and_recurrence_four_and_five_vertex_components -->

Let
\[
W\mid P\mid Q
\]
be a state in \(\mathcal C\), where \(W\) is Hamiltonian and \(|W|=4\). If \(P=(p_1,\ldots ,p_m)\) with \(m\ge6\), then Hamiltonicity of \(W\cup\{p_1\}\) or \(W\cup\{p_m\}\) gives a repartition with orders \((5,m-1)\), changing the two square terms by
\[
10-2m<0.
\]

If both endpoint five-sets are non-Hamiltonian, comparison of their Hamiltonian four-vertex deletions gives two Hamiltonian four-sets
\[
\{p_1,p_m,a,b\},
\qquad
\{p_1,p_m,a,c\}
\]
sharing the three-set \(\{p_1,p_m,a\}\). Their complements have path-cover number two.

For a Hamiltonian five-vertex component \(Y\) beside a long path \(P\), the analogous endpoint test gives either a strict decrease of \(\Phi\), an equal-\(\Phi\) exchange of one vertex of \(Y\) with one endpoint of \(P\), or a tight triple through a vertex of \(Y\) reversing an edge of \(P\).

Thus a componentwise minimum of \(\Phi\) does not terminate at an arbitrary small support. It contains explicit overlap, endpoint exchange, or reversal data.

### Bounded four-support closure

The rooted small-support descent now completely classifies the bounded case in which a minimum-\(\Phi\) state contains a component of order four. Unless an order-three component or a \(4|6\) endpoint order disagreement is already present, every component order lies in \(\{4,5,6\}\). The six possible profiles containing a four then behave as follows.

- \(4|4|4\): every displayed \(4|4\) pair lies on an eight-set with at least seven complementary Hamiltonian \(4+4\) decompositions. Applying this to all three component pairs gives at least eighteen distinct nontrivial neutral neighbors at every state.
- \(4|4|5\) and \(4|5|5\): every \(4|5\) pair has a nontrivial neutral repartition, so these profiles have forced neutral cycles.
- \(4|4|6\), \(4|5|6\), and \(4|6|6\): every relevant \(4|6\) pair either exhibits an endpoint-six-set order disagreement or admits the neutral migration \(4|6\to6|4\). If no disagreement occurs, each state has at least two distinct neutral neighbors.

Thus none of the six bounded four-support size profiles remains as an unstructured terminal case. At a minimum of \(\Phi\), the entire order-four regime has already been converted into explicit neutral recurrence or an order disturbance.

---

## Research Line — Equal-potential recurrence

<!-- research_line_id: three_cover_repartitions_and_recurrence_equal_potential_recurrence -->

Equal-\(\Phi\) moves occur at the equitable size profiles and in the one-vertex transfer case. They must therefore be treated directly.

Consider first the size multiset
\[
\{r+1,r+1,r\}.
\]
An equal-\(\Phi\) repartition transfers one endpoint from a large path to the small path. If no order disagreement or smaller Hamiltonian support appears, the transfers cycle through two labels \(x,y\) and three core paths \(A,B,C\):
\[
x:A\to B,\quad y:C\to A,\quad
x:B\to C,\quad y:A\to B,\quad
x:C\to A,\quad y:B\to C.
\]
Hence both \(x\) and \(y\) extend the same end of each of \(A,B,C\).

Let \(T\) be a two-cover of
\[
H-\{x,y\}=A\cup B\cup C.
\]
Decompose its paths into maximal blocks lying in \(A,B,C\). If \(t\) is the number of edges of \(T\) joining distinct cores and \(b_A,b_B,b_C\) are the block counts, then
\[
t=b_A+b_B+b_C-2.
\]
If \(t=1\), the three cores occur as whole blocks and the same-end extensions by \(x,y\) give a two-cover of \(H\). Thus \(t\ge2\). If \(t=2\), either an edge of one displayed core has endpoints in different paths of \(T\), or one path of \(T\) leaves and later returns to the same core. If \(t\ge3\), there are already three specified edges joining distinct cores.

Therefore a neutral cycle cannot return with only the size data changed: it leaves a concrete order or support discrepancy.

The profiles \(\{r,r,r\}\) and \(\{r+1,r,r\}\) admit the same endpoint comparison. A neutral transfer with opposite endpoint realizations gives a displayed end-edge reversal by greedy endpoint transport. If all endpoint realizations use the same side, Hall's theorem on the two transferred labels and the two paths of a double deletion gives either a two-cover, two reverse triples through one end edge, or two deletion covers differing by one transferred label.

We obtain:

**Lemma 4.** At a minimum of \(\Phi\) in \(\mathcal C\), equal-potential motion produces at least one of:
1. an order disagreement;
2. an edge of a comparison cover joining distinct displayed supports;
3. an inherited path edge whose endpoints lie in different paths of a comparison cover;
4. two separated blocks from one displayed support on one comparison path;
5. a tight triple reversing a displayed edge;
6. two Hamiltonian five-sets with a common four-set;
7. a one-vertex transfer whose endpoint realizations all use the same side.

These are the local recurrence residues.

---

## Research Line — Several deleted labels in one component

<!-- research_line_id: three_cover_repartitions_and_recurrence_several_deleted_labels_in_one_component -->

There is a second argument that does not follow one trajectory.

Two deletion covers are compatible when, after deleting both omitted labels, they induce the same support partition and the same relative order on every common support.

**Lemma 5.** If deletion covers \(F_x\) of \(H-x\) and \(F_y\) of \(H-y\) are compatible, their singleton lifts lie on one edge of \(\mathcal R(H)\).

**Proof.** On \(H-\{x,y\}\), compatibility gives two common ordered supports, say \(A,B\). In \(F_x\), the restored vertex \(y\) is inserted into one of them; in \(F_y\), the restored vertex \(x\) must be inserted into the same support, since insertion into the other support would produce two disjoint Hamiltonian supports covering \(H\). Suppose the common support is \(A\). Then the two singleton lifts have the form
\[
(A+y)\mid B\mid\{x\},
\qquad
(A+x)\mid B\mid\{y\}.
\]
Replacing
\[
(A+y)\mid\{x\}
\]
by
\[
(A+x)\mid\{y\}
\]
is a pairwise repartition. \(\square\)

Hence every connected component of the compatibility graph of chosen deletion covers maps into one connected component of \(\mathcal R(H)\).

By Lemma 1, this component then contains, for every deleted label in the compatibility component, its singleton lift and its central three- or five-vertex representative. Thus a large compatibility component produces many differently rooted bounded states in one component of \(\mathcal R(H)\).

If the compatibility graph has no large connected component, choosing labels from different components produces a large family of pairwise incompatible deletion covers. This is the complementary structural case and belongs to the deletion-cover argument rather than the recurrence argument.

---

## Research Line — Two distinct remaining lemmas

<!-- research_line_id: three_cover_repartitions_and_recurrence_two_distinct_remaining_lemmas -->

The one-trajectory and many-root arguments require different conclusions.

**Remaining Lemma A.** Let \(\mathcal C\) contain a singleton lift and let \(C\in\mathcal C\) minimize \(\Phi\). If \(C\) has one of the recurrence residues in Lemma 4, then either \(H\) has a two-cover, or \(\mathcal C\) contains a three-cover of smaller \(\Phi\), or there is an equal-\(\Phi\) move that strictly decreases a well-founded secondary integer.

A proof rules out recurrence in one component.

**Remaining Lemma B.** There is a constant \(k\) such that if one component of \(\mathcal R(H)\) contains central bounded representatives associated with \(k\) distinct deleted labels, then either \(H\) has a two-cover, that component contains a three-cover of smaller \(\Phi\), or two of the rooted representatives combine to give a spanning ordering of defect span at most \(2\).

A proof rules out congestion of many deletion roots without requiring a secondary invariant on every equal-\(\Phi\) move.

These statements are genuinely different. Lemma A orients one trajectory. Lemma B uses several rooted neighborhoods simultaneously.

---

## Research Line — Appendix. Why finiteness is insufficient

<!-- research_line_id: three_cover_repartitions_and_recurrence_appendix_why_finiteness_is_insufficient -->

A finite sequence of equal-\(\Phi\) pairwise repartitions may return to its initial three-cover. Finiteness alone therefore does not make neutral motion terminate. A valid recurrence argument needs either a secondary quantity that decreases on every selected neutral move or a contradiction obtained from the oriented data accumulated around a cycle.

Boundary reversal also remains local:
\[
(a,b,c)\text{ non-tight}
\quad\Longleftrightarrow\quad
(c,b,a)\text{ tight}.
\]
It does not justify reversing a path or cyclically rotating a triple. Every recurrence argument above therefore keeps the displayed path orders through each pairwise repartition.

---

## Research Line — Canonical references

<!-- research_line_id: three_cover_repartitions_and_recurrence_canonical_references -->

- [[fivefence01]] — Five-set fence: bare complement witnesses are not closure
