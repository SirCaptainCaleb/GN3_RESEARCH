# Article IV — endpoint transport and small-support gluing

## Composition status

- Composition version: 1
- Stale: False
- Composed through revision: 1083

## Composition

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



### Correction: the proposed second-edge propagation is not established

The previous Lemma 10 used the assertion that, on three vertices \(u,v,s_2\), exactly one of \((u,v,s_2)\) and \((v,u,s_2)\) is tight. Boundary antisymmetry does not imply this: the boundary flip of \((u,v,s_2)\) is \((s_2,v,u)\), while cyclic or other reorderings have no prescribed status. Therefore that propagation lemma and its claimed four-edge reversal wall are withdrawn.

The maximal-support statements before it, including global noninsertability outside a maximal support, remain valid. The sandwich-splice lemmas below are independent of the withdrawn argument and are retained. Any future inward-propagation argument must use only genuine boundary flips or an additional proved local-extension theorem.

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



### A nearly maximal complementary path is reversed at both ends

**Corollary 12 (one-sided sandwich threshold).** In the setting of Lemma 11, if
[
m+2>k,
]
then both
[
(p_2,p_1,s_1)
qquad	ext{and}qquad
(s_k,p_m,p_{m-1})
]
are tight. In particular, if
[
mge k-1,
]
the two endpoints (s_1,s_k) of the maximal support externally reverse the two displayed end edges of (P).

**Proof.** Suppose first that
[
(s_1,p_1,p_2)
]
is tight. Then
[
(s_2,s_1,p_1,p_2,ldots,p_m)
]
is a Hamiltonian path on a support of order (m+2): the first triple is supplied by Lemma 9 and all later triples are inherited from (P).

Its complement is covered by
[
(s_3,ldots,s_k)mid Q.
]
Thus the complement has path-cover number at most two. If (m+2>k), this is a proper Hamiltonian support larger than (S), contradicting maximality. Therefore
[
(s_1,p_1,p_2)
]
is non-tight, and boundary antisymmetry gives
[
(p_2,p_1,s_1)
]
tight.

The right end is symmetric. If
[
(p_{m-1},p_m,s_k)
]
were tight, then
[
(p_1,ldots,p_m,s_k,s_{k-1})
]
would be a Hamiltonian support of order (m+2), with complement covered by
[
(s_1,ldots,s_{k-2})mid Q.
]
Again maximality excludes this when (m+2>k), so
[
(s_k,p_m,p_{m-1})
]
is tight. (square)

Thus a complementary path whose order is within one of the maximal support order cannot merely carry some reversal: it is trapped between opposite endpoint reversals supplied by the two ends of (S).



### Half-order maximal support

### A maximal support contains at least half the tournament

**Lemma 13 (half-order bound).** Let (H) be a minimum counterexample on (n) vertices, and let
[
Ssubsetneq V(H)
]
be a maximum-cardinality Hamiltonian support satisfying
[
operatorname{pc}(H-S)=2.
]
Put
[
k=|S|.
]
Then
[
n-1le 2k.
]
Equivalently,
[
kge leftlceilrac{n-1}{2}ightceil.
]

**Proof.** Fix any vertex (xin V(H)). Since (H) is a minimum counterexample,
[
operatorname{pc}(H-x)le2.
]
The tournament (H-x) cannot be Hamiltonian, because then a Hamilton path on (H-x) together with the singleton path ({x}) would two-cover (H). Hence
[
H-x=Amid B
]
for two nonempty Hamiltonian paths (A,B).

Now (A) itself is a proper Hamiltonian support whose complement is two-coverable:
[
H-A=Bmid{x}.
]
By maximality of (S),
[
|A|le k.
]
Similarly,
[
H-B=Amid{x}
]
is two-coverable, so
[
|B|le k.
]
Therefore
[
n-1=|A|+|B|le2k.
]
(square)

Thus the maximal-support normalization controls at least half of the ground set. If
[
H-S=Pmid Q,
]
then
[
|P|+|Q|=n-kle k+1.
]
In particular the absorption problem is a majority-support problem: the fixed Hamiltonian support is at least as large as its entire complement up to one vertex.

This quantitative fact is independent of the displayed cover (Pmid Q) and should be used together with the sandwich-splice thresholds above.

### Every deletion cover yields a four-support

### Every deletion cover contains a doubly reversed end edge

