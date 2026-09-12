# Every bad singleton in a fixed-complement shell forces a current star to all good punctures

**Workspace:** D17
**State:** established
**Key:** `fixed-complement-bad-singleton-current-star`

**Summary:** Let V(H)=Omega disjoint_union Q in a hypothetical smallest counterexample, with Q a literal Hamilton path and Omega non-Hamiltonian. Let D subset Omega be Hamilton-deletable labels: Omega-d is Hamiltonian for every d in D. Fix a bad singleton y in Omega-D with Omega-y non-Hamiltonian, choose any exact row C_y of H-y, and for each d choose a fixed-complement good row P_d|Q of H-d. Then every pair {y,d} carries current common-residue geometry. If y is internal in P_d, trimming y gives a literal three-cover of H-{y,d}; if d is internal in C_y, trimming d does the same. If both are endpoints, the two trims are exact two-covers and cannot have the same support partition: equality would force either Omega-y Hamiltonian or Q+d Hamiltonian, while Q+d Hamiltonian together with Omega-d would close H. Hence R410 gives a current crossing. Moreover every bad row contains a selected Omega|Q crossing oq; for every d != o for which y is an endpoint of P_d, this identical physical edge survives deletion of d and crosses the exact fixed-complement cover (Omega-{y,d})|Q. In the order-seven two-ended necklace of SV64567, y is an endpoint of every good puncture path, so one mixed edge in H-y is a common selected crossing on four of the five pair deletions {y,d}. With two bad labels y,z, the residue therefore carries a current K_{2,5} bad-good pair graph together with two degree-four common-crossing subfans. This uses the external common complement and is invisible to the induced seven-vertex fence SV64875. No strict Phi/epsilon descent is claimed.

### 1. Fixed-complement good and bad singleton rows
Let H be a hypothetical smallest Strong Level-(1) counterexample. Retain a support split

  V(H)=Omega disjoint_union V(Q),

where Q is one literal Hamilton tight path and Omega is non-Hamiltonian. Let

  D subset Omega

be a set of GOOD puncture labels such that Omega-d is Hamiltonian for every d in D. For each d choose one actual Hamilton puncture path P_d on Omega-d and retain the literal exact singleton-deletion row

  C_d = P_d | Q     on H-d.                                (BS.1)

Exactness follows from smallest-counterexample minimality because the displayed two paths are nonempty and H-d cannot be Hamiltonian in a counterexample.

Fix a BAD label

  y in Omega-D,   Omega-y non-Hamiltonian,                  (BS.2)

and choose any literal exact two-cover

  C_y = A_y | B_y     of H-y.                              (BS.3)

Because Omega-y is non-Hamiltonian while Q is Hamiltonian, C_y cannot have support partition (Omega-y)|Q. Consequently C_y contains at least one selected physical state crossing the fixed cut Omega|Q. Retain one such selected state and write its physical endpoints as

  {o,q},   o in Omega-{y},   q in Q.                        (BS.4)

Its selected direction in C_y is retained but is irrelevant to the support-crossing assertions below.

### 2. Every good-bad pair is current on its common pair deletion
Fix d in D and compare the good row C_d with the bad row C_y on the common deleted pair {y,d}.

If y is INTERNAL on P_d, deleting y from C_d splits P_d into two nonempty tight intervals while Q survives unchanged. Thus C_d-y is a literal three-cover of H-{y,d}. Accepted R429 supplies an exact two-cover of the same residue, so the pair deletion carries a literal current 3-to-2 component-drop interface.                                           (BS.5)

Assume therefore that y is an endpoint of P_d. Then

  F_d := C_d-y = (P_d-y) | Q                               (BS.6)

is a literal exact two-cover of H-{y,d}; both components are nonempty, and R429 rules out Hamilton collapse.

Now inspect d in the bad row C_y. If d is INTERNAL on its C_y rail, deleting d gives a literal three-cover of H-{y,d}, again producing current 3-to-2 geometry against any exact two-cover. Hence assume d is an endpoint. A singleton d-rail in C_y is impossible: the other rail would Hamiltonize H-{y,d}, and the automatic dimer on {y,d} would close H. Therefore

  G_d := C_y-d                                               (BS.7)

is also a literal exact two-cover of H-{y,d}.

Suppose for contradiction that F_d and G_d induce the same unordered support partition. The F_d partition is

  (Omega-{y,d}) | Q.                                       (BS.8)

