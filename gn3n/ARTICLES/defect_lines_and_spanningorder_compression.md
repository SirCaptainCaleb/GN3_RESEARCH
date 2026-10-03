# Article III — defect lines and spanning-order compression

---

## Section — Introduction

<!-- section_id: defect_lines_and_spanning_order_compression_introduction -->

Let \(H\) be a minimum counterexample to \(\operatorname{pc}(H)\le2\).

For a spanning ordering \(\pi=(v_1,\ldots ,v_n)\), call \(i\), \(2\le i\le n-1\), a defect center when
\[
(v_{i-1},v_i,v_{i+1})
\]
is non-tight. The defect line \(L_\pi\) has vertices \(1,\ldots ,n-1\), representing the cuts between consecutive vertices, and has the edge \(\{i-1,i\}\) for each defect center \(i\).

Let \(c(\pi)\) be the minimum number of consecutive intervals into which \(\pi\) can be partitioned so that each interval is a tight path.

---

## Section — The defect-line identity

<!-- section_id: defect_lines_and_spanning_order_compression_the_defect_line_identity -->

**Lemma 1.**
\[
c(\pi)=1+\tau(L_\pi)=1+\nu(L_\pi).
\]

**Proof.** A set \(C\) of cuts partitions \(\pi\) into tight paths exactly when, for every defect center \(i\), at least one of the adjacent cuts \(i-1,i\) belongs to \(C\). Thus \(C\) is a vertex cover of \(L_\pi\), and
\[
c(\pi)=1+\tau(L_\pi).
\]
The graph \(L_\pi\) is a subgraph of a path and is therefore bipartite, so \(\tau(L_\pi)=\nu(L_\pi)\). \(\square\)

Hence \(H\) has a two-cover if and only if some spanning ordering satisfies
\[
\nu(L_\pi)\le1.
\]

If the defect centers occur in maximal consecutive runs of lengths \(r_1,\ldots ,r_s\), then
\[
\nu(L_\pi)=\sum_{j=1}^s\left\lceil\frac{r_j}{2}\right\rceil.
\]
In particular, \(c(\pi)=3\) exactly when there is one run of length three or four, or two separated runs, each of length one or two.

---

## Section — Defect span three is a deletion-cover ordering

<!-- section_id: defect_lines_and_spanning_order_compression_defect_span_three_is_a_deletion_cover_ordering -->

The defect span of \(\pi\) is \(0\) if there is no defect center and otherwise is
\[
\max D(\pi)-\min D(\pi)+1.
\]

A deletion cover
\[
H-x=P\mid Q
\]
gives the spanning ordering \(P,x,Q\), whose possible defect centers are the three positions adjacent to the join. The two outer join triples are non-tight, since otherwise \(x\) could be appended to one of the two paths and \(H\) would have a two-cover.

Conversely:

**Lemma 2.** If \(\pi=(v_1,\ldots ,v_n)\) has defect span \(3\), and \(i\) is its leftmost defect center, then with
\[
x=v_{i+1},\qquad
P=(v_1,\ldots ,v_i),\qquad
Q=(v_{i+2},\ldots ,v_n)
\]
the paths \(P,Q\) form a deletion cover of \(H-x\), and \(\pi=P,x,Q\).

**Proof.** No defect center occurs before \(i\) or after \(i+2\). Hence every internal triple of \(P\) and \(Q\) is tight. \(\square\)

There are two cases. If the middle join triple
\[
(v_i,x,v_{i+2})
\]
is tight, the central three vertices form a tight path. If it is non-tight, then all three join triples are non-tight, and boundary reversal gives the tight five-vertex path
\[
(v_{i+3},v_{i+2},x,v_i,v_{i-1})
\]
whenever the displayed vertices exist.

Thus every minimum-span ordering is a deletion-cover ordering whose central part is a Hamiltonian three-set or a Hamiltonian five-set.

---

## Section — Transport with the deleted vertex fixed

<!-- section_id: defect_lines_and_spanning_order_compression_transport_with_the_deleted_vertex_fixed -->

