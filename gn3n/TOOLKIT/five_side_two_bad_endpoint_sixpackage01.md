# Two bad extensions of a Hamiltonian five-set yield a six-set with four positioned good deletions

**Summary:** Two bad extensions of a Hamiltonian five-set yield a six-set with four positioned good deletions.

## Statement

Let H be a boundary tournament, let X be a Hamiltonian five-vertex set, and let e,f be distinct vertices outside X. Suppose X union {e} and X union {f} are non-Hamiltonian. Then there exist distinct x,z_1,z_2 in X such that, for U=(X-{x}) union {e,f}, each of U-{e}, U-{f}, U-{z_1}, and U-{z_2} is Hamiltonian. In particular U has four explicitly positioned Hamiltonian one-vertex deletions: both exterior labels e,f and two labels inherited from X.

## Body

Apply 41a89ea9eacf. It gives x in X such that both (X-{x}) union {e} and (X-{x}) union {f} are Hamiltonian, and at least two distinct vertices z_1,z_2 in X-{x} such that (X-{x,z_i}) union {e,f} is Hamiltonian for i=1,2. Put U=(X-{x}) union {e,f}. Then U-{f}=(X-{x}) union {e} and U-{e}=(X-{x}) union {f} are Hamiltonian, while U-{z_i}=(X-{x,z_i}) union {e,f} is Hamiltonian for i=1,2. The four deletion labels e,f,z_1,z_2 are distinct. No minimum-counterexample, path-cover, or extremality hypothesis is used.

## Metadata

- ID: five_side_two_bad_endpoint_sixpackage01
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
- Toolkit status: Limbo
