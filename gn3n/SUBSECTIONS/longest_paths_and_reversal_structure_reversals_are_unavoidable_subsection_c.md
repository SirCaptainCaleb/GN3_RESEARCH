# Global marked-reversal minimization

## Metadata

- ID: longest_paths_and_reversal_structure_reversals_are_unavoidable_subsection_c
- Parent Section: longest_paths_and_reversal_structure_reversals_are_unavoidable
- Position: 3
- Row version: 7
- Development version: 7
- Composition version: 1
- Composition stale: False

## Cold composition

### Imbalance in a frozen complement forces a new reversal carrier

Call a spanning three-cover
[
Amid Bmid C
]
a **marked reversal state** if some vertex outside (A) forms a tight triple reversing an end edge of the displayed path (A).

Choose a marked reversal state minimizing
[
Phi=|A|^2+|B|^2+|C|^2
]
over all marked reversal states of (H).

**Lemma 11 (frozen imbalance forces a carrier switch).** Suppose (A) is marked and, among all two-covers of (H-A), the displayed cover
[
B=(b_1,ldots,b_s)mid C=(c_1,ldots,c_t)
]
minimizes
[
Psi=|B|^2+|C|^2.
]
Assume (2le sle t) and
[
tge s+2.
]
Then each endpoint (cin{c_1,c_t}) of (C) reverses both displayed end edges of (B):
[
(b_2,b_1,c)
qquad	ext{and}qquad
(c,b_s,b_{s-1})
]
are tight.

In particular (B) is itself a valid reversal carrier, with either endpoint of (C) as an external reversing vertex.

**Proof.** Fix an endpoint (c) of (C). Suppose (Bcup{c}) were Hamiltonian. Since deleting an endpoint from the displayed path (C) leaves a tight path, we would obtain a two-cover
[
(Bcup{c})mid(C-c)
]
of (H-A). Its potential differs from that of (Bmid C) by
[
(s+1)^2+(t-1)^2-(s^2+t^2)
=2(s-t+1)le -2,
]
contradicting the choice of (Bmid C).

Thus (Bcup{c}) is non-Hamiltonian. In particular (c) cannot be prepended to the displayed order of (B), so
[
(c,b_1,b_2)
]
is non-tight and boundary antisymmetry gives
[
(b_2,b_1,c)
]
tight. Likewise (c) cannot be appended to (B), so
[
(b_{s-1},b_s,c)
]
is non-tight and therefore
[
(c,b_s,b_{s-1})
]
is tight. (square)

This is a genuine reduction mechanism: imbalance does not merely create a bounded configuration; it moves the reversal certificate from one component to another without changing the spanning cover.

### Consequence at a global marked minimum

**Corollary 12 (largest-component endpoints reverse both smaller components).** Let
[
Amid Bmid C
]
be a marked reversal state minimizing (Phi) globally, and order the component sizes as
[
|A|le |B|le |C|.
]
Suppose
[
|C|ge |B|+2.
]
Then both endpoints of (C) reverse both displayed end edges of (B).

Moreover (B) may now be taken as the marked carrier in the same (Phi)-minimal state. Consequently the displayed two-cover
[
Amid C
]
of (H-B) is also minimum-potential among all two-covers of (H-B). Since
[
|C|ge |B|+2ge |A|+2,
]
Lemma 11 applied with (B) as the marked carrier shows that the same two endpoints of (C) reverse both displayed end edges of (A) as well.

Thus, whenever the largest component is separated from the middle component by at least two vertices, each endpoint (c) of the largest component satisfies all four tight reversals
[
(a_2,a_1,c),qquad(c,a_{|A|},a_{|A|-1}),
]
[
(b_2,b_1,c),qquad(c,b_{|B|},b_{|B|-1}).
]

**Proof.** The first assertion is Lemma 11.

Because (B) now carries an external endpoint reversal, the same three-cover is a marked reversal state with carrier (B). If some two-cover
[
H-B=A'mid C'
]
had
[
|A'|^2+|C'|^2<|A|^2+|C|^2,
]
then
[
Bmid A'mid C'
]
would be a marked reversal state of smaller total (Phi), contradicting global minimality. Hence (Amid C) is frozen-minimal for the carrier (B). Applying Lemma 11 to that frozen complement gives the asserted reversals on (A). (square)

The unresolved global case has therefore narrowed to two regimes:

