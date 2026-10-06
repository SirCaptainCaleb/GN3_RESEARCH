# Matching-block seam bands always yield a local both-hole admissible seed

## Metadata

- ID: matching_block_endpoint_rectangles_force_local_both_hole_seam_seeds
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 180
- Row version: 4
- Development version: 4
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Complete matching-block seam bands always yield a both-hole admissible seed

Let
[
X={x,y}
]
be a minimum deletion pair with
[
H-X=Pmid Q,
]
where
[
P=(p_1,ldots,p_m),qquad Q=(q_1,ldots,q_t),
qquad m,tge2.
]

Assume the complete matching-block residue of
[[minimum_pair_endpoint_seeds_are_cross_tail_or_a_complete_matching_block_rectangle]].
After exchanging (x,y) if necessary, every exposed cross-tail four-set
[
{x,y,p,q},
qquad
pin{p_1,p_m}, qin{q_1,q_t},
]
is non-Hamiltonian, and the corresponding matching-block hooks hold.

At the oriented seam (P	o Q), put
[
W={x,y,q_2,q_1,p_m,p_{m-1}}.
]

The matching-block and minimum-hole synchronization identities give the explicit tight five-path
[
(q_2,q_1,y,p_m,p_{m-1}).
]

We prove that this seam always contains a both-hole Hamiltonian support with inherited two-path complement.

### Case 1: an inner five-deletion is Hamiltonian

If either
[
W-{q_2}
qquad	ext{or}qquad
W-{p_{m-1}}
]
is Hamiltonian, it is a both-hole five-support.

Its complement is respectively
[
(p_1,ldots,p_{m-2})mid(q_2,ldots,q_t)
]
or
[
(p_1,ldots,p_{m-1})mid(q_3,ldots,q_t),
]
so it is an admissible seed.

### Case 2: both inner five-deletions are non-Hamiltonian

Assume
[
W-{q_2}
quad	ext{and}quad
W-{p_{m-1}}
]
are both non-Hamiltonian.

The common four-set
[
D={x,y,q_1,p_m}
]
is non-Hamiltonian by the standing complete matching-block endpoint hypothesis.

Consider first the bad five-set
[
F_P=W-{q_2}
={x,y,q_1,p_m,p_{m-1}}.
]
It contains the non-Hamiltonian four-subset (D=F_P-{p_{m-1}}).

By the non-Hamiltonian-five-set theorem, a non-Hamiltonian five-set has at most one non-Hamiltonian four-subset. Therefore every other four-subset of (F_P) is Hamiltonian. In particular
[
oxed{{x,y,p_m,p_{m-1}}	ext{ is Hamiltonian}.}
]

Its complement in (H) is exactly
[
(p_1,ldots,p_{m-2})mid Q,
]
so it is a both-hole admissible four-seed.

Similarly, in
[
F_Q=W-{p_{m-1}}
={x,y,q_2,q_1,p_m},
]
the same bad four-set is
[
D=F_Q-{q_2}.
]
Hence every other four-subset is Hamiltonian, and in particular
[
oxed{{x,y,q_1,q_2}	ext{ is Hamiltonian}.}
]

Its complement is
[
Pmid(q_3,ldots,q_t),
]
again an inherited two-cover.

Thus the equality packet produces **two** same-rail both-hole admissible four-seeds.

### Conclusion

> **Local seam-seed theorem.** In the complete matching-block endpoint residue, every oriented seam contains a Hamiltonian support of order four or five, containing both minimum-hole labels, whose complement is covered by two inherited path intervals. If both inner five-deletions fail, the seam actually contains the two explicit admissible four-seeds
> [
> {x,y,p_{m-1},p_m},
> qquad
> {x,y,q_1,q_2}.
> ]

The opposite seam has the symmetric conclusion.

Hence the former exact four-good equality packet is not a terminal disturbance branch in this positional setting; it collapses directly back to bounded-seed re-entry.

This replaces development version 3.

No cyclic rotation, path reversal, minimum-counterexample hypothesis, or computation is used.

## Frontier

- Development version when composed: None
- Development version now: 4