**Lemma 14 (four-fold deletion reversal).** Let (H) be a minimum counterexample and let
[
H-x=Pmid Q,
qquad
P=(p_1,ldots,p_m),
qquad
Q=(q_1,ldots,q_s)
]
be any deletion cover. Then (m,sge2), and the omitted vertex (x) reverses all four displayed end edges:
[
(p_2,p_1,x),qquad
(x,p_m,p_{m-1}),
]
[
(q_2,q_1,x),qquad
(x,q_s,q_{s-1})
]
are tight.

**Proof.** Minimum-counterexample calculus gives (m,sge2).

If ((x,p_1,p_2)) were tight, then
[
(x,p_1,ldots,p_m)mid Q
]
would be a spanning two-cover of (H). Hence ((x,p_1,p_2)) is non-tight, and boundary antisymmetry gives
[
(p_2,p_1,x)
]
tight.

Likewise, if ((p_{m-1},p_m,x)) were tight, then
[
(p_1,ldots,p_m,x)mid Q
]
would two-cover (H). Thus its boundary flip
[
(x,p_m,p_{m-1})
]
is tight. The two statements for (Q) are symmetric. (square)

The omitted label is therefore not merely an external reverser somewhere: it simultaneously reverses both exposed ends of both paths in every deletion cover.

**Corollary 15 (every deletion cover yields a Hamiltonian four-support).** Under the hypotheses of Lemma 14, some displayed end edge of (P) or (Q) has two distinct exterior reversers. Consequently (H) contains a Hamiltonian four-support (K) with
[
operatorname{pc}(H-K)=2,
]
and (H-K) is non-Hamiltonian.

**Proof.** Try to concatenate the displayed orders (P,Q). Since
[
P,Qmid{x}
]
cannot be a two-cover, at least one of the two junction triples
[
(p_{m-1},p_m,q_1),
qquad
(p_m,q_1,q_2)
]
is non-tight.

If the first is non-tight, boundary antisymmetry gives
[
(q_1,p_m,p_{m-1})
]
tight. Together with Lemma 14,
[
(x,p_m,p_{m-1})
]
is tight as well. Thus the terminal edge (p_{m-1}p_m) of (P) has two distinct exterior reversers (x,q_1).

If instead the second junction triple is non-tight, then
[
(q_2,q_1,p_m)
]
is tight. Lemma 14 also gives
[
(q_2,q_1,x)
]
tight. Thus the initial edge (q_1q_2) of (Q) has two distinct exterior reversers (p_m,x).

In either case Lemma 38 of the spanning-order compression analysis applies. Since (n>10), choose the additional distinct vertex required there. It yields a Hamiltonian four-set (K).

Minimum-counterexample calculus gives
[
operatorname{pc}(H-K)le2.
]
The complement cannot be Hamiltonian, or a Hamilton path on (K) together with one on (H-K) would two-cover (H). Hence
[
operatorname{pc}(H-K)=2.
]
(square)

This is an arbitrary-order reduction from the general counterexample to the four-support interface. It uses no longest-path choice, no bounded-order classification, and no special support-graph geometry: **every deletion cover already contains enough endpoint failure to force such a four-support.**

The remaining issue is therefore not whether the general problem reaches order-four support—it does canonically from every deleted vertex—but whether the resulting four-support can be chosen with enough retained endpoint incidence to manufacture the one-defect bridge or a direct two-cover.

### Junction-rooted four-support

### The four-support can retain the deleted label at a Hamiltonian endpoint

**Lemma 16 (junction-rooted four-support).** Let
[
H-x=Pmid Q,
qquad
P=(p_1,ldots,p_m),
qquad
Q=(q_1,ldots,q_s),
]
be any deletion cover of a minimum counterexample. Then the five-vertex junction set
[
J={x,p_{m-1},p_m,q_1,q_2}
]
contains a Hamiltonian four-set (K) admitting a Hamilton order with (x) as an endpoint. Moreover
[
operatorname{pc}(H-K)=2.
]

**Proof.** Since (P,Qmid{x}) is not a two-cover, at least one of
[
(p_{m-1},p_m,q_1),
qquad
(p_m,q_1,q_2)
]
is non-tight.

