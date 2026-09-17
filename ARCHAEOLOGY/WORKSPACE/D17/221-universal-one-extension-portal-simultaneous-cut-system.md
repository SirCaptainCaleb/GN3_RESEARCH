# Portal edges impose simultaneous universal crossing cuts on one exact complement cover

**Workspace:** D17
**State:** established
**Key:** `universal-one-extension-portal-simultaneous-cut-system`

**Summary:** In the universal one-extension pair-core setup SV26947, fix the color s and one arbitrary exact two-cover F of H-s. For a pair-core edge de with Hamilton five-support K=(S-s)+{d,e} and complement Z=Y-{d,e}, if Z is non-Hamiltonian (the PORTAL case), then F must select a physical edge crossing the bipartition K|Z. Otherwise each connected F-rail lies wholly in K or wholly in Z; because both sides are nonempty and F has two rails spanning H-s, one rail would Hamiltonize K and the other would Hamiltonize Z, contradicting non-Hamiltonicity of Z. Hence the crossing quantifier is universal over all exact H-s representatives and does not depend on a chosen two-cover of Z. On the SV29868 shortest pair-core triangle or quadrilateral, one fixed arbitrary F therefore simultaneously crosses every portal cut among its perimeter supports. This strengthens the portal coordinate without asserting synchronization of crossing positions or extinction of the nucleus.


### 1. Pair-core portal setup
Retain the universal one-extension four-set construction SV26947. Let S be the four-set, let

  Y=V(H)-S,

fix one core label s in S, and put

  T=S-s.

For a good pair de in the color graph G_s, retain a Hamilton path K_de on the five-support

  X_de=T union {d,e}.                                    (PC.1)

Inside the common singleton residue H-s the complementary support is

  Z_de=Y-{d,e}.                                          (PC.2)

Call de PORTAL when Z_de is non-Hamiltonian, as in SV26947.

Fix ONCE an arbitrary literal exact two-cover

  F=F_1|F_2                                               (PC.3)

of H-s. Such a cover exists by R4 because H-s is a proper non-Hamiltonian induced subsystem.

### 2. Every portal cut is crossed by every exact representative
Let de be a PORTAL edge. Suppose, for contradiction, that no selected edge of F has one endpoint in X_de and the other in Z_de.

Each F_j is a connected path. With no selected state crossing the bipartition

  V(H-s)=X_de disjoint_union Z_de,                        (PC.4)

each entire F_j must lie wholly on one side of (PC.4). Both sides are nonempty, F spans H-s, and F has exactly two nonempty rails. Therefore one F-rail spans X_de and the other spans Z_de.

In particular Z_de has a Hamilton tight path, contradicting the PORTAL hypothesis that Z_de is non-Hamiltonian.

Hence EVERY exact two-cover F of H-s selects at least one physical directed state crossing

  X_de | Z_de.                                           (PC.5)

This quantifier is independent of any auxiliary chosen two-cover of Z_de.

### 3. Simultaneous cut system on the bounded nucleus
Now retain the SV29868 shortest pair-core cycle

  C=(v_0,...,v_{r-1},v_0),
  r in {3,4}.                                             (PC.6)

For each perimeter edge e_i=v_i v_{i+1}, put

  X_i=T union {v_i,v_{i+1}},
  Z_i=Y-{v_i,v_{i+1}}.                                   (PC.7)

Choose one arbitrary exact two-cover F of H-s and keep it fixed for the entire nucleus.

For EVERY perimeter edge i of PORTAL type, (PC.5) applied to this same F forces a selected F-edge crossing X_i|Z_i. Thus a triangle or quadrilateral containing p portal edges imposes p simultaneous cut-crossing obligations on one literal two-path representative F.                                   (PC.8)

No choice of independent restored covers is required, and no crossing position is identified across different cuts.

### 4. Scope
This is a universal-currentness strengthening of the portal coordinate, not a nucleus extinction theorem. A DONOR edge remains the case Z_i Hamiltonian and is not subject to (PC.5). For a portal-only triangle or quadrilateral, however, every exact H-s representative simultaneously crosses all three or four moving five-core cuts.

The next consumer may minimize the total number of selected cut crossings on F, use their parity/endpoints, or compare which single physical edge crosses several moving cuts. No such synchronization is asserted here.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R4"
    }
]
```
