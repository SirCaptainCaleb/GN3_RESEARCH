# Exact-cover disagreement and one-step component drops lift to phase one before payment

**Workspace:** D17
**State:** established
**Key:** `common-residue-prepayment-phase-lift`

**Summary:** Two broad current-kernel species are already forest-phase born. First, let D have order two or three and let R,T be two exact covers of H-D. Restoring a tight Hamilton path on D turns both into literal maximum three-forests. If R,T are not literally identical up to rail exchange, current R471 either gives same-support R435 geometry or, when support partitions differ, its proof supplies a selected T-state crossing two R-components. Since |H|>10 and |D|<=3, one crossed R-component is nontrivial; one old R-neighbor plus the crossing edge and R3 expose a proper tight trimer before any R176 payment. Second, let C be an exact cover of H-D0 for |D0|=1 or 2 and puncture an internal z, producing a three-cover R=C-z of H-(D0+z). Against any exact two-cover T of that residue, component counting supplies a crossing T-edge. If a crossed R-piece is nontrivial, an inherited C-edge gives the same trimer; if both crossed pieces are singleton, they must be the two sides of a three-vertex source rail and z supplies the inherited edge. In both cases the trimer is born from two retained phase-1 source forests. Choosing the lower-rank source checkpoint and applying SV52939 gives TWO-COVER or phased rank strictly below both source checkpoints. This converts support disagreement and the internal-puncture 3-to-2 packets used by the portal wheel from mere currentness into strict phase-rank instability.

### 1. Exact-cover disagreement on one two- or three-deletion residue
Let H be a hypothetical smallest Strong Level-(1) counterexample and let D be a physical deletion set with 2<=|D|<=3. Choose and retain a tight Hamilton path K_D on D: for |D|=2 this is automatic, while for |D|=3 boundary antisymmetry R3 gives one of the two complete-reversal trimer orders. Let

  R=R_1|R_2,   T=T_1|T_2

be two literal exact two-covers of W=H-D. Restoring K_D gives two literal spanning three-covers

  F_R=K_D|R_1|R_2,
  F_T=K_D|T_1|T_2.                                      (CL.1)

Accepted R4 makes pc(H)=3, so both are genuine phase-1 maximum-three-forest checkpoints.

Suppose first that the unordered support partitions of R and T differ. Use the proof mechanism of accepted R410/R471 before taking its balanced-pair output: some selected physical state xy of one cover, say T, has its endpoints in two distinct R-components. Accepted R533 gives |V(H)|>10, so |W|>=8. Hence the two crossed R-components cannot both be singletons. Choose z in {x,y} lying in a nontrivial R-component and let p be one literal R-neighbor of z. Let w be the other endpoint of {x,y}. Then p,z,w are distinct, the physical state zw is selected in T, and pz is selected in R. Boundary antisymmetry on {p,z,w} gives exactly one tight complete-reversal turn

  (w,z,p)  or  (p,z,w).                                  (CL.2)

Call the resulting proper trimer J. Its birth certificate is source-visible: one of its ordinary physical edges is the selected cross state of T and the other is the retained adjacent state of R. No R176 pair birth, payment, floor steering, or completed-anchor return has occurred.

Suppose instead that the support partitions agree but R and T are not literally the same two Hamilton words up to exchanging the two rails. Accepted current R471 applies directly. It emits one of the exact R435 species on a common support: an adjacent selected-state reversal, a tight reverse trimer, or a vertex-simple proper tight cycle. The reversed dimer and reverse trimer are proper tight paths; a proper cycle yields one after choosing a cyclic break. This geometry is again born directly from the two retained source covers (CL.1), before payment.

Thus every nonidentical exact-cover pair on one physical two- or three-deletion residue exposes a proper-path portal at the phase-1 source packet itself.

### 2. Rank comparison for the exact-exact packet
For a phase-1 forest F let M(F) be its largest rail order and Phi(F)=(1,n-M(F)). Put

  M_*=max(M(F_R),M(F_T))

