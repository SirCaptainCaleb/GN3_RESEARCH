# Every four-side beside a nontrivial path has an endpoint-rooted Hamiltonian four-set

**Summary:** A four-side W beside any path P of order at least two forces a Hamiltonian four-set containing both displayed endpoints of P and two vertices of W; in a minimum counterexample its complement has path-cover number two.

## Statement

Let H be a minimum counterexample and let W|P|Q be a spanning three-cover with |W|=4 and P=(p_1,...,p_m), m>=2. Then there are distinct x,y in W such that {p_1,p_m,x,y} is Hamiltonian. This four-set is proper, and its complement is non-Hamiltonian with path-cover number two.

## Body

Choose any three distinct vertices \(a,b,c\in W\), and consider the five-set
\[
F=\{p_1,p_m,a,b,c\}.
\]
Apply the endpoint-pair Hamiltonicity theorem to the prescribed pair
\[
\{p_1,p_m\}\subset F.
\]
It yields a Hamiltonian four-subset of \(F\) containing both prescribed endpoints. Such a four-subset has the form
\[
U=\{p_1,p_m,x,y\}
\]
for distinct \(x,y\in\{a,b,c\}\subset W\).

Because \(Q\ne\varnothing\), the set \(U\) is a proper subset of \(V(H)\). The minimum-counterexample complement principle therefore gives
\[
\operatorname{pc}(H-U)=2,
\]
and \(H-U\) is non-Hamiltonian.

Thus every four-side beside a nontrivial displayed path already carries a Hamiltonian four-set containing both endpoints of that path. No endpoint-extension test, insertion obstruction, path-length threshold, or gap analysis is required.

## Metadata

- ID: four_side_endpoint_lock_mixed_menu_m5_01
- Kind: toolkit
- Version: 3
- Math version: 3
- Audit: unaudited
- Refutation: unrefuted
