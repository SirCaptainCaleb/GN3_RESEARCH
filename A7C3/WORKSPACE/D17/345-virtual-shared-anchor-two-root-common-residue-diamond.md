# Two roots sharing one virtual anchor certificate synchronize to a singleton row or a root-dimer R407 packet

**Workspace:** D17
**State:** established
**Key:** `virtual-shared-anchor-two-root-common-residue-diamond`

**Summary:** Start from the repeated-certificate branch of SV73012: two distinct P5 roots d,e have alternative common-center floors {d,xi},{e,xi} whose chosen xi-channels produce the identical oriented signed dimer with the identical witness. Retain the exact pair-deletion source frames F_d on H-{d,xi} and F_e on H-{e,xi}. On W=H-{d,e,xi}, Hamiltonicity would combine with a tight trimer on {d,e,xi} to two-cover H, so pc(W)=2. Hence if e is internal in F_d or d internal in F_e, puncturing that root gives a literal three-cover of W against an exact two-cover and R159/R176 produces a source-visible balanced pair. Otherwise both roots are endpoints. Trimming them gives two exact two-covers of W; accepted R471 yields a balanced pair or explicit R435 geometry unless the trims are literally identical. In that synchronized branch both source incidences underlying the shared R434 certificate survive in one common exact base cover T and have the same selected orientation. The two original frames are endpoint attachments of e and d to T. Attachments on different rails or opposite ends commute; if the common base rail is a singleton, R3 merges the two roots through it. If both attach to the same end of a nontrivial rail, test the two possible root orders. A successful test merges them; if both fail, R3 makes both orientations of the root dimer {d,e} carry the same polarity under the common boundary witness, exactly R407. Every successful merge gives an exact singleton-deletion two-cover of H-xi, and that row retains the shared selected incidence and the tight xi-birth trimer. Thus a repeated virtual anchor certificate is not an amorphous flat recurrence: it currentizes to component-drop/R435 geometry, a source-visible singleton row, or an ancestry-pinned R407 root interaction. This does not yet extinguish phase-zero recurrence.


### 1. Two roots sharing one literal xi-ancestor
Retain the repeated-certificate outcome of `virtual-five-root-anchor-link-tournament-compression` SV73012. Thus d and e are distinct roots of the same Hamilton P5 K, xi is the common center outside K, and the two alternative rooted floor lineages

  {d,xi},   {e,xi}                                         (RD.1)

have chosen R434 xi-channels whose first nonclosing births are the IDENTICAL graph-intrinsic signed-dimer certificate: same tested oriented dimer, same polarity, same witness and same physical anchor xi.

Retain the exact pair-deletion source frames used for those births:

  F_d  exact two-cover of H-{d,xi},
  F_e  exact two-cover of H-{e,xi}.                         (RD.2)

Also retain their exact selected predecessor/successor incidences and chosen internal middles. The descendants are alternative; only the displayed source covers and the graph-intrinsic common birth certificate are compared.

Write the common birth as follows. In the HEAD case

  D=(xi,u),  witnessed by w,  so (w,xi,u) is tight;       (RD.3)

in the TAIL case

  D=(u,xi),  witnessed by w,  so (u,xi,w) is tight.       (RD.4)

For an R434 incidence the physical selected source state is exactly the edge {u,w}. Because the identical certificate occurs in both source frames, u,w are distinct from d,e,xi.

### 2. The common triple-deletion residue has exact cover number two
Put

  W=H-{d,e,xi}.                                            (RD.5)

The three-set {d,e,xi} has a tight Hamilton trimer by boundary antisymmetry R3. If H[W] were Hamiltonian, that Hamilton path together with the tight trimer on {d,e,xi} would be a spanning two-cover of H. Therefore W is non-Hamiltonian.

Smallest-counterexample minimality gives pc(W)<=2, hence

  pc(W)=2.                                                 (RD.6)

Fix when needed one literal exact two-cover T of W.

### 3. Any cross-root internal occurrence is already a component drop
Suppose e is internal on its rail in F_d. Deleting e from F_d splits that rail into two nonempty pieces and leaves the other rail nonempty, producing a literal three-cover

  R_d=F_d-e                                                (RD.7)

of W. Against any exact two-cover T of W, accepted R159 applies. Its fully reconstructed proof selects a T-state crossing two R_d-components and invokes R176, so the resulting balanced pair has explicit source-visible cross-state ancestry.

The same holds if d is internal in F_e.

Hence outside a source-visible R159/R176 component-drop output we may assume

  e is an endpoint in F_d,
  d is an endpoint in F_e.                                (RD.8)

### 4. Endpoint trimming synchronizes the two source frames
Under (RD.8), trim the endpoint root from each source frame:

  T_d=F_d-e,
  T_e=F_e-d.                                               (RD.9)

Pair-deletion rigidity makes both source rails of F_d,F_e nontrivial, so endpoint trimming leaves two nonempty rails. Thus T_d and T_e are literal exact two-covers of the same residue W.

