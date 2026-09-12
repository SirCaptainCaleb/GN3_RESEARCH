# Dense order-eleven donors force a lifted singleton endpoint or order discrepancy

**Workspace:** D17
**State:** established
**Key:** `singleton-universal-core-donor-discrepancy`

**Summary:** Retain the current universal-core order-eleven shell SV17264 with |X|=4, |Y|=7 and donor graph G_Y defined by ab donor-good iff Y-{a,b} is Hamiltonian, so every donor vertex has degree at least four. Every donor edge ab lifts to exact singleton-deletion covers (X+b)|(Y-{a,b}) of H-a and (X+a)|(Y-{a,b}) of H-b. If the lifted donor star at a is R408-quiet, endpoint counting forces deg_GY(a)=4: exactly two X vertices are endpoints in every lifted H-a cover, every donor neighbor is internal, and the two donor nonneighbors are exactly the endpoints of the donor rail. Hence if all stars are R408-quiet, G_Y is 4-regular. On a donor edge ab the two lifted covers contain Hamilton paths on the same donor support Y-{a,b}, whose endpoint pairs are the two nonneighbors of a and b respectively. R435-quiet comparison would force the same literal order and hence equal endpoint pairs. If every donor edge were also R435-quiet, connectedness of the 4-regular graph G_Y would make all complement-neighbor pairs identical, impossible. Therefore the order-eleven shell necessarily emits an explicit R408 endpoint/internal discrepancy or an explicit R435 reverse-state/reverse-trimer/proper-cycle event on a named donor support. This is structured currentization, not closure or generic payment.

### 1. Donor edges lift to exact singleton covers
Retain the current established universal-core shell `singleton-universal-core-order11-exchange-shell` at exact section version SV17264. Thus

  V(H)=X disjoint-union Y,   |X|=4,   |Y|=7,

`X+z` is Hamiltonian for every `z in Y`, and the donor graph `G=G_Y` on `Y` is defined by

  `ab in E(G)` iff `Y-{a,b}` is Hamiltonian.

The shell proves `deg_G(a)>=4` for every `a in Y`.

Fix a donor edge `ab`. Choose an actual Hamilton path `T_ab` on `Y-{a,b}`. Since `X+b` and `X+a` are Hamiltonian, choose actual Hamilton paths `P_a^b` on `X+b` and `P_b^a` on `X+a`. Then

  `F_a^b = P_a^b | T_ab`

is a literal two-cover of `H-a`, and

  `F_b^a = P_b^a | T_ab`

is a literal two-cover of `H-b`. Both are exact. Indeed, if `H-a` were Hamiltonian then that Hamilton path together with the singleton `a` would two-cover `H`; the same argument applies to `b`. Thus every donor edge gives two actual lifted singleton rows sharing one literal Hamilton donor rail.

### 2. An R408-quiet donor star has degree exactly four
Fix `a in Y` and retain one lifted exact cover `F_a^b` for every donor neighbor `b in N_G(a)`. If two such covers disagree on endpoint/internal status of any physical vertex, retain those two named covers and that vertex as the explicit R408 interface and stop.

Assume instead that the whole donor star at `a` is R408-quiet. By the proof mechanism of accepted R408, absence of an endpoint/internal disagreement means that all these exact covers of the same proper residue `H-a` have one common physical endpoint set `E_a`, of size four. Put

  `alpha_a = |E_a cap X|`.

In the lifted cover indexed by `b`, the active rail `P_a^b` has support `X+b` and exactly two endpoints. Hence

  `alpha_a + 1_{b in E_a} = 2`                         (DD.1)

for every donor neighbor `b`. Thus every donor neighbor has the same endpoint status. If that status were endpoint, then `alpha_a=1`; but then all at least four donor neighbors would lie in `E_a`, while only `4-alpha_a=3` endpoint slots lie in `Y`, impossible. Therefore every donor neighbor is internal, `alpha_a=2`, and exactly two vertices of `Y-{a}` lie in `E_a`.

Those two `Y`-endpoints cannot be donor neighbors, so they are nonneighbors of `a` in `G`. Since `deg_G(a)>=4`, there are at most two such nonneighbors. Therefore there are exactly two, and

  `deg_G(a)=4`,

  `E_a cap Y = (Y-{a}) - N_G(a)`.                    (DD.2)

Equivalently, in every lifted `H-a` cover the donor rail has as its two physical endpoints exactly the two nonneighbors of `a` in `G`.

### 3. Global endpoint quietness forces a 4-regular donor graph
Suppose no donor star emits an R408 interface. Applying Section 2 at every `a in Y` gives

  `deg_G(a)=4` for all `a`.                            (DD.3)

Let `J` be the complement of `G` on the seven donor labels. Then `J` is 2-regular. Write `N_J(a)` for the two nonneighbors of `a` in `G`. By (DD.2), `N_J(a)` is exactly the endpoint pair of the donor rail in every lifted exact cover of `H-a`.

### 4. R435-quiet donor edges would force impossible constant endpoint pairs
Fix a donor edge `ab in E(G)`. The two lifted exact covers

  `F_a^b = P_a^b | T_ab`,
  `F_b^a = P_b^a | T'_ab`

may use different actual Hamilton orders `T_ab,T'_ab` on the same support `Y-{a,b}`; retain both. Their physical endpoint pairs are respectively

  `N_J(a)` and `N_J(b)`.                              (DD.4)

Apply the proof mechanism of accepted R435 directly to these two Hamilton paths on the common support. If their orders are not monotone in one another, R435 emits an explicit selected-state reversal, reverse trimer, or proper tight cycle. In the R435-quiet branch, every vertex of the second Hamilton path occurs in increasing order along the first. Because the supports are equal and both paths are Hamiltonian, the literal vertex orders coincide. In particular their endpoint pairs coincide, so

  `N_J(a)=N_J(b)`                                      (DD.5)

for every donor edge on which no R435 output occurs.

Now suppose every donor edge were R435-quiet as well. The 4-regular simple graph `G` on seven vertices is connected: every connected component of a 4-regular simple graph has at least five vertices, so two components cannot fit inside seven vertices. Therefore (DD.5) propagates along `G` and makes `N_J(a)` one common two-set `S` for every `a in Y`. Choose `a in S`. Then `a in N_J(a)=S`, impossible in a simple graph.

Hence the simultaneous all-R408-quiet and all-R435-quiet branch cannot occur.

### 5. Exact output and fence
The order-eleven universal-core donor shell therefore necessarily supplies at least one of the following structured outputs:

1. **DONOR-STAR ENDPOINT DISCREPANCY:** for one fixed deletion label `a`, two named lifted exact covers `F_a^b,F_a^c` of `H-a` and one named physical vertex whose endpoint/internal status differs, giving the actual R408 component-drop interface after puncture; or
2. **COMMON-DONOR ORDER DISCREPANCY:** one donor edge `ab`, the common five-set `Y-{a,b}`, two actual Hamilton orders on that same support coming from the lifted `H-a` and `H-b` rows, and the explicit R435 reverse-state / reverse-trimer / proper-cycle geometry forced by their comparison.

This bypasses selection of the shortest fixed-puncture support-exchange circuit for the purpose of obtaining a first current order/endpoint discrepancy. It does **not** prove a spanning two-cover, R561, or a component-reducing linear-forest augment, and neither output is paid anonymously here. The lifted covers, donor edge/star, physical endpoint sets, common donor support, and exact R408/R435 witness are retained for the next augmentation consumer.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R408"
    },
    {
        "relation": "dependency",
        "revision_id": "R435"
    }
]
```
