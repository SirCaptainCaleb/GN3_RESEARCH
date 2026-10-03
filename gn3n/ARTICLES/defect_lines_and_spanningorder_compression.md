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

### Endpoint deletion exposes a comparison disturbance

The endpoint-rooted four-support interface can be pushed directly into the comparison-cover interfaces.

**Lemma 8.** Let \(H\) be a minimum counterexample. Let
\[
K=(k_0,k_1,k_2,k_3)
\]
be a Hamiltonian four-path and suppose
\[
H-K=A\mid B
\]
is a two-cover. Put
\[
C=(k_1,k_2,k_3),
\]
and let \(F\) be any deletion cover of \(H-k_0\). Relative to the displayed three-cover
\[
C\mid A\mid B
\]
of \(H-k_0\), at least one of the following holds.

1. \(F\) has an ordinary edge joining a vertex of \(A\) to a vertex of \(B\).
2. An inherited displayed path is split into at least two \(F\)-blocks. Consequently either an inherited displayed edge has its endpoints in different paths of \(F\), or one path of \(F\) leaves that displayed path through a nonempty exterior segment and later returns.
3. The order induced by \(F\) on the contiguous \(C\)-block disagrees with the inherited order \((k_1,k_2,k_3)\).
4. A tight triple reverses an end edge either of \(K\) or of the other displayed block meeting \(C\) in \(F\).
5. \(H\) has a two-cover.

The symmetric statement holds after deleting \(k_3\).

**Proof.** Since \(F\) has two path components while
\[
C\mid A\mid B
\]
has three, the component-drop lemma gives at least one ordinary edge of \(F\) whose endpoints lie in different displayed classes.

Suppose first that \(F\) has at least two such interclass edges. Cutting all interclass edges of \(F\) produces
\[
2+t\ge4
\]
nonempty monochromatic blocks, where \(t\) is the number of interclass edges. If no edge joins \(A\) directly to \(B\), outcome 1 is absent. The three displayed classes are nonempty, so at least one of \(C,A,B\) occurs in at least two blocks. Along its inherited displayed path, choose a first ordinary edge whose endpoints lie in different blocks. If those blocks belong to different paths of \(F\), the inherited edge is split between the two comparison paths. If they lie in the same path of \(F\), maximality of the blocks forces a nonempty exterior segment between them. Thus outcome 2 holds.

It remains to suppose that \(F\) has exactly one interclass edge. Cutting it produces exactly three blocks. Since the three displayed classes are nonempty, each of \(C,A,B\) is one contiguous block. One block is an entire component of \(F\), and the other two are concatenated in the other component.

The isolated block cannot be \(C\). Otherwise the other component is a Hamilton path on \(A\cup B=H-K\); replacing the isolated path on \(C\) by the displayed path \(K\) gives a two-cover of \(H\), outcome 5.

Hence \(C\) is concatenated with one of \(A,B\); call the other block \(D\), and call the isolated block \(E\). If the order induced on \(C\) differs from
\[
(k_1,k_2,k_3),
\]
then two common vertices occur in opposite relative order and outcome 3 holds. Assume therefore that the \(C\)-block has exactly the inherited order.

If the mixed component has order
\[
C\,D,
\]
prepend \(k_0\). Every consecutive triple is then either inherited from \(K\), inherited from the old mixed component, or wholly inside \(D\). Hence \(K\cup D\) is Hamiltonian, and together with \(E\) gives outcome 5.

Thus the only remaining orientation of the mixed component is
\[
D\,C.
\]
Write its final \(D\)-block as
\[
(d_1,\ldots,d_t),
\]
so the comparison path ends
\[
(d_1,\ldots,d_t,k_1,k_2,k_3).
\]
Insert \(k_0\) between \(d_t\) and \(k_1\). If all newly created consecutive triples are tight, the resulting path on \(D\cup K\), together with \(E\), two-covers \(H\). Otherwise boundary antisymmetry reverses a failed joining triple. If
\[
(d_t,k_0,k_1)
\]
fails, then
\[
(k_1,k_0,d_t)
\]
is tight and reverses the initial edge \(k_0k_1\) of \(K\). If \(t\ge2\) and
\[
(d_{t-1},d_t,k_0)
\]
fails, then
\[
(k_0,d_t,d_{t-1})
\]
is tight and reverses the terminal edge of the displayed \(D\)-block. Thus outcome 4 holds. \(\square\)

