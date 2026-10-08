# Canonical Sperner witness gluing reduces to disjoint merge squares and three-block associativity diamonds

## Composition

(none yet)

## Development

## Canonical Sperner witness gluing reduces to disjoint merge squares and three-block associativity diamonds

Use the global good-order selector g(S) from root §163. A proper ordered-partition face

F=B_1|...|B_s

has canonical witness

pi_F=g(B_1)...g(B_s).

A codimension-one move in the face poset merges two adjacent blocks.

### Two merge moves

Take two available codimension-one merges from one ordered partition.

There are only two structural cases.

#### 1. Disjoint merges

Suppose the merges are

A|B -> AB

and, farther away,

C|D -> CD,

with disjoint block pairs.

Then applying the merges in either order gives the same ordered partition and the same canonical full witness, because

...g(A)g(B)...g(C)g(D)...

is replaced in either order by

...g(AB)...g(CD)...

with every other block unchanged.

Thus disjoint face merges form an exact realized square of canonical witness states.

For the defect label L(F)=C(pi_F), the edge increments satisfy the exact square identity

Delta_{AB}(F)+Delta_{CD}(F/AB)
=
Delta_{CD}(F)+Delta_{AB}(F/CD),

simply because both sides equal L(final)-L(initial).

#### 2. Overlapping merges

The only overlap is on three consecutive blocks

A|B|C.

There are exactly two length-two merge paths to the same coarser block:

A|B|C
 -> AB|C
 -> ABC,

and

A|B|C
 -> A|BC
 -> ABC.

The four canonical witness orders are

g(A)g(B)g(C),
g(AB)g(C),
g(A)g(BC),
g(ABC),

with the same outside prefix and suffix.

Hence every noncommuting primitive face-gluing cell is supported entirely on the single proper block

A union B union C

plus its bounded ternary boundary collar.

Again the defect increments have zero algebraic holonomy:

[L(AB|C)-L(A|B|C)]
+
[L(ABC)-L(AB|C)]

=
[L(A|BC)-L(A|B|C)]
+
[L(ABC)-L(A|BC)].

### Ordered-partition coherence

Any two saturated merge chains between the same ordered partitions are related by repeated exchanges of these two primitive types:
- commuting disjoint merges;
- three-block associativity diamonds.

Therefore the entire canonical Sperner witness system has a local 2-dimensional coherence presentation with no larger primitive face-lattice relation.

### Consequence for Article III

Combined with:
- block-locality of face increments (§164);
- Abel decomposition of every Sperner zero (§165);
- bounded transition complexity of one merge (§166);

the global Sperner extraction problem reduces to the following local realization cells:

1. disjoint merge squares, which are already exactly compatible at the witness-state level;
2. three-block associativity diamonds inside one proper merged block.

Thus any failure to turn the topological flag into compatible repair dynamics must already occur inside one three-block merge diamond or in the two-sided boundary collar attaching that diamond to the frozen outside order.

This is the ordered-partition analogue of localizing a Coxeter complex obstruction to commuting squares and braid cells.