If
[
(p_{m-1},p_m,q_1)
]
is non-tight, boundary antisymmetry gives the tight three-path
[
(q_1,p_m,p_{m-1}).
]
Apply the prescribed-endpoint extension theorem to this tight triple, with the two further vertices
[
q_2, x,
]
prescribing (x) as the endpoint. It yields a Hamiltonian support
[
Ssubseteq J,
qquad
4le |S|le5,
qquad
xin S,
]
with a Hamilton order having (x) as an endpoint.

If instead
[
(p_m,q_1,q_2)
]
is non-tight, then
[
(q_2,q_1,p_m)
]
is a tight three-path. Apply the same theorem with the two further vertices
[
p_{m-1}, x,
]
again prescribing (x). The same conclusion follows.

If (|S|=4), put (K=S). If (|S|=5), delete from its displayed Hamilton order the endpoint opposite (x). The remaining four vertices inherit a Hamilton order still having (x) as an endpoint; call its support (K). Thus in every case
[
Ksubseteq J,qquad |K|=4,qquad xin K,
]
and (x) is a displayed endpoint.

Since (K) is proper, minimum-counterexample calculus gives
[
operatorname{pc}(H-K)le2.
]
The complement cannot be Hamiltonian without two-covering (H), hence
[
operatorname{pc}(H-K)=2.
]
(square)

This strengthens Corollary 15 in exactly the direction needed for comparison. The bounded support is not merely forced from the deletion cover: it can be chosen

- inside the five-vertex neighborhood of the failed (P)-(Q) junction;
- to contain the omitted label (x);
- with (x) as an endpoint of its Hamilton order.

Therefore endpoint deletion from (K) may be compared directly with the **same original deletion cover**
[
H-x=Pmid Q.
]
No second arbitrary deletion cover is needed to expose the first comparison disturbance.

The next target is correspondingly sharper: apply the endpoint-rooted comparison theorem with (k_0=x) and with (F=Pmid Q) fixed, and exploit that the three surviving vertices (K-{x}) lie among
[
{p_{m-1},p_m,q_1,q_2}.
]
The split/reversal alternatives are then confined to the original junction neighborhood rather than occurring at an unrelated support.

### The original deletion cover already splits the rooted three-core

The junction-rooted support of Lemma 16 makes the first comparison disturbance automatic.

**Corollary 17 (junction-core split).** Retain the setting of Lemma 16 and orient the Hamilton order of the resulting four-support from its prescribed endpoint:
[
K=(x,k_1,k_2,k_3).
]
Then
[
{k_1,k_2,k_3}subseteq
{p_{m-1},p_m,q_1,q_2}
]
meets both (V(P)) and (V(Q)). Consequently at least one of the two inherited ordinary edges
[
k_1k_2,qquad k_2k_3
]
has one endpoint in (P) and the other in (Q).

Equivalently, when the endpoint-rooted comparison theorem is applied to (K) with (k_0=x) and the comparison deletion cover fixed to be the original
[
F=Pmid Q
]
of (H-x), the split-core alternative occurs immediately: the three-vertex core (K-{x}) is distributed across the two comparison paths.

**Proof.** The junction set
[
J-{x}
=
{p_{m-1},p_m,q_1,q_2}
]
contains exactly two vertices of (P) and exactly two vertices of (Q). Since (K) contains (x) and has order four, its three remaining vertices form a three-subset of (J-{x}). Such a three-subset cannot lie wholly in either (P) or (Q); it has type (2+1) across the partition (Pmid Q).

The order
[
(k_1,k_2,k_3)
]
is a tight three-path inherited from (K). A three-vertex path whose vertex set meets both classes of a bipartition must have a consecutive pair crossing the bipartition. Hence one of (k_1k_2,k_2k_3) joins (P) to (Q). (square)

Thus no arbitrary second deletion cover is needed even to *produce* the positional disturbance. Every deletion cover
[
H-x=Pmid Q
]
canonically yields, inside the local five-set
[
{x,p_{m-1},p_m,q_1,q_2},
]
a rooted Hamiltonian four-support whose surviving tight three-core already crosses the original (P)-(Q) cut.

The global problem may therefore be sharpened again: determine how such a **junction-crossing rooted three-core** can coexist with the four endpoint reversals of Lemma 14 without producing a spanning two-cover or a one-cut defect order.



### Every deletion cover has explicit four-supports at both junction ends

The four endpoint reversals of Lemma 14 can be paired directly, without an auxiliary extension argument.

