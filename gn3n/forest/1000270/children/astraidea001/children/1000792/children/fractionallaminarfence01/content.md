# Laminar fractional optima are impossible in the sharp half-order shell; union-Hamiltonian two-support replacement fails

## Statement

Assume H is a minimum counterexample in the sharp half-order shell n=2lambda+1. Then no optimal fractional path cover can have a laminar family of positive-weight path supports. Indeed every path support carrying positive weight in every optimum has order lambda and every vertex has coverage exactly one. A laminar family of distinct lambda-subsets is pairwise disjoint, and at most two such subsets fit in 2lambda+1 vertices; their union has at most 2lambda vertices and cannot cover every vertex. Consequently the laminarization conjecture f4cf47d4f21d would, if proved, exclude the entire sharp half-order shell. However a two-support replacement that relies on the Hamiltonicity of the union of two distinct lambda-supports cannot operate there, because that union has size greater than lambda and is non-Hamiltonian by maximality of lambda. Thus any optimum-preserving transformation must work among lambda-vertex Hamiltonian supports without using Hamiltonicity of their union, or use a more global transformation.

## Body

# Proof

Work in the sharp half-order shell

n=2lambda+1.

By 9cdd9c6216a7, every optimal primal fractional path cover has two properties:

1. every path support carrying positive weight has exactly lambda vertices;
2. every ambient vertex has total fractional coverage exactly one.

Suppose the family of path supports carrying positive weight were laminar.

All such supports have the same cardinality lambda. Two distinct equal-cardinality sets in a laminar family cannot contain one another. Therefore any two distinct supports carrying positive weight must be disjoint.

But three pairwise disjoint lambda-subsets would require 3lambda vertices, which is greater than 2lambda+1 for lambda>=2. Hence the laminar family contains at most two distinct supports carrying positive weight.

The union of at most two lambda-subsets has at most 2lambda vertices. Since H has 2lambda+1 vertices, at least one vertex lies in no path support carrying positive weight. This contradicts property 2, which requires coverage exactly one at every vertex.

Thus no optimal fractional path cover in a hypothetical minimum counterexample in the sharp half-order shell has a laminar positive-weight path-support family.

It follows immediately that the laminarization assertion in f4cf47d4f21d would rule out the sharp half-order shell if established.

There is also a structural fence on one proposed proof mechanism. Let A,B be two distinct path supports carrying positive weight. Both have order lambda, so

|A union B| > lambda.

Since lambda is the maximum order of a tight path in H, H[A union B] cannot be Hamiltonian. Therefore no two-support transformation that requires replacing A,B by a Hamiltonian path on their union can operate in this shell.

Thus the missing theorem cannot be supplied by union-Hamiltonicity. Any optimum-preserving transformation must instead work among lambda-vertex Hamiltonian supports without requiring their union to be Hamiltonian, or use several supports or another nonlocal transformation.