# Four incompatible deletion covers without a uniform triple have only two support patterns

## Statement

Let F_1,F_2,F_3,F_4 be deletion covers associated with four distinct labels in a boundary tournament H with at least one vertex outside those labels. Assume the four covers are pairwise incompatible and contain no three covers whose three pairwise incompatibilities have one broad type. Let B be the graph on {1,2,3,4} whose edges are the support-compatible pairs. Then, up to relabeling, B is either a four-vertex path P_4 or two disjoint edges 2K_2.

## Body

# Proof

Color a pair blue when it is support-compatible (hence, under the pairwise-incompatibility hypothesis, support-compatible but order-incompatible), and red when it is support-incompatible. The hypothesis says there is no monochromatic triangle.

Let B be the blue graph. Since a blue triangle would already be a forbidden uniform triple, B is triangle-free. By compatsupportc5close24, every cycle in B spans a clique. Since B is triangle-free, B has no cycle at all. Thus B is a forest.

The red graph is the complement of B. Since there is no red triangle, the independence number of B is at most two.

It remains to classify forests on four vertices with independence number at most two. A forest with at most two edges is either a matching, a path plus an isolated vertex, or has at least two isolated/leaf choices; among these, only the perfect matching 2K_2 has independence number two. A forest with three edges is a tree. The star K_{1,3} has three independent leaves, so it is excluded. The only remaining tree is P_4, whose independence number is two.

Therefore B is, up to relabeling, either P_4 or 2K_2.

Both forms are genuine abstract support-pattern obstructions: support compatibility alone does not collapse either pattern to a uniform triple. Any further elimination must use the order information on the blue pairs or the support-switch information on the red pairs.
