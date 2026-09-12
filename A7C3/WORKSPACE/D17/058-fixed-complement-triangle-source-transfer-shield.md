# The quiet critical block pushes one step into the complementary rail by transfer-or-shield

**Workspace:** D17
**State:** established
**Key:** `fixed-complement-triangle-source-transfer-shield`

**Summary:** In the HHH fixed-complement quiet-R961 packet, let Y=(y0,y1,y2), M=(m0,m1,...) and Q=(q0,q1,...) with m0 the bidirectional triangle-wall endpoint from SV19513. For each cyclic j, test r_j=(y_{j+1},y_{j+2},q0). If r_j is bad, R3 reverses it and the existing reverse-Y-dimer-to-m0 turn plus the universal y-m0-m1 seam give an explicit Hamilton path q0,y_{j+2},y_{j+1},M on (Omega-y_j)+q0; together with the literal Q-q0 rail this is an exact H-y_j two-cover. If r_j is tight, Y followed by q0 is a role-correct P4 for the source of Q; the seam to q1 must then be bad or M | (Y,q0,Q-q0) closes H, so R3 gives the named reverse-source shield (q1,q0,y_{j+2}). Hence the three cyclic tests force either at least two exact transferred singleton fibers sharing literal complement Q-q0, or at least two distinct Y-witnesses on the same reverse Q-source boundary dimer. TTT is the terminal dual. This is a one-step complementary-support exchange mechanism, not closure.


### 1. HHH setup
Retain the fixed-complement quiet-R961 packet from `fixed-complement-r961-bidirectional-triangle-wall` SV19513. Write

  Omega=Y disjoint_union M,
  Y=(y_0,y_1,y_2),
  M=(m_0,m_1,...,m_r),
  Q=(q_0,q_1,...,q_t),

with cyclic indices on Y. In the fixed-complement smallest-counterexample realization, |M|,|Q|>=3. The HHH wall supplies, for every j modulo three,

  (y_{j+2},y_{j+1},m_0) tight,                         (TS.1)
  (y_j,m_0,m_1) tight.                                  (TS.2)

The first line is the original tail-signing of every reverse Y-dimer; the second is the universal role-correct M-boundary seam.

### 2. One cyclic test either transfers q_0 into the critical block or emits a Q-boundary shield
For each j modulo three test

  r_j=(y_{j+1},y_{j+2},q_0).                            (TS.3)

**Transfer branch.** If r_j is bad, boundary antisymmetry gives

  (q_0,y_{j+2},y_{j+1}) tight.                           (TS.4)

Concatenate (TS.4), (TS.1), (TS.2), and the inherited remainder M. The literal word

  P_j^*=(q_0,y_{j+2},y_{j+1},m_0,m_1,...,m_r)            (TS.5)

is a Hamilton tight path on

  (Omega-{y_j}) union {q_0}.

The literal suffix

  Q^-=(q_1,...,q_t)

is Hamiltonian. Therefore

  C_j^*=P_j^* | Q^-                                      (TS.6)

is a two-cover of H-y_j. It is exact: if H-y_j were Hamiltonian, that Hamilton path together with singleton y_j would two-cover H. Thus a bad cyclic test performs an actual one-vertex complementary-support transfer, moving q_0 from Q into the active critical-block side while moving the omitted y_j out.

**Shield branch.** If r_j is tight, the directed-triangle turn

  (y_j,y_{j+1},y_{j+2})

and r_j give the tight P4

  (y_j,y_{j+1},y_{j+2},q_0).                             (TS.7)

If the sole continuation seam

  s_j=(y_{j+2},q_0,q_1)                                  (TS.8)

were tight, then

  (y_j,y_{j+1},y_{j+2},q_0,q_1,...,q_t) | M

would be a spanning two-cover of H. Hence s_j is bad, and R3 gives the exact reverse-source shield

  (q_1,q_0,y_{j+2}) tight.                               (TS.9)

So a tight cyclic test does not disappear: it places a named Y-witness on the reverse source boundary dimer (q_1,q_0) of the literal complementary rail.

### 3. Pigeonhole compression
Let

  S={j : r_j is bad}.

If |S|>=2, then at least two of the exact singleton rows (TS.6) exist simultaneously. They share the SAME literal complementary rail Q^- and have the explicit active orders (TS.5). This is a coherent two-fiber complementary-support transfer, not merely existence of two unrelated covers.

If |S|<=1, then at least two of the three tests r_j are tight, so (TS.9) gives at least two distinct Y-witnesses on the same physical reverse source dimer (q_1,q_0). Since q_2 exists, this dimer is the reverse initial boundary dimer of the literal tight trimer (q_0,q_1,q_2). Retain the two witness identities and the source order of Q; do not immediately erase them into generic signed-dimer currency.

Thus the HHH quiet critical block has the exact dichotomy

  TWO COMMON-COMPLEMENT TRANSFERRED SINGLETON FIBERS,

or

  A TWO-WITNESS REVERSE Q-SOURCE BOUNDARY PACKET.         (TS.10)

The case |S|=3 gives all three transferred singleton fibers.

### 4. TTT dual and scope
The TTT packet is the exact terminal dual: use the terminal q_t of Q, the terminal wall vertex of M, and reverse all displayed orders. The conclusion is two common-complement transferred singleton fibers sharing Q-q_t, or a two-witness packet on the reverse terminal boundary dimer of Q.

This is not Critical-Block Complement Absorption and does not claim a spanning two-cover. Its significance is that the quiet R961 wall now performs one genuine step of the complementary-support exchange requested by G3: failure to transfer is converted into a concentrated physical obstruction on the boundary of the other rail.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    }
]
```
