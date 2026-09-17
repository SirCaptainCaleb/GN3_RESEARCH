# Exact-cover disagreement, support partitions, and global gluing

**Workspace:** D17
**State:** established
**Key:** `partition-rigidity`

**Summary:** Exact-cover disagreement and a direct R24-independent endpoint-universal gluing argument; rooted payment retains labels without currentizing covers. The elementary coherent-selection gluing lemma allows one compatible partition per pair deletion and removes endpoint-universality/uniqueness hypotheses; the positive global disagreement minimum is the remaining open obstruction.

R408 isolates the basic comparison engine. If a vertex x is an endpoint in one exact two-cover of the same proper residue but internal in another, deleting x turns the first into an at-most-two-cover and the second into a literal three-cover, so R159 births a graph-intrinsic balanced pair. R409 applies this independently to every internal vertex of a fixed endpoint-universal pair-deletion cover. R410/R470/R471 sharpen the contrapositive: outside a balanced-pair birth, every exact two-cover has the same unordered support partition; outside R435 reversal/reverse-trimer/cycle geometry, a common support also has the same literal Hamilton order. Hence endpoint universality factorizes supportwise in R411: every vertex of each fixed rail support is an endpoint of some Hamilton path on that support, and choices on the two supports combine independently. R412 packages the deleted-vertex attachability as a 2x2 bipartite graph. A perfect matching closes H; Hall failure leaves either a singleton-root return or one rail blocked from both deleted vertices, making its endpoint dimers collision-saturated. Endpoint universality globalizes the quiet branch directly, with no singleton-rail-floor input. Fix adjacent deletion pairs D={a,c} and E={a,d}. Choose an exact two-cover of H-D exposing d as a rail endpoint. The d-rail cannot be the singleton (d): otherwise the other rail is Hamiltonian on H-{a,c,d}, while R3 orients the deleted triple {a,c,d} as a tight trimer, and those two disjoint paths span H. Thus trimming d leaves two nonempty rails and hence a literal exact two-cover of H-{a,c,d}. Dually, choose an exact two-cover of H-E exposing c and trim c; the same singleton argument makes this another literal exact two-cover of the common triple-deletion residue. R410 now says that either this common-residue comparison births the graph-intrinsic balanced opposite-sign pair, or the two restricted support partitions agree. In the quiet branch every adjacent pair of deletion fibers therefore agrees on its triple overlap. Connectivity of the two-subset exchange graph makes same-block membership well defined globally, producing a bipartition A|B whose restrictions are all pair-deletion support partitions. Both classes have order at least three without any separate rail-floor theorem: if |A|<=2, choose a deletion pair containing A and the corresponding A-rail would be empty, contradicting exactness; similarly for B. Pair-deleting two vertices from A shows B itself Hamiltonian, and dually A is Hamiltonian, so A and B close H. Thus a globally quiet endpoint-universal regime cannot survive. This direct argument uses only R3 and R410 beyond endpoint universality itself.

### Rooted payment repairs deletion-label loss but not cross-fiber currentization

The component-drop section D23/component-drop now contains a direct rooted cross-state payment lemma. If two covers of a proper residue W exhibit a selected state alpha beta crossing components of the comparison cover, then for any chosen spare xi outside W, boundary antisymmetry makes the cross-state support {alpha,beta} and singleton {xi} a singleton-plus-dimer balanced pair of opposite polarity; accepted R428 then pays the nontrivial support while preserving xi. Consequently the noisy branch of R410 has a stronger smallest-counterexample interpretation: for W=H-D with D={p,t}, a partition-disagreement crossing can be paid, unless H closes, to an ancestry-bearing floor preserving either prescribed deletion label p or t. The same applies to each puncture-indexed R409 component drop, with the punctured vertex itself preserved.

This materially repairs a provenance loss, but it is not the mechanism used in the direct endpoint-universal gluing argument above. The R428 continuation retains the original pair-birth/cross-state certificate as historical ancestry while explicitly not preserving the old exact covers as current representatives. Hence a paid floor rooted at p does not by itself produce a new exact H-D cover with improved support partition, nor an exact cover of a neighboring deletion fiber whose endpoint block is physically coupled to the old crossing. For arguments that do not have endpoint universality available, the surviving global compatibility gap is therefore a currentization/transport statement, not mere pair or floor existence: one must turn source-labelled crossing ancestry back into a controlled exact-cover representative, or otherwise consume that source crossing in a closure argument. Generic floor steering and generic fixed-turn reentry do not supply this implication, and exact-replay fences in D16 prohibit counting anonymous re-entry as progress.

