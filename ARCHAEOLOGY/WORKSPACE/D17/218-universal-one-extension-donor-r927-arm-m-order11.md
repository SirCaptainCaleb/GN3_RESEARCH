# In the R927 uniform arm, a universal-core donor edge forces order eleven

**Workspace:** D17
**State:** established
**Key:** `universal-one-extension-donor-r927-arm-m-order11`

**Summary:** In the SV26947 universal one-extension four-set setup, a DONOR edge gives an exact singleton-deletion cover with rail orders 5 and m-2. In accepted R927 Arm M, n=2k+1 and no (k+1)-set is Hamiltonian, so every tight path has order at most k. Any exact cover of H-s spans 2k vertices and hence has both rails of order exactly k. Therefore a donor edge forces 5=k=m-2, so k=5, m=7 and n=11. Thus every larger Arm-M universal-core triangle/quadrilateral from SV29868 is portal-only; a donor at any other order forces the R927 universal-crossing arm. The order-eleven donor case and portal-only nuclei remain open.

### 1. Setup
Retain the universal one-extension four-set setup and pair-core cycle of SV26947. Thus S is a four-set, Y=V(H)-S has order m>=7, fix s in S and T=S-s, and a DONOR edge de of the pair-core cycle means

  K=T+{d,e}

is Hamiltonian of order five and

  R=Y-{d,e}

is Hamiltonian of order m-2. Therefore

  K | R

is an exact two-cover of the singleton deletion H-s.

### 2. Uniform middle-layer path-size bound
Assume H lies in accepted R927 Arm M. Then |V(H)|=2k+1, every k-set is Hamiltonian, and every (k+1)-set is non-Hamiltonian. Any tight path in H has at most k vertices: a longer tight path contains a contiguous tight subpath on exactly k+1 vertices, contradicting the Arm-M hypothesis.

The exact cover H-s=K|R spans 2k vertices. Since each rail has order at most k, both rails must have order exactly k. Hence

  5=k,
  m-2=k.

Thus k=5, m=7 and |V(H)|=11.

### 3. Consequence
A DONOR edge of the SV26947 pair-core cycle can occur in R927 Arm M only at order eleven. Consequently, in every Arm-M counterexample of order greater than eleven, every edge of the bounded triangle/quadrilateral nucleus of SV29868 is necessarily a CROSSING PORTAL edge.

Equivalently, if a universal one-extension four-set produces a donor edge at any order other than eleven, accepted R927 forces H into Arm U rather than Arm M.

No claim is made that the order-eleven donor case closes, nor that a portal-only triangle/quadrilateral closes. The result is a global fork-currentization theorem: outside one finite order, the universal-core holonomy in the uniform arm is purely portal-valued.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R927"
    }
]
```