So an endpoint-rooted Hamiltonian four-support is not a separate terminal obstruction: endpoint deletion converts it into a direct mixed edge, a split/leave-and-return disturbance, an order disagreement, an external end-edge reversal, or a two-cover.

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

### A prescribed endpoint survives reduction to four vertices

The order-five support alternative reduces to the four-support interface.

**Lemma 9.** Let \(H\) be a minimum counterexample, let \(F\subsetneq V(H)\) be a Hamiltonian five-support, and let \(a\in F\) be prescribed. Then there is a Hamiltonian four-set
\[
K\subset F,\qquad a\in K,
\]
such that \(H-K\) is non-Hamiltonian and has path-cover number two.

**Proof.** Choose a Hamilton path on \(F\). It has two endpoints, so at least one endpoint \(z\) is different from the prescribed vertex \(a\). Delete \(z\). The remaining four vertices inherit a Hamilton path, so
\[
K=F-\{z\}
\]
is Hamiltonian and contains \(a\).

The set \(K\) is proper. Minimum-counterexample calculus gives
\[
\operatorname{pc}(H-K)\le2.
\]
If \(H-K\) were Hamiltonian, a Hamilton path on \(K\) together with one on \(H-K\) would form a two-cover of \(H\), contrary to the choice of \(H\). Hence
\[
\operatorname{pc}(H-K)=2.
\]
\(\square\)

Consequently a Hamiltonian support of order four **or five** carrying displayed endpoint information, with two-coverable complement, may always be replaced by an endpoint-rooted Hamiltonian four-support with the same complement property. Lemma 8 of the preceding Section then converts this four-support into a direct mixed edge, a split/leave-and-return disturbance, an order disagreement, an external end-edge reversal, or a two-cover.

Thus the order-five support is no longer an independent terminal interface.

---

## Section — The remaining lemma

<!-- section_id: defect_lines_and_spanning_order_compression_the_remaining_lemma -->


### Two-cut normal form

The defect-line formulation has an exact normalization for three-covers.

**Lemma 9 (two-cut normal form).** Let (H) be a minimum counterexample. Let
[
C=P_1mid P_2mid P_3
]
be any three-cover, and let (pi) be the spanning ordering obtained by concatenating the three displayed path orders. If (a<b) are the two cuts between consecutive components, then
[

u(L_pi)=2,
]
and ({a,b}) is a minimum vertex cover of (L_pi).

Conversely, if (pi=(v_1,ldots,v_n)) is any spanning ordering with (
u(L_pi)=2), then every minimum vertex cover ({a,b}), (a<b), of (L_pi) cuts (pi) into the three tight paths
[
(v_1,ldots,v_a),qquad
(v_{a+1},ldots,v_b),qquad
(v_{b+1},ldots,v_n).
]

**Proof.** The two component boundaries of (C) form a set of cuts whose removal partitions (pi) into three tight intervals. Equivalently, the corresponding two vertices of the defect line meet every defect edge. Hence
[
	au(L_pi)le2.
]
By the defect-line identity,
[

u(L_pi)=	au(L_pi)le2.
]
If (
u(L_pi)le1), the same identity gives (c(pi)le2), so (H) has a two-cover, contrary to the choice of (H). Thus (
u(L_pi)=2), and the two displayed cuts form a minimum vertex cover.

Conversely, if ({a,b}) is a vertex cover of (L_pi), then no defect center lies wholly inside any of the three intervals determined by the cuts after positions (a) and (b). Each interval is therefore a tight path. Since (	au(L_pi)=
u(L_pi)=2), every minimum vertex cover has exactly two vertices. (square)

Thus the compression problem is exactly to eliminate one of the two necessary defect-cover cuts.

### Singleton lifts are entry states, not quadratic minima

Let
[
H-x=Pmid Q
]
be any deletion cover, and consider its singleton lift
[
Pmid{x}mid Q.
]
This state never minimizes
[
Phi(R_1mid R_2mid R_3)=|R_1|^2+|R_2|^2+|R_3|^2
]
in its pairwise-repartition component.

Indeed, since a minimum counterexample has more than ten vertices, one of (P,Q) has order (sge5); write that path as (C=(c_1,ldots,c_s)). The pair
[
(x,c_1)mid(c_2,ldots,c_s)
]
is a two-cover of ({x}cup V(C)). Replacing
[
{x}mid C
]
by this pair changes the affected square terms by
[
2^2+(s-1)^2-1-s^2=4-2s<0.
]
This is the first-step singleton descent already developed in [[line_rooted_small_support_descent_from_deletion_cover_lifts]].

