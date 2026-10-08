# Residual A2 suffix holonomy factors through the Klein four group

## Composition

(none yet)

## Development

## Residual A2 suffix holonomy factors through the Klein four group

Continue the flat (A_2) replacement-cycle setup of the previous subsection. Let
[
U={x,y,z}
]
and let
[
s(j)=(s_x(j),s_y(j),s_z(j))inmathbb F_2^3
]
be the three suffix-scan bits on the edge
[
(t_j,t_{j+1}).
]

The transport identity says that the residual tournament at pivot (t_{j+1}) is obtained from the tournament at (t_j) by toggling exactly those residual edges whose endpoints have different scan bits.

### Switching class of a scan vector

Replacing (s(j)) by its global complement
[
s(j)+(1,1,1)
]
does not change which pairs of residual vertices have different bits. Hence the induced tournament switch depends only on the class
[
[s(j)]in
G:=
mathbb F_2^3/langle(1,1,1)angle
congmathbb F_2^2.
]

The zero class consists of
[
000, 111
]
and acts trivially.

The other three classes are exactly the three nontrivial Seidel switches on a three-vertex tournament: switching one residual vertex is the same as switching its complementary pair.

Successive suffix edges compose by addition in (G).

### Holonomy loop

The residual tournament starts and ends as the same directed 3-cycle. Therefore the total switching class along the suffix is zero:
[
sum_j [s(j)]=0
qquad	ext{in }G.
]

Discard the zero-class edges, which do not change the residual tournament, and choose a shortest nonempty contiguous excursion whose cumulative switching class returns to zero.

Because (G) has only four elements, the nonzero partial sums before the return are distinct and lie among only three states. Hence a minimal return uses at most four nontrivial switching events.

More precisely its nonzero switching word has one of the following finite types:

1. **length 2:** (a,a);
2. **length 3:** (a,b,a+b), the three distinct nonzero elements;
3. **length 4:** an alternating two-generator loop such as (a,b,a,b) up to relabeling.

Thus every long suffix holonomy loop contains a bounded first-return carrier with at most four genuine residual switching events. Arbitrarily long stretches between those events may have zero scan class, but the residual pair tournament is constant on those stretches.

### Significance

The recurrent flat (A_2) replacement obstruction is therefore not a genuinely long-range object. Its nontrivial suffix transport factors through the rank-two group (Gcongmathbb F_2^2) and every first return has one of three bounded combinatorial types.

This gives a finite closure target compatible with the strategy brainstorm:

> For each of the three minimal Klein-holonomy words above, construct a full-support surgery across the corresponding constant-tournament stretches, or show that the packet forces a protected replacement which escapes the (A_2) exchange cycle.

The long untouched portions of the suffix need not be deleted or truncated; they are carried as monochromatic constant-holonomy corridors between the bounded switching events.