**Lemma 18 (canonical opposite-end four-supports).** Let
[
H-x=Pmid Q,
qquad
P=(p_1,ldots,p_m),
qquad
Q=(q_1,ldots,q_s)
]
be any deletion cover of a minimum counterexample. Then:

1. exactly one of the two four-vertex orders
   [
   (p_2,p_1,x,q_1),
   qquad
   (q_2,q_1,x,p_1)
   ]
   is a Hamiltonian path;

2. exactly one of the two four-vertex orders
   [
   (q_s,x,p_m,p_{m-1}),
   qquad
   (p_m,x,q_s,q_{s-1})
   ]
   is a Hamiltonian path.

Consequently (H) contains two explicitly located Hamiltonian four-supports, one using the two initial ends of the deletion cover and one using the two terminal ends. Each has non-Hamiltonian complement of path-cover number two.

**Proof.** Lemma 14 gives
[
(p_2,p_1,x),
qquad
(q_2,q_1,x)
]
tight. The triples
[
(p_1,x,q_1)
qquad	ext{and}qquad
(q_1,x,p_1)
]
are boundary flips, so exactly one is tight.

If ((p_1,x,q_1)) is tight, then
[
(p_2,p_1,x,q_1)
]
is a Hamiltonian four-path. If ((q_1,x,p_1)) is tight, then
[
(q_2,q_1,x,p_1)
]
is a Hamiltonian four-path. This proves (1), including exclusivity.

At the terminal ends, Lemma 14 gives
[
(x,p_m,p_{m-1}),
qquad
(x,q_s,q_{s-1})
]
tight. The triples
[
(q_s,x,p_m)
qquad	ext{and}qquad
(p_m,x,q_s)
]
are boundary flips. If the first is tight, then
[
(q_s,x,p_m,p_{m-1})
]
is a Hamiltonian four-path; if the second is tight, then
[
(p_m,x,q_s,q_{s-1})
]
is. This proves (2).

Every displayed four-set is proper because a minimum counterexample has more than ten vertices. Minimum-counterexample calculus therefore gives path-cover number at most two for its complement. The complement cannot be Hamiltonian, since that Hamilton path together with the displayed four-path would two-cover (H). Hence each complement has path-cover number exactly two. (square)

Thus a deletion cover does not merely force some bounded support near a failed concatenation. It carries a pair of **canonical four-support probes at opposite ends**, determined only by the orientation of the two central boundary-flip triples
[
p_1,x,q_1
qquad	ext{and}qquad
p_m,x,q_s.
]

Each probe contains (x), one complete displayed end edge from one old path, and the exposed endpoint of the other old path. This gives two fixed local interfaces that can be compared against each other, rather than restarting the four-support analysis from an arbitrary support.



### Every deletion cover descends to a neutral square of rooted three-supports

The four endpoint reversals admit a simpler canonical construction than the four-support probes.

**Lemma 19 (endpoint-pair rooted three-square).** Let
[
H-x=Pmid Q,
qquad
P=(p_1,ldots,p_m),
qquad
Q=(q_1,ldots,q_s)
]
be any deletion cover of a minimum counterexample. Let
[
E(P)={p_1,p_m},
qquad
E(Q)={q_1,q_s}.
]

For every pair
[
(p,q)in E(P)	imes E(Q),
]
exactly one of
[
(p,x,q),
qquad
(q,x,p)
]
is tight. Let (T_{p,q}) denote that oriented tight three-path. Then
[
mathcal C_{p,q}
=
(P-p)mid T_{p,q}mid(Q-q)
]
is a spanning three-cover of (H), where (P-p) and (Q-q) carry their inherited path orders.

Moreover:

1. every (mathcal C_{p,q}) lies in the same pairwise-repartition component as the singleton lift
   [
   Pmid{x}mid Q;
   ]

2. all four endpoint-pair states have the same profile
   [
   (m-1)mid3mid(s-1)
   ]
   and hence the same quadratic potential;

3. changing only the endpoint (p) or only the endpoint (q) is one pairwise repartition, so the four states contain a neutral 4-cycle in the repartition graph;

4. relative to the singleton lift,
   [
   Phi(mathcal C_{p,q})
   -
   Phi(Pmid{x}mid Q)
   =
   10-2(m+s)<0.
   ]

Thus every deleted label enters, after at most two pairwise repartitions, a canonical neutral square of strictly lower-(Phi) rooted three-support states.