Consequently every component containing a singleton lift contains a strictly smaller-(Phi) state, and every componentwise (Phi)-minimum in a minimum counterexample has all three component orders at least three. Any argument from a deletion cover must therefore treat the singleton lift as a starting state from which descent begins, not as the minimum state itself.

### A same-support reversed end edge gives descent or a neutral root exchange

The useful root-exchange statement is unconditional and belongs to the neutral branch of a trichotomy.

**Lemma 10 (same-support reversal trichotomy).** Let
[
H-x=Pmid Q
]
be a deletion cover, let (P=(p_0,ldots,p_m)) be a displayed Hamilton order, and suppose (P) has another Hamilton order
[
R=(A,p_m,p_{m-1},B)
]
containing the reverse of the displayed terminal edge (p_{m-1}p_m). Put (t=|A|) and (N=|P|). Then one of the following holds.

1. (t=0), and (H) has a two-cover.
2. (t=1), and there is a (Phi)-neutral root exchange: if (A=(a)), then
   [
   H-a=(x,p_m,p_{m-1},B)mid Q
   ]
   is a deletion cover compatible with (Pmid Q) on the common domain.
3. (tge2), and the singleton lift (Pmid{x}mid Q) has a strict pairwise (Phi)-decrease.

**Proof.** Since (H) has no two-cover, (x) cannot be appended to the displayed order (P). Hence
[
(p_{m-1},p_m,x)
]
is non-tight and boundary antisymmetry gives
[
(x,p_m,p_{m-1})
]
tight. Therefore
[
(x,p_m,p_{m-1},B)
]
is a tight path.

If (t=0), this path together with (Q) covers (H). If (tge1), repartition
[
Pmid{x}
]
as
[
Amid(x,p_m,p_{m-1},B).
]
The change in the two affected square terms is
[
t^2+(N-t+1)^2-N^2-1
=-2(t-1)(N-t).
]
Thus (t=1) is exactly the neutral case and (tge2) is strict descent.

When (t=1), write (A=(a)). Restrict the deletion covers at (x) and (a) to (H-{x,a}). They share (Q), and on the other support both induce the order
[
(p_m,p_{m-1},B).
]
Thus they are compatible and (a,x) occupy the same initial insertion slot. (square)

This lemma applies to a **same-support reversal**, meaning an alternate Hamilton order on (V(P)) containing the reversed displayed edge. A tight triple through an exterior vertex that reverses a displayed edge is a different object and does not by itself supply such an alternate Hamilton order. The external-reversal configurations produced earlier in Article III therefore remain an independent interface unless an additional argument converts them to the same-support situation.

### The opposite endpoint of a neutral root exchange cannot remain featureless

The neutral case of Lemma 10 has a strong closure property that does not require any minimality assumption.

**Lemma 11.** Suppose
[
F_x=(a,c_1,ldots,c_r)mid Q,qquad
F_a=(x,c_1,ldots,c_r)mid Q,
qquad rge2,
]
are deletion covers of (H-x) and (H-a), respectively. Put (b=c_r).

Then at least one of the following occurs:

1. (H) has a two-cover;
2. a deletion cover at (b) contains an edge joining a surviving vertex of (Q) to a surviving vertex of ({a,c_1,ldots,c_{r-1}});
3. two relevant deletion covers have an order disagreement on a common support;
4. a tight triple reverses the displayed terminal edge (c_{r-1}b).

**Proof.** Set (c_0=a), put
[
C=(c_0,c_1,ldots,c_{r-1}),
]
and choose a deletion cover (G_b) of (H-b).

If (G_b) is support-compatible with (F_x) but not compatible, outcome 3 holds. If it is compatible, the insertion-slot lemma shows that the omitted labels (x,b) are inserted into the same common support. Since (b) belongs to the varying support of (F_x), the cover (G_b) has support partition
[
(Ccup{x})mid Q,
]
and its Hamilton order on (Ccup{x}) preserves the inherited relative order on (C).

Now suppose (G_b) is support-incompatible with (F_x). Apply the endpoint-comparison lemma of Article I, with the two displayed supports interchanged. Relative to
[
Qmid Cmid{x},
]
the cover (G_b) has at least two interclass path edges. If one joins (Q) directly to (C), outcome 2 holds. Otherwise every interclass edge is incident with (x). Since (x) has degree at most two in a two-path cover, there are exactly two such edges, and the endpoint-comparison lemma implies that (Ccup{x}) is Hamiltonian. If every Hamilton order on this set disagrees with the inherited order on (C), outcome 3 holds; otherwise choose one that preserves that order.

