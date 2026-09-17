# A special-order rank-two cube fiber reduces to one outward endpoint weave

**Workspace:** D17
**State:** established
**Key:** `special-p5-rank2-cube-outward-endpoint-weave`

**Summary:** Assume a literal special source P5 K=(x,a,y,c,z) with the three source spoke turns and put W=H-K. The rank-two Boolean fiber G=W+{x,z}=H-{a,y,c} is non-Hamiltonian and exactly two-covered. For any exact two-cover F of G, R560 with absorber K forces at least two maximal W-blocks; three or more give the common-core R159 component drop, so the quiet branch has exactly two W-blocks. Contracting them gives p+tau=2, where p records a selected xz/zx root state. If p=1 and the root dimer is x→z, replacing that dimer by the whole P5 K changes exactly one boundary turn; success two-covers H and failure gives an R523 collision on (a,x) or (z,c). If the root dimer is z→x, R435 sees a consecutive reverse-order endpoint chord against K and emits reverse-trimer/proper-cycle geometry. If p=0, the contracted forest is only x-W1 | z-W2 or x-W1-z | W2; x,z are endpoints because an isolated root would Hamiltonize W plus the other root. Whenever x is terminal or z is source, trimming both roots and grafting K changes exactly one turn, again giving TWO-COVER or R523. Hence the only quiet p=0 orientation is x source and z terminal, in one of the two displayed outward-weave forms. By SV96465 this reduction is available in every source frame at order n>=13. The theorem does not consume R159/R523/R435 outputs and does not yet absorb the final outward weave.

### 1. Setup and the rank-two fiber
Let H be a hypothetical smallest counterexample and retain a literal special source order

  K=(x,a,y,c,z)

on five distinct vertices, together with the three same-orientation source turns

  (a,x,c), (a,y,c), (a,z,c) tight.

Put

  W=V(H)-V(K),
  G=W union {x,z}=V(H)-{a,y,c}.

The complement {a,y,c} is the retained tight trimer. If G were Hamiltonian, that Hamilton path together with (a,y,c) would two-cover H. Hence G is non-Hamiltonian. By smallest-counterexample minimality R4,

  pc(G)=2.                                                   (RW.1)

Fix an arbitrary exact two-cover F of G.

The same complementary-support argument and SV89302 show that W, W+x, and W+z are all non-Hamiltonian: their complementary supports are respectively K, a Hamilton P4 on {a,c,y,z}, and a Hamilton P4 on {a,c,x,y}. By R4 each has path-cover number exactly two. These lower-fiber facts will only be used to exclude singleton-root rails below.

### 2. Two W-blocks and p+tau=2
Apply R560 with

  D={a,y,c},
  S={x,z},
  C=W,
  A=K.

The absorber A is one Hamilton path on D union S and F is a two-cover of H-D. Since pc(H)=3, R560 gives at least two maximal nonempty W-blocks in F. If there are at least three, those W-blocks form a literal cover of W by at least three tight paths, while pc(W)=2. Accepted R159 therefore gives the common-core component-drop balanced-pair output.

Work outside that output. Then F has exactly two maximal W-blocks, say B_1,B_2. Let

  p = 1 if F selects the physical root state xz or zx, and 0 otherwise,
  tau = number of selected {x,z}|W transitions.

After contracting B_1,B_2, the two F-rails become a forest on four vertices with two components, hence exactly two selected edges. No edge joins B_1 to B_2 because they are maximal W-blocks. Therefore

  p+tau=2.                                                  (RW.2)

Thus only (p,tau)=(1,1) and (0,2) remain.

### 3. The p=1 cell: matching root orientation is one-hole, reverse orientation is R435
Assume p=1. Then tau=1. The unique-transition normal form in R560 says the two roots form one contiguous dimer block on the unique mixed rail; the other rail is the second pure W-block.

First suppose the selected root dimer is x->z. The mixed rail is literally either

  (x,z) followed by B,

or

  B followed by (x,z),

for one of the two W-blocks B.

In the first form replace the selected dimer (x,z) by the whole source path K=(x,a,y,c,z). Every old turn remains certified except the single new boundary turn

  (c,z,b_0),

where b_0 is the first vertex of B. If this turn is tight, K followed by B together with the untouched W-block is a spanning two-cover of H. Since H is a counterexample the turn is bad, so R3 gives

  (b_0,z,c) tight.

