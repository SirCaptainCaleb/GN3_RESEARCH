# Global augmentation by complementary path splices

**Summary:** For arbitrary deletion-cover path orders, two complementary splices give a two-cover if at most eight surrounding joining triples are tight. Every counterexample must obstruct one of those joins for every internal vertex pair.

## Statement

Two complementary exchanges of path pieces absorb a deleted vertex when their surrounding joins are tight; boundary reversal supplies one of their opposite central orientations, at arbitrary component orders.

## Body

Let \(H\) be a finite boundary \(3\)-tournament. All path orders in this Section are displayed; concatenation preserves the order inside every displayed block.

### Failed concatenation already supplies an external reversal

**Lemma 1.** Let \(A=(a_1,\ldots,a_r)\) and \(B=(b_1,\ldots,b_s)\) be disjoint tight paths, with \(r,s\ge2\). If their concatenation \(AB\) is not tight, then at least one of
\[
(b_1,a_r,a_{r-1}),\qquad (b_2,b_1,a_r)
\]
is tight.

**Proof.** The only consecutive triples of \(AB\) not inherited from the two paths are
\[
(a_{r-1},a_r,b_1),\qquad (a_r,b_1,b_2).
\]
At least one is non-tight. Its boundary flip is one of the displayed tight triples. \(\square\)

In particular, if \(A\mid B\mid C\) is a three-cover of a tournament with path-cover number greater than two, the lemma applies to every ordered pair of nontrivial displayed paths. A successful concatenation would reduce the cover to two paths. Thus external end-edge reversals are necessary local consequences of the obstruction to concatenation. Their existence alone supplies no additional repartition.

### Two complementary splices through a deleted vertex

Let
\[
H-x=P\mid Q,\qquad
P=(L,a,R),\qquad Q=(M,b,N),
\]
where \(L,R,M,N\) are nonempty contiguous subpaths in the displayed orders. In particular \(a,b\) are internal vertices of their respective paths. Write \(\ell\) and \(m\) for the final vertices of \(L\) and \(M\), and \(r\) and \(n\) for the initial vertices of \(R\) and \(N\).

Consider the two candidate covers
\[
\mathcal C_1=(L,a,x,b,N)\mid(M,R),
\]
\[
\mathcal C_2=(M,b,x,a,R)\mid(L,N).
\]
Each candidate partitions \(V(H)\) into two nonempty vertex sequences. No displayed subpath is reversed.

**Lemma 2 (paired splicing).** If the concatenations \(MR\) and \(LN\) are tight paths, and the four triples
\[
(\ell,a,x),\qquad(x,b,n),\qquad
(m,b,x),\qquad(x,a,r)
\]
are tight, then \(H\) has a two-cover.

More precisely, \(\mathcal C_1\) is a two-cover when \((a,x,b)\) is tight, and \(\mathcal C_2\) is a two-cover when \((b,x,a)\) is tight.

**Proof.** In the first sequence of \(\mathcal C_1\), all consecutive triples are inherited from \(P\) or \(Q\), except
\[
(\ell,a,x),\quad(a,x,b),\quad(x,b,n).
\]
Its second sequence is \(MR\), assumed tight. Hence \(\mathcal C_1\) is a two-cover if \((a,x,b)\) is tight.

Similarly the only noninherited triples in the first sequence of \(\mathcal C_2\) are
\[
(m,b,x),\quad(b,x,a),\quad(x,a,r),
\]
and its second sequence \(LN\) is tight. Hence \(\mathcal C_2\) is a two-cover if \((b,x,a)\) is tight.

The central triples \((a,x,b)\) and \((b,x,a)\) are boundary flips. Exactly one is tight, so one of the two candidate covers is valid. \(\square\)

The hypotheses do not bound the orders of \(L,R,M,N\). The vertex \(x\) is absorbed while pieces of both old paths are exchanged. The boundary-tournament axiom supplies the central orientation; the remaining hypotheses control the new joins.

### Opposite orientation constraints

