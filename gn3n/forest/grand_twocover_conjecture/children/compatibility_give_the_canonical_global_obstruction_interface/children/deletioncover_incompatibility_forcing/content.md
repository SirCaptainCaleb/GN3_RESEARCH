# Deletion-cover incompatibility forcing

## Statement

Build the graph on deletion labels in which two labels are adjacent when selected exact two-covers are fully compatible on their common vertices. Since four pairwise compatible deletion covers glue to a global two-cover, a minimum counterexample forbids K4. Conjecture that one can choose exact deletion covers so that boundary-tournament order constraints force minimum degree high enough, or force a local transitive triangle extension, to create a K4 unless a direct two-cover already exists.

## Body

Why it might matter globally:
This would turn the grand theorem into a global consistency statement across deletion covers rather than a local transport process. It is order-independent and exploits a certified sharp gluing theorem: enough compatibility is already closure, so the only task is to force compatibility density from antisymmetry and path order.

Plausible first attack:
For each deleted vertex choose an exact two-cover minimizing a canonical pair-state signature. Analyze triples of deletion labels a,b,c. If F_a and F_b disagree, the existing compatible-pair localization says disagreement must appear as support separation, same-slot insertion, or adjacent-slot reversal. Prove that among sufficiently many labels, these local disagreement types cannot all coexist without two labels sharing the same support/order data relative to a third, yielding a compatibility triangle that extends to a fourth label.