# A longest path

## Composition

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

### Lexicographic longest-path normal form

The global longest-path reduction can be sharpened by extremizing the complementary two-cover as well.

**Lemma 4 (lexicographic three-cover normal form).** Let \(H\) be a minimum counterexample. Choose a globally longest tight path
\[
A=(a_1,\ldots,a_r).
\]
By Lemma 3, \(H-A\) is non-Hamiltonian with path-cover number two. Among all two-covers
\[
H-A=P\mid Q,
\]
choose one for which \(\max\{|P|,|Q|\}\) is maximum, and relabel so that
\[
|P|\ge |Q|.
\]
Write
\[
P=(p_1,\ldots,p_m),\qquad Q=(q_1,\ldots,q_t).
\]

Then every displayed endpoint \(q\in\{q_1,q_t\}\) simultaneously reverses both end edges of both \(A\) and \(P\):
\[
(a_2,a_1,q),\qquad (q,a_r,a_{r-1}),
\]
and
\[
(p_2,p_1,q),\qquad (q,p_m,p_{m-1})
\]
are tight whenever the corresponding paths have order at least two.

Equivalently, \(q\) is noninsertable at every position of the displayed orders of both \(A\) and \(P\).

**Proof.** Since \(A\) is globally longest, \(A\cup\{q\}\) is non-Hamiltonian for every \(q\notin A\). Applying [[endpoint_replacement_truncation_dichotomy01]] to the displayed order of \(A\) shows that \(q\) is noninsertable at every gap of \(A\). In particular the two endpoint insertions fail, and boundary antisymmetry gives
\[
(a_2,a_1,q),\qquad(q,a_r,a_{r-1})
\]
tight.

Now let \(q\) be an endpoint of \(Q\). If \(P\cup\{q\}\) were Hamiltonian, then deleting \(q\) from the displayed endpoint of \(Q\) would leave a tight path \(Q-q\), and
\[
(P\cup\{q\})\mid(Q-q)
\]
would be a two-cover of \(H-A\) whose larger component has order \(|P|+1\). This contradicts the extremal choice of \(P\mid Q\). Thus \(P\cup\{q\}\) is non-Hamiltonian. Applying [[endpoint_replacement_truncation_dichotomy01]] again, now to \(P\), shows that \(q\) is noninsertable at every gap of the displayed order of \(P\). Hence its two endpoint insertion triples are non-tight, and their boundary reversals give
\[
(p_2,p_1,q),\qquad(q,p_m,p_{m-1})
\]
tight. \(\square\)

Thus the smallest component of a lexicographically extremal three-cover is not merely hard to absorb into one neighboring path. Each of its endpoints is simultaneously blocked from both larger paths and reverses both exposed end edges of each.

This converts the general two-cover problem into a two-path merger problem with a common obstruction certificate:

> **Four-ended merger problem.** Let \(A\mid P\mid Q\) be in the lexicographic normal form above. Use one endpoint of \(Q\), or both when \(|Q|\ge2\), together with the simultaneous reversal constraints on \(A\) and \(P\) to construct either a path on \(A\cup P\cup\{q\}\), a lexicographically larger three-cover, or a spanning two-cover.

Unlike the order-eleven reductions, this formulation is valid for arbitrary order and directly targets elimination of one whole path component.


### Endpoint transfer or mutual reversal inside the complement

The lexicographic normal form admits an explicit two-vertex augmentation step.

**Lemma 5 (two-vertex transfer dichotomy).** Work in the setting of Lemma 4, with
\[
P=(p_1,\ldots,p_m),\qquad Q=(q_1,\ldots,q_t),\qquad m\ge t.
\]
Assume \(m\ge3\) and \(t\ge2\).

At the left ends, exactly one of the following holds:

1. the path
   \[
   (p_2,p_1,q_1,q_2,\ldots,q_t)
   \]
   is tight, and therefore
   \[
   (p_2,p_1,q_1,\ldots,q_t)\mid(p_3,\ldots,p_m)
   \]
   is a two-cover of \(H-A\) with component orders
   \[
   t+2,\qquad m-2;
   \]
2. the triple
   \[
   (q_2,q_1,p_1)
   \]
   is tight, so \(p_1\) reverses the initial edge \(q_1q_2\) of \(Q\).

Symmetrically, at the right ends, exactly one of the following holds:

