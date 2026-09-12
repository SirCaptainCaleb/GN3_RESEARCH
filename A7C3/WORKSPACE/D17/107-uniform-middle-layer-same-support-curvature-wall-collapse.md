# Same-support triangle curvature is already a universal four-core; local reversal forms a bilateral cap-wall pair rectangle

**Workspace:** D17
**State:** established
**Key:** `uniform-middle-layer-same-support-curvature-wall-collapse`

**Summary:** In the fixed-cap Arm-M cylinder, combine the current same-support R435 compiler SV7932 with the universal two-ended cap wall SV42382. If reverse-trimer/proper-cycle compression reaches a tight directed triangle Y, SV7932 already says every five-set Y+{d,e} is Hamiltonian. Fixing any one exterior z makes S=Y+z a universally one-vertex Hamilton-extendable four-set, so the directed-triangle carrier is immediately the existing SMALL EXTENSION CORE parent rather than a separate curvature atom. If instead the compiler yields a local dimer reversal, retain tight trimers (x,u,v) and (x,v,u). Their terminal signed dimers pair with the opposite-polarity left and right cap-wall dimers to give four explicit mass-four balanced-pair births: the two reversed uv orientations pair through the left wall, while xu and xv pair through the right wall. R448 then yields fixed-trimer interaction certificates at both middle anchors u and v. This bilateral rectangle is a sharper unresolved interface, not closure: R448 may replay the two source trimers exactly, so no strict descent is claimed.

### 1. Fixed-cap same-support curvature
Work in accepted R927 Arm M in the live fixed-cap setting. Fix a literal Hamilton cap

  C=(c_0,c_1,...,c_{k-1})

and put

  Omega=V(H)-V(C).

Retain the current same-support R435 compiler `same-support-r435-cycle-reduction` SV7932. Its non-selected-reversal output reduces, by explicit seam tests and cycle shortening, to one of two graph-intrinsic three-vertex currencies:

1. a LOCAL DIMER REVERSAL, represented by two tight trimers on the same three-set; or
2. a tight directed triangle Y.

Retain also the universal fixed-cap boundary wall SV42382. For every y in Omega the two reverse cap-boundary dimers

  D_L=(c_1,c_0),
  D_R=(c_{k-1},c_{k-2})

satisfy

  (c_1,c_0,y) tight,                                      (CW.1)
  (y,c_{k-1},c_{k-2}) tight.                              (CW.2)

Thus D_L is tail-signed by every y in Omega and D_R is head-signed by every y in Omega.

The purpose of this section is to spend these two facts before exporting same-support curvature as an anonymous portal.

### 2. A directed triangle is already a universal one-extension four-core
Suppose the SV7932 compiler reaches a tight directed triangle

  Y={x,u,v} subset Omega.                                  (CW.3)

SV7932 proves the stronger FIVE-HAMILTONIAN property

  Y+{d,e} is Hamiltonian                                  (CW.4)

for every two distinct vertices d,e outside Y.

Fix any one vertex

  z outside Y.                                             (CW.5)

In the fixed-cap application one may, for example, take z=c_0, since C is disjoint from Omega. Put

  S=Y+{z}.                                                 (CW.6)

Now let w be any vertex outside S. The vertices z,w are distinct and both lie outside Y, so (CW.4) gives

  S+{w}=Y+{z,w} Hamiltonian.                               (CW.7)

Therefore S is a UNIVERSALLY ONE-VERTEX HAMILTON-EXTENDABLE FOUR-SET.

This is exactly the SMALL EXTENSION CORE parent used by the existing universal-one-extension program. No endpoint role, wall splice, payment, or representative synchronization is required.

Hence the directed-triangle output of same-support reverse-trimer/proper-cycle compression is not an irreducible fixed-cap carrier-conversion atom. It exits immediately to the universal-four-core branch.

### 3. The remaining local reversal has a bilateral four-birth wall rectangle
Now suppose instead that the SV7932 local compiler yields a local reversal. After naming its vertices, retain the two actual tight trimers

  T_u=(x,u,v),
  T_v=(x,v,u),                                             (CW.8)

with x,u,v in Omega and pairwise distinct.

