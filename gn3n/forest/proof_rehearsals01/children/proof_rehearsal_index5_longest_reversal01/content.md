# Proof rehearsal V — longest paths and reversal structure

## Statement

Let H be a minimum counterexample. Every minimum counterexample contains a tight triple reversing an edge of a tight path. If A is a longest tight path, its exterior has path-cover number two and every exterior vertex gives reversed tight triples at both ends of A. These relations force either a small Hamiltonian support with two-coverable complement, several Hamiltonian five-sets sharing a four-vertex core, or a synchronized endpoint-pair configuration. The remaining lemma is to convert one of these positioned configurations into a displayed end-edge reversal, a two-cover, or a spanning ordering of defect span at most two.

## Body

# Longest paths and reversal structure

Let \(H\) be a minimum counterexample to \(\operatorname{pc}(H)\le2\). A tight triple \((x,v,u)\) reverses the ordered edge \((u,v)\) of a tight path.

## 1. Reversals are unavoidable

**Lemma 1.** If two tight paths of order at least three have an order disagreement on their common vertices, then \(H\) contains a tight triple reversing an edge of one of the paths.

**Proof.** Choose a disagreeing pair with minimum union and then minimum total order. If a common edge is traversed in opposite directions, a consecutive tight triple containing that edge reverses the corresponding edge of the other path.

Otherwise the first change of relative order yields a reversing triple unless the two paths close into a vertex-simple tight cycle. Open such a cycle at any edge. Its complement is non-Hamiltonian and has a two-cover \(A\mid B\). Let \((a_{m-1},a_m)\) be an end edge of a nontrivial component \(A\). If both triples needed to concatenate \(A\) to the opened cycle were tight, the concatenation together with \(B\) would two-cover \(H\). Hence one of those triples is non-tight. Boundary reversal then gives a tight triple reversing either \((a_{m-1},a_m)\) or an edge of the opened cycle. \(\square\)

Deletion covers at different vertices cannot all induce one common support partition and one common relative order, since those orders would glue to a two-cover. Hence:

**Corollary 2.** Every minimum counterexample contains a tight triple reversing an edge of a tight path.

The remaining question is where such a reversal can be placed.

## 2. A longest path

Choose a longest tight path
\[
A=(a_0,\ldots ,a_{\lambda-1})
\]
and put
\[
U=V(H)-V(A).
\]

**Lemma 3.**
1. \(H[U]\) is non-Hamiltonian and has path-cover number two.
2. For every \(y\in U\),
\[
(a_1,a_0,y),\qquad
(y,a_{\lambda-1},a_{\lambda-2})
\]
are tight.
3. The complement of every nonempty proper contiguous subpath of \(A\) is non-Hamiltonian and has path-cover number two.

**Proof.** If \(H[U]\) were Hamiltonian, Hamilton paths on \(A\) and \(U\) would two-cover \(H\). Minimality gives a two-cover of every proper induced subtournament, proving (1).

If \((y,a_0,a_1)\) were tight, prepending \(y\) would give a longer tight path. Hence \((y,a_0,a_1)\) is non-tight and boundary reversal gives \((a_1,a_0,y)\) tight. The other end is symmetric.

Let \(I\) be a nonempty proper contiguous subpath of \(A\). If \(H-I\) were Hamiltonian, Hamilton paths on \(I\) and \(H-I\) would two-cover \(H\). Minimality again gives path-cover number two. \(\square\)

No two-cover of \(U\cup\{a_0,a_1\}\) can have a component ending with \((a_0,a_1)\), since the inherited suffix of \(A\) could then be appended. The symmetric statement holds at the other end. Thus the two reversed endpoint families coexist but cannot be joined directly.

## 3. A five-set or an internal reversal

For \(y\in U\), the first and third triples of
\[
(a_1,a_0,y,a_{\lambda-1},a_{\lambda-2})
\]
are tight by Lemma 3. If
\[
(a_0,y,a_{\lambda-1})
\]
is tight, these five vertices form a Hamilton path.