Assume the middle join is tight. Write
\[
H-x=P\mid Q.
\]
Move the last vertex of \(P\) across \(x\) toward \(Q\). If all new consecutive triples are tight, this produces another deletion cover of the same \(H-x\), with component orders \((|P|-1,|Q|+1)\). At the first failed move, the failed triple reverses and combines with the inherited neighboring triples to give a Hamiltonian four-set whose complement is covered by the remaining prefix and suffix.

**Lemma 3.** Repeating this move in one direction terminates with either
1. a deletion cover of the same \(H-x\) having one path of order \(3\); or
2. a Hamiltonian four-set whose complement has a two-cover.

**Proof.** Every successful move decreases the chosen component order by one and preserves \(x\). The move can therefore succeed at most until that component has order \(3\). If it fails earlier, the preceding paragraph gives (2). \(\square\)

The three-vertex-side case contains a stronger transport.

Let
\[
P=(p_0,p_1,p_2),\qquad Q=(q_0,\ldots ,q_s),\qquad
X=V(P)\cup\{x\}.
\]

**Lemma 4.** Suppose \(s\ge6\). Then at least two vertices \(z\in X\) have all six tight triples
\[
(q_1,q_0,z),\ (q_2,q_1,z),\ (q_3,q_2,z),
\]
\[
(z,q_s,q_{s-1}),\ (z,q_{s-1},q_{s-2}),\ (z,q_{s-2},q_{s-3}).
\]
For either such \(z\), there is a sequence of pairwise repartitions in which \(z\) is retained while a two-coverable complementary support is transported from the left end of \(Q\) to the right end.

**Proof.** The set \(X\) is non-Hamiltonian, since otherwise \(X\mid Q\) would two-cover \(H\). The sets \(X\cup\{q_0\}\) and \(X\cup\{q_s\}\) are also non-Hamiltonian, because their complements are inherited tight paths.

Consider \(X\cup\{q_0,q_s\}\). Its two deletions by \(q_0,q_s\) are non-Hamiltonian. The remaining four vertex deletions are Hamiltonian; otherwise the six-vertex Hamiltonian-deletion count would be violated. Hence, for every \(z\in X\),
\[
(X-\{z\})\cup\{q_0,q_s\}
\]
is Hamiltonian. Its complement
\[
\{z,q_1,\ldots ,q_{s-1}\}
\]
cannot be Hamiltonian, so \(z\) cannot be inserted at either end of the inherited path \((q_1,\ldots ,q_{s-1})\). Boundary reversal gives
\[
(q_2,q_1,z),\qquad(z,q_{s-1},q_{s-2}).
\]

Apply the same argument to the six-sets \(X\cup\{q_0,q_1\}\) and \(X\cup\{q_{s-1},q_s\}\). At least three choices of \(z\in X\) work on each side, so at least two choices work on both sides. Their complementary non-Hamiltonian paths give the four additional tight triples displayed above.

For transport, use the four seven-vertex sets
\[
X\cup\{q_0,q_1,q_2\},\
X\cup\{q_0,q_1,q_s\},\
X\cup\{q_0,q_{s-1},q_s\},\
X\cup\{q_{s-2},q_{s-1},q_s\}.
\]
For one such set \(W\), join \(a,b\in W\) when \(W-\{a,b\}\) is Hamiltonian. Each vertex has at least four neighbors, since deleting it leaves a six-set with at least four Hamiltonian five-vertex deletions. Consecutive graphs share six vertices; after removing the unique outside vertex each leaves at least eight edges on the common six-set, so the two edge sets intersect because \(8+8>15\). If \(z\) is one of the two vertices found above, it has at least three neighbors in each common five-vertex neighborhood, so the shared edge can be chosen incident with \(z\).

Every such edge \(ab\) yields a Hamiltonian five-set and a complementary support equal to an inherited interval of \(Q\) together with \(\{a,b\}\). The complement is non-Hamiltonian but is covered by that interval and the two-vertex path \((a,b)\). Following the shared edges gives the required sequence. \(\square\)

---

## Section — From transport to an end-edge reversal

