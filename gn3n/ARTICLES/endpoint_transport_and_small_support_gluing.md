# Article IV — endpoint transport and small-support gluing

---

## Section — Introduction

<!-- section_id: endpoint_transport_and_small_support_gluing_introduction -->

Let \(H\) be a minimum counterexample to \(\operatorname{pc}(H)\le2\). A three-cover
\[
P_1\mid P_2\mid P_3
\]
has quadratic potential
\[
\Phi=|P_1|^2+|P_2|^2+|P_3|^2.
\]
Pairwise repartition means replacing two displayed paths by another two-cover of their union while leaving the third path unchanged.

This argument begins with a Hamiltonian support attached to a displayed endpoint, a reversal of a displayed path edge, or two nearby Hamiltonian supports with a large common part. The purpose of the transport is to place the new order information at an actual end edge of a displayed path.

---

## Section — Greedy endpoint transport

<!-- section_id: endpoint_transport_and_small_support_gluing_greedy_endpoint_transport -->

Let
\[
X\mid C\mid D
\]
be a three-cover, with \(X\) Hamiltonian,
\[
C=(c_0,c_1,\ldots ,c_m),
\]
and \(D\ne\varnothing\). Suppose \(X\cup\{c_0\}\) is Hamiltonian.

First note that any deletion cover of \(H-c_0\) must contain an edge with one endpoint in \(X\) and the other in
\[
(C-\{c_0\})\cup D.
\]
Otherwise its two paths would each remain inside one side of this partition, and adjoining \(c_0\) to a Hamilton path on \(X\cup\{c_0\}\) would separate \(H\) into two tight paths.

Suppose now that some Hamilton path on \(X\cup\{c_0\}\) has \(c_0\) as the endpoint adjacent to \(c_1\). Extend this Hamilton path greedily by \(c_1,c_2,\ldots\).

**Lemma 1.** If the greedy extension does not absorb all of \(C\), then at the first failed extension there is a tight triple reversing the terminal edge of the current Hamilton path.

**Proof.** Let \(R\) be the maximal Hamilton path obtained, ending in an edge \((u,c_h)\), and suppose \(c_{h+1}\) is the first vertex that cannot be appended. Then
\[
(u,c_h,c_{h+1})
\]
is non-tight. Boundary reversal gives
\[
(c_{h+1},c_h,u)
\]
tight, which reverses the displayed terminal edge \((u,c_h)\). If every vertex of \(C\) were absorbed, the resulting Hamilton path together with \(D\) would be a two-cover of \(H\). \(\square\)

Thus endpoint realization gives a displayed end-edge reversal. The only alternative is that \(c_0\) is internal in every Hamiltonian order of \(X\cup\{c_0\}\).

---

## Section — A displayed end-edge reversal

<!-- section_id: endpoint_transport_and_small_support_gluing_a_displayed_end_edge_reversal -->

Let
\[
H-x=P\mid Q,\qquad P=(p_0,\ldots ,p_m),
\]
and suppose \(R\) is another Hamilton order of \(V(P)\) containing the reversed terminal edge
\[
(p_m,p_{m-1}).
\]
Write
\[
R=(A,p_m,p_{m-1},B),\qquad t=|A|,\qquad N=|P|.
\]

Since \(x\) cannot be appended to the displayed order \(P\),
\[
(p_{m-1},p_m,x)
\]
is non-tight, so
\[
(x,p_m,p_{m-1})
\]
is tight. Hence
\[
(x,p_m,p_{m-1},B)
\]
is a tight path.

If \(t=0\), this path together with \(Q\) gives a two-cover. If \(t\ge1\), the three paths
\[
A\mid(x,p_m,p_{m-1},B)\mid Q
\]
form a pairwise repartition of \(P\mid\{x\}\mid Q\). The change of the two affected square terms is
\[
t^2+(N-t+1)^2-(N^2+1)
=-2(t-1)(N-t).
\]

Therefore:

**Lemma 2.** A reversal of a displayed end edge gives one of:
1. a two-cover of \(H\);
2. a strict decrease of \(\Phi\);
3. the case \(t=1\), in which one vertex is transferred between the two non-singleton supports and \(\Phi\) is unchanged.

The initial edge is symmetric.

At a minimum of \(\Phi\) in a connected component of the pairwise-repartition graph, only the one-vertex transfer remains.

