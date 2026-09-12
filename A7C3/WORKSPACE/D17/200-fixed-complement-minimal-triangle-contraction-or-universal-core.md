# A quiet endpoint-return triangle contracts the common complement or promotes to a universal Hamilton four-core

**Workspace:** D17
**State:** established
**Key:** `fixed-complement-minimal-triangle-contraction-or-universal-core`

**Summary:** In the R961 quiet constant-role triangle of a fixed-complement critical block, classify each matched endpoint incidence by the transfer/blocker compiler. In HHH, if all three incidences transfer, SV24412 transports the triangle family through the double-prefix push to exact rows with common complement Q[2,t], yielding either shorter-complement R435 activity or the retained minimal triangle there. If any incidence blocks, say y_i->y_{i+1}, non-Hamiltonicity of Omega reverses the forward triangle turn to (y_i,y_{i+2},y_{i+1}), while the blocker is (y_{i+2},y_{i+1},q0); hence (y_i,y_{i+2},y_{i+1},q0) is a Hamilton P4 on Y+q0. The three reversed cyclic turns on Y form a directed comparison triangle, so every five-set Y+q0+d is nonintegrable and therefore Hamiltonian by R902. Thus Y+q0 is a universal Hamilton four-core. TTT is dual with qt. Therefore minimal quiet endpoint-return holonomy has only two parent-scale exits: strict common-complement contraction or universal-core promotion.


### 1. Constant-role minimal holonomy
Retain a fixed-complement critical block

  V(H)=Omega disjoint_union V(Q),
  Q=(q_0,q_1,...,q_t),

with Omega non-Hamiltonian and deletion-Hamiltonian. Apply accepted R961. Work in its R435-quiet residual branch. Then the extremal endpoint-return cycle is a directed triangle

  Y={y_0,y_1,y_2},

and all three matched endpoint roles are equal. Treat HHH; TTT is the exact terminal dual. R961 gives one common literal Hamilton order M on Omega-Y and actual puncture paths

  P_i=(y_{i+1},y_{i+2},M),                         (MH.1)

indices modulo three.

Because Omega is non-Hamiltonian, the missing label y_i cannot be prepended to P_i. Hence

  (y_i,y_{i+1},y_{i+2}) is bad,

so R3 gives

  (y_{i+2},y_{i+1},y_i) tight                         (MH.2)

for every i. The three turns (MH.2) are exactly a directed comparison triangle on the three ordinary edges of Y.

### 2. If all three incidences transfer, the common complement contracts
Apply the HEAD transfer/blocker compiler `fixed-complement-endpoint-return-transfer-compiler` SV23560 to the three matched incidences y_i->y_{i+1} realized by (MH.1).

If all three take the TRANSFER branch, `fixed-complement-transfer-cycle-holonomy-contraction` SV24412 applies. Every row double-prefix pushes q_0,q_1 into its active puncture support and pairs with the strictly shorter literal complement

  Q^{(2)}=Q[2,t].

If some adjacent pushed comparison is R435-active, the source-visible holonomy has therefore been transported to a family with common complement shorter by two. If all three pushed comparisons remain quiet, SV24412 retains the physical directed triangle as the minimal holonomy of that contracted family. In either case the all-transfer branch is a genuine common-complement contraction, not a new local packet.

### 3. One blocker Hamiltonizes the triangle plus the boundary vertex
Suppose instead that at least one matched incidence blocks. Choose i with y_i->y_{i+1} in the BLOCKER branch. Since P_i begins

  (y_{i+1},y_{i+2},...),

the failed transfer turn is

  (q_0,y_{i+1},y_{i+2}) bad.

R3 gives the retained blocker

  (y_{i+2},y_{i+1},q_0) tight.                         (MH.3)

Now use (MH.2) with index i+1:

  (y_i,y_{i+2},y_{i+1}) tight.                         (MH.4)

The two certified turns (MH.4) and (MH.3) concatenate to the literal Hamilton P4

  K_i=(y_i,y_{i+2},y_{i+1},q_0)                       (MH.5)

on the four-set

  X=Y union {q_0}.

Thus X is Hamiltonian.

### 4. The blocker P4 is automatically a universal Hamilton four-core
The directed comparison triangle (MH.2) on Y survives inside every five-set

  X union {d}=Y union {q_0,d}

with d outside X. Hence that five-set is nonintegrable. Accepted R902 says every nonintegrable five-vertex boundary tournament is Hamiltonian. Therefore

  X+d is Hamiltonian for every d outside X.            (MH.6)

Together with (MH.5), X=Y+q_0 is a universal Hamilton four-core: it is Hamiltonian and Hamilton-extends by every exterior vertex.

No endpoint prescription is asserted for the extensions in (MH.6).

### 5. Parent-scale dichotomy
Consequently the entire quiet HHH endpoint-return triangle has only two parent-scale exits:

1. COMMON-COMPLEMENT CONTRACTION: all three matched incidences transfer, and the cycle currentizes over Q[2,t] by SV24412; or
2. UNIVERSAL-CORE PROMOTION: at least one incidence blocks, and Y+q_0 is a universal Hamilton four-core.

The TTT case gives the exact dual with Y+q_t.

This does not prove full Critical-Block Complement Absorption, because universal Hamilton four-core absorption remains a global consumer and the R435-active branch of R961 is not addressed here. The gain is that the minimal R435-quiet holonomy no longer has any independent blocker residue: it either contracts the fixed complement or exits to a pre-existing grand parent structure.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R902"
    },
    {
        "relation": "dependency",
        "revision_id": "R961"
    }
]
```
