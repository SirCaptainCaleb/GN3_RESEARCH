# The opposite-role degree-three core hexagon has universal-core or boundary-P4 curvature

**Workspace:** D17
**State:** established
**Key:** `uniform-middle-layer-opposite-core-label-curvature`

**Summary:** In the fully quiet opposite-role degree-three-core residue of SV34534, normalize P_p=(p,K_R) on R+p and Q_p=(K_W,p) on W+p for p in {x,y,z}, with K_R=(r0,...,rm) and K_W=(w0,...,wm). For any tight ordering J=(a,b,c) of the three labels, the spanning three-cover K_R|K_W|J forces two exact boundary blockers: (r0,c,b) and (b,a,wm) are tight, since otherwise J+K_R or K_W+J would merge with the untouched opposite core into a spanning two-cover. Now inspect the comparison tournament on the three ordinary label edges xy,xz,yz. If it is cyclic, the directed comparison triangle persists in every five-set {x,y,z,r0,d}; R887/R902 therefore make {x,y,z,r0} universally one-vertex Hamilton-extendable. If it is transitive, let {uv} be the middle comparison edge and t the third label, so (t,v,u) and (v,u,t) are tight. The two blocker formulas give (r0,u,v) and (u,v,wm), hence the literal tight P4 (r0,u,v,wm). Its complement retains the explicit three-path cover K_R-r0 | K_W-wm | {t}, while R4 supplies an exact two-cover of that same complement and hence an actual maximum three-forest containing the P4. Thus the fully quiet opposite-role hexagon always exits to the universal-core program or to a structured current 3-to-2 complement recompletion / maximum-forest portal; it is not terminal holonomy.

### 1. Opposite-role complementary-core residue
Retain the fully quiet opposite-role residue of `uniform-middle-layer-degree-three-core-complementary-hexagon` SV34534 in accepted R927 Arm M. Thus

  V(H)=R disjoint_union W disjoint_union {x,y,z},
  |R|=|W|=k-1,

and after duality there are literal core orders

  K_R=(r_0,r_1,...,r_m),
  K_W=(w_0,w_1,...,w_m),
  m=k-2,

such that for every completion label p in {x,y,z},

  (p,K_R) is Hamiltonian on R+p,
  (K_W,p) is Hamiltonian on W+p.                         (LC.1)

The point of this section is to consume this residue directly, before any R579 wrap normalization.

### 2. Every tight label trimer forces two opposite core-boundary blockers
Choose ANY tight ordering

  J=(a,b,c)

of the three labels {x,y,z}. Such an ordering exists because every three-vertex induced system has a tight trimer orientation.

The three paths

  K_R | K_W | J                                           (LC.2)

form a literal spanning three-cover of H.

Because c is a source completion of K_R, the turn

  (c,r_0,r_1)

is tight. Consider the spanning two-path proposal

  (a,b,c,r_0,r_1,...,r_m) | K_W.                         (LC.3)

Every consecutive turn of its first rail is certified either by J, by K_R, or by (c,r_0,r_1), except possibly

  (b,c,r_0).

If (b,c,r_0) were tight, (LC.3) would be a spanning two-cover of H, contradiction. Hence (b,c,r_0) is bad, and R3 gives

  (r_0,c,b) tight.                                       (LC.4)

Dually, a is a terminal completion of K_W, so

  (w_{m-1},w_m,a)

is tight. The proposal

  K_R | (w_0,...,w_m,a,b,c)                              (LC.5)

has only the possible new hole (w_m,a,b). Therefore this turn is bad and R3 gives

  (b,a,w_m) tight.                                       (LC.6)

Thus EVERY tight label order J=(a,b,c) carries the two graph-intrinsic boundary blockers (LC.4)-(LC.6).

### 3. The label comparison tournament is cyclic or transitive
Apply the comparison-orientation viewpoint R887 to the three ordinary label edges

  xy, xz, yz.

They are the three vertices of a tournament. There are exactly two isomorphism types: a directed triangle or a transitive tournament.

#### 3a. Cyclic label comparison gives a universal one-extension four-core
Suppose the three label edges form a directed comparison triangle. This same directed comparison cycle remains present after adjoining arbitrary further vertices.

Put

  X={x,y,z,r_0}.

For every d outside X, the five-set X+d is nonintegrable because its comparison orientation still contains the directed label triangle. Accepted R902 says every non-Hamiltonian five-vertex boundary tournament is edge-orderable, so contrapositively every nonintegrable five-set is Hamiltonian. Hence

  X+d is Hamiltonian for every d outside X.              (LC.7)

Therefore X is a universally one-vertex Hamilton-extendable four-set. This exits directly to the universal-core absorber program.

#### 3b. Transitive label comparison gives a literal boundary P4
Suppose instead the label-edge comparison tournament is transitive. Let uv be its unique middle edge and let t be the third label. Orient u,v so the unique directed length-two comparison chain is

  tv -> vu -> ut.

Equivalently, the two label orders

  (t,v,u),
  (v,u,t)                                                 (LC.8)

are tight.

Apply (LC.4) to J=(t,v,u). Here b=v,c=u, so

  (r_0,u,v) is tight.                                    (LC.9)

Apply (LC.6) to J=(v,u,t). Here a=v,b=u, so

  (u,v,w_m) is tight.                                    (LC.10)

The two turns concatenate to the literal vertex-simple tight P4

  B=(r_0,u,v,w_m).                                       (LC.11)

### 4. The transitive curvature is immediately current
The complement of B retains the literal three-path cover

  (r_1,...,r_m) | (w_0,...,w_{m-1}) | {t}.              (LC.12)

Singleton pieces are allowed when k is small. This cover is not asserted to be minimum.

Because B is a proper graph-intrinsic tight path, accepted smallest-counterexample minimality R4 supplies an exact two-cover

  U | V

of H-B. Hence

  B | U | V                                               (LC.13)

is an actual maximum spanning three-forest of H. The original three components in (LC.12) are retained simultaneously as the explicit finer complement decomposition against which this exact recompletion can be compared.

Thus the transitive label case is not a static local sign packet: it is a concrete current 3-to-2 complement recompletion with the physical boundary vertices r_0,w_m, the middle label dimer uv, and the spare third label t all retained.

### 5. Johnson-curvature consequence
The fully quiet opposite-role degree-three-core hexagon of SV34534 has no terminal purely quiet state. Its label comparison tournament forces exactly one of two parent-scale exits:

1. CYCLIC CURVATURE: a universally one-extendable four-set {x,y,z,r_0};
2. TRANSITIVE CURVATURE: the literal boundary P4 (r_0,u,v,w_m), together with both the explicit three-component complement (LC.12) and an exact two-cover of that same complement from R4.

No Arm-M closure is claimed here. The gain is that the last fully quiet Johnson-triangle residue is consumed without additional wrap classification: it feeds either the universal-core lane or the actual maximum-three-forest / component-recompletion lane.

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
        "revision_id": "R887"
    },
    {
        "relation": "dependency",
        "revision_id": "R902"
    }
]
```
