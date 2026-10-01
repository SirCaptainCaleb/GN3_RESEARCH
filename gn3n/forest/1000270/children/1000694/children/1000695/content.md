# Deletion-cover consistency cocycle

## Statement

For each vertex x choose a two-path cover of H-x and regard the unordered pair of path endpoint-pairs as local boundary data. Conjecture that in every minimum counterexample these local data cannot be made globally consistent around all vertex deletions: along some cycle of deletions there is a forced nontrivial endpoint-transport defect. Prove conversely that any globally consistent choice of deletion covers glues to a spanning two-cover of H. This turns the grand theorem into showing that the boundary-tournament relations kill the only possible cocycle obstruction.

## Body

Why it might matter globally:
It replaces repeated local surgery by a global compatibility object. If the gluing theorem is right, every existing deletion-cover lemma becomes information about one common obstruction class, and proving that class trivial would close the theorem at arbitrary order.

Plausible first attack:
Define the weakest transport datum preserved when passing between covers of H-x and H-y on H-{x,y}. Prove a two-deletion compatibility lemma: if the induced transport between x and y is trivial in both directions, then the two local covers admit a common refinement on H-{x,y}. Then test whether transport around a triple x,y,z must compose trivially by the boundary-tournament axioms.