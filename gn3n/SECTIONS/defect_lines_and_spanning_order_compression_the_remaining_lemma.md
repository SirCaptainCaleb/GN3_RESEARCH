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


### Direct mixed edges are not a terminal interface

Corollary 9 of [[defect_lines_and_spanning_order_compression_an_endpoint_rooted_hamiltonian_four_set]] removes the direct-mixed-edge case from the route-level obstruction list. In the universal endpoint-rooted four-support supplied by Lemma 13, any comparison deletion cover with an edge joining the two old complement supports either already yields a two-cover or necessarily has at least two interclass transitions. The block count then forces a displayed support to occur in multiple comparison blocks, hence a split inherited edge or a leave-and-return disturbance.

Therefore the universal reduction can be sharpened once more.

**Corollary 15 (three-interface reduction).** Every minimum counterexample contains one of the following three disturbance configurations:

1. an external tight triple reversing an end edge of a relevant displayed or comparison path;
2. an order disagreement between relevant deletion or comparison covers;
3. an inherited displayed path edge split between two comparison paths, or a leave-and-return path disturbance through a nonempty exterior segment.

Consequently the Remaining Lemma need only prove that each of these three configurations yields either a two-cover of \(H\), a strict \(\Phi\)-decrease in the relevant pairwise-repartition component, or a spanning ordering \(\sigma\) with
\[
\nu(L_\sigma)\le1.
\]

**Proof.** Lemma 13 gives an endpoint-rooted Hamiltonian four-support in every minimum counterexample. Lemma 8 converts endpoint deletion from that support into a direct mixed edge, a split/leave-and-return disturbance, an order disagreement, an external end-edge reversal, or a two-cover. Corollary 9 absorbs the direct mixed-edge case into the split/leave-and-return case unless a two-cover already exists. \(\square\)

Thus the remaining defect-compression problem is now purely positional: a reversal of an exposed edge, a disagreement of common path order, or a comparison path that crosses the block structure must make one of the two necessary defect-cover cuts redundant.


### Order disagreement collapses to an external reversal

**Lemma 16.** Every genuine order-disagreement interface in Corollary 15 yields an external tight triple reversing an edge of one of the relevant displayed or comparison paths.

**Proof.** Let (R,S) be the two tight paths whose common vertices occur in different relative orders. A two-vertex tight path has no intrinsic orientation: both orders of its two vertices are tight. Hence if either (R) or (S) has order two, its orientation may be chosen to agree with the relative order induced by the other path, and there is no genuine order disagreement. Thus every unavoidable order disagreement may be represented by two tight paths of order at least three.

Lemma 1 of [[longest_paths_and_reversal_structure_reversals_are_unavoidable]] then applies directly: two tight paths of order at least three with an order disagreement contain a tight triple reversing an edge of one of the two paths. This is exactly the external-reversal interface. (square)

The reduction is independent of how the disagreement was produced. In particular it applies to the comparison-cover disagreements from endpoint deletion, to the opposite-endpoint disagreement in Lemma 11, and to disagreements arising from support-compatible or split-support comparisons.

**Corollary 17 (two-interface reduction).** Every minimum counterexample contains at least one of the following two disturbance configurations:

1. an external tight triple reversing an edge of a relevant displayed or comparison path;
2. an inherited displayed path edge split between two comparison paths, or a leave-and-return path disturbance through a nonempty exterior segment.

Consequently the Remaining Lemma need only show that each of these two configurations yields either a two-cover of (H), a strict (Phi)-decrease in the relevant pairwise-repartition component, or a spanning ordering (sigma) with
[

u(L_sigma)le1.
]

**Proof.** Corollary 15 reduces every minimum counterexample to external reversal, order disagreement, or split/leave-and-return. Lemma 16 absorbs the order-disagreement alternative into external reversal. (square)

Thus all comparison phenomena that preserve path supports and differ only by order have been absorbed into the reversal branch. The unresolved defect-compression problem has only two genuinely different geometries: a locally reversed exposed edge, or a comparison path that crosses the inherited block decomposition.


### External endpoint reversal is the only interface needed for reachability

The split/leave-and-return interface remains a useful comparison configuration, but it is not needed to guarantee entry into the unresolved regime. External endpoint reversals already occur in every minimum counterexample.

**Corollary 18 (single-interface reduction).** Let (H) be a minimum counterexample. Then (H) has a spanning three-cover
[
Amid (u,v)mid C
]
in which a tight triple through (u) or (v) reverses an end edge of one of the displayed complementary paths (A,C).

Consequently, to prove the grand two-cover statement by the defect-compression strategy, it is enough to prove the following single implication:

> whenever a minimum counterexample has a spanning three-cover with an external tight triple reversing an end edge of one displayed component, then (H) has a two-cover, or the relevant pairwise-repartition component admits strict (Phi)-descent, or (H) has a spanning ordering (sigma) with
> [
> 
u(L_sigma)le1.
> ]

**Proof.** Choose any distinct vertices (u,vin V(H)). Lemma 3 of [[longest_paths_and_reversal_structure_reversals_are_unavoidable]] gives
[
operatorname{pc}(H-{u,v})=2.
]
For every two-cover
[
H-{u,v}=Amid C,
]
both displayed paths have order at least two, and the two-vertex middle component ((u,v)) forces one of three endpoint patterns. In each pattern a tight triple through (u) or (v) reverses an exposed end edge of (A) or (C). Hence such an external endpoint reversal exists in every minimum counterexample.

Therefore a proof of the displayed single implication immediately contradicts the existence of a minimum counterexample. The split/leave-and-return configuration of Corollary 17 may still provide additional positional information when it occurs, but it is no longer an independent reachability requirement. (square)

This changes the logical role of the earlier machinery. Endpoint-rooted four-supports, direct mixing, order disagreement, and split/leave-and-return comparisons are now alternative ways to manufacture or enrich a reversal that is already universally available. The central unresolved problem is purely local-to-global: convert one externally reversed displayed end edge into a one-cut defect ordering (or into strict descent or a two-cover).


### Universal reversals are entry states, not terminal minima

Corollary 18 requires the same qualification as the earlier singleton-lift discussion. The universal two-vertex-middle reversal state is never a quadratic minimum, so allowing bare strict descent as a successful conclusion makes the proposed single-interface implication vacuous.

**Lemma 19 (two-vertex-middle descent).** Let
\[
A\mid U\mid C
\]
be any spanning three-cover of a minimum counterexample \(H\), with \(|U|=2\). Then this state admits a strict pairwise \(\Phi\)-decrease.

**Proof.** Write \(|A|=r\), \(|C|=s\). Since \(|V(H)|>10\),
\[
r+s=|V(H)|-2\ge9,
\]
so after interchanging \(A,C\) we may assume \(r\ge5\). Let \(a\) be an endpoint of the displayed path \(A\). Then \(A-\{a\}\) inherits a tight path of order \(r-1\), while the three-set
\[
U\cup\{a\}
\]
has a Hamilton tight path: for any choice of middle vertex, boundary antisymmetry chooses one of the two orders of the remaining vertices.

Thus
\[
A\mid U
\quad\longrightarrow\quad
(A-\{a\})\mid (U\cup\{a\})
\]
is a legal pairwise repartition. Its change in quadratic potential is
\[
(r-1)^2+3^2-r^2-2^2
=6-2r<0.
\]
\(\square\)