---

## Section — Endpoint positions of a transferred vertex

<!-- section_id: endpoint_transport_and_small_support_gluing_endpoint_positions_of_a_transferred_vertex -->

Suppose \(X,Y,D,\{x\}\) partition \(V(H)\) and both
\[
(X\cup\{x\})\mid Y\mid D
\quad\text{and}\quad
X\mid(Y\cup\{x\})\mid D
\]
are three-covers.

**Lemma 3.** If \(x\) is the final vertex of a Hamilton path on \(X\cup\{x\}\) and the initial vertex of a Hamilton path on \(Y\cup\{x\}\), then a displayed end-edge reversal occurs. The same holds with initial and final interchanged.

**Proof.** Start with the Hamilton path on \(X\cup\{x\}\) ending at \(x\), and greedily append the vertices following \(x\) in the Hamilton path on \(Y\cup\{x\}\). If the whole path is absorbed, its union with \(D\) is a two-cover. Otherwise Lemma 1 gives a displayed end-edge reversal. \(\square\)

Consequently, if no two-cover, strict decrease, or displayed end-edge reversal occurs, then either
- \(x\) is internal in every Hamiltonian order of one augmented support; or
- whenever \(x\) is an endpoint in either augmented support, it is always on the same side in both.

The second possibility is governed by insertion positions.

---

## Section — Compatible one-vertex extensions

<!-- section_id: endpoint_transport_and_small_support_gluing_compatible_one_vertex_extensions -->

Let \(K\) be a vertex set and let \(x,y\notin K\). Suppose \(K\cup\{x\}\) and \(K\cup\{y\}\) have Hamilton paths that induce the same order
\[
C=(c_1,\ldots ,c_m)
\]
on \(K\). Each path is obtained by inserting its exceptional vertex into a gap of \(C\), allowing the two endpoint gaps.

**Lemma 4.**
1. If the insertion gaps are separated by at least one gap, inserting both vertices gives a Hamilton path on \(K\cup\{x,y\}\).
2. If the gaps are adjacent, the simultaneous order is Hamiltonian unless the unique triple containing \(x\), the intervening core vertex, and \(y\) is non-tight; in that case its boundary flip is tight.
3. If the gaps coincide at an internal edge \(uv\) of \(C\), then \(\{u,v,x,y\}\) is Hamiltonian.

**Proof.** In the first case no consecutive triple in the simultaneous order contains both \(x\) and \(y\); every triple is inherited from one of the two given Hamilton paths. In the adjacent case there is exactly one new triple, so boundary reversal gives the alternative. In the common internal gap, both
\[
(u,x,v),\qquad(u,y,v)
\]
are tight. Among the boundary pair on \(\{x,y,u\}\) or \(\{x,y,v\}\), the tight orientation extends one of these triples to a Hamilton path on the four vertices. \(\square\)

Thus, if neither a larger Hamiltonian support nor a reverse triple nor a Hamiltonian four-set occurs, two compatible extensions use the same endpoint gap.

Three extensions of one four-set cannot all remain featureless.

**Lemma 5.** Let \(C\) be a four-set and \(r_1,r_2,r_3\notin C\). If each \(C\cup\{r_i\}\) is Hamiltonian, then at least one of the following holds:
1. two chosen Hamilton paths have an order disagreement on \(C\);
2. \(C\cup\{r_i,r_j\}\) is Hamiltonian for some \(i\ne j\);
3. a Hamiltonian four-set lies in \(C\cup\{r_1,r_2,r_3\}\);
4. a tight triple through two roots reverses an edge of one chosen path.

**Proof.** If the induced orders on \(C\) disagree, (1) holds. Otherwise all roots are inserted into one common order on \(C\). Lemma 4 gives (2), (3), or (4) unless all three occupy one endpoint gap. In that remaining case assume they all precede \(c_1\). Failure of every pair union to be Hamiltonian forces
\[
(c_1,r_i,r_j)
\]
tight for every ordered pair \(i\ne j\). One of
\[
(r_1,r_2,r_3),\qquad(r_3,r_2,r_1)
\]
is tight, so one of
\[
(c_1,r_1,r_2,r_3),\qquad(c_1,r_3,r_2,r_1)
\]
is a Hamilton path. This gives (3). The common terminal gap is symmetric. \(\square\)

