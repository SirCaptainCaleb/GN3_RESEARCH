# A longest path

## Body

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



## Metadata

- ID: longest_paths_and_reversal_structure_a_longest_path
- Kind: section
- Version: 6
- Math version: 6
- Audit: unaudited
- Refutation: unrefuted

## Authoring state

- Subsection 1 — HOT, version 6: (untitled)
