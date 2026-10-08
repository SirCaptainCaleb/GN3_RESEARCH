# Threshold cuts turn one-change NOR into antipodal rankwise reachability intersection — preserved pre-item development


Fix a polarity s in {+1,-1}. Let the ternary memory-lift DAG be layered by the number q of completed window transitions, with m=n-2 window signs in a full order.

At rank q define P_q^s to be the memory states reachable from the source by a prefix whose completed windows all have sign s. Define Q_q^s to be the memory states from which the sink is reachable by a suffix whose remaining windows all have sign -s.

Then a full coordinate order with sign word s...s,-s...-s and switch after q exists if and only if

P_q^s intersect Q_q^s is nonempty.

Indeed a state in the intersection concatenates an s-monochromatic prefix and a -s-monochromatic suffix, and conversely every one-change order determines the common memory state at its switch rank.

Thus NOR is equivalent to the existence of s and q with P_q^s intersect Q_q^s nonempty.

Reversal-oddness gives an exact antipodal relation. Reversing an s-monochromatic prefix produces a -s-monochromatic suffix on the reversed state. Therefore the memory-state involution carries

P_q^s  to  Q_{m-q}^s.

So a counterexample consists, for each s, of a rooted layered carrier P^s disjoint rank by rank from its antipodal image.

Geometrically, after realizing memory states as overlapping flag faces in the refined completed simplex, the rank q is precisely the threshold/cut coordinate. The family of one-change target patterns is an interval from the all--s pattern at q=0 to the all-s pattern at q=m, and reversal reflects this interval.

This is a natural Connector/Hex formulation: if all rankwise intersections are empty, the two antipodal reachability carriers admit a separator running through the threshold prism. A closure proof can target the connected separator rather than a support-only Sperner label.

The formulation retains full memory state and full support; it does not splice deletion orders or drop coordinates.
