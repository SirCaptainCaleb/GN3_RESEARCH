# A four-side beside a path of order at least six strictly descends or creates an adjacent opposite-end four-window fork

**Summary:** A four-side beside a path of order at least six strictly descends or creates an adjacent opposite-end four-window fork.

## Statement

Let H be a boundary tournament, let X be a Hamiltonian four-vertex set, and let P=(p_1,...,p_m) be a vertex-disjoint tight path of order m>=6. Then either X|P admits a legal two-path repartition of V(X) union V(P) with strictly smaller quadratic contribution than 4^2+m^2, or there are distinct x,y,z in X such that {p_1,p_m,x,y} and {p_1,p_m,x,z} are both Hamiltonian four-sets. Thus the non-descent branch is a positioned adjacent fork of Hamiltonian four-windows sharing the three-core {p_1,p_m,x}; no neutral or generic-order-disagreement outcome is needed. If H is a minimum counterexample, each of the two forked four-sets has non-Hamiltonian path-cover-two complement.

## Body

If X union {p_1} is Hamiltonian, move p_1 from P into X and retain the inherited path (p_2,...,p_m). This changes the pair orders from (4,m) to (5,m-1), with new quadratic contribution minus old equal to 25+(m-1)^2-(16+m^2)=10-2m<0 for m>=6. The same argument applies if X union {p_m} is Hamiltonian. Hence assume both five-sets X union {p_1} and X union {p_m} are non-Hamiltonian. Apply two_bad_five_extensions_adjacent_four01 to the Hamiltonian four-set X and exterior vertices p_1,p_m. It yields distinct x,y,z in X such that {p_1,p_m,x,y} and {p_1,p_m,x,z} are Hamiltonian. They share exactly the three vertices {p_1,p_m,x}. This proves the dichotomy. In a minimum counterexample the forked four-sets are proper; their complements cannot be Hamiltonian, else either one together with its Hamilton path would two-cover H, while minimality gives path-cover number at most two. Therefore each complement is non-Hamiltonian of path-cover number exactly two.

## Metadata

- ID: four_path_long_pair_endpoint_fork01
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
- Toolkit status: Limbo