Suppose instead that this middle triple is non-tight for every \(y\in U\). Then
\[
(a_{\lambda-1},y,a_0)
\]
is tight for every \(y\in U\). Define a tournament on \(U\) by
\[
p\to q
\quad\Longleftrightarrow\quad
(p,a_{\lambda-1},q)\text{ is tight}.
\]
Since \(|U|\ge4\), some \(y\) has an in-neighbor \(w\) and an out-neighbor \(z\). Then
\[
(w,a_{\lambda-1},y,a_0)
\]
is a tight four-path, while
\[
(y,a_{\lambda-1},z)
\]
reverses its internal edge \((a_{\lambda-1},y)\).

Thus:

**Lemma 4.** Either some
\[
(a_1,a_0,y,a_{\lambda-1},a_{\lambda-2})
\]
is a Hamilton path, or a four-vertex tight path contains an explicitly reversed internal edge.

The induced four-set in the second case is Hamiltonian, cyclic non-Hamiltonian, or the edge-orderable matching-block \(K_4\). The Hamiltonian case already has a two-coverable complement. The matching-block case supplies forced reverse relations for further extension.

## 4. A common four-vertex core

Put
\[
D=\{a_1,a_0,a_{\lambda-1},a_{\lambda-2}\}.
\]
Call \(y\in U\) good when \(D\cup\{y\}\) is Hamiltonian in the displayed order. If three vertices of \(U\) are not good, the tournament argument above produces the internal reversal of Lemma 4. Therefore:

**Lemma 5.** Unless the internal-reversal four-set occurs, all but at most two vertices of \(U\) are good.

When \(|U|\ge6\), at least four such labels exist.

**Lemma 6.** If \(|U|\ge6\) and the internal-reversal four-set does not occur, then either
1. \(H\) contains a Hamiltonian six-set with two-coverable complement; or
2. there is a four-set \(C\) and three distinct vertices \(r_1,r_2,r_3\notin C\) such that each \(C\cup\{r_i\}\) is Hamiltonian and has two-coverable complement.

**Proof.** Choose a good \(y\) and put \(X=D\cup\{y\}\). If \(X\cup\{z\}\) is Hamiltonian for another good \(z\), this is (1).

Otherwise at least three good labels fail to enlarge \(X\). For each such label \(z\), some four-vertex deletion \(X-\{x\}\) must accept \(z\); if all five failed, comparison of the five insertion positions and boundary reversal would produce the internal-reversal configuration. By pigeonhole, one deletion \(C=X-\{x\}\) accepts at least two labels \(z_1,z_2\). Then
\[
C\cup\{x\},\quad C\cup\{z_1\},\quad C\cup\{z_2\}
\]
are the three five-sets in (2). Their complements are non-Hamiltonian and have path-cover number two by minimality. \(\square\)

Choose Hamilton orders on the three five-sets. If two induce different orders on \(C\), there is an order disagreement. Otherwise each root is inserted into one gap of a common order on \(C\). Separated gaps give a Hamiltonian six-set; adjacent gaps give either a Hamiltonian six-set or a reverse tight triple through the intervening core vertex; a common internal gap gives a Hamiltonian four-set. If all three roots use one endpoint gap, boundary reversal among the roots gives a Hamiltonian four-set. Thus the common-core case always carries additional ordered information.

## 5. The endpoint-pair family

Assume a displayed end-edge reversal has been chosen maximal with respect to the order of its path and no preceding small Hamiltonian support occurs. Then every other exterior vertex satisfies the reverse relations at both ends. In the difficult orientation one also has
\[
(a_{\lambda-1},y,a_0)
\]
tight for every exterior \(y\).

For distinct \(y,z\), exactly one of
\[
(y,a_{\lambda-1},z),\qquad
(z,a_{\lambda-1},y)
\]
is tight. In the first case
\[
(y,a_{\lambda-1},z,a_0)
\]
is Hamiltonian; in the second, the reversed order is. Therefore every four-set
\[
\{a_0,a_{\lambda-1},y,z\}
\]
is Hamiltonian, and its complement is non-Hamiltonian with path-cover number two.

Among any three exterior vertices, orient \(p\to q\) when \((p,a_{\lambda-1},q)\) is tight. Some vertex has both an in-neighbor and an out-neighbor, yielding two Hamiltonian four-paths whose common pair is ordered oppositely. Thus this endpoint case gives a family of overlapping Hamiltonian four-sets with explicit order disagreement.