<!-- section_id: defect_lines_and_spanning_order_compression_from_transport_to_an_end_edge_reversal -->

The lower states in Lemma 4 have path orders \(4,3,m\), with the same long path retained. Repartitioning the four- and three-vertex sides may strictly decrease the quadratic potential
\[
\Phi(P_1\mid P_2\mid P_3)=|P_1|^2+|P_2|^2+|P_3|^2.
\]
If two adjacent lower states admit the same strict decrease, a state of smaller \(\Phi\) lies in the same component of the pairwise-repartition graph.

Assume no such synchronized decrease is available. Fix the transported vertex \(z\) and one seven-vertex set \(W\). Let \(\Omega\) be the graph in the proof of Lemma 4. We have \(\deg_\Omega(z)\ge4\). If the degree is larger, two adjacent choices give synchronized descent. If the degree is four, let \(u,v\) be the two nonneighbors of \(z\). Then
\[
F=W-\{z,u\}
\]
is a non-Hamiltonian five-set with at least four Hamiltonian vertex deletions.

Choose Hamilton paths on these four deletions. If all common vertices had the same relative order in every pair, the orders would combine to a Hamilton path of \(F\). Hence two have an order disagreement. A minimal such pair contains either a common edge traversed in opposite directions or a tight triple reversing an edge of one of the paths. A tight-cycle-only alternative is impossible inside a non-Hamiltonian edge-orderable five-set. In the common-edge case, one adjacent triple of the other Hamilton path reverses that edge. Therefore:

**Lemma 5.** If synchronized strict decrease is unavailable, a three-cover in the same component contains a Hamiltonian four-path \(K\) and a tight triple on the surrounding five vertices that reverses an edge of \(K\).

If the reversed edge is an end edge of \(K\), nothing further is needed. If it is the internal edge, the four vertices of \(K\) together with the reversing triple contain either a Hamiltonian four-set or an edge-orderable matching-block \(K_4\). In the Hamiltonian case the complement has path-cover number two. In the matching-block case, adjoining an endpoint of the long path produces a Hamiltonian support of order four or five containing that endpoint; its complement again has path-cover number two.

Hence:

**Proposition 6.** The fixed-deletion transport produces one of:
1. a strict decrease of \(\Phi\) inside the same component of the pairwise-repartition graph;
2. a reversal of an end edge of a displayed Hamiltonian four-path;
3. a Hamiltonian support of order four or five containing a displayed endpoint of the complementary path, with two-coverable complement.

---

## Section — An endpoint-rooted Hamiltonian four-set

<!-- section_id: defect_lines_and_spanning_order_compression_an_endpoint_rooted_hamiltonian_four_set -->

Suppose
\[
W\mid P\mid Q
\]
is a three-cover with \(|W|=4\), and let
\[
P=(p_1,\ldots,p_m),\qquad m\ge2.
\]

**Lemma 7.** There are distinct vertices \(x,y\in W\) such that
\[
\{p_1,p_m,x,y\}
\]
is a Hamiltonian four-set. Its complement is non-Hamiltonian and has path-cover number two.

**Proof.** Choose any three distinct vertices \(a,b,c\in W\). In the five-set
\[
F=\{p_1,p_m,a,b,c\},
\]
apply the endpoint-pair Hamiltonicity theorem with prescribed pair \(\{p_1,p_m\}\). Some Hamiltonian four-subset of \(F\) contains both prescribed vertices, so it has the form
\[
\{p_1,p_m,x,y\}
\]
for distinct \(x,y\in\{a,b,c\}\). The third cover component \(Q\) is nonempty, so this Hamiltonian four-set is proper. Minimum-counterexample calculus therefore gives a two-cover of its complement. \(\square\)

Thus every four-set state beside a nontrivial path already contains a bounded Hamiltonian support carrying both displayed endpoints of that path. No lower bound such as \(m\ge6\), endpoint-extension case split, or finite-order remainder is needed.

---

## Section — A Hamiltonian five-set beside a long path

<!-- section_id: defect_lines_and_spanning_order_compression_a_hamiltonian_five_set_beside_a_long_path -->

