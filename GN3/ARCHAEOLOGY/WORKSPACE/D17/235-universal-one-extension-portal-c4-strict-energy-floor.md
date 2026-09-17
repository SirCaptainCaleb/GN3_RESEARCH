# In the surviving k>=8 portal C4, four-cut energy is at least ten and its minimum cell has one fragmented W block pair

**Workspace:** D17
**State:** established
**Key:** `universal-one-extension-portal-c4-strict-energy-floor`

**Summary:** In R927 Arm M with k>=8, retain a portal-only shortest pair-core C4 and any exact H-s cover F. Let Sigma be the sum of the four perimeter cut crossing counts, q the number of inter-type transitions among T,W,a,b,c,d, and f the number of selected transitions joining the three antipodal type pairs T-W,a-c,b-d. If B is the total number of maximal type blocks, then B=2+q and Sigma=2q+2f=8+2(B-6)+2f. Since |W|=2k-7>k while each exact H-s rail has order k, W cannot be one contiguous block; hence B>=7 and Sigma>=10. Equality Sigma=10 forces f=0, exactly seven type blocks, W as the unique fragmented type with exactly two blocks, every other type contiguous, and one W block on each rail. The T block has degree one or two. Degree one is the unique T|Y crossing cell: if S is non-Hamiltonian it exports by SV31933 to a fresh maximum three-forest; if S is Hamiltonian accepted R570 gives the exact one-sided Hamilton-boundary rigidity / R435-collision alternative. Degree two forces the two neighbors of T to be adjacent rim labels, since opposite neighbors Hamiltonize a forbidden diagonal. Thus, after rotation, F contains a literal five-vertex segment a-T-b spanning K_ab with endpoints a,b. Since S+a and S+b are Hamiltonian endpoint replacements, accepted R966 applies with exterior vertex s: either S+a+b is Hamiltonian or explicit R435 geometry occurs. Therefore the minimum-energy C4 cell is reduced to unique-crossing rigidity/fresh forest, explicit R435, or a Hamilton six-extension S+a+b.

### 1. Setup and four-cut energy
Retain accepted R927 Arm M with

  |V(H)|=2k+1,
  every k-set Hamiltonian,
  no (k+1)-set Hamiltonian,

and retain a surviving portal-only shortest pair-core quadrilateral in the range k>=8. Write

  T=S-{s},
  rim a,b,c,d cyclically,
  W=Y-{a,b,c,d}.

Thus the four perimeter five-supports

  K_ab=T+{a,b}, K_bc=T+{b,c}, K_cd=T+{c,d}, K_da=T+{d,a}

are Hamiltonian, the two diagonals T+{a,c}, T+{b,d} are non-Hamiltonian, and every perimeter edge is PORTAL.

Fix an arbitrary literal exact two-cover F of H-s. By Arm M both F-rails have order exactly k. Let tau_ab,tau_bc,tau_cd,tau_da be the four portal-cut crossing counts and put

  Sigma=tau_ab+tau_bc+tau_cd+tau_da.

Use the six physical membership types T,W,a,b,c,d from SV32358. For a selected F-edge joining different types, its contribution to Sigma is the Hamming distance of their four cut-membership vectors, hence either 2 or 4. The distance-four pairs are exactly

  T-W, a-c, b-d.

Let q(F) be the number of selected inter-type F-edges and let f(F) be the number among them joining one of these three distance-four pairs.

### 2. Exact energy identity
Split the two F-rails into maximal contiguous blocks of the six types. Let B(F) be the total number of such nonempty blocks. Every inter-type selected edge increases the total block count by one, so

  B(F)=2+q(F).                                      (EF.1)

Every inter-type edge contributes its baseline 2 to Sigma, and each distance-four edge contributes two additional units. Therefore

  Sigma=2q(F)+2f(F)
       =8+2(B(F)-6)+2f(F).                          (EF.2)

This is an exact identity, not merely the lower bound Sigma>=8.

### 3. The large W type forces strict excess
Here

  |W|=|Y|-4=(2k-3)-4=2k-7.

For k>=8,

  |W|=2k-7>k.                                       (EF.3)

