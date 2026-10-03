# Main Line II — quadratic potential and pairwise repartition

---

## Research Line — Introduction

<!-- research_line_id: quadratic_potential_and_pairwise_repartition_introduction -->

Let \(H\) be a minimum counterexample to \(\operatorname{pc}(H)\le2\). For each \(x\in V(H)\), choose a deletion cover
\[
H-x=P\mid Q.
\]
The singleton lift \(P\mid Q\mid\{x\}\) is a three-cover of \(H\).

Let \(\mathcal R(H)\) be the graph whose vertices are three-covers of \(H\). Two three-covers are adjacent when one is obtained from the other by a pairwise repartition: two displayed paths are replaced by a two-cover of their union and the third path is unchanged. Since \(H\) has no two-cover, every such repartition again has three nonempty paths.

For a three-cover \(C=P_1\mid P_2\mid P_3\), define
\[
\Phi(C)=|P_1|^2+|P_2|^2+|P_3|^2.
\]
Fix a connected component of \(\mathcal R(H)\) containing a singleton lift and choose \(C\) in that component with minimum \(\Phi\).

---

## Research Line — Pairwise extremality

<!-- research_line_id: quadratic_potential_and_pairwise_repartition_pairwise_extremality -->

**Lemma 1.** Let \(a+b=s\) and \(a',b'>0\) with \(a'+b'=s\). Then
\[
(a')^2+(b')^2<a^2+b^2
\]
if and only if
\[
|a'-b'|<|a-b|.
\]

**Proof.** Since
\[
a^2+b^2=\frac{s^2+(a-b)^2}{2},
\]
the assertion follows. \(\square\)

**Corollary 2.** If \(C=P_1\mid P_2\mid P_3\) minimizes \(\Phi\) in its component of \(\mathcal R(H)\), then for \(i\ne j\), every two-cover \(R\mid S\) of
\[
H[V(P_i)\cup V(P_j)]
\]
satisfies
\[
\bigl||R|-|S|\bigr|\ge\bigl||P_i|-|P_j|\bigr|.
\]

**Proof.** Replacing \(P_i\mid P_j\) by \(R\mid S\) is a pairwise repartition. A smaller size difference would decrease \(\Phi\) by Lemma 1. \(\square\)

Thus every displayed pair is as balanced as possible among its two-covers. Further information must come from path order, endpoint position, or comparison with another cover.

---

## Research Line — Absolute minima

<!-- research_line_id: quadratic_potential_and_pairwise_repartition_absolute_minima -->

**Lemma 3.** Among triples of positive integers with fixed sum \(n\), the minimum of \(a^2+b^2+c^2\) is attained exactly when the largest and smallest entries differ by at most one.

**Proof.** If \(a\ge b+2\), replacing \((a,b)\) by \((a-1,b+1)\) changes the sum of squares by
\[
-2(a-b)+2<0.
\]
Repeated balancing terminates exactly when no two entries differ by at least \(2\). \(\square\)

The possible size multisets at an absolute minimum are
\[
\{r,r,r\},\qquad \{r+1,r,r\},\qquad \{r+1,r+1,r\}.
\]
No strict decrease of \(\Phi\) is possible from these sizes while three nonempty paths remain.

### Small-component consequences

Two elementary balancing facts substantially narrow the possible minimum states. By [[toolkit_minimal_three_covers_have_no_components_of_order_one_or_two]], every component of a minimum-(\Phi\) three-cover has order at least three.

There is a further restriction at order three. Let \(T\mid C\) be two displayed components with \(|T|=3\) and \(|C|=s\). If \(s\ge6\), then [[three_vertex_component_long_neighbor_rotation01]] gives a strict pairwise decrease of \(\Phi\), contradicting minimality. Hence a three-vertex component can occur at a minimum only when each of the other two components has order at most five. In particular, for \(|V(H)|\ge14\), every component of a minimum-(\Phi\) three-cover has order at least four.

At the boundary value \(s=5\), the same lemma gives an explicit equal-(\Phi\) rotation
\[
3\mid5\longleftrightarrow5\mid3
\]
whenever the direct endpoint enlargement to a Hamiltonian four-set is unavailable. Thus the smallest surviving component is accompanied by a concrete neutral recurrence, not an unstructured exceptional case.

