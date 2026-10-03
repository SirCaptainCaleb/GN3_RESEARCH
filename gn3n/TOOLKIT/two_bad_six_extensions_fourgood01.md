# Two bad six-extensions of any five-set force a four-positioned-deletion six-set

**Summary:** Two bad six-extensions of any five-set force a four-positioned-deletion six-set.

## Statement

Let H be a boundary tournament, let X be any five-vertex set, and let e,f be distinct vertices outside X. Suppose X union {e} and X union {f} are both non-Hamiltonian. Then there exist distinct x,z_1,z_2 in X such that, for U=(X-{x}) union {e,f}, each of U-{e}, U-{f}, U-{z_1}, and U-{z_2} is Hamiltonian. Thus no Hamiltonicity assumption on X is required.

## Body

For g in {e,f}, let I_g={x in X : (X-{x}) union {g} is Hamiltonian}. Apply the four-of-six theorem in smallset01 to X union {g}.

If X is Hamiltonian, deleting g is one Hamiltonian deletion of X union {g}; since at least four deletions are Hamiltonian, |I_g|>=3. Hence |I_e intersect I_f|>=3+3-5=1.

If X is non-Hamiltonian, deleting g is not a Hamiltonian deletion. Therefore at least four of the five deletion labels in X are good, so |I_g|>=4. Hence |I_e intersect I_f|>=4+4-5=3.

In either case choose x in I_e intersect I_f. Put U=(X-{x}) union {e,f}. Then U-{f}=(X-{x}) union {e} and U-{e}=(X-{x}) union {f} are Hamiltonian. Apply four-of-six again to U. At least four one-vertex deletions of U are Hamiltonian; e and f already account for two, so at least two distinct vertices z_1,z_2 in X-{x} are also Hamiltonian deletion labels. Therefore U-{z_1} and U-{z_2} are Hamiltonian, as claimed.

## Metadata

- ID: two_bad_six_extensions_fourgood01
- Kind: toolkit
- Version: 2
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
- Toolkit status: Promoted
