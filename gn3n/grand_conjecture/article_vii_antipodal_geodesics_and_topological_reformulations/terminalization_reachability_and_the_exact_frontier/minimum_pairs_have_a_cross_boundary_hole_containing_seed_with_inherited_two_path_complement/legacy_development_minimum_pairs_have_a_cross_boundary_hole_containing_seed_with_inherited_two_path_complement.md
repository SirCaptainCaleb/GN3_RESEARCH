# Minimum pairs have a cross-boundary hole-containing seed with inherited two-path complement — preserved pre-item development

## Every minimum pair has a cross-boundary hole-containing Hamiltonian seed

Let
[
X={x,y}
]
be a minimum two-cover deletion pair and fix a displayed complementary two-cover
[
H-X=Pmid Q.
]
Assume (P) has order at least two and (Q) is nonempty. Write
[
P=(ldots,a,b),qquad Q=(q_1,q_2,ldots).
]
Put
[
F={a,b,q_1,x,y}.
]

Then (H) contains a Hamiltonian support (S_0subseteq F), of order four or five, such that:
1. ({x,y}subseteq S_0);
2. (S_0) meets both displayed complementary paths;
3. (H-S_0) is covered by at most two inherited contiguous subpaths of (P,Q).

### Proof

If (F) is Hamiltonian, take
[
S_0=F.
]
Its complement is covered by
[
P-{a,b}
qquad	ext{and}qquad
Q-{q_1},
]
with empty intervals omitted.

Assume (F) is non-Hamiltonian. By the non-Hamiltonian-five-set theorem in [[smallset01]], at most one four-subset of (F) is non-Hamiltonian.

Consider the two four-subsets
[
K_1=F-{q_1}={a,b,x,y},
]
[
K_2=F-{a}={b,q_1,x,y}.
]
At least one of (K_1,K_2) is Hamiltonian.

If (K_1) is Hamiltonian, then
[
H-K_1
]
is covered by the inherited paths
[
P-{a,b}
qquad	ext{and}qquad
Q.
]

If (K_2) is Hamiltonian, then
[
H-K_2
]
is covered by
[
P-{b}
qquad	ext{and}qquad
Q-{q_1}.
]
Both are contiguous inherited path intervals.

Thus in every case the desired (S_0) exists. (square)

### Consequences

This seed contains the entire minimum pair and is tied to an actual (P|Q) seam. It is therefore stronger, for endpoint transport purposes, than an arbitrary bounded Hamiltonian support with two-coverable complement.

In particular, [[seed_preserving_maximalization_retains_absolute_endpoint_nonaugmentability]] may be applied while retaining both hole labels and the cross-boundary seed.

Even more conservatively, one may enlarge (S_0) only by exposed endpoints of the two inherited complementary intervals. This preserves the original interval geometry at every step and terminates at an endpoint-saturated three-cover
[
Smid P'mid Q'
]
in which (S) contains (x,y), (P',Q') are inherited intervals of the original (P,Q), and no displayed endpoint of (P'|Q') can enlarge (S) Hamiltonianly.

No splice failure, cyclic rotation, path reversal, minimum-counterexample hypothesis, or finite computation is used.
