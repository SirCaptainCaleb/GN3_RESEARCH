# The tau-three hard cell has source ancestry on a low-transition boundary

**Workspace:** D17
**State:** established
**Key:** `g35-tau-three-hard-cell-source-boundary`

**Summary:** Assume the only numerical non-descent cell from the zipper shortcut, tau(F)=3 (in particular the sharp cell tau(F)=3,w(C*)=2). Let e_j,e_k be the first and last F-transitions on the unique augmenter. They cannot both be incident with the nonsource vertex v. If they were, those two distinct edges would already consume two of the three total F transitions. Source-bearingness of C* supplies a third transition incident with some source spoke, leaving no transition for a second source spoke, contradicting the established old-source degree law that at least two distinct source spokes are B-active. Hence at least one boundary transition is source-spoke-to-B. Its canonical boundary defect state from SV110040 has matching size |M_J| and tau<=2, so the sharp tau-three residue has actual source ancestry at the edge of the low-transition corridor rather than only somewhere in its interior.

### 1. Hard-cell input
Retain the G35 packet and suppose

  tau(F)=3.                                                (SB.1)

This includes the unique numerical non-descent cell of SV111278, where additionally w(C_*)=2. Let

  e_j, e_k

be respectively the first and last old F transitions encountered along the unique augmenting path C_* as in SV110040. They are distinct because C_* contains at least two F transitions.

The old source-cover degree law SV101138 says that at least two distinct source spokes among p,q,r are B-active in F. Equivalently, at least two distinct spokes are incident with selected old F X|B transitions.

### 2. Both boundary transitions cannot be v-transitions
Assume for contradiction that neither e_j nor e_k is source-bearing. Every X|B transition has its X-endpoint in

  X={v,p,q,r}.

Hence both e_j and e_k are incident with v. They are two distinct selected F transitions, so under (SB.1) they consume two of the three total X|B transitions of F.

By SV109219 the augmenter C_* is source-bearing, so C_* also contains an old F transition t-h with t in {p,q,r} and h in B. This is a third transition, distinct from e_j,e_k. Therefore all three F transitions have now been exhausted: two at v and one at the single source spoke t.

But SV101138 requires a selected B-transition at a second distinct source spoke t'!=t. Such an edge would be a fourth F transition, contradicting tau(F)=3. Hence the assumption was impossible.

Therefore

  at least one of e_j,e_k is incident with a source spoke. (SB.2)

### 3. Source ancestry lies on a low-transition boundary state
If e_j is source-bearing, the left boundary defect state L of SV110040 has

  |L|=|M_J|,   tau(L)<=2,                                 (SB.3)

and the newly installed boundary transition is an actual old source-spoke-to-B incidence t-h. The historical source trimer (A,t,C) is retained with it.

If e_k is source-bearing, the exact right-hand dual state R satisfies the same conclusion. Thus in every tau-three packet, and in particular in the sharp zipper cell

  tau(F)=3,  w(C_*)=2,                                    (SB.4)

source ancestry occurs at one of the two canonical low-transition boundaries of the defect corridor.

This improves the weaker statement that source ancestry lies somewhere between the two boundaries. The only numerical cell not already beaten by the internal shortcut cannot hide all source-spoke transitions in the interior.

### 4. Consequence for forward transport
Orient the defect-transport discussion from a source-bearing boundary side. Before the first F-transition on that side, no old F transition has yet been installed, so the prefix transition ledger cannot rise above its tau-one start. Neutral normalization from the preceding section cannot increase it. Thus every physical blocker encountered before the source-bearing boundary either is removed by normalization or points strictly forward toward that boundary. Upon reaching the boundary, one has a matching-size three-cover state of transition count at most two carrying the literal old source edge t-h and the source trimer (A,t,C).

The remaining problem is now genuinely local to source-bearing defect transport: consume the shortcut/pivot blocker at or beyond this boundary. No second source-free tau-three corridor exists.

### 5. Scope
This theorem does not assert that the source-bearing boundary state is already a physical forest and does not by itself produce a full-H cover. It is a structural extinction of the source-free hard cell. It uses only the exact source-degree and corridor facts already retained, and no R24, R5, payment, replay, finite search, or seam classification.
