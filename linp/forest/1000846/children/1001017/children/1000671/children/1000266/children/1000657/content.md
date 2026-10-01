# Terminal adjacency forces rank rise or a blocker

## Statement

Let e,f be distinct nonspecial edges of a linear 3-graph, sharing a vertex v that is terminal for e and also terminal for f. Let t=phi(e), and choose a t-edge path P ending in e with physical terminal v. If f meets P only in v, then appending f gives a (t+1)-edge linear path ending in f through the entrance label v; hence phi(f)>=t+1. Consequently, if phi(f)<=phi(e), every longest path witnessing v as a terminal of e must meet f in a second vertex. In particular, on any cycle of the terminal-pair graph, every edge of minimum rank blocks both neighboring terminal witnesses in the corresponding incoming directions.

## Body

Proof. Let P=(e_1,...,e_t) with e_t=e and terminal vertex v. Since v is terminal for e, v lies in e_t and no earlier edge of P. The edge f also contains v. If f meets no other edge or vertex of P, then (e_1,...,e_t,f) is a linear path: consecutive e_t,f meet at v, and by hypothesis f is disjoint from all earlier path edges. Thus phi(f)>=t+1. Moreover this path enters f through v. Therefore whenever phi(f)<=t, such an extension is impossible and f must meet P in some second vertex. The final cycle statement follows because adjacent edges in the terminal-pair graph share a vertex that is terminal in both hyperedges; if f is a minimum-rank cycle edge and e is either cycle neighbor, then phi(f)<=phi(e), so f blocks every longest terminal-v witness for e.