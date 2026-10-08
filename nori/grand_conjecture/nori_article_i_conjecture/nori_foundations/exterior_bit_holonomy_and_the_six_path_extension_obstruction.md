# Exterior-bit holonomy and the six-path extension obstruction

Let \(S=\{a,b,c,d,e,f\}\subsetneq V\), and suppose \(g\in V\setminus S\). Consider attempting to reuse the six-geodesic forcing certificate of the dimension-six theorem inside an \(S\)-coordinate block of \(Q_V\), with the \(g\)-coordinate untraversed throughout the four consecutive length-three windows associated with each of the six orders. Each window in one such geodesic has the same fixed \(g\)-bit \(z_i\), determined by the starting vertex and by whether \(g\) occurs before or after the entire \(S\)-block.

**Lemma (exterior-bit parity obstruction).** There is no choice of bits \(z_1,z_2,z_4\in\mathbb F_2\) for the first, second, and fourth rows of the dimension-six forcing table that simultaneously preserves all three face identifications used in that proof:
(i) row 2's first \(dcb\)-window is the antipodal reversal of row 1's second \(bcd\)-window;
(ii) row 4's first \(dcb\)-window is likewise the antipodal reversal of row 1's second \(bcd\)-window;
(iii) row 4's last \(fea\)-window is the antipodal reversal of row 2's last \(aef\)-window.

**Proof.** To be antipodal reversals in the ambient cube, the fixed exterior \(g\)-bits of two compared faces must be complements. Relation (i) forces \(z_2=1\oplus z_1\), relation (ii) forces \(z_4=1\oplus z_1\), and relation (iii) forces \(z_4=1\oplus z_2=z_1\). Thus \(z_1=1\oplus z_1\), impossible. \(\square\)

**General parity principle.** Build a graph whose vertices are windows or blocks with a fixed value of a chosen outside coordinate \(g\); mark an identification edge 0 when the two windows are required to be the same ordered face, and mark it 1 when the two windows are required to be antipodal reversals. Existence of consistent \(g\)-bit assignments is equivalent to the parity label being a coboundary: every cycle must contain an even number of edges marked 1. The equivalence follows by propagating one chosen root bit along edges; consistency on cycles is necessary and sufficient. In the six-path forcing gadget, rows 1,2,4 form a triangle with three marked-1 edges, giving odd holonomy.

**Precise extension obligation.** A dimension-raising use of this six-path gadget must (a) traverse at least one additional coordinate between selected comparison windows in some path, so the exterior bit changes within that path, or (b) replace at least one of the three antipodal comparisons by another valid forcing relation. Simply appending or prepending all additional coordinates to contiguous six-coordinate blocks cannot preserve the proof's face identifications. This is a limitation of this particular forcing certificate; it does not assert any obstruction to the grand conjecture for \(n\ge7\).
