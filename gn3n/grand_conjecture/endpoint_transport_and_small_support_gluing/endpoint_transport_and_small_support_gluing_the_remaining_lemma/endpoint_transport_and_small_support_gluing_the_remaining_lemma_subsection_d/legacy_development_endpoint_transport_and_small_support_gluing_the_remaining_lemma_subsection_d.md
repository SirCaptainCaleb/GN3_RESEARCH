# Junction-rooted four-support — preserved pre-item development

### The four-support can retain the deleted label at a Hamiltonian endpoint

**Lemma 16 (junction-rooted four-support).** Let
[
H-x=Pmid Q,
qquad
P=(p_1,ldots,p_m),
qquad
Q=(q_1,ldots,q_s),
]
be any deletion cover of a minimum counterexample. Then the five-vertex junction set
[
J={x,p_{m-1},p_m,q_1,q_2}
]
contains a Hamiltonian four-set (K) admitting a Hamilton order with (x) as an endpoint. Moreover
[
operatorname{pc}(H-K)=2.
]

**Proof.** Since (P,Qmid{x}) is not a two-cover, at least one of
[
(p_{m-1},p_m,q_1),
qquad
(p_m,q_1,q_2)
]
is non-tight.

If
[
(p_{m-1},p_m,q_1)
]
is non-tight, boundary antisymmetry gives the tight three-path
[
(q_1,p_m,p_{m-1}).
]
Apply the prescribed-endpoint extension theorem to this tight triple, with the two further vertices
[
q_2, x,
]
prescribing (x) as the endpoint. It yields a Hamiltonian support
[
Ssubseteq J,
qquad
4le |S|le5,
qquad
xin S,
]
with a Hamilton order having (x) as an endpoint.

If instead
[
(p_m,q_1,q_2)
]
is non-tight, then
[
(q_2,q_1,p_m)
]
is a tight three-path. Apply the same theorem with the two further vertices
[
p_{m-1}, x,
]
again prescribing (x). The same conclusion follows.

If (|S|=4), put (K=S). If (|S|=5), delete from its displayed Hamilton order the endpoint opposite (x). The remaining four vertices inherit a Hamilton order still having (x) as an endpoint; call its support (K). Thus in every case
[
Ksubseteq J,qquad |K|=4,qquad xin K,
]
and (x) is a displayed endpoint.

Since (K) is proper, minimum-counterexample calculus gives
[
operatorname{pc}(H-K)le2.
]
The complement cannot be Hamiltonian without two-covering (H), hence
[
operatorname{pc}(H-K)=2.
]
(square)

This strengthens Corollary 15 in exactly the direction needed for comparison. The bounded support is not merely forced from the deletion cover: it can be chosen

- inside the five-vertex neighborhood of the failed (P)-(Q) junction;
- to contain the omitted label (x);
- with (x) as an endpoint of its Hamilton order.

Therefore endpoint deletion from (K) may be compared directly with the **same original deletion cover**
[
H-x=Pmid Q.
]
No second arbitrary deletion cover is needed to expose the first comparison disturbance.

The next target is correspondingly sharper: apply the endpoint-rooted comparison theorem with (k_0=x) and with (F=Pmid Q) fixed, and exploit that the three surviving vertices (K-{x}) lie among
[
{p_{m-1},p_m,q_1,q_2}.
]
The split/reversal alternatives are then confined to the original junction neighborhood rather than occurring at an unrelated support.

### The original deletion cover already splits the rooted three-core

The junction-rooted support of Lemma 16 makes the first comparison disturbance automatic.

**Corollary 17 (junction-core split).** Retain the setting of Lemma 16 and orient the Hamilton order of the resulting four-support from its prescribed endpoint:
[
K=(x,k_1,k_2,k_3).
]
Then
[
{k_1,k_2,k_3}subseteq
{p_{m-1},p_m,q_1,q_2}
]
meets both (V(P)) and (V(Q)). Consequently at least one of the two inherited ordinary edges
[
k_1k_2,qquad k_2k_3
]
has one endpoint in (P) and the other in (Q).

