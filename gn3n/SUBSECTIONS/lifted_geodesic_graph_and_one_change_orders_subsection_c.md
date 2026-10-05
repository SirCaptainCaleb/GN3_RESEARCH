# Pole geodesics are spanning orders

## Metadata

- ID: lifted_geodesic_graph_and_one_change_orders_subsection_c
- Parent Section: lifted_geodesic_graph_and_one_change_orders
- Position: 3
- Row version: 4
- Development version: 4
- Composition version: 1
- Composition stale: False

## Cold composition

Every edge changes rank by one, so \(d(s,t)\ge n\). For every permutation \(\pi=(v_1,\ldots,v_n)\) and each \(\sigma\), there is a length-\(n\) path
\[
s,\quad
(\sigma,S_i,v_{i+1},v_{i+2})\quad(0\le i\le n-2),\quad
t.
\]
Conversely, every \(s\)-\(t\) geodesic must increase rank at every step, so it chooses each label exactly once and hence determines a unique permutation and copy index.

Therefore the pole geodesics are in bijection with pairs \((\sigma,\pi)\), and their color words are
\[
\sigma,\quad h(v_1,v_2,v_3),\ldots,
h(v_{n-2},v_{n-1},v_n),\quad1-\sigma.
\]

It follows immediately that \(H\) has a spanning order whose consecutive-triple statuses change at most once if and only if \(\Gamma_n\) has a pole geodesic with at most one edge-color change. Deleting the two artificial endpoint colors gives one direction; choosing \(\sigma\) to match the first run gives the other.

## Development

Every edge changes rank by one, so \(d(s,t)\ge n\). For every permutation \(\pi=(v_1,\ldots,v_n)\) and each \(\sigma\), there is a length-\(n\) path
\[
s,\quad
(\sigma,S_i,v_{i+1},v_{i+2})\quad(0\le i\le n-2),\quad
t.
\]
Conversely, every \(s\)-\(t\) geodesic must increase rank at every step, so it chooses each label exactly once and hence determines a unique permutation and copy index.

Therefore the pole geodesics are in bijection with pairs \((\sigma,\pi)\), and their color words are
\[
\sigma,\quad h(v_1,v_2,v_3),\ldots,
h(v_{n-2},v_{n-1},v_n),\quad1-\sigma.
\]

It follows immediately that \(H\) has a spanning order whose consecutive-triple statuses change at most once if and only if \(\Gamma_n\) has a pole geodesic with at most one edge-color change. Deleting the two artificial endpoint colors gives one direction; choosing \(\sigma\) to match the first run gives the other.
