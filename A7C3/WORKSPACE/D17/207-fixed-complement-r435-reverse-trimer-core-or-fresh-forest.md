# A one-foreign R435 reverse trimer yields a universal extension core or a fresh maximum three-forest

**Workspace:** D17
**State:** established
**Key:** `fixed-complement-r435-reverse-trimer-core-or-fresh-forest`

**Summary:** Inside a live puncture cylinder, let P=(v0,...,vk) be a retained Hamilton path on A-a with fixed Hamilton complement Q, and suppose a neighboring-support R435 comparison emits a one-foreign reverse trimer at one seam. For the first-seam form (a,vi,v{i-1}), if i=k then P[0,k-1] | (a,vk) | Q is already a fresh spanning three-cover. If i<k, test the opposite local turn across the same middle vi. Tight (vi+1,vi,a) together with the inherited (vi-1,vi,vi+1) and the reverse trimer forms a directed comparison triangle on {a,vi-1,vi,vi+1}, so by R902 that four-set is universally one-extendable. Otherwise R3 gives (a,vi,vi+1), and cutting P before vi yields the fresh maximum three-forest P[0,i-1] | (a,vi,...,vk) | Q. The second-seam form is the exact dual, cutting after vj. Hence seam-reverse-trimer output in neighboring-support R435 geometry is never static debt: it immediately produces Astra v57's small extension core or an actual new maximum-three-forest representative.

### 1. Current one-foreign reverse-trimer setup
Retain a live puncture cylinder

  V(H)=A disjoint_union V(Q)

in a hypothetical smallest counterexample. Fix a live label a and one retained Hamilton puncture path

  P=(v_0,v_1,...,v_k)

on A-a, with literal common complement Q. Suppose a neighboring-support R435 comparison uses P as its reference path and its unique foreign vertex is a. By the one-foreign localization, any reverse-ear seam trimer uses this same physical label a.

### 2. First-seam reverse trimer
Suppose R435 emits

  (a,v_i,v_{i-1}) tight                                    (RT.1)

for some i>=1.

If i=k, then

  P[0,k-1] | (a,v_k) | Q                                  (RT.2)

is already a literal spanning three-path cover of H. The dimer (a,v_k) needs no turn certificate. Since H has no spanning two-cover, (RT.2) is a maximum compatible spanning three-forest. This is a fresh representative unless it coincides with a previously retained state.

Assume now i<k. The reference path P certifies

  (v_{i-1},v_i,v_{i+1}) tight.                             (RT.3)

Test the third comparison at the same physical middle v_i.

If

  (v_{i+1},v_i,a) tight,                                   (RT.4)

then in the local comparison tournament at v_i the ordinary incident edges satisfy

  a v_i -> v_i v_{i-1} -> v_i v_{i+1} -> a v_i.

Thus the four-set

  X={a,v_{i-1},v_i,v_{i+1}}

contains a directed comparison triangle. This triangle persists after adjoining any exterior vertex d. Hence every five-set X+d is nonintegrable, and accepted R902 makes X+d Hamiltonian. Therefore

  X+d is Hamiltonian for every d outside X.                (RT.5)

So X is a universally one-extendable four-set in the exact sense of current Guidance G9. No Hamiltonicity of X itself is claimed.

If (RT.4) is bad, boundary antisymmetry R3 gives

  (a,v_i,v_{i+1}) tight.                                   (RT.6)

Now cut P immediately before v_i. The two active paths

  L=P[0,i-1],
  R=(a,v_i,v_{i+1},...,v_k)

are both literal tight paths: L is inherited from P, and R uses (RT.6) followed only by inherited P turns. Therefore

  L | R | Q                                                (RT.7)

is a literal spanning three-path cover of H, hence a maximum compatible spanning three-forest. It is a fresh current representative created directly from the R435 seam output.

### 3. Second-seam reverse trimer
The terminal-side R435 seam is dual. Suppose

  (v_{j+1},v_j,a) tight                                    (RT.8)

for some j<=k-1.

If j=0, then

  (v_0,a) | P[1,k] | Q

is already a spanning maximum three-forest.

If j>0, test (a,v_j,v_{j-1}). If it is tight, then together with the inherited turn (v_{j-1},v_j,v_{j+1}) and (RT.8) it forms a directed comparison triangle at middle v_j, so

  {a,v_{j-1},v_j,v_{j+1}}

is universally one-extendable by R902. If instead (a,v_j,v_{j-1}) is bad, R3 gives

  (v_{j-1},v_j,a) tight,

and cutting P immediately after v_j gives the literal spanning maximum three-forest

  (v_0,...,v_j,a) | P[j+1,k] | Q.                         (RT.9)

### 4. Consequence for active neighboring-support holonomy
Therefore a one-foreign neighboring-support R435 conflict has the following exact status for its reverse-trimer branch:

1. SMALL CORE: a physical four-set is universally one-extendable; or
2. FRESH REPRESENTATIVE: the old puncture path is cut once and the foreign omitted label is attached to one side, while the literal common complement Q is retained.

The fresh representative is a maximum three-forest on H itself, so it enters the closed-exchange-class parent directly. No support-copy theorem, Hall argument, or generic payment is used.

Combined with the sibling movable-break theorem for proper-cycle output, this means two of the three nonquiet R435 species already satisfy the G9 principle that a blocked/current conflict must either emit the small extension core or generate an actual new maximum representative. The adjacent selected-state reversal branch remains separate.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R435"
    },
    {
        "relation": "dependency",
        "revision_id": "R902"
    }
]
```