In particular, the universal reversal state supplied by Corollary 18 is an **entry state**, not a terminal obstruction. A statement of the form

> external endpoint reversal \(\Rightarrow\) two-cover, strict descent, or one-cut compression

does not by itself complete the proof: Lemma 19 supplies the strict-descent alternative before the reversal is used at all, and the descended state need not retain that reversal.

Accordingly the logical target must be strengthened in one of two ways.

1. **Direct compression:** every external endpoint-reversal configuration yields a two-cover or a spanning ordering \(\sigma\) with
   \[
   \nu(L_\sigma)\le1,
   \]
   without using unqualified descent as an escape; or
2. **reversal-preserving descent:** a strict descent from an external endpoint-reversal state can be chosen so that the descended state still carries an external endpoint reversal (or another certified terminal disturbance), and this invariant persists until a componentwise \(\Phi\)-minimum is reached.

Absent such a persistence statement, Corollary 18 is a reachability observation only. It does not eliminate the minimum-state disturbance analysis of Corollary 17.

Thus the current proof frontier is sharper: either prove **direct one-cut compression from an external endpoint reversal**, or prove a **descent invariant** that transports reversal/disturbance data all the way to a quadratic minimum.


## The universal four-support is immediate

### The first descent can preserve the universal reversal

The strict descent from Lemma 19 can be chosen so that the exposed endpoint reversal survives.

**Lemma 20 (reversal-preserving first descent).** Let
\[
A\mid (u,v)\mid C
\]
be one of the universal reversal states supplied by Corollary 18. Then there is a strict pairwise \(\Phi\)-decrease to a spanning three-cover
\[
A'\mid X\mid C'
\]
with
\[
|X|=3,
\]
such that an external tight triple through one of \(u,v\) still reverses an end edge of \(A'\) or \(C'\).

**Proof.** Write
\[
A=(a_1,\ldots,a_r),\qquad C=(c_1,\ldots,c_s).
\]
Since \(r+s\ge9\), one of \(r,s\) is at least five.

By Lemma 3 of [[longest_paths_and_reversal_structure_reversals_are_unavoidable]], the two-vertex-middle state has one of three endpoint patterns.

In the first pattern, one or both of \(u,v\) reverse the terminal edge
\[
a_{r-1}a_r
\]
of \(A\). If \(r\ge5\), move the opposite endpoint \(a_1\) from \(A\) into the two-set \(\{u,v\}\). The residual path
\[
A'=(a_2,\ldots,a_r)
\]
retains the reversed terminal edge, while \(\{u,v,a_1\}\) has a Hamilton tight order. Thus the reversal survives. If instead \(s\ge5\), transfer the endpoint \(c_s\) from \(C\); \(A\) is unchanged, so its reversal survives.

The second endpoint pattern is symmetric.

In the third pattern, after naming the middle vertices \(z,w\), the vertex \(w\) reverses both exposed end edges,
\[
a_{r-1}a_r
\qquad\text{and}\qquad
c_1c_2.
\]
Choose a side of order at least five and transfer the endpoint opposite its reversed edge: \(a_1\) from \(A\), or \(c_s\) from \(C\). The other reversal is untouched, and the reversal on the shortened side is also untouched.

In every case the transferred endpoint together with \(u,v\) forms a Hamiltonian three-set, so the pairwise repartition is legal. If the donor side has order \(m\ge5\), the two affected component orders change from
\[
(m,2)\quad\text{to}\quad(m-1,3),
\]
and hence
\[
\Delta\Phi=(m-1)^2+3^2-m^2-2^2
=6-2m<0.
\]
Thus the descent is strict and the external endpoint reversal persists. \(\square\)

Lemma 20 repairs the first step of the persistence route: the universal reversal is not merely present before descent; it can be carried into the order-three regime. From there [[three_cover_repartitions_and_recurrence_moving_away_from_a_three_vertex_side]] becomes the natural next interface. The remaining persistence question is therefore narrower:

> starting from a three-cover with a three-vertex component and a certified external endpoint reversal on another component, can every further strict descent be chosen to preserve a certified reversal or else produce direct one-cut compression?


### The order-three persistence obstruction is one-sided

The reversal-preserving route can be pushed one step further.

**Lemma 21 (one-sided obstruction after the first descent).** Let
\[
X\mid P\mid Q
\]
be a spanning three-cover of a minimum counterexample, where \(|X|=3\), and suppose an external tight triple through a vertex of \(X\) reverses the terminal edge
\[
p_{m-1}p_m
\]
of
\[
P=(p_1,\ldots,p_m).
\]
Then at least one of the following holds.

1. There is a strict pairwise \(\Phi\)-decrease after which a certified external endpoint reversal still survives.
2. The same pairwise-repartition component reaches a Hamiltonian support of order four or five carrying endpoint information, hence the bounded-support comparison regime.
3. All three component orders are at most four.
4. The following one-sided residue occurs:
   \[
   |Q|\le4,\qquad m\ge5,
   \]
   the four-set \(X\cup\{p_m\}\) is Hamiltonian, but \(X\cup\{p_1\}\) is non-Hamiltonian.

The symmetric statement holds for a reversal of the initial edge of \(P\).

**Proof.** First suppose \(|Q|\ge5\). Apply Lemma 3 of [[three_cover_repartitions_and_recurrence_moving_away_from_a_three_vertex_side]] to the pair \(X\mid Q\). If it yields strict descent, only \(X\) and \(Q\) are repartitioned, so the path \(P\) and its reversed terminal edge remain untouched; outcome 1 holds. Otherwise that lemma produces a Hamiltonian four- or five-support with endpoint information, giving outcome 2.

Hence assume \(|Q|\le4\). If also \(m\le4\), outcome 3 holds. Thus we may assume \(m\ge5\).

Apply the same three-vertex-side analysis to \(X\mid P\). If \(X\cup\{p_1\}\) is Hamiltonian, transfer the endpoint \(p_1\) into \(X\). The residual path
\[
(p_2,\ldots,p_m)
\]
retains the reversed terminal edge \(p_{m-1}p_m\), and the move changes the affected orders from \((3,m)\) to \((4,m-1)\), with
\[
\Delta\Phi=8-2m<0.
\]
Thus outcome 1 holds.

If neither \(X\cup\{p_1\}\) nor \(X\cup\{p_m\}\) is Hamiltonian, Lemma 3 produces a bounded Hamiltonian four- or five-support, giving outcome 2.

The only remaining possibility is therefore that \(X\cup\{p_m\}\) is Hamiltonian while \(X\cup\{p_1\}\) is not. This is outcome 4. \(\square\)

Thus, after the universal reversal has been carried into the order-three regime, reversal-preserving descent fails only at a sharply asymmetric local configuration: the opposite complementary path has order at most four, and the reversed side admits extension only at the very endpoint whose incident edge is being reversed. Any proof of persistence need now address only this one-sided residue (plus the bounded \(3|4|4\) profile).


### The one-sided obstruction also preserves a reversal

The asymmetric residue in Lemma 21 is not a genuine failure of the reversal invariant. Although the old reversed edge disappears under the only available endpoint transfer, the resulting four-component forces a new endpoint reversal.

**Lemma 22 (reversal regeneration after the one-sided transfer).** In outcome 4 of Lemma 21, write
[
Xmid Pmid Q,qquad
P=(p_1,ldots,p_m),
]
where (|X|=3), (mge5), (Xcup{p_m}) is Hamiltonian, and (Xcup{p_1}) is non-Hamiltonian. Then there is a strict pairwise (Phi)-decrease to a spanning three-cover that still contains a certified external endpoint reversal.

