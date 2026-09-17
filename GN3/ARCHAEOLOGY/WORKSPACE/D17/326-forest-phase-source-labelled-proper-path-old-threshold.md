# Any source-labelled prepayment proper-path output descends below its original phase-one checkpoint

**Workspace:** D17
**State:** established
**Key:** `forest-phase-source-labelled-proper-path-old-threshold`

**Summary:** Let F0 be a literal phase-1 maximum-three-forest checkpoint of largest-rail height M. Suppose a finite certificate-retaining legal descendant analysis rooted at F0, without yet entering phase 0, produces a graph-intrinsic proper tight path K; a proper tight cycle counts after choosing one certified cyclic break. The ancestry requirement is essential: K must be an actual output of the source analysis, not an arbitrary path existing elsewhere. Currentize K by R4 to a maximum forest G and compare its largest rail L with the OLD source threshold M. If L>M, G already has phase-1 rank below F0. If L<=M, run the SV40879 marked-largest-rail continuation until closure, first height M+1, or a terminal state. Height M+1 gives strict phase-1 descent below F0; a terminal state enters SV41376 phase 0 and is therefore also strictly below F0. Thus every source-labelled proper-path output born anywhere before payment yields TWO-COVER or strict phased-rank descent below its original phase-1 source, even if intermediate representatives have worse height. This abstracts the threshold argument of SV68431 from pair portals to arbitrary prepayment path/cycle outputs.


### 1. Source-labelled prepayment output
Let H be a hypothetical smallest Strong Level-(1) counterexample and retain a literal maximum spanning three-forest

  F_0=A|B|C                                                (OT.1)

as a phase-1 checkpoint of the SV41376 phased system. Mark a largest rail and put

  M=max{|A|,|B|,|C|},
  Phi_0=(1,|V(H)|-M).                                     (OT.2)

Suppose a finite certificate-retaining LEGAL DESCENDANT ANALYSIS rooted at F_0, and occurring before the lineage has entered any phase-0/payment checkpoint, produces a graph-intrinsic proper vertex-simple tight path

  K.                                                       (OT.3)

A proper vertex-simple tight cycle is permitted as input after choosing and retaining one of its certified cyclic breaks as K.

The source-label hypothesis is essential. It means the proof that produces K retains an actual ancestry chain from F_0 through the intervening phase-1 source representatives and the physical event that emits K: for example an R435 seam output, a blocker P4, a current crossing plus R3 contact, a universal-core Hamilton extension produced by the source packet, or another explicitly legal prepayment construction. An arbitrary tight path that merely exists elsewhere in H is NOT an input to this theorem.

Intermediate phase-1 representatives in the descendant analysis may have largest rail larger or smaller than M. No monotonicity before the birth of K is assumed.

### 2. Currentize the path, but compare to the old source threshold
Accepted smallest-counterexample minimality R4 supplies an exact two-cover

  H-V(K)=U|V                                               (OT.4)

of the proper complement, so

  G=K|U|V                                                  (OT.5)

is a literal maximum spanning three-forest. Let L be the order of a largest rail of G and mark one such rail.

If

  L>M,                                                     (OT.6)

then G already has phase-1 rank

  (1,|V(H)|-L) < (1,|V(H)|-M)=Phi_0.                     (OT.7)

Thus stop with strict descent below the ORIGINAL source F_0.

Assume henceforth L<=M. The key point is that we do not compare G with the possibly worse intermediate representative at which K was emitted. We retain M as the finite ceiling inherited from F_0.

### 3. Largest-rail normalization against the old ceiling
Starting from G, run the chosen marked-largest-rail A-growth continuation of SV40879. Every successful nonclosing growth increases the marked physical descendant by one vertex. Stop at the first of:

1. TWO-COVER: the continuation closes H;
2. OLD-THRESHOLD OVERSHOOT: the marked rail first reaches order M+1;
3. TERMINAL: no further marked-rail growth is available while the marked rail has order at most M.

The process is finite.

In case 2, the current phase-1 checkpoint has rank

  (1,|V(H)|-(M+1)) < Phi_0.                               (OT.8)

In case 3, SV40879 supplies its certificate-bearing balanced-pair entrance and SV41376 passes to phase 0. The leading phase coordinate is then 0, hence the resulting phased rank is strictly below the phase-1 source rank Phi_0 regardless of the trailing pair/payment coordinates:

  phased-rank < Phi_0.                                    (OT.9)

Therefore every nonclosing continuation from K reaches a legitimate checkpoint strictly below the original source F_0.

### 4. Old-threshold source theorem
Combining Sections 1-3 gives:

> SOURCE-LABELLED PREPAYMENT PROPER-PATH DESCENT. If a certificate-retaining legal descendant analysis rooted at a phase-1 maximum-three-forest F_0 produces a proper tight path or proper-cycle break before entering phase 0, then there is a finite certificate-retaining continuation to either a spanning two-cover or a checkpoint of SV41376 phased rank strictly below F_0. The comparison uses the old source height M(F_0); no bound on the height of the intermediate birth representative is required.

This is the path-level parent of the current-pair dimer lift SV68431. In SV68431 the pair-deletion portal plus the restored deleted dimer and one R3 test are merely the mechanism producing the source-labelled proper trimer K; once K is present, the proof above is exactly the remaining threshold argument.

### 5. Why the ancestry condition cannot be dropped
Singletons and dimers are vacuously tight paths in every boundary tournament. If one were allowed to choose an arbitrary proper path unrelated to F_0 and call it a birth, Section 2 would falsely turn mere existence of a dimer into a legal descent from every source state. The theorem makes no such claim.

The progress certificate is the retained source-to-K production chain. In particular, any later use must name the source checkpoint, the physical portal/blocker/curvature event, and the prepayment proof step that produced K. This is the exact distinction between a graph-intrinsic path existing somewhere in H and a path portal born in the reconstruction-closed moduli space.

### 6. Scope fence
The theorem does not consume curvature whose only retained parent checkpoint already lies in phase 0. Returning such a phase-0 lineage to a maximum forest gives leading coordinate 1 and the old-threshold comparison above cannot certify descent below the phase-0 parent.

Likewise, a support change or a fresh maximum forest without any source-labelled proper-path output is not automatically progress. One must either exhibit the proper path/cycle birth or compare the representative by another legitimate global objective. R24 and R5 are not used.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R4"
    }
]
```