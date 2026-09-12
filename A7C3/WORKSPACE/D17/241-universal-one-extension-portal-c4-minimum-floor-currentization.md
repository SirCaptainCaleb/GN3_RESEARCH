# The entire Sigma=10 portal-C4 floor is current in maximum-three-forest exchange space

**Workspace:** D17
**State:** established
**Key:** `universal-one-extension-portal-c4-minimum-floor-currentization`

**Summary:** Continue SV34314/SV34757. The only unconsumed Sigma=10 branch was deg_F(T)=1 with S Hamiltonian. Orient the unique mixed rail as (t0,t1,t2,u,Arest)|B, with T=(t0,t1,t2) and A=(u,Arest), so A|B is an exact two-cover of Y. Restoring s gives the actual maximum forest {s}|(T,A)|B. Since S=T+s is Hamiltonian, choose a Hamilton order Q_S; then Q_S|A|B is another actual maximum forest with the same A,B supports. Compare Q_S with T by R435. A nonmonotone comparison gives current reversal/reverse-trimer/proper-cycle geometry. Otherwise Q_S is one of the four literal insertions of s into (t0,t1,t2). Boundary insertion changes the first forest to Q_S|A|B by one explicit component transfer. The first internal insertion factors through (t0,s)|(t1,t2,u,Arest)|B; the second factors through (t0,t1,s)|(t2,u,Arest)|B. Hence every internal insertion gives an explicit length-two walk of literal maximum three-forests. Together with SV31933 for non-Hamilton S and SV34757 for degree two, every Sigma=10 C4 representative exits local C4 geometry into current maximum-forest/R435/high-transition dynamics.

### 1. The last minimum-energy cell
Retain the strict portal-C4 floor SV34314 with

  Sigma=10,
  deg_F(T)=1,
  S Hamiltonian.                                         (MF.1)

The non-Hamiltonian-S degree-one branch is already exported by SV31933, and the degree-two branch is exported by SV34757.

Orient the unique mixed F-rail so that its T-block comes first. Write

  T=(t_0,t_1,t_2),
  A=(u,a_1,...,a_r),
  F = (t_0,t_1,t_2,u,a_1,...,a_r) | B.                 (MF.2)

Here t_2u is the unique selected T|Y transition. Deleting the T-block from (MF.2) leaves

  A | B                                                   (MF.3)

as a literal two-path cover of Y. Since Y is non-Hamiltonian, (MF.3) is exact.

Restoring the deleted singleton s to F gives the actual maximum spanning three-forest

  F_0 = {s} | (t_0,t_1,t_2,u,a_1,...,a_r) | B.          (MF.4)

### 2. Hamiltonicity of S gives a second current representative
Because S=T+{s} is Hamiltonian, choose any Hamilton path Q_S on S. Pairing it with the exact residual cover (MF.3) gives another literal maximum spanning three-forest

  F_1 = Q_S | A | B.                                     (MF.5)

Compare Q_S with the inherited tight trimer T=(t_0,t_1,t_2) by accepted R435.

If the three T-contacts occur nonmonotonically in Q_S, R435 gives an exact selected reversal, reverse trimer, or proper tight cycle. The selected reversal is already literally present between current representatives (MF.4)-(MF.5); a reverse trimer is currentized by R4, and a proper cycle enters the existing movable-break orbit. Hence assume the comparison is quiet.

Then the T-contacts occur in the literal order t_0,t_1,t_2, so Q_S is exactly one of the four insertions

  (s,t_0,t_1,t_2),
  (t_0,s,t_1,t_2),
  (t_0,t_1,s,t_2),
  (t_0,t_1,t_2,s).                                     (MF.6)

### 3. Boundary insertions are one-step current exchanges
If

  Q_S=(s,t_0,t_1,t_2),

replace in F_0 the selected edge t_2u by the edge st_0. The resulting components are exactly

  (s,t_0,t_1,t_2) | A | B = F_1.                         (MF.7)

Both before and after are literal tight three-path covers, so this is an explicit one-step maximum-forest component transfer.

If

  Q_S=(t_0,t_1,t_2,s),

replace t_2u by t_2s. Again the result is exactly F_1. Thus both boundary slots give literal one-step representative switches.

### 4. First internal insertion factors through one intermediate forest
Suppose

  Q_S=(t_0,s,t_1,t_2).                                   (MF.8)

Define

  G=(t_0,s) | (t_1,t_2,u,a_1,...,a_r) | B.              (MF.9)

This is a literal spanning three-path cover: (t_0,s) is a dimer and the second rail is a contiguous subpath of the mixed rail in F_0. Hence G is another maximum spanning three-forest.

The transition F_0 -> G deletes t_0t_1 and adds t_0s. The transition G -> F_1 deletes t_2u and adds st_1. The final first rail is exactly (t_0,s,t_1,t_2), certified by (MF.8), while the split-off residual rail is A. Therefore

  F_0 -> G -> F_1                                        (MF.10)

is an explicit length-two walk of literal maximum-three-forest representatives.

### 5. Second internal insertion has its own forward intermediate
Suppose

  Q_S=(t_0,t_1,s,t_2).                                   (MF.11)

Define

  G'=(t_0,t_1,s) | (t_2,u,a_1,...,a_r) | B.             (MF.12)

The first rail is tight because (t_0,t_1,s) is a certified turn of Q_S; the second is a contiguous subpath of the original mixed rail. Thus G' is an actual maximum three-forest.

The transition F_0 -> G' deletes t_1t_2 and adds t_1s. The transition G' -> F_1 deletes t_2u and adds st_2. The resulting first rail is exactly (t_0,t_1,s,t_2), and the residual A=(u,a_1,...,a_r) is split off literally. Hence

  F_0 -> G' -> F_1                                       (MF.13)

is another explicit length-two current walk. No path reversal is used anywhere.

### 6. Floor currentization
Therefore every Hamilton-S degree-one Sigma=10 cell gives either

1. explicit current R435 geometry between actual maximum forests, or
2. a literal maximum-forest representative switch of length at most two from the singleton-rooted representative F_0 to the core-rooted representative F_1.

Combining this with SV31933 and SV34757, the entire minimum portal-C4 energy floor

  Sigma=10                                                (MF.14)

is currentized out of static C4 geometry. No Sigma=10 representative can be a terminal local obstruction.

Consequently, after quotienting these explicit current exits, the surviving portal-C4 extinction problem begins strictly above the floor, at Sigma>=12. The next target is to show that an energy-minimal Sigma>=12 representative admits a strict representative-improving move or forces the endpoint-port / maximum-forest holonomy consumers.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R4"
    },
    {
        "relation": "dependency",
        "revision_id": "R435"
    }
]
```