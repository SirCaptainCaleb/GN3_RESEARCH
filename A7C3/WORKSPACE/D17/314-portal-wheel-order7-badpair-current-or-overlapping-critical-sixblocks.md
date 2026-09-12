# The two-bad order-seven shell is current on the bad pair or promotes to two overlapping critical six-blocks

**Workspace:** D17
**State:** established
**Key:** `portal-wheel-order7-badpair-current-or-overlapping-critical-sixblocks`

**Summary:** Retain the coherent hub-opposite order-seven residue Omega=K disjoint_union {y,z} from SV64567, with K a Hamilton P5, Q a literal Hamilton complement, y,z the two bad singleton labels, and for every d in K an actual Hamilton puncture path P_d on Omega-d whose physical endpoints are exactly y,z. Then U_y=K+y and U_z=K+z are intrinsically non-Hamiltonian deletion-Hamiltonian six-blocks: non-Hamiltonicity is badness of z/y, deleting the extra label leaves K, and deleting d leaves the Hamilton path P_d with the opposite bad endpoint trimmed. Compare arbitrary exact bad singleton rows C_y,C_z on the common pair residue H-{y,z}=K|Q. If z is internal in C_y (or y internal in C_z), trimming gives a literal 3-to-2 component drop. If the surviving label is an endpoint, trimming gives an exact two-cover; any support partition different from K|Q gives an R410 current crossing. Hence outside current bad-pair geometry, both trims have the K|Q partition. Badness rules out attaching z to K in C_y and y to K in C_z, so Q+z and Q+y must be Hamiltonian. Consequently U_y has fixed Hamilton complement Q+z and U_z has fixed Hamilton complement Q+y: the two bad labels promote the residue to TWO overlapping fixed-complement critical blocks sharing K. Applying the complete local CBCA router SV30477 to each block sends each to a universal one-extension four-core or actual/closed maximum-three-forest holonomy. Thus the G24 two-bad coherent residue is not terminal: it is current already on {y,z}, or doubly promoted to the existing global holonomy programs.

### 1. The order-seven coherent coordinates
Retain the coherent hub-opposite order-seven branch of SV64567. Thus

  V(H)=Omega disjoint_union V(Q),
  Omega=V(K) disjoint_union {y,z},

where K is one retained Hamilton P5, Q is one retained literal Hamilton path, Omega is non-Hamiltonian, and y,z are the two BAD labels:

  Omega-y = K+z is non-Hamiltonian,
  Omega-z = K+y is non-Hamiltonian.                         (BP.1)

For every d in V(K), the spoke/coherent shell supplies an actual Hamilton puncture path

  P_d on Omega-d

whose two physical endpoints are exactly y and z and whose four K-d vertices occur as one contiguous interior block. Pairing P_d with Q gives the exact good singleton row H-d=P_d|Q.

The common pair deletion is especially simple:

  H-{y,z}=K|Q.                                             (BP.2)

Both rails in (BP.2) are nonempty Hamilton paths, and accepted R429 says pc(H-{y,z})=2 with every exact pair cover nontrivial.

### 2. The two six-blocks are already deletion-Hamiltonian
Put

  U_y=V(K) union {y},
  U_z=V(K) union {z}.                                     (BP.3)

By (BP.1), U_y=Omega-z and U_z=Omega-y are non-Hamiltonian.

They are nevertheless deletion-Hamiltonian. For U_y:

- deleting y leaves the Hamilton P5 K;
- fix d in K. Since z is a physical endpoint of P_d, deleting z from the actual word P_d leaves a Hamilton path on

    (Omega-d)-z = (K-d)+y = U_y-d.

Thus every singleton deletion of U_y is Hamiltonian. The same argument with y and z exchanged proves every singleton deletion of U_z Hamiltonian. Therefore

  U_y and U_z are non-Hamiltonian deletion-Hamiltonian six-blocks,
  sharing the literal Hamilton five-core K.                 (BP.4)

This uses the physical endpoint statement of SV64567; it is stronger than merely knowing that the five K-punctures of Omega are Hamiltonian.

### 3. Compare one bad singleton row with the common pair fiber
Choose an arbitrary exact two-cover

  C_y=A_y|B_y

of H-y. Inspect the surviving bad label z in this actual row.

If z is internal on its C_y rail, delete z. That rail splits into two nonempty intervals and the other rail remains nonempty, giving a literal three-cover of H-{y,z}. Compare it with the exact two-cover K|Q from (BP.2). The selected component-drop crossing is CURRENT on the bad pair {y,z}; accepted R159 supplies the corresponding graph-intrinsic balanced-pair certificate. Stop in this branch.

