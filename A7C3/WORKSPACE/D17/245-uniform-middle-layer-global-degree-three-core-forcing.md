# Every Arm-M endpoint system contains a degree-three core, so the whole uniform layer enters the three parent holonomies

**Workspace:** D17
**State:** established
**Key:** `uniform-middle-layer-global-degree-three-core-forcing`

**Summary:** In R927 Arm M, take the complete all-endpoint incidence graph whose left side is every k-subset of V(H), all Hamiltonian, and whose right side consists of realized endpoint-deletion (k-1)-cores. The full left family is Hall-deficient because C(2k+1,k)>C(2k+1,k-1), while all right vertices are (k-1)-sets. Choose an inclusion-minimal deficient family F. Accepted R934 gives |N(F)|=|F|-1 and degree at least two at every right core. Every left support also has degree at least two, since any Hamilton path has two distinct endpoints and therefore two distinct endpoint-deletion cores. If every right core had degree exactly two, edge counting would give |E|=2|N|=2|F|-2 but also |E|>=2|F|, impossible. Hence some right core R has degree at least three, meaning there are three distinct completion labels x,y,z for which R+p has a Hamilton path exposing p as an endpoint. Thus the degree-three Johnson-face router SV35204 applies in every surviving Arm-M system. Its forbidden P_(k+1) output is impossible by Arm M, so the entire uniform layer is globally reduced to only three parent destinations: the same-role three-port spindle entrance, a universally one-extendable four-set, or current/closed maximum-three-forest and component-recompletion dynamics. No extinction of those three parent outputs is claimed.

### 1. Complete endpoint incidence in Arm M
Assume accepted R927 Arm M:

  |V(H)|=2k+1,
  every k-set is Hamiltonian,
  no (k+1)-set is Hamiltonian.                            (GF.1)

The case k=2 is impossible already from R3: every three-set has one tight orientation in each complete-reversal pair and therefore has a tight Hamilton P3. Hence in the live Arm-M range k>=3.

Form the COMPLETE all-endpoint incidence graph B. Its left side L consists of every k-subset S of V(H). For every actual Hamilton path on S and every physical endpoint p of that path, join S to the right core

  R=S-{p}.                                                (GF.2)

Right vertices are therefore realized (k-1)-subsets. All actual endpoint realizations are retained.

### 2. The complete system is automatically Hall-deficient
There are

  |L| = binom(2k+1,k)                                    (GF.3)

left supports. Every right vertex is a (k-1)-set, so even before asking which such sets are realized,

  |N(L)| <= binom(2k+1,k-1).                             (GF.4)

But

  binom(2k+1,k) / binom(2k+1,k-1) = (k+2)/k > 1.         (GF.5)

Hence

  |N(L)| < |L|.                                          (GF.6)

Thus the complete endpoint system itself violates Hall. Choose an inclusion-minimal nonempty Hall-deficient left family

  F subseteq L,
  N=N(F).                                                (GF.7)

### 3. Minimal Hall deficiency forces a right core of degree at least three
Apply accepted R934 to F. Its factor-critical Hall structure gives

  |N|=|F|-1,                                             (GF.8)

and every right core R in N has at least two support neighbors.

On the other hand every left support S in F also has degree at least two. Indeed choose any actual Hamilton path on S. Its two physical endpoints p!=q give the two distinct endpoint-deletion cores

  S-{p},
  S-{q}.                                                 (GF.9)

Because the incidence graph is complete over all actual endpoint realizations, both are neighbors of S. Therefore

  deg_B(S)>=2 for every S in F.                          (GF.10)

Suppose for contradiction every right core had degree exactly two. Double-counting the incidence edges gives from the right side

  |E(B[F,N])| = 2|N| = 2(|F|-1)=2|F|-2,                (GF.11)

while the left-degree bound gives

  |E(B[F,N])| >= 2|F|.                                  (GF.12)

Contradiction. Hence some right core R satisfies

  deg_B(R)>=3.                                           (GF.13)

### 4. Right degree three is exactly a three-port endpoint core
Choose three distinct support neighbors S_x,S_y,S_z of R. Since |R|=k-1 and each S_p has order k,

  S_x=R+{x},
  S_y=R+{y},
  S_z=R+{z}                                             (GF.14)

for three distinct physical completion labels x,y,z outside R.

The incidence S_p-R means, by definition of the complete endpoint graph, that there is an ACTUAL Hamilton path on R+p exposing p as a physical endpoint. Thus R is precisely a degree-three endpoint core in the sense of SV34534/SV35204.

No PORT-SWITCH, PAIR-SWITCH, rigid-bicycle classification, or off-circuit replacement is needed to obtain this three-port core. It is forced by the raw deficiency-one edge count.

### 5. Global uniform-layer router
Apply the degree-three parent router SV35204 to R and three chosen completion labels x,y,z. That theorem sends the Johnson face to one of:

1. a forbidden tight P_(k+1);
2. the same-role three-port spindle entrance;
3. a universally one-vertex Hamilton-extendable four-set;
4. actual or closed maximum-three-forest / component-recompletion dynamics.   (GF.15)

Alternative 1 is excluded by the defining Arm-M condition (GF.1). Consequently every surviving Arm-M system globally enters one of only three parent programs:

  THREE-PORT SPINDLE,
  UNIVERSAL ONE-EXTENSION FOUR-CORE,
  CURRENT MAXIMUM-THREE-FOREST HOLONOMY.                 (GF.16)

This turns the local Johnson-overlap moonshot into a global reduction of the entire uniform layer. It does not extinguish Arm M by itself: the three parent consumers in (GF.16) remain to be closed. But no separate Hall-circuit or Johnson-triangle residue is needed as a fourth terminal branch.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R927"
    },
    {
        "relation": "dependency",
        "revision_id": "R934"
    }
]
```