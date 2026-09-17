# A bad-row mixed edge phase-lifts directly at every good source forest

**Workspace:** D17
**State:** established
**Key:** `fixed-complement-bad-mixed-edge-prepayment-phase-lift`

**Summary:** In a fixed-complement shell V(H)=Omega disjoint Q, fix a bad singleton row C_y of H-y and one actual selected Omega|Q adjacency on physical endpoints o in Omega and q in Q. For every good d != o with Hamilton puncture P_d on Omega-d, the restored row F_d=P_d|Q|{d} is a literal maximum three-forest. If |Q|>=2, choose one Q-neighbor q' of q. Boundary antisymmetry on {o,q,q'} gives one fixed tight trimer using the bad-row mixed edge and the selected Q edge; this same cross-rail proper-path portal is born at every F_d before any R176/payment. If |Q|=1, choose a selected P_d-neighbor r_d of o; antisymmetry on {q,o,r_d} gives a root-specific tight trimer crossing the P_d and Q rails, again born at F_d before payment. Hence every retained bad mixed edge has a prepayment phase-1 lift on every good source forest. By SV52939 each such portal gives TWO-COVER or strict SV41376 phased-rank descent below its source checkpoint. The selected orientation of the bad-row edge is retained as ancestry; the portal may use either physical orientation as forced by R3 and no reversed state is claimed selected. This bypasses the SV66139 paid common-center route for phase lifting, though it does not by itself compare against an already lower phase-0 checkpoint.

### 1. Fixed-complement packet and the phase-1 good source forests
Let H be a hypothetical smallest Strong Level-(1) counterexample and retain

  V(H)=Omega disjoint_union V(Q),

where Q is one literal Hamilton path and Omega is non-Hamiltonian. Let D subset Omega be a family of GOOD labels such that Omega-d is Hamiltonian for every d in D. Fix a BAD label

  y in Omega-D,   Omega-y non-Hamiltonian.

For every d in D choose one actual Hamilton puncture path

  P_d on Omega-d

and retain the exact singleton-deletion row

  C_d=P_d|Q on H-d.

Restoring d as a singleton gives the literal spanning three-cover

  F_d=P_d|Q|{d}.                                           (PL.1)

Accepted R4 gives pc(H)=3, so F_d is a genuine maximum spanning three-forest. Mark any largest rail and regard F_d as a phase-1 checkpoint in the SV41376 phased system. All these good-root forests have the same rail-size profile

  {|Omega|-1, |Q|, 1}.                                    (PL.2)

Now choose one literal exact bad row

  C_y=A|B on H-y.                                          (PL.3)

Because Omega-y is non-Hamiltonian while Q is Hamiltonian, C_y mixes the fixed cut Omega|Q. Retain one ACTUAL SELECTED adjacency of C_y whose physical endpoints lie on opposite sides of the cut. Write the physical endpoints as

  o in Omega-y,   q in Q,                                  (PL.4)

and retain separately the selected direction occurring in C_y. The construction below uses the physical adjacency {o,q}; if R3 forces the reverse dimer orientation inside the new trimer, this does not assert that the reverse orientation was selected in C_y.

Fix any

  d in D-{o}.                                               (PL.5)

Then o belongs to the Hamilton rail P_d of the phase-1 forest F_d.

### 2. Nontrivial fixed complement: one common portal for every good root
Assume first |Q|>=2. Since q lies on the literal Hamilton path Q, choose one actual Q-neighbor q' of q. Thus qq' or q'q is one selected adjacency of the Q rail of every F_d.