1. the path
   \[
   (q_1,\ldots,q_t,p_m,p_{m-1})
   \]
   is tight, and therefore
   \[
   (p_1,\ldots,p_{m-2})\mid(q_1,\ldots,q_t,p_m,p_{m-1})
   \]
   is a two-cover of \(H-A\) with component orders
   \[
   m-2,\qquad t+2;
   \]
2. the triple
   \[
   (p_m,q_t,q_{t-1})
   \]
   is tight, so \(p_m\) reverses the terminal edge \(q_{t-1}q_t\) of \(Q\).

If \\(m\\ge4\\) and both transfer alternatives hold simultaneously, then
\[
(p_2,p_1,q_1,\ldots,q_t,p_m,p_{m-1})
\]
is a tight path and, together with
\[
(p_3,\ldots,p_{m-2}),
\]
gives a two-cover of \(H-A\) with component orders
\[
t+4,\qquad m-4
\]
when the middle path is nonempty.

**Proof.** By Lemma 4, the left endpoint \(q_1\) is noninsertable at the left end of \(P\), so
\[
(p_2,p_1,q_1)
\]
is tight.

Test the next junction triple
\[
(p_1,q_1,q_2).
\]
If it is tight, then the displayed path
\[
(p_2,p_1,q_1,q_2,\ldots,q_t)
\]
is tight, because all later triples are inherited from \(Q\). The remaining vertices of \(P\) form the inherited path
\[
(p_3,\ldots,p_m).
\]
This proves the left transfer alternative.

If \((p_1,q_1,q_2)\) is non-tight, boundary antisymmetry gives
\[
(q_2,q_1,p_1)
\]
tight, which is the mutual-reversal alternative.

The right-hand statement is symmetric. If both transfer junctions are tight, their two constructions concatenate through the whole displayed order of \(Q\), giving the final path and the inherited middle segment of \(P\). \(\square\)

**Corollary 6 (near-balanced complements force mutual reversal).** Under the same hypotheses:

- if \(m-t\le1\), both ends are in the mutual-reversal alternative;
- if \(m-t\le3\), at least one end is in the mutual-reversal alternative.

**Proof.** A single transfer creates a component of order \(t+2\). If \(m-t\le1\), then \(t+2>m\), contradicting the maximal choice of the larger component \(P\) in Lemma 4. Hence neither transfer is possible.

If both transfers occur, the resulting two-cover has a component of order \(t+4\). When \(m-t\le3\), this exceeds \(m\), again contradicting maximality. Hence at least one transfer must fail, and the corresponding mutual reversal occurs. \(\square\)

Thus, when the complementary two-cover is close to balanced, an endpoint of \(Q\) and the corresponding endpoint of \(P\) reverse one another's exposed end edges, while both endpoints already reverse the two ends of the globally longest path \(A\). This is a genuinely global terminal pattern, independent of the total order of \(H\).


### A longest path forces bounded support at arbitrary order

**Corollary 7 (universal bounded-support reduction).** Let (H) be a minimum counterexample. Then (H) has a proper Hamiltonian support (K) of order at most four such that
[
operatorname{pc}(H-K)=2
]
and (H-K) is non-Hamiltonian.

More precisely, in the lexicographic normal form of Lemma 4,
[
Amid Pmid Q,
qquad |P|ge |Q|,
]
either (|Q|=1), in which case (Q) itself is such a support, or (|Q|ge2), in which case there is a Hamiltonian four-support meeting an endpoint edge of the globally longest path (A).

**Proof.** If (|Q|=1), the singleton (Q) is a proper Hamiltonian support. Its complement is two-covered by (Amid P). It cannot be Hamiltonian, since a Hamilton path on (H-Q) together with the singleton path (Q) would two-cover (H). Hence
[
operatorname{pc}(H-Q)=2.
]

Assume now that
[
Q=(q_1,ldots,q_t),qquad tge2.
]
By Lemma 4, both distinct endpoints (q_1,q_t) reverse the same terminal edge of the globally longest path
[
A=(a_1,ldots,a_r):
]
[
(q_1,a_r,a_{r-1}),
qquad
(q_t,a_r,a_{r-1})
]
are tight.

Choose any vertex
[
y
otin{a_{r-1},a_r,q_1,q_t}.
]
Such a vertex exists because a minimum counterexample has more than ten vertices.

