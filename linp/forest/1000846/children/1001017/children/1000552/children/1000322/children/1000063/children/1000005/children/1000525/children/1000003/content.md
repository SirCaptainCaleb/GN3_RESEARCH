# Maximum-rank nonspecial edge can have no low-degree opposite endpoint

## Statement

The opposite-end degree conjecture 75e5875cac45 is false. There is a 9-vertex, 8-edge linear 3-graph of global maximum path length L=3 with a globally maximum-rank nonspecial edge e such that, for every longest path ending in e, both last vertices at the opposite end have degree 3>floor(2(L+1)/3)=2.

## Body

Let the edges be E0={0,1,2}, E1={3,4,8}, E2={0,5,7}, E3={2,3,7}, E4={2,5,6}, E5={1,6,7}, E6={1,3,5}, E7={0,3,6}. The system is linear. Its intersection graph on vertices E0,...,E7 is K8 with exactly the four nonedges E0E1,E1E2,E1E4,E1E5 deleted. Hence it has no induced P4: without E1 the graph is complete, while any four-vertex induced subgraph containing E1 has the other three vertices pairwise adjacent and therefore cannot be a P4. It does have induced P3s, for example E0,E7,E1, so the global maximum linear-path length is L=3. The only neighbors of E1 in the intersection graph are E3,E6,E7, and each meets E1 in the same hypergraph vertex 3. Thus every longest path ending in E1 enters E1 through 3, so E1 is nonspecial with phi(E1)=3=L. A longest path ending in E1 has first edge among E0,E2,E4,E5. Every vertex of each of these four triples has hypergraph degree 3. Therefore whichever of its two vertices are the last vertices at the end opposite E1, both have degree 3. Since floor(2(3+1)/3)=2, the proposed opposite-end bound fails for every longest path ending in E1. The global minimum degree is 1, so this does not refute a version imposing the dense-core minimum-degree hypothesis.