and choose F_* among F_R,F_T with largest rail order M_*. Then Phi(F_*)<=Phi(F_R),Phi(F_T). Exactly as in the two-checkpoint argument of SV67475, the portal of Section 1 is born from the retained packet {F_R,F_T}; after the path is exposed, the proof of SV52939 only uses the retained phase-1 birth threshold. Apply SV52939 with threshold M_*. It gives either a spanning two-cover or a forest/pair state G with

  phased-rank(G)<Phi(F_*)<=Phi(F_R),Phi(F_T).              (CL.3)

Therefore exact representative disagreement on one pair/triple deletion cannot survive in a nonclosing phase-rank-minimal family. At such a minimum, every exact two-cover of one fixed pair/triple residue is literally the same representative up to rail exchange.

### 3. One internal puncture: lift the 3-to-2 component drop before R159 payment
Now let D_0 be a physical set with |D_0|=1 or 2, let

  C=P|Q

be a literal exact two-cover of H-D_0, and let z outside D_0 be internal on one C-rail, say P. Delete z. The punctured source is a literal three-cover

  R=C-z=L|R'|Q                                            (CL.4)

of W=H-(D_0 union {z}), where L,R' are the two nonempty sides of P-z. Choose any literal exact two-cover T of W. Component counting, equivalently the proof of R159, gives a selected T-state xy whose endpoints lie in two distinct components of (CL.4).

Choose a tight Hamilton path K_0 on D_0 (singleton or automatic dimer) and a tight Hamilton path K_1 on D_0 union {z} (automatic dimer when |D_0|=1, and an R3 trimer when |D_0|=2). Then

  F_C=K_0|P|Q,
  F_T=K_1|T                                                   (CL.5)

are both literal spanning maximum three-forests.

If one of the two crossed components of R is nontrivial, choose the crossing endpoint s in that component and an inherited C-neighbor p of s inside the same component. With t the other endpoint of xy, R3 on {p,s,t} gives a proper trimer whose two source edges are the T crossing and the inherited C-edge, exactly as in (CL.2).

It remains to treat the apparent singleton-split degeneracy where both R-components met by xy are singletons. The untouched C-rail Q is nontrivial. If |D_0|=2 this is accepted R429. If |D_0|=1 and Q were singleton q, the opposite C-rail P would be a Hamilton path of H-(D_0 union {q}), contradicting R429 for that deleted pair. Hence the two crossed singleton components must be L and R'. Therefore P has exactly three vertices

  P=(ell,z,r)  or its reverse,                              (CL.6)

and {x,y}={ell,r}. The selected T-state joins ell and r. Use either source edge z-r or ell-z from (CL.6); one R3 test on the crossing edge and that source edge gives a proper tight trimer. Again the certificate is born from (CL.5) before any R159/R176 pair payment.

Choose the lower-rank checkpoint of F_C,F_T exactly as in Section 2 and apply SV52939. One obtains TWO-COVER or strict phased-rank descent below both source checkpoints. Thus the INTERNAL puncture component-drop packet is phase-one cancellable, including the length-three split-rail corner.

### 4. Parent phase-lifting principle obtained
Combining Sections 1-3 gives the source-visible common-residue phase lift:

> Whenever the current kernel is witnessed either by (i) two nonidentical exact two-covers of one pair/triple deletion residue, or (ii) puncturing one internal vertex from an exact singleton/pair-deletion source cover and comparing the resulting three-cover with an exact two-cover of the same residue, the current obstruction is born as a proper path at a retained phase-1 maximum-three-forest packet. It therefore has a finite certificate-retaining continuation to TWO-COVER or strict SV41376 phased-rank descent.

The theorem consumes the crossing before pair payment. It is stronger than merely applying R159/R176 and paying the resulting pair.

### 5. Scope fence
No claim is made for an arbitrary historical 3-to-2 certificate lacking an exact source cover whose internal puncture produced the larger cover. The phase lift uses the literal source edge adjacent to the punctured vertex or to the crossed component. Likewise, exact-cover disagreement is treated only for deletion sets of order two or three, where the deleted set itself has a retained tight Hamilton path and the source checkpoints (CL.1) are literal minimum three-covers. R24 and R5 are not used.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R4"
    },
    {
        "relation": "dependency",
        "revision_id": "R429"
    },
    {
        "relation": "dependency",
        "revision_id": "R471"
    },
    {
        "relation": "dependency",
        "revision_id": "R533"
    }
]
```