Apply accepted R471. If their support partitions differ, its R410 branch gives a graph-intrinsic R176 balanced pair. If the support partitions agree but one Hamilton rail order differs, R435 gives an exact reversed state, reverse trimer, or proper tight cycle. Therefore outside those explicit outputs,

  T_d=T_e=:T                                               (RD.10)

literally up to exchange of the two rail names.

The physical selected incidence {u,w} underlying the common R434 birth survives both trims because u,w are not d or e. Since the two trimmed covers are literally identical, its selected orientation is the same in both. Consequently the direct-versus-reverse R434 birth subtype is also the same in the two root branches. We have one common exact base cover T of W carrying one common local xi-birth cell.

### 5. The two root frames are endpoint attachments of the common base
Write

  T=P|Q.                                                   (RD.11)

Because e was an endpoint of F_d and trimming it gives T, F_d is obtained from T by attaching e to one endpoint of one base rail. Likewise F_e is obtained from T by attaching d to one endpoint of one base rail. All inherited rail orders are literal.

If the two roots attach to different base rails, perform both endpoint attachments simultaneously. Their seam certificates are disjoint and the two resulting paths form a literal two-cover of H-xi.

If they attach to opposite ends of the same base rail of order at least two, the two endpoint seam certificates again coexist and the doubly extended rail is tight, giving a literal two-cover of H-xi together with the untouched second rail.

If the common attachment rail is a singleton (p), no seam was required by either individual dimer attachment. Boundary antisymmetry on {d,p,e} chooses one of the two complete-reversal trimer orders, so d,p,e or e,p,d is a tight path. Replacing the singleton rail (p) by that trimer again gives a literal two-cover of H-xi.

Thus the only unmerged endpoint pattern is two attachments to the SAME end of one nontrivial base rail.

### 6. Same-end attachment is merge or bidirectional root saturation
Treat the common SOURCE end; the terminal case is dual. Write

  P=(p_0,p_1,...),                                        (RD.12)

with |P|>=2. The two exact source frames certify

  (e,p_0,p_1) tight,
  (d,p_0,p_1) tight.                                      (RD.13)

Test the two possible root-order seams

  alpha=(e,d,p_0),
  beta =(d,e,p_0).                                        (RD.14)

If alpha is tight, then

  (e,d,p_0,p_1,...)                                       (RD.15)

is a tight path, so adjoining the untouched Q gives a literal two-cover of H-xi. If beta is tight, use the order d,e,p_0,p_1,... instead.

Assume both tests are bad. R3 gives the complete reversals

  (p_0,d,e) tight,
  (p_0,e,d) tight.                                        (RD.16)

Thus both tested orientations of the physical root dimer {d,e} are HEAD-signed by the same witness p_0. This is exactly the accepted R407 bidirectional same-witness dimer interaction packet, with the two root labels and common-base ancestry retained.

At the common TERMINAL end the same calculation gives either a doubly extended tight rail or

  (d,e,p_r), (e,d,p_r) tight,                             (RD.17)

so both root-dimer orientations are TAIL-signed by the common terminal witness p_r and R407 again applies.

### 7. The merged branch is an exact singleton row carrying the common xi-birth cell
Whenever Sections 5-6 merge the two endpoint attachments, we obtain a literal two-cover

  C_xi of H-xi.                                            (RD.18)

It is exact: if H-xi were Hamiltonian, a Hamilton path on H-xi together with the singleton (xi) would two-cover H.

Moreover the common selected incidence {u,w} of T survives literally in C_xi, with the same selected orientation. The common graph-intrinsic R434 birth also gives the tight proper trimer

  (w,xi,u) in the HEAD case,
  (u,xi,w) in the TAIL case.                              (RD.19)

Hence the repeated virtual certificate has currentized to one actual singleton-deletion source row carrying its own source-visible xi-birth trimer. Restoring singleton xi gives a literal phase-1 maximum three-forest source for the existing old-threshold portal machinery. G26's fence remains: source-relative phase-1 descent is not by itself strict progress below a phase-zero bottom state.

### 8. Parent consequence and scope
Two distinct roots of the SV73012 repeated-certificate branch therefore have only the following common-parent destinations:

1. SOURCE COMPONENT DROP: an internal cross-root occurrence gives an R159/R176 certificate on W;
2. SAME-RESIDUE DISAGREEMENT: endpoint trims give R410/R435 geometry by R471;
3. SINGLETON-ROW CURRENTIZATION: the attachments merge to an exact H-xi two-cover retaining the common selected incidence and tight xi-birth trimer;
4. ROOT-DIMER INTERACTION: the unique noncommuting same-end fork gives accepted R407 on {d,e} under one common boundary witness.

Thus sharing one literal xi-ancestor is not anonymous replay. It creates a finite two-root common-residue diamond with exact physical outputs before either alternative paid descendant is followed.

This is still not bottom-family extinction. R159 payment, R435 geometry, the singleton-row phase-1 excursion and R407 interaction may all require a family-level consumer. No simultaneous currentness of F_d and F_e is asserted beyond their use as alternative graph-intrinsic source certificates. R24 and R5 are unused.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R159"
    },
    {
        "relation": "dependency",
        "revision_id": "R407"
    },
    {
        "relation": "dependency",
        "revision_id": "R471"
    }
]
```