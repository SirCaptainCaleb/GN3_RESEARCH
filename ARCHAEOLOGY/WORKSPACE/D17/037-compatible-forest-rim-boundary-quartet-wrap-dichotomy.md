# Two-sided rim walls give a fixed wrap family or Hamiltonize the boundary quartet

**Workspace:** D17
**State:** established
**Key:** `compatible-forest-rim-boundary-quartet-wrap-dichotomy`

**Summary:** Under the two-sided all-break wall on a complementary rail U=(u0,...,ua), |U|>=4, each adjacent rim edge q_{i-1}q_i supports two tight Hamilton P6 orders with the rim pair in either orientation and the same boundary vertices u1,u0,ua,u_{a-1}. Applying R548 to either order has two wrap seam tests independent of i: (u_{a-1},u1,u0) and (ua,u_{a-1},u1). If either is tight, the corresponding cyclic rotation succeeds for every rim edge, yielding a coherent new family of tight six-vertex carriers. If both are bad, R3 gives (u0,u1,u_{a-1}) and (u1,u_{a-1},ua), so the fixed boundary quartet {u0,u1,u_{a-1},ua} is Hamiltonian. The earlier wall already Hamilton-extends this quartet by every rim vertex qi. Thus complete wrap failure promotes the partial extension shell to a Hamilton four-core over the whole rim; only the one- or two-wrap-success branch remains dynamic.

### 1. Retain the two-sided wall
Let H be a hypothetical smallest counterexample. Let Q be a shortest ordinary comparison rim, and let

  U=(u_0,u_1,...,u_a),   a>=3,

be one complementary rail satisfying the two-sided all-break wall conclusions of the rim opposite-end R508 section. Thus for every rim vertex q_i:

  (u_1,u_0,q_i) is tight,                              (BW.1)
  (q_i,u_a,u_{a-1}) is tight,                          (BW.2)

and the u_0-spoke is LOW while the u_a-spoke is HIGH relative to both incident rim edges.

### 2. Every rim edge has two six-vertex Hamilton orders
Fix the rim edge q_{i-1}q_i. LOW at q_i gives

  (u_0,q_i,q_{i-1}) tight,

and HIGH at q_{i-1} gives

  (q_i,q_{i-1},u_a) tight.

Together with (BW.1)-(BW.2),

  P_i^+=(u_1,u_0,q_i,q_{i-1},u_a,u_{a-1})             (BW.3)

is a literal Hamilton P6 on the fixed boundary quartet plus q_{i-1},q_i.

The same argument with i and i-1 exchanged gives

  P_i^-=(u_1,u_0,q_{i-1},q_i,u_a,u_{a-1}).            (BW.4)

Thus the physical rim dimer can be selected in either orientation inside the same six-vertex support while both outer boundary dimers remain fixed.

### 3. R548 wrap tests are independent of the rim edge
Apply accepted R548 to P_i^+. The wrap joins the terminal u_{a-1} to the source u_1. Its two possible cyclic rotations require exactly the seam turns

  A=(u_{a-1},u_1,u_0),                                (BW.5)
  B=(u_a,u_{a-1},u_1).                                (BW.6)

These tests involve only the four boundary vertices of U and are independent of i. Hence:

- if A is tight, the corresponding head rotation of P_i^+ succeeds for every rim edge i;
- if B is tight, the corresponding tail rotation succeeds for every rim edge i.

The same two seam tests govern P_i^- because its first two and last two vertices are identical to those of P_i^+.

Therefore any successful wrap is automatically synchronized around the entire rim and yields a coherent family of new literal tight six-vertex carriers.

### 4. Complete wrap failure Hamiltonizes the boundary quartet
Suppose both A and B are bad. By boundary antisymmetry R3 their complete reversals are tight:

  (u_0,u_1,u_{a-1}) tight,
  (u_1,u_{a-1},u_a) tight.

Hence

  B_U=(u_0,u_1,u_{a-1},u_a)                           (BW.7)

is a literal Hamilton P4 on the fixed boundary quartet

  S_U={u_0,u_1,u_{a-1},u_a}.

Independently, the two-sided wall already gives for every rim vertex q_i the Hamilton P5

  (u_1,u_0,q_i,u_a,u_{a-1}),                          (BW.8)

where the middle turn (u_0,q_i,u_a) is forced because the u_0-spoke is LOW, the u_a-spoke is HIGH, and the local comparison tournament at q_i has no directed star triangle shorter than the chosen shortest rim.

Thus in the complete-wrap-failure branch S_U is itself Hamiltonian and

  S_U+q_i is Hamiltonian for every q_i in V(Q).        (BW.9)

This is a Hamilton four-core with universal one-vertex extension over the entire rim support. No extension claim is made for vertices outside Q union S_U.

### 5. Exact residual
The two-sided all-break wall therefore has a further global dichotomy:

1. at least one fixed boundary wrap seam succeeds, and the same R548 rotation succeeds simultaneously for every rim edge carrier P_i^+ and P_i^-; or
2. both fixed wrap seams fail, and the boundary quartet S_U is Hamiltonian while Hamilton-extending by every rim vertex.

The theorem does not assert that a successful wrap already escapes the terminal exchange class or that the partial universal-extension property in (BW.9) extends to all exterior vertices.