**Proof.** Choose a Hamilton path (Y) on
[
V(Y)=Xcup{p_m}.
]
The inherited prefix
[
R=(p_1,ldots,p_{m-1})
]
is a tight path. Hence
[
Xmid Pmid Q
longrightarrow
Ymid Rmid Q
]
is a legal pairwise repartition. The affected component orders change from
[
(3,m)quad	ext{to}quad(4,m-1),
]
so
[
DeltaPhi
=
4^2+(m-1)^2-3^2-m^2
=
8-2m<0
]
because (mge5).

Now apply the theorem *A displayed four-path is reversed or reverses both ends of its partner* from [[line_rooted_small_support_descent_from_deletion_cover_lifts]] to the displayed pair (Ymid R). Since (H) is a minimum counterexample, one of the following holds:

- a tight triple through a vertex of (R) reverses an end edge of the displayed four-path (Y); or
- both displayed end edges of (R) are reversed through endpoints of (Y).

In either case the descended three-cover (Ymid Rmid Q) contains a certified external endpoint reversal. Thus the strict descent preserves the reversal invariant, although generally with a different reversing triple from the one present before the move. (square)

Combining Lemmas 20–22, every strict descent encountered from the universal two-vertex-middle reversal state through the order-three regime can be chosen so that a certified external endpoint reversal survives, except possibly when the process reaches the bounded profile
[
3mid4mid4.
]

Thus the persistence frontier has collapsed to a single bounded size profile. The remaining question is no longer whether a reversal can survive arbitrary long-path descent; it is whether a (3|4|4) state carrying a certified external endpoint reversal already compresses directly, or can be moved neutrally to a state where strict reversal-preserving descent resumes.


### Neutral endpoint swaps preserve the reversal invariant in (3|4|4)

The remaining (3|4|4) profile is an absolute minimum of the quadratic potential, so its natural dynamics are neutral rather than descending. The reversal invariant nevertheless survives the basic neutral move.

**Lemma 23 (neutral reversal persistence in (3|4|4)).** Let
[
Tmid Amid B
]
be a spanning three-cover of a minimum counterexample with
[
|T|=3,qquad |A|=|B|=4,
]
and suppose a tight triple through a vertex (win T) reverses an end edge of one of the displayed four-paths, say
[
A=(a_1,a_2,a_3,a_4),
qquad
(w,a_4,a_3) 	ext{tight}.
]
Suppose a displayed (3|4) pair admits a neutral endpoint swap
[
3|4longrightarrow4|3.
]
Then the resulting (3|4|4) state also contains a certified external endpoint reversal.

**Proof.** There are two cases according to which four-side participates in the swap.

First suppose the neutral swap repartitions (Tmid B). The component (A) is unchanged. Every vertex of the old (T), including (w), belongs to the new four-component produced from (T) together with one endpoint of (B). Hence (w) remains external to (A), and the same tight triple
[
(w,a_4,a_3)
]
still reverses the terminal edge of (A).

Now suppose the swap repartitions (Tmid A). If the endpoint (a_1) is transferred into (T), the residual three-path
[
(a_2,a_3,a_4)
]
still contains the reversed terminal edge (a_3a_4), while (w) belongs to the new four-component. Thus the same reversing triple survives.

It remains that the endpoint (a_4) is transferred into (T). Let (Y) be a Hamiltonian four-path on
[
V(T)cup{a_4},
]
and let
[
A'=(a_1,a_2,a_3)
]
be the residual three-path. The old reversed edge (a_3a_4) is no longer contained in one displayed component. However the third component (B) is still a displayed Hamiltonian four-path. Apply the theorem *Two displayed four-paths force an end-edge reversal* from [[line_rooted_small_support_descent_from_deletion_cover_lifts]] to the pair (Ymid B). It supplies a tight triple through one of these components reversing an end edge of the other. Hence the new three-cover again carries a certified external endpoint reversal. (square)

Therefore every neutral endpoint-swap edge in the (3|4|4) state graph preserves the property
[
	ext{“some displayed component has an externally reversed end edge.”}
]
Combined with Lemmas 20–22, the reversal invariant now survives both all strict descents identified by the order-three analysis and all neutral (3|4leftrightarrow4|3) endpoint swaps at the terminal balanced profile.

The remaining (3|4|4) difficulty is consequently not loss of the reversal under reconfiguration. It is the genuinely terminal question: use a reversal that persists throughout the absolute-minimum neutral component to obtain a two-cover or a one-cut defect ordering.


### Every prescribed root has a canonical order-eleven reversal state

The terminal (3|4|4) profile has a stronger normal form than neutral persistence alone suggests. At order eleven, the three-component may be required to contain any prescribed vertex, while the two four-components simultaneously admit Hamiltonian extensions through that vertex.

**Lemma 24 (prescribed-root terminal normal form).** Let (H) be a minimum counterexample of order eleven, and prescribe any vertex (xin V(H)). Then there exist distinct vertices (p,q
e x) and disjoint Hamiltonian four-sets (C,D) such that
[
V(H)=Cmathbin{dotcup}Dmathbin{dotcup}{p,q,x},
]
with all of
[
C,qquad D,qquad Ccup{x},qquad Dcup{x}
]
Hamiltonian. Consequently
[
Cmid Dmid{p,q,x}
]
is a spanning (4|4|3) three-cover containing a certified external endpoint reversal.

**Proof.** By the order-eleven consequence in [[extremal01]], the deletion (H-x) has an equitable Hamiltonian two-cover
[
H-x=Pmid Q,
qquad |P|=|Q|=5.
]
Both six-sets
[
V(P)cup{x},
qquad
V(Q)cup{x}
]
are non-Hamiltonian, since Hamiltonicity of either would give a spanning (6|5) two-cover of (H).

Apply the prescribed Hamiltonian (K_4)-overlap theorem from [[extremal01]] to the non-Hamiltonian six-set (V(P)cup{x}), prescribing the good deletion (x). It yields (pin V(P)) such that both
[
C=V(P)-{p}
]
and
[
Ccup{x}
]
are Hamiltonian. Applying the same theorem to (V(Q)cup{x}) gives (qin V(Q)) such that
[
D=V(Q)-{q}
]
and
[
Dcup{x}
]
are Hamiltonian.

The remaining three vertices are exactly ({p,q,x}), and every three-vertex boundary tournament has a Hamiltonian tight path. Hence
[
Cmid Dmid{p,q,x}
]
is a spanning (4|4|3) cover.

Finally choose displayed Hamiltonian four-paths on (C) and (D). The theorem *Two displayed four-paths force an end-edge reversal* from [[line_rooted_small_support_descent_from_deletion_cover_lifts]] applies to the pair (Cmid D): a tight triple through one four-component reverses an end edge of the other. Thus the canonical state carries a certified external endpoint reversal. (square)

This normal form is stronger than merely knowing that some (3|4|4) minimum state carries a reversal. The root (x) is arbitrary, and it simultaneously Hamiltonian-extends **both** four-components:
[
C+x,qquad D+x.
]
Therefore the terminal order-eleven problem may be studied under this synchronized extension hypothesis without loss of generality.