If W occurred as one contiguous F-block, that whole block would lie on one F-rail, impossible because each rail has only k vertices. Hence W is fragmented and

  B(F)>=7.                                          (EF.4)

Combining (EF.2) and (EF.4),

  Sigma>=10.                                        (EF.5)

Thus the surviving large-order portal C4 has strict octahedral excess in EVERY exact H-s representative.

### 4. Exact normal form at Sigma=10
Assume Sigma=10. By (EF.2),

  (B(F)-6)+f(F)=1.                                  (EF.6)

Because W is fragmented, B(F)-6>=1, so necessarily

  B(F)=7,
  f(F)=0.                                           (EF.7)

Therefore:

1. every inter-type selected edge has Hamming weight two;
2. there is exactly one extra type block beyond the six nonempty types;
3. W is the unique fragmented type, with exactly two blocks;
4. T,a,b,c,d each occur as one contiguous block.

Moreover each F-rail contains exactly one W-block. If both W-blocks lay on the same rail, the other rail would contain only vertices from T+a+b+c+d, altogether seven vertices, contradicting its required order k>=8.

So the Sigma=10 quotient is a seven-block two-path forest with one W-block on each rail and five pure octahedral transitions.

### 5. The T-degree split
Since T is one contiguous block, the number

  e_F(T,Y)

of selected T|Y transitions is exactly the degree of the T-block in the seven-block quotient. It is nonzero by the universal cut fan SV31933 and at most two because F is a path forest. Hence

  deg_F(T) in {1,2}.                                (EF.8)

#### Degree one
If deg_F(T)=1, F has exactly one T|Y transition.

If S is non-Hamiltonian, SV31933 applies exactly and produces an actual fresh maximum spanning three-forest by moving from the singleton-deletion coordinate s to the universal-extension coordinate at the Y-endpoint of the unique crossing.

If S is Hamiltonian, accepted R570 applies with deleted set D={s}, absorber block T, complement Y, and absorber X=S. Thus outside its explicit same-oriented crossing-collision / R435 output, the unique-crossing cell is one-sided Hamilton-boundary rigid: the opposite augmented side is non-Hamiltonian and the relevant Hamilton boundary multiplicity of S is at most one. No closure is asserted in this subcase.

#### Degree two
Assume deg_F(T)=2 and let x,y be its two neighboring type blocks. T cannot have opposite rim neighbors a,c or b,d, because then the literal quotient segment

  x - T - y

is itself a Hamilton tight path on the forbidden diagonal five-support T+{x,y}. Therefore x,y are adjacent rim labels. After cyclic relabelling they are a,b.

Consequently one F-rail contains a literal contiguous five-vertex segment

  a - T - b                                            (EF.9)

or its reversal, spanning K_ab and exposing a,b as the two endpoints of that segment.

The universal-one-extension hypothesis supplies Hamilton paths on

  S+a = (K_ab-{b})+s,
  S+b = (K_ab-{a})+s.

Thus accepted R966 applies to the Hamilton base path (EF.9) with exterior vertex s and its two endpoint-replacement supports. Therefore exactly one of the following occurs:

  S+a+b is Hamiltonian,                                (EF.10)

or at least one of the three comparisons among the base K_ab path and the two endpoint-replacement paths emits explicit R435 geometry: a selected reversal, reverse trimer, or proper tight cycle.

### 6. Minimum-energy consequence
Every Sigma=10 portal-C4 representative in the surviving k>=8 Arm-M range is therefore reduced to one of three theorem-sized destinations:

1. unique T|Y crossing, hence fresh maximum-forest export when S is non-Hamiltonian and accepted R570 rigidity / explicit interaction when S is Hamiltonian;
2. explicit R435 output from the endpoint-controlled perimeter segment;
3. a Hamilton six-extension S+a+b containing one perimeter support K_ab.

The only genuinely new minimum-energy cell not already routed into mature currentization machinery is therefore the Hamilton six-extension alternative (EF.10), together with the interaction-free Hamilton-S degree-one rigidity cell. No claim is made here that Sigma>10 is impossible or that either remaining cell closes H.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R927"
    },
    {
        "relation": "dependency",
        "revision_id": "R570"
    },
    {
        "relation": "dependency",
        "revision_id": "R966"
    }
]
```
