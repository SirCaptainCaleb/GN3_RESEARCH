# A terminal puncture is last-gap localized outside explicit R435 geometry

**Workspace:** D17
**State:** established
**Key:** `terminal-puncture-last-gap`

**Summary:** Let Omega=X+p be a non-Hamiltonian deletion-Hamiltonian saturated petal with retained Hamilton order X=(x_1,...,x_k), and delete the terminal x_k. For any Hamilton path K on Omega-x_k, either K has explicit R435 geometry relative to the retained order X-x_k, or K is exactly that retained order with p inserted in the final gap or at the tail. In the final-gap case (x_k,x_{k-1},p) is tight; in the tail case (x_k,p,x_{k-1}) is tight. Combined with the accepted source-anchored R961 theorem, complete absence of explicit R435 geometry forces the TTT tail packet and the exact final-gap puncture order.


### Role-correct terminal puncture localization
Let

  Omega = X union {p},
  X=(x_1,...,x_k),   k>=4,

where X is a retained Hamilton path, Omega is non-Hamiltonian, and every puncture Omega-y is Hamiltonian. Put

  u=x_k,   A=X-{u}=(x_1,...,x_{k-1}).

Let K be ANY Hamilton path on A+p=Omega-u.

Compare K with the literal retained order A by accepted R435. If the comparison has explicit R435 reversal, reverse-trimer, or proper-cycle geometry, retain that output. Otherwise the A-contacts of K occur in increasing A-order. Since K contains every vertex of A and only the additional label p, K is obtained by inserting p into one slot of the literal order A.

If p is inserted before x_{k-1} and not in the final gap, then K ends with the literal terminal dimer

  (x_{k-2},x_{k-1}).

Appending u=x_k preserves every turn of K and adds only the old source turn

  (x_{k-2},x_{k-1},x_k),

which is tight. This would Hamiltonize Omega, contradiction.

Hence outside explicit R435 geometry there are only two possible literal orders:

  K=(x_1,...,x_{k-2},p,x_{k-1}),

or

  K=(x_1,...,x_{k-2},x_{k-1},p).

In the first case appending u would fail only at (p,x_{k-1},u). Since Omega is non-Hamiltonian,

  (p,x_{k-1},u) is bad,

and boundary antisymmetry gives

  (u,x_{k-1},p) tight.

In the second case appending u would fail only at (x_{k-1},p,u), so

  (x_{k-1},p,u) is bad,
  (u,p,x_{k-1}) is tight.

No path is reversed in this argument.

### Relation to the accepted source-anchored R961 packet
Apply the accepted exact-unit theorem `source-anchored-r961-fan` to the same saturated petal. If its globally quiet constant-role packet is HHH, then u=x_k is a non-anchor puncture and every Hamilton path on Omega-u already has explicit R435 geometry against the fixed HHH packet. Thus a globally R435-quiet terminal puncture can occur only in the TTT anchored case.

In that TTT case the accepted packet contains the literal puncture path

  P_u=(x_1,...,x_{k-2},p,x_{k-1}),

which is exactly the final-gap alternative above. Therefore if the entire terminal puncture family is free of explicit R435 geometry, the final-gap order is forced. Any tail order (...,x_{k-1},p), if it also exists, is itself R435-nonquiet against this retained TTT puncture path and should be kept as the explicit order-conflict output rather than silently identified with it.

### Use in the stationary recurrence
For each stationary seam terminal u_X or u_Y, the saturated puncture path on X-u_X+p or Y-u_Y+p may therefore be treated as follows: explicit R435 geometry is already a current order-valued exit; otherwise p is localized at the terminal source gap, with the exact reverse turn through the omitted terminal retained. This is the correct input when analyzing the four common-cross types A-B, A-Z, B-Z, p-Z from `stationary-two-seam-common-cross`.

Status: complete internal deduction from accepted R435, R3, and the accepted exact-unit source-anchored R961 theorem. It is a localization interface, not an absorber by itself.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R435"
    },
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R961"
    }
]
```