---

## Section — Two same-side extension vertices

<!-- section_id: endpoint_transport_and_small_support_gluing_two_same_side_extension_vertices -->

Suppose \(x,y\) can occur only at the same endpoint side of the relevant augmented supports, and let
\[
R\mid S
\]
be a two-cover of \(H-\{x,y\}\). Form a bipartite graph with left class \(\{x,y\}\) and right class \(\{R,S\}\), joining a label to a path if it can be attached at the prescribed endpoint.

If there is a perfect matching, attach \(x\) and \(y\) to different paths and obtain a two-cover of \(H\). If no perfect matching exists, Hall's theorem leaves two possibilities:
- one of \(R,S\) accepts neither label;
- one of \(x,y\) can be attached to neither \(R\) nor \(S\).

In the first case, the two failed attachments give reverse tight triples through one common end edge. In the second, deleting the blocked label yields two deletion covers that differ by a one-vertex transfer.

**Lemma 6.** Two reverse triples through the same displayed end edge yield two Hamiltonian five-sets with a common four-set, unless an earlier two-cover or Hamiltonian four-set occurs.

**Proof.** For each reverse triple, form a graph on exterior labels by joining two labels when their simultaneous extension fails. Each failure graph is triangle-free: three pairwise failures, after boundary reversal of the three non-tight insertion triples, give a Hamiltonian five-vertex extension. If no exterior pair succeeds for both reverse triples, the edges of \(K_6\) can be colored according to which failure graph contains them, with no monochromatic triangle. This contradicts \(R(3,3)=6\). Hence some pair succeeds for both reverse triples, giving the required two five-sets. \(\square\)

Let the two five-sets be \(K\cup\{p\}\) and \(K\cup\{q\}\), where \(|K|=4\). Their six-vertex union has three relevant forms:
- it is Hamiltonian;
- two Hamiltonian vertex deletions are adjacent, giving overlapping Hamiltonian four- and five-sets;
- the Hamiltonian deletion pairs form a matching, fixing the three pairwise insertion relations on the six vertices.

Each form is a bounded common-core configuration with a two-coverable complement inherited from the construction.

---

## Section — A vertex internal in every Hamiltonian order

<!-- section_id: endpoint_transport_and_small_support_gluing_a_vertex_internal_in_every_hamiltonian_order -->

It remains to consider an augmented support \(K\cup\{x\}\) in which \(x\) is internal in every Hamiltonian order.

Take two such labels \(x,y\) occurring over the same four-vertex support and compare deletion covers of the one- and two-label deletions. If a comparison cover has only one edge joining the path pieces obtained by deleting \(x\) or \(y\) from a Hamilton path, the block-count identity forces that edge to join the two pieces directly; otherwise restoring the deleted label would place it at an endpoint, contrary to the assumption.

With two labels, the same count shows that either at least two such inter-piece edges occur, or the labels occupy adjacent internal positions and every lower deletion cover uses the direct join between the two outer pieces. Comparing the three lower deletion covers in the adjacent case gives either an order disagreement or the same inherited order on all common pieces. In the latter case the one- and two-label deletions form a four-state configuration in which the opposite path is unchanged and all direct joins occur in the same position.

We record this as follows.

**Lemma 7.** If two relevant labels are internal in every Hamiltonian order of their augmented supports, then either
1. a comparison deletion cover has at least two edges joining distinct inherited path pieces;
2. an order disagreement occurs among the lower deletion covers; or
3. the one- and two-label deletion covers preserve one common inherited order and one unchanged complementary path.

The proof is the preceding block count applied successively to the one- and two-label deletions.

---

## Section — The remaining lemma

<!-- section_id: endpoint_transport_and_small_support_gluing_the_remaining_lemma -->

All non-decreasing cases now have one of the following forms:
- a displayed end-edge reversal;
- a one-vertex transfer whose endpoint realizations all use the same side;
- two Hamiltonian five-sets with a common four-set;
- overlapping Hamiltonian four- and five-sets;
- the matching deletion pattern on a six-set;
- the internal-deletion configuration of Lemma 7.

The first form is handled by Lemma 2. The remaining forms require one common statement.

**Remaining Lemma.** Let a minimum counterexample contain one of the bounded configurations listed above, obtained from a deletion cover through pairwise repartitions in one connected component. Then either \(H\) has a two-cover, or the same component contains a three-cover of strictly smaller quadratic potential, or \(H\) has a spanning ordering of defect span at most \(2\).