1. the marked-minimum size profile is nearly balanced at the top,
   [
   |C|le |B|+1;
   ]
2. the two endpoints of the largest component simultaneously reverse both end edges of each smaller component.

This dichotomy is valid for arbitrary order. It is the appropriate starting point for a general reduction to the complementary-splice framework rather than for further bounded-order case analysis.

### Imbalance at a global marked minimum forces bounded support

**Corollary 13.** Let
[
Amid Bmid C
]
be a marked reversal state minimizing (Phi) globally among all marked reversal states, with
[
|A|le |B|le |C|.
]
If
[
|C|ge |B|+2,
]
then (H) contains a Hamiltonian component of order at most five whose complement has path-cover number two. More precisely, either (|A|le3), or there is a Hamiltonian four- or five-support containing an endpoint of (C) and both displayed endpoints of (A).

**Proof.** By Corollary 12, each endpoint (c) of (C) reverses both displayed end edges of (A). Write
[
A=(a_1,ldots,a_r).
]

If (rle3), the displayed component (A) is already a bounded Hamiltonian support, and its complement is two-covered by (Bmid C).

Assume (rge4). Put
[
T={a_1,a_r,c}.
]
Consider the two four-sets
[
Tcup{a_2},
qquad
Tcup{a_{r-1}}.
]
If either is Hamiltonian, we have the required Hamiltonian four-support.

Assume both are non-Hamiltonian. The two-bad-four-extension lemma from [[localextend01]], applied to the common three-set (T) and the two distinct exterior vertices (a_2,a_{r-1}), gives a Hamiltonian path on
[
Tcup{a_2,a_{r-1}},
]
a five-set containing (c) and both displayed endpoints (a_1,a_r).

Thus in all cases there is a Hamiltonian support (K) of order four or five containing the asserted anchor vertices, unless (A) itself already has order at most three.

Since (K) is a proper Hamiltonian support in a minimum counterexample, minimum-counterexample calculus gives
[
operatorname{pc}(H-K)le2.
]
The complement cannot be Hamiltonian, because then (K) together with a Hamilton path on (H-K) would two-cover (H). Hence
[
operatorname{pc}(H-K)=2.
]
(square)

Therefore the imbalanced branch of the global marked-reversal minimum is already reduced, at arbitrary order, to bounded support. The only marked-minimum regime not yet reduced in this way is
[
|C|le |B|+1.
]

This isolates the genuinely global remaining case: a nearly balanced pair of largest components in a marked-reversal state. No bounded-order hypothesis is involved.



### A global marked minimum is almost equitable unless bounded support appears

**Corollary 14.** Let
[
Amid Bmid C
]
be a marked reversal state minimizing (Phi) globally, with
[
|A|le |B|le |C|.
]
If (H) has no Hamiltonian support of order four or five arising from the marked-minimum analysis, then
[
|B|le |A|+1
qquad	ext{and}qquad
|C|le |B|+1.
]
In particular
[
|C|-|A|le2.
]

**Proof.** Corollary 13 already shows that
[
|C|ge |B|+2
]
forces bounded Hamiltonian support. Hence, in the unresolved branch,
[
|C|le |B|+1.
]

It remains to compare (A) and (B). Write
[
A=(a_1,ldots,a_r),
]
and suppose the marked reversal is on the terminal edge (a_{r-1}a_r). Assume for contradiction that
[
|B|ge r+2.
]

Let (z) be any endpoint of (B). If
[
(z,a_1,a_2)
]
were tight, then
[
(z,a_1,ldots,a_r)
]
would be a Hamilton path on (Acup{z}), while deleting the endpoint (z) from (B) leaves a tight path. Repartitioning (Amid B) therefore changes their sizes from
[
(r,|B|)
]
to
[
(r+1,|B|-1).
]
The potential change is
[
(r+1)^2+(|B|-1)^2-r^2-|B|^2
=
2(r-|B|+1)<0.
]
The displayed terminal edge of (A) and its standing external reversal are untouched. Hence the new state is still marked, contradicting global minimality.

Therefore
[
(z,a_1,a_2)
]
is non-tight, and boundary antisymmetry gives
[
(a_2,a_1,z)
]
tight.

The same argument applies to both endpoints of (B). It also applies to both endpoints of (C), since
[
|C|ge|B|ge r+2.
]
Thus there are at least four distinct vertices (zin V(B)cup V(C)) satisfying
[
(a_2,a_1,z)
]
tight.

