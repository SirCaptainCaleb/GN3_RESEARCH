# Two same-side extension vertices

Suppose \(x,y\) can occur only at the same endpoint side of the relevant augmented supports, and let
\[
R\mid S
\]
be a two-cover of \(H-\{x,y\}\). Form a bipartite graph with left class \(\{x,y\}\) and right class \(\{R,S\}\), joining a label to a path if it can be attached at the prescribed endpoint.

If there is a perfect matching, attach \(x\) and \(y\) to different paths and obtain a two-cover of \(H\). If no perfect matching exists, Hall's theorem leaves two possibilities:
- one of \(R,S\) accepts neither label;
- one of \(x,y\) can be attached to neither \(R\) nor \(S\).

In the first case, the two failed attachments give reverse tight triples through one common end edge. In the second, deleting the blocked label yields two deletion covers that differ by a one-vertex transfer.

**Lemma 6.** Two reverse triples through the same displayed end edge yield two Hamiltonian five-sets with a common four-set, unless an earlier two-cover or Hamiltonian four-set occurs.

**Proof.** For each reverse triple, form a graph on exterior labels by joining two labels when their simultaneous extension fails. Each failure graph is triangle-free: three pairwise failures, after boundary reversal of the three non-tight insertion triples, give a Hamiltonian five-vertex extension. If no exterior pair succeeds for both reverse triples, the edges of \(K_6\) can be colored according to which failure graph contains them, with no monochromatic triangle. This contradicts \(R(3,3)=6\). Hence some pair succeeds for both reverse triples, giving the required two five-sets. \(\square\)

Let the two five-sets be \(K\cup\{p\}\) and \(K\cup\{q\}\), where \(|K|=4\). Their six-vertex union has three relevant forms:
- it is Hamiltonian;
- two Hamiltonian vertex deletions are adjacent, giving overlapping Hamiltonian four- and five-sets;
- the Hamiltonian deletion pairs form a matching, fixing the three pairwise insertion relations on the six vertices.

Each form is a bounded common-core configuration with a two-coverable complement inherited from the construction.
