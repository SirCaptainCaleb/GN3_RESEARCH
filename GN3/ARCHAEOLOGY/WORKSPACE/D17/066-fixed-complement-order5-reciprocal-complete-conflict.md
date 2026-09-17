# Order-five reciprocal activity upgrades to a complete support-family Reverse-Ear conflict

**Workspace:** D17
**State:** established
**Key:** `fixed-complement-order5-reciprocal-complete-conflict`

**Summary:** Continue the order-five same-support transfer packet of SV23268 and let H_2,H_3 be the nonempty Hamilton-order families on Q-q2+p and Q-q3+p. Exactly one of two useful interfaces is available. Either every K3 in H_3 is R435-active against the ancestral Q, or there exists a Q-quiet K3; any such quiet K3 is one of the two insertion words C3,D3 from SV23268, and then EVERY K2 in H_2 is R435-active against that fixed K3. The second assertion is symbolic. If K2 were also quiet against K3, accepted insertion-cell unit SV302 forces q3 to occupy the same or an adjacent slot to q2 in their common four-vertex order because their union Q+p is non-Hamiltonian. For C3 all three candidate q3 slots either reproduce an already-forbidden Q-quiet pair, directly Hamiltonize E0=Q-q0+p, or violate the reciprocal wall. For D3 the three candidates are eliminated by the terminal wall or by the R902 edge order on E0, with one comparison in the last case. Thus one fixed Hamilton path always has complete R435 conflict with every Hamilton representative of one adjacent reciprocal support. All representatives retain the same literal complement A in exact singleton fibers.

### 1. Two adjacent reciprocal Hamilton-order families
Retain all notation and conclusions of `fixed-complement-order5-reciprocal-r435-forcing` SV23268. Thus

  Q=(q_0,q_1,q_2,q_3,q_4),
  p=y_i,
  A=Omega-{p},
  Lambda=Q+{p}

with Lambda and E_0=Q-q_0+p non-Hamiltonian, while the reciprocal supports

  X_2=Q-q_2+p,
  X_3=Q-q_3+p

are Hamiltonian. Let H_2 and H_3 denote their nonempty families of literal Hamilton tight paths.

We prove the following complete-conflict alternative.

**(Q-CONFLICT)** Every K_3 in H_3 has an explicit R435 output when compared with the ancestral Q.

**(CROSS-CONFLICT)** There exists a Q-quiet K_3 in H_3, and for every K_2 in H_2 the comparison (K_3,K_2) has an explicit R435 output.

Thus in either case one fixed Hamilton path, Q in the first branch or one chosen quiet K_3 in the second, is R435-active against an entire neighboring reciprocal Hamilton-order family.

### 2. A quiet K_3 has only the two SV23268 forms
If Q-CONFLICT fails, choose K_3 in H_3 whose comparison with Q is R435-quiet. By SV23268 its literal order is exactly one of

  C_3=(q_0,q_1,p,q_2,q_4),
  D_3=(q_0,q_1,q_2,q_4,p).                              (CC.1)

Fix this K_3. Suppose toward contradiction that some K_2 in H_2 is also R435-quiet against K_3.

The two supports share

  S={q_0,q_1,q_4,p}

and differ by q_3 versus q_2. R435 quietness makes the common S vertices occur in one common literal order. Since

  X_2 union X_3 = Lambda

is non-Hamiltonian, the accepted exact insertion-cell unit `middle-layer-two-active-supports` SV302 applies through its elementary proof mechanism: if q_2 and q_3 occupied insertion slots separated by at least two positions in that common S-order, the two insertion windows would combine to a Hamilton path of Lambda. Therefore their slots are equal or adjacent. We now eliminate the resulting three possibilities in each row of (CC.1).

### 3. C_3 permits no cross-quiet K_2
For C_3 the common S-order is

  (q_0,q_1,p,q_4),