Together with the retained source turn (a,z,c), the tested oriented dimer (z,c) has two distinct same-polarity witnesses b_0 and a. Accepted R523 gives a same-oriented collision.

In the second form write b_t for the last vertex of B. Replacing (x,z) by K changes only

  (b_t,x,a).

Tightness gives a spanning two-cover; badness gives (a,x,b_t) tight, which collides by R523 with the retained source turn (a,x,c) on the tested oriented dimer (a,x).

Now suppose the selected root dimer is z->x. Compare the source path K with the mixed F-rail. Their only K-contacts on that root block are the consecutive F-contacts z,x, encountered in the reverse of their K-order, and x,z are not adjacent in K. Accepted R435 therefore gives an explicit reverse-trimer or vertex-simple proper-cycle output. Thus the p=1 cell has no quiet residue: it gives TWO-COVER, a source-pinned R523 collision, or explicit R435 geometry.

### 4. The p=0 cell has only two contracted support shapes
Assume p=0, so tau=2. Contract B_1,B_2. We obtain a two-component path forest on {x,z,B_1,B_2} with two edges, no xz edge, and no B_1B_2 edge.

Neither x nor z can be isolated. If x were isolated, it would be a singleton F-rail and the other F-rail would be a Hamilton path on W+z, contradicting the non-Hamiltonicity of W+z. The argument for z is identical.

Hence, up to exchanging the W-block labels, the contracted support has exactly one of the forms

  x-B_1  |  z-B_2,                                      (RW.3)

or

  x-B_1-z  |  B_2.                                      (RW.4)

In particular x and z are literal physical endpoints of their F-rails.

### 5. Every endpoint-role pattern except x-source/z-terminal is one-hole consumable
Suppose first that x is a terminal endpoint of its F-rail. Since p=0, its selected neighbor u lies in W. Trim both roots x,z from F. The surviving W-blocks remain two tight paths. Reattach the whole K at the x-end, producing a candidate spanning two-cover whose only new turn is

  (u,x,a).

All turns before u,x are inherited from F and all later turns are inherited from K. If (u,x,a) is tight, the proposal two-covers H. If it is bad, R3 gives

  (a,x,u) tight,

which is a second same-oriented certificate on (a,x) beside the source turn (a,x,c); R523 gives a collision.

Dually, suppose z is a source endpoint of its F-rail, with selected W-neighbor v. Trim x,z and reattach K at the z-end. The only new turn is

  (c,z,v).

Tightness gives a spanning two-cover; badness gives (v,z,c), which collides on (z,c) with source (a,z,c).

Therefore outside TWO-COVER/R523 geometry, neither of these compatible endpoint roles may occur. The only surviving endpoint orientation is

  x is the source endpoint,
  z is the terminal endpoint.                             (RW.5)

Combining (RW.3)-(RW.5), the p=0 quiet cell is exactly one of the two literal outward forms

  x-B_1  |  B_2-z,                                      (RW.6)

or

  x-B_1-z  |  B_2,                                      (RW.7)

with the displayed source-to-terminal orientation.

### 6. Rank-two reduction and high-order use
Thus for a literal special source P5 K=(x,a,y,c,z), every exact rank-two cube fiber F on W+{x,z} yields at least one of

1. common-W R159 component-drop geometry;
2. TWO-COVER of H;
3. a source-pinned R523 collision on (a,x) or (z,c);
4. explicit R435 reverse-trimer/proper-cycle geometry;
5. the single outward endpoint weave (RW.6) or (RW.7).

This is a complete physical reduction of the rank-two fiber and every successful splice above uses its full changed-turn window; the productive cases are genuinely one-hole.

By SV96465, every exact source frame of a smallest counterexample of order n>=13 contains some three internal spokes admitting such a special order. Hence above order twelve the special-order branch can always be normalized further to this rank-two outward-weave cell or one of the explicit outputs above. This is not yet frame absorption: under G31, R159/R523/R435 outputs remain constructive until a direct global consumer is supplied, and the outward weave itself is the remaining static cell.

R24 and R5 are unused.

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
        "revision_id": "R159"
    },
    {
        "relation": "dependency",
        "revision_id": "R435"
    },
    {
        "relation": "dependency",
        "revision_id": "R523"
    },
    {
        "relation": "dependency",
        "revision_id": "R560"
    }
]
```