## 6. Opposite endpoint replacements

Let \(x,y\notin V(A)\). Suppose \(L\) is a Hamilton path on
\[
(V(A)-\{a_0\})\cup\{x\}
\]
and \(R\) is a Hamilton path on
\[
(V(A)-\{a_{\lambda-1}\})\cup\{y\},
\]
and both preserve the order inherited from \(A\). Assume \(\lambda\ge6\).

**Lemma 7.** The support
\[
(V(A)-\{a_0,a_{\lambda-1}\})\cup\{x,y\}
\]
is Hamiltonian.

**Proof.** Since \(A\cup\{x\}\) is not Hamiltonian, \(x\) can occupy only one of the first two positions relative to \(a_1,\ldots ,a_{\lambda-1}\); otherwise prepending \(a_0\) extends \(A\). Thus
\[
L=(x,a_1,\ldots ,a_{\lambda-1})
\]
or
\[
L=(a_1,x,a_2,\ldots ,a_{\lambda-1}).
\]
Similarly,
\[
R=(a_0,\ldots ,a_{\lambda-2},y)
\]
or
\[
R=(a_0,\ldots ,a_{\lambda-3},y,a_{\lambda-2}).
\]
Delete the old endpoints and combine the corresponding left and right forms. Every consecutive triple is inherited from \(L\), \(R\), or the middle of \(A\), so the resulting order is Hamiltonian. \(\square\)

Thus a difficult pair of opposite endpoint replacements must change the inherited order. Comparing deletion covers at \(a_0\) and \(a_{\lambda-1}\), one obtains either a reversed surviving edge of \(A\), different support partitions on the common double deletion, or an order disagreement on a common support.

## 7. Amplification from an arbitrary reversing triple

Let \(T\) be the vertex set of a reversing tight triple, and let \(J_T\) be the graph on \(V(H)-T\) in which \(yz\) is an edge exactly when \(T\cup\{y,z\}\) is Hamiltonian.

**Lemma 8.**
\[
\alpha(J_T)\le2.
\]

**Proof.** If three exterior vertices were pairwise nonadjacent, each of the three two-vertex extensions of \(T\) would be non-Hamiltonian. Comparing their non-Hamiltonian insertion positions, boundary reversal forces one of the three five-vertex supports to be Hamiltonian, a contradiction. \(\square\)

Thus the complement of \(J_T\) is triangle-free, so Mantel's theorem gives
\[
|E(J_T)|
\ge
\binom{m}{2}-\left\lfloor\frac{m^2}{4}\right\rfloor,
\qquad m=|V(H)-T|.
\]
Every edge gives a Hamiltonian five-set containing the same reversal and having two-coverable complement. Hence some exterior vertex lies in several such edges, producing Hamiltonian five-sets with a common four-vertex core. The insertion-position analysis following Lemma 6 then gives a Hamiltonian four- or six-set, an order disagreement, or another positioned reversal.

## 8. The remaining lemma

The preceding lemmas produce one of the following:
- a Hamiltonian support of order four, five, or six with two-coverable complement and displayed endpoint information;
- three Hamiltonian five-sets with a common four-set;
- the endpoint-pair family of Section 5;
- an order disagreement attached to the two endpoint deletions of a longest path;
- a tight triple reversing an edge in one of these displayed configurations.

**Remaining Lemma.** In a minimum counterexample, any one of these configurations yields a reversal of an end edge of a displayed path occurring in a deletion-cover or three-cover state, or directly yields a two-cover, or yields a spanning ordering of defect span at most \(2\).

A proof completes the longest-path argument.

## Appendix. Two invalid shortcuts

For an ordered triple \((u,v,z)\), the boundary-reversed triple is
\[
(z,v,u),
\]
not \((v,u,z)\). A repeated-cut argument that substitutes the latter therefore uses an unsupported cyclic rotation.

Likewise, a deletion-cover path may contain a small exceptional set without those vertices forming a contiguous interval in the displayed longest-path order. A bound on the size of the exceptional set cannot by itself justify deleting one interval from the longest path.

These observations invalidate the corresponding shortcut arguments but do not affect Lemmas 1–8.