Choose any three of them. The three-hook consequence of [[localextend01]] produces a Hamiltonian support of order four or five containing the ordered anchor pair
[
(a_2,a_1),
]
contrary to the unresolved assumption.

Hence
[
|B|le |A|+1.
]
Together with
[
|C|le |B|+1,
]
this proves the result. (square)

Thus every unresolved global marked-reversal minimum has an almost equitable size profile:
[
(r,r,r),qquad (r,r,r+1),qquad (r,r+1,r+1),
qquad	ext{or}qquad (r,r+1,r+2)
]
up to the displayed ordering of component sizes.

The remaining global problem is therefore no longer arbitrary imbalance. It is to exploit the marked reversal inside these four near-balanced profile families.



### Carrier switching removes the remaining size gap

**Lemma 15 (carrier switch between displayed components).** Let
[
A=(a_1,ldots,a_r),qquad B=(b_1,ldots,b_s)
]
be two nontrivial components of a spanning three-cover of a minimum counterexample. Then either (B) is a marked reversal carrier in the same three-cover, or (H) contains a Hamiltonian four-support.

**Proof.** The concatenation (AB) cannot be tight, since together with the third displayed component it would give a two-cover. By Lemma 1 of [[global_augmentation_by_complementary_path_splices]], either
[
(b_1,a_r,a_{r-1})
]
is tight, marking (A), or
[
(b_2,b_1,a_r)
]
is tight, marking (B).

Likewise (BA) cannot be tight. Hence either
[
(a_1,b_s,b_{s-1})
]
is tight, marking (B), or
[
(a_2,a_1,b_s)
]
is tight, marking (A).

Suppose (B) is not marked by either comparison. Then
[
(b_1,a_r,a_{r-1}),qquad(a_2,a_1,b_s)
]
are tight.

If
[
(a_1,b_s,b_1)
]
is tight, then
[
(a_2,a_1,b_s,b_1)
]
is a Hamiltonian four-path. If
[
(b_s,b_1,a_r)
]
is tight, then
[
(b_s,b_1,a_r,a_{r-1})
]
is a Hamiltonian four-path. If both displayed middle triples are non-tight, their boundary flips
[
(b_1,b_s,a_1),qquad(a_r,b_1,b_s)
]
are tight, and
[
(a_r,b_1,b_s,a_1)
]
is a Hamiltonian four-path. (square)

**Corollary 16 (full balance or bounded support).** Let
[
Amid Bmid C
]
be a globally (Phi)-minimal marked reversal state with
[
|A|le |B|le |C|.
]
Then either (H) contains a Hamiltonian support of order at most five with two-coverable complement, or
[
|B|le |A|+1,qquad |C|le |B|+1,
]
and in fact
[
|C|-|A|le1.
]

Equivalently the unresolved size profiles are exactly
[
(r,r,r),qquad(r,r,r+1),qquad(r,r+1,r+1).
]

**Proof.** Corollary 14 already gives
[
|B|le |A|+1,qquad |C|le |B|+1.
]
Only the profile ((r,r+1,r+2)) remains to exclude.

Assume
[
|A|=r,qquad |B|=r+1,qquad |C|=r+2.
]
If (rle5), then the displayed Hamiltonian component (A) itself is bounded support with two-coverable complement (Bmid C). Hence assume (rge6).

By Lemma 15, unless a Hamiltonian four-support already exists, (C) can be taken as the marked carrier in this same state. Global marked minimality then implies that
[
Amid B
]
is minimum-potential among all two-covers of (H-C): a lower-potential replacement would give a marked three-cover of smaller total (Phi).

But
[
|B|=|A|+1,
]
so no contradiction yet. Now instead take (B) as marked carrier, again using Lemma 15. Its frozen complement is
[
Amid C,
]
whose component orders differ by two. Lemma 11 therefore applies and says that each endpoint of (C) reverses both displayed end edges of (A). Corollary 13's local double-reversal argument then produces a Hamiltonian support of order at most five with two-coverable complement, contradiction.

Thus the profile ((r,r+1,r+2)) is impossible in the unresolved branch. (square)

Therefore the global marked-reversal problem lands exactly in the three near-equitable size families treated separately in Article II, with no bounded-order hypothesis.



### Global marked minima reduce to two disturbance geometries

