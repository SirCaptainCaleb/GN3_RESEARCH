# The four-endpoint incidence system cannot remain featureless

## Metadata

- ID: the_four_endpoint_incidence_system_cannot_remain_featureless
- Parent Section: article_vii_synthesis_and_exact_frontier
- Position: 76
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## The four-endpoint incidence system cannot remain featureless

Retain the hard rooted five-component setup
\[
Y\mid P\mid Q,
\qquad
Y=\{x,y,a,b,c\},
\]
where \(x,y\) are the distinguished holes. Assume that for each of the four exposed endpoints \(e\) of \(P,Q\), the six-set
\[
U_e=Y\cup\{e\}
\]
is non-Hamiltonian. Define
\[
A_e
=
\{r\in\{a,b,c\}:(Y-\{r\})\cup\{e\}\text{ is Hamiltonian}\}.
\]

By four-of-six, every \(A_e\) is nonempty.

Suppose, for contradiction, that none of the bounded disturbance outputs already obtained in the endpoint analysis occurs.

First, no ordinary label can belong to three of the sets \(A_e\), because that is the threefold-core branch and [[threefold_hole_preserving_cores_force_bounded_ordered_disturbance]] produces a bounded support, order disagreement, or reversing triple. Hence every ordinary label has incidence degree at most two:
\[
\deg(a),\deg(b),\deg(c)\le2.
\]
Therefore
\[
\sum_e |A_e|\le6.
\]

By [[four_endpoints_force_a_threefold_core_or_two_double_hole_equality_endpoints]], after the threefold-core branch is excluded at least two exposed endpoints satisfy
\[
|A_e|=1.
\]
Under the present no-disturbance assumption these are featureless equality endpoints, so [[featureless_equality_endpoints_have_distinct_ordinary_deletion_labels]] says that their singleton labels are distinct.

Let \(s\) be the number of singleton rows \(A_e\).

### Case 1: \(s\ge3\)

Four singleton rows are impossible because there are only three ordinary labels and singleton labels must be distinct. Thus \(s=3\).

The three singleton rows use \(a,b,c\) once each. Let \(f\) be the fourth endpoint. Since \(A_f\ne\varnothing\), choose
\[
r\in A_f.
\]
Let \(e_r\) be the singleton endpoint with
\[
A_{e_r}=\{r\}.
\]
Put
\[
C=Y-\{r\}.
\]
Then all three five-sets
\[
C\cup\{r\}=Y,\qquad
C\cup\{e_r\},\qquad
C\cup\{f\}
\]
are Hamiltonian. Lemma 5 of [[endpoint_transport_and_small_support_gluing_compatible_one_vertex_extensions]] forces an order disagreement, a Hamiltonian six-set, a Hamiltonian four-set, or a positioned reversing triple, contradicting the no-disturbance assumption.

### Case 2: \(s=2\)

Let the two singleton rows be
\[
A_{e_1}=\{a\},\qquad A_{e_2}=\{b\},
\qquad a\ne b.
\]
The other two rows are not singletons, so each has order at least two. Hence
\[
\sum_e |A_e|
\ge1+1+2+2=6.
\]
Since the total incidence is at most six, equality holds throughout. Thus:
- both remaining rows have order exactly two;
- every ordinary label has degree exactly two.

The singleton incidences already use one copy of \(a\) and one copy of \(b\), leaving incidence capacities
\[
a,\ b,\ c,\ c
\]
for the two size-two rows. Because a row is a set, each of those two rows must contain \(c\). Let their endpoints be \(f,g\). Then
\[
c\in A_f\cap A_g.
\]
Put
\[
C=Y-\{c\}.
\]
Again the three five-sets
\[
C\cup\{c\}=Y,\qquad
C\cup\{f\},\qquad
C\cup\{g\}
\]
are Hamiltonian, and the same three-extension lemma forces a bounded disturbance, contradiction.

The two cases exhaust the possibilities.

Therefore:

> **Four-endpoint synchronization theorem.** In the hard rooted five-component state, the four exposed endpoint tests cannot all remain featureless. They necessarily force one of the established bounded outputs: an order disagreement, a positioned reversing triple, or a Hamiltonian support of order at most six (including the direct endpoint-extension cases handled earlier).

Equivalently, the ordinary-deletion-label synchronization problem is closed: there is no residual incidence pattern requiring a new endpoint-core theorem.

This removes the endpoint-label synchronization branch from the Article VII frontier. The remaining obligation is the conversion of the resulting bounded disturbance into either a protected outward carrier or a spanning two-cover.