Equivalently, when the endpoint-rooted comparison theorem is applied to (K) with (k_0=x) and the comparison deletion cover fixed to be the original
[
F=Pmid Q
]
of (H-x), the split-core alternative occurs immediately: the three-vertex core (K-{x}) is distributed across the two comparison paths.

**Proof.** The junction set
[
J-{x}
=
{p_{m-1},p_m,q_1,q_2}
]
contains exactly two vertices of (P) and exactly two vertices of (Q). Since (K) contains (x) and has order four, its three remaining vertices form a three-subset of (J-{x}). Such a three-subset cannot lie wholly in either (P) or (Q); it has type (2+1) across the partition (Pmid Q).

The order
[
(k_1,k_2,k_3)
]
is a tight three-path inherited from (K). A three-vertex path whose vertex set meets both classes of a bipartition must have a consecutive pair crossing the bipartition. Hence one of (k_1k_2,k_2k_3) joins (P) to (Q). (square)

Thus no arbitrary second deletion cover is needed even to *produce* the positional disturbance. Every deletion cover
[
H-x=Pmid Q
]
canonically yields, inside the local five-set
[
{x,p_{m-1},p_m,q_1,q_2},
]
a rooted Hamiltonian four-support whose surviving tight three-core already crosses the original (P)-(Q) cut.

The global problem may therefore be sharpened again: determine how such a **junction-crossing rooted three-core** can coexist with the four endpoint reversals of Lemma 14 without producing a spanning two-cover or a one-cut defect order.



### Every deletion cover has explicit four-supports at both junction ends

The four endpoint reversals of Lemma 14 can be paired directly, without an auxiliary extension argument.

**Lemma 18 (canonical opposite-end four-supports).** Let
[
H-x=Pmid Q,
qquad
P=(p_1,ldots,p_m),
qquad
Q=(q_1,ldots,q_s)
]
be any deletion cover of a minimum counterexample. Then:

1. exactly one of the two four-vertex orders
   [
   (p_2,p_1,x,q_1),
   qquad
   (q_2,q_1,x,p_1)
   ]
   is a Hamiltonian path;

2. exactly one of the two four-vertex orders
   [
   (q_s,x,p_m,p_{m-1}),
   qquad
   (p_m,x,q_s,q_{s-1})
   ]
   is a Hamiltonian path.

Consequently (H) contains two explicitly located Hamiltonian four-supports, one using the two initial ends of the deletion cover and one using the two terminal ends. Each has non-Hamiltonian complement of path-cover number two.

**Proof.** Lemma 14 gives
[
(p_2,p_1,x),
qquad
(q_2,q_1,x)
]
tight. The triples
[
(p_1,x,q_1)
qquad	ext{and}qquad
(q_1,x,p_1)
]
are boundary flips, so exactly one is tight.

If ((p_1,x,q_1)) is tight, then
[
(p_2,p_1,x,q_1)
]
is a Hamiltonian four-path. If ((q_1,x,p_1)) is tight, then
[
(q_2,q_1,x,p_1)
]
is a Hamiltonian four-path. This proves (1), including exclusivity.

At the terminal ends, Lemma 14 gives
[
(x,p_m,p_{m-1}),
qquad
(x,q_s,q_{s-1})
]
tight. The triples
[
(q_s,x,p_m)
qquad	ext{and}qquad
(p_m,x,q_s)
]
are boundary flips. If the first is tight, then
[
(q_s,x,p_m,p_{m-1})
]
is a Hamiltonian four-path; if the second is tight, then
[
(p_m,x,q_s,q_{s-1})
]
is. This proves (2).

