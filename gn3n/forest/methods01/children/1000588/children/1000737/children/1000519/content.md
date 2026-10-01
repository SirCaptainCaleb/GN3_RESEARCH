# Counterexample to Norine gives a rook labeling

## Statement

If an antipodal red--blue coloring of Q_n has no monochromatic antipodal path, then after enlarging dimension if necessary it yields an antipodally symmetric rook labeling q:V(Q_K)->Omega_K: antipodes swap the two label coordinates, and adjacent cube vertices agree in at least one coordinate.

## Body


Source: Wu--Yang 2026, Lemma 2.2 and Theorem 2.3, https://arxiv.org/abs/2607.19276.

Let the red spanning subgraph have components C_1,...,C_r, and let p(x) be the index of the red component containing x. Define
  q_0(x)=(p(x),p(Ax)).
There is no monochromatic antipodal path, so p(x) != p(Ax): equality would itself give a red path from x to Ax. Also
  q_0(Ax)=(p(Ax),p(x)),
so antipodality swaps the coordinates.

Now consider an edge xy of Q_n. If xy is red then p(x)=p(y), so q_0(x),q_0(y) agree in their first coordinate. If xy is blue, its antipodal edge Ax Ay is red, so p(Ax)=p(Ay), and the two labels agree in their second coordinate. Hence every adjacent pair behaves like two nonattacking/attacking rook positions sharing a row or a column: this is the rook condition.

If the number r of red components exceeds n, choose K>=max{n,r,2}, inject the component labels into [K], identify Q_K=Q_n x Q_{K-n}, and make the label independent of the extra coordinates. Old-coordinate edges retain the rook property and new-coordinate edges have equal labels. Thus a counterexample gives a rook labeling Q_K->Omega_K.

Wu--Yang then prove the diagonal rook theorem: no such rook labeling Q_K->Omega_K exists. That second step is the technically heavy chain-level obstruction summarized in the parent node.

LINP translation. The clean reusable pattern is: label each state x by (component containing x, component containing its involutive mate). If every allowed local transition preserves one of the two component coordinates, while the involution swaps them, then a global antipodal obstruction becomes available.
 