Let
\[
X\mid P\mid Q
\]
be a three-cover with \(|X|=5\) and \(P=(p_1,\ldots ,p_m)\), \(m\ge7\).

**Lemma 8.** One of the following holds:
1. a pairwise repartition of \(X\mid P\) strictly decreases \(\Phi\);
2. a pairwise repartition preserves the component orders \(\{5,m\}\) and replaces one vertex of \(X\) by an endpoint of \(P\);
3. a tight triple containing a vertex of \(X\) reverses an edge of the displayed path \(P\).

**Proof.** If an endpoint transfer makes the two component orders more balanced, (1) holds. Otherwise there is \(x\in X\) such that, with \(D=X-\{x\}\), both
\[
D\cup\{p_1\},\qquad D\cup\{p_m\}
\]
are Hamiltonian. If \((V(P)-\{p_1\})\cup\{x\}\) or \((V(P)-\{p_m\})\cup\{x\}\) is Hamiltonian, pair it with the corresponding Hamiltonian five-set to obtain (2). If neither is Hamiltonian, \(x\) cannot be inserted at either end of the displayed path. Testing insertion positions along \(P\), the first unavailable internal insertion gives, by boundary reversal, a tight triple through \(x\) that reverses the corresponding displayed edge. \(\square\)

Thus both central cases reduce to the same ordered objects.

---

## Section — The remaining lemma

<!-- section_id: defect_lines_and_spanning_order_compression_the_remaining_lemma -->

### Two-cut normal form

The defect-line formulation has an exact normalization for three-covers.

**Lemma 9 (two-cut normal form).** Let \(H\) be a minimum counterexample. Let
\[
C=P_1\mid P_2\mid P_3
\]
be any three-cover, and let \(\pi\) be the spanning ordering obtained by concatenating the three displayed path orders. If \(a<b\) are the two cuts between consecutive components, then
\[
\nu(L_\pi)=2,
\]
and \(\{a,b\}\) is a minimum vertex cover of \(L_\pi\).

Conversely, if \(\pi=(v_1,\ldots ,v_n)\) is any spanning ordering with \(\nu(L_\pi)=2\), then every minimum vertex cover \(\{a,b\}\), \(a<b\), of \(L_\pi\) cuts \(\pi\) into the three tight paths
\[
(v_1,\ldots ,v_a),\qquad
(v_{a+1},\ldots ,v_b),\qquad
(v_{b+1},\ldots ,v_n).
\]

**Proof.** The two component boundaries of \(C\) form a set of cuts whose removal partitions \(\pi\) into three tight intervals. Equivalently, the corresponding two vertices of the defect line meet every defect edge. Hence
\[
\tau(L_\pi)\le2.
\]
By the defect-line identity,
\[
\nu(L_\pi)=\tau(L_\pi)\le2.
\]
If \(\nu(L_\pi)\le1\), the same identity gives \(c(\pi)\le2\), so \(H\) has a two-cover, contrary to the choice of \(H\). Thus \(\nu(L_\pi)=2\), and the two displayed cuts form a minimum vertex cover.

Conversely, if \(\{a,b\}\) is a vertex cover of \(L_\pi\), then no defect center lies wholly inside any of the three intervals determined by the cuts after positions \(a\) and \(b\). Each interval is therefore a tight path. Since \(\tau(L_\pi)=\nu(L_\pi)=2\), every minimum vertex cover has exactly two vertices, giving the asserted three-cover. \(\square\)

This identifies the pairwise-repartition problem with a two-cut defect problem. Every three-cover state in a minimum counterexample carries two necessary defect-cover cuts; obtaining a two-cover is exactly the problem of finding a spanning ordering whose defect line can be covered by one cut. Thus the remaining compression step should be read as eliminating one of the two necessary cuts, rather than merely shortening the geometric span of the visible defects.

### Neutral end-edge reversal is a deletion-root exchange

The neutral residue of an end-edge reversal has additional structure when it starts from a singleton lift.

