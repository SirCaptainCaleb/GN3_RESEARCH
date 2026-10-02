# The one-backward Astra-010 residue produces an inseparable pair in an edge-orderable tournament

## Statement

Assume the normalized Astra-010 witness has exactly one backward comparison alpha between incident ordinary edges ab and bc. Reverse alpha, obtaining G. Then G is edge-orderable with respect to the chosen total edge order and has a spanning two-cover. Every spanning two-cover of G contains the newly tight ordered triple (a,b,c); in particular a and c lie in the same component of every two-cover of G. Thus the b=1 obstruction to Astra idea 010 yields a counterexample to prescribed-vertex separation inside the edge-orderable subclass. Consequently Astra idea 005 restricted to edge-orderable boundary tournaments would eliminate the entire one-backward branch of Astra idea 010.

## Body

With one backward comparison, reversing alpha makes every comparison agree with the chosen total edge order, so G is edge-orderable. By astra010criticalarcs, G has path-cover number at most two. Since H itself has no two-cover, every two-cover of G must use the comparison changed at alpha; otherwise all of its consecutive triples would also be tight in H. Hence every two-cover contains the consecutive vertex triple (a,b,c), so a and c are always on the same component. They are therefore inseparable by two-covers in G. The final implication is immediate from the statement of Astra idea 005.