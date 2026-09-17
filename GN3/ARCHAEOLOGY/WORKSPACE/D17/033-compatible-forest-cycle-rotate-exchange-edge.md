# Tight-cycle break motion is an explicit reversible CYCLE-ROTATE edge in maximum-three-forest space

**Workspace:** D17
**State:** established
**Key:** `compatible-forest-cycle-rotate-exchange-edge`

**Summary:** If a maximum spanning three-forest has one rail whose support closes to a literal tight cycle C, then moving the omitted rim edge by one step gives another maximum three-forest with the other two rails literally unchanged. This is exactly a successful R548 cyclic rotation: both neighboring rotations are legal because their sole new seam turns are inherited turns of C. Hence CYCLE-ROTATE may be added as a reversible edge type to the literal maximum-three-forest exchange graph. In any terminal SCC of this augmented graph, one representative containing a tight-cycle rail forces the entire cyclic-break orbit with fixed complementary rails to lie in the same SCC. This sharpens the movable-break family from existence to an explicit allowed exchange transition; no claim is made about terminal SCCs defined before adding this edge type.

### 1. Literal cycle rail in a maximum three-forest
Let H be a boundary tournament with pc(H)=3, and let

  F_i = Q_i | U | V

be a literal maximum spanning three-forest. Assume the support of Q_i is a vertex-simple tight cycle

  C=(q_0,q_1,...,q_{r-1},q_0),

and write the break beginning at q_i as

  Q_i=(q_i,q_{i+1},...,q_{i-1}),

indices modulo r. Thus every cyclic turn

  (q_{j-1},q_j,q_{j+1})

is tight.

### 2. R548 gives both neighboring break moves
Apply accepted R548 to the path component Q_i. Its wrap state joins terminal q_{i-1} back to source q_i.

The tail cyclic rotation is

  Q_{i+1}=(q_{i+1},...,q_{i-1},q_i).

Relative to Q_i its only new seam turn is

  (q_{i-2},q_{i-1},q_i),

which is tight because it is an inherited cyclic turn of C. Hence Q_{i+1} is tight.

The head cyclic rotation is

  Q_{i-1}=(q_{i-1},q_i,...,q_{i-2}),

whose only new seam is

  (q_{i-1},q_i,q_{i+1}),

again a tight cyclic turn of C. Hence Q_{i-1} is tight as well.

Therefore

  Q_i|U|V  <-->  Q_{i+1}|U|V

is a reversible literal maximum-three-forest transition, with U and V unchanged as ordered paths. Call this move CYCLE-ROTATE.

### 3. Augmented closed exchange classes
Define the augmented literal maximum-three-forest exchange digraph by adjoining CYCLE-ROTATE in both directions to whatever proved successor moves are already being used, in particular SLIDEs and legal DOUBLE recompletions. This changes no vertex set of representatives; it only records an additional proved legal transition.

Because the exchange graph is finite, one may choose a terminal strongly connected component in this augmented graph. If such a terminal component contains one representative Q_i|U|V whose Q-support closes to C, then closure under the two reversible CYCLE-ROTATE edges implies that it contains

  Q_j|U|V

for every cyclic break j, with the same literal U,V orders throughout. Thus every cyclic break is available inside one genuinely closed representative class, not merely as an externally listed family.

This conclusion is specifically about terminal classes of the augmented graph. It does not retroactively assert that a terminal SCC defined using only a smaller move set was already closed under CYCLE-ROTATE.

### 4. Relation to the proper-cycle movable-break section
The earlier movable-break section proves existence of the whole break family from a proper tight cycle and one fixed exact complement cover. The present result strengthens the dynamical interpretation: consecutive family members are connected by an explicit reversible proved move, namely the successful R548 rotation whose seam is already a cycle turn. This is the natural closed-class interface for the shortest-rim program.