A proof completes the endpoint-transport argument.

### Maximal-support reduction

The endpoint-transport problem admits a global normalization that removes all dependence on small total order.

**Lemma 8 (maximal Hamiltonian support).** Let \(H\) be a minimum counterexample. Among all proper Hamiltonian supports \(S\subsetneq V(H)\) satisfying
\[
\operatorname{pc}(H-S)=2,
\]
choose one with \(|S|\) maximum, and fix a Hamilton order
\[
S=(s_1,\ldots,s_k).
\]
Let
\[
H-S=P\mid Q
\]
be any two-cover of the complement.

Then every displayed endpoint \(y\) of \(P\) or \(Q\) satisfies:

1. \(S\cup\{y\}\) is non-Hamiltonian;
2. \(y\) is noninsertable at every position of the displayed order \(s_1,\ldots,s_k\);
3. in particular,
\[
(y,s_1,s_2),\qquad (s_{k-1},s_k,y)
\]
are non-tight, and therefore
\[
(s_2,s_1,y),\qquad (y,s_k,s_{k-1})
\]
are tight.

Thus every endpoint of the complementary two-cover reverses both displayed end edges of the same maximal Hamiltonian path \(S\).

**Proof.** Let \(y\) be an endpoint of \(P\); the case \(y\in Q\) is identical. If \(S\cup\{y\}\) were Hamiltonian, then
\[
H-(S\cup\{y\})=(P-\{y\})\mid Q
\]
would still have a two-cover, because deleting an endpoint from a displayed tight path leaves a tight path. This contradicts maximality of \(|S|\). Hence \(S\cup\{y\}\) is non-Hamiltonian.

Apply [[endpoint_replacement_truncation_dichotomy01]] to the displayed Hamilton path \(S\) and exterior vertex \(y\). Its non-Hamiltonian branch says that \(y\) is noninsertable at every gap of the inherited order on \(S\), including both endpoint gaps. Therefore neither
\[
(y,s_1,\ldots,s_k)
\qquad\text{nor}\qquad
(s_1,\ldots,s_k,y)
\]
is a tight path. Equivalently,
\[
(y,s_1,s_2)
\quad\text{and}\quad
(s_{k-1},s_k,y)
\]
are non-tight. Boundary antisymmetry gives the two displayed reversals. \(\square\)

This is the correct global endpoint-transport target. A proof of the grand two-cover theorem now follows from any statement showing that four endpoint labels lying on two complementary tight paths cannot all remain globally noninsertable into one maximal Hamiltonian path.

Equivalently, the remaining problem can be posed without any bounded-order hypothesis:

> **Maximal-support absorption problem.** Let \(S\) be a maximal Hamiltonian support with \(\operatorname{pc}(H-S)=2\). Show that at least one endpoint of some two-cover of \(H-S\) Hamiltonian-extends \(S\), or else use the simultaneous two-sided reversal constraints forced above to construct a strictly larger Hamiltonian support \(S'\) with \(\operatorname{pc}(H-S')=2\).

Any solution is a genuine reduction of the general case: each successful step increases \(|S|\), so iteration terminates only when the complement is Hamiltonian, yielding a two-cover of \(H\).


### Maximality forces every exterior vertex to reverse both ends

The endpoint restriction in Lemma 8 is unnecessary.

**Lemma 9 (global noninsertability outside a maximal support).** Let (H) be a minimum counterexample, and let
[
S=(s_1,ldots,s_k)
]
be a maximum-cardinality proper Hamiltonian support satisfying
[
operatorname{pc}(H-S)=2.
]
Then for every vertex (y
otin S):

1. (Scup{y}) is non-Hamiltonian;
2. (y) is noninsertable at every position of the displayed order of (S);
3. in particular,
   [
   (s_2,s_1,y),qquad (y,s_k,s_{k-1})
   ]
   are tight.

Hence **every** exterior vertex reverses both displayed end edges of the same maximal Hamiltonian path (S).

Moreover
[
|V(H)-S|ge4,
]
so there are at least four distinct vertices with this simultaneous double-reversal property.