If
[
(y,q_1,a_r)
]
is tight, then
[
(y,q_1,a_r,a_{r-1})
]
is a Hamiltonian four-path. The same conclusion holds with (q_t) in place of (q_1).

Assume therefore that both
[
(y,q_1,a_r),qquad(y,q_t,a_r)
]
are non-tight. Boundary antisymmetry gives
[
(a_r,q_1,y),qquad(a_r,q_t,y)
]
tight. The parallel-middle lemma in [[localextend01]] then makes
[
{a_r,q_1,q_t,y}
]
Hamiltonian.

Thus in every case (H) has a Hamiltonian four-support (K). Since (K) is proper, minimum-counterexample calculus gives
[
operatorname{pc}(H-K)le2.
]
The complement cannot be Hamiltonian, because then (K) together with a Hamilton path on (H-K) would two-cover (H). Therefore
[
operatorname{pc}(H-K)=2.
]
(square)

This is an arbitrary-order reduction: bounded Hamiltonian support is forced directly from a globally longest path and an extremal two-cover of its complement. No bounded-order analysis or numerical case classification is used.

The remaining issue is therefore not whether the general problem reaches bounded support. It does. The relevant question is which additional anchor data on (K) is needed to convert its path-cover-two complement into the one-defect bridge or a two-cover.



### The universal four-support can be chosen mixed across all three components

**Corollary 8 (mixed-anchor refinement).** Work in the lexicographic normal form
[
Amid Pmid Q,
qquad
A=(a_1,ldots,a_r),quad
P=(p_1,ldots,p_m),quad
Q=(q_1,ldots,q_t),
]
with (tge2).

Then (H) has a Hamiltonian four-support (K) with non-Hamiltonian path-cover-two complement such that (K) meets all three displayed components and one of the following holds.

1. For some (qin{q_1,q_t}),
   [
   K={p_1,q,a_{r-1},a_r}.
   ]
   Thus (K) contains the full terminal edge of the globally longest path together with vertices from both complementary paths.

2. 
   [
   K={p_1,q_1,q_t,a_r},
   ]
   and (K) has a Hamilton order whose one endpoint is (a_r) and whose other endpoint lies in ({q_1,q_t}).

**Proof.** Repeat the proof of Corollary 7 with the auxiliary vertex chosen to be
[
y=p_1.
]
Lemma 4 gives
[
(q_1,a_r,a_{r-1}),
qquad
(q_t,a_r,a_{r-1})
]
tight.

If one of
[
(p_1,q_1,a_r),qquad(p_1,q_t,a_r)
]
is tight, say the former, then
[
(p_1,q_1,a_r,a_{r-1})
]
is a Hamilton four-path, giving outcome 1.

Assume both triples are non-tight. Boundary antisymmetry gives
[
(a_r,q_1,p_1),
qquad
(a_r,q_t,p_1)
]
tight. The parallel-middle lemma then gives one of the two Hamilton paths
[
(a_r,q_1,p_1,q_t),
qquad
(a_r,q_t,p_1,q_1).
]
This is outcome 2.

In either case (K) is proper. Minimum-counterexample calculus gives
[
operatorname{pc}(H-K)le2,
]
and the complement cannot be Hamiltonian without two-covering (H). Hence
[
operatorname{pc}(H-K)=2.
]
(square)

Thus the longest-path reduction does not merely force an unspecified small support. It forces a **mixed** four-support tied simultaneously to the longest path and to both paths of an extremal complementary two-cover.

This is the natural bounded interface for the global problem: endpoint deletion from (K) can now be compared against inherited path geometry on all three sides, rather than restarting from an unanchored four-set.



### Opposite extremal covers force a crossing or bidirectional reversal

The transfer dichotomy is more effective when one compares opposite extremal two-covers of the same complement rather than iterating an allowed transfer.

Let
\[
U=H-A,
\]
where \(A\) is globally longest. Choose:

- a **maximally imbalanced** two-cover
  \[
  U=P\mid Q,\qquad |P|\ge |Q|,
  \]
  maximizing \(|P|\); and
- a **maximally balanced** two-cover
  \[
  U=R\mid S,\qquad |R|\ge |S|,
  \]
  minimizing \(|R|-|S|\).

The first cover is the one used in Lemma 4.