---

## Research Line — A block-count identity

<!-- research_line_id: quadratic_potential_and_pairwise_repartition_a_block_count_identity -->

Let \(A,B,C\) be disjoint vertex sets and let \(T\) be a two-cover of their union. Decompose the paths of \(T\) into maximal nonempty blocks contained in one of \(A,B,C\). If \(b_A,b_B,b_C\) are the corresponding block counts and \(t\) is the number of edges of the paths of \(T\) whose endpoints lie in different sets among \(A,B,C\), then
\[
t=b_A+b_B+b_C-2.
\]

Indeed, deleting those \(t\) edges from two paths produces \(t+2\) blocks. Hence \(t\ge1\). If \(t=1\), each displayed set occurs as one block. If \(t=2\), the block counts are \((2,1,1)\) in some order. If the two blocks of the split set lie in different paths of \(T\), an edge of any displayed Hamilton path on that set has endpoints in different paths of \(T\). If the two blocks lie in the same path of \(T\), a nonempty block from another displayed set lies between them.

---

## Research Line — The size profile \(\{r+1,r+1,r\}\)

<!-- research_line_id: quadratic_potential_and_pairwise_repartition_the_size_profile_r1r1r -->

**Lemma 4.** Suppose a minimum-\(\Phi\) level in one component of \(\mathcal R(H)\) has size multiset \(\{r+1,r+1,r\}\), \(r\ge3\). Assume that an equal-\(\Phi\) pairwise repartition never gives a two-cover, a strict decrease of \(\Phi\), an order disagreement, or a Hamiltonian support of order four or five whose complement has path-cover number two. Then there are disjoint tight paths \(A,B,C\), each of order \(r\), and distinct vertices \(x,y\) such that both \(x\) and \(y\) extend the same end of each of \(A,B,C\).

For every two-cover \(T\) of
\[
H-\{x,y\}=A\cup B\cup C,
\]
at least one of the following holds:
1. a path of \(T\) and one of \(A,B,C\) have an order disagreement;
2. \(T\) has at least three edges whose endpoints lie in different sets among \(A,B,C\);
3. an edge of one of \(A,B,C\) has endpoints in different paths of \(T\);
4. one path of \(T\) contains two nonempty blocks from one of \(A,B,C\) separated by a nonempty block from another.

**Proof.** At this size profile, an equal-\(\Phi\) repartition can only transfer one endpoint from a path of order \(r+1\) to the path of order \(r\). Under the hypotheses, both large paths admit such a transfer, and the transfers use the same end of the receiving path; opposite ends or different inherited orders give one of the excluded conclusions.

Write one state as
\[
(x,A)\mid B\mid(y,C),
\]
with all chosen transfers at the initial end. After one transfer, its reverse is one of the two available equal-\(\Phi\) moves, so choosing the other move forces
\[
x:A\to B,\quad y:C\to A,\quad x:B\to C,\quad
y:A\to B,\quad x:C\to A,\quad y:B\to C.
\]
After six moves the support partition returns to the initial state. The first three states and their unused reverse moves show that both \(x\) and \(y\) initial-extend each of \(A,B,C\). The terminal-end case is symmetric.

Now let \(T\) be a two-cover of \(A\cup B\cup C\). If there is an order disagreement, (1) holds. Otherwise let \(t\) be the number of edges of \(T\) joining different cores. If \(t=1\), the block-count identity gives one block in each core. One path of \(T\) is the concatenation of two whole cores and the other is the third core. Prepending \(x\) to the first path and \(y\) to the second gives a two-cover of \(H\), a contradiction. Thus \(t\ge2\). If \(t\ge3\), (2) holds. If \(t=2\), Section 3 gives (3) or (4). \(\square\)

---

## Research Line — The size profile \(\{r+1,r,r\}\)

<!-- research_line_id: quadratic_potential_and_pairwise_repartition_the_size_profile_r1rr -->

Let \(A\mid B\mid C\) have orders \(r+1,r,r\), and let \(x,y\) be the endpoints of \(A\).

