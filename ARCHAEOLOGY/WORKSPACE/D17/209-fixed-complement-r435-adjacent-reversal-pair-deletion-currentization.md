# A neighboring-support selected reversal currentizes on the exchanged pair deletion

**Workspace:** D17
**State:** established
**Key:** `fixed-complement-r435-adjacent-reversal-pair-deletion-currentization`

**Summary:** Inside a live puncture cylinder, let P_a on A-a and P_b on A-b be neighboring Hamilton puncture paths with common literal complement Q, and suppose their R435 comparison contains an adjacent selected-state reversal on a common physical dimer {u,v}: P_a selects u->v while P_b selects v->u. Delete both exchanged labels a,b. If b is an endpoint of P_a and a an endpoint of P_b, the two trims are literal exact two-covers of the same residue H-{a,b}, with identical support partition (A-{a,b})|Q and the same dimer selected oppositely, giving a current fixed-complement reversal interface. If either exchanged label is internal in its opposite puncture path, that trim is a literal three-cover of the pair-deletion residue. Accepted smallest-counterexample minimality R4 applied to the deleted dimer {a,b} supplies an exact two-cover T of the same residue; elementary component counting forces T to select a physical edge crossing two components of every internal trim. The lifted dimer (a,b)|T is an actual maximum spanning three-forest of H. If both labels are internal, one common T simultaneously crosses both three-cover decompositions. Thus adjacent-reversal R435 output is never merely abstract order debt: it currentizes as a same-residue fixed-complement reversal or as a fresh pair-deletion maximum-three-forest portal with explicit component crossings.

### 1. Neighboring selected-state reversal
Retain a live puncture cylinder

  V(H)=A disjoint_union V(Q)

in a hypothetical smallest Strong Level-(1) counterexample. Let a,b be distinct live labels and retain actual Hamilton puncture paths

  P_a on A-a,
  P_b on A-b,

so P_a|Q and P_b|Q are exact singleton-deletion two-covers with the same literal complement Q.

Assume a neighboring-support R435 comparison exhibits an adjacent selected-state reversal on a common physical dimer {u,v}, with u,v in A-{a,b}. After orienting the statement,

  P_a selects u -> v,
  P_b selects v -> u.                                    (AR.1)

### 2. Trim both exchanged labels to one common residue
Put

  S=A-{a,b},
  W=H-{a,b}=S disjoint_union V(Q).

Delete b from the literal path P_a. If b is an endpoint of P_a, the surviving P_a-b is one Hamilton path on S; if b is internal, P_a-b is the disjoint union of its two nonempty prefix/suffix paths. Hence

  R_a=(P_a-b)|Q                                           (AR.2)

is respectively a literal two-cover or three-cover of W.

Dually

  R_b=(P_b-a)|Q                                           (AR.3)

is a two-cover when a is an endpoint of P_b and a three-cover when a is internal.

Since u,v are common retained vertices and neither is deleted, the selected states in (AR.1) survive literally in R_a and R_b.

### 3. Endpoint-endpoint case gives a same-residue fixed-complement reversal
Suppose b is an endpoint of P_a and a is an endpoint of P_b. Then R_a and R_b are literal two-covers of the same residue W. Their support partitions are identical:

  S | V(Q).                                                (AR.4)

Moreover they retain the same literal Hamilton complement Q and select {u,v} in opposite directions. Thus (R_a,R_b;u,v;Q) is a current same-residue fixed-complement selected-reversal interface.

No R561 conclusion is asserted here. The point is currentization: the neighboring-support reversal has descended one deletion level to two exact representatives with identical support partition and literal complement, which is exactly the input geometry of the existing fixed-complement selected-reversal transport program.

### 4. Any internal exchanged label forces a current component crossing
Now suppose b is internal in P_a, so R_a has three nonempty path components. The two-vertex word

  D=(a,b)

is a proper tight path, vacuously at order two. By accepted smallest-counterexample minimality R4/P601, its complement W has path-cover number exactly two. Choose any literal exact two-cover

  T=T_1|T_2                                                (AR.5)

of W.

Then T must select a physical adjacency joining two distinct components of the three-cover R_a. Indeed, if no selected T-edge crossed between R_a-components, each connected T-rail would lie wholly inside one R_a-component. Two T-rails could then meet at most two of the three nonempty R_a-components, contradicting that T spans W. Retain one such selected crossing state

  x_a -> y_a.                                              (AR.6)

The dimer D together with T is therefore a literal spanning three-path cover

  (a,b)|T_1|T_2                                            (AR.7)

of H. Since H admits no spanning two-cover, (AR.7) is a maximum compatible spanning three-forest. It is an actual current representative produced from the adjacent-reversal pair deletion, with the crossing (AR.6) retaining its source decomposition R_a.

If instead a is internal in P_b, the same argument gives a selected T-crossing x_b->y_b between two components of R_b.

If both a and b are internal in the opposite puncture paths, choose T once. The same exact T must cross both literal three-cover decompositions R_a and R_b, so one pair-deletion representative carries two simultaneously current component-crossing obligations, one relative to each ancestry-preserving trim.

### 5. Parent-scale consequence
Therefore the adjacent selected-state reversal branch of neighboring-support R435 has only two current destinations:

1. ENDPOINT-ENDPOINT: two exact covers of one pair-deletion residue with identical support partition and literal complement Q, selecting one physical dimer oppositely;
2. INTERNAL: an exact pair-deletion two-cover T which crosses the explicit three-cover obtained by trimming the internal exchanged label, and whose lift (a,b)|T is an actual maximum three-forest on H.

Together with the proper-cycle movable-break family and the reverse-trimer core-or-fresh-forest consumer, this removes every R435 output from the status of anonymous local conflict. This section itself does not prove escape from the resulting representative family.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R4"
    },
    {
        "relation": "dependency",
        "revision_id": "R435"
    }
]
```