**Lemma 7 (dual extremal normal form).** If
\[
|R|-|S|\ge2,
\]
then every displayed endpoint \(r\) of \(R\) is noninsertable at every position of the displayed Hamilton order of \(S\). In particular \(r\) reverses both end edges of \(S\).

**Proof.** Let \(r\) be an endpoint of \(R\). If \(S\cup\{r\}\) were Hamiltonian, deleting \(r\) from the displayed endpoint of \(R\) would leave a tight path \(R-r\), giving the two-cover
\[
(R-r)\mid(S\cup\{r\})
\]
of \(U\). Its component-size difference is
\[
(|R|-1)-(|S|+1)=|R|-|S|-2,
\]
strictly smaller than the chosen minimum. Hence \(S\cup\{r\}\) is non-Hamiltonian. By [[endpoint_replacement_truncation_dichotomy01]], \(r\) is noninsertable at every gap of the displayed order of \(S\); in particular both endpoint insertions fail, so boundary antisymmetry gives the two end-edge reversals. \(\square\)

Thus the complement of a longest path carries reversal certificates in opposite directions: endpoints of the small side of a maximally imbalanced cover reverse the large side, while endpoints of the large side of a maximally balanced cover reverse the small side.

**Lemma 8 (extremal-cover comparison).** With the two covers above, at least one of the following holds.

1. The support partitions coincide:
   \[
   \{V(P),V(Q)\}=\{V(R),V(S)\}.
   \]
   If their common size difference is at least two, then the endpoints on both sides reverse both end edges of the opposite side.
2. Some ordinary edge of one of \(R,S\) joins a vertex of \(P\) to a vertex of \(Q\).

**Proof.** Suppose no ordinary edge of either \(R\) or \(S\) joins \(V(P)\) to \(V(Q)\). Since each of \(R,S\) is connected as an ordinary path, each lies wholly inside one of \(V(P),V(Q)\). Because \(R,S\) partition \(U=V(P)\sqcup V(Q)\) and both old supports are nonempty, one of \(R,S\) equals \(V(P)\) and the other equals \(V(Q)\). Thus the support partitions coincide.

If they coincide and the common size difference is at least two, Lemma 4 applied to the maximally imbalanced realization gives reversal from the smaller side into the larger, while Lemma 7 applied to the maximally balanced realization gives reversal from the larger side into the smaller. \(\square\)

Consequently the general problem on \(H-A\) has only two global geometries:

\[
\boxed{\text{bidirectional end reversal on one fixed partition}}
\]
or
\[
\boxed{\text{a comparison path crossing the two supports}}.
\]

The second case is precisely the kind of cut-interaction disturbance controlled by [[coversurg01]]: a crossing comparison edge, together with an inherited neighbor on one old support, immediately yields a local reversal/cut interaction. The first case is still more rigid: both component endpoints attack the opposite component at both ends.

This is a genuinely global reduction. It uses no bounded-order hypothesis and no assumption that an allowed transfer must be monotone. The next step is to show that either global geometry merges \(P,Q\), or can be spliced through the globally longest path \(A\) to create a path longer than \(A\).


### Longestness forces the same transfer dichotomy across \(A\) and \(P\)

**Lemma 9.** In the lexicographic normal form
\[
A=(a_1,\ldots,a_r),\qquad P=(p_1,\ldots,p_m),\qquad r\ge m\ge2,
\]
exactly one of the following holds at the left end:

1. \((a_2,a_1,p_1,\ldots,p_m)\) is a tight path of order \(m+2\);
2. \((p_2,p_1,a_1)\) is tight.

Exactly one of the following holds at the right end:

1. \((p_1,\ldots,p_m,a_r,a_{r-1})\) is a tight path of order \(m+2\);
2. \((a_r,p_m,p_{m-1})\) is tight.

If both transfer alternatives hold, then
\[
(a_2,a_1,p_1,\ldots,p_m,a_r,a_{r-1})
\]
is a tight path of order \(m+4\).

**Proof.** Longestness of \(A\) gives
\[
(a_2,a_1,p_1),\qquad (p_m,a_r,a_{r-1})
\]
tight. Test \((a_1,p_1,p_2)\). If tight, it completes the left displayed path; otherwise boundary antisymmetry gives \((p_2,p_1,a_1)\). The right side is symmetric, testing \((p_{m-1},p_m,a_r)\). If both tested triples are tight, the two constructions concatenate through \(P\). \(\square\)

