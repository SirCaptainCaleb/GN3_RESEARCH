# The five-side endpoint-core alternative is component-local in arbitrary path covers

## Statement

Let H be a boundary tournament and let F be any spanning path cover containing a component X of order five and a component P=(p_1,...,p_m) of order m>=6. Then either transferring one endpoint of P into X gives a legal pairwise repartition with quadratic-potential change 12-2m, or there exists x in X such that both (X-{x}) union {p_1} and (X-{x}) union {p_m} are Hamiltonian. Thus the conclusion of five_side_endpoint_core_m6_01 does not require the ambient cover to have exactly three components.

## Body

The proof of five_side_endpoint_core_m6_01 only uses the two displayed components X and P. If X+p_1 or X+p_m is Hamiltonian, replace X|P by a Hamilton path on the six-set and the inherited path on the remaining m-1 vertices; every other cover component stays fixed and the potential change is 6^2+(m-1)^2-(5^2+m^2)=12-2m. If neither endpoint extension is Hamiltonian, four-of-six applied separately to X+p_1 and X+p_m gives at least three replacement labels x in X for each endpoint. Two subsets of a five-set of size at least three intersect, yielding a common x. No property of the untouched components is used.