Every displayed four-set is proper because a minimum counterexample has more than ten vertices. Minimum-counterexample calculus therefore gives path-cover number at most two for its complement. The complement cannot be Hamiltonian, since that Hamilton path together with the displayed four-path would two-cover (H). Hence each complement has path-cover number exactly two. (square)

Thus a deletion cover does not merely force some bounded support near a failed concatenation. It carries a pair of **canonical four-support probes at opposite ends**, determined only by the orientation of the two central boundary-flip triples
[
p_1,x,q_1
qquad	ext{and}qquad
p_m,x,q_s.
]

Each probe contains (x), one complete displayed end edge from one old path, and the exposed endpoint of the other old path. This gives two fixed local interfaces that can be compared against each other, rather than restarting the four-support analysis from an arbitrary support.



### Every deletion cover descends to a neutral square of rooted three-supports

The four endpoint reversals admit a simpler canonical construction than the four-support probes.

**Lemma 19 (endpoint-pair rooted three-square).** Let
[
H-x=Pmid Q,
qquad
P=(p_1,ldots,p_m),
qquad
Q=(q_1,ldots,q_s)
]
be any deletion cover of a minimum counterexample. Let
[
E(P)={p_1,p_m},
qquad
E(Q)={q_1,q_s}.
]

For every pair
[
(p,q)in E(P)	imes E(Q),
]
exactly one of
[
(p,x,q),
qquad
(q,x,p)
]
is tight. Let (T_{p,q}) denote that oriented tight three-path. Then
[
mathcal C_{p,q}
=
(P-p)mid T_{p,q}mid(Q-q)
]
is a spanning three-cover of (H), where (P-p) and (Q-q) carry their inherited path orders.

Moreover:

1. every (mathcal C_{p,q}) lies in the same pairwise-repartition component as the singleton lift
   [
   Pmid{x}mid Q;
   ]

2. all four endpoint-pair states have the same profile
   [
   (m-1)mid3mid(s-1)
   ]
   and hence the same quadratic potential;

3. changing only the endpoint (p) or only the endpoint (q) is one pairwise repartition, so the four states contain a neutral 4-cycle in the repartition graph;

4. relative to the singleton lift,
   [
   Phi(mathcal C_{p,q})
   -
   Phi(Pmid{x}mid Q)
   =
   10-2(m+s)<0.
   ]

Thus every deleted label enters, after at most two pairwise repartitions, a canonical neutral square of strictly lower-(Phi) rooted three-support states.

**Proof.** Fix (pin E(P)) and (qin E(Q)). Boundary antisymmetry at the middle vertex (x) says that exactly one of
[
(p,x,q),
qquad
(q,x,p)
]
is tight. Hence (T_{p,q}) is a tight three-path.

Deleting an endpoint from a displayed tight path leaves a tight path, so (P-p) and (Q-q) are tight. Their supports are disjoint from (T_{p,q}), and together the three supports partition (V(H)). Thus (mathcal C_{p,q}) is a spanning three-cover.

To connect it to the singleton lift, first repartition
[
Qmid{x}
]
as
[
(Q-q)mid{x,q},
]
orienting the two-vertex path ({x,q}) as (x,q) or (q,x) according to the orientation of (T_{p,q}). This is always legal because every two-vertex order is a tight path. Then repartition
[
Pmid{x,q}
]
as
[
(P-p)mid T_{p,q}.
]
This gives (mathcal C_{p,q}) in two pairwise repartitions.

All four choices remove one endpoint from each of (P,Q) and create a three-component, so their common profile is
[
(m-1,3,s-1).
]

Now hold (q) fixed and switch the chosen endpoint of (P) from (p_1) to (p_m). The (Q-q) component is unchanged. On the complementary vertex set
[
V(P)cup{x,q},
]
both
[
(P-p_1)mid T_{p_1,q}
qquad	ext{and}qquad
(P-p_m)mid T_{p_m,q}
]
are two-path covers. Replacing one by the other is therefore one pairwise repartition. The same argument switches the chosen endpoint of (Q) while (p) is fixed. Hence the four states contain the square
[
(p_1,q_1);-;(p_m,q_1);-;(p_m,q_s);-;(p_1,q_s);-;(p_1,q_1),
]
and every edge is (Phi)-neutral because the profile is unchanged.