**Corollary 10.**
If \(r-m\le1\), both ends of \(A\) and \(P\) are mutually reversing. If \(r-m\le3\), at least one end is mutually reversing.

Indeed, a successful one-sided transfer gives a path of order \(m+2\), while two successful transfers give a path of order \(m+4\); either would exceed the longest-path order \(r\) under the stated inequalities.

Together with Corollary 6, if both
\[
r-m\le1,\qquad m-|Q|\le1,
\]
then each end carries a reversal ladder
\[
A\longleftrightarrow P\longleftrightarrow Q,
\]
and the endpoints of \(Q\) also reverse the corresponding end edges of \(A\).

Thus the arbitrary-order problem now couples component-size gaps to explicit reversal density rather than to any fixed total order.


### A single crossing is a genuine segment transfer from the large side

Continue with the maximally imbalanced cover
\[
U=P\mid Q,\qquad |P|=m\ge t=|Q|,
\]
and a maximally balanced cover
\[
U=R\mid S.
\]
Let \(c\) be the number of ordinary edges of \(R\mid S\) joining \(V(P)\) to \(V(Q)\).

**Lemma 11 (single-crossing augmentation).** If \(c=1\), then the balanced cover does not keep all of \(P\) in one component. Equivalently, it is \(P\), not \(Q\), that is split into two nonempty monochromatic blocks.

More precisely, cutting the unique crossing edge produces three nonempty monochromatic blocks. One is all of \(Q\), while the other two partition \(P\). One path of \(R\mid S\) consists of \(Q\) concatenated with one \(P\)-block, and the other path is the remaining \(P\)-block.

**Proof.** Cutting the unique crossing edge of the two-path forest \(R\mid S\) produces exactly three monochromatic blocks. Since both old classes \(P,Q\) are nonempty, one old class occurs in two blocks and the other in one.

Suppose \(Q\) were the split class. Then \(P\) would occur as one whole block. The unique crossing edge joins that whole \(P\)-block to one nonempty \(Q\)-block, so one component of \(R\mid S\) would have order strictly greater than
\[
|P|=m.
\]
But \(P\mid Q\) was chosen so that \(m\) is the maximum possible component order among all two-covers of \(U\). Contradiction.

Hence \(P\) is split and \(Q\) is one whole block. The unique crossing edge joins \(Q\) to one of the two \(P\)-blocks; the remaining \(P\)-block is the second component. \(\square\)

If, in addition, the two \(P\)-blocks occur as inherited intervals of the displayed order
\[
P=(p_1,\ldots,p_m),
\]
then Lemma 11 is literally a segment transfer:
\[
P=P^{\mathrm{left}}\,P^{\mathrm{right}}
\]
at one inherited cut, and the balanced cover is
\[
(P^{\mathrm{left}}\cup Q)\mid P^{\mathrm{right}}
\]
or its symmetric version, with the first union realized by one tight path.

If the \(P\)-blocks are not inherited intervals, then some inherited edge of \(P\) is split between comparison blocks or one comparison path leaves \(P\) and later returns. Thus:

**Corollary 12 (global augment-or-disturb dichotomy).** Comparing maximally imbalanced and maximally balanced two-covers of \(H-A\) yields one of:

1. the same support partition, with bidirectional endpoint reversal when the size gap is at least two;
2. a genuine transfer of an inherited end segment of the large path \(P\) onto the whole small path \(Q\);
3. a split inherited edge or leave-and-return disturbance in \(P\) or \(Q\).

When there are at least two crossing edges, outcome 3 follows from the block count. When there is exactly one, Lemma 11 gives outcome 2 unless the comparison blocks already disturb the inherited order.

This is the global augmenting-path formulation: the move from maximal imbalance toward maximal balance is either an honest segment transfer or it leaves a concrete path disturbance. No bounded total order is involved.


## Metadata

- ID: longest_paths_and_reversal_structure_a_longest_path
- Kind: section
- Version: 9
- Math version: 9
- Audit: unaudited
- Refutation: unrefuted
- Composition version: 1
- Composition stale: False

## Development tree

- [Subsection 1 — (untitled)](../SUBSECTIONS/longest_paths_and_reversal_structure_a_longest_path_subsection_a.md) (`longest_paths_and_reversal_structure_a_longest_path_subsection_a`; development v9; composition vNone; stale=False)
