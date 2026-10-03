# The remaining lemma

## Body


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


## Metadata

- ID: defect_lines_and_spanning_order_compression_the_remaining_lemma
- Kind: section
- Version: 9
- Math version: 9
- Audit: unaudited
- Refutation: unrefuted

## Authoring state

- Subsection 1 — HOT, version 9: (untitled)