In particular, the persistence route and the equitable-deletion route meet at the same terminal object. The remaining obstruction can be stated purely at order eleven:

> rule out a minimum counterexample admitting, for every prescribed root (x), a (4|4|3) cover (C|D|{p,q,x}) such that (C+x) and (D+x) are Hamiltonian and the two four-components carry an external endpoint reversal.

The extra simultaneous extensions through (x) are the new structure available for attacking the final one-cut compression step.


### The quiet order-eleven residue is a double same-slot square

The prescribed-root normal form has three naturally linked deletion covers. Their compatibility already forces a much more rigid terminal configuration.

**Lemma 25 (double same-slot reduction).** In the setting of Lemma 24, write
[
P=Ccup{p},qquad Q=Dcup{q},
]
and choose Hamilton orders witnessing
[
F_x=Pmid Q,qquad
F_p=(Ccup{x})mid Q,qquad
F_q=Pmid(Dcup{x}).
]
Then, on each of the two four-cores (C,D), one of the following occurs:

1. the corresponding pair of deletion covers has an order disagreement on the common four-core;
2. the omitted labels occupy adjacent insertion slots, in which case the insertion-slot lemma produces a tight reversing triple through the unique common vertex between the two slots;
3. the omitted labels occupy exactly the same insertion slot.

Consequently, if neither spoke produces order disagreement nor an adjacent-slot reversing triple, there are Hamilton orders
[
C=(c_1,c_2,c_3,c_4),qquad
D=(d_1,d_2,d_3,d_4)
]
such that (p) and (x) occupy the same insertion slot in (C), while (q) and (x) occupy the same insertion slot in (D).

**Proof.** Restrict (F_x) and (F_p) to the common vertex set (H-{x,p}). Both induce the support partition
[
Cmid Q.
]
If their common-support orders disagree, outcome 1 holds. Otherwise the covers are compatible. Lemma 3 of [[deletion_covers_and_the_support_graph_compatibility_of_deletion_covers]] applies: the omitted labels (x,p) are inserted into the same common support, namely (C), and their insertion slots are equal or adjacent. If adjacent, that lemma gives a tight triple reversing the two inserted labels across the intervening core vertex, which is outcome 2. Otherwise the slots are equal, giving outcome 3.

The same argument applied to (F_x,F_q), after restricting to (H-{x,q}), uses the common support partition
[
Pmid D
]
and yields the identical trichotomy for (x,q) on (D). (square)

Thus the terminal order-eleven obstruction has a precise quiet form. After excluding the already-developed order-disagreement and reversing-triple branches, the prescribed root (x) is synchronized with both displaced labels:
[
p 	ext{and} x 	ext{share one slot of }C,
qquad
q 	ext{and} x 	ext{share one slot of }D.
]

This is stronger than the mere simultaneous Hamiltonicity
[
C+p, C+x, D+q, D+x.
]
The four five-sets are now aligned by common core orders and insertion positions. The remaining order-eleven problem can therefore be attacked as a finite slot-synchronization problem: show that a double same-slot square either creates a cross-extension, a two-cover, or a one-cut defect ordering.


### Near-end same slots force a two-cover

The double same-slot residue has only three viable slot positions on each four-core.

**Lemma 26 (near-end slots are impossible).** In the quiet case of Lemma 25, let
[
C=(c_1,c_2,c_3,c_4)
]
be the common core order for (p,x). Then their common insertion slot cannot be between (c_1,c_2) or between (c_3,c_4). Hence the only possible common slots on (C) are:

- before (c_1);
- between (c_2,c_3);
- after (c_4).

The same conclusion holds for the common insertion slot of (q,x) in
[
D=(d_1,d_2,d_3,d_4).
]

**Proof.** Suppose first that (p,x) are both inserted between (c_1,c_2). Then
[
(c_1,p,c_2,c_3,c_4)
qquad	ext{and}qquad
(c_1,x,c_2,c_3,c_4)
]
are tight Hamilton paths.

Boundary antisymmetry on the triple ({p,c_1,x}) says exactly one of
[
(x,c_1,p),qquad (p,c_1,x)
]
is tight. In the first case
[
(x,c_1,p,c_2,c_3,c_4)
]
is a Hamilton tight path on (Ccup{p,x}); in the second case
[
(p,c_1,x,c_2,c_3,c_4)
]
is such a path. Thus (Ccup{p,x}) is Hamiltonian.

But its complementary five-set is
[
Dcup{q}=Q,
]
which is Hamiltonian by construction. These two disjoint Hamilton paths give a spanning two-cover of (H), contradiction.

Now suppose (p,x) are both inserted between (c_3,c_4). Then
[
(c_1,c_2,c_3,p,c_4)
qquad	ext{and}qquad
(c_1,c_2,c_3,x,c_4)
]
are tight. Exactly one of
[
(p,c_4,x),qquad (x,c_4,p)
]
is tight. Accordingly one of
[
(c_1,c_2,c_3,p,c_4,x),
qquad
(c_1,c_2,c_3,x,c_4,p)
]
is a Hamilton tight path on (Ccup{p,x}). Again (Q=Dcup{q}) supplies the complementary Hamilton five-path, giving a two-cover of (H), contradiction.

Thus neither near-end internal slot is possible. The argument for (D) is identical, with complementary Hamilton five-set (P=Ccup{p}). (square)

Hence the exact-slot synchronization problem has only three local states per core:
[
	ext{left endpoint},qquad
	ext{central gap},qquad
	ext{right endpoint}.
]
The quiet order-eleven residue is therefore reduced from twenty-five slot pairs to nine.


## Slot synchronization reductions

### Central slots and opposite endpoint slots

The nine slot pairs left by Lemma 26 separate into two immediate structural classes.

**Lemma 27 (central bridge or cross reversal).** Work in the quiet double same-slot square of Lemma 25.

1. Suppose the common insertion slot of (p,x) in
   [
   C=(c_1,c_2,c_3,c_4)
   ]
   is the central gap between (c_2,c_3). Then
   [
   {c_2,c_3,p,x}
   ]
   is a Hamiltonian four-set. The analogous statement holds on (D).

2. Suppose the common slot of (p,x) in (C) is the right endpoint slot and the common slot of (q,x) in
   [
   D=(d_1,d_2,d_3,d_4)
   ]
   is the left endpoint slot. Then either (H) has a two-cover or
   [
   (d_1,x,c_4)
   ]
   is tight. Symmetrically, if the slots are left on (C) and right on (D), then either (H) has a two-cover or
   [
   (c_1,x,d_4)
   ]
   is tight after the corresponding reversal of notation.

**Proof.** For (1), the two Hamilton paths on (Ccup{p}) and (Ccup{x}) induce the same core order and insert their exceptional vertices into the same internal edge (c_2c_3). Lemma 4(3) of the compatible one-vertex extension calculus gives a Hamilton path on the four-set ({c_2,c_3,p,x}).

For (2), the endpoint-slot assumptions give Hamilton paths
[
(c_1,c_2,c_3,c_4,x)
qquad	ext{and}qquad
(x,d_1,d_2,d_3,d_4).
]
Hence every consecutive triple in
[
(c_1,c_2,c_3,c_4,x,d_1,d_2,d_3,d_4)
]
is tight except possibly
[
(c_4,x,d_1).
]
If this triple is tight, the displayed nine vertices form one tight path; the remaining two vertices are (p,q), which form a tight two-vertex path. Thus (H) has a two-cover.

