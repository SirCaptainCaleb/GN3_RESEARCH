# Sharp affine NORI fixed-order obstruction: all roots have exactly two switches at rank n−5

# Sharp rank-(n−5) NORI example: a fixed permutation admits exactly two switches, never fewer

Let n=7 and fix the direction order pi=(1,2,3,4,5,6,7). Define the following ordered-three-face colors as affine functions of exterior face bits z_i:
  c(F,(1,2,3))=0,
  c(F,(2,3,4))=z_7,
  c(F,(3,4,5))=1+z_1+z_7,
  c(F,(4,5,6))=z_1,
  c(F,(5,6,7))=0.
These five ordered triples are distinct from each other and from their own reversed orders. Extend to the reversed-ordered triple of each prescribed face by
  c(bar F,(k,j,i))=1+c(F,(i,j,k)),
so the ACTIVE ordered-three-face NORI axiom holds. Fill all other ordered-triple reversal orbits arbitrarily with affine exterior-bit functions and define their antipodal-reverse mates by the same equation. This is well-defined, corner-independent on each ordered physical face, and affine in its exterior bits.

**Theorem (sharpness).** For every one of the 2^7 starting roots x, the five ordered-three-face colors along the pi-directed full antipodal geodesic are
  C(x)=(0,x_7,x_7+x_1,1+x_1,0).
Explanation: after the first two steps, position1 is flipped, so its physical exterior bit is z_1=1+x_1 in the third and fourth windows, while position7 is unflipped until the final step.

The four successive color changes are therefore
  D(x)=(x_7,x_1,1+x_7,1+x_1).
Each pair (D1,D3) and (D2,D4) has precisely one nonzero bit, so EVERY root yields EXACTLY TWO color changes and NO root makes the fixed direction order pi good. The affine switch matrix M_pi has rank exactly2=n−5; its two-dimensional parity check imposes D1+D3=1 and D2+D4=1. Thus the rank >=n−4 threshold for a good fixed-order root from the preceding syndrome theorem is sharp, even among fully valid antipodal-reversal-odd ordered-face colorings.

The attainable two-switch patterns are precisely the complete bipartite cross pairs I={1,3}, J={2,4}: for each of the four possible crossing pairs there are 32 roots, because root bits x_1 and x_7 determine the switch vector and the remaining five bits are unrestricted.

**Critical scope.** This coloring is NOT a counterexample to the grand conjecture: it obstructs only the chosen direction permutation, and other permutations may admit full one-switch geodesics. It also does not refute the affine exterior three-chain subclass theorem, because its exterior coefficient vectors vary with the ordered triple. The point is to show the universal fixed-order rank criterion has an exact tight obstacle, which a global permutation-exchange argument must eliminate.
