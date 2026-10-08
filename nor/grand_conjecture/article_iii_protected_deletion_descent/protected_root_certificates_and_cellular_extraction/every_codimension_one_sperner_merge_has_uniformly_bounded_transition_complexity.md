# Every codimension-one Sperner merge has uniformly bounded transition complexity

## Composition

(none yet)

## Development

## Every codimension-one Sperner merge has uniformly bounded transition complexity

Use the global good-order selector g(S) of root §163.

Let a codimension-one face step merge two consecutive proper blocks A|C into

B=A union C.

The fine-face witness uses

U=g(A)g(C),

while the coarse-face witness uses

U'=g(B),

with exactly the same outside prefix and suffix.

### Change count in the fine witness

The ternary status word internal to g(A) has at most one change. The same holds for g(C).

Concatenating two coordinate orders creates exactly two ternary windows crossing the A|C boundary, after endpoint clipping.

Therefore the status segment through A|C has schematic form

(word of g(A)), x, y, (word of g(C)),

where each outer word has at most one change.

The total number of changes in this entire merged-block segment is therefore at most

1 + 1 + 1 + 1 + 1 = 5:

- at most one inside A;
- at most one between the end of A's internal word and x;
- at most one between x and y;
- at most one between y and the beginning of C's internal word;
- at most one inside C.

The coarse witness g(B) has at most one internal change.

### Consecutive-change defect increment

Root §164 writes every defect label as

C(pi)
=
sum over actual transition roots
+
one first/last-change endpoint correction.

Hence the codimension-one label increment

Delta=C(P g(B) Q)-C(P g(A)g(C) Q)

is the difference of:
- at most one actual transition root from the coarse block order;
- at most five actual transition roots from the fine concatenation;
- the two endpoint-correction terms.

All transitions outside the merged block and its two ternary boundary collars cancel exactly.

Thus Delta is a linear combination of at most six actual transition roots plus at most four endpoint basis terms. Equivalently it is a sum of at most eight type-A root vectors after pairing the endpoint correction terms.

### Uniform interface bound

Consequently every codimension-one face-merge increment lies in a type-A coordinate subspace supported on at most sixteen physical coordinates, regardless of |A|, |C|, |B|, or ambient n.

The numerical bound sixteen is deliberately coarse; repeated endpoints usually make the support much smaller. The important point is uniformity.

### Significance

This is not a small-ambient-order reduction. The merged block may contain arbitrarily many coordinates, but only its two internal one-change switches and its two-window connector contribute to the Sperner label change.

Combined with root §165, every global Sperner zero decomposes with positive coefficients into uniformly bounded-interface merge increments arranged along one nested face flag.

Therefore any genuinely new incompatibility in the topological extraction must come from overlap of these bounded merge interfaces. Long solved interiors of proper blocks contribute no additional algebraic complexity.
