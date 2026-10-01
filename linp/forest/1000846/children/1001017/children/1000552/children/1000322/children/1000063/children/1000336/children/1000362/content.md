# Maximum-rank nonspecial edges have a three-color blocker system with terminal-pair control on clean replacements

## Statement

Let P=(g_1,...,g_{L-1},e) be globally longest with nonspecial e={x,y,z} entered through x, and W=V(P) minus e. The double blockers through x,y,z form three pairwise edge-disjoint matchings on W. At terminal vertices y,z every other incident edge is blocking on W. At entrance x, clean replacements may occur; every such clean edge has rank L, and if it is special then every alternate-entrance longest witness for it meets the fixed terminal pair {y,z}.

## Body

For each v in {x,y,z}, linearity makes the blocker pairs f minus {v} pairwise disjoint, hence a matching M_v. The same blocker pair cannot appear in two colors, since the corresponding hyperedges would share two vertices. Thus M_x,M_y,M_z are pairwise edge-disjoint.

For v=y,z, an edge through v avoiding W would meet the longest path only at v and could be appended after e, impossible. Hence all such terminal edges are single- or double-blocking. Clean edges can occur only through entrance x. The clean entrance replacement lemma gives rank L for each such edge f, and if f is nonspecial its unique entrance is x.

Now suppose a clean f={x,a,b} is special and R is an L-edge path ending in f through an entrance other than x. The old edge e cannot occur earlier in R: if adjacent to f the entrance would be x, and if nonadjacent it would intersect f nonconsecutively at x. Orient R with last vertex x. If R minus {f} avoided both y and z, appending e at x would create an (L+1)-edge linear path, contradicting global maximality. Therefore every alternate-entrance longest witness for a special clean replacement meets y or z. Thus the only escape from the three-color blocker system is itself controlled by the fixed terminal pair.