Suppose first that \(x\) extends both \(B\) and \(C\). For a two-cover \(T\) of \(H-x\), use the partition
\[
(A-\{x\})\mid B\mid C.
\]
If \(T\) had only one edge joining different classes, its three blocks could be restored with \(x\) to produce a two-cover of \(H\). Hence there are at least two such edges. With exactly two, Section 3 gives either an inherited displayed edge whose endpoints lie in different paths of \(T\), or two blocks of one displayed support separated by a block of another.

Suppose instead that \(x\) extends \(B\) and \(y\) extends \(C\), while the opposite extensions are unavailable. If either Hamiltonian extension reverses the order of two core vertices, there is an order disagreement. Otherwise the extensions are obtained by inserting \(x\) and \(y\) into the displayed orders of \(B\) and \(C\).

Write \(A=(x,M,y)\), and let \(T\) be a two-cover of \(H-\{x,y\}\). If at least two edges of \(T\) join distinct sets among \(M,B,C\), Section 3 again gives the preceding alternatives. If there is only one, the three sets occur as whole blocks on two paths. The insertion positions of \(x\) into \(B\) and \(y\) into \(C\) must then be adjacent to the unique join between two blocks; otherwise both insertions can be made while leaving the join unchanged, giving a two-cover of \(H\). The triple needed to perform both insertions at the remaining join is therefore non-tight, and its boundary flip is tight.

Hence:

**Lemma 5.** At a minimum of \(\Phi\) with size multiset \(\{r+1,r,r\}\), one obtains an order disagreement, an edge joining distinct displayed supports in a comparison cover, an inherited displayed edge split between the two paths of a comparison cover, two blocks of one displayed support separated by another, or a reverse tight triple at a displayed join.

---

## Research Line — The size profile \(\{r,r,r\}\)

<!-- research_line_id: quadratic_potential_and_pairwise_repartition_the_size_profile_rrr -->

Let \(A\mid B\mid C\) have equal orders. Delete an endpoint of one displayed path and compare a deletion cover with the inherited three-part partition. The block count of Section 3 applies.

If a comparison cover uses one edge joining different displayed sets, the three sets occur as whole blocks. Restoring the deleted endpoint at its displayed end gives either a two-cover or an insertion that is impossible in the inherited order. Compare deletion covers at both endpoints of the same displayed path. If both preserve the core order, their insertion positions are equal, adjacent, or separated. Equal compatible positions or separated positions give a simultaneous insertion and a two-cover. Adjacent positions force the boundary-flipped triple at the intervening core vertex. Therefore:

**Lemma 6.** At a minimum of \(\Phi\) with size multiset \(\{r,r,r\}\), one obtains an order disagreement, at least two explicitly located edges between displayed classes in a comparison cover, or a reverse tight triple at a displayed join.

The three equitable size profiles therefore all produce ordered information after numerical descent stops.

---

## Research Line — Reversal of a displayed end edge

<!-- research_line_id: quadratic_potential_and_pairwise_repartition_reversal_of_a_displayed_end_edge -->

Let
\[
H-x=P\mid Q,\qquad P=(p_0,\ldots ,p_m),
\]
and suppose another Hamilton order of \(V(P)\) contains the reverse of the terminal edge \(p_{m-1}p_m\). Write it as
\[
A,p_m,p_{m-1},B
\]
and put \(t=|A|\), \(N=|P|\). Boundary reversal at the deleted vertex supplies the tight triple needed to place \(x\) before the suffix beginning at \(p_m\). The resulting pairwise repartition has three cases. Direct calculation of the two changed square terms gives
\[
\Delta\Phi=-2(t-1)(N-t).
\]

If \(t=0\), the repartition gives a two-cover. If \(2\le t\le N-2\), \(\Phi\) decreases strictly. If \(t=1\), \(\Phi\) is unchanged and exactly one vertex is transferred between the two non-singleton supports. The initial-edge case is symmetric.

Thus a minimum of \(\Phi\) leaves only the one-vertex transfer.

**Lemma 7.** If the transferred vertex can occur at opposite ends in its two Hamiltonian realizations, then comparison of the two orders gives a reversal of a displayed end edge. Hence a persistent equal-\(\Phi\) transfer has only two forms: the transferred vertex is internal in every relevant Hamilton order of one augmented support, or every endpoint realization places it on the same side.

