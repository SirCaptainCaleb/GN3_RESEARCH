# The degree-two core block at the portal-C4 energy floor exports completely to current maximum-forest or high-transition dynamics

**Workspace:** D17
**State:** established
**Key:** `universal-one-extension-portal-c4-minimum-degree2-export`

**Summary:** Continue SV34314 in the Sigma=10, deg_F(T)=2 branch. After cyclic relabelling the exact H-s cover contains a literal Hamilton P5 Q=a-T-b on K_ab with endpoints a,b. The endpoint replacements S+b=(K_ab-a)+s and S+a=(K_ab-b)+s are Hamiltonian. R966 with exterior s gives either a Hamilton six-set U=S+a+b or explicit R435. If U is Hamiltonian, any Hamilton P6 on U is a proper path and R4 currentizes it directly to an actual maximum spanning three-forest. Reverse-trimer R435 output is likewise a proper path and currentizes by R4; proper-cycle output enters the existing movable-break closed orbit. For selected reversal between two neighboring P5 supports inside U, let D be the reversed common dimer, let x,y be the exchanged labels, let C=U-{x,y}-D (two vertices), and E=V(H)-U. If E is Hamiltonian, the two P5s pair with the same E in exact singleton-deletion rows and the fixed-complement selected-reversal currentization/transport applies. If E is non-Hamiltonian, every exact H-D two-cover has at least three transitions across C,{x},{y},E by the block identity b_C+b_x+b_y+b_E=2+tau with lower bounds 1,1,1,2. Thus the whole degree-two minimum-energy cell exits to actual/closed maximum-forest dynamics, fixed-complement reversal transport, or a universal high-transition common-dimer portal.

### 1. Input from the strict energy floor
Retain `universal-one-extension-portal-c4-strict-energy-floor` SV34314 in its minimum-energy branch

  Sigma=10,
  deg_F(T)=2.

After cyclic relabelling, the two neighbors of the contiguous T-block are adjacent rim labels a,b, and one literal F-rail contains the contiguous Hamilton five-path

  Q = a - T - b                                           (DE.1)

on

  K_ab=T+{a,b}.

The endpoints of Q are the physical labels a,b.

The universal-one-extension hypothesis gives Hamilton paths on the two endpoint-replacement supports

  (K_ab-{a})+s = S+b,
  (K_ab-{b})+s = S+a.                                    (DE.2)

### 2. Apply accepted R966
Apply accepted R966 to the base path Q with exterior vertex s and the two replacement supports (DE.2).

There are two parent outcomes.

#### Hamilton extension
If

  U:=S+{a,b}=K_ab+{s}                                    (DE.3)

is Hamiltonian, choose any Hamilton P6 on U. Since U is a proper subset of H in the surviving k>=8 range, accepted R4 supplies an exact two-cover of H-U. Restoring the P6 gives a literal spanning maximum three-forest containing U as one rail.

Thus the Hamilton-extension branch of R966 is already an ACTUAL representative export. It is not a static local exception.

#### Explicit R435 geometry
Otherwise R966 supplies an explicit R435 output in one of the three comparisons among Q and the two endpoint-replacement paths.

A reverse-trimer output is a proper graph-intrinsic tight path, hence R4 currentizes it to an actual maximum spanning three-forest.

A proper-cycle output enters the existing movable-break maximum-three-forest orbit of SV25652.

It remains only to currentize a selected-state reversal.

### 3. Generic currentization of the selected-reversal species
Retain two Hamilton P5s P_x,P_y on neighboring supports inside the six-set U which differ by exchanged labels x,y and which select one common physical dimer

  D={p,q}

in opposite directions. Their common support has four vertices. Put

  C=U-{x,y,p,q},
  E=V(H)-U.                                             (DE.4)

Thus |C|=2 and E is nonempty in the surviving range.

There are two graph-intrinsic cases.

#### E Hamiltonian
Choose a Hamilton path B on E. Then

  P_x | B,
  P_y | B                                               (DE.5)

are exact singleton-deletion rows on the two exchanged deletion fibers. Exactness follows because a Hamilton singleton deletion together with the deleted singleton would two-cover H.

The two rows have one literal common Hamilton complement B and retain the named opposite selection of D. Therefore `fixed-complement-r435-adjacent-reversal-pair-deletion-currentization` applies. If an exchanged label is internal, the reversal emits a fresh pair-deletion maximum-three-forest portal. If both are endpoints, trimming them gives two exact covers of one common pair-deletion residue with identical support partition and literal complement B selecting D oppositely; `fixed-complement-selected-reversal-normal-form` then transports the named reversal monotonically toward R561 or named wrap shields.

#### E non-Hamiltonian
Let G be an arbitrary exact two-cover of H-D, supplied by R4 after deleting the proper dimer D. Partition its vertices into the four nonempty classes

  C | {x} | {y} | E.                                   (DE.6)

Let tau(G) be the number of selected G-edges between different classes and b_Z the number of maximal contiguous blocks of class Z in the two G-rails. Elementary path-block counting gives

  b_C+b_x+b_y+b_E = 2+tau(G).                           (DE.7)

Here

  b_C>=1,
  b_x=b_y=1,
  b_E>=2                                                   (DE.8)

because C is nonempty, x,y are singleton classes, and E is non-Hamiltonian. Hence

  tau(G)>=3.                                             (DE.9)

Since G was arbitrary, every exact H-D cover has at least three transitions across (DE.6). Restoring the dimer D makes D|G an actual maximum spanning three-forest, so this is a UNIVERSAL HIGH-TRANSITION common-dimer deletion portal.

### 4. Degree-two floor extinction as a local object
Consequently the entire

  Sigma=10, deg_F(T)=2                                  (DE.10)

portal-C4 cell exits local C4 geometry into one of:

1. an actual maximum three-forest containing a Hamilton P6 on S+a+b;
2. an actual maximum forest from a reverse trimer;
3. a closed movable-break maximum-forest orbit from a proper cycle;
4. fixed-complement selected-reversal transport / fresh pair-deletion maximum forest;
5. a universal 3+-transition common-dimer deletion portal.

No new bounded C4 obstruction survives in (DE.10). The only minimum-energy portal-C4 cell not consumed here is the degree-one T-block branch, whose non-Hamiltonian-S subcase is already exported by SV31933 and whose Hamiltonian-S subcase is governed by accepted R570 one-sided boundary rigidity.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R4"
    },
    {
        "relation": "dependency",
        "revision_id": "R966"
    }
]
```