Therefore in a minimum counterexample ((c_4,x,d_1)) is non-tight. Boundary antisymmetry gives
[
(d_1,x,c_4)
]
tight. The opposite orientation is symmetric. (square)

Thus after Lemmas 25--27 the exact-slot residue has only three genuinely different forms:

- at least one core uses the central slot, producing a Hamiltonian four-bridge through (x) and its displaced label;
- the two cores use opposite endpoint slots, producing an explicit cross reversal through (x);
- both cores use endpoint slots on the same side.

The last case is the only endpoint-slot pattern with no additional structure yet forced.

### Reciprocal swaps force a three-extension common core

**Lemma 28.** In the order-eleven normal form
[
H-x=Pmid Q,quad P=Ccup{p},quad Q=Dcup{q},
]
there is a four-set (E) with three distinct vertices (r_1,r_2,r_3
otin E) such that every (Ecup{r_i}) is Hamiltonian and has two-coverable complement.

**Proof.** By [[extremal01]], (Pmid Q) has at least five double-good reciprocal-swap cells. If one uses row (p), say ((p,d)), then (C+p,C+x,C+d) are three Hamiltonian extensions of (C). A cell in column (q) is symmetric.

Otherwise all five cells lie in the (4	imes4) matrix (C	imes D). Some row or column has degree at least two. Suppose (cin C) has distinct neighbors (d_1,d_2in D), and put
[
E=(C-{c})cup{p}.
]
Then (E+c=P) is Hamiltonian, and double-goodness gives (E+d_1,E+d_2) Hamiltonian. Their complements are two-coverable: for (E+c) use (Qmid{x}); for (E+d_i), use the swapped Hamiltonian five-set ((Q-{d_i})cup{c}) together with ({x}). The column case is symmetric. (square)

Hence every balanced order-eleven deletion state enters the three-extension configuration of [[longest_paths_and_reversal_structure_a_common_four_vertex_core]]. The same-direction endpoint residue cannot remain isolated under reciprocal-swap mobility.



## Same-side endpoint reduction

### Same-side endpoint squares return to bounded support

**Lemma 29 (same-side endpoint reduction).** In the quiet double same-slot square of Lemma 25, suppose both cores use endpoint slots on the same side. Then either (H) has a two-cover, or (H) contains a Hamiltonian support of order four or five whose complement is non-Hamiltonian with path-cover number two.

**Proof.** Reverse both core orders if necessary, so that the common slots are the left endpoint slots. Thus
[
(p,c_1,c_2,c_3,c_4),qquad
(x,c_1,c_2,c_3,c_4)
]
and
[
(q,d_1,d_2,d_3,d_4),qquad
(x,d_1,d_2,d_3,d_4)
]
are Hamilton paths.

Consider the two-cover
[
Cmid Q,qquad Q=(q,d_1,d_2,d_3,d_4)
]
of (H-{p,x}). Both (p) and (x) attach at the left endpoint of (C). If either also attached at the left endpoint of (Q), assigning the two omitted labels to different components would give a two-cover of (H). Hence
[
(p,q,d_1),qquad(x,q,d_1)
]
are non-tight, and boundary antisymmetry gives
[
(d_1,q,p),qquad(d_1,q,x)
]
tight.

Similarly, from the two-cover
[
Dmid P,qquad P=(p,c_1,c_2,c_3,c_4)
]
of (H-{q,x}), absence of a two-cover forces
[
(q,p,c_1),qquad(x,p,c_1)
]
non-tight, and hence
[
(c_1,p,q),qquad(c_1,p,x)
]
tight.

Put
[
K_C={c_1,p,q,x},qquad
K_D={d_1,p,q,x}.
]
If (K_C) is Hamiltonian, its complement is two-covered by
[
(c_2,c_3,c_4)mid(d_1,d_2,d_3,d_4).
]
That complement cannot be Hamiltonian, since together with (K_C) it would two-cover (H). Thus its path-cover number is two. The same argument applies if (K_D) is Hamiltonian.

It remains that both (K_C) and (K_D) are non-Hamiltonian. They share the three-set
[
T={p,q,x}.
]
By the small-order theorem that two non-Hamiltonian four-sets (Tcup{u}) and (Tcup{v}) force their five-vertex union to be Hamiltonian,
[
F={c_1,d_1,p,q,x}
]
is Hamiltonian. Its complement is two-covered by
[
(c_2,c_3,c_4)mid(d_2,d_3,d_4).
]
Again the complement cannot be Hamiltonian, or (F) together with it would two-cover (H). Hence its path-cover number is exactly two. (square)

Thus the same-side endpoint square feeds directly back into the bounded four/five-support comparison machinery.

### The central slot is also bounded support

**Lemma 30 (central-slot reduction).** In the quiet double same-slot square of Lemma 25, suppose the common slot of (p,x) in
[
C=(c_1,c_2,c_3,c_4)
]
is the central gap between (c_2,c_3). Then either (H) has a two-cover, or (H) contains a Hamiltonian four-support whose complement is non-Hamiltonian with path-cover number two.

**Proof.** Lemma 27 gives the Hamiltonian four-set
[
K={c_2,c_3,p,x}.
]
Its complement is covered by the two tight paths
[
(c_1,c_4)mid(q,d_1,d_2,d_3,d_4).
]
Here ((c_1,c_4)) is a two-vertex path and the second component is the displayed Hamilton path (Q). Thus
[
operatorname{pc}(H-K)le2.
]
If (H-K) were Hamiltonian, a Hamilton path on (K) together with one on (H-K) would two-cover (H). Hence
[
operatorname{pc}(H-K)=2.
]
(square)

The same argument applies when the central slot occurs on (D). Therefore, after Lemmas 27--30, every exact-slot configuration returns to bounded four/five-support comparison except the opposite-endpoint case. In that remaining case Lemma 27 supplies an explicit cross reversal through (x).

### Exact-slot synchronization has no independent terminal branch

Lemmas 27--30 close the slot analysis completely.

**Corollary 31 (slot-closure reduction).** In the order-eleven prescribed-root normal form, every quiet double same-slot configuration yields at least one of:

1. a two-cover of \(H\);
2. an external tight triple reversing an end edge of a displayed path;
3. a Hamiltonian support of order four or five whose complement is non-Hamiltonian with path-cover number two.

Consequently, after the bounded-support reductions already established in Article III, every exact-slot configuration returns to the two global disturbance interfaces:
\[
\text{external endpoint reversal}
\qquad\text{or}\qquad
\text{split/leave-and-return}.
\]

**Proof.** If both cores use endpoint slots on the same side, Lemma 29 gives outcome 1 or 3. If at least one core uses the central slot, Lemma 30 gives outcome 1 or a Hamiltonian four-support with two-coverable complement, hence outcome 3. If the two cores use opposite endpoint slots, Lemma 27 gives either a two-cover or a cross reversal through \(x\). In the displayed five-path on the core whose endpoint slot contains \(x\), that cross triple reverses the terminal edge, so outcome 2 holds.

Finally, an order-five support in outcome 3 reduces to order four by Lemma 9 of [[defect_lines_and_spanning_order_compression_a_hamiltonian_five_set_beside_a_long_path]]. Applying the strengthened endpoint-deletion Lemma 8 of [[defect_lines_and_spanning_order_compression_an_endpoint_rooted_hamiltonian_four_set]] to the resulting four-support yields either a two-cover, an external endpoint reversal, or a split/leave-and-return disturbance. \(\square\)

