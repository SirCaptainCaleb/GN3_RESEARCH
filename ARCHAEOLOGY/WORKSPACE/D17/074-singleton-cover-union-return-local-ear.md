# A quiet fixed-complement replacement return localizes to a two-step ear

**Workspace:** D17
**State:** established
**Key:** `singleton-cover-union-return-local-ear`

**Summary:** Let C=(c0,...,ct) be a Hamilton rail with C+p non-Hamiltonian and let an actual replacement cover P|D on C-x+p retain the same other rail D and select p-ci. Outside explicit R435 comparison output, P is C-x in the same literal order with p inserted adjacent to ci. Non-Hamiltonicity forces x to lie within two C-positions of ci; at distance two p must be inserted toward x. Restoring x at its old position gives a spanning proposal W|D with at most two uncertified local turns, so at least one is bad and its exact reversal is tight. Thus replacement-side separator returns are never arbitrary interior contacts: after the positive-kappa branch is removed they reduce to explicit R435 geometry or a bounded source-labelled one/two-hole ear retaining the fixed Hamilton complement.

### Fixed-complement replacement setup
Let

  C=(c_0,c_1,...,c_t)

be a literal Hamilton tight path and let p be exterior to C. Let D be a disjoint tight path such that C|D is the retained exact p-deletion cover. Assume C+p is non-Hamiltonian. Suppose that for some x in C there is another actual exact singleton-deletion cover

  P | D

with V(P)=(C-{x}) union {p}, and suppose P selects a physical return adjacency p-c_i for a surviving c_i in C.

In the hard fixed-complement separator cell this is exactly the Hamilton-replacement branch of `singleton-cover-union-return-defect-or-replacement`. The argument below only uses the displayed fixed-other-rail data.

### Quiet R435 comparison turns the return into one literal insertion
Compare P and C by accepted R435. If the comparison is nonquiet, retain its explicit reversed old state, reverse trimer, or vertex-simple tight cycle together with p, x, c_i and the unchanged rail D.

Assume the comparison is quiet. Then all common C-vertices occur on P in their literal C-order. Since p is the only new vertex, P is obtained from C-{x} by inserting p in one slot. Since p-c_i is selected, p is inserted immediately before or immediately after c_i.

Write x=c_j. Necessarily j is not i because c_i survives on P.

### The omitted owner lies within two C-positions of the return
If |j-i|>=3, restore x at its original C-position while leaving p in its selected P-position. Every turn in the p-insertion window is a literal P-turn, every new turn in the x-restoration window is a literal C-turn, and these radius-two windows are disjoint. The resulting word is therefore a Hamilton tight path on C+p, contradiction.

Hence

  |j-i| <= 2.

There is a directional restriction at distance two. If x=c_{i+2} and p were inserted before c_i, the same restoration has disjoint certified windows and Hamiltonizes C+p. Therefore x=c_{i+2} forces p immediately after c_i. Dually, x=c_{i-2} forces p immediately before c_i.

Thus, omitting nonexistent boundary indices, the complete quiet local list is:

1. x=c_{i+2}:  ... c_i,p,c_{i+1},c_{i+3},... ;
2. x=c_{i+1}, p after c_i:  ... c_i,p,c_{i+2},... ;
3. x=c_{i+1}, p before c_i: ... c_{i-1},p,c_i,c_{i+2},... ;
4. x=c_{i-1}, p after c_i:  ... c_{i-2},c_i,p,c_{i+1},... ;
5. x=c_{i-1}, p before c_i: ... c_{i-2},p,c_i,c_{i+1},... ;
6. x=c_{i-2}:  ... c_{i-3},c_{i-1},p,c_i,... .

This is the two-step local-ear normal form.

### Restoring x leaves only one or two local holes
For each form, restore x at its original C-position and keep p where P selected it. Call the resulting vertex-simple word W on C+p. Pair W with the unchanged tight rail D. Outside the displayed local window W agrees literally with C or P. Its complete uncertified-turn set E is therefore:

1. x=c_{i+2}:
   E={ (p,c_{i+1},x) }.

2. x=c_{i+1}, p after c_i, writing r=c_{i+2} when it exists:
   E={ (c_i,p,x), (p,x,r) }, with the second turn omitted when r does not exist.

3. x=c_{i+1}, p before c_i:
   E={ (p,c_i,x) }.

4. x=c_{i-1}, p after c_i:
   E={ (x,c_i,p) }.

5. x=c_{i-1}, p before c_i, writing l=c_{i-2} when it exists:
   E={ (l,x,p), (x,p,c_i) }, with the first turn omitted when l does not exist.

6. x=c_{i-2}:
   E={ (x,c_{i-1},p) }.

If every existing turn in E were tight, W|D would be a spanning two-cover of H. Hence at least one existing hole is bad. Boundary antisymmetry R3 gives its complete reversal as a tight turn. In the four one-hole forms this produces a forced labelled reverse turn; in the two two-hole forms it produces the exact mate disjunction

  reverse(e_1) OR reverse(e_2).

The return label p, omitted owner x, contact c_i, insertion side, fixed rail D, and complete hole set are retained. No state is transported between deletion fibers.

### Endpoint-or-ear interpretation
The theorem is independent of whether c_i is an endpoint of the displayed Hamilton order C. At an endpoint, only the corresponding truncated cases survive. At an interior contact, the same conclusion shows that a replacement return cannot wander through the complement: outside R435 it is supported in the five-vertex window from c_{i-2} through c_{i+2} and exports an exact one/two-hole spanning proposal.

More generally, one may repeat the comparison against any Hamilton order Q on the same support C. If a comparison is quiet, the omitted owner x must lie within two positions of the physical return contact c in that Q-order. Therefore, if the same return is quiet against several Hamilton orders, all of those orders place x inside the radius-two neighborhood of c. Failure of such simultaneous localization is itself explicit R435 order geometry. This is the order-valued replacement for the unique-arm-order property used in the solved theta case.

Combining with `singleton-cover-union-return-defect-or-replacement`, every forced separator return now has the following exact front door:

1. positive current kappa defect; or
2. explicit R435 comparison geometry; or
3. a fixed-complement two-step local ear with one/two exact restoration holes and a labelled reverse mate.

### Scope
The local reverse mate is not claimed to close H, decrease K, or satisfy R561 by itself; R483 fences generic reverse geometry. The gain is that the former arbitrary interior-return obstruction has been compressed to a bounded order-valued ear while retaining the actual singleton fibers and fixed complementary rail. Any next consumer needs only this radius-two window, not an unrestricted interior contact.

Status: complete deduction from accepted R435 quiet order preservation, R3, and the actual fixed-complement replacement covers. Established exposition only; not canonically reviewed as an exact section unit.

## References

```json
[
    {
        "role": "At least one failed restoration hole has a certified exact reverse turn.",
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "role": "Outside explicit comparison output, the common C-vertices retain literal order, reducing P to insertion of p into C-x.",
        "relation": "dependency",
        "revision_id": "R435"
    },
    {
        "role": "Fence: localized reverse geometry remains currency requiring a cover-valued consumer.",
        "relation": "related",
        "revision_id": "R483"
    }
]
```
