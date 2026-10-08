# A lexicographic moment potential forbids cycles of same side bubble repairs

## Composition

(none yet)

## Development

## A lexicographic moment potential forbids cycles of same-side bubble repairs

Fix a ternary switch cut k and threshold target. For a switch state z let
[
E(z)
]
be the number of violating windows, and let
[
M(z)=sum_{iin D(z)} i^2,
]
where D(z) is the set of violating window ranks.

Consider a same-side bubble edge in the violation-to-satisfaction direction as in subsections 143-144. On the four affected window positions
[
j-1, j, j+1, j+2,
]
the two central windows change from violations to satisfactions.

There are two cases.

### Strict case

If fewer than two outer defects are created, then
[
E(z')<E(z).
]

### Equality case

If the defect count is preserved, subsection 144 shows that the local defect pattern is exactly
[
0,1,1,0
longmapsto
1,0,0,1.
]
Hence
[
M(z')-M(z)
=
(j-1)^2+(j+2)^2-j^2-(j+1)^2
=
4.
]

Therefore every violation-to-satisfaction same-side bubble repair strictly increases the lexicographically ordered potential
[
Psi(z)=(-E(z),,M(z)).
]

Because there are finitely many switch states at a fixed cut, no directed cycle of same-side bubble repairs is possible.

### Consequence

The carrier-extraction dichotomy now has a termination principle on both branches:

- switch-crossing complementary edges are genuine endpoint repairs;
- same-side violation-to-satisfaction bubbles form an acyclic directed dynamics under Psi.

Thus a topological opposite-middle carrier cannot support an indefinitely circulating sequence of same-side equality transports. Repeatedly taking available violation-to-satisfaction bubble repairs must terminate after finitely many steps at a state where either:
1. threshold defect count has dropped;
2. the relevant violation has reached a boundary/cut interaction;
3. no further same-side violation-to-satisfaction bubble is available.

Combined with the threshold-band potential for flat endpoint combing, this removes two distinct sources of repair cycles. Any surviving terminal obstruction must be supported by full-curvature barriers or by a state in which the opposite-middle violation cannot be continued through same-side bubble moves.
