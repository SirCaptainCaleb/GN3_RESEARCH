# The same-break same-side cycle-dimer residue exits by one wrap test

**Workspace:** D17
**State:** established
**Key:** `compatible-forest-cycle-dimer-same-side-wrap-extinction`

**Summary:** Retain the quiet residue of SV30888. Normalize the common cyclic break as R=(r0,...,b) and the two singleton-deletion active paths as P_x=(R,x), P_y=(R,y), with common fixed complement V and Omega=Q+x+y non-Hamiltonian; the head-attached case is dual. Since P_y certifies the tail seam into y, tightness of (x,r0,r1) would make (x,R,y) Hamiltonian on Omega, so that wrap seam is bad. Apply accepted R548 to P_x. If its other wrap seam (b,x,r0) is bad, R548 gives the literal reverse P4 (r1,r0,x,b); R4 then supplies an exact two-cover of its complement, so the P4 lifts to an actual maximum three-forest. If (b,x,r0) is tight, the cyclic rotation P_x*=(r1,...,b,x,r0) is Hamiltonian on Q+x. Its Q-contact order uses a different break from P_y, hence comparison P_x* versus P_y is R435-nonquiet. The exchanged label x is internal in P_x*, so any adjacent selected-reversal output lies in the internal branch of SV27136 and produces a fresh maximum-three-forest portal; reverse-trimer and proper-cycle outputs are already routed by SV26759 and SV25652. Therefore the quiet same-side cycle-dimer two-row residue cannot remain terminal: one wrap test exports it to a universal one-extension four-set or actual/closed maximum-three-forest dynamics. Together with SV30888, the entire SV30097 two-row singleton branch is exported to the G10 global holonomy programs.


### 1. Same-break same-side quiet residue
Retain the R435-quiet residue of `compatible-forest-cycle-dimer-two-row-r435-reduction` SV30888. Thus Q is one fixed oriented tight cycle, V is a common literal Hamilton complement, and

  H-y=P_x|V,
  H-x=P_y|V

are exact singleton-deletion two-covers on the active non-Hamiltonian support

  Omega=V(Q) union {x,y}.

The Q contacts of P_x and P_y use the same cyclic break and x,y attach on the same side. Normalize the TAIL-attached case as

  R=(r_0,r_1,...,r_{m-1})=(r_0,...,b),
  P_x=(r_0,r_1,...,b,x),
  P_y=(r_0,r_1,...,b,y).                                 (SW.1)

The HEAD-attached case is the exact reversal-dual argument with path ends exchanged.

### 2. The other singleton row blocks one wrap of P_x
Because P_y is tight, its terminal seam gives

  (r_{m-2},b,y) tight                                    (SW.2)

when m>=2; for the order-three cycle this notation is still literal with r_{m-2}=r_1. All internal turns of R are inherited from Q.

Test the turn

  alpha=(x,r_0,r_1).                                     (SW.3)

If alpha were tight, then

  (x,r_0,r_1,...,b,y)                                    (SW.4)

would be a Hamilton tight path on Omega: the first turn is alpha, every internal R-turn is inherited, and the last turn is the certified seam (SW.2). This contradicts the retained non-Hamiltonicity of Omega. Therefore

  (x,r_0,r_1) is bad.                                    (SW.5)

By R3 its complete reversal (r_1,r_0,x) is tight.

### 3. Apply the one remaining R548 wrap test
Apply accepted R548 to the Hamilton path P_x in (SW.1). The head cyclic rotation

  (x,r_0,r_1,...,b)

is blocked exactly by (SW.5). The only remaining possible successful rotation is

  P_x^*=(r_1,r_2,...,b,x,r_0),                           (SW.6)

whose unique new seam is

  beta=(b,x,r_0).                                        (SW.7)

If beta is bad, R548/R3 gives

  (r_0,x,b) tight.                                       (SW.8)

Together with the already retained reverse turn (r_1,r_0,x), this yields the literal tight P4

  K=(r_1,r_0,x,b).                                       (SW.9)

K is proper because the common complement V is nonempty. Accepted R4/P601 gives an exact two-cover of H-V(K), and adjoining K produces an actual maximum spanning three-forest of H. Thus double wrap failure exits directly to current representative dynamics.

### 4. Successful wrap forces productive neighboring-support activity
Suppose instead beta is tight. Then R548 certifies the rotated Hamilton path P_x^* in (SW.6) on V(Q) union {x}.

The Q contacts of P_x^* occur in cyclic order

  r_1,r_2,...,b,r_0,

whereas P_y retains

  r_0,r_1,...,b.                                        (SW.10)

These are distinct complete linearizations of the same cyclic order, so the Q contacts cannot be monotone. Accepted R435 therefore emits explicit nonquiet geometry in the comparison P_x^* versus P_y.

The exchanged label x is strictly internal in P_x^*: it lies between b and r_0. Hence if R435 emits an adjacent selected-state reversal, the endpoint-endpoint branch of SV27136 is impossible. The internal branch of SV27136 gives an exact pair-deletion two-cover crossing the corresponding trim and an actual maximum-three-forest lift.

If R435 emits a reverse seam trimer, SV26759 gives a universally one-extendable four-set or a fresh maximum three-forest. If it emits a proper tight cycle, SV25652 gives a closed movable-break maximum-three-forest orbit.

Thus successful wrap also exits to the global small-core or maximum-forest holonomy programs.                        (SW.11)

### 5. Extinction of the quiet two-row residue
Both values of the sole remaining wrap test beta are productive. Therefore the same-break same-side quiet residue of SV30888 cannot remain terminal.

Combining with SV30888, the entire two-row fixed-complement cylinder exported by SV30097 reaches

  UNIVERSAL ONE-EXTENSION FOUR-SET,
  or FRESH MAXIMUM THREE-FOREST,
  or CLOSED MOVABLE-BREAK MAXIMUM-FOREST ORBIT.          (SW.12)

The HEAD-attached case is dual. This theorem does not absorb the universal core or extinguish the resulting global representative orbit, so it does not by itself close O4.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R4"
    },
    {
        "relation": "dependency",
        "revision_id": "R435"
    },
    {
        "relation": "dependency",
        "revision_id": "R548"
    }
]
```
