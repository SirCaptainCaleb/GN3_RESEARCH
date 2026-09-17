# Coherent donor lifts force a same-residue R408 discrepancy at order eleven

**Workspace:** D17
**State:** established
**Key:** `singleton-universal-core-coherent-lift-r408`

**Summary:** In the order-eleven universal-core shell, choose one Hamilton path P^b on each X+b and one Hamilton donor path T^{ab} on each donor-good Y-{a,b}, and reuse these literal orders coherently in every lifted singleton row. If every donor star were R408-quiet, the endpoint-count argument forces the donor graph G to be 4-regular and makes the donor endpoints in every H-a row exactly the two nonneighbors N_J(a). For each donor edge ab, however, the same literal T^{ab} occurs in both lifted rows H-a and H-b, so its unique endpoint pair equals both N_J(a) and N_J(b). Since a 4-regular graph on seven vertices is connected, all N_J(a) would be one common two-set, impossible because a is never its own nonneighbor. Hence a coherently chosen lifted family necessarily contains two exact covers of one fixed H-a with a named physical endpoint/internal disagreement, i.e. an actual R408 interface. No R435 fallback is needed. This is currentization, not closure.

### 1. Coherent lift family

Retain the order-eleven universal-core shell SV17264:

  V(H)=X disjoint-union Y,   |X|=4,   |Y|=7,

`X+b` is Hamiltonian for every `b in Y`, and the donor graph `G` on `Y`, defined by

  `ab in E(G)` iff `Y-{a,b}` is Hamiltonian,

has minimum degree at least four.

Make the Hamilton-order choices globally coherent. For every `b in Y`, choose once and for all one literal Hamilton path `P^b` on `X+b`. For every unordered donor edge `ab in E(G)`, choose once and for all one literal Hamilton path `T^{ab}` on `Y-{a,b}`. For each oriented incidence `(a,b)` of `G`, form

  `F_a^b = P^b | T^{ab}`

as a literal two-cover of `H-a`. It is exact: a Hamilton path on `H-a` together with the singleton `a` would two-cover `H`.

The point of the coherent choice is that `P^b` is literally the same path in every star using label `b`, and `T^{ab}` is literally the same donor path in the two rows `H-a` and `H-b`. No comparison theorem is needed to identify those orders.

### 2. Quiet stars force degree four and identify donor endpoints

Suppose, toward contradiction, that no donor star contains an endpoint/internal disagreement between two of its lifted covers. Fix `a`. All covers `F_a^b`, `b in N_G(a)`, are exact covers of the same proper residue `H-a`. By the contrapositive endpoint-set clause in the proof of accepted R408, they have one common physical endpoint set `E_a`, with `|E_a|=4`. Put

  `alpha_a = |E_a cap X|`.

The active rail `P^b` has support `X+b` and exactly two endpoints, so for every `b in N_G(a)`,

  `alpha_a + 1_{b in E_a} = 2`.                         (CL.1)

All donor neighbors of `a` therefore have the same endpoint status. They cannot all be endpoints: then `alpha_a=1`, but at least four donor neighbors would have to occupy only `4-alpha_a=3` slots of `E_a cap Y`. Hence every donor neighbor is internal and `alpha_a=2`. Thus `E_a cap Y` consists of exactly two nonneighbors of `a`. Since `deg_G(a)>=4`, there are at most two nonneighbors among the other six labels, so there are exactly two and

  `deg_G(a)=4`,
  `E_a cap Y = (Y-{a}) - N_G(a)`.                      (CL.2)

Applying this at every `a` makes `G` 4-regular. Let `J` be its complement on `Y`; then `J` is 2-regular and (CL.2) reads

  `E_a cap Y = N_J(a)`.                                (CL.3)

### 3. One literal donor order synchronizes adjacent stars

Fix any donor edge `ab in E(G)`. The coherent family contains

  `F_a^b = P^b | T^{ab}` in H-a,
  `F_b^a = P^a | T^{ab}` in H-b.

The donor rail is the identical literal path `T^{ab}` in both covers. Its support is `Y-{a,b}`. In the first cover its physical endpoint pair is, by (CL.3), `N_J(a)`; in the second it is `N_J(b)`. A literal path has one endpoint pair, hence

  `N_J(a)=N_J(b)`                                      (CL.4)

for every edge `ab` of `G`.

No R435 comparison is used here. Equality follows solely because we deliberately reused the same actual Hamilton order on the common donor support.

### 4. Connectedness contradiction

A 4-regular simple graph on seven vertices is connected: every nonempty connected component of a 4-regular simple graph has at least five vertices, so two components cannot fit into seven vertices. Therefore (CL.4) propagates along `G`, and there is one fixed two-set `S subset Y` such that

  `N_J(a)=S` for every `a in Y`.

Choose `a in S`. Then `a in N_J(a)`, impossible in a simple graph.

Thus the assumption that every donor star is R408-quiet is false.

### 5. Exact output and nonclaim

There exist a donor label `a`, two distinct donor neighbors `b,c in N_G(a)`, and a physical vertex `z in V(H)-{a}` such that the two named exact covers

  `F_a^b = P^b | T^{ab}`,
  `F_a^c = P^c | T^{ac}`

of the same residue `H-a` disagree on whether `z` is an endpoint or internal. By the fully reconstructed proof mechanism of R408, puncturing that named `z` gives the component-drop interface and hence the structured R408 output.

This strictly strengthens the first-discrepancy conclusion of SV17667 in the coherent-lift family: no common-donor R435 fallback is required. It does not yet restore the omitted label `a`, prove R561, or give a spanning two-cover of `H`; the exact covers, star labels, literal Hamilton orders, and discrepant physical vertex must be retained for the next consumer.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R408"
    }
]
```