Thus the entire order-eleven synchronization analysis contributes structure, but no new terminal geometry. The only unresolved local-to-global conversions are the same two already isolated before the order-eleven refinement:
\[
\boxed{\text{external endpoint reversal}}
\qquad\text{and}\qquad
\boxed{\text{split/leave-and-return disturbance}}.
\]


### Split and leave-and-return disturbances already force an external reversal

**Lemma 32 (split-to-reversal collapse).** Let (H) satisfy (operatorname{pc}(H)>2), and let
[
M=(m_0,ldots,m_t)mid A=(a_0,ldots,a_r)mid B=(b_0,ldots,b_s)
]
be a spanning three-cover. Suppose an inherited displayed edge (m_i m_{i+1}) of (M) is singled out, for example because its endpoints lie in different comparison-path blocks, or because the comparison path leaves (M) between the two blocks and later returns. Then (H) contains an external tight triple reversing an edge of one of the displayed paths (M,A,B).

**Proof.** Apply Proposition 2.1 of [[coversurg01]] to the cut of (M) between (m_i) and (m_{i+1}). Pair the prefix (M[0,i]) with (A), and pair (B) with the suffix (M[i+1,t]). Every consecutive triple in these two spanning sequences is inherited except possibly the present members of
[
(m_{i-1},m_i,a_0),qquad
(m_i,a_0,a_1),qquad
(b_{s-1},b_s,m_{i+1}),qquad
(b_s,m_{i+1},m_{i+2}).
]
At least one present triple is non-tight, since otherwise the two concatenated sequences form a spanning two-cover of (H).

Boundary antisymmetry reverses any failed triple. Respectively the four possibilities give
[
(a_0,m_i,m_{i-1}),qquad
(a_1,a_0,m_i),qquad
(m_{i+1},b_s,b_{s-1}),qquad
(m_{i+2},m_{i+1},b_s),
]
whenever the corresponding triple exists. Each is an external tight triple reversing an edge of one of the displayed paths. (square)

In particular, both positional outcomes of the endpoint-deletion comparison—an inherited displayed edge split between two comparison paths, and a leave-and-return disturbance through a nonempty exterior segment—feed immediately into the external-reversal interface.

**Corollary 33 (single remaining interface).** After the reductions of Article III, the only unresolved local-to-global conversion is
[
oxed{	ext{external endpoint reversal}.}
]
The split/leave-and-return branch is not independent.



## Two-label one-defect bridge

### The opposite-endpoint residue is a two-label completion problem

**Lemma 34 (one-defect bridge with two one-label completions).** In the opposite-endpoint case of Lemma 27, normalize the common slot orders so that
[
C=(c_1,c_2,c_3,c_4),qquad D=(d_1,d_2,d_3,d_4),
]
with
[
(c_1,c_2,c_3,c_4,p),qquad
(c_1,c_2,c_3,c_4,x),
]
and
[
(q,d_1,d_2,d_3,d_4),qquad
(x,d_1,d_2,d_3,d_4)
]
Hamiltonian. Then, unless (H) already has a two-cover, Lemma 27 gives
[
(d_1,x,c_4)
]
tight and
[
(c_4,x,d_1)
]
non-tight.

The following three orderings have the indicated defect-line structure.

1. On (H-{p,q}),
   [
   sigma_0=(c_1,c_2,c_3,c_4,x,d_1,d_2,d_3,d_4)
   ]
   has exactly one defect triple, namely
   [
   (c_4,x,d_1).
   ]
   Hence
   [
   
u(L_{sigma_0})=1.
   ]

2. On (H-q),
   [
   sigma_p=(c_1,c_2,c_3,c_4,p,x,d_1,d_2,d_3,d_4)
   ]
   has no possible defect triples except
   [
   (c_4,p,x),qquad(p,x,d_1).
   ]
   These are consecutive, so
   [
   
u(L_{sigma_p})le1.
   ]

3. On (H-p),
   [
   sigma_q=(c_1,c_2,c_3,c_4,x,q,d_1,d_2,d_3,d_4)
   ]
   has no possible defect triples except
   [
   (c_4,x,q),qquad(x,q,d_1).
   ]
   Again these are consecutive, so
   [
   
u(L_{sigma_q})le1.
   ]

**Proof.** In (sigma_0), every triple wholly inside (C) or (D) is tight, and the slot assumptions give
[
(c_3,c_4,x),qquad(x,d_1,d_2)
]
tight. The only remaining junction triple is ((c_4,x,d_1)), which is non-tight by Lemma 27. This proves (1).

For (sigma_p), the displayed Hamilton path (C+p) gives
[
(c_3,c_4,p)
]
tight, while (D+x) gives
[
(x,d_1,d_2)
]
tight. Thus the only undecided consecutive triples are the two displayed in (2), and their defect-line edges are adjacent. The proof of (3) is identical, using (C+x) and (q+D). (square)

Thus the terminal opposite-endpoint state is much narrower than a generic external reversal. There is a common nine-vertex ordering with one defect, and each of the two missing labels can be restored separately without increasing the defect-line matching number above one.

### Three simultaneous completions and the coherent failure residue

The simultaneous insertion problem has only three relevant orders.

**Lemma 35 (three-order completion criterion).** Under the hypotheses of Lemma 34, consider
[
egin{aligned}
sigma_1&=(c_1,c_2,c_3,c_4,p,x,q,d_1,d_2,d_3,d_4),\
sigma_2&=(c_1,c_2,c_3,c_4,p,q,x,d_1,d_2,d_3,d_4),\
sigma_3&=(c_1,c_2,c_3,c_4,x,p,q,d_1,d_2,d_3,d_4).
end{aligned}
]
If any one of these has defect-line matching number at most one, then (H) has a two-cover.

If all three have defect-line matching number two, then the six triples
[
egin{gathered}
(c_4,p,x),qquad (x,q,d_1),\
(c_4,p,q),qquad (q,x,d_1),\
(c_4,x,p),qquad (p,q,d_1)
end{gathered}
]
are all non-tight. Hence their boundary reversals
[
egin{gathered}
(x,p,c_4),qquad (d_1,q,x),\
(q,p,c_4),qquad (d_1,x,q),\
(p,x,c_4),qquad (d_1,q,p)
end{gathered}
]
are all tight.

Moreover, unless
[
(p,x,q),qquad(p,q,x),qquad(x,p,q)
]
are all tight, (H) contains a Hamiltonian five-support
[
F={c_4,d_1,p,q,x}
]
whose complement has path-cover number two.

**Proof.** In (sigma_1), every possible defect lies among
[
(c_4,p,x),qquad(p,x,q),qquad(x,q,d_1).
]
The corresponding defect-line edges form three consecutive edges. Their matching number is two exactly when the first and third triples are both non-tight. Thus failure of (sigma_1) to have defect matching number at most one forces
[
(c_4,p,x),qquad(x,q,d_1)
]
non-tight. The identical argument for (sigma_2,sigma_3) gives the other four failures. Boundary antisymmetry gives the six displayed reverse triples.

Now suppose at least one of
[
(q,x,p),qquad(x,q,p),qquad(q,p,x)
]
is tight. Respectively, one of
[
(d_1,q,x,p,c_4),qquad
(d_1,x,q,p,c_4),qquad
(d_1,q,p,x,c_4)
]
is a Hamiltonian path on (F), because its first and last triples are among the six forced reverse triples above. Hence (F) is Hamiltonian.

