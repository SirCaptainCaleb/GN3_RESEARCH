# The three-arm bicyclic theta is impossible by a clean short-fiber reduction

**Workspace:** D17
**State:** established
**Key:** `singleton-cover-union-three-arm-theta-exclusion`

**Summary:** R24-free replacement of historical SC17/SV4060. Crossed traversal closes except the 1+1 residue, where clean R594+R880 force the opposite C rail to order at least seven and an internal C-deletion row has no legal orientation. Parallel traversal makes both bridged interiors order at most two by R3; 1+1, 1+2, 2+1 close directly. In 2+2, direct singleton-row floor gives |C|>=3; |C|=3 contradicts R594+R880, internal deletion restoration forbids C-branch and same-arm omissions, the c2 row forces |C|=4, and c2/c3 rows cross-splice. Clean deps R3,R594,R880 with exact separator-row ancestry SV3158.

### Status and clean input
This is an R24-free replacement of the historically certified section SV4060. The old exact unit and SC17 certification remain historical provenance; they are not used below.

Let U be the selected-edge union of a chosen singleton-cover family in a hypothetical smallest counterexample. Assume U is 2-connected, beta(U)=2, and its degree-three branch vertices p,q satisfy c(U-{p,q})=3. Let A,B,C be the three nonempty theta-arm interiors. By exact separator-row unit SV3158, A,B,C are Hamilton atoms. Different p/q connector pairs already close H, so relabel with C_p=(A-q-B)|C, and let C_q join the same A,B atoms through p. Every atom Hamilton order is its physical arm order up to reversal.

We use one clean consequence of the modern short-fiber reconstruction. If an exact singleton-deletion row H-z=P|Q has |P|<=3, R594 closes |P|=1,2 and reduces the only surviving case to |P|=3 with Q=(q_0,...,q_m), m>=4. Accepted R880 eliminates m=4,5. Hence

  |P|=3  implies  |Q|>=7.                              (T.1)

No R24 or R5 is used in (T.1).

We also need the elementary singleton-row floor. In any exact H-z=P|Q, both rails have order at least three. A singleton P={u} lets the dimer (z,u) pair with Q. If P=(u,v), R3 makes exactly one of (z,u,v),(v,u,z) tight, again pairing a trimer on {z,u,v} with Q.

### 1. Crossed traversal
Orient every physical arm from p to q. In C_p, A is traversed p-to-q and B q-to-p. Suppose C_q has crossed atom order B-p-A, so it traverses both B and A in those same directions.

If |B|>=2, A-q-B-p is tight and Hamiltonizes A+B+p+q, pairing with C. If |B|=1 and |A|>=2, the dual B-p-A-q closes. Thus only |A|=|B|=1 remains. Write A={a},B={b}. Then C_p has trimer rail (a,q,b) opposite C, so (T.1) gives |C|>=7. Write C physically as p-c_1-...-c_t-q, t>=7.

C+q is non-Hamiltonian, since a Hamilton path there would pair with the crossed C_q trimer (b,p,a). Thus

  (c_{t-1},c_t,q) is bad.                              (T.2)

Delete c_3. The theta U has n+1 selected-union edges on n vertices. U-c_3 therefore has n-1 vertices and n-1 edges, while an exact two-path row selects n-3 edges. Exactly two U-c_3 edges are omitted. Since p,q each retain degree three, one omitted edge is incident with p and one with q.

Neither omitted edge can be p-c_1 or q-c_t. If p-c_1 is omitted, c_1-c_2 is an isolated selected rail; R3 on {c_1,c_2,c_3} restores c_3 to that rail in one orientation, producing a spanning two-cover with the untouched rail. The q-side is dual. Nor can both omissions be the two ends of A or of B: that isolates singleton a or b, which absorbs c_3 as a dimer and again closes H.

Hence the omissions are crossed between A and B. In either pattern the q-component has underlying order

  x-q-c_t-c_{t-1}-...-c_4,   x in {a,b}.               (T.3)

Oriented from x toward c_4, it contains a complete reversal of a physical tight C-triple because t>=7. The reverse orientation contains the bad turn (T.2). So (T.3) has no legal tight orientation, contradiction.

### 2. Parallel traversal and the short profiles
Thus C_q has parallel atom order A-p-B. Relative to C_p, both A and B are traversed in complete reverse orders. If |A|>=3, a consecutive physical A triple and its complete reversal are both selected tight turns, contradicting R3. Hence |A|<=2, and similarly |B|<=2. The elementary singleton-row floor gives |A|+|B|+1>=3 and |C|>=3. The profiles are 1+1, 1+2, 2+1, 2+2.