**Corollary 17.** Let
[
Amid Bmid C
]
be a globally (Phi)-minimal marked reversal state of a minimum counterexample. Unless a Hamiltonian support of order at most five with two-coverable complement has already appeared, the state has one of the three absolute-minimum profiles
[
(r,r,r),qquad (r,r,r+1),qquad (r,r+1,r+1).
]
Consequently the Article II profile theorems produce, after the standard reductions, either

1. an external tight triple reversing an edge of a relevant displayed or comparison path; or
2. an inherited displayed edge split between two comparison paths, or a leave-and-return disturbance through a nonempty exterior segment.

**Proof.** Corollary 16 leaves exactly the three displayed size profiles. For totals (3r,3r+1,3r+2), respectively, these are the absolute minimizers of
[
x^2+y^2+z^2
]
among positive integer triples of the same sum. Hence the state is a genuine (Phi)-minimum in its whole pairwise-repartition component, not merely among marked states.

Apply the corresponding profile theorem from Article II:
[[quadratic_potential_and_pairwise_repartition_the_size_profile_rrr]],
[[quadratic_potential_and_pairwise_repartition_the_size_profile_r1rr]],
or
[[quadratic_potential_and_pairwise_repartition_the_size_profile_r1r1r]].

Their outputs are order disagreement, direct mixing between displayed supports, split inherited edges, leave-and-return block patterns, reversing tight triples, or the additional same-side recurrence structures in the ((r,r+1,r+1)) profile.

Order disagreement gives an external reversing triple by Lemma 1 of this Section. Direct mixing enters the disturbance theorem
[[path_disturbance_endpoint_reversal_descent_or_an_omission_swap]], which yields split/leave-and-return, external reversal, a two-cover, strict descent, or a compatible omission swap. Strict descent contradicts the global marked minimum whenever the marked certificate survives; the compatible neutral residue is precisely the bridge-manufacture interface now isolated in Article III. The same-side recurrence alternatives either give bounded common-core structure or return to these comparison disturbances by the Article II/IV recurrence analysis.

Thus, outside bounded support and the coherent neutral omission-swap residue, the only genuinely geometric outputs are external reversal and split/leave-and-return. (square)

This gives an arbitrary-order chain
[
	ext{external reversal}
Longrightarrow
	ext{global marked minimum}
Longrightarrow
	ext{absolute equitable profile}
Longrightarrow
	ext{reversal or split disturbance}.
]

Hence the remaining new global mathematics is not a small-order classification. It is the conversion of a split/leave-and-return comparison—or its compatible neutral omission-swap residue—into the abstract one-defect bridge of Article III.



## Development

### Imbalance in a frozen complement forces a new reversal carrier

Call a spanning three-cover
[
Amid Bmid C
]
a **marked reversal state** if some vertex outside (A) forms a tight triple reversing an end edge of the displayed path (A).

Choose a marked reversal state minimizing
[
Phi=|A|^2+|B|^2+|C|^2
]
over all marked reversal states of (H).

**Lemma 11 (frozen imbalance forces a carrier switch).** Suppose (A) is marked and, among all two-covers of (H-A), the displayed cover
[
B=(b_1,ldots,b_s)mid C=(c_1,ldots,c_t)
]
minimizes
[
Psi=|B|^2+|C|^2.
]
Assume (2le sle t) and
[
tge s+2.
]
Then each endpoint (cin{c_1,c_t}) of (C) reverses both displayed end edges of (B):
[
(b_2,b_1,c)
qquad	ext{and}qquad
(c,b_s,b_{s-1})
]
are tight.

In particular (B) is itself a valid reversal carrier, with either endpoint of (C) as an external reversing vertex.

**Proof.** Fix an endpoint (c) of (C). Suppose (Bcup{c}) were Hamiltonian. Since deleting an endpoint from the displayed path (C) leaves a tight path, we would obtain a two-cover
[
(Bcup{c})mid(C-c)
]
of (H-A). Its potential differs from that of (Bmid C) by
[
(s+1)^2+(t-1)^2-(s^2+t^2)
=2(s-t+1)le -2,
]
contradicting the choice of (Bmid C).

Thus (Bcup{c}) is non-Hamiltonian. In particular (c) cannot be prepended to the displayed order of (B), so
[
(c,b_1,b_2)
]
is non-tight and boundary antisymmetry gives
[
(b_2,b_1,c)
]
tight. Likewise (c) cannot be appended to (B), so
[
(b_{s-1},b_s,c)
]
is non-tight and therefore
[
(c,b_s,b_{s-1})
]
is tight. (square)

