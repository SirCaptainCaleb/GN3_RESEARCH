# Spare-color reachability inside a normalized rainbow path

Analyze the matching structure of a fixed rainbow Hamilton path in a tournament system. The goal is to move the unused mediator color without changing the vertex order or the already-normalized parity status word.

Let P=(v_1,...,v_m) be a fixed directed Hamilton path on a vertex set U in a system of m tournaments {T_c:c in C}, |C|=m. Let E(P)={e_1,...,e_{m-1}} be its consecutive directed edges. Suppose a rainbow assignment M matches every path edge e_i to a distinct color c with e_i directed forward in T_c, leaving one spare color s.

Form the bipartite incidence graph G with left part C and right part E(P), where c~e iff T_c directs e forward. The rainbow assignment M is a matching saturating E(P), with unique unmatched color s.

Orient unmatched incidence edges from colors to path edges and matching edges from path edges to colors. Let R be the set of colors reachable from s and F the set of path edges reachable from s.

Then:

1. |R|=|F|+1. Every reached path edge has exactly its matched color reached, while s is the unique reached unmatched color.

2. Every c in R can be made the unique spare color by an alternating-path recoloring. The vertex order P and every path status remain unchanged.

3. If R is not all of C, there is no incidence edge from R to E(P)-F. Otherwise that edge would continue the alternating reachability. Hence every color c in R directs every edge e in E(P)-F backward.

Thus a normalized rainbow block has an exact dichotomy:

  FLEXIBILITY: many colors lie in R and can be moved to the junction/spare position without changing the block order;

  POLARITY: if reachability stops early, the entire reachable color set R unanimously reverses every path edge outside F.

This is a Dulmage-Mendelsohn/Hall-type structural decomposition intrinsic to the fixed rainbow path. It is stronger than merely having many possible rainbow paths because it preserves the vertex order and the already-correct parity status word.

The next target is positional: understand the shape of F along the path. If F is an interval prefix/suffix, then the stopped-reachability branch already produces a one-change-type cut. If F is highly disconnected, the alternating components themselves may supply independent recoloring controls or a natural Tucker label.