By the signed-trimer convention used in R41/R448, T_u supplies terminal signed dimers

  (x,u) tail-signed by v,
  (u,v) head-signed by x,                                 (CW.9)

while T_v supplies

  (x,v) tail-signed by u,
  (v,u) head-signed by x.                                 (CW.10)

The cap wall supplies the opposite polarities on physically disjoint supports:

  D_L is tail-signed by x,u,v,
  D_R is head-signed by x,u,v.                            (CW.11)

Since V(C) and Omega are disjoint, each wall dimer is physically disjoint from every dimer in (CW.9)-(CW.10). Accepted R514 therefore recognizes four direct mass-four balanced-pair births:

  D_L  <->  (u,v),
  D_L  <->  (v,u),                                       (CW.12)

  D_R  <->  (x,u),
  D_R  <->  (x,v).                                       (CW.13)

The left wall simultaneously pairs with the two opposite orientations of the reversed physical dimer {u,v}. The right wall pairs with the two source-side terminal dimers sharing x. This is a literal BILATERAL 2x2 WALL PAIR RECTANGLE. All four births are graph-intrinsic certificates in the same fixed-cap parent frame. Executing any one R514 continuation is optional and need not preserve the other births as current representatives.

Each birth has the accepted R514 continuation to either a spanning two-cover or an ancestry-bearing both-singleton floor. The stronger point here is the simultaneous birth geometry before any such continuation is chosen.

### 4. The rectangle fires the fixed-trimer interaction engine at both middle anchors
For the fixed trimer T_u=(x,u,v), the right-wall birth

  D_R <-> (x,u)

uses one terminal signed dimer of T_u, while the left-wall birth

  D_L <-> (u,v)

uses its other terminal signed dimer. These two births are already present before any unrelated reset. Accepted R448 therefore gives its concrete fixed-trimer interaction certificate at the middle anchor u.

Likewise T_v=(x,v,u) has the two births

  D_R <-> (x,v),
  D_L <-> (v,u),

so R448 gives the corresponding interaction certificate at the middle anchor v.

Thus a local dimer reversal inside the fixed-cap cylinder cannot remain merely a three-vertex reversal label. It canonically carries TWO fixed-trimer interaction interfaces, one at each middle anchor of the two reversed trimer orders, with the partner supports pinned to opposite ends of the same cap.

### 5. Exact replay fence
This bilateral interaction is not yet curvature cancellation.

R448 explicitly warns that its strict-growth alternative may reproduce the already-known source trimer. Here that warning is real, not cosmetic: the u-interaction may replay T_u=(x,u,v), while the v-interaction may replay T_v=(x,v,u). Both replays can reproduce exactly the local reversal data with which we began.

Therefore this section does NOT claim that the local-reversal branch has descended, closed, or re-entered the global Morse lineage below its old checkpoint. The additional wall partners D_L,D_R have not yet been used to rule out simultaneous replay.

The correct surviving interface is consequently:

  LOCAL REVERSAL
    -> four explicit mass-four wall pair births
    -> R448 interaction at u and at v,

with the simultaneous source-trimer replay as the only presently identified reason this does not already count as strict progress.

### 6. Fixed-cap curvature consequence
Combining the current same-support compiler with Sections 2-5 sharpens the G18 fixed-cap curvature problem as follows.

- The DIRECTED-TRIANGLE outcome is already a universal one-extension four-core.
- The LOCAL-REVERSAL outcome carries the bilateral 2x2 cap-wall pair rectangle and two anchored R448 interaction certificates.
- The adjacent full-support selected-reversal outcome remains governed by the existing fixed-complement reversal transport and its singleton-row R561 closure mechanism.

Hence a same-support R435 reverse-trimer/proper-cycle packet has no generic directed-triangle carrier debt left. The genuinely unresolved wall-form atom is the local-reversal replay cell, now with four named pair births and both middle anchors retained.

This is a routing/refinement theorem only. It does not prove Arm-M extinction, global small-core extinction, or fixed-cap curvature cancellation.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R448"
    },
    {
        "relation": "dependency",
        "revision_id": "R514"
    }
]
```