**Proof.** Fix (pin E(P)) and (qin E(Q)). Boundary antisymmetry at the middle vertex (x) says that exactly one of
[
(p,x,q),
qquad
(q,x,p)
]
is tight. Hence (T_{p,q}) is a tight three-path.

Deleting an endpoint from a displayed tight path leaves a tight path, so (P-p) and (Q-q) are tight. Their supports are disjoint from (T_{p,q}), and together the three supports partition (V(H)). Thus (mathcal C_{p,q}) is a spanning three-cover.

To connect it to the singleton lift, first repartition
[
Qmid{x}
]
as
[
(Q-q)mid{x,q},
]
orienting the two-vertex path ({x,q}) as (x,q) or (q,x) according to the orientation of (T_{p,q}). This is always legal because every two-vertex order is a tight path. Then repartition
[
Pmid{x,q}
]
as
[
(P-p)mid T_{p,q}.
]
This gives (mathcal C_{p,q}) in two pairwise repartitions.

All four choices remove one endpoint from each of (P,Q) and create a three-component, so their common profile is
[
(m-1,3,s-1).
]

Now hold (q) fixed and switch the chosen endpoint of (P) from (p_1) to (p_m). The (Q-q) component is unchanged. On the complementary vertex set
[
V(P)cup{x,q},
]
both
[
(P-p_1)mid T_{p_1,q}
qquad	ext{and}qquad
(P-p_m)mid T_{p_m,q}
]
are two-path covers. Replacing one by the other is therefore one pairwise repartition. The same argument switches the chosen endpoint of (Q) while (p) is fixed. Hence the four states contain the square
[
(p_1,q_1);-;(p_m,q_1);-;(p_m,q_s);-;(p_1,q_s);-;(p_1,q_1),
]
and every edge is (Phi)-neutral because the profile is unchanged.

Finally,
[
egin{aligned}
Phi(mathcal C_{p,q})
-
Phi(Pmid{x}mid Q)
&=
(m-1)^2+9+(s-1)^2-(m^2+1+s^2)\
&=
10-2(m+s).
end{aligned}
]
Since (m+s=|V(H)|-1) and a minimum counterexample has more than ten vertices, this quantity is strictly negative. (square)

This canonical square strengthens the usual singleton descent in two ways: it is symmetric in the two deletion-cover paths, and it preserves four simultaneous choices of exposed endpoint geometry on one common (Phi)-level. Any componentwise minimum reached from the deletion root therefore inherits a four-way rooted entry family rather than a single preferred descent path.



### The rooted endpoint square is minimal only at order eleven

**Corollary 20.** Retain the endpoint-pair square of Lemma 19. If one, equivalently all, of the four states
[
mathcal C_{p,q}
]
minimizes (Phi) in its pairwise-repartition component, then
[
|P|=|Q|=5
qquad	ext{and}qquad
|V(H)|=11.
]

Equivalently, if (|V(H)|
e11), the common repartition component of the four endpoint-pair states contains a three-cover of strictly smaller quadratic potential.

**Proof.** All four states lie in the same repartition component and have the same profile
[
3mid(m-1)mid(s-1).
]
Hence either all four are componentwise (Phi)-minimum or none is.

The rooted small-support classification
[[line_rooted_small_support_descent_from_deletion_cover_lifts]]
shows that at a quadratic minimum, any state containing a component of order three has exactly profile
[
3mid4mid4.
]
Therefore
[
m-1=s-1=4,
]
so (m=s=5). Since (m+s=|V(H)|-1),
[
|V(H)|=11.
]
The contrapositive gives the second assertion. (square)

Thus the canonical endpoint-pair square has only one possible immediate terminal order. At every other order, the square is not merely a strict improvement over the singleton lift: its entire neutral four-cycle sits strictly above another state in the same repartition component.





### Correction: the cross-endpoint central orientation is not forced

For a deletion cover
[
H-x=Pmid Q,qquad
P=(p_1,ldots,p_m),qquad
Q=(q_1,ldots,q_s),
]
the endpoint-insertion failures give
[
(p_{m-1},p_m,x) 	ext{non-tight},
qquad
(x,q_1,q_2) 	ext{non-tight},
]
but they do not determine the status of the distinct middle triple
[
(p_m,x,q_1).
]
In particular, the spanning order
[
(p_1,ldots,p_m,x,q_1,ldots,q_s)
]
has three new triples around (x), not one. Even if ((p_m,x,q_1)) is tight, the two outer new triples above remain non-tight, so this order is not Hamiltonian.

