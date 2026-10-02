# A loose path refutes automatic production of a genuine endpoint lens

## Statement

Two maximum endpoint paths, one containing the other's last vertex, need not contain any genuine clean elementary lens. This remains false for arbitrarily long paths. The two-common-vertices conclusion of b35b0fd4e4cd is not refuted.

## Body

Fix t>=1. Let H consist exactly of a loose path g_1,...,g_{2t+1}, where consecutive edges meet in one vertex, all these joints are distinct, and nonconsecutive edges are disjoint. Choose x private in g_{2t+1} and y private in g_{t+1}. Then Q=(g_1,...,g_{2t+1}) is a maximum path with last vertex x, of length 2t+1. A path ending at y must have last edge g_{t+1}, because it is the only edge containing y. The intersection graph of H is the ordinary path on g_1,...,g_{2t+1}, so an edge sequence ending at g_{t+1} can approach from only one side and has at most t+1 edges. Thus phi(y)=t+1, and P=(g_1,...,g_{t+1}) is a maximum path with last vertex y. In particular y belongs to V(Q) and y!=x, exactly as required by b35b0fd4e4cd.

Nevertheless P is an initial edge segment of Q. The incidence graph of H (with a node for each vertex and each hyperedge) is a tree. Two distinct internally disjoint routes between distinct boundary vertices would give a cycle in that tree. Hence H contains no genuine lens: there cannot be two distinct internally vertex-disjoint path sides with the same boundary vertices. Suppressing the common edge segment of P and Q leaves no pair of sides ending at y. This proves the counterexample.

The smallest instance is g_1={a,b,c}, g_2={c,d,e}, g_3={e,f,g}, with x=g and y=d. Here phi(x)=3, phi(y)=2, Q=(g_1,g_2,g_3), P=(g_1,g_2).

The exact failed step in the existing proof is the asserted existence of a next common vertex after suppressing common edge segments that bounds two genuine sides. Maximum endpoint paths may share only common segments and never diverge and rejoin. If the word lens is instead allowed to include coincident sides, the existence claim becomes weaker, but its use in 50edfd4bc99c and no-piercing arguments for distinct lens sides is then unjustified. The robust consequence retained for source-rail work is only that a source hit forces at least two common vertices (5854d853a44b and cddeebb1b0b2). A genuine lens and the legality of both replacements must be established separately. This example does not satisfy or refute the paid four-edge target; it fences one proposed proof tool.