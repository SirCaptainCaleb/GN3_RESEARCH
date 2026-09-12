# The portal-only pair-core quadrilateral at k=6 or 7 is already a fixed-complement critical block

**Workspace:** D17
**State:** established
**Key:** `universal-one-extension-portal-c4-arm-m-k67-critical-block-export`

**Summary:** In R927 Arm M, let U=T+{a,b,c,d} be the seven-vertex union of a shortest pair-core C4. Donor edges are absent in the surviving uniform arm. If k=6, then |U|=7=k+1, so U is non-Hamiltonian and every U-x is a Hamiltonian k-set, while its complement E has order k and is Hamiltonian. Thus U is a fixed-complement deletion-Hamiltonian critical block and SV30477 exports it to universal-core or maximum-forest holonomy. If k=7, the roles reverse: U has order k and is Hamiltonian, while E has order k+1, is non-Hamiltonian, and every E-x is Hamiltonian; again SV30477 applies. Hence no genuinely new portal-C4 local obstruction occurs at k=6 or 7. Combined with triangle extinction SV33654 and the SV32358 high-transition dichotomy, any remaining local universal-core C4 in Arm M must have k>=8, n>=17, be portal-only, and force a 3+-transition perimeter cut in every exact H-s representative.


### 1. Uniform portal-only quadrilateral setup
Retain accepted R927 alternative (M):

  |V(H)|=2k+1,
  every k-set is Hamiltonian,
  no (k+1)-set is Hamiltonian.                             (K67.1)

Retain a shortest universal-core pair-core quadrilateral from SV32358. Thus for one core label s, with

  T=S-{s},  |T|=3,

and four exterior rim labels a,b,c,d, the four perimeter five-supports

  T+{a,b}, T+{b,c}, T+{c,d}, T+{d,a}                     (K67.2)

are Hamiltonian while the diagonals T+{a,c},T+{b,d} are non-Hamiltonian. In the surviving Arm-M regime donor edges are absent: SV30682 says any donor edge forces k=5, and accepted R957 eliminates that order-eleven uniform residue. Hence the bounded nucleus is portal-only.

Put

  U=T union {a,b,c,d}.                                    (K67.3)

Then |U|=7. Let

  E=V(H)-U,                                                (K67.4)

so |E|=2k-6. Notice that E contains the omitted core label s together with every exterior vertex not among a,b,c,d.

### 2. k=6: U is the critical block and E is its Hamilton complement
Assume k=6. Then |V(H)|=13 and

  |U|=7=k+1,
  |E|=6=k.                                                 (K67.5)

By (K67.1), U is non-Hamiltonian. For every x in U, the puncture U-x has order six and is therefore Hamiltonian. Hence U is a non-Hamiltonian deletion-Hamiltonian critical block.

Also E has order k and is Hamiltonian. Choose and retain one literal Hamilton path Q_E on E. Therefore

  V(H)=U disjoint_union E                                 (K67.6)

is exactly the fixed-complement critical-block setting of SV30477, with critical block Omega=U and literal Hamilton complement Q_E.

Consequently the entire k=6 quadrilateral configuration already exports, by SV30477, to

  a universally one-extendable four-set,
  or actual/closed maximum-three-forest holonomy.          (K67.7)

There is no independent k=6 portal-C4 local residue.

### 3. k=7: E is the critical block and U is its Hamilton complement
Assume k=7. Then |V(H)|=15 and

  |U|=7=k,
  |E|=8=k+1.                                               (K67.8)

Now U is Hamiltonian by (K67.1); retain one literal Hamilton path Q_U on U.

The set E has order k+1 and is therefore non-Hamiltonian. For every x in E, E-x has order seven=k and is Hamiltonian. Hence E is a non-Hamiltonian deletion-Hamiltonian critical block.

Thus

  V(H)=E disjoint_union U                                 (K67.9)

is again exactly the SV30477 fixed-complement setting, this time with critical block Omega=E and literal Hamilton complement Q_U. Therefore the k=7 quadrilateral also exports to the two global destinations in (K67.7).

There is no independent k=7 portal-C4 local residue.

### 4. Order floor for genuinely new high-transition C4 holonomy
SV32358 shows that in Arm M every exact H-s representative of a portal-only C4 either produces a trimer rail or has some perimeter portal cut with at least three selected crossings; the trimer alternative is impossible in Arm M at the present orders. Sections 2-3 now remove k=6 and k=7 from the local C4 program altogether by fixed-complement critical-block routing.

Therefore any portal-only high-transition quadrilateral which is not already exported through the completed fixed-complement router must satisfy

  k>=8,
  |V(H)|=2k+1>=17.                                        (K67.10)

Together with SV33654, which extinguishes the pair-core triangle locally, this leaves one bounded universal-core local shape in the surviving uniform arm:

  portal-only C4,
  k>=8,
  and every exact H-s two-cover has some perimeter portal cut of transition multiplicity at least three.  (K67.11)

This is a parent reduction, not extinction of the high-transition C4 and not closure of Arm M.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R927"
    },
    {
        "relation": "dependency",
        "revision_id": "R957"
    }
]
```