**Proposition 3.** Assume \(\operatorname{pc}(H)>2\) and retain the displayed decomposition above.

If \(MR\), \((\ell,a,x)\), and \((x,b,n)\) are tight, then \((b,x,a)\) is tight.

If \(LN\), \((m,b,x)\), and \((x,a,r)\) are tight, then \((a,x,b)\) is tight.

Consequently these two collections of hypotheses cannot both hold.

**Proof.** Under the first collection, every consecutive triple in the two sequences of \(\mathcal C_1\) is tight except possibly \((a,x,b)\). If that triple were tight, \(\mathcal C_1\) would two-cover \(H\). It is therefore non-tight and its boundary flip \((b,x,a)\) is tight. The second assertion follows from \(\mathcal C_2\) in the same way. Both conclusions cannot hold because the two triples are boundary flips. \(\square\)

Thus the obstruction has a uniform form over arbitrary path orders: for every choice of internal vertices \(a,b\), at least one of the two complementary concatenations or the four displayed attachment triples fails.

### At most eight joining triples

The concatenation \(MR\) is tight precisely when its present joining triples are tight:
\[
(m^{-},m,r)\quad\text{if }|M|\ge2,\qquad
(m,r,r^{+})\quad\text{if }|R|\ge2,
\]
where \(m^{-}\) precedes \(m\) in \(M\), and \(r^{+}\) follows \(r\) in \(R\).

Likewise \(LN\) is tight precisely when
\[
(\ell^{-},\ell,n)\quad\text{if }|L|\ge2,\qquad
(\ell,n,n^{+})\quad\text{if }|N|\ge2
\]
are tight. These equivalences follow because all other triples are inherited from the original paths.

**Corollary 4.** If \(\operatorname{pc}(H)>2\), then for every such internal pair \(a,b\), at least one present triple among these four joining triples and the four attachment triples of Lemma 2 is non-tight. Its boundary flip is tight.

This corollary eliminates the central triple from the necessary obstruction: its orientation cannot prevent both candidate covers. It does not prove that some internal pair satisfies all the surrounding conditions. Establishing such a pair, possibly after changing the deletion cover, remains the global augmentation problem. The number eight bounds the joins in each proposed surgery, not the order of a counterexample or the number of possible path decompositions.


### A large clean splice grid forces bounded Hamiltonian support

Let
[
H-x=Pmid Q,qquad
P=(p_1,ldots,p_r),qquad
Q=(q_1,ldots,q_s),
]
with (r,sge3).

Call an internal index (iin{2,ldots,r-1}) **(P)-clean** when
[
(p_{i-1},p_i,x)
qquad	ext{and}qquad
(x,p_i,p_{i+1})
]
are both tight. Define (Q)-clean indices analogously:
[
(q_{j-1},q_j,x),
qquad
(x,q_j,q_{j+1})
]
must both be tight.

Let (I,J) be the sets of clean internal indices of (P,Q).

**Lemma 5 (clean-grid incidence bound).** Suppose (operatorname{pc}(H)>2). If
[
|I||J|>4(|I|+|J|),
]
then (H) contains a Hamiltonian support of order four or five.

**Proof.** Fix ((i,j)in I	imes J), and apply Corollary 4 to the internal pair
[
a=p_i,qquad b=q_j.
]
All four attachment triples through (x) are tight by cleanliness. Hence at least one of the four cross-join triples must be non-tight.

These four possible failures are
[
(q_{j-2},q_{j-1},p_{i+1}),
qquad
(q_{j-1},p_{i+1},p_{i+2}),
]
[
(p_{i-2},p_{i-1},q_{j+1}),
qquad
(p_{i-1},q_{j+1},q_{j+2}),
]
whenever the displayed vertices exist; at boundary-clean indices the absent conditions are simply omitted.

Boundary reversal converts each failure into a one-sided hook. The first and fourth types are anchored on a fixed ordered edge of (Q) when (j) is fixed and vary with (i); the second and third types are anchored on a fixed ordered edge of (P) when (i) is fixed and vary with (j).

