# A fixed-witness pair-disagreement star contains a visible crossing edge cover

**Workspace:** D17
**State:** established
**Key:** `pair-disagreement-visible-or-interval-cage`

**Summary:** Strengthen the positive-Phi fixed-witness Johnson-star fan using the certified hidden-conflict normal form. A hidden cross edge a-b has literal form C_{p,a}: X-b-Z|Y and C_{p,b}: X-a-Y|Z. Its nonempty terminal fragment Z has a physical endpoint z. If z is on the B side, z is an endpoint of C_{p,a}, so a-z cannot be hidden; if z is on the A side, z lies opposite the common witnesses u,v in C_{p,b}, so z-b cannot be hidden. Hence every hidden cross edge shares a star endpoint with a visible common-residue crossing edge. The visible edges therefore form an edge-dominating set of the complete bipartite fixed-witness conflict fan; equivalently they touch every vertex of at least one color class, so there are at least min(|A|,|B|) visible conflicts. In particular an all-hidden positive-Phi star is impossible. Each visible edge is already a cover-valued common-residue selected-crossing portal. This is a family-level currentization theorem, not yet total-Phi descent.

### 1. Fixed-witness Johnson-star conflict
Retain the chosen pair-deletion partition family and the fixed-witness star of `pair-disagreement-star`. Thus {u,v} is a physical witness pair, U=V(H)-{u,v}, and p in U is a deletion label whose p-star is mixed. Normalize

  A={a in U-{p}: f({p,a})=0},
  B={b in U-{p}: f({p,b})=1}.

Both A and B are nonempty and |A|+|B|=n-3. For every cross pair a in A, b in B, the adjacent pair-deletion fibers D={p,a} and E={p,b} disagree on the surviving pair {u,v}. Fix actual exact two-covers C_D,C_E realizing the chosen partitions.

Call the cross conflict VISIBLE if, after trimming b from C_D and a from C_E to the common triple-deletion residue, at least one trimmed forest contains a selected state crossing the support partition induced by the other trimmed forest. Call it HIDDEN if it is hidden in both directions in the exact sense of `codimension-one-coherence`. Every cross edge is exactly one of these species.

### 2. Hidden-edge normal form
Fix a in A and b in B and suppose the conflict is HIDDEN. The certified hidden-conflict normal form gives three nonempty supports X,Y,Z such that, after possibly reversing displayed path orders,

  pi_D restricted = (X union Z) | Y,
  pi_E restricted = (X union Y) | Z,

and the actual source covers have literal path/support form

  C_D : X - b - Z | Y,
  C_E : X - a - Y | Z.

The witness pair {u,v} is different-block in the first restricted partition and same-block in the second. Therefore exactly one of u,v lies in Y and the other lies in X. Neither witness lies in Z. In particular b is internal in C_D, while a is internal in C_E and lies physically between u and v on the rail X-a-Y.

### 3. Every hidden edge is adjacent to a visible edge
Keep one hidden cross edge a-b and its normal form. The fragment Z is nonempty and is a terminal fragment of the b-containing rail X-b-Z of C_D. Let z be the physical endpoint of that rail lying in Z. Since z survives the common deletion,

  z in (A-{a}) union (B-{b});

u,v are excluded because neither lies in Z.

There are two cases.

**Case z in B.** Then z is a physical rail endpoint of C_D=C_{p,a}. If the cross edge a-z were HIDDEN, Section 2 applied to a-z would force z to be internal in this same fixed cover C_{p,a}. Contradiction. Hence a-z is VISIBLE. It shares the A-endpoint a with the original hidden edge a-b.

**Case z in A.** In the E-fiber partition for the original hidden edge, Z is exactly the block opposite X union Y, and u,v both lie in X union Y. Thus z is in the block opposite the common witnesses u,v in the fixed cover C_E=C_{p,b}. If the cross edge z-b were HIDDEN, Section 2 applied to z-b would force z to lie internally between u and v on the common u-v rail of this same fixed cover C_{p,b}. Contradiction. Hence z-b is VISIBLE. It shares the B-endpoint b with the original hidden edge a-b.

Therefore every HIDDEN edge of the complete bipartite conflict fan shares at least one star endpoint with a VISIBLE edge. Equivalently, the visible cross edges form an edge-dominating set of the complete bipartite graph K_{A,B}.

### 4. Visible edges cover one whole color class
Let V_vis be the set of visible cross edges. Suppose some a in A and some b in B were both incident with no visible edge. Then the cross edge a-b is not visible and hence is hidden. By Section 3 it must share a or b with a visible edge, contradicting the choice of a,b.

Thus unhit vertices can occur on at most one side. Equivalently, every vertex of A is incident with a visible edge, or every vertex of B is incident with a visible edge (possibly both). Hence

  |V_vis| >= min(|A|,|B|).

In particular every positive-Phi fixed-witness p-star contains at least one physically visible common-residue conflict, and a balanced star contains linearly many. The all-hidden interval-cage alternative is impossible.

The earlier internal-capacity estimate remains a compatible weaker corollary: a hidden cross edge forces its exchanged label internal in the opposite pair-deletion cover, so each star vertex has hidden degree at most n-6. The edge-domination argument is stronger because it uses the terminal endpoint of the hidden normal form itself rather than only counting internal slots.

### 5. Family-level consequence and fence
A VISIBLE cross edge is already cover-valued. On the common triple-deletion residue one of the two trimmed source forests contains a literal selected state crossing the support partition supplied by the other. Thus a positive global pair-partition disagreement minimum cannot consist only of abstract or doubly-hidden overlap bits: one whole side of a canonical fixed-witness conflict star is incident to actual current crossing portals.

This is the exact finite normal form relevant to G22:

  positive Phi witness star
     => visible common-residue crossings touching every vertex of at least one star color.

No total-Phi descent is claimed. The visible crossings may be different physical states, and paying them separately would lose the current representatives unless their source ancestry is reused. The remaining parent problem is now narrower: simultaneously consume a visible crossing edge cover of one fixed-witness Johnson star, or show that its certificate-retaining returns force strict global disagreement improvement/closure.