# Tetrahedral link curvature has only zero one or four cyclic pivots

## Composition

(none yet)

## Development

## Tetrahedral link-curvature has only 0, 1, or 4 cyclic pivots

Let (alpha) be an alternating orientation on triples. For a four-set
[
T={0,1,2,3},
]
say that a vertex (iin T) is **curved in (T)** if the other three vertices form a directed triangle in the pivot link tournament (G_i).

Write the four face-orientation bits in increasing order as
[
A=alpha(0,1,2),quad
B=alpha(0,1,3),quad
C=alpha(0,2,3),quad
D=alpha(1,2,3).
]

A direct translation into the four pivot links gives:

[
K_0 iff A=C
e B,
]
[
K_1 iff B=D
e A,
]
[
K_2 iff A=C
e D,
]
[
K_3 iff B=D
e C,
]
where (K_i) denotes that pivot (i) is curved.

### Theorem

For every oriented tetrahedron, the number of curved pivots is exactly
[
0,quad 1,quad	ext{or}quad 4.
]
In particular, exactly two or exactly three cyclic pivot links are impossible.

### Proof

If two of the (K_i) hold, their displayed equalities force the remaining two.

For example, if (K_0) and (K_2) hold, then
[
A=C,qquad B
e A,qquad D
e A.
]
Since the values are binary, (B=D=1-A). Therefore
[
B=D
e A,qquad B=D
e C,
]
so (K_1) and (K_3) also hold.

If (K_0) and (K_1) hold, then
[
A=C,quad B
e A,quad B=D,quad A
e B,
]
so again
[
A=C=1-B=1-D,
]
which gives (K_2) and (K_3). The other pairs follow by symmetry.

Thus whenever at least two pivots are curved, all four are. Otherwise there are zero or one. (square)

### Interpretation

Every oriented 3-simplex has one of three curvature types:

1. **flat:** all four pivot links are transitive on the opposite face;
2. **singly curved:** exactly one vertex is distinguished by a cyclic opposite link;
3. **fully curved:** every pivot link is cyclic.

This is a higher-dimensional analogue of the triangle orientation-plus-defect decomposition. Failure of the simplex orientation to come from a global cyclic order is therefore not arbitrary across pivots: on each tetrahedron its local link nontransitivity has a sharply quantized form.

A promising next reduction is to treat singly curved tetrahedra as carrying a marked vertex and fully curved tetrahedra as an irreducible parity defect. If the marked-vertex part can again be routed around by insertion, the pure-orientation obstruction would reduce to the fully curved tetrahedra.