Suppose instead that z is an endpoint of its C_y rail. It cannot be a singleton rail: deleting such a singleton would leave a Hamilton path spanning H-{y,z}, contradicting R429, which gives pc(H-{y,z})=2. Hence trimming z leaves two nonempty paths and therefore a literal exact two-cover

  C_y-z

of H-{y,z}. Compare its unordered support partition with that of K|Q. If the partitions differ, accepted R410 supplies a physical selected cross-state between the two actual common-residue covers. Retain that CURRENT bad-pair crossing and stop.

Thus, outside current geometry on {y,z}, z is an endpoint of C_y and

  supp(C_y-z) = {K,Q}.                                    (BP.5)

Restoring endpoint z to the rail from which it was trimmed has only two support possibilities:

  (K+z)|Q,
  or K|(Q+z).                                              (BP.6)

The first is impossible because it would make K+z=Omega-y Hamiltonian, contradicting badness of y in (BP.1). Therefore the second must occur. In particular

  Q+z is Hamiltonian.                                     (BP.7)

Apply the identical argument to an arbitrary exact H-z row C_z. Outside current bad-pair geometry it forces

  Q+y is Hamiltonian.                                     (BP.8)

Hence we have the exact dichotomy

  CURRENT BAD PAIR: H-{y,z} carries a literal 3-to-2 component drop or support-disagreement crossing;

  QUIET BAD PAIR: Q+y and Q+z are both Hamiltonian.        (BP.9)

No singleton-deletion rail-floor theorem is used; the singleton-rail possibility in Section 3 is excluded directly by pair-deletion rigidity R429.

### 4. Quiet bad pair promotes two overlapping fixed-complement critical blocks
Assume the quiet branch of (BP.9). By (BP.4), U_y is non-Hamiltonian deletion-Hamiltonian. By (BP.7), its literal complement in H is the Hamilton support

  V(H)-U_y = Q+z.                                         (BP.10)

Therefore

  V(H)=U_y disjoint_union (Q+z)

is a full fixed-complement critical-block decomposition. Every Hamilton puncture U_y-u pairs with the same Hamilton complement Q+z in an exact singleton-deletion row of H-u.

Likewise, by (BP.4) and (BP.8),

  V(H)=U_z disjoint_union (Q+y)                            (BP.11)

is a second fixed-complement critical-block decomposition. The two non-Hamiltonian critical blocks U_y and U_z have order six and overlap in the entire Hamilton P5 K; their Hamilton complements differ by exchanging y and z against the original Q.

Thus a quiet survival of the two bad singleton labels does not remain a partial critical shell. It upgrades simultaneously to TWO honest fixed-complement critical blocks.

### 5. Feed both promoted blocks into the completed local CBCA router
Apply `fixed-complement-critical-block-local-routing-complete` SV30477 separately to (BP.10) and (BP.11). For each promoted block, the complete local fixed-complement program has only the global destinations

  UNIVERSAL ONE-EXTENSION FOUR-CORE,
  or ACTUAL/CLOSED MAXIMUM-THREE-FOREST HOLONOMY.           (BP.12)

Therefore the two-bad order-seven coherent residue has the parent-scale trichotomy

  current geometry on the bad pair {y,z},
  or a small extension core exported from U_y or U_z,
  or actual/closed maximum-three-forest holonomy exported from the promoted critical blocks.

More precisely, in the quiet branch BOTH overlapping critical blocks are available to the global consumer; they are alternatives only at the later routing choices, not at the level of the graph-intrinsic decompositions (BP.10)-(BP.11).

### 6. G24 consequence and fence
This consumes the principal defect of the local seven-vertex fence SV64875. The fence showed that five common-endpoint good punctures plus even complete pair-deletion Hamiltonicity inside Omega do not force y or z good. The missing information is exactly the external Hamilton complement. Once the actual bad singleton rows are compared through the literal common pair fiber K|Q, either the bad pair itself becomes current or the external complement Hamiltonizes both reciprocal one-extensions Q+y,Q+z, promoting the two bad labels into overlapping full critical blocks.

The theorem does not by itself extinguish the current bad-pair branch and does not prove the global small-core/maximum-forest destinations impossible. Its gain is the G24-requested promotion: the stubborn two-bad coherent shell has no third local support-only residue.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R159"
    },
    {
        "relation": "dependency",
        "revision_id": "R410"
    },
    {
        "relation": "dependency",
        "revision_id": "R429"
    }
]
```