We are therefore reduced to inserting (x) into
[
C=(c_0,c_1,ldots,c_{r-1}),
qquad c_0=a.
]
If (x) is inserted anywhere except the two final gaps of this order—between (c_{r-2}) and (c_{r-1}), or after (c_{r-1})—then the resulting order still ends with
[
c_{r-2},c_{r-1}.
]
Appending (b=c_r) therefore gives a Hamilton path on
[
{x}cup V(P),
]
because ((c_{r-2},c_{r-1},c_r)) is inherited from (P). This also covers the boundary case (r=2), where (c_0=a). Together with (Q), this gives outcome 1.

Hence (x) is inserted either between (c_{r-2}) and (c_{r-1}), or after (c_{r-1}). In the first case, ((x,c_{r-1},b)) must be non-tight, since otherwise (b) could again be appended; therefore
[
(b,c_{r-1},x)
]
is tight and outcome 4 holds.

The only remaining insertion is
[
(a,c_1,ldots,c_{r-1},x).
]
After deleting (a,b), the cover (F_a) induces
[
(x,c_1,ldots,c_{r-1}),
]
while the cover at (b) induces
[
(c_1,ldots,c_{r-1},x).
]
These common-support orders disagree. (square)

Thus a neutral same-slot root exchange immediately feeds the Article I disturbance interfaces; it need not be iterated in search of a large compatible family.

### The five-set clique is transient

The support-compatible clique discovered when a singleton lift has a four-vertex component is valid, but it is not a minimum-state obstruction.

**Lemma 12 (transient five-set clique).** Let
[
H-x=Pmid Q,qquad |P|=4,
]
and put
[
X=V(P)cup{x}.
]
Then (X) is non-Hamiltonian and there is a set
[
Dsubseteq X,qquad |D|ge4,qquad xin D,
]
such that for every (din D), the set (X-{d}) is Hamiltonian. Choosing a Hamilton path (P_d) on each (X-{d}), the deletion covers
[
F_d=P_dmid Q
]
are pairwise support-compatible, and their singleton lifts
[
P_dmid{d}mid Q
]
form a (Phi)-neutral clique.

However, none of these singleton lifts is (Phi)-minimal in its pairwise-repartition component.

**Proof.** If (X) were Hamiltonian, a Hamilton path on (X) together with (Q) would two-cover (H). Since (X) is a non-Hamiltonian five-set, [[smallset01]] implies that at most one of its four-vertex deletions is non-Hamiltonian. Thus the stated set (D) has order at least four and contains (x).

For distinct (d,ein D), the two singleton lifts agree on (Q), while on (X) they replace the two-component cover
[
P_dmid{d}
]
by
[
P_emid{e}.
]
Hence they are adjacent by one pairwise repartition. Their size profiles are all
[
{4,1,|Q|},
]
so these edges are neutral. Restricting (F_d,F_e) after deleting (d,e) gives the common support partition
[
(X-{d,e})mid Q,
]
so the family is pairwise support-compatible.

Finally, each displayed singleton lift has a singleton component. By the singleton-descent argument above, it admits a strict pairwise (Phi)-decrease. (square)

Thus the clique is useful transient structure, but it cannot itself be the terminal minimum state.

### Correct remaining interface

Starting from a deletion cover, one may use its singleton lift as an entry state and descend inside its pairwise-repartition component. A componentwise \(\Phi\)-minimum has no components of order one or two.

The bounded-support alternative is no longer independent. A Hamiltonian five-support carrying prescribed endpoint information reduces to a Hamiltonian four-support retaining that endpoint, with non-Hamiltonian two-coverable complement. Endpoint deletion from the four-support then yields a direct mixed edge, a split/leave-and-return disturbance, an order disagreement, an external end-edge reversal, or a two-cover.

Thus the fixed-deletion, small-support, and comparison arguments reduce the route to four genuinely unresolved interfaces:

1. an **external** tight triple reversing an end edge of a relevant displayed or comparison path;
2. an order disagreement between relevant deletion or comparison covers;
3. a comparison cover with a direct edge joining distinct displayed supports;
4. an inherited displayed path edge split between two comparison paths, or a leave-and-return path disturbance through a nonempty exterior segment.

