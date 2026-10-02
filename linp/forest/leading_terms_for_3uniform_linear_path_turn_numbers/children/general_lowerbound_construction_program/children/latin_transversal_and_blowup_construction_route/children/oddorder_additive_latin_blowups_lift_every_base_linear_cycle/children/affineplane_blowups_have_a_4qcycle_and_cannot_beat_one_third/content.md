# Additive affine-plane blow-ups have a 4q-cycle and cannot beat one third

## Statement

Let A be the affine-plane Steiner triple system AG(2,3). For every odd q, replace each of its nine points by a copy of Z_q and each of its twelve lines by the additive transversal design whose three coordinates sum to zero. The resulting linear 3-graph has 9q vertices and 12q^2 edges, but contains a linear cycle of length 4q and hence a path of length 4q-1. Therefore its normalized density at its first forbidden path length is at most 1/3.

## Body


Choose two distinct lines L_1,L_3 from one parallel class of AG(2,3), and two distinct lines L_2,L_4 from a second parallel class. Lines L_1 and L_3 are disjoint, as are L_2 and L_4, while every line from the first parallel class meets every line from the second in exactly one point. Thus L_1,L_2,L_3,L_4 in cyclic order form a linear four-cycle.

Apply the additive cycle-lift lemma 8faf5f45d76c with s=4. The blow-up therefore contains a linear cycle of length 4q. Deleting one lifted edge yields P_{4q-1}.

The blow-up has 9q vertices and 12q^2 hyperedges, so its edge/vertex density is 4q/3. If ell is one plus its maximum path length, then ell>=4q and
  (|E|/|V|)/ell <= (4q/3)/(4q)=1/3.
Hence the natural additive blow-up of the exact P4 affine-plane extremizer cannot improve the leading lower coefficient.
