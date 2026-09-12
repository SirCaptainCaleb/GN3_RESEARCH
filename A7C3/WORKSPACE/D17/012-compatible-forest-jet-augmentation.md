# Compatible-forest augmentation has a jet-transport calculus and a two-cut cyclic seam grid

**Workspace:** D17
**State:** established
**Key:** `compatible-forest-jet-augmentation`

**Summary:** Under G3's full compatible-forest moonshot, a maximum spanning compatible forest in a smallest counterexample has exactly three components. R4 implies complete physical-edge coverage across the family of maximum forests: every ordinary dimer occurs literally in some maximum three-cover. A neutral suffix transfer is an exact boundary-1-jet move: a terminal jet of one rail absorbs a suffix of another rail after one selected cut, preserving component count and exposing the predecessor jet left by that cut; targeting the source yields a genuine augmentation. Choosing a maximum forest with lexicographically maximal sorted component sizes forces every suffix/prefix absorption into a largest rail to have a bad complete seam window. Physical-label collisions admit a local exact dichotomy: two tight turns (p,v,q),(r,v,s) with four distinct neighbors either admit one of the mixed turns (p,v,s),(r,v,q), or the two mixed failures reverse by R3 to a directed 4-cycle in the local comparison tournament at v, so the five-set {p,q,r,s,v} is nonintegrable and hence Hamiltonian by R902. In the acyclic R887 branch, a first physical repetition of any directed comparison walk always has its chronological shortcut tight, since a bad shortcut would close a directed comparison cycle; lifting that shortcut through forest-exchange parity remains an explicit unresolved requirement. Finally, any three-cover A|B|C has a natural two-cut cyclic augmentation proposal: split B and C, then form B^- C^+ and C^- A B^+. Its complete new-turn window is finite and in the nondegenerate interior case consists of six boundary turns. A cell with all turns tight is a spanning two-cover. Thus the full augmentation problem can be attacked as a two-dimensional seam-grid/transversal problem rather than only through whole-component concatenation.

### 1. Maximum compatible forests and complete physical-edge coverage
Work in a hypothetical smallest Strong Level-(1) counterexample H. A compatible spanning linear forest means a spanning ordinary linear forest whose nontrivial components carry orientations that are tight paths. Since accepted R4 gives pc(H)=3 and H has no two-cover, every maximum compatible spanning linear forest has exactly n-3 selected ordinary edges and exactly three components.

There is an important family-level completeness property. Fix ANY two distinct physical vertices u,v. The dimer (u,v) is vacuously tight. Apply accepted R4 to this proper graph-intrinsic path. Its complement H-{u,v} has exact path-cover number two, so restoring the literal dimer produces a spanning three-cover containing the physical edge uv. Because pc(H)=3, this is a maximum compatible forest. Therefore

  every ordinary edge of K_V occurs in at least one maximum compatible spanning forest.     (JF.1)

A cross-component edge blocked in one maximum forest is therefore never globally forbidden. The augmentation theorem should be viewed as an exchange theorem across the family of maximum forests, not as an attempt to prove one fixed source forest contains all useful edges.

### 2. Exact one-cut boundary-jet transport
Let a current spanning three-cover contain oriented rails

  A=(a_0,...,a_r),    B=(b_0,...,b_m),

and retain the third rail C. Fix i with 1<=i<=m and write

  B^-=(b_0,...,b_{i-1}),   B^+=(b_i,...,b_m).

Try the neutral suffix transfer

  (A followed by B^+) | B^- | C.                       (JF.2)

Every old turn inside A,B^-,B^+,C is inherited. The complete uncertified window is precisely every consecutive triple crossing the new A|B^+ junction. In the ordinary nondegenerate case |A|>=2 and |B^+|>=2 these are

  (a_{r-1},a_r,b_i),
  (a_r,b_i,b_{i+1}).                                   (JF.3)

If the appropriate boundary block is a singleton, delete the nonexistent turn from this list; equivalently define the window intrinsically as the new consecutive triples of the displayed path in (JF.2).

When the complete window is tight, (JF.2) is another compatible spanning three-forest. The terminal 1-jet of A has been transported through the physical target b_i, and the new exposed terminal is b_{i-1}, with predecessor b_{i-2} when i>=2. In selected-edge language one adds the fresh edge a_r b_i and deletes b_{i-1}b_i. If the target is the source b_0 instead, no selected edge is deleted; success gains one edge and merges A,B, producing a spanning two-cover. Thus an augmenting sequence is a chain of neutral jet transports ending at a source target.

The head/prefix dual is exact.

### 3. Lexicographically extremal maximum forests have all-vertex absorption walls
Among all maximum compatible spanning forests choose F so that the sorted component-size vector is lexicographically maximal. Let A be a largest component. For any other component B and any nonempty proper suffix B^+ as in Section 2, the transfer (JF.2) cannot be tight: it preserves three components but makes the component containing A strictly larger than the old largest component, contradicting the extremal choice. The source case i=0 would reduce the component count and contradict counterexamplehood directly. Therefore every suffix position of every exterior rail has a bad complete A-tail absorption window.

Dually every nonempty prefix of every exterior rail has a bad complete window for absorption into the head of A. This is stronger than the six intact-component clauses of accepted R879: a largest rail carries a blocked boundary-jet window indexed by EVERY physical position of every other rail. It does not by itself say which turn in each window is bad.

