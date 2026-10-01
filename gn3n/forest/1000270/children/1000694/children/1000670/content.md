# Defect-span local-search theorem

## Statement

Choose a spanning ordering pi minimizing lexicographically (defect span, number of defect centers, sum of distances between consecutive defect centers). Conjecture that any such locally optimal ordering has defect span at most two. The proposed maneuver is to use adjacent transpositions and short block rotations around the leftmost and rightmost defect centers: if the two extreme defects are separated, boundary antisymmetry should force one of a bounded menu of rotations that removes an extreme defect without creating a farther one.

## Body

Why it might matter globally:
A spanning ordering has defect span at most two exactly when it encodes a two-cover, so this attacks the conclusion directly with a scalar/local-search invariant. It avoids choosing deletion covers, support partitions, or half-order states.

Plausible first attack:
Write the five- or six-vertex window consisting of two vertices before/after the leftmost defect plus the next tight run. Enumerate symbolically which triples flip under the two shortest rotations. Prove a local lemma: unless a second defect lies within distance two, one of the rotations strictly improves the lexicographic defect objective. Then mirror at the rightmost defect and try to make the obstruction windows incompatible.