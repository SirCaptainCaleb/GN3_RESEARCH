# Astra result-mining specialist pass: reusable mathematics extracted

**Summary:** Astra result-mining specialist pass: reusable mathematics extracted

## Statement

Repository-mining summary for the 2026-09-27 Astra abstraction pass: general results were rehomed or extracted into path restriction, cover surgery, insertion, and fractional-cover toolkits while Astra-specific applications and genuinely line-specific hypotheses were preserved.

## Body

# Durable toolkit/general results

**Fractional path-cover and LP toolkit (fractionaltoolkit01).**
Created under methods01 as the topic home for reusable weighted/fractional arguments.
- fractionalduality01: pure fractional path-cover LP duality and weighted-capture minimax theorem, extracted from weightedfractionalduality01. Removed Astra-001 framing and all minimum-counterexample/sharp-shell applications; proof is the same finite LP argument.
- fractionaldeletionfamilyavg01: common deletion-family averaging theorem. From covers of H-v only for v in an arbitrary set A, obtains tau*(H) <= (sum k_v)/(|A|-1), and with an r-component cover of H[A], tau*(H) <= (sum k_v+r)/|A|. This strictly generalizes fractionaldeletionavg01 and fractionalpathavg01; minimum-counterexample hypotheses were only suppliers of deletion covers.
- Rehomed 9acf756c30e6 (dual excess/slack), astra001slackcharge01 (replacement slack charging), and the general laminar-rounding/uncrossing chain rooted at f1d73ee7e88e.
- 508602659032 is a reusable negative fence: a same-mass two-for-two laminar uncrossing of crossing supports must put the whole old union inside the larger replacement support.
- b51448c366fb now depends directly on fractionalduality01, not on the Astra-001 application node.

**Path-cover surgery/comparison (coversurg01).**
- Rehomed 81882d24a52f and f7eff2f10061: minimum-imbalance two-covers forbid every balance-improving Hamiltonian exchange, with nested endpoint-segment non-Hamiltonicity as a direct corollary. No Astra or minimum-counterexample hypothesis is used.
- threecoverquadraticmin01: if a spanning three-cover is Phi-minimal in its pairwise-repartition component, every displayed pair is already a minimum-imbalance two-cover of its union. This is the general core of 9b1b920f0aab / astra003quadraticpotential; trapping and absence of a reachable two-cover were removed.
- Rehomed and retitled 257497a6d724 as “Local balance improvement drives quadratic descent to equitable three-covers.” Its theorem is general; Astra-002/003 are consumers.
- threecoverlexmax01: lexicographic maximality alone confines every pair-union repartition size. This extracts the proof of repartlex01 while removing the no-reachable-two-cover assumption and Astra framing.
- twocoverinseparability01: the relation “u,v lie together in every two-cover” is an equivalence relation and every two-cover respects its classes. This is the general core of astra005criticalclass; the minimum-failure vertex-critical conclusion remains line-specific.
- Rehomed the already-general inseparability consequences rooted at cc27560d3e40, including ac412d91495d.
- Rehomed 6dcb9bd6f3b8: compatible deletion covers separating one prescribed pair have a same-support, equal-or-adjacent insertion obstruction. It needs failure of that prescribed separation, not minimum-counterexample machinery.

**Path restriction/intersection (pathcalc01).**
- Rehomed ca8dc4ee0bde: contiguous-path number of an ordering is one plus the vertex-cover number of its defect line (equivalently the matching number). No Astra hypothesis is used.
- Rehomed astra004fourgooddisagree: four Hamiltonian vertex deletions of a non-Hamiltonian set force relative-order disagreement among their Hamilton paths. The proof is an arbitrary-order consistency argument and does not require a longest path.

**Insertion (insert01).**
- Rehomed astra003adjacentonedefect: two exterior vertices individually insertable on opposite sides of one old path vertex produce a combined ordering with at most the single cross defect; hence their enlargement always has a two-cover. The proof is purely local.

# Consolidation and provenance

No cosmetic theorem clones were created where a certified general statement already existed. cc27560d3e40 / ac412d91495d, the minimum-imbalance exchange lemmas, the defect-line theorem, the four-good-deletion disagreement theorem, and the adjacent-insertion lemma were moved to their mathematical topic homes and linked back to the Astra conjectures they inform.

A trial move of 9b1b920f0aab revealed that it owns a large Astra-003 descendant subtree. That move was immediately reversed; instead threecoverquadraticmin01 records only its general core. This preserves the Astra reasoning tree while making the reusable theorem discoverable.

The two old fractional averaging results were not duplicated separately: fractionaldeletionfamilyavg01 subsumes both with one common statement. Likewise fractionalduality01 isolates the pure LP theorem while weightedfractionalduality01 retains the Astra-001 consequences.

# Apparent generality that is false or materially limited

- astra005criticalclass: equivalence/inseparability classes are general, but the assertion that deleting every nonprescribed vertex destroys the distinguished class uses minimum prescribed-separation failure essentially.
- 9cdd9c6216a7: the fractional-perfect-matching conclusion genuinely uses the sharp half-order minimum-counterexample shell; it was returned to fractionalequalityshell01 after being carried along by a toolkit move.
- Astra-003 fixed-order and small-side branches (including order-eleven, 4|4|3, five-side, and synchronized finite-kernel statements) use their size hypotheses substantially; they were not weakened by cosmetic replacement of those hypotheses.
- Astra-004 repeated-label shell conclusions depend on the shell structure. Only the four-good-deletion order-disagreement theorem was extracted.
- Astra-008’s determinant/correlation work is presently a route-specific reformulation around Hamiltonian-support/complement events rather than a standalone general boundary-tournament theorem.
- Astra-009’s packing result is chiefly an application of the deletion-cover supply in a minimum counterexample; no additional reusable mechanism was identified in this pass.
- Astra-010 critical-arc/cube statements genuinely use minimization of backward comparison count/span among path-cover-three witnesses. Their criticality conclusions should not be advertised for arbitrary orders.
- 73bc1e5a9042 genuinely uses failure of a spanning two-cover to force same-support restoration; the global obstruction is doing real work, so it was not generalized merely by deleting pc(H)>2.

# Promising unmined areas

The Astra-003 two-label insertion cluster around astra003twoinsertlocal, astra003uniqueinsertgap, and astra003uniquegaplocal contains more local statements that appear reusable, but their current dependency/provenance chain is intertwined enough to deserve a separate careful extraction pass rather than a bulk move.

The deletion-cover compatibility family surrounding 6dcb9bd6f3b8 likely contains further line-independent support-switch / near-slot transport statements. The endpoint-support comparison around 73bc1e5a9042 may also contain smaller local bridge lemmas once the genuinely global no-two-cover step is separated.

# Repository maintenance note

fractionaltoolkit01 now lives under methods01, but the static core-toolkit Atlas entry does not yet list it. The public GN3N RPC surface exposes Atlas reads but no Atlas-edit operation, and raise_need accepts only predefined need keys, so this Atlas/orientation update remains explicit maintenance debt rather than being forced through an unrelated scheduler need.

## Metadata

- ID: astramining20260927
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