The first item includes the displayed Hamiltonian four-path reversals produced by fixed-deletion transport. More general positioned reversals can be amplified through the reversal machinery of Article V into bounded Hamiltonian supports, order disagreements, or further positioned reversals; the bounded supports feed back through the four-support comparison above.

A same-support reversed edge is also no longer terminal: Lemma 10 gives a two-cover, strict descent, or the neutral same-slot exchange, and Lemma 11 immediately converts the neutral exchange into the disturbance interfaces above.

**Remaining Lemma.** Each of the four interfaces above yields either a two-cover of \(H\), a strict \(\Phi\)-decrease in the relevant singleton-lift component, or a spanning ordering \(\sigma\) with
\[
\nu(L_\sigma)\le1.
\]

By Lemma 9 and the defect-line identity, a proof completes the defect-compression route.


### The endpoint-rooted four-support interface is universal

The bounded-support route does not need to be reached through fixed-deletion transport. It is present in every minimum counterexample.

**Lemma 13 (universal endpoint-rooted support).** Let \(H\) be a minimum counterexample. Then there exist a Hamiltonian four-set \(X\), a two-cover
\[
H-X=P\mid Q,
\]
and an endpoint \(y\) of \(P\) such that \(H\) has a proper Hamiltonian support \(S\) of order four or five with
\[
y\in S,
\qquad
\operatorname{pc}(H-S)=2.
\]
Moreover the order-five alternative may be reduced, while retaining \(y\), to an endpoint-rooted Hamiltonian four-support with non-Hamiltonian two-coverable complement. Hence every minimum counterexample reaches one of the four disturbance interfaces in the preceding subsection by endpoint deletion from a Hamiltonian four-support.

**Proof.** Minimum-counterexample calculus gives
\[
\operatorname{pc}(H)=3
\]
and \(|V(H)|>10\). Choose any spanning three-cover
\[
A\mid B\mid C.
\]
At least one component has order at least four; choose four consecutive vertices of that component and call their support \(X\). Then \(X\) is a proper Hamiltonian four-set.

By minimum-counterexample calculus,
\[
\operatorname{pc}(H-X)=2.
\]
Choose a two-cover
\[
H-X=P\mid Q.
\]
Since
\[
|V(H-X)|=|V(H)|-4\ge7,
\]
at least one of \(P,Q\) is nontrivial; indeed one has order at least four. Relabel so that \(P\) is nontrivial and choose either displayed endpoint \(y\) of \(P\).

Apply [[ham4_exterior_mixed_support01]] to the Hamiltonian four-set \(X\) and the prescribed exterior vertex \(y\). It gives a Hamiltonian support \(S\) of order four or five containing \(y\); in the four-vertex case \(S\) is obtained from \(X\) by replacing one vertex by \(y\), and in the five-vertex case \(S=X\cup\{y\}\). In either case the same theorem, together with minimum-counterexample calculus, gives
\[
\operatorname{pc}(H-S)=2
\]
and \(H-S\) is non-Hamiltonian.

If \(|S|=5\), Lemma 9 of [[defect_lines_and_spanning_order_compression_a_hamiltonian_five_set_beside_a_long_path]] deletes an endpoint of a Hamilton order of \(S\) different from the prescribed vertex \(y\). Thus it produces a Hamiltonian four-set
\[
K\subset S,\qquad y\in K,
\]
with
\[
\operatorname{pc}(H-K)=2.
\]
Finally Lemma 8 of [[defect_lines_and_spanning_order_compression_an_endpoint_rooted_hamiltonian_four_set]] applies to \(K\): deleting an endpoint of a Hamilton order of \(K\) yields either a direct mixed edge, a split inherited edge or leave-and-return disturbance, an order disagreement, an external end-edge reversal, or a two-cover of \(H\). \(\square\)

**Corollary 14 (route-level reduction).** To prove the grand two-cover statement by the defect-compression strategy, it is not necessary to prove that fixed-deletion transport, quadratic descent, or the support-forest analysis eventually reaches a bounded endpoint-rooted support. Such a support exists in every minimum counterexample independently of those routes. Therefore the unresolved mathematical core of Article III is exactly the conversion of the four disturbance interfaces
\[
\text{external reversal},\qquad
\text{order disagreement},\qquad
\text{direct mixed edge},\qquad
\text{split/leave-and-return}
\]
into a two-cover or a one-cut defect ordering.

The earlier transport and support-forest developments remain useful because they produce these disturbances with additional positional information, but they are no longer required merely to establish reachability of the disturbance regime.


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
