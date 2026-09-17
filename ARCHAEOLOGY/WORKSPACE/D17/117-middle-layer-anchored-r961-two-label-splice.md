# Two equal source-anchored R961 roles force a forbidden middle-layer extension

**Workspace:** D17
**State:** established
**Key:** `middle-layer-anchored-r961-two-label-splice`

**Summary:** Fix a Hamilton k-path P=(x_1,...,x_k) in the uniform middle-layer residue. At most one exterior label can realize the fully P-quiet source-anchored HHH packet, and at most one can realize the fully P-quiet TTT packet. Two HHH labels y,z supply the puncture paths (x_2,y,x_3,...,x_k) and (x_2,z,x_3,...,x_k); exactly one of the reversal pair (y,x_2,z),(z,x_2,y) is tight, giving a literal P_{k+1}. The terminal-dual argument handles TTT. Thus among the k+1 exterior critical blocks relative to fixed P, all but at most two must emit explicit source-relative R435 geometry. This is a compression theorem, not an R435 consumer.

### Setup
Work in the accepted R927 uniform middle-layer residue with k>=4: |V(H)|=2k+1, every k-set is Hamiltonian, and every (k+1)-set is non-Hamiltonian. Fix one actual Hamilton order

  P=(x_1,x_2,...,x_k)

on a k-support X. Let y,z be distinct vertices outside X. Use the accepted source-anchored R961 theorem for the critical blocks X+y and X+z.

### Two HHH anchors cannot coexist
Suppose both exterior labels y,z realize the fully P-quiet source-anchored HHH packet. The exact anchored normal form supplies, among the puncture paths,

  L_y=(x_2,y,x_3,...,x_k),
  L_z=(x_2,z,x_3,...,x_k).

The ordered triples (y,x_2,z) and (z,x_2,y) are complete reversals. By boundary antisymmetry exactly one is tight. If (y,x_2,z) is tight then

  (y,x_2,z,x_3,...,x_k)

is a literal tight path: its first turn is the chosen tight reversal-pair member and every later turn is inherited from L_z. If instead (z,x_2,y) is tight, then

  (z,x_2,y,x_3,...,x_k)

is tight by the same argument using L_y. In either case the path has vertex set

  (X-{x_1}) union {y,z}

of order k+1, contradicting the uniform residue. Hence at most one exterior label can be fully source-anchored quiet HHH relative to P.

### TTT dual
If y,z are both fully P-quiet source-anchored TTT labels, the exact terminal normal form supplies

  R_y=(x_1,...,x_{k-2},y,x_{k-1}),
  R_z=(x_1,...,x_{k-2},z,x_{k-1}).

Exactly one of the reversal pair (y,x_{k-1},z),(z,x_{k-1},y) is tight. Appending the corresponding exterior label to the opposite puncture order gives one of

  (x_1,...,x_{k-2},y,x_{k-1},z),
  (x_1,...,x_{k-2},z,x_{k-1},y),

a literal tight path on k+1 vertices. Thus at most one quiet TTT label exists.

### Consequence
There are k+1 exterior labels outside X. For each critical block X+p, the source-anchored theorem yields either explicit source-relative R435 geometry or one of the two quiet anchored types above. Since each quiet type occurs for at most one label, at least k-1 exterior labels force explicit source-relative R435 geometry against the fixed P packet.

This is strictly stronger than merely knowing that R435 events are abundant: it eliminates all repeated quiet constant-role behavior across distinct exterior critical blocks. It does NOT consume the remaining R435 majority; R483 still forbids treating generic Reverse-Ear existence as closure. The next parent target is to synchronize the one-hole R435 events across these k-1 labels into a fixed-support R561 boundary reversal or a two-label P_{k+1}.

Status: complete symbolic deduction from the accepted source-anchored R961 normal form and boundary antisymmetry; working/established exposition, not a canonically reviewed standalone claim.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R927"
    },
    {
        "relation": "dependency",
        "revision_id": "R435"
    },
    {
        "relation": "dependency",
        "revision_id": "R961"
    }
]
```