**Proof.** Opposite endpoint positions agree on the inherited core until the first position at which one order has already placed the transferred vertex and the other has not. At that position the two consecutive inherited core vertices occur in opposite local orders, producing the displayed end-edge reversal. \(\square\)

---

## Research Line — Two same-side extenders

<!-- research_line_id: quadratic_potential_and_pairwise_repartition_two_same_side_extenders -->

Let \(x,y\) be two labels that can occur only at the same side of the relevant core paths, and let \(R\mid S\) be a two-cover of \(H-\{x,y\}\). Form a bipartite graph with left class \(\{x,y\}\) and right class \(\{R,S\}\), joining a label to a path when adjoining the label at the prescribed end gives a Hamiltonian path.

A perfect matching gives a two-cover of \(H\). If no perfect matching exists, Hall's theorem gives one of two possibilities:
1. one of \(R,S\) is adjacent to neither \(x\) nor \(y\);
2. one of \(x,y\) is adjacent to neither \(R\) nor \(S\).

In the first case, the two failed end insertions give two reverse tight triples through one displayed end edge. In the second, deleting the blocked label gives two deletion covers that differ by transferring the other label.

Two reverse triples through one end edge force a bounded common-core configuration. For each reverse triple, record pairs of exterior labels whose simultaneous extension fails. Each failure graph is triangle-free: three pairwise failures force, by applying boundary reversal to the three corresponding insertion triples, a Hamiltonian order on one of the three five-vertex extensions. On six exterior labels, if no pair succeeds for both reverse triples, the edges of \(K_6\) are covered by two triangle-free graphs. Coloring each edge by one graph containing it gives a two-coloring of \(K_6\) without a monochromatic triangle, contradicting \(R(3,3)=6\). Hence two labels simultaneously extend both reverse triples, producing two Hamiltonian five-vertex supports with a common four-vertex core.

Their six-vertex union has three relevant possibilities: it is Hamiltonian; two Hamiltonian vertex deletions are adjacent; or the Hamiltonian vertex deletions form a matching. These give, respectively, a Hamiltonian six-vertex support, overlapping Hamiltonian four- and five-vertex supports, or a fixed matching-block configuration. Each alternative preserves the common four-vertex core.

---

## Research Line — The remaining lemma

<!-- research_line_id: quadratic_potential_and_pairwise_repartition_the_remaining_lemma -->

The quadratic-potential argument is reduced to the following statement.

**Remaining Lemma.** Let \(C\) minimize \(\Phi\) in the component of \(\mathcal R(H)\) containing a singleton lift. Suppose one of the following occurs:
- two relevant Hamiltonian paths have an order disagreement;
- a comparison two-cover contains an edge joining distinct displayed supports;
- an edge of a displayed core has endpoints in different paths of a comparison cover;
- one comparison path contains two separated blocks from the same displayed core;
- a reverse tight triple occurs at a displayed join or end edge;
- two Hamiltonian five-vertex supports share a four-vertex core;
- two covers of the same deletion differ by one transferred vertex whose endpoint realizations all use the same side;
- a relevant label is internal in every Hamiltonian order of an augmented support.

Then \(H\) has a two-cover or a spanning ordering of defect span at most \(2\).

A proof of this lemma completes the argument, since strict decrease of \(\Phi\) is impossible at the chosen state and Sections 4–8 describe the equal-\(\Phi\) alternatives.

---

## Research Line — Appendix. Pairwise balancing is insufficient

<!-- research_line_id: quadratic_potential_and_pairwise_repartition_appendix_pairwise_balancing_is_insufficient -->

Suppose one attempted to prove that every imbalanced two-coverable induced subtournament admits a more balanced two-cover, without using the third path. Iterating such a statement would refine every two-cover until its component orders differed by at most one. Conversely, a theorem guaranteeing such a balanced refinement immediately gives the pairwise improvement whenever the displayed sizes differ by at least two. Thus a purely two-support balancing argument is as strong as the general balanced-refinement problem for two-coverable boundary tournaments. The third path, a deletion label, or comparison of path orders is therefore essential to this method.
