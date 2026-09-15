# S9023 — Fixed-Trimer Extension and Triangle-Free Bad Graph

## Theorem A — three exterior vertices force a good pair

Let P be a three-vertex support carrying a tight trimer in a Strong Level-(1) boundary tournament, and let x,y,z be three distinct vertices outside P. Then at least one of the three five-sets P∪{x,y}, P∪{x,z}, P∪{y,z} supports a tight five-vertex path.

### Proof

Relabel the fixed tight trimer as P={0,1,2} with (0,1,2) tight, and the three exterior vertices as 3,4,5. Encode every complete-reversal pair {(a,b,c),(c,b,a)} of ordered triples of distinct vertices by one Boolean variable. There are 6P3/2=60 variables. For a fully deterministic numbering, take the lexicographically smaller ordered triple in each reversal pair as its canonical representative, sort the 60 canonical representatives lexicographically, and number them x_1,...,x_60 in that order. The literal for a turn t is x_i when t is the canonical representative of pair i and ¬x_i when its reverse is canonical. By boundary antisymmetry, every Boolean assignment is exactly one Strong Level-(1) turn assignment on these six vertices. Add the unit clause asserting (0,1,2) tight.

Assume for contradiction that all three five-sets P∪{3,4}, P∪{3,5}, P∪{4,5} are non-Hamiltonian. For each of these supports and each of its 5!=120 vertex orders q=(q_1,...,q_5), add the clause saying that not all three consecutive turns q_1q_2q_3, q_2q_3q_4, q_3q_4q_5 are tight. Replacing each turn by its Boolean literal gives one three-literal clause. Thus the CNF has exactly 60 variables and 3·120+1=361 clauses.

This CNF is UNSAT by the following completely deterministic exhaustive DPLL procedure. Repeatedly perform unit propagation until no unit clause remains; when several unit clauses are present, process them in increasing variable index. If an empty clause appears, close the branch. If all clauses are satisfied, report SAT. Otherwise choose the smallest-index unassigned variable that occurs in a remaining clause and branch False before True. With the lexicographic numbering above, the exhaustive search visits 1,397 DPLL nodes, reaches maximum branch depth 22, and closes every branch by contradiction. These figures were independently regenerated from the displayed encoding and rule.

Therefore no Strong Level-(1) assignment can make all three P-plus-pair supports non-Hamiltonian. At least one of P∪{3,4}, P∪{3,5}, P∪{4,5} supports a tight P5, which is the claim.

## Theorem B — bad extension pairs form a triangle-free graph

Let P be a tight trimer in a Strong Level-(1) boundary tournament and let X be any set of m>=3 vertices disjoint from P. Form a graph G_bad on X by joining x,y when the five-set V(P) union {x,y} does not support a tight P5. Then G_bad is triangle-free. Consequently |E(G_bad)|<=floor(m^2/4), so at least binom(m,2)-floor(m^2/4) pairs {x,y} extend P to a Hamiltonian five-support. Equality in the bad-pair bound forces the Mantel extremal structure: G_bad is a complete bipartite graph with part sizes floor(m/2),ceil(m/2). Equivalently, in the equality case the outside vertices split into two nearly equal classes and every within-class pair extends P to a tight P5.

### Proof

For any three distinct x,y,z in X, Theorem A applied to P,x,y,z says at least one of Pxy,Pxz,Pyz supports a tight P5. Therefore not all three pairs xy,xz,yz can be edges of G_bad, so G_bad is triangle-free. Mantel gives |E(G_bad)|<=floor(m^2/4), with equality exactly for the balanced complete bipartite graph K_{floor(m/2),ceil(m/2)}. The complementary good-pair count is binom(m,2)-|E(G_bad)|. In the equality case every within-part pair is absent from G_bad and hence is a good P5 extension of P.

## Why this is reusable

The package converts five-vertex Hamilton extension around a fixed tight trimer into ordinary graph theory. Failure pairs form a triangle-free graph, so Mantel's theorem and its equality case become immediately available.

## Scope and nonclaims

The finite six-vertex existence theorem is computationally certified. The bad graph records only whether a pair extends the fixed trimer to a Hamilton P5; it does not encode endpoint control.

## Provenance

Rescued from accepted archived results `R146`, `R328`.
