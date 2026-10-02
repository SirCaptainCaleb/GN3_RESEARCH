# Maximum-rank forest gives canonical blocker chords

## Statement

Let T be the terminal-pair graph of the nonspecial edges of a linear 3-graph, weighted by hyperedge rank φ(e). Choose a spanning forest F of T with maximum total rank. Then every nonforest edge f is a minimum-rank edge on its fundamental cycle C_f, and the number of nonforest edges is β(T). Hence each unit of cycle rank has a canonical representative f whose two fundamental-cycle neighbors have rank at least φ(f) and must block longest-path witnesses for those neighbors through the corresponding shared terminal vertices.

## Body

The number of nonforest edges of any spanning forest is |E(T)|-|V(T)|+c(T)=β(T). Let f be a nonforest edge and C_f its fundamental cycle. If some tree edge g on C_f had φ(g)<φ(f), replacing g by f would give a spanning forest with larger total rank, contradicting maximality. Hence f has minimum rank on C_f. Its two cycle neighbors share the two endpoints of the terminal pair of f. For either neighbor e, φ(e)>=φ(f); applying terminal adjacency forces rank rise or a blocker in the direction from a longest witness for e toward f. Since rank rise past φ(e)>=φ(f) is unavailable in that direction, f must have an additional contact with the witness path. Thus the β(T) nonforest chords provide canonical two-sided blocker obligations. No claim about rank-2 chords is made.