Restoring the endpoint d to G_d has only two support-level possibilities.

1. d is restored to the Omega-side rail. Then C_y has support partition

     (Omega-y) | Q,

   so Omega-y is Hamiltonian, contradicting badness (BS.2).

2. d is restored to the Q-side rail. Then C_y has support partition

     (Omega-{y,d}) | (Q+{d}),

   so Q+d is Hamiltonian. But Omega-d is Hamiltonian by goodness of d, and the two disjoint Hamilton paths on Omega-d and Q+d would span H, contradiction.

Therefore F_d and G_d have different support partitions. Accepted R410 then supplies a selected current crossing on the common residue H-{y,d} and a graph-intrinsic balanced-pair birth.                                  (BS.9)

Combining the three cases gives the exact star statement:

  for EVERY d in D, the pair deletion H-{y,d}
  carries current common-residue crossing/component-drop geometry.   (BS.10)

This is stronger than merely saying the bad singleton row mixes Omega with Q: every good puncture label is tied to y by an actual current pair fiber.

### 3. One bad-row mixed edge survives as a common crossing subfan
Retain the selected cut-crossing {o,q} from (BS.4). Fix d in D with

  d != o                                                   (BS.11)

and suppose y is an endpoint of P_d, so the exact fixed-complement pair row F_d of (BS.6) exists.

Deleting d from C_y does not remove either endpoint of the selected state {o,q}, so that same physical selected state survives in the literal path forest C_y-d. In F_d, o lies in the Omega-{y,d} component and q lies in the Q component. Hence

  the SAME physical selected state {o,q}
  crosses two components of F_d on H-{y,d}.                (BS.12)

No payment, representative replacement, or historical replay is involved. The current crossing is inherited literally from the one bad singleton row C_y.

Thus one mixed state of C_y simultaneously currentizes every pair {y,d} satisfying d != o and endpoint exposure of y in P_d. The exceptional good label o, if o belongs to D, is the only root for which this particular selected state disappears under pair deletion.

If y is internal in P_d instead, BS.5 already gives current 3-to-2 geometry. Therefore the only reason the common state {o,q} fails to represent a particular good-bad pair is that the GOOD row itself has already currentized that pair by fragmentation.

### 4. Order-seven two-ended necklace consequence
Now specialize to the hub-opposite quiet residue of SV64567 with

  Omega = K union {y,z},   |K|=5,                          (BS.13)

where K is the Hamilton P5, every Omega-d for d in K is Hamiltonian, and every retained P_d has physical endpoints exactly y,z. SV64875 shows that the induced seven-vertex support pattern can have both y and z bad, so no support-only contradiction is available.

Take any exact bad row C_y of H-y. It must contain a selected Omega|Q crossing {o,q}. Because y is an endpoint of EVERY P_d, Section 3 applies to every d in K-{o}. Therefore one and the same physical state {o,q} is a current cross-state on at least four distinct pair deletions

  H-{y,d},   d in K-{o}.                                   (BS.14)

Independently BS.10 gives current geometry on the fifth good-bad pair as well. Thus y supports a full five-spoke current star to K, with a degree-at-least-four common-crossing subfan carried by one actual bad singleton row.

The same argument applied to the second bad label z yields another five-spoke star. Hence the two-bad order-seven residue carries the physical bad-good current graph

  K_{2,5} on {y,z} versus K,                               (BS.15)

and each bad side has a degree-at-least-four substar represented by one common selected Omega|Q crossing from its own actual singleton row.

This geometry is genuinely external to the induced block Omega: it uses the fixed Hamilton complement Q and selected mixed singleton rows, so it is not present in the exact local fence SV64875.

### 5. Relation to current-kernel uncrossing
BS.10-BS.15 provide a new G24 interface. In a coherent fixed-complement shell, BAD singleton labels are not passive holes in the puncture family. Each bad label forces a current star to every good puncture label, and in the rigid order-seven residue one actual mixed singleton crossing is reused simultaneously across four pair-deletion fibers.

This is precisely the kind of shared-source current kernel that a global Phi/epsilon_* uncrossing theorem can exploit: the current pair portals are not anonymous and do not arise from independent payments. They inherit one literal bad singleton row, one fixed cut Omega|Q, one selected mixed state, the good fixed-complement rows, and all original capture/wheel ancestry.

No strict decrease of Phi or epsilon_* is asserted here. The theorem is a currentization/synchronization result, not the final consumer. R24 and R5 are not used.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R4"
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