Its complement is covered by the inherited paths
[
(c_1,c_2,c_3)mid(d_2,d_3,d_4).
]
If that complement were Hamiltonian, it together with a Hamilton path on (F) would two-cover (H). Therefore its path-cover number is exactly two.

Finally, for each choice of middle vertex in the three-set ({p,q,x}), exactly one of an ordered triple and its boundary reverse is tight. Thus if none of
[
(q,x,p),qquad(x,q,p),qquad(q,p,x)
]
is tight, their reverses are precisely
[
(p,x,q),qquad(p,q,x),qquad(x,p,q),
]
and all three are tight. (square)

Consequently the two-label completion problem has only one genuinely coherent failure pattern left. After excluding a direct one-cut order and a bounded Hamiltonian five-support, the root triple must satisfy
[
(p,x,q),qquad(p,q,x),qquad(x,p,q)
]
tight simultaneously, together with the six forced bridge reversals above.

This finite oriented configuration is the exact terminal residue of the order-eleven route.

## Coherent residue collapses

### The coherent bridge residue already contains a bounded support

**Lemma 36 (coherent residue collapse).** In the coherent failure residue of Lemma 35, the four-set
[
K={c_4,d_1,p,q}
]
is Hamiltonian. Consequently either (H) has a two-cover, or
[
operatorname{pc}(H-K)=2.
]

**Proof.** Lemma 35 gives the tight triples
[
(d_1,q,p)
qquad	ext{and}qquad
(q,p,c_4).
]
Hence
[
(d_1,q,p,c_4)
]
is a Hamilton tight path on (K).

Since (K) is a proper Hamiltonian support, minimum-counterexample calculus gives
[
operatorname{pc}(H-K)le2.
]
If (H-K) were Hamiltonian, a Hamilton path on (K) together with a Hamilton path on (H-K) would form a spanning two-cover of (H). Thus, in a minimum counterexample,
[
operatorname{pc}(H-K)=2.
]
(square)

Therefore the two-label one-defect analysis has no independent terminal residue. In the opposite-endpoint synchronization case, either one of the three simultaneous completion orders already has
[

u(L_sigma)le1,
]
or the failure pattern produces a Hamiltonian four- or five-support with non-Hamiltonian two-coverable complement.

Combined with the bounded-support comparison reductions, the order-eleven synchronization route returns entirely to the single global interface
[
oxed{	ext{external endpoint reversal}.}
]

The remaining problem is thus genuinely the general local-to-global reversal problem, not a special order-eleven slot or completion obstruction.

### Two labels reversing both exposed sides force bounded support

**Lemma 37.** Let \(A=(\ldots,a_{r-1},a_r)\) and \(C=(c_1,c_2,\ldots)\) be disjoint tight paths, and let \(u,v\) be distinct exterior vertices. Suppose \((u,a_r,a_{r-1})\), \((v,a_r,a_{r-1})\), \((c_2,c_1,u)\), and \((c_2,c_1,v)\) are tight. Then these exposed vertices contain a Hamiltonian support of order four or five.

**Proof.** For \(z\in\{u,v\}\), if \((c_1,z,a_r)\) is tight, then \((c_2,c_1,z,a_r,a_{r-1})\) is a Hamilton five-path. Otherwise both central triples fail, so boundary antisymmetry gives \((a_r,u,c_1)\) and \((a_r,v,c_1)\) tight. The parallel-middle lemma in [[localextend01]] makes \(\{a_r,c_1,u,v\}\) Hamiltonian. \(\square\)

Thus simultaneous double-sided reversal by both middle labels is not a terminal configuration; in a minimum counterexample the resulting proper Hamiltonian support has non-Hamiltonian path-cover-two complement.


### The two-label bridge is not specific to order eleven

The completion argument above depends only on the local junction pattern, not on the lengths of the two inherited tight paths.

**Lemma 37 (abstract two-label one-defect bridge).** Let \(H\) be a minimum counterexample. Let \(p,q,x\) be distinct vertices, and suppose the remaining vertices are ordered as two nonempty tight paths
\[
L=(\ldots,\ell),\qquad R=(r,\ldots).
\]
Assume that the following three deletion orders have no possible defect triples except those displayed:
\[
\begin{aligned}
\sigma_0&=L,x,R,
&&(\ell,x,r),\\
\sigma_p&=L,p,x,R,
&&(\ell,p,x),\ (p,x,r),\\
\sigma_q&=L,x,q,R,
&&(\ell,x,q),\ (x,q,r).
\end{aligned}
\]
Then either \(H\) has a two-cover, or \(H\) contains a Hamiltonian support of order four or five whose complement is non-Hamiltonian with path-cover number two.

**Proof.** Consider the three spanning orders
\[
\begin{aligned}
\tau_1&=L,p,x,q,R,\\
\tau_2&=L,p,q,x,R,\\
\tau_3&=L,x,p,q,R.
\end{aligned}
\]
By the hypotheses on \(\sigma_p,\sigma_q\), every possible defect of these orders lies, respectively, among
\[
\begin{aligned}
&(\ell,p,x),\ (p,x,q),\ (x,q,r),\\
&(\ell,p,q),\ (p,q,x),\ (q,x,r),\\
&(\ell,x,p),\ (x,p,q),\ (p,q,r).
\end{aligned}
\]
In each line the three possible defect edges are consecutive in the defect line. Hence if any \(\tau_i\) has defect matching number at most one, the defect-line identity gives a two-cover of \(H\).

Assume therefore that all three have defect matching number two. For three consecutive possible defect edges, matching number two forces the first and third to be present. Thus the six triples
\[
(\ell,p,x),\ (x,q,r),\ 
(\ell,p,q),\ (q,x,r),\ 
(\ell,x,p),\ (p,q,r)
\]
are all non-tight. Boundary antisymmetry gives
\[
(x,p,\ell),\ (r,q,x),\ 
(q,p,\ell),\ (r,x,q),\ 
(p,x,\ell),\ (r,q,p)
\]
tight.

If at least one of
\[
(q,x,p),\qquad (x,q,p),\qquad (q,p,x)
\]
is tight, then respectively one of
\[
(r,q,x,p,\ell),\qquad
(r,x,q,p,\ell),\qquad
(r,q,p,x,\ell)
\]
is a Hamiltonian path on
\[
F=\{\ell,r,p,q,x\}.
\]
Hence \(F\) is a Hamiltonian five-support.

Otherwise all three displayed triples are non-tight, so their boundary reversals
\[
(p,x,q),\qquad (p,q,x),\qquad (x,p,q)
\]
are tight. But the already-forced triples
\[
(r,q,p),\qquad(q,p,\ell)
\]
then show directly that
\[
(r,q,p,\ell)
\]
is a Hamiltonian path on the four-set
\[
K=\{\ell,r,p,q\}.
\]

Thus in every case there is a proper Hamiltonian support \(S\) of order four or five. Minimum-counterexample calculus gives
\[
\operatorname{pc}(H-S)\le2.
\]
If \(H-S\) were Hamiltonian, \(S\) together with \(H-S\) would two-cover \(H\). Therefore
\[
\operatorname{pc}(H-S)=2.
\]
\(\square\)

