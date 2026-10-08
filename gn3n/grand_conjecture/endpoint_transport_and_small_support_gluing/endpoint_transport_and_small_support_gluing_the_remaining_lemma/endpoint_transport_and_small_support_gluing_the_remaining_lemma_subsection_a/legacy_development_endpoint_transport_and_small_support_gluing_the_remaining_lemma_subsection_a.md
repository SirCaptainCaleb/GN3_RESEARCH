#  — preserved pre-item development

## Development

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
