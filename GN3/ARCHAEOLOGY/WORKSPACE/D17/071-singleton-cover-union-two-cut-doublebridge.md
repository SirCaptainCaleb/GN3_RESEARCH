# Three-component 2-cut: R24-free fixed-complement packets with one explicit crossed atom cell

**Workspace:** D17
**State:** established
**Key:** `singleton-cover-union-two-cut-doublebridge`

**Summary:** R24-free replacement of the old SC12 double-bridge argument. From the separator equality row, synchronize the two bridged Hamilton atoms by R435. A direct R3 argument proves that every rail of an exact singleton-deletion two-cover has order at least three. Hence every crossed quiet row closes by bridge concatenation except the single cell |A|=|B|=1, which is retained explicitly as the selected K_{2,2} bridge core a-q-b-p-a. In both the parallel row and this crossed singleton-singleton cell, C+p and C+q are non-Hamiltonian and the same p,q witnesses sign both reverse endpoint dimers of a retained Hamilton C-order, yielding dual R542/R696 packets with |C|>=3. If U has a cut vertex, use the clean critical-block normal form; otherwise {p,q} is a minimum equality separator and both p,q have actual selected returns into C by the accepted minimum-incidence unit. No R24 premise is used.

### Input and clean structural fork
Retain the three-component equality 2-cut from `singleton-cover-union-separator-row`. Thus, after relabelling,

  U-{p,q}=A disjoint_union B disjoint_union C

with A,B,C Hamilton components and actual singleton rows

  C_p=(A_q-q-B_q) | C_p^C,
  C_q=(A_p-p-B_p) | C_q^C,

where the two connector labels join the same unordered atom-pair A,B and C is the fixed Hamilton complement.

The selected-edge union U is connected by `singleton-cover-union-disconnection`: a disconnected U already closes H by two Hamilton component paths. If U has a cut vertex, stop and retain the clean output of `singleton-cover-union-block-normal-form`: two overlapping non-Hamiltonian deletion-Hamiltonian critical blocks meeting in that articulation vertex. Hence the genuinely 2-cut branch below may assume that U has no cut vertex.

Under that assumption {p,q} is a minimum-cardinality nonempty equality separator. Indeed it attains c(U-{p,q})=3=|{p,q}|+1, while a singleton equality set would be a cut vertex. Therefore the accepted minimum-equality-incidence unit applies: both p and q have actual U-adjacencies, hence actual selected states in the chosen singleton-cover family, into each of A,B,C. In particular, besides the displayed A/B bridge rows, there is a selected p-C return and a selected q-C return somewhere in the family. These returns are retained as physical ancestry; no claim is made that they already lie in either displayed row.

### Clean singleton-row floor: every rail has order at least three
We use only boundary antisymmetry R3. Let

  H-z=P | Q

be any exact singleton-deletion two-cover in a hypothetical counterexample.

If |P|=1, say P={u}, the vacuous tight dimer (z,u) together with Q is a spanning two-cover of H, contradiction.

If |P|=2, write P=(u,v). Of the two complete reversals (z,u,v) and (v,u,z), R3 makes one a tight trimer. That trimer spans {z,u,v}; together with the untouched rail Q it is a spanning two-cover of H, contradiction.

Thus |P|>=3, and symmetrically |Q|>=3. In particular every displayed complement rail C has order at least three. This is the only rail-size input used below.

### Synchronize the two bridged atoms
Compare A_q with A_p and B_q with B_p using accepted R435 path-order comparison. If either comparison emits an adjacent selected reversal, a reverse tight trimer, or a proper tight cycle, retain that source-labelled R435 geometry together with the physical connector labels p,q and fixed Hamilton complement C.

In the R435-quiet branch the literal Hamilton orders agree. Write

  A=(a_0,...,a_r),  B=(b_0,...,b_s)

for these common orders and normalize

  C_p=(A-q-B)|C.

The mixed rail of C_q has exactly one of the two orientations

  A-p-B  or  B-p-A.

### Crossed orientation: all but one atom cell closes
Suppose the C_q mixed rail is B-p-A.

If |B|>=2, concatenate

  A-q-B-p.

Every turn through A-q-B is selected in C_p. The final B-p seam is selected in C_q because B-p-A is a literal tight path and B has at least two vertices, so its terminal B-state supplies that turn. Hence A-q-B-p is Hamiltonian on A union B union {p,q}. Pair it with the Hamilton C-rail of C_p to obtain a spanning two-cover of H.