This is a genuine reduction mechanism: imbalance does not merely create a bounded configuration; it moves the reversal certificate from one component to another without changing the spanning cover.

### Consequence at a global marked minimum

**Corollary 12 (largest-component endpoints reverse both smaller components).** Let
[
Amid Bmid C
]
be a marked reversal state minimizing (Phi) globally, and order the component sizes as
[
|A|le |B|le |C|.
]
Suppose
[
|C|ge |B|+2.
]
Then both endpoints of (C) reverse both displayed end edges of (B).

Moreover (B) may now be taken as the marked carrier in the same (Phi)-minimal state. Consequently the displayed two-cover
[
Amid C
]
of (H-B) is also minimum-potential among all two-covers of (H-B). Since
[
|C|ge |B|+2ge |A|+2,
]
Lemma 11 applied with (B) as the marked carrier shows that the same two endpoints of (C) reverse both displayed end edges of (A) as well.

Thus, whenever the largest component is separated from the middle component by at least two vertices, each endpoint (c) of the largest component satisfies all four tight reversals
[
(a_2,a_1,c),qquad(c,a_{|A|},a_{|A|-1}),
]
[
(b_2,b_1,c),qquad(c,b_{|B|},b_{|B|-1}).
]

**Proof.** The first assertion is Lemma 11.

Because (B) now carries an external endpoint reversal, the same three-cover is a marked reversal state with carrier (B). If some two-cover
[
H-B=A'mid C'
]
had
[
|A'|^2+|C'|^2<|A|^2+|C|^2,
]
then
[
Bmid A'mid C'
]
would be a marked reversal state of smaller total (Phi), contradicting global minimality. Hence (Amid C) is frozen-minimal for the carrier (B). Applying Lemma 11 to that frozen complement gives the asserted reversals on (A). (square)

The unresolved global case has therefore narrowed to two regimes:

1. the marked-minimum size profile is nearly balanced at the top,
   [
   |C|le |B|+1;
   ]
2. the two endpoints of the largest component simultaneously reverse both end edges of each smaller component.

This dichotomy is valid for arbitrary order. It is the appropriate starting point for a general reduction to the complementary-splice framework rather than for further bounded-order case analysis.

### Imbalance at a global marked minimum forces bounded support

**Corollary 13.** Let
[
Amid Bmid C
]
be a marked reversal state minimizing (Phi) globally among all marked reversal states, with
[
|A|le |B|le |C|.
]
If
[
|C|ge |B|+2,
]
then (H) contains a Hamiltonian component of order at most five whose complement has path-cover number two. More precisely, either (|A|le3), or there is a Hamiltonian four- or five-support containing an endpoint of (C) and both displayed endpoints of (A).

**Proof.** By Corollary 12, each endpoint (c) of (C) reverses both displayed end edges of (A). Write
[
A=(a_1,ldots,a_r).
]

If (rle3), the displayed component (A) is already a bounded Hamiltonian support, and its complement is two-covered by (Bmid C).

Assume (rge4). Put
[
T={a_1,a_r,c}.
]
Consider the two four-sets
[
Tcup{a_2},
qquad
Tcup{a_{r-1}}.
]
If either is Hamiltonian, we have the required Hamiltonian four-support.

Assume both are non-Hamiltonian. The two-bad-four-extension lemma from [[localextend01]], applied to the common three-set (T) and the two distinct exterior vertices (a_2,a_{r-1}), gives a Hamiltonian path on
[
Tcup{a_2,a_{r-1}},
]
a five-set containing (c) and both displayed endpoints (a_1,a_r).

Thus in all cases there is a Hamiltonian support (K) of order four or five containing the asserted anchor vertices, unless (A) itself already has order at most three.

Since (K) is a proper Hamiltonian support in a minimum counterexample, minimum-counterexample calculus gives
[
operatorname{pc}(H-K)le2.
]
The complement cannot be Hamiltonian, because then (K) together with a Hamilton path on (H-K) would two-cover (H). Hence
[
operatorname{pc}(H-K)=2.
]
(square)

Therefore the imbalanced branch of the global marked-reversal minimum is already reduced, at arbitrary order, to bounded support. The only marked-minimum regime not yet reduced in this way is
[
|C|le |B|+1.
]

This isolates the genuinely global remaining case: a nearly balanced pair of largest components in a marked-reversal state. No bounded-order hypothesis is involved.