For 1+1, write A={a},B={b}. The rows contain (a,q,b) and (a,p,b). R3 on (p,a,q)/(q,a,p) makes one tight, so one of (p,a,q,b),(q,a,p,b) is a Hamilton P4 and pairs with C.

For 1+2, write A={a} and B=p-b_1-b_2-q. The mixed rails are a,q,b_2,b_1 and a,p,b_1,b_2. The candidates

  (p,a,q,b_2,b_1),   (q,a,p,b_1,b_2)

have only the reversal-pair holes (p,a,q),(q,a,p); R3 makes one tight. The 2+1 case is dual.

### 3. Internal C-deletion lemma in the 2+2 profile
It remains that A=p-a_1-a_2-q and B=p-b_1-b_2-q, with

  C_p=(a_1,a_2,q,b_2,b_1)|C,
  C_q=(a_2,a_1,p,b_1,b_2)|C.                           (T.4)

Write C=p-c_1-...-c_t-q, t>=3.

For any internal deletion c_k, 2<=k<=t-1, the same edge count shows exactly two U-c_k edges are omitted, one incident with p and one with q. Neither p-c_1 nor q-c_t can be omitted. If p-c_1 is omitted, the selected left C segment c_1,...,c_{k-1} is an isolated rail. For k=2 it is a singleton and absorbs c_k as a dimer. For k=3 it is a dimer and absorbs c_k through the inherited C turn. For k>=4, the isolated segment must be oriented in the physical C direction, since its reverse contains a reversed physical C triple; appending c_k then uses the inherited C turn. Every case restores c_k and closes H. The q-side is dual.

Nor can the two omissions be both ends of A or both ends of B. That isolates the corresponding dimer, and R3 on that dimer with c_k supplies a tight trimer restoring c_k. Therefore only the crossed omission patterns remain:

  X: omit p-a_1 and q-b_2,
  Y: omit p-b_1 and q-a_2.                              (T.5)

### 4. The 2+2 profile forces |C|=4
If t=3, C is a trimer rail in exact singleton row C_p and the opposite mixed rail has order five, contradicting (T.1), which requires the opposite rail to have order at least seven. Hence t>=4.

Both C+p and C+q are non-Hamiltonian, since they would pair with the opposite mixed rails in (T.4). Thus

  (p,c_1,c_2) bad,   (c_{t-1},c_t,q) bad.               (T.6)

Delete c_2. Under Y the B/right-C component has underlying order b_1-b_2-q-c_t-...-c_3. Its displayed orientation contains (b_1,b_2,q), the reversal of selected tight (q,b_2,b_1) from C_p; the reverse orientation contains the bad turn (c_{t-1},c_t,q). Hence Y is impossible and X is forced.

Under X the A/right-C component has underlying order a_1-a_2-q-c_t-...-c_3. Its reverse contains (q,a_2,a_1), the reversal of selected tight (a_1,a_2,q), so the actual orientation is the displayed one. If t>=5 it contains the reversed physical C triple (c_t,c_{t-1},c_{t-2}), impossible by R3. Hence t<=4, so t=4.

For C=(c_1,c_2,c_3,c_4), the actual c_2 row is

  R_2=(a_1,a_2,q,c_4,c_3),
  S_2=(c_1,p,b_1,b_2).                                  (T.7)

### 5. Final c2/c3 cross-splice
Delete c_3. Again only X,Y remain. Under Y one component has underlying order a_2-a_1-p-c_1-c_2. The displayed orientation contains bad (p,c_1,c_2); its reverse contains (p,a_1,a_2), the reversal of selected tight (a_2,a_1,p) from C_q. Thus Y is impossible. X is forced, with actual rails

  R_3=(a_1,a_2,q,c_4),
  S_3=(c_2,c_1,p,b_1,b_2).                              (T.8)

Now R_2 from the c_2 row and S_3 from the c_3 row are vertex-disjoint actual tight paths whose supports partition V(H). Thus R_2|S_3 is a spanning two-cover, contradiction.

### Consequence and dependency repair
No hypothetical smallest counterexample can have a three-component beta-two theta selected-edge union.

Historical SC17/SV4060 used R24 to kill crossed 1+1, impose a four-vertex mixed-rail floor, and force |C|>=4 / forbid an isolated three-vertex C segment. The direct R3 singleton-row argument replaces the easy floor; R594+R880 replace the genuinely difficult trimer-fiber use; and the internal C-deletion restoration lemma eliminates branch-edge and same-arm omissions directly.

The clean theorem dependencies are R3,R594,R880. Exact separator-row provenance is SV3158. R24,P22,R5 and their descendants are absent from the proof.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R594"
    },
    {
        "relation": "dependency",
        "revision_id": "R880"
    },
    {
        "relation": "related",
        "revision_id": "R24"
    }
]
```
