# Every short pair-deletion endpoint transfer either doubles at the B-boundary or exposes a named extremal wrap shield

**Workspace:** D17
**State:** established
**Key:** `singleton-deep-p5-short-transfer-boundary-transport`

**Summary:** For each of the four pair-deletion fibers of SV16347 and either physical endpoint of the literal complement B, choose the transferred Hamilton five-path extremally with respect to the position of that endpoint. If the endpoint reaches its matching active boundary, the synchronized SV16094 endpoint star immediately absorbs the adjacent B vertex too, giving a strict two-vertex support transfer; when |B|=2 this Hamiltonizes the pair-deletion residue and closes H with the deleted dimer. Otherwise the unique improving cyclic rotation has a bad sole seam, and R3 gives its exact reverse as a named wrap shield on the extremal transferred representative. Thus all eight one-vertex transfers normalize branch-freely to two-vertex transfer/closure or an ancestry-bearing wrap shield, with no generic R435/R159/R542 payment.


### 1. Setup
Retain the accepted short-cell unit `singleton-deep-p5-short-r961-currentization` SV16094 and the current pair-support-transfer unit `singleton-deep-p5-short-pair-support-transfer` SV16347.

Thus for each of the four deleted pairs

  {s,q}, {s,u}, {q,t}, {t,p}

there is a named four-set X=U-{x,y}, an actual Hamilton P4 A_X on X, and an exact pair-deletion cover

  A_X | B

of H-{x,y}, where B=(b_0,...,b_k) is the retained literal Hamilton complement. Moreover, for either physical endpoint b of B, the five-set X+{b} is Hamiltonian and there is an exact transferred cover

  P^b | (B-b)                                           (BT.1)

with P^b an actual Hamilton path on X+{b}. The synchronized endpoint stars of SV16094 give

  (b_1,b_0,z),   (z,b_k,b_{k-1}) tight for every z in U.  (BT.2)

SV16347 already excludes |B|=1 in the surviving counterexample branch.

The argument below is order-theoretic after these facts. No Hamilton order on X+{b} is identified with A_X.

### 2. Source endpoint: minimize its active position
Fix one of the four fibers and take b=b_0. Among all Hamilton paths on X+{b_0}, choose

  P_L=(p_0,p_1,p_2,p_3,p_4)

so that the index i with p_i=b_0 is minimum. Pair it with the literal complement B-b_0 as in (BT.1).

If i=0, write

  P_L=(b_0,z_1,z_2,z_3,z_4),   z_j in X.

Then (b_1,b_0,z_1) is tight by (BT.2). Hence

  (b_1,b_0,z_1,z_2,z_3,z_4)                         (BT.3)

is a Hamilton path on X+{b_0,b_1}. Deleting the first two vertices of the displayed B-order leaves the literal path

  B-{b_0,b_1}=(b_2,...,b_k)

when nonempty. Therefore the same pair-deletion residue has undergone the strict support move

  X | B  ->  (X+{b_0,b_1}) | (B-{b_0,b_1}).          (BT.4)

If |B|=2, the residual complement is empty and (BT.3) Hamiltonizes H-{x,y}; the deleted two-vertex path (x,y) then gives a spanning two-cover of H, contradiction. Thus in a surviving boundary-hit branch |B|>=3 and (BT.4) is an exact two-cover of the pair-deletion residue.

Suppose instead i>0. Consider the tail cyclic rotation

  P_L'=(p_1,p_2,p_3,p_4,p_0).

Every turn of P_L' is inherited from P_L except

  alpha_L=(p_3,p_4,p_0).

If alpha_L were tight, P_L' would be Hamiltonian on the same support X+{b_0}; since b_0 is not p_0, its index would decrease from i to i-1, contradicting the extremal choice of P_L. Therefore alpha_L is bad. By R3 its complete reversal

  alpha_L^*=(p_0,p_4,p_3)                              (BT.5)

is tight.

Thus source-endpoint transfer has exactly the required finite normal form: either b_0 reaches the active source and immediately drags b_1 with it, or the actual source-minimal transferred path carries the named reverse tail-wrap shield (BT.5). The physical path order and the exact location of b_0 are retained.

### 3. Terminal endpoint: maximize its active position
The terminal endpoint is the literal dual without reversing any certified path. Take b=b_k and choose

  P_R=(q_0,q_1,q_2,q_3,q_4)

Hamiltonian on X+{b_k} so that the index j with q_j=b_k is maximum.

If j=4, write

  P_R=(z_1,z_2,z_3,z_4,b_k).

By (BT.2), (z_4,b_k,b_{k-1}) is tight, so

  (z_1,z_2,z_3,z_4,b_k,b_{k-1})                       (BT.6)

is Hamiltonian on X+{b_k,b_{k-1}}. With literal residual complement B-{b_k,b_{k-1}}, this gives the terminal analogue of the strict two-vertex transfer (BT.4), and again |B|=2 would close H.

If j<4, consider the head cyclic rotation

  P_R'=(q_4,q_0,q_1,q_2,q_3).

Its sole non-inherited turn is

  alpha_R=(q_4,q_0,q_1).

If alpha_R were tight, P_R' would be Hamiltonian on X+{b_k}; because b_k is not q_4, its index would increase from j to j+1, contradicting maximality. Hence alpha_R is bad, and R3 gives the exact reverse shield

  alpha_R^*=(q_1,q_0,q_4)                              (BT.7)

as a tight turn.

### 4. Eight normalized endpoint transfers
There are four explicit pair-deletion fibers in SV16347 and two physical endpoints of B. On each of these eight endpoint-transfer problems choose the corresponding extremal Hamilton five-path as above. Then exactly one of the following outcomes is retained:

1. BOUNDARY HIT: the transferred endpoint reaches its matching active boundary, and the synchronized SV16094 star absorbs the adjacent B vertex as well, yielding a strict two-vertex support transfer on the same pair-deletion residue; for |B|=2 this is immediate closure of H.

2. EXTREMAL WRAP SHIELD: the endpoint remains interior relative to its matching boundary, and the unique cyclic rotation that would improve its position is blocked. Its sole bad seam yields the exact named reverse turn (BT.5) or (BT.7), with the complete active order and endpoint position retained.

This is stronger than recording an arbitrary R548/R3 payment: the shield is attached to an extremal representative of a fixed transferred support, and its failure is precisely the obstruction to an additional physical support transfer. No generic R435, R159, R408, R542, or anonymous reverse-P4 conclusion is taken.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R548"
    }
]
```