### A global marked minimum is almost equitable unless bounded support appears

**Corollary 14.** Let
[
Amid Bmid C
]
be a marked reversal state minimizing (Phi) globally, with
[
|A|le |B|le |C|.
]
If (H) has no Hamiltonian support of order four or five arising from the marked-minimum analysis, then
[
|B|le |A|+1
qquad	ext{and}qquad
|C|le |B|+1.
]
In particular
[
|C|-|A|le2.
]

**Proof.** Corollary 13 already shows that
[
|C|ge |B|+2
]
forces bounded Hamiltonian support. Hence, in the unresolved branch,
[
|C|le |B|+1.
]

It remains to compare (A) and (B). Write
[
A=(a_1,ldots,a_r),
]
and suppose the marked reversal is on the terminal edge (a_{r-1}a_r). Assume for contradiction that
[
|B|ge r+2.
]

Let (z) be any endpoint of (B). If
[
(z,a_1,a_2)
]
were tight, then
[
(z,a_1,ldots,a_r)
]
would be a Hamilton path on (Acup{z}), while deleting the endpoint (z) from (B) leaves a tight path. Repartitioning (Amid B) therefore changes their sizes from
[
(r,|B|)
]
to
[
(r+1,|B|-1).
]
The potential change is
[
(r+1)^2+(|B|-1)^2-r^2-|B|^2
=
2(r-|B|+1)<0.
]
The displayed terminal edge of (A) and its standing external reversal are untouched. Hence the new state is still marked, contradicting global minimality.

Therefore
[
(z,a_1,a_2)
]
is non-tight, and boundary antisymmetry gives
[
(a_2,a_1,z)
]
tight.

The same argument applies to both endpoints of (B). It also applies to both endpoints of (C), since
[
|C|ge|B|ge r+2.
]
Thus there are at least four distinct vertices (zin V(B)cup V(C)) satisfying
[
(a_2,a_1,z)
]
tight.

Choose any three of them. The three-hook consequence of [[localextend01]] produces a Hamiltonian support of order four or five containing the ordered anchor pair
[
(a_2,a_1),
]
contrary to the unresolved assumption.

Hence
[
|B|le |A|+1.
]
Together with
[
|C|le |B|+1,
]
this proves the result. (square)

Thus every unresolved global marked-reversal minimum has an almost equitable size profile:
[
(r,r,r),qquad (r,r,r+1),qquad (r,r+1,r+1),
qquad	ext{or}qquad (r,r+1,r+2)
]
up to the displayed ordering of component sizes.

The remaining global problem is therefore no longer arbitrary imbalance. It is to exploit the marked reversal inside these four near-balanced profile families.



### Carrier switching removes the remaining size gap

**Lemma 15 (carrier switch between displayed components).** Let
[
A=(a_1,ldots,a_r),qquad B=(b_1,ldots,b_s)
]
be two nontrivial components of a spanning three-cover of a minimum counterexample. Then either (B) is a marked reversal carrier in the same three-cover, or (H) contains a Hamiltonian four-support.

**Proof.** The concatenation (AB) cannot be tight, since together with the third displayed component it would give a two-cover. By Lemma 1 of [[global_augmentation_by_complementary_path_splices]], either
[
(b_1,a_r,a_{r-1})
]
is tight, marking (A), or
[
(b_2,b_1,a_r)
]
is tight, marking (B).

Likewise (BA) cannot be tight. Hence either
[
(a_1,b_s,b_{s-1})
]
is tight, marking (B), or
[
(a_2,a_1,b_s)
]
is tight, marking (A).

Suppose (B) is not marked by either comparison. Then
[
(b_1,a_r,a_{r-1}),qquad(a_2,a_1,b_s)
]
are tight.

If
[
(a_1,b_s,b_1)
]
is tight, then
[
(a_2,a_1,b_s,b_1)
]
is a Hamiltonian four-path. If
[
(b_s,b_1,a_r)
]
is tight, then
[
(b_s,b_1,a_r,a_{r-1})
]
is a Hamiltonian four-path. If both displayed middle triples are non-tight, their boundary flips
[
(b_1,b_s,a_1),qquad(a_r,b_1,b_s)
]
are tight, and
[
(a_r,b_1,b_s,a_1)
]
is a Hamiltonian four-path. (square)

