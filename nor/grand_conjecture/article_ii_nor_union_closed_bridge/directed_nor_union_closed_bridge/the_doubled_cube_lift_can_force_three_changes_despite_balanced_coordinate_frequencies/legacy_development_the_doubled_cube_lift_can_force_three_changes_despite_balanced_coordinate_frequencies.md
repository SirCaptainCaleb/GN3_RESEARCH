# The doubled-cube lift can force three changes despite balanced coordinate frequencies — preserved pre-item development

## Composition

(none yet)

## Development

## The canonical doubled-cube lift can force three changes on every antipodal geodesic

This tests the doubled-cube construction in the research charter against the proposed one-change geometry. It uses a union-closed family, not an arbitrary set family.

### Proposition
For every finite ground set V containing distinct coordinates a,b, there is a nontrivial union-closed family F such that:
1. each old coordinate occurs in precisely half the members of F;
2. its canonical antipodal vertex-coloring lift to Q_{V union {star}} changes color three times along every antipodal geodesic.

### Proof
Let R=V\{a,b}, and put
F={C:C subseteq R} union {C union {a,b}:C subseteq R}.
Equivalently a set belongs to F if and only if it contains both a,b or neither.

The family is union-closed: the union of two members still contains both distinguished coordinates or neither, and its R-part is an arbitrary subset of R.

Its size is 2^{|R|+1}. Each of a,b occurs in the second half of the family. Each coordinate of R occurs in half the choices of C, in both halves. Thus every coordinate has frequency |F|/2.

Use bits x_a(A),x_b(A) in {0,1} and membership sign g(A)=+1 on F and -1 otherwise. Then
g(A)=(-1)^{x_a(A)+x_b(A)}.
Complementing A flips both distinguished bits, so
g(V\A)=g(A).
The canonical lift is
G(A,0)=g(A), G(A,1)=-g(V\A),
hence
G(A,s)=(-1)^{x_a(A)+x_b(A)+s}.
This is antipodal because complementation flips all three displayed bits.

Every antipodal geodesic in the enlarged cube flips every coordinate once. Its color changes precisely when it flips a, b, or star. Each of these occurs once; other coordinates have no effect on the color. Therefore the full vertex-color word has three changes, for every starting vertex and every coordinate order. Square.

### Consequences for the bridge program
The canonical antipodal lift preserves Frankl's coordinate-bias statement, but union closure does not make that lift admit a one-change antipodal vertex path. Here Frankl holds with equality at every coordinate, while the proposed vertex-path conclusion fails uniformly.

Accordingly, a reduction cannot simply apply a one-change vertex-coloring principle to the doubled lift. It must alter the colored objects, introduce an additional construction, or use a different feature of the lift.

This result does not refute the directed translation-invariant coordinate conjecture. G depends on the base vertex and is a vertex coloring, whereas the directed coordinate sector colors ordered windows with reversal antisymmetry. The distinction is precisely why the charter's ordered-window encoding step is essential.

The example persists under adding arbitrarily many free old coordinates, so its role is a structural obstruction to this particular reduction step rather than a dimension cutoff.
