# The anchored triangle forces a three-witness reverse wall at both ends of the complementary rail

**Workspace:** D17
**State:** established
**Key:** `fixed-complement-triangle-complement-double-boundary-wall`

**Summary:** In the quiet fixed-complement R961 triangle packet, for every triangle label y_i the other two triangle labels together with the anchored remainder rail M form a literal Hamilton path. Therefore y_i cannot be prepended to or appended after the complementary Hamilton rail Q, since either attachment would pair with that other Hamilton path and two-cover H. Exact reversal forces (q1,q0,y_i) and (y_i,q_t,q_{t-1}) tight for all three y_i. Thus both reverse outer boundary dimers of Q carry the same full three-label witness set Y. The statement holds in both HHH and TTT orientations and uses the full M|Q complement geometry rather than endpoint-only five-set Hamiltonicity.

### 1. Fixed-complement anchored-triangle setup
Retain the quiet fixed-complement R961 packet from `fixed-complement-r961-quiet-triangle-promotion` SV19367 and `fixed-complement-r961-bidirectional-triangle-wall` SV19513. Write

  V(H)=Y disjoint_union V(M) disjoint_union V(Q),
  Y=(y_0,y_1,y_2),
  Q=(q_0,q_1,...,q_t),

with cyclic indices on Y and |M|,|Q|>=3. The rail M is the remainder of the non-Hamiltonian critical block Omega=Y union V(M), while Q is the fixed literal Hamilton complement. The exact cover of H-Y is M|Q.

### 2. For each missing triangle label, the other two labels already Hamiltonize with M
First take the HHH orientation, with

  M=(m_0,m_1,...,m_r).

SV19513 retains, for every i modulo three,

  (y_{i+2},y_{i+1},m_0) tight,
  (y_{i+1},m_0,m_1) tight.

Together with the inherited M order these turns give the literal Hamilton path

  R_i=(y_{i+2},y_{i+1},m_0,m_1,...,m_r)                 (DB.1)

on V(M) union (Y-{y_i}).

In the TTT orientation the exact dual wall places the reverse Y-dimer after the terminal of M. Thus for every i there is again a literal Hamilton path R_i on the same support V(M) union (Y-{y_i}); only its displayed orientation is dual. The argument below uses only existence of this retained literal path and therefore applies to both HHH and TTT.

### 3. No triangle label can attach to either end of Q
Fix i. Suppose

  (y_i,q_0,q_1)                                          (DB.2)

were tight. Then

  (y_i,q_0,q_1,...,q_t)                                  (DB.3)

is a literal Hamilton path on {y_i} union V(Q): after the unique new source turn (DB.2), every later turn is inherited from Q. This path is vertex-disjoint from R_i in (DB.1), and their supports partition V(H). Hence (DB.3)|R_i is a spanning two-cover of H, contradiction.

Therefore (DB.2) is bad. Boundary antisymmetry R3 forces

  (q_1,q_0,y_i) tight.                                   (DB.4)

The terminal argument is exact dual. If

  (q_{t-1},q_t,y_i)                                      (DB.5)

were tight, then

  (q_0,...,q_{t-1},q_t,y_i)                              (DB.6)

would be Hamiltonian on V(Q) union {y_i}, again disjoint from R_i and together spanning H. Hence (DB.5) is bad and R3 gives

  (y_i,q_t,q_{t-1}) tight.                               (DB.7)

Since i was arbitrary, all three triangle vertices satisfy both (DB.4) and (DB.7).

### 4. Output
Put

  D_L=(q_1,q_0),
  D_R=(q_t,q_{t-1}).

Then every y in Y is a tail witness on the same tested orientation D_L and a head witness on the same tested orientation D_R:

  (q_1,q_0,y) tight,
  (y,q_t,q_{t-1}) tight                                  (DB.8)

for all y in Y.

Thus the anchored quiet critical-block packet forces a TWO-ENDED THREE-WITNESS REVERSE BOUNDARY WALL on the complementary rail Q. This is stronger than the two-witness alternative in `fixed-complement-triangle-source-transfer-shield`: the full witness set Y occurs at both ends, independently of the cyclic source-transfer test bits.

The proof spends the complete fixed-complement geometry. It is not a consequence of five-Hamiltonicity of Y plus two exterior vertices, and it does not assert the first-inward stars required by R974. In particular one must not silently replace (q_1,q_0,y) by (q_2,q_1,y), or (y,q_t,q_{t-1}) by (y,q_{t-1},q_{t-2}). Those one-layer propagations remain open and require additional reconstruction geometry.

Status: direct working deduction from the literal anchored packet and accepted R3. No spanning two-cover, R561 conclusion, or generic signed-payment descent is claimed.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    }
]
```