**Proof.** Since (operatorname{pc}(H-S)=2), the complement (H-S) is non-Hamiltonian. Every boundary tournament of order at most three is Hamiltonian, so (|V(H)-S|ge4). Consequently (Scup{y}) is proper for every (y
otin S).

Suppose (Scup{y}) were Hamiltonian. Minimum-counterexample calculus gives
[
operatorname{pc}igl(H-(Scup{y})igr)le2.
]
That complement cannot be Hamiltonian, because then it and a Hamilton path on (Scup{y}) would two-cover (H). Hence its path-cover number is exactly two. Thus (Scup{y}) would be a strictly larger Hamiltonian support with two-coverable complement, contradicting the maximal choice of (S). This proves (1).

Now apply [[endpoint_replacement_truncation_dichotomy01]] to the displayed path (S) and the exterior vertex (y). Since (Scup{y}) is non-Hamiltonian, (y) is noninsertable at every inherited gap, proving (2).

In particular (y) cannot be prepended or appended. Therefore
[
(y,s_1,s_2),qquad(s_{k-1},s_k,y)
]
are non-tight. Boundary antisymmetry gives
[
(s_2,s_1,y),qquad(y,s_k,s_{k-1})
]
tight, proving (3). (square)

Thus maximal-support absorption is stronger than an endpoint problem for one chosen complementary two-cover. The entire exterior set is a family of simultaneous double reversers of the same two displayed end edges. The remaining task is to exploit this global family to build a Hamiltonian support strictly larger than (S).



### Maximality propagates the reversal wall one edge inward

**Lemma 10 (second-edge propagation).** In the setting of Lemma 9, write
[
Y=V(H)-S,qquad S=(s_1,ldots,s_k).
]
Then (kge5). Moreover:

1. at most one vertex (yin Y) satisfies
   [
   (y,s_2,s_3)
   ]
   tight. Hence all but at most one vertex of (Y) satisfy
   [
   (s_3,s_2,y)
   ]
   tight;

2. at most one vertex (yin Y) satisfies
   [
   (s_{k-2},s_{k-1},y)
   ]
   tight. Hence all but at most one vertex of (Y) satisfy
   [
   (y,s_{k-1},s_{k-2})
   ]
   tight.

Since (|Y|ge4), there are at least two distinct vertices (u,vin Y) that simultaneously reverse the two leftmost displayed edges
[
s_1s_2,qquad s_2s_3
]
and the two rightmost displayed edges
[
s_{k-2}s_{k-1},qquad s_{k-1}s_k.
]

**Proof.** First, (kge5). Since (|V(H)|>10), choose any six vertices. By [[smallset01]], that six-set contains a Hamiltonian five-set (F). Minimum-counterexample calculus gives
[
operatorname{pc}(H-F)le2.
]
The complement cannot be Hamiltonian, or (F) and (H-F) would two-cover (H). Thus (operatorname{pc}(H-F)=2), so maximality of (S) gives (|S|ge5).

Now suppose two distinct exterior vertices (u,vin Y) both satisfy
[
(u,s_2,s_3),qquad(v,s_2,s_3)
]
tight. On the three-set ({u,v,s_2}), exactly one of the two opposite cyclic orientations is tight. Hence one of
[
(u,v,s_2),qquad(v,u,s_2)
]
is tight.

