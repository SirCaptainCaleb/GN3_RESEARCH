# Proof rehearsal IV — endpoint transport and small-support gluing

## Statement

Let H be a minimum counterexample. Starting from a Hamiltonian four- or five-vertex support with two-coverable complement, or from a Hamiltonian enlargement at an endpoint of a displayed path, greedy endpoint transport produces a reversal of a displayed end edge unless the added vertex is internal in every Hamiltonian order. A displayed end-edge reversal gives a two-cover, a strict decrease of quadratic potential, or a one-vertex transfer. Opposite endpoint realizations eliminate the transfer; same-side realizations reduce by insertion positions and Hall's theorem to a common reversed edge, a same-deletion transfer, or a bounded common-core configuration.

## Body

# Endpoint transport and small-support gluing

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

## 1. Greedy endpoint transport

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

## 2. A displayed end-edge reversal

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

## 3. Endpoint positions of a transferred vertex

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

## 4. Compatible one-vertex extensions

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

## 5. Two same-side extension vertices

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

## 6. A vertex internal in every Hamiltonian order

It remains to consider an augmented support \(K\cup\{x\}\) in which \(x\) is internal in every Hamiltonian order.

Take two such labels \(x,y\) occurring over the same four-vertex support and compare deletion covers of the one- and two-label deletions. If a comparison cover has only one edge joining the path pieces obtained by deleting \(x\) or \(y\) from a Hamilton path, the block-count identity forces that edge to join the two pieces directly; otherwise restoring the deleted label would place it at an endpoint, contrary to the assumption.

With two labels, the same count shows that either at least two such inter-piece edges occur, or the labels occupy adjacent internal positions and every lower deletion cover uses the direct join between the two outer pieces. Comparing the three lower deletion covers in the adjacent case gives either an order disagreement or the same inherited order on all common pieces. In the latter case the one- and two-label deletions form a four-state configuration in which the opposite path is unchanged and all direct joins occur in the same position.

We record this as follows.

**Lemma 7.** If two relevant labels are internal in every Hamiltonian order of their augmented supports, then either
1. a comparison deletion cover has at least two edges joining distinct inherited path pieces;
2. an order disagreement occurs among the lower deletion covers; or
3. the one- and two-label deletion covers preserve one common inherited order and one unchanged complementary path.

The proof is the preceding block count applied successively to the one- and two-label deletions.

## 7. The remaining lemma

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

## Appendix. Local failures do not imply global absorption

The following implications are not valid without additional hypotheses:
- two vertices extending the same end of a path need not concatenate with each other;
- two reverse triples through the two ends of a small support need not make that support Hamiltonian;
- Hamiltonicity of \(K\cup\{x\}\) does not imply that \(x\) can be an endpoint of a Hamilton path;
- boundary reversal of one triple does not permit cyclic rotation of that triple or reversal of an entire tight path.

Accordingly, every use of an endpoint in the main proof is tied to a displayed Hamilton order, and every iterative move is a pairwise repartition in a specified connected component.