Therefore the former claim that ((q_1,x,p_m)) and ((p_1,x,q_s)) are forced tight is withdrawn, as are the canonical five-path conclusions that depended on those forced orientations.

The valid preceding statements remain unchanged. In particular:

- Lemma 18 supplies canonical four-supports at the same-end endpoint pairs without choosing the orientation of the central boundary pair.
- Lemma 19 supplies the four endpoint-pair rooted three-support states by orienting each central triple in whichever direction is actually tight.
- At a cross pair such as ((p_m,q_1)), if ((q_1,x,p_m)) happens to be tight then
  [
  (q_2,q_1,x,p_m,p_{m-1})
  ]
  is indeed a tight five-path; if the opposite orientation ((p_m,x,q_1)) is tight, that five-path is unavailable and this is a genuine separate branch.

Thus future arguments at the two cross corners must retain the central orientation as case data rather than infer it from the failure of the deletion-cover concatenation.


---

## Section — Appendix. Local failures do not imply global absorption

<!-- section_id: endpoint_transport_and_small_support_gluing_appendix_local_failures_do_not_imply_global_absorption -->

The following implications are not valid without additional hypotheses:
- two vertices extending the same end of a path need not concatenate with each other;
- two reverse triples through the two ends of a small support need not make that support Hamiltonian;
- Hamiltonicity of \(K\cup\{x\}\) does not imply that \(x\) can be an endpoint of a Hamilton path;
- boundary reversal of one triple does not permit cyclic rotation of that triple or reversal of an entire tight path.

Accordingly, every use of an endpoint in the main proof is tied to a displayed Hamilton order, and every iterative move is a pairwise repartition in a specified connected component.

## Contained Sections

- 1. [Introduction](../SECTIONS/endpoint_transport_and_small_support_gluing_introduction.md) (`endpoint_transport_and_small_support_gluing_introduction`; composition v1; stale=False)
- 2. [Greedy endpoint transport](../SECTIONS/endpoint_transport_and_small_support_gluing_greedy_endpoint_transport.md) (`endpoint_transport_and_small_support_gluing_greedy_endpoint_transport`; composition v1; stale=False)
- 3. [A displayed end-edge reversal](../SECTIONS/endpoint_transport_and_small_support_gluing_a_displayed_end_edge_reversal.md) (`endpoint_transport_and_small_support_gluing_a_displayed_end_edge_reversal`; composition v1; stale=False)
- 4. [Endpoint positions of a transferred vertex](../SECTIONS/endpoint_transport_and_small_support_gluing_endpoint_positions_of_a_transferred_vertex.md) (`endpoint_transport_and_small_support_gluing_endpoint_positions_of_a_transferred_vertex`; composition v1; stale=False)
- 5. [Compatible one-vertex extensions](../SECTIONS/endpoint_transport_and_small_support_gluing_compatible_one_vertex_extensions.md) (`endpoint_transport_and_small_support_gluing_compatible_one_vertex_extensions`; composition v1; stale=False)
- 6. [Two same-side extension vertices](../SECTIONS/endpoint_transport_and_small_support_gluing_two_same_side_extension_vertices.md) (`endpoint_transport_and_small_support_gluing_two_same_side_extension_vertices`; composition v1; stale=False)
- 7. [A vertex internal in every Hamiltonian order](../SECTIONS/endpoint_transport_and_small_support_gluing_a_vertex_internal_in_every_hamiltonian_order.md) (`endpoint_transport_and_small_support_gluing_a_vertex_internal_in_every_hamiltonian_order`; composition v1; stale=False)
- 8. [The remaining lemma](../SECTIONS/endpoint_transport_and_small_support_gluing_the_remaining_lemma.md) (`endpoint_transport_and_small_support_gluing_the_remaining_lemma`; composition v1; stale=False)
- 9. [Appendix. Local failures do not imply global absorption](../SECTIONS/endpoint_transport_and_small_support_gluing_appendix_local_failures_do_not_imply_global_absorption.md) (`endpoint_transport_and_small_support_gluing_appendix_local_failures_do_not_imply_global_absorption`; composition v1; stale=False)
