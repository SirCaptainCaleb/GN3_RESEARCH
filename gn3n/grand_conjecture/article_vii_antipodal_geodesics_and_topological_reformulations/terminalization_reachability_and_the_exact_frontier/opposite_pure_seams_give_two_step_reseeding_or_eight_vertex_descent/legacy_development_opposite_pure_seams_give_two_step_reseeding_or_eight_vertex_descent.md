# Opposite pure seams give two-step reseeding or eight-vertex descent — preserved pre-item development

## Opposite pure seams give a two-step descent/reseed mechanism

Let (H) satisfy
[
kappa_2(H)=2
]
and let
[
Smid Pmid Q
]
be a saturated maximal-support state, with
[
P=(p_1,ldots,p_m),qquad Q=(q_1,ldots,q_t),
qquad m,tge5.
]

Assume both legitimate oriented seams are in the pure cross-seam branch of
[[every_deletion_critical_complement_corner_forces_a_hamiltonian_four_support]].
Thus
[
K_{PQ}={p_{m-1},p_m,q_1,q_2}
]
and
[
K_{QP}={q_{t-1},q_t,p_1,p_2}
]
are Hamiltonian four-supports.

Because (m,tge5), these two supports are disjoint.

Apply [[maximal_support_seams_reduce_to_reseeding_or_four_vertex_descent]] first to (K_{PQ}).

### First seam

Either
[
operatorname{pc}(H-K_{PQ})le2,
]
in which case (K_{PQ}) is an admissible bounded seed, or
[
H_1=H-K_{PQ}
]
has no spanning two-cover.

Assume the second case.

Since (K_{QP}cap K_{PQ}=arnothing), the opposite support (K_{QP}) remains Hamiltonian in (H_1).

### Opposite seam survives the first descent

Now inspect
[
H_1-K_{QP}
=
H-(K_{PQ}cup K_{QP}).
]

Either
[
operatorname{pc}(H_1-K_{QP})le2,
]
so (K_{QP}) is an admissible bounded seed in the strictly smaller no-two-cover graph (H_1), or
[
H_2=H-(K_{PQ}cup K_{QP})
]
has no spanning two-cover.

Thus two opposite pure seams give, without recomputing any endpoint structure, the trichotomy

1. reseed immediately in (H);
2. descend by four vertices and reseed immediately in (H_1);
3. descend by eight vertices to (H_2).

### The twice-descended graph has explicit residual rails

In the third case,
[
H_2
=
S
mid
(p_3,ldots,p_{m-2})
mid
(q_3,ldots,q_{t-2}),
]
with empty intervals omitted.

The residual rail orders are
[
m-4,qquad t-4.
]

If (m=5), the residual (P)-rail is a singleton. Deleting that one vertex leaves the two Hamiltonian paths
[
Smid(q_3,ldots,q_{t-2}),
]
so, because (H_2) itself has no two-cover,
[
kappa_2(H_2)=1.
]

If (m=6), deleting the two-vertex residual (P)-rail leaves the same two-cover, hence
[
kappa_2(H_2)le2.
]

The same statements hold with (P,Q) exchanged.

Therefore:

> **Two-seam depth bound.** A twice-descended state that escapes the already-developed deletion-distance-one/two machinery can occur only when
> [
> oxed{m,tge7.}
> ]

Equivalently, opposite pure seam certificates strip two boundary layers from both complementary rails before any genuinely higher-deletion-distance residue can survive.

No cyclic rotation, path reversal, minimum-counterexample induction, or finite computation is used.
