# Deletion-distance-one states have opposite hole-rooted admissible four-seeds

## Metadata

- ID: deletion_distance_one_states_have_opposite_hole_rooted_admissible_four_seeds
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 185
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Deletion-distance-one states have canonical admissible four-seeds at both ends

Assume (H) has no spanning two-cover and
[
kappa_2(H)=1.
]
Let
[
H-x=Pmid Q,
]
where
[
P=(p_1,ldots,p_r),qquad Q=(q_1,ldots,q_s).
]
By [[kappa_one_four_end_reversal]],
[
r,sge3
]
and
[
h(p_2,p_1,x)=1,qquad h(q_2,q_1,x)=1,
]
[
h(x,p_r,p_{r-1})=1,qquad h(x,q_s,q_{s-1})=1.
]

### Initial-end seed

Boundary antisymmetry at middle vertex (x) gives exactly one of
[
h(p_1,x,q_1)=1,
qquad
h(q_1,x,p_1)=1.
]

In the first case
[
(p_2,p_1,x,q_1)
]
is a tight Hamiltonian four-path.

In the second case
[
(q_2,q_1,x,p_1)
]
is a tight Hamiltonian four-path.

Thus there is a Hamiltonian four-support
[
K_Isubseteq{x,p_2,p_1,q_2,q_1}
]
containing (x,p_1,q_1) and one of (p_2,q_2).

Its complement is covered by two inherited intervals:
- in the first orientation,
  [
  (p_3,ldots,p_r)mid(q_2,ldots,q_s);
  ]
- in the second,
  [
  (p_2,ldots,p_r)mid(q_3,ldots,q_s).
  ]

Hence
[
operatorname{pc}(H-K_I)le2.
]

### Terminal-end seed

Exactly one of
[
h(p_r,x,q_s)=1,
qquad
h(q_s,x,p_r)=1
]
is tight.

Combining this boundary pair with
[
h(x,p_r,p_{r-1})=1,
qquad
h(x,q_s,q_{s-1})=1
]
gives exactly one of the tight Hamiltonian four-paths
[
(q_s,x,p_r,p_{r-1}),
qquad
(p_r,x,q_s,q_{s-1}).
]

Thus there is a Hamiltonian four-support
[
K_Tsubseteq{x,p_{r-1},p_r,q_{s-1},q_s}
]
containing (x,p_r,q_s) and one of (p_{r-1},q_{s-1}), again with inherited two-path complement.

Therefore:

> **Opposite seed theorem for (kappa_2=1).** Every deletion-distance-one no-two-cover state carries two explicitly located Hamiltonian four-supports (K_I,K_T), both containing the unique deletion label (x), one at each opposite boundary of the deletion cover, and each having two-coverable complement by inherited path intervals.

No minimum-counterexample hypothesis, cyclic rotation, path reversal, or computation is used.
