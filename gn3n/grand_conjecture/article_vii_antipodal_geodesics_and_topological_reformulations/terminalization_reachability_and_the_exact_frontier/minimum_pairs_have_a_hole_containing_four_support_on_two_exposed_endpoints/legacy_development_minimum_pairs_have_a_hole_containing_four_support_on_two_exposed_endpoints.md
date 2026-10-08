# Minimum pairs have a hole-containing four-support on two exposed endpoints — preserved pre-item development

## Development

## A minimum pair has a Hamiltonian four-support on two actual complementary endpoints

Let
[
X={x,y}
]
be a minimum two-cover deletion pair and let
[
H-X=Pmid Q
]
be a displayed complementary two-cover.

In a no-two-cover state, both (P) and (Q) have order at least two. Indeed, if (P={p}) were a singleton, the three-set ({x,y,p}) is Hamiltonian, and together with the Hamiltonian path (Q) would two-cover (H).

Write
[
P=(p_1,ldots,p_m),qquad Q=(q_1,ldots,q_t),
qquad m,tge2.
]
Let
[
E={p_1,p_m,q_1,q_t}
]
be the four exposed complementary endpoints.

Partition (E) by its orientation through the fixed pair ({x,y}):
[
E_+={zin E:h(x,z,y)=1},
qquad
E_-={zin E:h(y,z,x)=1}.
]
Boundary antisymmetry makes this a partition.

By pigeonhole, one class contains two distinct endpoints (u,v). The fixed-pair orientation-class theorem then gives
[
oxed{{x,y,u,v}	ext{ Hamiltonian}.}
]

Put
[
S_0={x,y,u,v}.
]

Because (u,v) are displayed endpoints of (P,Q), deleting them leaves at most two inherited contiguous path intervals:
- if (u,v) lie on different paths, truncate one endpoint from each;
- if they are the two endpoints of one path, its interior remains a tight path and the other displayed path is untouched.

Thus
[
operatorname{pc}(H-S_0)le2
]
with a two-cover inherited directly from the original (P|Q).

Therefore:

> **Exposed-endpoint four-support theorem.** Every genuine minimum deletion pair admits a Hamiltonian four-support consisting of the two hole labels and two exposed endpoints of a displayed complementary two-cover, whose complement is covered by at most two inherited path intervals.

No five-set extension theorem, splice failure, cyclic rotation, path reversal, minimum-counterexample hypothesis, or finite computation is used.

### Consequences

This sharpens [[minimum_pairs_have_a_cross_boundary_hole_containing_seed_with_inherited_two_path_complement]] from order (4/5) to order exactly four and uses only actual endpoints.

The seed is especially suited to [[seed_preserving_maximalization_retains_absolute_endpoint_nonaugmentability]]: one may maximalize while retaining both minimum-hole labels and this endpoint-rooted four-support.

Alternatively, maximizing only among hole-containing Hamiltonian supports whose complements remain two inherited intervals of the original (P|Q) preserves the original corridor geometry throughout.