**Corollary 16 (full balance or bounded support).** Let
[
Amid Bmid C
]
be a globally (Phi)-minimal marked reversal state with
[
|A|le |B|le |C|.
]
Then either (H) contains a Hamiltonian support of order at most five with two-coverable complement, or
[
|B|le |A|+1,qquad |C|le |B|+1,
]
and in fact
[
|C|-|A|le1.
]

Equivalently the unresolved size profiles are exactly
[
(r,r,r),qquad(r,r,r+1),qquad(r,r+1,r+1).
]

**Proof.** Corollary 14 already gives
[
|B|le |A|+1,qquad |C|le |B|+1.
]
Only the profile ((r,r+1,r+2)) remains to exclude.

Assume
[
|A|=r,qquad |B|=r+1,qquad |C|=r+2.
]
If (rle5), then the displayed Hamiltonian component (A) itself is bounded support with two-coverable complement (Bmid C). Hence assume (rge6).

By Lemma 15, unless a Hamiltonian four-support already exists, (C) can be taken as the marked carrier in this same state. Global marked minimality then implies that
[
Amid B
]
is minimum-potential among all two-covers of (H-C): a lower-potential replacement would give a marked three-cover of smaller total (Phi).

But
[
|B|=|A|+1,
]
so no contradiction yet. Now instead take (B) as marked carrier, again using Lemma 15. Its frozen complement is
[
Amid C,
]
whose component orders differ by two. Lemma 11 therefore applies and says that each endpoint of (C) reverses both displayed end edges of (A). Corollary 13's local double-reversal argument then produces a Hamiltonian support of order at most five with two-coverable complement, contradiction.

Thus the profile ((r,r+1,r+2)) is impossible in the unresolved branch. (square)

Therefore the global marked-reversal problem lands exactly in the three near-equitable size families treated separately in Article II, with no bounded-order hypothesis.



### Global marked minima reduce to two disturbance geometries

**Corollary 17.** Let
[
Amid Bmid C
]
be a globally (Phi)-minimal marked reversal state of a minimum counterexample. Unless a Hamiltonian support of order at most five with two-coverable complement has already appeared, the state has one of the three absolute-minimum profiles
[
(r,r,r),qquad (r,r,r+1),qquad (r,r+1,r+1).
]
Consequently the Article II profile theorems produce, after the standard reductions, either

1. an external tight triple reversing an edge of a relevant displayed or comparison path; or
2. an inherited displayed edge split between two comparison paths, or a leave-and-return disturbance through a nonempty exterior segment.

**Proof.** Corollary 16 leaves exactly the three displayed size profiles. For totals (3r,3r+1,3r+2), respectively, these are the absolute minimizers of
[
x^2+y^2+z^2
]
among positive integer triples of the same sum. Hence the state is a genuine (Phi)-minimum in its whole pairwise-repartition component, not merely among marked states.

Apply the corresponding profile theorem from Article II:
[[quadratic_potential_and_pairwise_repartition_the_size_profile_rrr]],
[[quadratic_potential_and_pairwise_repartition_the_size_profile_r1rr]],
or
[[quadratic_potential_and_pairwise_repartition_the_size_profile_r1r1r]].

Their outputs are order disagreement, direct mixing between displayed supports, split inherited edges, leave-and-return block patterns, reversing tight triples, or the additional same-side recurrence structures in the ((r,r+1,r+1)) profile.

Order disagreement gives an external reversing triple by Lemma 1 of this Section. Direct mixing enters the disturbance theorem
[[path_disturbance_endpoint_reversal_descent_or_an_omission_swap]], which yields split/leave-and-return, external reversal, a two-cover, strict descent, or a compatible omission swap. Strict descent contradicts the global marked minimum whenever the marked certificate survives; the compatible neutral residue is precisely the bridge-manufacture interface now isolated in Article III. The same-side recurrence alternatives either give bounded common-core structure or return to these comparison disturbances by the Article II/IV recurrence analysis.

Thus, outside bounded support and the coherent neutral omission-swap residue, the only genuinely geometric outputs are external reversal and split/leave-and-return. (square)

This gives an arbitrary-order chain
[
	ext{external reversal}
Longrightarrow
	ext{global marked minimum}
Longrightarrow
	ext{absolute equitable profile}
Longrightarrow
	ext{reversal or split disturbance}.
]

Hence the remaining new global mathematics is not a small-order classification. It is the conversion of a split/leave-and-return comparison—or its compatible neutral omission-swap residue—into the abstract one-defect bridge of Article III.