### Scope of the direct endpoint-universal gluing implication

The direct proof above assumes absence of the R410/R176 cross-state output in every common-residue comparison it actually uses, including the triple-deletion comparisons produced by endpoint trimming. Endpoint universality plus support rigidity only inside the original pair-deletion fibers would not suffice by itself: the triple-overlap step needs those literal trimmed covers on the common residue. Also, merely choosing a new representative that agrees with another does not establish universal support rigidity while the original disagreeing representatives still exist.

### Coherent selection of pair-deletion partitions suffices for closure

Let V be finite with n>=5, in any setting with vertex-simple paths on prescribed supports. Suppose that for every two-set D subset V we can choose a cover of V-D by two nonempty disjoint paths. Write its unordered support partition as pi_D. Assume only the following overlap consistency: whenever D and E are two-sets sharing one vertex, the restrictions of pi_D and pi_E to V-(D union E) agree as equivalence relations. Equivalently, every pair u,v surviving both deletions has the same same-block status in the two partitions. Empty blocks are discarded when restricting. No endpoint-exposure or tightness of trimmed paths is assumed.

Then V has a spanning two-path cover.

Proof. For distinct u,v choose any deletion pair D disjoint from {u,v}; declare u~v when they are in the same pi_D block. The graph of two-subsets of V-{u,v}, adjacent when they share one vertex, is connected: replace an element toward any desired pair, in at most two exchanges. Each exchange preserves the status of u,v by overlap consistency. Thus ~ is well defined. Set u~u for every u. Symmetry is immediate. For three distinct u,v,w there is a deletion pair disjoint from all three because n>=5, so transitivity follows from transitivity in its partition pi_D.

There are at most two equivalence classes: if there were three, choose representatives u,v,w and a deletion pair avoiding them, contradicting the fact that pi_D has only two blocks. There are at least two classes, because any pi_D has two nonempty blocks whose representatives are inequivalent. Write the global classes as A,B. For every D, its partition pi_D is exactly the restriction of A|B to V-D, with both restrictions nonempty.

Each class has at least three vertices. If |A|<=2, choose a deletion pair containing A; then V-D has only vertices of B, contrary to the two nonempty pi_D blocks. Similarly |B|>=3. Choose two vertices of A for D. The selected cover on V-D has an entire path with support B. Choose two vertices of B for E to obtain an entire path with support A. These two certified paths have disjoint supports spanning V. This proves the conclusion.

The statement is conditional on existence of a coherent selection; it does not prove that such a selection exists. It allows other exact covers in each residue to have different partitions. It does not require coherent path orders, endpoint universality, partition uniqueness, or a no-balanced-pair hypothesis. Its proof is elementary and independent of the quarantined singleton rail floor and payment machinery. It recovers the useful gluing mechanism under an explicit weaker selection contract. In a smallest-counterexample application, pair-deletion cover domains are nonempty by R3/R4 (as in R429), but compatibility remains the unproved step.

### An exact global disagreement objective

For each D let P_D be the finite nonempty set of unordered support partitions realizable by two nonempty tight paths on H-D. Choose one pi_D in each P_D. Define
  Phi(pi) = sum_{unordered adjacent pairs {D,E}} sum_{{u,v} subset V-(D union E)}
              1[ same_pi_D(u,v) != same_pi_E(u,v) ].
All terms refer to physical vertices of the same H; exchanging path names does not affect Phi. The choices are finite, so Phi has a minimum. Phi=0 is precisely the overlap consistency above. Therefore a hypothetical smallest counterexample of order at least five forces min Phi>0.

The unresolved possible strengthening is a disagreement-repair theorem: from a minimizing family with positive Phi, construct a spanning two-cover of H, or change a collection of chosen actual covers to decrease total Phi. Such a theorem would close the smallest-counterexample problem. No claim of this strengthening, of single-fiber repair sufficiency, or of absence of positive local minima is made here. Every affected overlap must be counted; improving a single comparison while worsening others does not prove descent.

The restrictions in the definition are set partitions, not automatically two-path covers of triple-deletion residues. Applying R176 to a restricted comparison requires an actual path construction, such as lawful endpoint trimming or explicit fragmentation/recompletion. The elementary gluing theorem does not silently provide that construction.

Status: complete internal proof of the conditional gluing and finite-objective statements; independent canonical review has not been performed. The disagreement-repair strengthening is an explicit open target.

## References

```json
[
    {"relation":"dependency","revision_id":"R3"},
    {"relation":"dependency","revision_id":"R408"},
    {"relation":"dependency","revision_id":"R410"},
    {"relation":"dependency","revision_id":"R471"}
]
```
