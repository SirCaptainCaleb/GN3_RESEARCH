# Sharp-shell longest-path supports: four-good disturbance or linear support expansion

## Statement

Let H be a minimum counterexample in the sharp half-order shell |V(H)|=2lambda+1, and let G be the Hamiltonian-support odd graph on Hamiltonian lambda-subsets. Then at least one of the following holds. (I) Some nonisolated support S has deg_G(S)>=4. Writing R=V(H)-S, the complement R has at least four Hamiltonian vertex deletions, so the Astra-004 many-good theorem applies: for arbitrary exact covers of the two endpoint deletions of a Hamilton order on S, some good label t in R forces either a direct ordinary mixed edge between R-{t} and the surviving vertices of S, or explicit relative-order disagreement. (II) Every nonisolated support has degree at most three, in which case G has at least ceil(2|V(H)|/3) nonisolated vertices. Thus absence of a four-good complement forces a linear-size family of distinct globally longest tight-path supports.

## Body

# Proof

If some nonisolated S has degree at least four, astra004odddegree identifies deg_G(S) with the number of Hamiltonian vertex deletions of R=V(H)-S. Hence |D(R)|>=4. Choose any Hamilton order A on S. Since A is globally longest in the sharp shell, astra004manygoodmixed applies to A and R and gives the direct mixed-edge / order-disagreement conclusion. This is (I).

Otherwise every nonisolated vertex of G has degree at most three. The low-degree expansion conclusion of astra004odddegree gives at least ceil(2n/3) nonisolated vertices, where n=|V(H)|. Every vertex of G is by definition a Hamiltonian lambda-support, hence a globally longest tight-path support. This is (II). ∎