If ((u,v,s_2)) is tight, then
[
(u,v,s_2,s_3,ldots,s_k)
]
is a Hamilton path on
[
S'=(S-{s_1})cup{u,v}.
]
If ((v,u,s_2)) is tight, use
[
(v,u,s_2,s_3,ldots,s_k)
]
instead. In either case (|S'|=|S|+1).

The set (S') is proper because (|Y|ge4). Minimum-counterexample calculus gives
[
operatorname{pc}(H-S')le2.
]
If (H-S') were Hamiltonian, it and (S') would two-cover (H); hence (operatorname{pc}(H-S')=2). This contradicts maximality of (S). Therefore at most one such (y) exists.

For every other (yin Y), the triple ((y,s_2,s_3)) is non-tight, so boundary antisymmetry gives
[
(s_3,s_2,y)
]
tight. This proves (1).

The proof of (2) is symmetric. If two distinct (u,v) both satisfy
[
(s_{k-2},s_{k-1},u),qquad
(s_{k-2},s_{k-1},v)
]
tight, exactly one of
[
(s_{k-1},u,v),qquad
(s_{k-1},v,u)
]
is tight. Appending the correspondingly ordered pair to
[
(s_1,ldots,s_{k-1})
]
again gives a Hamiltonian support of order (k+1), contradiction.

Finally Lemma 9 says every (yin Y) already reverses (s_1s_2) and (s_{k-1}s_k). The exceptional sets in (1) and (2) have total size at most two, while (|Y|ge4). Hence at least two vertices lie outside both exceptional sets and reverse all four displayed edges claimed. (square)

Thus maximality creates a genuine inward-propagating reversal wall: not only every exterior vertex, but all but one at each side, is forced to reverse the next displayed edge. Any further propagation mechanism would enlarge the forbidden reversed boundary layers and offers a monotone route toward contradiction.



### A long complementary path either enlarges the maximal support or becomes a reversal carrier

Retain the maximal-support setting of Lemma 9:
[
S=(s_1,ldots,s_k),
qquad
H-S=Pmid Q,
]
where
[
P=(p_1,ldots,p_m),qquad mge2,
]
and (S) has maximum cardinality among proper Hamiltonian supports with two-coverable complement.

By Lemma 9 every exterior vertex reverses both displayed end edges of (S). In particular
[
(s_2,s_1,p_1)
qquad	ext{and}qquad
(p_m,s_k,s_{k-1})
]
are tight.

**Lemma 11 (sandwich splice).** At least one of the following holds:

1. the sequence
   [
   (s_2,s_1,p_1,ldots,p_m,s_k,s_{k-1})
   ]
   is a Hamiltonian path on a support of order (m+4);
2. the triple
   [
   (p_2,p_1,s_1)
   ]
   is tight, so (s_1) externally reverses the initial displayed edge (p_1p_2) of (P);
3. the triple
   [
   (s_k,p_m,p_{m-1})
   ]
   is tight, so (s_k) externally reverses the terminal displayed edge (p_{m-1}p_m) of (P).

Consequently, if
[
m+4>k,
]
then outcome 1 is impossible by maximality of (S), and (P) is a marked reversal carrier in the same spanning three-cover (Smid Pmid Q).

**Proof.** All consecutive triples in
[
(s_2,s_1,p_1,ldots,p_m,s_k,s_{k-1})
]
are already known tight except possibly
[
(s_1,p_1,p_2)
qquad	ext{and}qquad
(p_{m-1},p_m,s_k).
]
Indeed, the first and final triples are supplied by Lemma 9, while all triples wholly inside (P) are inherited from its displayed path.

If both remaining junction triples are tight, outcome 1 holds.

If
[
(s_1,p_1,p_2)
]
is non-tight, boundary antisymmetry gives
[
(p_2,p_1,s_1)
]
tight, which is outcome 2. If
[
(p_{m-1},p_m,s_k)
]
is non-tight, boundary antisymmetry gives
[
(s_k,p_m,p_{m-1})
]
tight, which is outcome 3.

Finally suppose outcome 1 holds. Its complement is covered by the inherited interval
[
(s_3,ldots,s_{k-2})
]
and the displayed path (Q), with the empty-interval cases omitted. Hence the complement has path-cover number at most two. If (m+4>k), this produces a proper Hamiltonian support strictly larger than (S) with two-coverable complement, contradicting the maximal choice of (S). Therefore when (m+4>k), at least one of outcomes 2 and 3 holds. (square)

Thus every complementary path longer than (k-4) automatically acquires a reversal certificate from an endpoint of (S). The maximal-support normalization therefore has a size-sensitive carrier-switch mechanism: a long outside path cannot remain inert.



---

## Section — Appendix. Local failures do not imply global absorption

<!-- section_id: endpoint_transport_and_small_support_gluing_appendix_local_failures_do_not_imply_global_absorption -->

The following implications are not valid without additional hypotheses:
- two vertices extending the same end of a path need not concatenate with each other;
- two reverse triples through the two ends of a small support need not make that support Hamiltonian;
- Hamiltonicity of \(K\cup\{x\}\) does not imply that \(x\) can be an endpoint of a Hamilton path;
- boundary reversal of one triple does not permit cyclic rotation of that triple or reversal of an entire tight path.

Accordingly, every use of an endpoint in the main proof is tied to a displayed Hamilton order, and every iterative move is a pairwise repartition in a specified connected component.
