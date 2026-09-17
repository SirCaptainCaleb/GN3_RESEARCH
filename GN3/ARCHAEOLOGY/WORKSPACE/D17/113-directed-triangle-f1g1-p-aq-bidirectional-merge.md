# The P | (A union Q) fragmented-B split has a bidirectional active-merge blocker

**Workspace:** D17
**State:** established
**Key:** `directed-triangle-f1g1-p-aq-bidirectional-merge`

**Summary:** In the v42 t=3 fragmented-B support split P | (A union Q), write the current whole active blocks as a tight trimer P_T=(p0,p1,p2) and a Hamilton four-path Z_T=(z0,z1,z2,z3). Either concatenation P_T Z_T or Z_T P_T, if its complete two-turn junction window passes, Hamiltonizes all seven active labels and with the retained literal B gives the desired exact H-{u,v} representative. Thus an unresolved cell blocks both directions, yielding one exact reversed free-boundary witness from each two-turn window. Because |P|=3, the P-side endpoint-transposition certificate of SV14216 is simultaneously pinned to the physical B|P attachment. Outside explicit same-support R435 order activity, P_T is the literal (j0,j1,m) and Z_T is the literal L=(a,b,c,x); then the P_T Z_T window is already blocked at its first seam by the ancestral F1G1 G1 failure (j1,m,a), so only the opposite L P window {(c,x,j0),(x,j0,j1)} is new. Its first-bad alternatives retain either the dual-Q common-source fork (j0,c,x),(j0,x,c), or the two-continuation fork (j1,j0,c),(j1,j0,x) together with (c,x,j0). This is a structured two-ended blocker, not closure or generic packet payment.

### 1. Exact v42 support split
Retain the exact F1G1 t=3 fragmented-B cell of SV14216 and specialize to the active support distribution

  P | (A union Q),

where P={j0,j1,m}, A={a,b}, Q={c,x}. Let the two whole active blocks in the actual exact target cover T of G=H-{u,v} have their ACTUAL tight orders

  P_T=(p0,p1,p2),
  Z_T=(z0,z1,z2,z3),

with V(P_T)=P and V(Z_T)=A union Q. The two B-fragments and both physical B|active attachments remain exactly as in T; no statement about their ancestral B-order is made.

Because the P-side active block has exactly three vertices, the inward certificate of the endpoint-transposition gate in SV14216 is pinned to the physical B|P attachment. If P_T is terminal on its mixed rail, the SV14216 window (...,r,s,h,e) has s,h,e equal to the three P vertices and r equal to the touched B endpoint, so r->s is the actual B->P transition. If P_T is source, the dual first-four window has its inward state s->r equal to the actual P->B transition. Hence every non-success P-side gate already returns DF or MX geometry on one of the two v42 physical B contacts.

### 2. Both active concatenations are complete two-turn tests
Test the two Hamilton concatenations of the ACTUAL active block orders.

First,

  M_PZ=(p0,p1,p2,z0,z1,z2,z3).

Its complete new-turn window is exactly

  lambda_1=(p1,p2,z0),
  lambda_2=(p2,z0,z1).

Every other turn is inherited from P_T or Z_T. If both lambda turns are tight, M_PZ is a Hamilton path on all seven active labels. Together with the retained literal Hamilton path B on the disjoint complement this gives

  M_PZ | B

as an exact two-cover of H-{u,v}. This is precisely the desired literal-B codimension-two currentization, so an unresolved cell must block the window. Under deterministic FIRST-BAD normalization:

  PZ1: lambda_1 bad, hence (z0,p2,p1) tight;
  PZ2: lambda_1 tight and lambda_2 bad, hence (z1,z0,p2) tight.

Thus the failed P->Z merge retains either a named witness on the reverse terminal dimer of P_T or a named witness on the reverse source dimer of Z_T.

Second,

  M_ZP=(z0,z1,z2,z3,p0,p1,p2).

Its complete new-turn window is

  rho_1=(z2,z3,p0),
  rho_2=(z3,p0,p1).

Again, full success gives M_ZP|B, the desired literal-B exact pair-deletion representative. Hence the unresolved cell blocks this window as well. FIRST-BAD gives

  ZP1: rho_1 bad, hence (p0,z3,z2) tight;
  ZP2: rho_1 tight and rho_2 bad, hence (p1,p0,z3) tight.

Therefore the SAME exact fragmented-B target carries, in addition to its two physical B attachments and the P-side contact certificate from Section 1, a blocker from EACH direction of active merging. These are free-boundary blockers on the actual active block orders. No R523/R542 payment is taken.

### 3. R435-quiet current orders reduce the new work to one two-turn window
Compare P_T with the retained literal trimer

  P=(j0,j1,m)

and compare Z_T with the retained locked Hamilton path

  L=(a,b,c,x).

Both comparisons are on identical supports. By accepted R435/P448, outside explicit same-support order activity the current contact order is increasing relative to the reference order. Since every vertex of each support is a contact, the quiet case forces literal equality

  P_T=(j0,j1,m),
  Z_T=(a,b,c,x).

This is only a normalization of the R435-quiet subcell; the R435-active alternatives remain structured outputs and are not called progress by themselves.

In this quiet subcell the P->Z merge is

  (j0,j1,m,a,b,c,x),

whose first junction turn is exactly

  (j1,m,a).

But F1G1 means the ancestral G1 first seam (j1,m,a) is bad. Hence the P->Z active merge is already blocked with the retained reverse turn

  (a,m,j1) tight.

The only genuinely new active-merge test is therefore the opposite concatenation

  (a,b,c,x,j0,j1,m),

with complete window

  h_1=(c,x,j0),
  h_2=(x,j0,j1).

At least one is bad. FIRST-BAD gives exactly two subcells.

### 4. The two quiet first-bad outputs retain the old wrap ancestry
The simultaneous-wrap-failure parent SV11804 already retains

  (j0,c,x),
  (j1,j0,c)

tight.

If h_1 is bad, R3 gives

  (j0,x,c) tight.

Thus on the three-support {j0,c,x} both terminal Q orientations are realized from the common source j0:

  (j0,c,x),  (j0,x,c).

Neither corresponding reverse boundary can start a Hamilton trimer on this same support: (x,c,j0) is the complete reverse of the already-tight (j0,c,x), while (c,x,j0)=h_1 is bad. Retain this as the dual-Q common-source boundary lock; it is stronger data than one anonymous reversed seam.

If h_1 is tight and h_2 is bad, R3 gives

  (j1,j0,x) tight.

Together with the old wrap turn (j1,j0,c), the reverse ancestral source dimer j1->j0 has TWO named tight continuations c and x, while h_1=(c,x,j0) is also tight. Retain this two-continuation fork with the actual Q orientation and the old reverse-boundary P4 ancestry. No claim is made that this same-polarity fork is itself R561 or closure.

### 5. Scope
This section only treats the v42 support split P | (A union Q). It proves a legal simultaneous two-direction active-merge test and identifies the exact failure geometry. It does not consume the resulting DF/MX plus merge-blocker state, does not assume any order on B1,B2, and does not extend to the other two 1+2 support distributions or to t>=4. Its useful output is that the P-side physical B contact and both free active merge directions are now simultaneously currentized, with the F1G1 G1 blocker reused in the quiet literal-order subcell rather than respent as generic sign currency.

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
    }
]
```
