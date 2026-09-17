# Four short pair-deletion fibers admit a strict one-vertex transfer out of the common complement

**Workspace:** D17
**State:** established
**Key:** `singleton-deep-p5-short-pair-support-transfer`

**Summary:** Inside the accepted six-vertex short G1 universe U of SV16094, two one-hole non-Hamiltonicity tests first force (t,q,p) and (t,v,u). Four explicit pair-deletion active four-sets are then simultaneously Hamiltonian and comparison-cyclic: deleting {s,q}, {s,u}, {q,t}, or {t,p} leaves respectively {t,p,u,v}, {q,t,p,v}, {s,p,u,v}, or {s,q,u,v}. Each has an explicit Hamilton P4 with literal complement B, and each contains an explicit directed comparison 3-cycle. For either endpoint b of the retained Hamilton order B, R887/R902 makes the five-set X+b Hamiltonian while B-b remains a literal path. Hence the same pair-deletion residue has a second exact cover (X+b)|(B-b). This is a strict one-vertex support transfer from B into the active rail, with both old and transferred exact representatives retained. No R435 payment, R159 payment, or endpoint synchronization is used.


### 1. Setup and two forced one-hole turns
Retain the accepted exact short-cell unit `singleton-deep-p5-short-r961-currentization` SV16094. Thus

  U={s,q,t,p,u,v}

is non-Hamiltonian, B is the common literal Hamilton complement, the old singleton row contains

  (s,v,u,p,q)|B  in H-t,

and SC.3-SC.4 of SV16094 give all of

  (s,v,u), (v,u,p), (u,p,q),
  (s,u,v), (v,t,q),
  (v,p,t), (p,t,v),
  (u,p,v),
  (v,s,u), (u,s,q), (q,s,v),
  (v,q,s), (s,q,t), (t,q,v),
  (q,t,p), (t,p,u), (p,u,s).

Two further turns follow from complete one-hole proposals, with no search or classification.

First, appending t to the actual U-t path (s,v,u,p,q) would Hamiltonize U if (p,q,t) were tight. Hence

  (p,q,t) is bad, so (t,q,p) is tight.                 (PT.1)

Now the six-vertex proposal

  (s,u,v,t,q,p)

has every turn tight except possibly (u,v,t): its other turns are (s,u,v), (v,t,q), and (t,q,p). Since U is non-Hamiltonian,

  (u,v,t) is bad, so (t,v,u) is tight.                 (PT.2)

These are the only extra signs needed below.

### 2. Four active four-sets are already Hamiltonian
For the following four deleted pairs, put X=U-{x,y}. The displayed order is a literal Hamilton P4 on X:

  {x,y}={s,q}:   X_sq={t,p,u,v},   A_sq=(t,v,u,p);
  {x,y}={s,u}:   X_su={q,t,p,v},   A_su=(v,t,q,p);
  {x,y}={q,t}:   X_qt={s,p,u,v},   A_qt=(s,v,u,p);
  {x,y}={t,p}:   X_tp={s,q,u,v},   A_tp=(q,s,v,u).

Indeed A_sq uses (t,v,u) from PT.2 and (v,u,p); A_su uses (v,t,q) and (t,q,p) from PT.1; A_qt uses (s,v,u),(v,u,p); and A_tp uses (q,s,v),(s,v,u).

Therefore for each row

  A_X | B

is a literal two-cover of H-{x,y}. It is exact: if H-{x,y} were Hamiltonian, that Hamilton path together with the vacuous tight dimer (x,y) would be a spanning two-cover of H.

### 3. The same four-sets contain explicit directed comparison cycles
Each X above also contains a directed comparison 3-cycle, using only turns retained in SV16094:

- X_sq={t,p,u,v}, at the ordinary p-star:

    (v,p,t), (t,p,u), (u,p,v),

  giving pv -> pt -> pu -> pv.

- X_su={q,t,p,v}, at the ordinary t-star:

    (v,t,q), (q,t,p), (p,t,v),

  giving tv -> tq -> tp -> tv.

- X_qt={s,p,u,v}, at the ordinary u-star:

    (v,u,p), (p,u,s), (s,u,v),

  giving uv -> up -> us -> uv.

- X_tp={s,q,u,v}, at the ordinary s-star:

    (v,s,u), (u,s,q), (q,s,v),

  giving sv -> su -> sq -> sv.

By accepted R887 these are literal directed cycles in the comparison orientation.

### 4. Either endpoint of B transfers into the active rail
Fix any one of the four rows and let b be either physical endpoint of the retained Hamilton order B. The induced five-set

  X+{b}

still contains the directed comparison cycle from Section 3. Accepted R902 says every non-Hamiltonian five-vertex boundary tournament is edge-orderable, while R887 says an edge-orderable cell has acyclic comparison orientation. Hence X+b is Hamiltonian. Choose an actual Hamilton path A_X^b on it.

Because b is an endpoint of the retained Hamilton B-order, deleting b leaves the literal tight path B-b. Thus

  A_X^b | (B-b)                                      (PT.3)

is a two-path cover of the same pair-deletion residue H-{x,y}.

If B were the singleton {b}, then A_X^b itself would Hamiltonize H-{x,y}, and the deleted dimer (x,y) would close H. Hence in the surviving counterexample branch B-b is nonempty. As above, H-{x,y} cannot itself be Hamiltonian, so (PT.3) is exact.

### 5. Strict support transfer
For every one of the four pair-deletion residues and for either endpoint b of B, retain simultaneously the exact representatives

  A_X | B,
  A_X^b | (B-b).

Their unordered support partitions differ by exactly one physical vertex:

  X | B   ->   (X+{b}) | (B-b).

Thus the short G1 critical universe has a branch-free strict one-vertex support transfer from the common complement into a five-vertex Hamilton active rail on four distinct pair-deletion fibers. The transferred Hamilton order A_X^b is kept actual but otherwise arbitrary; no endpoint role, selected reversed dimer, or R561 state is asserted.

This conclusion bypasses generic R435/R159/R542 payment. It is already one of the Director-v44 target progress types: a literal support-changing exact representative on one fixed pair-deletion residue. The next consumer may compare the two endpoint choices of b, exploit the actual b-to-X attachment in A_X^b, or use the surviving B endpoint stars from SV16094. It may not silently identify the transferred Hamilton order with A_X.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R887"
    },
    {
        "relation": "dependency",
        "revision_id": "R902"
    }
]
```