Finally,
[
egin{aligned}
Phi(mathcal C_{p,q})
-
Phi(Pmid{x}mid Q)
&=
(m-1)^2+9+(s-1)^2-(m^2+1+s^2)\
&=
10-2(m+s).
end{aligned}
]
Since (m+s=|V(H)|-1) and a minimum counterexample has more than ten vertices, this quantity is strictly negative. (square)

This canonical square strengthens the usual singleton descent in two ways: it is symmetric in the two deletion-cover paths, and it preserves four simultaneous choices of exposed endpoint geometry on one common (Phi)-level. Any componentwise minimum reached from the deletion root therefore inherits a four-way rooted entry family rather than a single preferred descent path.



### The rooted endpoint square is minimal only at order eleven

**Corollary 20.** Retain the endpoint-pair square of Lemma 19. If one, equivalently all, of the four states
[
mathcal C_{p,q}
]
minimizes (Phi) in its pairwise-repartition component, then
[
|P|=|Q|=5
qquad	ext{and}qquad
|V(H)|=11.
]

Equivalently, if (|V(H)|
e11), the common repartition component of the four endpoint-pair states contains a three-cover of strictly smaller quadratic potential.

**Proof.** All four states lie in the same repartition component and have the same profile
[
3mid(m-1)mid(s-1).
]
Hence either all four are componentwise (Phi)-minimum or none is.

The rooted small-support classification
[[line_rooted_small_support_descent_from_deletion_cover_lifts]]
shows that at a quadratic minimum, any state containing a component of order three has exactly profile
[
3mid4mid4.
]
Therefore
[
m-1=s-1=4,
]
so (m=s=5). Since (m+s=|V(H)|-1),
[
|V(H)|=11.
]
The contrapositive gives the second assertion. (square)

Thus the canonical endpoint-pair square has only one possible immediate terminal order. At every other order, the square is not merely a strict improvement over the singleton lift: its entire neutral four-cycle sits strictly above another state in the same repartition component.





### Correction: the cross-endpoint central orientation is not forced

For a deletion cover
[
H-x=Pmid Q,qquad
P=(p_1,ldots,p_m),qquad
Q=(q_1,ldots,q_s),
]
the endpoint-insertion failures give
[
(p_{m-1},p_m,x) 	ext{non-tight},
qquad
(x,q_1,q_2) 	ext{non-tight},
]
but they do not determine the status of the distinct middle triple
[
(p_m,x,q_1).
]
In particular, the spanning order
[
(p_1,ldots,p_m,x,q_1,ldots,q_s)
]
has three new triples around (x), not one. Even if ((p_m,x,q_1)) is tight, the two outer new triples above remain non-tight, so this order is not Hamiltonian.

Therefore the former claim that ((q_1,x,p_m)) and ((p_1,x,q_s)) are forced tight is withdrawn, as are the canonical five-path conclusions that depended on those forced orientations.

The valid preceding statements remain unchanged. In particular:

- Lemma 18 supplies canonical four-supports at the same-end endpoint pairs without choosing the orientation of the central boundary pair.
- Lemma 19 supplies the four endpoint-pair rooted three-support states by orienting each central triple in whichever direction is actually tight.
- At a cross pair such as ((p_m,q_1)), if ((q_1,x,p_m)) happens to be tight then
  [
  (q_2,q_1,x,p_m,p_{m-1})
  ]
  is indeed a tight five-path; if the opposite orientation ((p_m,x,q_1)) is tight, that five-path is unavailable and this is a genuine separate branch.

Thus future arguments at the two cross corners must retain the central orientation as case data rather than infer it from the failure of the deletion-cover concatenation.
