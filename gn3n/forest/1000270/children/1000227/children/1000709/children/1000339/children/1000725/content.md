# Four good deletions need not contain a compatible triangle

## Statement

There exists a non-Hamiltonian edge-ordered five-vertex boundary tournament with exactly four Hamiltonian vertex deletions such that no three good deletion labels admit Hamilton paths that are pairwise compatible on their common three-vertex intersections. Hence the four-label synchronized omission family at small-side order four does not automatically yield a compatible deletion triangle.

## Body

# Four good deletions need not contain a compatible triangle

There is an edge-ordered complete graph on five vertices which has no increasing Hamilton path, has four Hamiltonian vertex deletions, but for which no three good deletion labels admit pairwise-compatible Hamilton paths.

Let the vertex set be {0,1,2,3,4} and order the ten ordinary edges by

01 < 02 < 34 < 13 < 03 < 24 < 04 < 12 < 14 < 23.

Write a vertex word for the corresponding path.

## Hamilton paths of the vertex deletions

For an edge-ordered K4, the first and third edges of any Hamilton path are disjoint. Thus they form one opposite-edge matching, with the first edge lower than the third, and the middle edge must be a cross edge whose rank lies strictly between them. Conversely every such cross edge gives exactly one increasing Hamilton path.

Applying this observation gives exactly:

| deleted vertex | increasing Hamilton paths |
| --- | --- |
| 0 | 3421, 4312 |
| 1 | none |
| 2 | 1304, 3041 |
| 3 | 0214, 0241, 1024, 2041 |
| 4 | 0123, 0132, 1023, 1032 |

For completeness, the nonempty opposite-edge intervals are:

- delete 0: 34<12 contains 13 and 24;
- delete 2: 03<14 contains 04, and 13<04 contains 03;
- delete 3: 01<24 contains 02, and 02<14 contains 04,12,24;
- delete 4: 01<23 contains 02,03,12,13.

All other opposite-edge intervals contain no cross edge. In particular deletion 1 is non-Hamiltonian.

## The full five-set is non-Hamiltonian

Any increasing Hamilton path on all five vertices would, after deleting one endpoint d, leave one of the listed increasing Hamilton paths of K5-d. We check that none of the listed paths can be extended by its missing vertex at either endpoint.

Using the displayed edge order:

- d=0:
  - 3421 would require 03<34 or 12<01;
  - 4312 would require 04<34 or 12<02.
- d=2:
  - 1304 would require 12<13 or 04<24;
  - 3041 would require 23<03 or 14<12.
- d=3:
  - 0214 would require 03<02 or 14<34;
  - 0241 would require 03<02 or 14<13;
  - 1024 would require 13<01 or 24<34;
  - 2041 would require 23<02 or 14<13.
- d=4:
  - 0123 would require 04<01 or 23<34;
  - 0132 would require 04<01 or 23<24;
  - 1023 would require 14<01 or 23<34;
  - 1032 would require 14<01 or 23<24.

Every displayed inequality is false. Hence the five-set itself has no increasing Hamilton path.

Its good deletion labels are therefore exactly {0,2,3,4}.

## No compatible deletion triangle

Compatibility of two Hamilton deletion paths means that their restrictions to the common three vertices have the same linear order.

Three pairs of good labels are completely incompatible.

For deletions 0 and 3, the two 0-deletion paths restrict on {1,2,4} to

421, 412,

whereas the four 3-deletion paths restrict to

214, 241, 124, 241.

There is no match.

For deletions 0 and 4, the 0-deletion paths restrict on {1,2,3} to

321, 312,

whereas the 4-deletion paths restrict to

123, 132, 123, 132.

Again there is no match.

For deletions 2 and 4, the 2-deletion paths restrict on {0,1,3} to

130, 301,

whereas the 4-deletion paths restrict to

013, 013, 103, 103.

Again there is no match.

Every three-element subset of {0,2,3,4} contains at least one of the forbidden pairs {0,3}, {0,4}, {2,4}. Therefore no three good deletion labels admit pairwise-compatible Hamilton deletion paths.

Thus the four-label synchronized omission family available when the small deletion side has order four does not, by five-set structure alone, force entry into the compatible-triangle/common-gap machinery. Additional information from the fixed opposite path, endpoint hooks, or global counterexample structure is genuinely necessary. ∎
