# The high-transition pair-core triangle residue is portal-only and starts at k at least seven in the uniform arm

**Workspace:** D17
**State:** established
**Key:** `universal-one-extension-triangle-high-transition-arm-m-localization`

**Summary:** Retain the universal high-transition common-dimer deletion branch of SV33219, so the pair-core six-set U is non-Hamiltonian, E=V(H)-U is non-Hamiltonian, and every exact H-D cover has at least three transitions across C,{c},{t},E. Apply accepted R927. Outside Arm M, H is already in the Universal Source-Crossing arm. In Arm M, |H|=2k+1, every k-set is Hamiltonian, and no k+1-set is Hamiltonian. If k=5 then |E|=5, forcing E Hamiltonian and contradicting the high-transition branch. If k=6 then |U|=6=k, forcing U Hamiltonian. Hence k>=7. Moreover any DONOR edge of the pair-core triangle forces k=5 by the existing donor/order-eleven theorem, again impossible. Thus the only Arm-M high-transition selected-reversal residue is a portal-only pair-core triangle with k>=7. This aligns the last selected-reversal obstruction with the existing portal-multiplicity program rather than creating a separate lane.

### 1. High-transition input
Retain the NON-HAMILTON E branch of `universal-one-extension-triangle-selected-reversal-dimer-deletion-contraction` SV33219. Thus the pair-core triangle carries its non-Hamiltonian six-set U, the outside set

  E=V(H)-U

is non-Hamiltonian, and for the reversed common dimer D every exact two-cover of H-D has at least three selected transitions across the fixed partition

  C | {c} | {t} | E.                                      (HT.1)

### 2. Enter the accepted R927 global split
Apply accepted R927.

If branch (U) holds, H already has a universally crossed singleton source and the configuration belongs to the Universal Source-Crossing arm. Nothing further is required here.

Assume therefore branch (M). Then

  |V(H)|=2k+1,

 every k-set is Hamiltonian, and no (k+1)-set is Hamiltonian.

### 3. Orders k=5 and k=6 are impossible
The pair-core triangle support U has order six.

If k=5, then |V(H)|=11 and

  |E|=11-6=5=k.

Arm M Hamiltonizes every k-set, so E is Hamiltonian. This contradicts the defining NON-HAMILTON E branch of SV33219.

If k=6, then U itself has order k. Arm M therefore Hamiltonizes U, contradicting the non-Hamiltonian six-union retained by the pair-core triangle construction.

Hence every Arm-M realization of the high-transition branch satisfies

  k>=7.                                                    (HT.2)

### 4. A donor perimeter edge is also impossible
The established section `universal-one-extension-donor-r927-arm-m-order11` proves that in Arm M any DONOR edge of the universal-one-extension pair-core cycle forces

  k=5, |V(H)|=11.

But k=5 is excluded by Section 3. Therefore every perimeter edge of the surviving pair-core triangle is PORTAL.

Thus the only Arm-M residue compatible with (HT.1) is

  k>=7,
  portal-only pair-core triangle,
  universal high transition on the common-dimer deletion. (HT.3)

### 5. Strategic consequence
The last selected-reversal residue from the pair-core triangle does not define a new global branch. It has only two destinations:

  R927(U): Universal Source-Crossing;

  R927(M): portal-only triangle with k>=7 and the high-transition dimer-deletion condition (HT.1).

Hence further work may be concentrated on the existing portal-multiplicity/uniform-arm program.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R927"
    }
]
```
