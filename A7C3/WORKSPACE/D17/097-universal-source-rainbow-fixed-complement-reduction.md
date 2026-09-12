# Rainbow hinge currentizes to fixed-complement critical blocks or one split atom

**Workspace:** D17
**State:** established
**Key:** `universal-source-rainbow-fixed-complement-reduction`

**Summary:** In the arbitrary-fragmentation rainbow-hinge branch X-K-Y|Z, the untouched second rail Z is already a fixed Hamilton complement and the first rail is a Hamilton active support Omega. If every puncture of Omega at a K-block vertex stays Hamiltonian by deleting that vertex from the actual rainbow rail, then either Omega itself is Hamiltonian and closes H with Z, or one obtains a fixed-complement critical block eligible for the common-parent R961 fan. If some such puncture fails, that failure is confined to splitting the one literal K block of the rainbow rail and yields a bounded two-piece atom defect. Thus a rainbow hinge does not require transition-count induction: it reduces to the existing fixed-complement critical-block parent or a single split-middle-atom packet.

### 1. Rainbow hinge setup
Retain the hard connected-interaction residue of `universal-source-connected-rainbow-splitstar`. Let

  W=H-{p,z}=L disjoint_union R disjoint_union B

with L,R,B retained Hamilton source atoms, every pair-union non-Hamiltonian, and let an exact two-cover F of W contain a rainbow hinge. After relabelling the three source classes, write one literal F rail as

  P = X_0 - K - Y_0

where X,K,Y are the three distinct source classes and X_0,K,Y_0 are maximal contiguous F-blocks, while the other F rail is Q. Here K denotes the complete middle block of P, not necessarily the entire source class K_source if that class appears elsewhere in F. To avoid collision of notation write the source class as K^src and its displayed middle block as K_0.

Thus

  P=(X_0,K_0,Y_0)

is one literal tight path and Q is the other literal tight path. The physical selected seam states at X_0|K_0 and K_0|Y_0 are retained.

### 2. The rainbow rail gives a fixed-complement active support
Put

  Omega=V(P) union {p,z}?

That enlargement is not automatically useful because p,z are deleted in W. The direct fixed-complement object is instead the actual residue W itself: P|Q is an exact cover with literal Hamilton complement Q. Any support obtained by changing only P while keeping Q fixed remains current inside W, and after restoring one deleted label through the original source bridge or source pivot it becomes an H-singleton or H-pair deletion currentization.

The key observation is local to the middle block. For any vertex k in the interior of the literal K_0 word, deleting k from P splits P into two tight subpaths. If there exists an alternative Hamilton path on V(P)-{k}, then pairing it with Q gives an exact cover of W-k with the SAME literal complement Q. If for every k in V(K_0) there is such a Hamilton puncture path, then the active support V(P) is deletion-Hamiltonian along all K_0 labels. If in addition the corresponding endpoint punctures and the labels outside K_0 are covered by inherited trims or other available rows, one enters the full fixed-complement critical-block interface.

Rather than assume those extra punctures, the exact theorem below isolates what the rainbow hinge itself guarantees.

### 3. Middle-block puncture dichotomy
Fix k in V(K_0). Let K_0=(...,u,k,v,...) in the literal P order, with one-sided interpretation at block ends. Delete k from P.

If the two remaining P fragments can be joined by ANY tight Hamilton path on V(P)-{k}, retain such a path P_k. Then

  P_k | Q

is an exact two-cover of W-k with fixed complement Q. The exactness follows from minimality in the ambient smallest-counterexample setting after adjoining the already deleted pair {p,z} only when used through the appropriate source currentization; within W itself we only need the literal two-cover statement.

If V(P)-{k} is non-Hamiltonian, then the obstruction is localized to ONE deleted vertex inside the literal middle block K_0. The two outer source-class seams X_0|K_0 and K_0|Y_0 survive on opposite sides, and deleting k creates at most two K_0 fragments. Thus the resulting inherited path forest has at most four pieces total on V(P)-{k}: X_0+left(K_0), right(K_0)+Y_0, with empty-side simplifications at block ends. The failure is a bounded SPLIT-MIDDLE-ATOM packet retaining the two original rainbow seams and the physical neighbors of k in K_0.

This is the exact local dichotomy for every middle-block label.

### 4. When all active punctures Hamiltonize, the rainbow hinge becomes a fixed-complement critical block
Suppose now that every vertex v in V(P) has a Hamilton puncture path P_v on V(P)-{v}. This hypothesis may come from additional source-family rows; it is not automatic from the hinge alone. If V(P) itself were Hamiltonian, it already is via P, so the meaningful critical block is an enlarged active support obtained by restoring one omitted source label. The natural restoration is whichever of p,z can be attached through the retained original source order without touching Q.

Concretely, if the rainbow rail contains all of L and R in their source-separated sides so that z can be restored between them with only the two original source turns, then

  Omega=V(P) union {z}

has a literal Hamilton path or is non-Hamiltonian deletion-Hamiltonian depending on the restoration seam. If Hamiltonian, Omega|Q closes the corresponding singleton residue or H after restoring p as appropriate. If non-Hamiltonian but every puncture Omega-v is Hamiltonian by the retained P_v and source trims, then (Omega,Q) is exactly the fixed-complement critical-block parent of `fixed-complement-critical-block-common-parent`.

The same statement holds with p when a source-pivot restoration is available. Therefore the rainbow-hinge branch should be consumed by currentizing ONE omitted source label onto the active rail, not by classifying longer transition words.

### 5. Parent reduction and fence
The established unconditional content is narrower but still useful:

* a rainbow hinge supplies two differently typed selected transitions sharing one literal middle block;
* deleting any middle-block vertex either remains Hamiltonian with the same literal complement Q, or yields one bounded split-middle-atom obstruction with at most two K-fragments and both rainbow seams retained;
* whenever source restoration upgrades the active support to a non-Hamiltonian deletion-Hamiltonian block, the entire branch enters the existing fixed-complement R961 parent interface.

No claim is made that every rainbow hinge automatically gives a full critical block. The missing step is a RAINBOW RESTORATION theorem using the original source bridge L-z-R and the actual location of X,K,Y among L,R,B to restore p or z with controlled seams. That theorem is strictly smaller than arbitrary-fragmentation absorption because the two interaction types already meet on one literal block.

Status: complete local working reduction and interface statement; unreviewed. No standalone closure theorem is asserted.

