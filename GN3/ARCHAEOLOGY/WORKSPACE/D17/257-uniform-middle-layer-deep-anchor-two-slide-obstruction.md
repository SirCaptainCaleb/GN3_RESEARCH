# Interior fixed-turn anchors annihilate portal-free cap transport in Arm M

**Workspace:** D17
**State:** established
**Key:** `uniform-middle-layer-deep-anchor-two-slide-obstruction`

**Summary:** In Arm M with k>=5, choose the retained terminal cap turn J=(a1,a2,a3), so both possible R434/R436 completed outer anchors are interior vertices of the cap rail A*. Every support-changing one-edge transfer is exactly a reversible one-vertex endpoint SLIDE. A flat completed-anchor dimer exit currentizes to D|U|V with sizes 2|k|(k-1) and the historical anchor e in D. Compare the old cap forest with this currentization by SV40898. If the comparison factored through at most two support-changing one-edge transfers, e would have to leave the A*-descendant. Since e is initially interior, it cannot leave in one SLIDE. If it leaves on the second, the first SLIDE must remove an A* endpoint to expose e, and the second removes e itself; because no SLIDE can add to a cap k-rail without creating the forbidden (k+1)-path, the surviving A*-descendant has size k-2. For k>=5 this is none of the final sizes k,k-1,2, contradiction. Hence the one/two-edge factorization branch is impossible. Every cap-level flat exit necessarily exposes a C4/C6 support-incidence nucleus, repeated-crossing nucleus, same-cell R435 portal, or current mixed-seam trimer. Together with SV42128 below-cap strict height gain and the fact that all other R172 productive exits are already named portals, the actual phased continuation has no portal-free cap-support transition at all for k>=5; the G16 portal-free cap-support quotient is edgeless, so in particular it has no nontrivial closed walk.


### 1. One-edge support change is literally one endpoint vertex
Let

  F=A|B|C,   A=(a_0,...,a_{m-1})                         (IA.1)

be a literal maximum spanning three-forest. By SV38940 Section 2, every reversible SUPPORT-CHANGING one-edge transfer is determined by a terminal-to-source merge seed between two distinct rails. The unique deleted old edge is the unique bad root boundary edge. Thus, exactly as in SV22098, every such generator is a literal one-vertex endpoint SLIDE:

  one donor rail loses exactly one physical endpoint vertex,
  one recipient rail gains exactly that vertex at an endpoint,
  the third rail is unchanged.                           (IA.2)

In particular a physical vertex which is internal on a rail cannot leave that rail in the next support-changing one-edge transfer.

### 2. Cap rails cannot receive a SLIDE in Arm M
Work in accepted R927 Arm M:

  |V(H)|=2k+1,
  every k-set is Hamiltonian,
  no (k+1)-set is Hamiltonian,                            (IA.3)

with k>=5. Let

  F*=A*|B*|C*,   A*=(a_0,...,a_{k-1})                    (IA.4)

be a terminal cap forest with |A*|=k.

No one-vertex SLIDE can add a vertex to the physical descendant of A* while it still has order k, because the recipient rail would be a literal tight path of order k+1, forbidden by (IA.3). Therefore before A* first loses a vertex, every support-changing generator either leaves A* unchanged or removes one endpoint from it.                                        (IA.5)

### 3. Flat completed-anchor exits have the rigid final profile 2 | k | (k-1)
Retain the fixed-turn paid continuation of SV41376. Suppose a genuinely flat R434/R436 productive exit occurs at a completed outer anchor e of the retained turn, producing only a new signed dimer D through e and no larger growth/cycle/reversal output.

The current flat-exit theorem SV42128 applies R4 to D and obtains a literal maximum forest

  F_D=D|U|V,
  |D|=2, |U|=k, |V|=k-1,                                (IA.6)

with e in D. At cap the new k-support U is physically different from V(A*).

Compare F* and F_D by SV40898. Outside a C4/C6 support-incidence nucleus, repeated-crossing nucleus, same-cell R435 geometry, or a current mixed-seam trimer, the only remaining outcome is a factorization through at most two support-changing one-edge transfers:

  F* -> G -> F_D,                                        (IA.7)

where either arrow may be absent.

### 4. An interior historical anchor cannot traverse the two-SLIDE quotient
Assume e is INTERNAL on the old cap rail A*.

Because e lies in the final dimer D, while A* has order k>=5, e cannot stay forever in the physical A*-descendant during (IA.7): after at most two one-vertex SLIDEs a rail retaining all but at most two A*-vertices still has order at least k-2>=3, and in particular cannot be the order-two rail D unless k=4. Thus e must itself be transferred out of the A*-descendant.

It cannot leave on the first SLIDE, because it is internal by hypothesis and every generator transfers only an endpoint vertex.

Suppose it leaves on the second SLIDE. Then the first SLIDE must make e an endpoint of the A*-descendant. Since no SLIDE may add to the cap rail by (IA.5), the first move must remove an A* endpoint. The second move then removes e itself. Consequently the surviving physical descendant of A* has order exactly

  k-2.                                                    (IA.8)

But every final rail of F_D has order in

  {k,k-1,2}.                                              (IA.9)

For k>=5,

  k-2 notin {k,k-1,2}.                                   (IA.10)

The A*-descendant cannot disappear under a SLIDE, since k-2>=3. Hence it must be one of the three final rails, contradicting (IA.9).

Therefore the factorization (IA.7) is impossible whenever the flat exit anchor e was internal on A*.

### 5. Choose one fixed turn whose two possible anchors are both internal
SV41376 permits ANY proper turn of A* to be fixed before pair payment. For every k>=5 choose

  J=(a_1,a_2,a_3).                                       (IA.11)

The two outer vertices a_1 and a_3 are both internal on A*: a_1 is not a_0 or a_{k-1}, and because k>=5, a_3 is also not a_{k-1}.

The completed R434 anchor in this fixed-J lineage is always one of these two outer vertices. Therefore whichever anchor supports the later flat dimer exit, Section 4 applies. The one/two-edge factorization outcome of SV40898 is excluded.

Hence EVERY cap-level flat completed-anchor exit for k>=5 necessarily exposes one of the bounded/named curvature species:

  - a physical C4 or C6 support-incidence nucleus;
  - a repeated-crossing nucleus on at most four seam vertices;
  - same-cell R435 reversal / reverse-trimer / proper-cycle geometry;
  - a current mixed-seam trimer.                          (IA.12)

### 6. The portal-free cap-support quotient has no flat edges
Combine Section 5 with SV42128.

Below cap, a flat completed-anchor dimer exit currentizes to a k-rail and strictly improves the primary largest-rail record.

At cap, with the legal fixed-turn choice (IA.11), the same flat exit cannot pass through the portal-free one/two-edge quotient at all; it necessarily emits bounded/named curvature (IA.12).

All OTHER productive exits of the SV41376/R172 continuation are already explicit named growth/cycle/reversal/contact portals by definition of that continuation. Therefore, for the actual phased continuation in Arm M with k>=5,

  THERE IS NO PORTAL-FREE CAP-SUPPORT TRANSITION.         (IA.13)

Equivalently, the G16 terminal cap-support quotient retaining the physical exit ancestry is edgeless after the bounded/named portal species are removed. In particular it has no nontrivial portal-free closed walk, no portal-free cap monodromy, and no rank-zero cap recurrence to extinguish.

This does not consume the bounded C4/C6 or repeated-crossing nuclei, nor the named R435/trimer/cycle portals themselves. It removes the purported portal-free transport sector: productive-exit reentry at the hard cap must expose curvature immediately.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R927"
    }
]
```