**Lemma 10 (root exchange).** Let
\[
H-x=P\mid Q
\]
be a deletion cover of a minimum counterexample, and suppose its singleton lift
\[
P\mid\{x\}\mid Q
\]
minimizes \(\Phi\) in its component of the pairwise-repartition graph. Let \(P\) have a Hamilton order
\[
R=(A,p_m,p_{m-1},B)
\]
containing the reversed terminal edge \((p_m,p_{m-1})\) of a displayed order of \(P\). Then either \(H\) has a two-cover, or \(|A|=1\). In the latter case, writing \(A=(a)\),
\[
H-a=(x,p_m,p_{m-1},B)\mid Q
\]
is a deletion cover at \(a\).

Moreover, after choosing \(R\) as the order of the first support in the deletion cover at \(x\), the deletion covers at \(x\) and \(a\) are compatible on their common domain. They share the support \(Q\), and on the other common support
\[
P-\{a\}=\{p_m,p_{m-1}\}\cup B
\]
they induce the same order \((p_m,p_{m-1},B)\). Equivalently, the omitted labels \(a\) and \(x\) occupy the same initial insertion slot of this common ordered support.

**Proof.** The displayed end-edge reversal lemma gives a two-cover, a strict decrease of \(\Phi\), or the neutral case \(|A|=1\). The strict-decrease alternative is impossible at the chosen minimum. In the neutral case boundary reversal gives
\[
(x,p_m,p_{m-1})
\]
tight, and the suffix \((p_m,p_{m-1},B)\) is inherited from the Hamilton order \(R\). Hence
\[
(x,p_m,p_{m-1},B)
\]
is a tight path. Together with \(Q\) it covers \(H-a\), proving the deletion-cover assertion.

For compatibility, restrict both deletion covers to \(H-\{x,a\}\). The fixed support \(Q\) is unchanged. The other support is \(P-\{a\}\) in both covers, and using the Hamilton order \(R\) at \(x\) gives exactly the order \((p_m,p_{m-1},B)\), which is also inherited from the deletion cover at \(a\). Thus the restricted covers are compatible. Both omitted labels are restored before \(p_m\), so their insertion slots coincide. \(\square\)

This identifies the neutral branch of defect compression with the support-compatible deletion-cover regime of Article I. Repeated neutral end-edge reversals therefore generate a family of deletion covers with a fixed support and a varying support, rather than an unconstrained family of three-cover states. Once three distinct deleted labels occur in such a compatible family, the localization machinery applies directly.

**Remaining Lemma.** Starting from a \(\Phi\)-minimum singleton lift, suppose the fixed-deletion transport reaches either
1. a displayed end-edge reversal; or
2. a Hamiltonian support of order four or five carrying a displayed endpoint, with two-coverable complement.

Then either \(H\) has a two-cover, or the resulting neutral root exchanges extend to a support-compatible family large enough for the deletion-cover compatibility machinery to force a spanning ordering \(\sigma\) with
\[
\nu(L_\sigma)\le1.
\]

In the two-cut normal form, the unresolved task is thus narrower than before: show that the endpoint-rooted bounded-support alternative either creates a third compatible deletion root or makes one of the two necessary defect-cover cuts redundant.

---

## Section — Appendix. Boundary reversal is local

<!-- section_id: defect_lines_and_spanning_order_compression_appendix_boundary_reversal_is_local -->

Boundary reversal says only that
\[
(a,b,c)\text{ is non-tight}\quad\Longleftrightarrow\quad(c,b,a)\text{ is tight}.
\]
It does not imply cyclic rotation of an ordered triple and does not reverse a tight path. An internal reversed edge therefore cannot be treated as an end-edge reversal without an explicit sequence of valid path orders.

---

## Section — Canonical references

<!-- section_id: defect_lines_and_spanning_order_compression_canonical_references -->

- [[common_endpoint_constraints_fivewindow_counterexample01]] — Common endpoint constraints do not force Hamiltonian five-vertex windows
- [[mincex01]] — Minimum-counterexample calculus
- [[minimum_counterexample_has_a_genuine_reversing_tight_triple]] — Every minimum counterexample has a genuine reversing tight triple
