# Repeated arbitrary proper-color lifts have a one-quarter asymptotic ceiling

## Statement

Let G be any finite properly edge-colored simple graph on u vertices with color set S. For r>=1 form H_r from r vertex-disjoint copies of G by adjoining one common hypergraph vertex for each color c in S and replacing every graph edge xy of color c by {x,y,c}. If H_r is P_ell-free for arbitrarily large r, then |E(G)|/u <= ceil(ell/2)/2. Consequently |E(H_r)|/|V(H_r)| <= ell/4+O(1)+o_r(1), so no repeated shared-color lift of this form can improve the one-third leading lower coefficient.

## Body


Define the color-adjacency graph C on the colors used by G: distinct colors a,b are adjacent in C exactly when some vertex of G is incident with one edge of color a and one edge of color b.

First observe that every q-edge simple path c_0,c_1,...,c_q in C yields a 2q-edge linear path in H_r whenever r>=q. For each i=1,...,q choose a vertex v_i of G incident with an edge e_i^- of color c_{i-1} and an edge e_i^+ of color c_i. Realize this two-edge wedge in the i-th copy of G, and list the lifted hyperedges in the order
 e_1^-, e_1^+, e_2^-, e_2^+, ..., e_q^-, e_q^+.
Within a wedge the two lifted triples meet in the private graph vertex v_i. Between successive wedges, e_i^+ and e_{i+1}^- lie in different private copies and have the same color c_i, so they meet exactly in the common color vertex c_i. Because the color path is simple, no color appears except in one wedge or in the two consecutive hyperedges straddling one bridge. Distinct private copies are disjoint. Hence every nonconsecutive pair of lifted hyperedges is disjoint, proving that the displayed sequence is a linear path of length 2q.

Assume now that H_r is P_ell-free for arbitrarily large r. Then C cannot contain a simple path of q edges with 2q>=ell, since choosing r>=q would give P_ell as an initial segment. Therefore every simple path in C has fewer than ell/2 edges.

At any graph vertex v, properness implies that its d_G(v) incident graph edges have pairwise distinct colors. Every pair of those colors is adjacent in C through v, so they span a clique K_{d_G(v)}. Such a clique contains a simple path of d_G(v)-1 edges. Hence
  2(d_G(v)-1) < ell,
which gives
  d_G(v) <= ceil(ell/2).
Averaging,
  |E(G)|/u = (1/(2u)) sum_v d_G(v) <= ceil(ell/2)/2.

Finally H_r has ru+|S| vertices and r|E(G)| hyperedges, so as r tends to infinity its density tends to |E(G)|/u <= ceil(ell/2)/2 = ell/4+O(1). Thus repeated arbitrary shared-color lifts are asymptotically bounded well below the one-third target.

This strictly generalizes the earlier repeated one-factorization fences: no regularity, completeness, equal color-class size, or pairwise color-incidence hypothesis is needed.