If some fixed anchor receives three failures of one type, the three-hook consequence of [[localextend01]] produces a Hamiltonian support of order four or five, and we are done.

Assume no such support occurs. Then, for each fixed (jin J), the first failure type can occur for at most two values of (i), and the fourth type can occur for at most two values of (i). Hence these two types cover at most
[
4|J|
]
cells of (I	imes J).

Likewise, for each fixed (iin I), the second and third failure types together cover at most
[
4|I|
]
cells.

Every cell of (I	imes J) must be covered by at least one failure type. Therefore
[
|I||J|le4|I|+4|J|,
]
contrary to the hypothesis. (square)

In a minimum counterexample every proper Hamiltonian support supplied by the lemma has non-Hamiltonian complement of path-cover number two. Thus whenever the clean-index rectangle is large, the general splice problem reduces canonically to the bounded-support comparison regime.

Equivalently, if the bounded-support conclusion is unavailable, then
[
|I||J|le4(|I|+|J|).
]
Hence at least one of the two deletion-cover paths has a high density of **dirty** internal positions, where (x) externally reverses one of the two incident displayed edges. The remaining global augmentation problem is therefore reduced to controlling this dense attachment-failure regime.





### Deep attachment failures are reversal certificates

The clean-grid argument above remains valid, but a single dirty internal position does not by itself force a Hamiltonian four-support.

**Lemma 6 (dirty positions give displayed-edge reversals).** Retain
[
H-x=Pmid Q,qquad P=(p_1,ldots,p_r).
]
For every internal index (2le ile r-1):

- if ((p_{i-1},p_i,x)) is non-tight, then
  [
  (x,p_i,p_{i-1})
  ]
  is tight and reverses the displayed edge (p_{i-1}p_i);

- if ((x,p_i,p_{i+1})) is non-tight, then
  [
  (p_{i+1},p_i,x)
  ]
  is tight and reverses the displayed edge (p_ip_{i+1}).

**Proof.** Each assertion is exactly boundary antisymmetry applied to the failed attachment triple. (square)

No Hamiltonicity conclusion for the corresponding four-set follows from this alone. In particular, if
[
(p_{i-2},p_{i-1},p_i)
]
is an inherited tight triple, then its reversed triple
[
(p_i,p_{i-1},p_{i-2})
]
is non-tight, not tight.

Accordingly Lemma 5 yields only the inequality
[
|I||J|le4(|I|+|J|)
]
when no bounded Hamiltonian support has yet appeared. It does **not** by itself give lower bounds such as
[
|I|ge r-4,qquad |J|ge s-4.
]

The previously stated consequences
[
(r-8)(s-8)le16
]
and the resulting order-(35) reduction therefore do not follow from the clean-grid argument and are withdrawn.

The surviving global splice frontier is therefore exactly the following.

> Either Lemma 5 already produces a Hamiltonian four- or five-support, or the actual clean-index sets satisfy
> [
> |I||J|le4(|I|+|J|).
> ]

This inequality by itself does **not** imply that either path contains many dirty positions: one clean-index set may be small simply because the corresponding path has few internal vertices. An additional balance or lower-bound argument is needed before any reversal-density conclusion can be drawn.

When dirty positions do occur, Lemma 6 converts each of them into a displayed-edge reversal through the deleted vertex. Thus a future density argument may legitimately use dirty positions as reversal certificates, but the clean-grid inequality alone supplies no such density.

The unresolved global augmentation problem is therefore to supplement Lemma 5 with a valid source of clean-index lower bounds, or else to exploit the dirty reversals produced by Lemma 6 without assuming that they are numerous.

## Metadata

- ID: global_augmentation_by_complementary_path_splices
- Kind: section
- Version: 6
- Math version: 6
- Audit: unaudited
- Refutation: unrefuted

## Authoring state

- Subsection 1 — HOT, version 6: (untitled)