### 4. A physical middle collision is mixed-turn recombination or a Hamilton five-set
Let p,q,r,s,v be five distinct physical vertices and suppose

  (p,v,q),   (r,v,s)                                    (JF.4)

are tight. Test the two mixed turns

  (p,v,s),   (r,v,q).                                   (JF.5)

If either is tight, it is a literal mixed local recombination through the same physical middle v. Suppose both are bad. Boundary antisymmetry R3 gives

  (s,v,p),   (q,v,r)                                    (JF.6)

tight. In the local comparison tournament at v, (JF.4) and (JF.6) give the directed cycle

  vp -> vq -> vr -> vs -> vp.                           (JF.7)

Hence the comparison orientation of the induced five-set {p,q,r,s,v} is cyclic, so the five-set is nonintegrable under accepted R887. Accepted R902 then gives an actual Hamilton tight P5 on this five-set. Thus every four-neighbor physical middle collision has the exact dichotomy

  MIXED TURN AVAILABLE, or HAMILTON FIVE-VERTEX BLOSSOM. (JF.8)

The P5 conclusion has NO endpoint prescription. It is a gadget requiring a later expansion/splice theorem, not an augmentation by itself.

### 5. First-repetition shortcut in the acyclic comparison branch
There is a useful clean fact in the R887 acyclic branch. Let a directed comparison walk have physical trace containing a first repeated vertex v, displayed locally as

  ... p,v,q, ..., r,v,s ... .                            (JF.9)

The directed comparison chain contains the route from edge pv through the intervening edge states to edge vs. If the chronological shortcut turn (p,v,s) were bad, R3 would make (s,v,p) tight, i.e. the comparison arc vs -> vp. Together with the intervening directed route this is a directed comparison cycle. Therefore when Gamma(H) is acyclic,

  (p,v,s) is necessarily tight.                          (JF.10)

At the level of a bare directed comparison walk, the whole repeated-v segment may therefore be shortcut to p,v,s. This proves that physical repetition is never a LOCAL turn obstruction in the edge-ordered branch. However an augmenting forest exchange carries alternating add/delete parity and parked path pieces. Deleting the comparison-walk loop is not yet proved to preserve that exchange data. This is the exact remaining lifting fence required by G3.

### 6. Two-cut cyclic augmentation of a spanning three-cover
Retain any literal spanning three-cover

  A=(a_0,...,a_r), B=(b_0,...,b_m), C=(c_0,...,c_l).

Choose cuts before b_i and c_j with 1<=i<=m and 1<=j<=l, and write B=B^- B^+, C=C^- C^+ in the inherited orders. Consider the two displayed paths

  R_1 = B^- followed by C^+,
  R_2 = C^- followed by A followed by B^+.               (JF.11)

Their supports are disjoint and partition V(H). Every consecutive triple wholly inside one inherited block is already tight. Hence (JF.11) is a spanning two-cover exactly when every NEW consecutive triple across the three displayed joins is tight. In the nondegenerate interior case where A,B^-,B^+,C^-,C^+ all have order at least two, the complete new-turn set is

  (a_{r-1},a_r,b_i),        (a_r,b_i,b_{i+1}),
  (b_{i-2},b_{i-1},c_j),    (b_{i-1},c_j,c_{j+1}),
  (c_{j-2},c_{j-1},a_0),    (c_{j-1},a_0,a_1).           (JF.12)

For boundary/singleton blocks, the exact definition is again simply 'all consecutive triples of R_1,R_2 not inherited from A,B,C'; this automatically removes nonexistent turns and includes any triple spanning a singleton block.

Sequentially, (JF.11) is three jet transports: A absorbs B^+, the leftover B^- absorbs C^+, and the leftover C^- finally absorbs the ENTIRE parked A B^+ component at its source a_0. The last move has no compensating selected cut, so success is a genuine +1 edge augmentation.

Accepted R459 says whole-component concatenations alone are exhausted. Formula (JF.11) is the smallest natural cross-partition enlargement: two cut coordinates (i,j), three junction windows, and an exact final two-cover. The new full-theorem target can therefore be sharpened to a TWO-CUT CYCLIC AUGMENTATION principle: among some orientation/order of the three source rails and some cut cell (i,j), all complete junction windows pass. If this stronger formulation is false, the failed cells form a structured two-dimensional seam-transversal object that should be attacked globally rather than expanded into unrelated local cases.

### 7. Status
Sections 1-6 are direct deductions from accepted R3/R4/R887/R902 plus literal path surgery; they do not prove the full compatible-forest augmentation theorem. The decisive open steps are either (a) prove the two-cut cyclic augmentation principle, or (b) characterize a minimal seam-grid obstruction and use representative exchange (JF.1), jet collision (JF.8), and acyclic shortcutting (JF.10) to destroy it. No comparison cycle or Hamilton P5 is being counted as an augmentation without a physical expansion proof.

## References

```json
[
    {"relation":"dependency","revision_id":"R3"},
    {"relation":"dependency","revision_id":"R4"},
    {"relation":"dependency","revision_id":"R887"},
    {"relation":"dependency","revision_id":"R902"},
    {"relation":"comparison","revision_id":"R879"},
    {"relation":"comparison","revision_id":"R459"}
]
```
