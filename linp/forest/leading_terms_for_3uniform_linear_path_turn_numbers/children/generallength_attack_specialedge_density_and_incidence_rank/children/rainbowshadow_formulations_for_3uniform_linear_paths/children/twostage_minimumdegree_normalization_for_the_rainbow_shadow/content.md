# Two-stage minimum-degree normalization for the rainbow shadow

## Statement

Let H be a nonempty linear 3-graph with density rho=|E(H)|/|V(H)|. There is a linear subhypergraph H0 with delta(H0)>=rho0:=|E(H0)|/|V(H0)|>=rho. From H0 one can choose an A/B shadow graph J and then a graph subgraph J0 such that J0 is properly edge-colored, every rainbow path in J0 lifts to a linear path in H0, and delta(J0)>=3rho0/4>=3rho/4.

## Body

Proof. First take H0 from the original-hypergraph density-core lemma, so delta(H0)>=rho0>=rho. Color every shadow pair yz by the unique third vertex x with xyz in E(H0). Independently put each vertex into A or B with probability 1/2, and let J be the graph on A consisting of shadow pairs whose color lies in B. Each hyperedge contributes exactly one edge to J exactly when it has two vertices in A and one in B, which occurs with probability 3/8. Thus E|E(J)|=3|E(H0)|/8 and E|A|=|V(H0)|/2. Hence E[|E(J)|-(3rho0/4)|A|]=0, so some nonempty choice has |E(J)|/|A|>=3rho0/4. Now choose a nonempty subgraph J0 maximizing |E|/|V|. The usual deletion argument gives delta(J0)>=|E(J0)|/|V(J0)|>=|E(J)|/|A|>=3rho0/4. Proper edge-coloring and absence of a rainbow P_ell are inherited by subgraphs. By the certified shadow-rainbow lifting lemma, every rainbow graph path in J0 lifts to a linear hypergraph path in H0.