and q_2 occupies the slot between p and q_4. Hence q_3 has only the three same/adjacent slots:

  (i)   (q_0,q_1,q_3,p,q_4),
  (ii)  (q_0,q_1,p,q_3,q_4),
  (iii) (q_0,q_1,p,q_4,q_3).                            (CC.2)

Case (i) is exactly the B_2 quiet insertion word paired with C_3, already eliminated symbolically in SV23268 because it Hamiltonizes E_0 in the R902 edge order.

Case (ii) is the forbidden middle Q-relative insertion from SV23268: together with the retained transfer shield (q_2,q_1,p), it gives the literal Hamilton path

  (q_2,q_1,p,q_3,q_4)

on E_0.

In case (iii), K_2 itself supplies the consecutive turns

  (q_1,p,q_4), (p,q_4,q_3).

Together with the same retained transfer shield (q_2,q_1,p), the word

  (q_2,q_1,p,q_4,q_3)

is a literal Hamilton path on E_0. Again contradiction.

So no K_2 can be cross-quiet with C_3.

### 4. D_3 permits no cross-quiet K_2
For D_3 the common S-order is

  (q_0,q_1,q_4,p),

and q_2 occupies the slot between q_1 and q_4. Thus q_3 has only

  (i)   (q_0,q_3,q_1,q_4,p),
  (ii)  (q_0,q_1,q_3,q_4,p),
  (iii) (q_0,q_1,q_4,q_3,p).                            (CC.3)

Case (ii) is impossible immediately: its terminal turn (q_3,q_4,p) is bad because the fixed-complement terminal wall supplies the reverse turn (p,q_4,q_3).

For the other two cases use the total edge order on the non-Hamiltonian five-set E_0 supplied by accepted R902. Write uv for the ordinary edge {u,v}. The retained Q order and inward/terminal walls give

  q_1q_2 < q_2q_3 < q_3q_4,
  q_2q_3 < q_2p,
  q_4p < q_3q_4.                                       (CC.4)

D_3 gives

  q_1q_2 < q_2q_4 < q_4p.                              (CC.5)

In case (iii), K_2 gives

  q_1q_4 < q_3q_4 < q_3p.

Combining (CC.5) with q_4p<q_3q_4<q_3p yields

  q_1q_2 < q_2q_4 < q_4p < q_3p,

so

  (q_1,q_2,q_4,p,q_3)

is an increasing Hamilton path of E_0, contradiction.

In case (i), K_2 gives

  q_1q_3 < q_1q_4 < q_4p.                              (CC.6)

Compare the two incident edges q_4p and q_2p in the total order. If

  q_4p < q_2p,

then (CC.6) gives the increasing Hamilton path

  (q_3,q_1,q_4,p,q_2).

If instead q_2p < q_4p, then (CC.4) gives q_1q_2<q_2p and the terminal wall gives q_4p<q_3q_4, so

  (q_1,q_2,p,q_4,q_3)

is increasing. Either way E_0 is Hamiltonian, contradiction.

Hence no K_2 can be cross-quiet with D_3 either.

### 5. Complete conflict and current provenance
We have proved that whenever a Q-quiet K_3 exists, every Hamilton K_2 on X_2 is R435-active against that fixed K_3. If no Q-quiet K_3 exists, then by definition every Hamilton K_3 is R435-active against Q. This is exactly Q-CONFLICT or CROSS-CONFLICT.

Every path in H_2 and H_3 pairs with the same literal Hamilton complement A, yielding exact singleton-deletion covers of H-q_2 and H-q_3 respectively; Q itself pairs with A in the exact H-p cover. Thus the complete order conflict remains inside one fixed-complement exchange family. No source ancestry is discarded.

This theorem does not consume the resulting R435 outputs. Its gain over a single forced Reverse-Ear event is quantifier strength: at complement order five there is a fixed base representative against which an entire reciprocal support fiber is order-active. The TTT statement is the exact order dual.


## References

```json
[
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
