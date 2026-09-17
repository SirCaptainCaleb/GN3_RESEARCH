# A prepayment proper-path output of a finite phase-one source packet descends below every source in the packet

**Workspace:** D17
**State:** established
**Key:** `forest-phase-source-packet-proper-path-old-threshold`

**Summary:** Finite-packet variant of SV69721. Let F_1,...,F_r be retained literal phase-1 maximum-three-forest checkpoints participating simultaneously in one certificate-retaining prepayment analysis, with largest-rail heights M_i. If that source packet legally produces a graph-intrinsic proper tight path K or certified proper-cycle break before any phase-0 transition, put M*=max_i M_i. Currentize K by R4. If the new largest rail exceeds M*, its phase-1 rank is below every packet source. Otherwise run SV40879 against the common ceiling M*: closure, first height M*+1, or terminal phase0. The latter two are also strictly below every source because (1,n-M*) is the minimum phase-1 rank among the packet. Thus a joint comparison of several source rows needs no fictitious one-source transition: any genuine packet-born proper-path output gives TWO-COVER or strict phased-rank descent below all participating sources.


### 1. Finite phase-one source packet
Let H be a hypothetical smallest counterexample and retain finitely many literal phase-1 maximum-three-forest checkpoints

  F_1,...,F_r.                                             (PK.1)

For each i let M_i be the largest rail order of F_i and put

  M_* = max_i M_i,
  Phi_*=(1,|V(H)|-M_*).                                   (PK.2)

Then Phi_* is the smallest phased rank among the phase-1 packet:

  Phi_* <= rank(F_i) for every i.                          (PK.3)

Suppose one certificate-retaining legal analysis uses this finite packet jointly, without entering phase 0, and produces a graph-intrinsic proper tight path K or one certified cyclic break of a proper tight cycle. The birth certificate must retain the actual source representatives and the physical comparison/blocker/current event that produced K. An arbitrary path unrelated to the packet is not eligible.

This setup covers, in particular, R435 comparisons of two actual singleton rows and endpoint-return triangles whose output uses three retained puncture rows.

### 2. Normalize against the best old source height
By R4, currentize K as a literal rail of a maximum forest

  G=K|U|V.                                                 (PK.4)

Let L be the largest rail order of G. If L>M_*, then

  rank(G)=(1,n-L)<(1,n-M_*)=Phi_*<=rank(F_i)              (PK.5)

for every packet source.

If L<=M_*, run the SV40879 marked-largest-rail continuation from G and stop at TWO-COVER, first marked order M_*+1, or a terminal state of order at most M_*. At M_*+1 the phase-1 rank is strictly below Phi_*. At a terminal state SV41376 enters phase 0, again strictly below Phi_*.

Thus every nonclosing branch reaches a legitimate checkpoint whose phased rank is strictly below every source F_i in the packet.

### 3. Packet old-threshold theorem
> If a finite packet of retained phase-1 maximum-three-forest representatives jointly produces a source-labelled proper tight path/cycle output before payment, then there is a finite certificate-retaining continuation to TWO-COVER or phased rank strictly below every source representative participating in that packet.

No transition from one packet source to another is asserted or needed. The packet itself is the retained simultaneous input to the comparison theorem. This is the correct interface for R435 comparisons, Johnson triangles, endpoint-return cycles, and other genuinely multi-source constructions.

### 4. Scope fence
The theorem does not legalize arbitrary simultaneous representatives: the source packet must be the actual finite family retained by the upstream theorem, and K must be an output of that packet's physical comparison or reconstruction. It does not apply when the participating parent checkpoints already lie in phase 0. R24 and R5 are unused.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R4"
    }
]
```