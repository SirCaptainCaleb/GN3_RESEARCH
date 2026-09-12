# A quiet neighboring puncture exchange is a local swap arrow, a one-sided fan, or a universal extension four-set

**Workspace:** D17
**State:** established
**Key:** `fixed-complement-quiet-neighbor-slot-core-or-swap`

**Summary:** Let A be a non-Hamiltonian active support and let P_a,P_b be Hamilton paths on A-a and A-b whose common A-{a,b} vertices occur in one literal order, as in an R435-quiet neighboring-support comparison. Then P_a and P_b are obtained by inserting b and a into one common order K, and their insertion slots are equal or adjacent; separated slots would combine to a Hamilton path on A. For adjacent slots across a common vertex u, the unique mixed turn needed to insert both labels must be bad, so R3 forces the reverse local swap turn through u. For the same internal gap u|v, test the two double-insertion orders u,a,b,v and u,b,a,v. If their forced failures occur on opposite sides of the gap, the reversals together with the inherited u-a-v or u-b-v turn form a directed comparison triangle on {u,v,a,b}; hence by R902 this four-set Hamilton-extends after adjoining every exterior vertex. If both failures occur on the left, the physical edge ab has the two outgoing comparison arcs ab->au and ab->bu; if both occur on the right, it has the two incoming arcs av->ab and bv->ab. Boundary same-gap cells give the corresponding one-sided fan directly. Thus an R435-quiet neighboring live-puncture transition has an order-free core-or-oriented-swap normal form.

### 1. Neighboring quiet puncture rows
Let H be a hypothetical smallest Strong Level-(1) counterexample. Let A be a non-Hamiltonian vertex set and let a,b be distinct vertices of A. Retain Hamilton paths

  P_a on A-a,
  P_b on A-b,

and assume their R435 comparison is quiet. Therefore the common vertices

  S=A-{a,b}

occur in one literal order

  K=(k_0,...,k_m)

in both paths. Thus P_a is K with b inserted in one slot and P_b is K with a inserted in one slot.

### 2. The two insertion slots are equal or adjacent
If the two slots are separated by at least one whole K-slot, insert both labels into K in their respective inherited positions. Every consecutive turn of the resulting order on all of A is already a turn of P_a or P_b, because the two insertion windows are disjoint. This gives a Hamilton path on A, contradiction.

Hence the two insertion slots are the same or adjacent.

### 3. Adjacent slots force one reverse swap turn
Suppose the slots are adjacent across a common vertex u. Without loss of notation, P_b inserts a immediately before u and P_a inserts b immediately after u. Combining the two inherited orders gives a spanning order of A whose only uncertified turn is

  (a,u,b).

If this turn were tight, A would be Hamiltonian. Therefore it is bad and R3 gives

  (b,u,a) tight.                                          (QS.1)

The opposite slot orientation gives the exact dual turn (a,u,b). Thus every quiet adjacent-slot exchange carries one graph-intrinsic directed swap mark at the shared common vertex.

### 4. Same internal gap: two double-insertion proposals
Suppose both labels occupy the same internal gap u|v of K. Then the two spanning candidate orders obtained by inserting both labels are locally

  u,a,b,v,                                                  (QS.2)
  u,b,a,v.                                                  (QS.3)

All turns outside these displayed windows are inherited. Since A is non-Hamiltonian, each proposal has a bad local turn.

For (QS.2), either

  (u,a,b) bad, hence (b,a,u) tight,                         (L_a)

or

  (a,b,v) bad, hence (v,b,a) tight.                         (R_b)

For (QS.3), either

  (u,b,a) bad, hence (a,b,u) tight,                         (L_b)

or

  (b,a,v) bad, hence (v,a,b) tight.                         (R_a)

### 5. Opposite-side failures produce a universal one-extension four-set
If the failures are L_a and R_a, then on the ordinary comparison edges of the four-set

  X={u,v,a,b}

we have

  ab -> au       from (b,a,u),
  au -> av       from the inherited tight turn (u,a,v) in P_b,
  av -> ab       from (v,a,b).

Hence X contains a directed comparison triangle.

If the failures are R_b and L_b, then similarly

  ub -> bv -> ab -> ub

is a directed comparison triangle, using the inherited tight turn (u,b,v) in P_a.

A directed comparison triangle remains present after adjoining any exterior vertex d. Therefore every five-set X+d is nonintegrable. Accepted R902 Hamiltonizes every nonintegrable five-vertex boundary tournament. Consequently

  X+d is Hamiltonian for every d outside X.                (QS.4)

Thus the mixed-side same-gap cell produces exactly the universal one-extension four-set targeted by current Guidance G9. No Hamiltonicity of X itself is asserted.

### 6. Same-side failures are one-sided comparison fans
If both failures are left, L_a and L_b, then the physical edge ab has two outgoing comparison arcs

  ab -> au,
  ab -> bu.                                                 (QS.5)

If both failures are right, R_a and R_b, then ab has two incoming comparison arcs

  av -> ab,
  bv -> ab.                                                 (QS.6)

These are graph-intrinsic one-sided SOURCE/SINK fan marks attached to the same exchanged pair {a,b}.

If the common insertion slot lies before the first K vertex, each of the two possible double-insertion orders has only its right local turn uncertified, so non-Hamiltonicity forces the SINK form (QS.6). If the common slot lies after the last K vertex, it forces the SOURCE form (QS.5).

### 7. Live-cylinder / closed-class interface
Inside a live puncture cylinder, both source rows P_a|Q and P_b|Q are exact and have the same literal complement. Hence the local mark (QS.1), the one-sided fan (QS.5)/(QS.6), or the universal extension core (QS.4) is current with the two neighboring singleton-rooted maximum three-forests

  P_a | Q | {a},
  P_b | Q | {b}.

This does not yet prove that a one-sided fan can be transported around every closed exchange class. It does show that quiet neighboring-support recurrence has only two non-core local species: an adjacent-slot swap arrow or a same-gap one-sided fan. Any mixed same-gap holonomy exits immediately to the small-core absorber.

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
        "revision_id": "R902"
    }
]
```
