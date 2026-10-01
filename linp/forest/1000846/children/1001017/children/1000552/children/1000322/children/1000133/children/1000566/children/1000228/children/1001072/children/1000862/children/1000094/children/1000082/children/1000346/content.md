# Every pair of zero-slack triples has many same-color double jumps

## Statement

In the zero-slack |D|=k critical-core model, for every two distinct forest triples A,B, all but at most 12 threshold colors d admit two distinct d-colored matching edges e_A,e_B such that e_A leaves A away from B and e_B leaves B away from A. The lifted sequence A,h_A,h_B,B is then a four-edge linear path. Thus every pair of forest triples has at least k-12 legal same-color two-edge connector jumps.

## Body

Work in the zero-slack critical-core model 13500728c22f. Thus X is partitioned into disjoint forest triples F_1,...,F_c, where c=2k/3, and for each color d in D the d-colored graph on X is a perfect matching M_d.

Fix a color d and a forest triple A. Since |A|=3 and M_d is a perfect matching, the restriction of M_d to the three vertices of A has one of two forms:
(i) one internal matching edge in A and one matching edge leaving A; or
(ii) no internal edge and three matching edges leaving A.

For another triple B, call B d-bad from A if every d-matching edge leaving A goes to B. There is at most one such B.

If B is not d-bad from A, choose a d-matching edge e_A with one endpoint in A and the other endpoint outside A∪B. Likewise, if A is not d-bad from B, choose a d-matching edge e_B with one endpoint in B and the other endpoint outside A∪B. The two matching edges are distinct and disjoint in X. Let h_A,h_B be their lifted hyperedges, each obtained by adjoining the common color vertex d.

Then
  A, h_A, h_B, B
is a four-edge linear hypergraph path: A meets h_A in one X-vertex, h_A meets h_B only in d, h_B meets B in one X-vertex, while the choice of the two matching edges prevents the nonconsecutive intersections A∩h_B and B∩h_A; the forest triples A,B are disjoint.

Thus a same-color double jump from A to B fails only if B is d-bad from A or A is d-bad from B.

Now fix A,B and count colors for which B is d-bad from A. If M_d has one internal edge on A, that internal graph edge is one of the three pairs inside A. Since the colored graph is simple, at most three colors can occur this way. If M_d has no internal edge on A and all three leaving edges go to B, the color d uses three distinct graph edges between the 3-set A and the 3-set B. There are only nine such graph edges in total, and different colors are edge-disjoint, so this can happen for at most three colors. Hence at most six colors satisfy that B is d-bad from A. Symmetrically at most six colors satisfy that A is d-bad from B.

Therefore for every two distinct forest triples A,B, at least
  k-12
colors d admit a same-color double jump, and hence a four-edge linear path segment
  A,h_A,h_B,B.
