# Every exterior vertex of a Hamiltonian four-set lies in a mixed Hamiltonian four- or five-support

**Summary:** Every exterior vertex of a Hamiltonian four-set lies in a mixed Hamiltonian four- or five-support.

## Statement

Let H be a boundary tournament, let X be a Hamiltonian four-vertex set, and let y lie outside X. Then either X union {y} is Hamiltonian, or at least three distinct vertices x in X satisfy that (X-{x}) union {y} is Hamiltonian. In particular there is always a Hamiltonian induced set of order four or five containing y and at least three vertices of X. If H is a minimum counterexample and the support is proper, its complement is non-Hamiltonian with path-cover number two.

## Body

Put F=X union {y}, a five-set. If F is Hamiltonian, take F itself. Otherwise the five-vertex small-set theorem in smallset01 says that a non-Hamiltonian five-set has at most one non-Hamiltonian four-subset, so at least four of the five sets F-{v} are Hamiltonian. One of those five four-subsets is F-{y}=X, which is already Hamiltonian. Hence at least three of the remaining four subsets F-{x}=(X-{x}) union {y}, x in X, are Hamiltonian. In a minimum counterexample any proper Hamiltonian support has complement of path-cover number at most two, and that complement cannot be Hamiltonian because the two Hamilton paths would cover H. Hence the complement is non-Hamiltonian with path-cover number two.

## Metadata

- ID: ham4_exterior_mixed_support01
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
- Toolkit status: Limbo
