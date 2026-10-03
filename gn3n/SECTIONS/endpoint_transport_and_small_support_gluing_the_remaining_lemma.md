# The remaining lemma

## Body

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



## Metadata

- ID: endpoint_transport_and_small_support_gluing_the_remaining_lemma
- Kind: section
- Version: 5
- Math version: 5
- Audit: unaudited
- Refutation: unrefuted

## Authoring state

- Subsection 1 — HOT, version 5: (untitled)