If |B|=1 and |A|>=2, use instead

  B-p-A-q.

The initial B-p-A part is selected in C_q and the final A-q seam is selected in C_p; again this is a Hamilton path on A union B union {p,q}, disjoint from a Hamilton path on C.

Therefore a crossed quiet row can survive only when

  |A|=|B|=1.

Write A={a}, B={b}. The two mixed rails are then the literal tight trimers

  (a,q,b),  (b,p,a),

and their selected adjacencies form the four-cycle

  a-q-b-p-a.

This CROSSED SINGLETON-SINGLETON K_{2,2} CELL is retained explicitly. R3 alone does not eliminate it, and this replacement does not pretend otherwise.

### Parallel row and crossed K_{2,2} cell share the same complement packets
There are now two quiet survivors:

PARALLEL:
  C_p=(A-q-B)|C,
  C_q=(A-p-B)|C_q^C;

or the explicit crossed singleton-singleton cell
  C_p=(a-q-b)|C,
  C_q=(b-p-a)|C_q^C.

In either survivor both C+p and C+q are non-Hamiltonian. If C+p were Hamiltonian, pair such a Hamilton path with the full mixed rail A-q-B from C_p (with A={a},B={b} in the exceptional cell). These paths are disjoint and span H. If C+q were Hamiltonian, pair it with the full C_q mixed rail A-p-B in the parallel case or b-p-a in the exceptional crossed case. Again H would have a spanning two-cover.

Fix the retained literal Hamilton order from C_p,

  C=(c_0,c_1,...,c_t),

where t>=2 by the clean singleton-row floor above.

Since C+p is non-Hamiltonian, prepending p to this C-order fails at its only new initial turn. Thus (p,c_0,c_1) is bad and R3 gives

  (c_1,c_0,p) tight.

The same argument with q gives

  (c_1,c_0,q) tight.

Hence the reverse initial dimer

  S_L=(c_1,c_0)

of the tight carrier K_L=(c_0,c_1,c_2) has the two distinct same-polarity witnesses p,q.

At the other end, appending p to C fails at (c_{t-1},c_t,p), so R3 gives

  (p,c_t,c_{t-1}) tight,

and similarly

  (q,c_t,c_{t-1}) tight.

Thus the reverse terminal dimer

  S_R=(c_t,c_{t-1})

of K_R=(c_{t-2},c_{t-1},c_t) has the same witness pair p,q. When |C|=3 the two trimer carriers coincide, but the two boundary dimers and their signs remain well-defined; no fourth C-vertex is needed.

Accepted R542 therefore applies independently at both endpoints, and accepted R696 gives the corresponding pair-deletion refinements. The two packets coexist graph-intrinsically with the same distinguished witnesses p,q.

Because we are in the no-cut-vertex branch, the minimum-equality-incidence unit additionally retains actual selected p-C and q-C returns elsewhere in the chosen singleton family. These are physical selected states, not support-only placeholders, but no same-row currentization is asserted here.

### R24-free parent residue
Thus the three-component equality 2-cut admits the following R24-free alternatives:

1. a spanning two-cover of H;
2. a cut-vertex critical-block normal form from the clean block-normal-form unit;
3. explicit source-labelled R435 geometry on one bridged Hamilton atom; or
4. a fixed-complement quiet bridge cell carrying dual R542/R696 endpoint packets with common witnesses {p,q}, where the bridge orientation is parallel except for the single explicit crossed cell |A|=|B|=1. In the no-cut branch, both bridge labels also have actual selected returns into C in other singleton fibers.

This replaces the old use of R24 exactly. The previous stronger sentence “crossed quiet orientation is impossible” is not retained in the singleton-singleton atom cell. The downstream consumer should either absorb that finite K_{2,2} bridge core or exploit the same dual endpoint packets and cross-fiber returns already present there.

Status: complete R24-free working deduction from the accepted clean units and R3,R435,R542,R696. It supersedes the current exposition of this stable section key but does not retroactively alter the historical SC12 certification of SV3446; the new exact section version requires independent review.

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
        "revision_id": "R542"
    },
    {
        "relation": "dependency",
        "revision_id": "R696"
    }
]
```
