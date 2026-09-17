# Source-anchored R961 synchronization forces a global Reverse-Ear event in the uniform middle layer

**Workspace:** D17
**State:** established
**Key:** `uniform-middle-layer-global-source-anchored-reverse-ear-forcing`

**Summary:** Fix any Hamilton k-path P in the R927 uniform residue. For each exterior label y, accepted R961 plus the certified source-anchored theorem SV304 says either explicit source-relative R435 geometry occurs on X+y or the fully P-quiet residue is the HHH or TTT packet anchored at the first or last source gap. Exact two-label splices show at most one exterior y can realize quiet HHH and at most one can realize quiet TTT; same-role equal anchors splice to a P_{k+1}. Since k>=5 in the live branch, at least four exterior critical blocks remain, so some explicit source-anchored R435 event is unavoidable. Hence every uniform middle-layer system has actual order activity relative to one fixed source path; no all-quiet support-only configuration survives. This does not by itself absorb the R435 event.

### 1. Uniform critical blocks around one fixed source path
Work in accepted R927 Arm M with k>=5:

  |V(H)|=2k+1,
  every k-set is Hamiltonian,
  no (k+1)-set is Hamiltonian.

Fix any actual Hamilton order

  P=(x_1,...,x_k)

on one k-support X. For every exterior label y in V(H)-X, the (k+1)-set

  Omega_y=X union {y}

is non-Hamiltonian, while every singleton deletion of Omega_y has order k and is Hamiltonian by uniformity. Thus every Omega_y is a saturated non-Hamiltonian deletion-Hamiltonian block with the SAME retained source puncture P=Omega_y-y.

Apply accepted R961/P1033 to each Omega_y, then the certified exact section unit `source-anchored-r961-fan` SV304. For each y there are only two parent outputs.

(ACTIVE_y) Some Hamilton puncture comparison in Omega_y has explicit R435 geometry relative to the retained source P / fixed three-path packet.

(QUIET_y) The fully P-quiet constant-role packet is source-anchored, necessarily one of the exact forms below.

HHH(y):
  P_y=P,
  P_{x_1}=(x_2,y,x_3,...,x_k),
  P_{x_2}=(y,x_1,x_3,...,x_k).

TTT(y):
  P_y=P,
  P_{x_k}=(x_1,...,x_{k-2},y,x_{k-1}),
  P_{x_{k-1}}=(x_1,...,x_{k-2},x_k,y).

No path is reversed and no endpoint incidence is silently chosen. These are actual Hamilton puncture paths on the displayed supports.

### 2. Two HHH labels splice immediately to P_{k+1}
Suppose two distinct exterior labels y,z both realize QUIET-HHH. Then retain the two actual puncture paths

  K_y=(x_2,y,x_3,...,x_k),
  K_z=(x_2,z,x_3,...,x_k).

Boundary antisymmetry R3 on the physical triple {y,x_2,z} makes exactly one of

  (y,x_2,z),
  (z,x_2,y)

tight.

If (y,x_2,z) is tight, then

  (y,x_2,z,x_3,...,x_k)

is a literal tight path: its first turn is the tested R3 turn and every later turn is inherited from K_z. Its support has

  3+(k-2)=k+1

vertices, contradicting the uniform no-(k+1)-Hamiltonian condition. If the reverse tested turn is tight, use K_y instead and obtain

  (z,x_2,y,x_3,...,x_k),

the same contradiction.

Therefore at most ONE exterior label is QUIET-HHH relative to the fixed source path P.

### 3. Two TTT labels splice dually
Suppose distinct exterior labels y,z both realize QUIET-TTT. Retain

  L_y=(x_1,...,x_{k-2},y,x_{k-1}),
  L_z=(x_1,...,x_{k-2},z,x_{k-1}).

R3 on {y,x_{k-1},z} makes exactly one of

  (y,x_{k-1},z),
  (z,x_{k-1},y)

tight.

Appending the corresponding exterior label to the opposite puncture order gives one of

  (x_1,...,x_{k-2},y,x_{k-1},z),
  (x_1,...,x_{k-2},z,x_{k-1},y),

again a literal tight path on k+1 vertices. Contradiction.

Hence at most ONE exterior label is QUIET-TTT.

### 4. Global forcing count
There are exactly

  |V(H)-X|=k+1

exterior labels. Sections 2-3 allow at most two quiet labels total: one HHH and one TTT. Therefore at least

  k-1

exterior labels y are ACTIVE_y, meaning the accepted R961/SV304 analysis produces explicit source-anchored R435 geometry on Omega_y relative to the SAME retained source path P / its anchored packet.

Since k>=5, this gives at least four active exterior critical blocks. In particular at least one source-anchored R435 event exists. Therefore the entire uniform middle-layer branch CANNOT remain order-quiet around one fixed Hamilton source path.

This conclusion is stronger than local endpoint-jet or Hall activity: it applies to ANY fixed Hamilton source P and uses complete saturated critical blocks Omega_y, while preserving the exterior label y and the exact puncture path producing the event.

### 5. R927 compression
Accepted R927 gives the top-level alternative

  U: universal physical source crossing,
  M: uniform middle layer.

The present theorem upgrades M to

  M*: uniform middle layer + explicit source-anchored R435 geometry

on at least k-1 exterior critical blocks relative to any fixed Hamilton k-path P.

Thus a hypothetical smallest counterexample satisfies

  universal source crossing,
  OR a support-wide source-anchored Reverse-Ear family.

This is a genuine parent compression: the all-quiet uniform configuration is eliminated without solving endpoint Hall, near-maximal OUT/OUT, or K5 special cases separately.

### 6. Scope and next parent target
This is NOT O4 closure. Accepted R483 warns that generic R435 output is cheap, and the theorem does not yet convert these k-1 events into R561, a legal source repair, a spanning two-cover, or strict portal descent.

The next theorem should exploit the MULTIPLICITY and COMMON SOURCE:

- all active events are attached to one fixed P;
- each lives in a critical block X+y;
- the only quiet exceptional labels, if any, are source-anchored at opposite ends;
- every active y retains the exact R435 puncture path / reversed state / reverse trimer / proper cycle supplied by SV304.

A promising target is SOURCE-ANCHORED REVERSE-EAR ABSORPTION: among at least k-1 active exterior labels, two events sharing a physical old P-state or one endpoint role must combine to a P_{k+1}, full-support boundary reversal/R561, or a source-current support transfer. No such final consumer is claimed here.

Status: complete internal symbolic deduction from accepted R3, R961, the certified exact source-anchored section unit SV304, and Arm-M hypotheses. No R24/R5 is used.

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
        "revision_id": "R927"
    },
    {
        "relation": "dependency",
        "revision_id": "R961"
    }
]
```
