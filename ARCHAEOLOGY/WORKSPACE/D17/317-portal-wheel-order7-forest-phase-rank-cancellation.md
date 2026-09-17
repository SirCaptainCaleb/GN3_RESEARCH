# The order-seven coherent necklace is forest-phase rank-cancellable

**Workspace:** D17
**State:** established
**Key:** `portal-wheel-order7-forest-phase-rank-cancellation`

**Summary:** Compose the asymmetric P5-dimer checkpoint SV66530 with the forest-phase portal absorber SV52939. Every order-seven coherent necklace has a literal maximum three-forest F0=S|(e,f)|Q. The two actual good singleton rows give neighboring maximum forests P_e|{e}|Q and P_f|{f}|Q, and the comparisons S versus P_e and S versus P_f are necessarily R435-nonquiet. Hence, already from the retained F0 packet, an explicit R435 portal is born. Each possible R435 output is a proper-path portal in the precise sense of SV52939: an adjacent selected reversal supplies its named reversed dimer, a reverse-trimer output is itself a proper path, and a proper cycle supplies any cyclic break. Mark a largest rail of F0, of order M=max(5,|Q|), so its phase-1 checkpoint rank is Phi0=(1,n-M). SV52939 then gives a finite certificate-retaining continuation from the born portal to either a spanning two-cover or a forest/pair state with phased rank strictly below Phi0. Therefore the order-seven necklace is not merely exported to maximum-forest dynamics: it is strictly cancellable relative to its own canonical forest-phase birth checkpoint. In any reconstruction-closed family refined by the legitimate SV41376 phased rank, no nonclosing lex-minimal order-seven coherent kernel can survive. This conclusion does not depend on whether the bad pair {y,z} is current or quiet and consumes the local fence SV64875 at the global representative level.

### 1. Retain the canonical order-seven forest checkpoint
Retain the order-seven coherent necklace of SV64567. Apply SV66530. It constructs physical vertices y,z, a Hamilton P5

  S=(r_1,y,r_2,z,r_3),

two remaining good roots e,f, and the literal maximum spanning three-forest

  F_0 = S | (e,f) | Q.                                    (RC.1)

The two actual good puncture rows are

  H-e=P_e|Q,   H-f=P_f|Q,                                 (RC.2)

where P_e is Hamiltonian on S+f and P_f is Hamiltonian on S+e. Restoring the deleted root as a singleton gives the two literal neighboring maximum forests

  F_e=P_e|{e}|Q,
  F_f=P_f|{f}|Q.                                           (RC.3)

All three forests and the exact physical ancestry relating them are part of the retained SV66530 packet.

Mark a largest rail of F_0. Since |S|=5 and |(e,f)|=2, its order is

  M=max(5,|Q|).                                            (RC.4)

Thus F_0 is a phase-1 checkpoint of the SV41376 hybrid rank with

  Phi_0=(1,n-M).                                           (RC.5)

### 2. Reverse-Ear curvature is forced at that checkpoint
SV66530 proves that neither comparison

  S versus P_e,
  S versus P_f                                             (RC.6)

can be R435-quiet. The reason is physical: y,z occupy internal positions of the retained S-word, while they are the two physical endpoints of each actual puncture path P_e,P_f. Therefore at least one, in fact both, comparisons emit an exact accepted R435 output.

Fix one emitted output and retain its full comparison ancestry to F_0 and F_e or F_f. Accepted R435 has exactly three nonquiet species:

1. an adjacent selected S-state is selected in reverse in the neighboring puncture path;
2. a tight reverse trimer;
3. a vertex-simple proper tight cycle.                      (RC.7)

Crucially these are exactly the forest-phase portal species covered by SV52939. In case 1 the named reversed physical dimer is itself a proper tight path. In case 2 the reverse trimer is a proper tight path. In case 3 choose any cyclic break, producing a proper tight path on the cycle support. Hence RC.7 supplies a graph-intrinsic proper tight path K_port with explicit birth ancestry from the retained phase-1 checkpoint packet.

The selected-reversal case is not being treated as generic anonymous dimer existence: its two physical vertices and reversed selected-state certificate are retained from the actual S/P_e or S/P_f comparison. This is precisely the portal-birth data required by SV52939.

### 3. Apply forest-phase path-portal absorption
Apply SV52939 to the checkpoint F_0 and the proper path K_port born in Section 2. The theorem first currentizes K_port by accepted minimality R4 into a literal maximum three-forest. If its largest rail has order exceeding M, the forest-phase coordinate already satisfies

  (1,n-L)<Phi_0.                                           (RC.8)

Otherwise SV52939 runs largest-rail A-growth from that currentization. Every nonclosing SLIDE strictly grows the marked rail. The continuation therefore reaches exactly one of:

- a spanning two-cover of H;
- marked rail order M+1, giving forest-phase rank strictly below Phi_0;
- a terminal signed forest at rail order at most M, where SV40879 enters the certified pair lineage and the phase coordinate drops from 1 to 0, again giving rank strictly below Phi_0.

Thus

  ORDER-SEVEN NECKLACE
    => TWO-COVER
       or finite certificate-retaining reentry at Phi<Phi_0.   (RC.9)

No payment-phase comparison is hidden here. The R435 curvature is born before payment, at the literal maximum-forest packet RC.1-RC.3, so the phase-1 hypothesis of SV52939 is exact.

### 4. G24 extinction consequence
Equation RC.9 upgrades the previous order-seven results in an essential way. SV64875 showed that the induced seven-vertex necklace can exist locally. SV66530 showed that adding the external Hamilton complement Q forces a P5-dimer forest and unavoidable R435 curvature. The present composition shows that this curvature is not merely another portal: its forest-phase birth makes it STRICTLY RANK-CANCELLABLE.

Consequently, in any reconstruction-closed family whose finite lexicographic objective is refined by the legitimate SV41376 phased rank, a nonclosing lex-minimal order-seven coherent kernel cannot survive: its own retained representative packet produces a continuation to strictly smaller rank. This is a rigorously stronger finite substitute for bare pair-partition disagreement and therefore meets the G24 success criterion.

The argument is independent of the bad-singleton pair branch. It does not matter whether {y,z} already carries current pair-deletion geometry or whether SV65829 promotes the two bad labels to overlapping critical six-blocks; the five GOOD punctures alone build F_0 and force the rank-cancellable curvature.

### 5. Scope fence
This theorem extinguishes the bounded order-seven coherent residue relative to the phased-rank refinement. It does not by itself prove that every larger incoherent/current wheel lowers the original pair-partition objective Phi, nor does it consume phase-0 curvature born only after completed-anchor payment. The decisive hypothesis is exactly the one identified by SV52939: the portal is born at a retained phase-1 maximum-forest checkpoint.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R435"
    }
]
```