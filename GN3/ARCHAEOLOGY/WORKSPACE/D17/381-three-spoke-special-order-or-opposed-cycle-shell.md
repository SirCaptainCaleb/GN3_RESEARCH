# Three common-orientation spokes give the special P5 order or opposite local spoke cycles

**Workspace:** D17
**State:** established
**Key:** `three-spoke-special-order-or-opposed-cycle-shell`

**Summary:** For three spokes p,q,r with (a,s,c) tight, define tournaments T_a,T_c by x→_a y iff (x,a,y) is tight and x→_c y iff (x,c,y) is tight. Either some permutation (x,y,z) has x→_a y and y→_c z, yielding the literal Hamilton P5 (x,a,y,c,z), or both local tournaments are directed 3-cycles and T_c is exactly the reverse of T_a. In the latter branch, every T_a edge x→y certifies the two consecutive tight turns (x,a,y),(a,y,c), hence the Hamilton P4 (x,a,y,c), and also (a,y,c),(y,c,x), hence the Hamilton P4 (a,y,c,x). No tight C4 is claimed: the missing cyclic turn (c,x,a) is bad because (a,x,c) is retained tight. Thus the non-special obstruction is an opposite-local-cycle shell with paired Hamilton P4s, not a tight-cycle shell.

### 1. Local spoke tournaments
Let a,c,p,q,r be distinct vertices in a Strong Level-(1) boundary tournament and assume

  (a,p,c), (a,q,c), (a,r,c)

are tight. Put S={p,q,r}. Define two ordinary tournaments on S by

  x ->_a y  iff  (x,a,y) is tight,
  x ->_c y  iff  (x,c,y) is tight.

Boundary antisymmetry R3 makes each relation a tournament. A permutation (x,y,z) of S gives the special Hamilton order

  (x,a,y,c,z)

exactly when

  x ->_a y  and  y ->_c z,

because the middle turn (a,y,c) is one of the retained spoke turns.

### 2. No special order forces both local tournaments cyclic
Assume no permutation gives the special order. If T_a were transitive, let y be its sink. Then y has two T_a predecessors. T_c gives y some out-neighbor z; choose a T_a predecessor x distinct from z. Then x->_a y->_c z, contradiction. Hence T_a is a directed 3-cycle.

Dually, if T_c were transitive, let y be its source. It has two T_c out-neighbors. Choose one distinct from a T_a predecessor x of y, again giving x->_a y->_c z. Hence T_c is also a directed 3-cycle.

### 3. The two cycles are exact opposites
Fix y. Let x be the unique T_a predecessor of y and z the unique T_c successor of y. If x!=z, then x->_a y->_c z gives a special order. Therefore x=z for every y. Thus T_c is exactly the reverse directed cycle of T_a. After cyclic relabeling,

  p ->_a q ->_a r ->_a p,
  q ->_c p,  r ->_c q,  p ->_c r.

### 4. Valid path geometry in the opposite-cycle branch
Take any T_a edge x->_a y. Then

  (x,a,y),
  (a,y,c),
  (y,c,x)

are tight. Consequently the four-set {a,c,x,y} has at least the two literal Hamilton P4 orders

  (x,a,y,c),
  (a,y,c,x).

These are genuine path certificates and may be used with their displayed endpoint pairs.

There is NO tight four-cycle x-a-y-c-x. A tight four-cycle would additionally require (c,x,a), but retained source turn (a,x,c) is tight, so R3 makes (c,x,a) bad. Thus no cyclic-break consequences are licensed from this branch.

### 5. Dichotomy and scope
Exactly one of the following holds.

(SPECIAL) Some permutation (x,y,z) gives the literal Hamilton P5 (x,a,y,c,z).

(OPPOSITE-LOCAL-CYCLES) The local spoke tournaments at a and c are reverse directed 3-cycles. Each directed a-edge x->_a y yields the paired Hamilton P4s (x,a,y,c) and (a,y,c,x), while the would-be closing turn (c,x,a) is bad.

This classification uses only R3 and the three common-orientation spoke turns. It repairs the source-order gap exposed by SV94935 without asserting nonexistent tight C4s. It does not absorb either branch. R24 and R5 are unused.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    }
]
```
