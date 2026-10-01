# A compatibility component supplies canonical central path states inside one trapped pairwise-repartition component

## Statement

Let H be a minimum counterexample. Choose one deletion cover F_v of H-v for each label v in a set D, and let G be their compatibility graph. For every connected component K of G, all singleton lifts F_v|{v}, v in V(K), lie in one trapped component of the pairwise-repartition graph on spanning covers with at most three components. Moreover that same component contains, for every v in V(K), the canonical central state with a three- or five-vertex middle path reached from F_v|{v}; in the five-vertex case it also contains the intermediate state with a three-vertex middle path from the first move. Thus each compatibility component yields one trapped pairwise-repartition component carrying a three-vertex central-path state associated with every deletion label in K.

## Body

Fix a connected component K of the compatibility graph G.

By 10e82bd852dc, each compatibility edge vw gives one legal pairwise repartition between the singleton lifts F_v|{v} and F_w|{w}. Concatenating along a path in K shows that all singleton lifts
F_v|{v},  v in V(K),
belong to one common component of the pairwise-repartition graph; call it C_K.

Because H is a counterexample, C_K is trapped: no state in it can have at most two components, since such a state would itself be a spanning two-cover of H.

For each v in V(K), apply centralbridgereach to the singleton lift F_v|{v}. The corresponding canonical central state is reached by two legal pairwise repartitions, so it also belongs to C_K. If its middle path has five vertices, centralbridgereach states that the first move passes through a spanning state with a three-vertex middle path. If its middle path has three vertices, the final canonical state itself supplies the required three-vertex middle path.

Hence C_K contains a three-vertex central-path state associated with every deletion label in K, and also the final canonical central state with a three- or five-vertex middle path associated with each label. ∎
