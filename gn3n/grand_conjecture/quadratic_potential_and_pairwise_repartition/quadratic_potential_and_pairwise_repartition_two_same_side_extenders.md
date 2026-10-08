# Two same-side extenders

Let \(x,y\) be two labels that can occur only at the same side of the relevant core paths, and let \(R\mid S\) be a two-cover of \(H-\{x,y\}\). Form a bipartite graph with left class \(\{x,y\}\) and right class \(\{R,S\}\), joining a label to a path when adjoining the label at the prescribed end gives a Hamiltonian path.

A perfect matching gives a two-cover of \(H\). If no perfect matching exists, Hall's theorem gives one of two possibilities:
1. one of \(R,S\) is adjacent to neither \(x\) nor \(y\);
2. one of \(x,y\) is adjacent to neither \(R\) nor \(S\).

In the first case, the two failed end insertions give two reverse tight triples through one displayed end edge. In the second, deleting the blocked label gives two deletion covers that differ by transferring the other label.

Two reverse triples through one end edge force a bounded common-core configuration. For each reverse triple, record pairs of exterior labels whose simultaneous extension fails. Each failure graph is triangle-free: three pairwise failures force, by applying boundary reversal to the three corresponding insertion triples, a Hamiltonian order on one of the three five-vertex extensions. On six exterior labels, if no pair succeeds for both reverse triples, the edges of \(K_6\) are covered by two triangle-free graphs. Coloring each edge by one graph containing it gives a two-coloring of \(K_6\) without a monochromatic triangle, contradicting \(R(3,3)=6\). Hence two labels simultaneously extend both reverse triples, producing two Hamiltonian five-vertex supports with a common four-vertex core.

Their six-vertex union has three relevant possibilities: it is Hamiltonian; two Hamiltonian vertex deletions are adjacent; or the Hamiltonian vertex deletions form a matching. These give, respectively, a Hamiltonian six-vertex support, overlapping Hamiltonian four- and five-vertex supports, or a fixed matching-block configuration. Each alternative preserves the common four-vertex core.