Apply boundary antisymmetry R3 to the three distinct physical vertices {o,q,q'} with middle q. Exactly one of the complete reversals

  (o,q,q'),   (q',q,o)                                    (PL.6)

is tight. Retain the tight one and call it K.

K is a vertex-simple proper tight trimer. More importantly, it is a genuine CROSS-RAIL path relative to every good source forest F_d: its physical edge {q,q'} is selected in the Q rail, while o belongs to the disjoint P_d rail, and its other physical edge is the retained mixed bad-row adjacency {o,q}. Hence K is not merely an arbitrary trimer already lying on one F_d rail. It is born from the packet

  (F_d, C_y, selected mixed state on {o,q}, selected Q edge {q,q'}),

before any R176 birth, signed-pair payment, floor steering, R434 incidence, or completed-anchor spend.

Crucially, K is independent of d. Therefore one actual mixed edge of one actual bad row supplies the SAME graph-intrinsic cross-rail proper-path portal at every good phase-1 checkpoint F_d with d != o.

### 3. Singleton fixed complement: rootwise portals still exist
Assume now |Q|=1, so Q={q}. The common-Q-neighbor construction is unavailable. Fix d in D-{o}. Because |D|>=2 in every application of interest and y is an additional label of Omega, the Hamilton support Omega-d has order at least two; in the G25 bad-singleton kernel |D|>=5, so this is automatic. Thus o has at least one actual selected neighbor r_d on the Hamilton path P_d.

Apply R3 to the three distinct vertices {q,o,r_d} with middle o. Exactly one of

  (q,o,r_d),   (r_d,o,q)                                  (PL.7)

is tight. Call the tight trimer K_d.

Again K_d is cross-rail relative to F_d: {o,r_d} is selected on P_d while q is the singleton Q rail, and the other physical edge is the retained mixed bad-row adjacency {o,q}. Thus K_d is a proper-path portal born at the literal phase-1 checkpoint F_d before payment. The portal may now depend on d, but no good root is lost.

### 4. Forest-phase absorption
Apply `forest-phase-path-portal-threshold-reentry` SV52939 to the portal K in Section 2, or K_d in Section 3, with birth checkpoint F_d. Let

  M=max{|Omega|-1, |Q|}.                                  (PL.8)

The phase-1 birth rank is

  Phi_d=(1, |V(H)|-M),                                    (PL.9)

independent of d. SV52939 gives a finite certificate-retaining continuation from the born proper path to either

  TWO-COVER,
  or a forest/pair checkpoint of SV41376 phased rank strictly below Phi_d. (PL.10)

The complete ancestry packet is retained: the good root d, actual puncture path P_d, literal fixed complement Q, bad row C_y, exact selected orientation of its mixed state, physical mixed support {o,q}, the selected host-rail neighbor used in the trimer, the R3 orientation test, and the resulting proper path.

### 5. G25 phase-lifting consequence
The good-bad current star of SV65183/SV65492 and the common-center paid star of SV66139 are therefore not needed merely to obtain a forest-phase birth. A stronger prepayment statement holds:

> BAD-MIXED-EDGE PREPAYMENT PHASE LIFT. In a fixed-complement shell, every actual selected Omega|Q edge of a bad singleton row phase-lifts at every good-root maximum forest F_d (except only the vacuous root d=o where o is deleted) to a graph-intrinsic cross-rail proper tight trimer born before payment. If |Q|>=2 the same trimer works for every root; if |Q|=1 a rootwise trimer works. Each birth is source-relative rank-cancellable by SV52939.

This is exactly a phase lift rather than another current-pair certificate: the proper path is born while the retained state is still the literal spanning maximum three-forest F_d. No R176 descendant, floor, or alternative paid representative is declared current.

### 6. Scope fence
The theorem gives strict phased-rank descent below each GOOD SOURCE checkpoint F_d. It does not, by itself, compare the returned state to an unrelated phase-0 checkpoint that may already have smaller leading phase coordinate. Therefore it is a source-relative phase-lifting theorem, not a standalone proof that every reconstruction-closed global family is extinct.

Likewise, the R3 trimer may use the physical mixed dimer in the orientation opposite to its selected direction in C_y. The selected direction is retained as ancestry, but no reverse selection is asserted. R24 and R5 are not used.

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
    }
]
```