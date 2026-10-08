# Fundamental cycles of the terminal-pair graph

Form a graph \(J\) whose edges are the terminal pairs \(uv\) of the edges
\[
e=\{x,u,v\}
\]
appearing in the families \(G_v\). Give \(uv\) weight \(\phi(e)\). In each component choose a spanning tree of maximum total weight.

## Lemma 9

After deleting \(o(S)\) further incidences, one obtains families \(H_v\subseteq G_v\) satisfying
\[
\sum_v\left(\frac{\phi(v)}8-|H_v|\right)_+=o(S), \tag{36}
\]
such that every \(e\in H_v\) is a nonforest edge, has minimum edge rank on its fundamental cycle, and has the following property: if \(f\) is either neighboring edge on that cycle and \(w\) is their common terminal, then every maximum path with last edge \(f\) and last vertex \(w\) contains a second vertex of \(e\).

#### Proof
A spanning forest contains fewer than \(n_+\) graph edges. Deleting the associated terminal incidences costs \(O(n_+)=o(S)\), proving (36).

Let \(e\) be a remaining nonforest edge. If a tree edge \(f\) on its fundamental cycle had smaller weight, replacing \(f\) by \(e\) would increase the total tree weight. Thus \(e\) has minimum edge rank on the cycle.

Let \(f\) be a cycle-neighbor of \(e\), sharing terminal \(w\). Since
\[
\phi(f)\ge\phi(e),
\]
a maximum path ending in \(f\) at \(w\) cannot meet \(e\) only at \(w\); otherwise appending \(e\) gives a path with last edge \(e\) longer than \(\phi(e)\). ∎

Since an ascending edge can belong to at most the two families indexed by its terminal vertices, (36) contains
\[
\left(\frac1{16}-o(1)\right)S \tag{37}
\]
distinct hyperedges.