Lemma 37 isolates the genuinely global part of the reversal problem. Once an external reversal can be placed inside a common one-defect bridge for two omitted labels, there is no further completion obstruction: the bridge either compresses directly to one defect cut or falls back into the bounded four/five-support comparison machinery.

Accordingly the remaining local-to-global task may be stated more sharply:

> starting from an external endpoint reversal in a minimum counterexample, manufacture two omitted labels whose deletion covers realize the three bridge orders \(\sigma_0,\sigma_p,\sigma_q\) of Lemma 37.

The difficult step is now **bridge manufacture**, not bridge completion.


### Two reversers of one end edge force a Hamiltonian four-set

**Lemma 38.** Let \(A=(\ldots,a_{r-1},a_r)\) be a tight path, let \(u,v\) be distinct exterior vertices with \((u,a_r,a_{r-1})\) and \((v,a_r,a_{r-1})\) tight, and let \(y\) be any further distinct vertex. Then the five exposed vertices contain a Hamiltonian four-set.

**Proof.** If \((y,u,a_r)\) is tight, then \((y,u,a_r,a_{r-1})\) is a Hamilton four-path; likewise for \(v\). If both triples are non-tight, boundary antisymmetry gives \((a_r,u,y)\) and \((a_r,v,y)\) tight. The parallel-middle lemma in [[localextend01]] then makes \(\{a_r,u,v,y\}\) Hamiltonian. \(\square\)

**Corollary 39.** In Lemma 3 of [[longest_paths_and_reversal_structure_reversals_are_unavoidable]], the alternatives in which both prescribed labels reverse the same exposed end edge immediately yield a proper Hamiltonian four-support with non-Hamiltonian path-cover-two complement. Therefore, outside the bounded-support regime, only the mixed pattern remains: one prescribed label bridges the two complementary paths while the other reverses both exposed end edges.


### The mixed universal pattern forces a bridge or a split

**Lemma 40 (bridge-or-split comparison).** Let (H) be a minimum counterexample and suppose
[
H-{z,w}=Amid C,
]
where
[
A=(a_1,ldots,a_r),qquad C=(c_1,ldots,c_s),qquad r,sge2,
]
and
[
(a_{r-1},a_r,z),qquad (z,c_1,c_2),
]
[
(w,a_r,a_{r-1}),qquad (c_2,c_1,w)
]
are tight.

Then:

1. ((a_r,z,c_1)) is non-tight, so
   [
   (c_1,z,a_r)
   ]
   is tight. Hence (H-w) has the two deletion covers
   [
   (A,z)mid C,qquad Amid(z,C).
   ]

2. Every two-cover (F) of (H-z) has one of the following forms:
   - (F) contains an ordinary path edge joining (A) directly to (C);
   - (w) is internal in one component of (F), with one path-neighbor in (A) and one in (C), and one of the old supports (A,C) is split between the two components of (F).

**Proof.** If ((a_r,z,c_1)) were tight, then
[
(a_1,ldots,a_r,z,c_1,ldots,c_s)
]
would be Hamiltonian on (H-w). Together with the singleton path ((w)), this would two-cover (H). Thus ((a_r,z,c_1)) is non-tight, and boundary antisymmetry gives ((c_1,z,a_r)) tight. The two displayed covers of (H-w) follow from the two assumed bridge triples.

Now let (F) be any two-cover of (H-z). The set (Acup{z}) is Hamiltonian, so [[hamiltonian_enlargement_forces_cut_edge01]] applied with deleted vertex (z) forces an (F)-edge crossing
[
Amid(Ccup{w}).
]
Likewise ({z}cup C) is Hamiltonian, so an (F)-edge crosses
[
Cmid(Acup{w}).
]

If an (F)-edge joins (A) directly to (C), we are done. Otherwise every required crossing is incident with (w). Since (w) has degree at most two in a path cover, there are exactly two such crossing edges: one joins (w) to (A), and one joins (w) to (C). Thus (w) is internal in one component of (F), lying between a nonempty (A)-block and a nonempty (C)-block.

The second component of (F) is nonempty because (H-z) is non-Hamiltonian. It cannot contain (w), and with no direct (A)-(C) edge it lies wholly in one of (A,C). That old support therefore occurs both in the mixed component and in the second component, so it is split between the two comparison paths. (square)

Thus the hard mixed universal endpoint pattern automatically manufactures the geometry needed for bridge construction. Deleting the bridge label (z) forces either direct (A)-to-(C) mixing or an explicit internal (A)-(w)-(C) bridge together with a split old support. The remaining task is to synchronize this mandatory comparison disturbance with the one-defect deletion orders of the abstract two-label bridge.



### Direct mixing in the universal mixed pattern reduces to the disturbance toolkit

**Lemma 41.** Retain the mixed universal pattern of Lemma 40:
[
H-{z,w}=Amid C,
]
with
[
A=(a_1,ldots,a_r),qquad C=(c_1,ldots,c_s),
]
and
[
(a_{r-1},a_r,z),qquad (z,c_1,c_2),
]
[
(w,a_r,a_{r-1}),qquad(c_2,c_1,w)
]
tight.

Let
[
H-w=(A,z)mid C
]
be the displayed deletion cover, and let (F) be any two-cover of (H-z) containing an ordinary path edge joining (A) directly to (C).

Then at least one of the following holds:

1. (F) has an order disagreement with the inherited order on (A);
2. an inherited edge of (A) has endpoints in two different paths of (F);
3. one path of (F) leaves (A) through a nonempty exterior segment and later returns;
4. a tight triple reverses the displayed endpoint edge (a_rz);
5. (H) has a two-cover;
6. the three-cover (Fmid{z}) admits a strict quadratic-potential decrease;
7. endpoint restoration is neutral and produces a deletion cover compatible with (F) on the common domain.

**Proof.** If (F) does not preserve the inherited relative order of the surviving vertices of (A), outcome 1 holds.

Otherwise apply [[path_disturbance_endpoint_reversal_descent_or_an_omission_swap]] with
[
y=w,qquad
R=(a_1,ldots,a_r,z),qquad
Q=C,
]
and with the omitted endpoint of (R) equal to (z). The hypothesis that (F) contains a direct (A)-to-(C) edge is exactly the required mixed-edge hypothesis. The theorem gives outcomes 2–7. (square)

Thus the direct-mixing alternative of Lemma 40 is not a new global obstruction. It enters the already-developed disturbance system immediately.

Consequently, bridge manufacture may be narrowed further: after excluding order disagreement, split/leave-and-return disturbance, fresh endpoint reversal, two-cover, and strict descent, the only coherent direct-mix residue is a neutral omission swap producing compatible deletion covers.

Together with the second alternative of Lemma 40, the unresolved bridge-manufacture problem is therefore reduced to **compatible omission swaps and split-support comparisons**.



## Metadata

- ID: defect_lines_and_spanning_order_compression_the_remaining_lemma
- Kind: section
- Version: 40
- Math version: 35
- Audit: unaudited
- Refutation: unrefuted

## Authoring state

- Subsection 1 — crystallized, version 14: (untitled)
- Subsection 2 — crystallized, version 10: The universal four-support is immediate
- Subsection 3 — crystallized, version 4: Slot synchronization reductions
- Subsection 4 — crystallized, version 6: Same-side endpoint reduction
- Subsection 5 — crystallized, version 4: Two-label one-defect bridge
- Subsection 6 — HOT, version 7: Coherent residue collapses
