# D16 — Balanced-pair payment, ancestry, steering, and fixed-turn entry

Complete generic payment development: raw-pair versus paid-floor semantics, signed-support actualization, the historical refund compiler and one-hole correction, terminal and literal-frame descent, endpoint-selective floor preservation, arbitrary coordinate steering, and the R24-free fixed-turn entry.

## Paid floor versus raw mass-two pair

Accepted R547 says two opposite-polarity signed dimers sharing exactly one hinge can be cut to opposite-sign singleton supports on the two nonhinge vertices. Graph-intrinsically this always gives a balanced pair of total support mass two. Its stronger name “ancestry-bearing floor” is licensed only when the ancestor dimers already live inside the signed-payment lineage whose ledger is being retained.

R777 is the explicit retraction that made this semantic boundary unavoidable. At q_1 and q_{m-1}, raw accepted signed dimers already satisfy R547 abundantly, so bare mass-two balanced pairs are almost free. They are not evidence of support descent, cut movement, or proof progress. R784 then blocks the tempting composition raw R547 pair -> R432: Complete Floor Pair Steering requires an active ancestry-bearing floor and its birth/refund/actualization ledger.

Accordingly every use below records whether “floor” means a genuine paid descendant or merely a raw signed singleton pair. This distinction is about provenance, not about the truth of the underlying signed turns.

## Universal preserved-coordinate theorem: R654

R654/P732 is the clean order-free parent for coordinate existence. Fix any vertex p and target x!=p in a hypothetical smallest counterexample. Choose auxiliary t!=p. Pair-Deletion Rigidity gives an exact two-cover H-{p,t}=U sqcup V with both rails nontrivial. Split U at any selected state yz into nonempty contiguous paths A,B. Then A sqcup B sqcup V is a literal three-cover of the same residue, while U sqcup V selects yz across A|B.

Apply R176 to this explicit cross state with spare vertex d=p. The reconstructed R176 proof produces an opposite-sign pair with one support literally singleton (p) and the other of order at most two. If the other support is a dimer, R428 pays it to singleton width while preserving p. This is a genuine chosen payment lineage, not a raw R547 shortcut. Then R432 steers only the other singleton to prescribed x while retaining p. Thus closure occurs or an ancestry-bearing floor {p,x} is obtained.

Consequences for migration. Any older theorem whose only mathematical purpose was “there exists some floor containing prescribed coordinates p,x” is coordinate-subsumed by R654. It should survive only when it carries extra physical ancestry used downstream.

## Minimum R24 cell: payable spokes and explicit pair births

Retired accepted R600/P679 finds two directly R542-payable spoke packets in the exactly-two-bad transitive R24 cell. On tested dimer (a,z), Laz and caz are two head certificates with witnesses L,c; carrier (b,z,a) places (a,z) on a reverse boundary and both witnesses outside. Dually (z,c) is tail-signed by R,a using zcR,zca and carrier (c,z,b). Both packets share complementary carrier singleton b. The durable scarce content is the exact tested spoke orientations, witness sets, and short carriers. Any later hinge cut must retain the appropriate payment ancestry if it is to be called a paid floor.

Retired accepted R603/P682 adds a richer nonanonymous structure. Two explicit H-{a,c} covers force (b,a) tail-signed by L,z and (c,b) head-signed by z,R, so both reverse terminal dimers of J=(a,b,c) are R542-payable. Using common witness z and explicit pair-deletion frames, R526 actualizes two graph-intrinsic opposite-sign births:
  Pi_A=((L,z)_head,(b,a)_tail),
  Pi_C=((c,b)_head,(z,R)_tail).
Their cross overlaps are source-labelled: Pi_A.head intersects Pi_C.tail at z and Pi_A.tail intersects Pi_C.head at b, while like-polarity supports are disjoint.

These facts are not made obsolete by R654 because they remember the minimum-cell gates, common witness z, exact pair-deletion covers, and physical overlap pattern.

## Corrected reading of the R602 cross-end triangle

Retired accepted R602/P681 establishes substantial exact geometry in the minimum R24 cell. First it derives the cross-end tight turns RaL and RcL by explicit P5/P6 obstruction and retains J_*=(L,b,R) tight. It then exhibits three opposite-sign hinged dimer pairs:

1. (L,b) tail-signed by c and (b,R) head-signed by a, hinging at b, so R547 cuts to singleton supports {L},{R}.
2. (a,L) head-signed by R and (b,a) tail-signed by z, hinging at a, so R547 cuts to {L},{b}.
3. (R,c) tail-signed by L and (c,b) head-signed by z, hinging at c, so R547 cuts to {R},{b}.

Therefore the physical triangle on vertices L,b,R is real: every edge is the nonhinge pair of an explicit R547 configuration, and the six ancestor signed dimers and witnesses are exactly known.

Modern provenance correction. P681 does not itself construct a signed-payment lineage for these three ancestor pairs; it applies R547 directly to raw graph-intrinsic signs. By the later accepted R547/R777/R784 dictionary, the unconditional conclusion is three graph-intrinsic opposite-sign singleton pairs with retained hinge-cut ancestry. Calling each a steerable ancestry-bearing floor requires an additional payment-lineage certificate. Thus the old structural mathematics survives intact, while the unqualified “complete floor triangle” wording must not be used to invoke R432.

This section is a fresh document-level correction and is submitted for review because it narrows the operational interpretation of historically accepted R602 without changing its verified turn calculations.

## Root-pinned floors: R623 survives as provenance, R654 subsumes coordinates

Retired accepted R623/P702 starts from one of the exact crossed R621 singleton-deletion cross states for root r. In R176 the spare vertex outside that residue is forced to be r, so the birth has singleton support (r) and an opposite support of order at most two. R428 pays the opposite side while fixing r; R432 then steers only the other singleton to any target x. Hence R623 gives a root-pinned floor {r,x} or closure.

Coordinate-wise this is subsumed by R654. Its retained value is provenance: the chosen R621 cross state, deep/shallow weave, common R176 witness, and root-labelled singleton birth survive as historical ancestry. A consumer that needs only {r,x} should use R654; a consumer that needs to know **which crossed root and which source weave produced the floor** should cite R623.

## Nonstationary root interaction: R627 to R638

R627/P706 had the right strategic idea: preserve a root singleton through payment, target a floor deleting one inward coordinate, puncture the corresponding deep cover into three nonempty paths, force the exact target two-cover to cross those pieces, and run R176 again with spare root r. The intended conclusion was a genuinely later R436 anchor event rather than stationary replay. The revision remained needs-more-work because the proof did not make the difference between old and new signed extension physically explicit enough.

Accepted R638/P717 repairs exactly that issue by choosing the old source cross state so its R176 singleton-r witness is the vertex x_r later deleted. For z use La and x_r=a; for b use Lc and x_r=c; for a,c use Lu and x_r=u. After steering to floor {r,x_r}, puncturing x_r leaves a literal three-cover. Any exact target pair-deletion two-cover selects a crossing e_1. The second R176 birth with spare r gives singleton-r witness y_1 lying in H-{r,x_r}, hence y_1!=x_r. Therefore the new extension dimer {r,y_1} is physically different from the old {r,x_r}. R436 now sees a genuinely later nontrivial contact at the historical anchor and yields strict growth or its explicit reversal/cycle alternatives.

The repair is a provenance repair, not a different high-level strategy: witness inequality y_1!=x_r is the missing nonreplay certificate.

## R640: mathematically informative endpoint-rooted route, but not noncircular R24 restoration

R640/P719 is retained because its construction is useful. At each endpoint e=L,R, punctured deep covers produce opposite boundary trimers. R612 yields a two-witness short-carrier packet, R542 forces a selected singleton-carrier crossing, R527 orients that crossing to capture e, R155 mirror-reenters through a genuine old carrier edge to make a trimer with middle e, and R450 gives closure, a mate clause, or a floor preserving e.

However the deposited proof begins by using R533 to infer |H|>10 and uses R5 to certify exact punctured covers. In the R24 restoration program those facts carry historical dependence back through R24 (directly for the four-deletion part of R5 and through the legacy order-ten lineage for R533). Therefore the claim's old scope sentence calling this a noncircular R24 restoration route cannot be operationally accepted. The revision correctly remains needs-more-work.

Safe use: as a conditional/historical theorem in a context where R5 and R533 are already licensed independently, P719 explains how to retain endpoint identity through capture, mirror reentry, and the final mate/floor consumer. Unsafe use: feeding R640 back into a proof whose purpose is to reconstruct R24 noncircularly.

## Paired middle-gate deletion covers before anonymous payment

Accepted R698/P775 couples the two tested orientations on one physical middle-gate deletion cover. If both complementary X vertices were in the R696 SANDWICH branch, they would each have selected neighbor set {L,R}; the selected-state graph would contain the 4-cycle L-z-R-b-L (or its dual), impossible in a disjoint union of paths. Hence at least one packet is END or FREE.

Retired accepted R699/P776 couples one exact H-{a,c} cover and one exact H-{b,z} cover. If either side yields END, retain the literal one/two-hole mate proposal. Otherwise choose a FREE crossing on each side. Actualize the {a,c}-side with endpoint witness L and the {b,z}-side with R. R527/R526 gives an X-anchored tail dimer P_e and head dimer P_f. Their support bookkeeping shows they are disjoint or meet in exactly one hinge. The disjoint case enters R39's genuine balanced-pair/payment continuation; the hinge case enters R547 with exact actualization ancestry. The two source deletion covers remain distinct; no representative synchronization is asserted.

R702, developed also in D15, is the alternative no-payment consumer of the same paired-orientation idea: outside END mate geometry it retains an actual selected X-Q state into strict interior Q.

## Before paying a signed dimer, inspect its source-cover endpoint seams

Accepted R834 has a clean preferred proof P956 through R879. Suppose H=D sqcup U sqcup V is a literal spanning three-cover by nontrivial paths with D=(p,q). If y is the first vertex of U and tail witness on D, so (p,q,y) is tight, the complete D+U seam clause consists of reversals of (p,q,y) and (q,y,u_1). The first reverse is bad by antisymmetry, so the second reverse (u_1,y,q) is forced tight. Dually, if terminal x of U is a head witness with (x,p,q) tight, then (p,x,u_{r-1}) is forced.

Thus in a source three-cover, sign witnesses at polarity-misaligned rail endpoints produce named reverse seams before any payment is attempted. A seam-quiet cover can only place tail witnesses at rail ends and head witnesses at rail starts in the stated tested orientation. This is a valuable structural consumer of signed-dimer currency and is safe under the corrected width-two seam accounting of D14.

## Interfaces: what payment preserves and what it forgets

A graph-intrinsic balanced pair and an ancestry-bearing paid floor are different objects. R777/R784 are the standing provenance fence. R654 supplies arbitrary coordinate steering once a genuine paid lineage exists; it intentionally forgets specialized gate, seam, carrier, or puncture labels. R224 preserves a chosen endpoint of an ancestry-bearing signed dimer through descent. R249 enters a fixed-turn lineage from a genuine mass-two floor. Specialized constructions may cite these interfaces while retaining extra source geometry, but they do not become identical to the generic payment theorem.

## Signed-support actualization and same-frame capture primitives

R35 is the historical signed-support actualization theorem; accepted R526/P546 is its fully reconstructible modern proof. Let P be a signed support with witness w and let M=(m_0,...,m_r), r>=1, be a disjoint tight marker. If P is head-signed, test the terminal turn (m_{r-1},m_r,w). If it is tight, M is tail-signed by w. If it is bad, R3 forces (w,m_r,m_{r-1}), so the dimer (w,m_r) is tail-signed by m_{r-1}. In either branch one obtains a physical support disjoint from P with polarity opposite to P, together with the exact marker endpoint and witness that certify the birth. The tail-signed case is the head/tail dual, testing (w,m_0,m_1). If P is a dimer in a smallest counterexample, R427 applies to the resulting balanced pair and gives a certificate-retaining continuation to closure or singleton width. This is the actualization/payment primitive; the marker need not remain current later.\n\nR36 is the historical same-frame crossing/capture theorem; accepted R527/P547 is the complete reconstruction. Let T=U⊔V be the exact support-deletion two-cover and suppose it selects a carrier/exterior state xy avoiding the sign witness w. The dimer {x,y} is disjoint from the old signed support and from w; orient it as a marker so that R526 makes either desired endpoint the new signed anchor. This gives the graph-intrinsic pair birth and, for a width-two old support, its aligned paid continuation. If no selected carrier/exterior crossing avoids w, then every such crossing meets w. Delete w from its T-rail. At most three path components remain. Any surviving component that met both sides of the carrier/exterior cut would contain a selected crossing not incident with w, contradiction. Hence all remaining components are cut-pure, giving the exact concentration alternative.\n\nR37 is the witness-adaptive specialization of this same proof: once a selected crossing is present, choose a retained sign witness outside that crossing and orient the marker to capture the desired endpoint. Capture is a historical event attached to the physical crossing, not automatic protection.\n\nR41/R515/P530 gives the compatible fixed-trimer interaction used by payment constructions. For disjoint trimers T=(a,b,c) and U=(p,q,r), the natural terminal dimers (a,b) tail-signed by c and (b,c) head-signed by a cross-pair with the corresponding opposite-polarity terminal dimers of U, producing two mass-four balanced pair births with common middle-anchor pair {b,q}. Applying R448 from each trimer viewpoint gives the explicit nonquiet anchor interaction at b and q. Windowing the argument along any disjoint tight path gives the same conclusion independently for each three-vertex window.\n\nThus D16 contains the actual physical tests behind R526/R527/R515, not merely their names.

## Refund/payment compiler and the exact one-hole boundary

R65-R78 are the cleanest version of the early payment compiler. A fresh far-return state is first made into an actual selected crossing; R527 supplies same-frame capture. Only after a genuine capture and a designated continuation may R42 protection language be used. R66 gives exact endpoint-cut realization. R67 is the literal opposite-support refund lift: restore the deleted set, test the opposite rail at an outside endpoint, and either obtain a two-cover or freeze a strict width-two payment while preserving the far seam. R68 turns the remaining one-hole residue into its exact reverse mate. R69 gives the complete-shield kernel; R70 is the alternative actualization/payment-support classification.

R71-R76 enumerate the finite reroot and gate layers: seam-selective grafts, the transitive triple kernel, Type-E and Type-B boundary outputs, then one-spend and both-spend port templates. These are finite compilers, not broad structural theorems. R76 was parked rather than refuted: the both-spend templates are mathematically usable but strategically unfinished. R77 identifies the precise birth condition for protection: an actual captured descendant followed by the designated quiet continuation. R78 is the zero-move strict-paid compiler: if its single new turn is tight it closes, while if it is bad one gets the exact reverse mate. There is no third inference saying a bad hole automatically finishes.



### One-hole correction

The most important repair in this era is C62. Historical R64 asserted too much: a one-hole proposal does **not** automatically become a spanning two-cover merely because the reverse mate is tight. That revision and its legacy proof are invalid. Accepted R394 is the correct residue theorem: a tight hole closes the proposal; a bad hole gives the exact reverse mate by boundary antisymmetry, and that mate is retained as a physical certificate for a later consumer. Nothing further follows without another argument.

R79-R87 classify the small residual cells generated by the compiler: seam activation, `|U|=4`, seam-shielded `|U|=5`, minimal failure sets, cross-end reverse Hamilton exclusion, the E-bad and E-tight/A-bad amplifiers, and the BDF mate-saturated corner. R85/R87 are especially useful negative information: local first-order saturation is weaker than the desired global closure. R88-R96 continue by compiling a fully failed `|U|=3` cell into an external singleton root and then a fixed-pivot/adaptive-capture/fixed-turn packet. Their conclusion is **local saturation plus a named residual object**, not a hidden global finish.



## Terminal reversal payment with retained ancestry

R532 is the terminal-reversal payment theorem. Write the tail-terminal case with D={t_{m-1},t_m}; the head-terminal case is dual. Choose ν∈V(S) and test E=(t_{m-1},t_m,ν). If E is tight, T extends literally by ν. If E is bad, R3 gives the exact reverse trimer E*=(ν,t_m,t_{m-1}). Retain E or E*, D, T, and the original pair birth as historical ancestry.\n\nFor strict paid descent choose either endpoint z of D to survive and call the other endpoint d. Let O=V(H)\\(V(S)∪V(D)); O is nonempty, else S⊔D already two-covers H. If |O|>=2, choose distinct u,v∈O and orient {d,u,v} by R3 as a tight trimer C. C meets D exactly at d and misses S. R425 then rebirths D as the signed singleton (z) while leaving S untouched, lowering mass by one. If O={u}, the exterior bound R169 gives |S|>=4. Let q be the unsigned endpoint of S; orient {d,u,q} as C. R425 rebirths D as (z) and S as its nonempty signed-side interval S-q, lowering mass by two. Thus either physical endpoint of D can be selected for survival by choosing the other endpoint in the refund marker.\n\nThis is the selected P592 one-marker proof. P593 is a distinct modular route: perform only the terminal attachment/reversal test above, then invoke the endpoint-selective floor theorem R224. Both methods retain the named terminal dimer and its ancestry; P592 preserves the explicit local refund marker, while P593 is shorter when R224 is already in the interface. The displayed P592 argument is complete, but its total dependency closure still inherits the legacy R169/P168 reconstruction gap, which remains explicit.

## Literal pair-frame discharge, refund descent, and the fixed-turn clock

R171 is the strongest same-representative discharge theorem of this era. In a literal cover `H=K ⊔ P ⊔ T` carrying a historical balanced pair of total support mass M, one gets one of three outcomes: a spanning two-cover; strict support-mass descent; or a bounded **support swallow** where the contact trimer contains the whole support, necessarily of size at most three. The preferred proof retains the literal representative throughout. An abandoned alternate proof produced a weaker cover-or-descent statement but lost this same-frame strength, so it is preserved only as an alternate route, not a replacement.

R172 turns the pair descent into a fixed-turn lexicographic clock. For a fixed turn `J=(a,b,c)`, let `A_J` record completed captures of the outer endpoints, let `M` be pair mass, and let the floor-distance coordinate measure whether a mass-two floor contains the target pair `{a,c}`. The lexicographic quantity

`Ψ = (2-|A_J|, M-2, δ_J)`

strictly decreases on every designated quiet nonclosing macro: above mass two, support descent lowers M; at mass two off target, floor steering lowers δ; at a target floor, a completed endpoint capture lowers the first coordinate. The theorem is lineage-relative. It does not provide a global scalar across arbitrary turn changes.

R173/R463 supplies the mate-clause implication calculus. Each literal two-hole proposal is a physical clause `A∨B` and hence gives implication arcs `¬A→B` and `¬B→A`, with the actual proposal retained as certificate. Directed paths propagate tightness. A path from `¬X` to X forces X; a reachable sink decorated by a same-support retained collision gives the corresponding interaction. R173's clause-cycle forcing is the finite special case. Abstract SAT reasoning without the physical proposal certificates is not an allowed substitute.

R174 is the multi-support adjacent-color refund lemma. Disjoint nontrivial signed supports on one tight carrier color the carrier. At an adjacent color change, a carrier interval meets exactly one vertex of each of two supports; refund/rebirth along that interval reduces total support mass by at least two. This is the geometric engine behind many later endpoint floors.

R175 is the one-rail unsigned-end refund: with a singleton on one side and a nontrivial signed support on the other, a current outside path supplies a three-vertex boundary turn; clipping the unsigned end and refunding reduces mass by one while retaining the singleton.



## Literal signed-pair frames have a clean mass-four floor, so R171 strict descent terminates without R24


### Clean literal-frame floor
Let H be a hypothetical smallest Strong Level-(1) counterexample and suppose

  H = K | P | T

is a literal spanning three-cover in the scope of accepted R171, with K a nonempty proper tight path and P,T the two nonempty historical opposite-signed supports. Put

  M = |P|+|T|.

Then M>=4.

Indeed E:=V(P) union V(T) is exactly V(H)-V(K). If M=2, E itself is a tight dimer. If M=3, R3 implies that the three vertices of E admit a tight trimer order. (The formal M=1 case cannot occur because P,T are both nonempty; if one allows an empty-side variant, a singleton is of course a tight path.) Thus whenever M<=3 the whole exterior E supports one tight Hamilton path Q. Since K and Q are disjoint and together span H, K|Q is a spanning two-cover, contradiction. Hence every nonclosing literal R171 frame satisfies M>=4.

This is the strongest floor available from boundary antisymmetry alone at this point: M=4 is not eliminated by the argument because four-vertex P4-free boundary tournaments can exist. The historical upgrade M>=5 in R214 is exactly where the quarantined exterior-four/R24 core enters. We do not use that upgrade here.

### Consecutive R171 descent terminates
Now start from any literal R171 frame of initial pair mass M_0 and follow only the strict historical pair-mass descent output of R171 whenever it occurs. The preferred reconstructible proof P597 is crucial here: every successful peel is performed inside the displayed literal representative, with no fresh completion or representative reset; after a bad seam that does not swallow a whole support, R425 rebirths nonempty opposite-signed descendants and the pair mass strictly decreases. Thus every consecutive strict-descent descendant is again a literal R171 frame to which the clean M>=4 argument above applies.

Consequently the masses form a strictly decreasing integer sequence

  M_0 > M_1 > ... >= 4.

There can therefore be at most M_0-4 consecutive strict-descent outputs. The next R171 output must be one of its two non-descent alternatives: a spanning two-cover or bounded support swallow.

This proves a stronger-scope clean replacement for the termination content of historical R220: no anchored-capacity or one-residual hypothesis is needed once a literal R171 frame is present. In the historical one-residual branch, accepted R217 supplies exactly such a literal frame, so the old R220 conclusion survives with the numerical bound M_0-4 in place of M_0-5.

### Quarantine boundary
Historical R214/R220 used R169 to impose M>=5. Their genuinely R24-sensitive residue is now isolated to the single mass-four literal frame. Everything needed merely to rule out indefinite strict R171 mass descent is R24-free.

No claim is made that a mass-four literal frame is impossible, that bounded support swallow closes H, or that pair mass is monotone across unrelated remints or representative resets.


## One-residual R171 swallow is cleanly six-profile; R24 is exactly the three mass-four cells


### Setup and clean inherited bounds
Start in the accepted one-residual anchored-capacity branch. Accepted R217 reconstructs the literal entrance

  H = J_0 | P_0 | T_0

in the scope of R171, with 1<=|J_0|<=3. Follow the literal R171 peel lineage through consecutive strict historical pair-mass descents until its first non-descent output. By the clean termination theorem `literal-frame-r24-free-mass-floor-and-termination`, this occurs after finitely many strict descents without using R24.

The proof-level interval persistence used in historical P221 is independent of its quarantined rail-floor citations: the preferred R171/P597 peel stays in the same literal no-recompletion lineage, and the third component at the terminal frame is a surviving literal interval of the original one-residual path J_0. Hence at the terminal non-descent frame

  H = J | S | T

we retain

  1 <= |J| <= 3.

If the non-descent output is bounded support swallow, R171 itself says the order-three failure/contact marker contains the whole swallowed historical support S. Therefore

  1 <= |S| <= 3.

No R24, R168, R169, or R214 is used in either bound.

### Clean total-size floor
The union V(S) union V(J) is the full physical complement of the untouched literal rail T in the terminal three-cover. If

  |S|+|J| <= 3,

then that entire complement is Hamiltonian: order two is a dimer, and order three admits a tight trimer orientation by R3. Its Hamilton path together with T is a spanning two-cover of H. Therefore every nonclosing terminal swallow satisfies

  |S|+|J| >= 4.

Combining 1<=|S|,|J|<=3 with this clean total-size floor leaves exactly

  (|S|,|J|) in {(1,3),(2,2),(2,3),(3,1),(3,2),(3,3)}.

This is the complete R24-free terminal size normal form for the one-residual swallow branch.

### Exact quarantine boundary
Historical R221/P221 claimed only

  (2,3), (3,2), (3,3).

Inspecting its proof shows why. It used R24 to exclude the singleton-swallow row (1,3), and R168 to exclude the dimer short rail in the pair-deletion row (2,2) and the singleton short rail in the triple-deletion row (3,1). Those are exactly the three profiles omitted from the clean six-profile theorem.

Equivalently, the difference between the clean theorem and historical R221 is precisely the total-mass-four layer

  (1,3), (2,2), (3,1).

Each asks, in one guise, for Hamiltonian absorption across a four-vertex union where boundary antisymmetry alone does not force a P4. This is the same four-cell obstruction already exposed in R24/R5/R168/R169 repairs.

Thus the one-residual branch no longer depends on R24 for termination or for arbitrary size compression. Its entire remaining quarantine is a finite three-cell mass-four boundary. Any future proof eliminating these three cells restores the historical R221 corner theorem; absent such a proof, the clean profiles (2,3),(3,2),(3,3) remain available exactly as before, while the three mass-four cells must be retained rather than silently discarded.

No claim is made that the three mass-four profiles are realizable, mutually equivalent without additional structure, or closed by the present argument.


## Every one-residual terminal swallow has an R24-free reentry: exterior gateway or the common R881 core


### Input
Use the accepted exact section `one-residual-swallow-clean-six-profile-normal-form` (SV54936). At the first non-descent terminal R171 swallow we have a literal spanning three-cover

  H = J | S | T

where S is the completely swallowed historical signed support, J is the surviving third literal rail, and

  (|S|,|J|) in {(1,3),(2,2),(2,3),(3,1),(3,2),(3,3)}.

The three profiles (2,3),(3,2),(3,3) are already consumed R24-free by accepted R226: because the literal exterior of the untouched path T is exactly E=S union J, the first two profiles have |E|=5 and recycle to the R192 five-exterior replacement program, while (3,3) has |E|=6 and recycles to the R196 four-root puncture fan. We therefore only need to consume the three mass-four profiles.

### Exactness after deleting the swallowed component
Because H=J|S|T is a literal three-cover and S itself is a tight path, deleting all vertices of S leaves the literal two-cover

  H-S = J | T.

This two-cover is exact without any staircase theorem. If H-S had a Hamilton path, that path together with the tight path S would be a spanning two-cover of H, contrary to the counterexample hypothesis.

### The three mass-four profiles all create an order-three singleton-floor failure
Put X=V(S) union V(J), so |X|=4 in each of the remaining profiles.

**Profile (1,3).** Write S={z}. Then H-z=J|T is already an exact singleton-deletion two-cover and J has order three. Thus this is literally an order-three singleton-floor failure with four-cell X=V(J) union {z}.

**Profile (2,2).** Write S={z,w}. The rail J is a tight dimer. By R3, the three-set V(J) union {w} admits a tight trimer P. Hence

  H-z = P | T

is a two-cover. It is exact: if H-z were Hamiltonian, a Hamilton path of H-z together with singleton {z} would two-cover H. Again the short rail has order three and

  V(P) union {z} = V(J) union V(S) = X.

No swallow-contact orientation, R223 payment lineage, or R168 pair-deletion floor is needed.

**Profile (3,1).** Write S={z,w_1,w_2} and J={j}. By R3, the three-set {j,w_1,w_2} admits a tight trimer P. Therefore

  H-z = P | T

is a two-cover, exact by the same singleton-restoration argument. Its four-cell is again

  V(P) union {z} = V(J) union V(S) = X.

Thus every mass-four terminal swallow produces an explicit exact singleton-deletion two-cover with a rail of order three, and it does so on the **same physical four-set X=S union J** carried by the terminal swallow.

### Common R881 reentry
Apply accepted R881 to that explicit singleton-floor failure. Its proof first uses the R594 normalization and R880 finite-base exclusion, then R810. Consequently the retained mass-four union X is a transitive matching-height no-P4 four-cell; the opposite rail is the same literal T (with its chosen Hamilton order, relabelled as the R594 long rail); the surviving long case has m>=6; and H decomposes as the associated order-eight pc=2 core G_8 together with a nonempty Hamilton middle rail N. The ALIGNED/CROSSED gate split is internal to G_8.

Therefore the three mass-four profiles do not constitute three new local cleanup problems. They are three entrances to one already accepted bounded-core O6 object.

### Complete clean terminal interface
Every terminal one-residual R171 swallow now has one of two R24-free consumers:

1. (2,3),(3,2),(3,3): accepted R226 sends the literal untouched rail T and exterior E=S union J to the five/six-exterior gateway machinery;
2. (1,3),(2,2),(3,1): the construction above sends the same physical four-set X=S union J into accepted R881.

Hence termination, size compression, and **reentry of every terminal swallow profile** are all independent of R24, R5, R168, R169, and R214. The mass-four branch is not proved impossible here; rather, its entire uncertainty is exported exactly to the common synchronized-transitive R881/O6 core. Historical R221's use of R24/R168 is no longer needed as a routing theorem.


## A terminal R171 support swallow cannot have swallowed-plus-third-rail mass four


### Statement
Let H be a hypothetical smallest Strong Level-(1) counterexample and let

  H = J | S | T

be a literal terminal frame in the bounded-swallow output of accepted R171. Thus S is the completely swallowed historical signed support, T is the untouched opposite-signed historical support, and J is the third literal rail. Then

  |S| + |J| != 4.

Equivalently, none of the terminal size profiles (1,3),(2,2),(3,1) can occur.

### The untouched support retains a sign witness inside the four-set
R171 begins with a graph-intrinsic opposite-signed historical pair and explicitly preserves the historical signs as ancestry throughout the literal peel. Therefore T is still a signed support in the terminal frame. Let beta be its retained sign witness. By definition beta is outside V(T). Since the displayed terminal frame partitions all vertices as

  V(H)=V(J) disjoint-union V(S) disjoint-union V(T),

we have

  beta in X := V(J) union V(S).

Assume for contradiction that |X|=4. R171 already gives 1<=|S|<=3 in a bounded swallow, and J is nonempty, so the only profiles are (1,3),(2,2),(3,1).

### Build an exact singleton-deletion trimer row with long rail T
First observe that deleting all of S leaves the literal two-cover J|T of H-S. It is exact: if H-S were Hamiltonian, a Hamilton path of H-S together with the tight path S would be a spanning two-cover of H.

We now produce, in each profile, a vertex z in X and a tight trimer P on X-{z} such that

  H-z = P | T.

- If (|S|,|J|)=(1,3), write S={z} and take P=J.
- If (|S|,|J|)=(2,2), write S={z,w}. The rail J is a tight dimer. By R3 the three-set V(J) union {w} has a tight trimer order P.
- If (|S|,|J|)=(3,1), write S={z,w_1,w_2} and J={j}. By R3 the three-set {j,w_1,w_2} has a tight trimer order P.

In every case P|T is a two-cover of H-z and V(P) union {z}=X. It is exact, because Hamiltonicity of H-z together with singleton {z} would two-cover H.

### R594 endpoint stars contradict the retained sign of T
Apply accepted R594 to the exact singleton-deletion row

  H-z = P | T,

whose short rail P has order three. Use the **same literal order** of T from the terminal R171 frame, and write it as

  T=(t_0,...,t_m).

R594 either closes the small opposite-rail cases or, in its surviving normalization, gives m>=4 and the simultaneous endpoint reverse stars

  (t_1,t_0,x) tight,
  (x,t_m,t_{m-1}) tight

for every x in X.

Now take x=beta, the retained historical sign witness of T.

If T is head-signed by beta, then its historical sign is

  (beta,t_0,t_1) tight.

But R594 gives

  (t_1,t_0,beta) tight,

which is the complete reversal of the same ordered triple. This contradicts R3.

If T is tail-signed by beta, then its historical sign is

  (t_{m-1},t_m,beta) tight,

while R594 gives

  (beta,t_m,t_{m-1}) tight,

again the complete reversal. This also contradicts R3.

Thus |S|+|J|=4 is impossible.

### Consequence for the one-residual corner
Combining this extinction with the accepted six-profile normal form SV54936 leaves exactly

  (|S|,|J|) in {(2,3),(3,2),(3,3)}.

So the historical R221 terminal size conclusion is recovered **without R24, R5, R168, R169, or R214**. The old uses of the singleton rail floor and the pair/triple deletion staircase were stronger than necessary: the retained sign on the untouched historical support T clashes directly with the universal endpoint reverse stars forced by the clean R594 normalization.


## Universal anchored-capacity reduction to contact or the 2+3 / 3+2 / 3+3 swallow corner, without R24


### The clean universal floor entrance
Assume H is a hypothetical smallest Strong Level-(1) counterexample and that no spanning two-cover has yet occurred. Fix any two distinct physical vertices p,x. Accepted R654 gives a finite certificate-retaining continuation to an ancestry-bearing mass-two balanced opposite-sign floor whose singleton supports are exactly {p,x}. Retain its two signed singleton supports together with their witnesses and birth/payment ancestry.

Orient the opposite polarities as a head-signed support (alpha;P) and a tail-signed support (T;beta). At this point P,T are singletons, but only their fixed signed anchors and witnesses matter for the next extremal step.

### Anchored capacity
Apply accepted R179: among all disjoint tight supports realizing those same fixed signed head/tail anchors and witnesses, choose an anchored-capacity maximum (P,T). Let

  X_cap = V(H) - (V(P) union V(T) union {alpha,beta})

be its ordinary reservoir. Accepted R180 gives three exhaustive cases.

1. If X_cap is empty, H has a spanning two-cover.
2. If |X_cap|>=2, retain the R180 capacity-specific same-tested-dimer two-witness collision/contact output. This is the first residual branch.
3. If |X_cap|=1, accepted R217 constructs a nonempty tight path J_0 on the physical complement of P union T, with 1<=|J_0|<=3, and gives the literal signed-pair frame

     H = J_0 | P | T

   to which accepted R171 applies.

The rest of the proof concerns only case 3.

### Clean termination of the literal R171 peel
Follow the preferred literal R171/P597 interval-peel continuation through consecutive strict historical pair-mass descents. At every stage the displayed third rail J is a nonempty surviving interval of J_0, hence

  1 <= |J| <= 3.

Let M be the historical pair mass, the total order of the two signed pair supports in the current literal frame. Every such literal frame satisfies

  M >= 4.                                                     (AC.1)

Indeed, if M<=3, the union of the two pair supports has at most three vertices. For total order two it is a tight dimer; for total order three R3 supplies a tight trimer order on that whole union. Hence the entire pair-support union is one tight path, which together with the third rail J would be a spanning two-cover of H. Contradiction.

Therefore strict integer pair-mass descent can occur only finitely many times. Since H is assumed nonclosing, the first non-descent output is a bounded support swallow. Write its terminal literal frame

  H = J | S | T,                                             (AC.2)

where S is the completely swallowed historical signed support and T is the untouched opposite-signed historical support. R171 gives

  1 <= |S| <= 3,

while the interval persistence above gives 1<=|J|<=3.

Also

  |S|+|J| >= 4.                                              (AC.3)

For if |S|+|J|<=3, the whole physical set V(S) union V(J) has a tight Hamilton path (dimer for order two, R3 trimer for order three), and this path together with T would two-cover H.

Thus the only possible terminal profiles before using the historical sign are

  (|S|,|J|) in {(1,3),(2,2),(2,3),(3,1),(3,2),(3,3)}.       (AC.4)

### The three mass-four profiles are impossible
Assume one of (1,3),(2,2),(3,1), and put

  X_4 = V(S) union V(J),   |X_4|=4.

The terminal R171 pair is still graph-intrinsically signed. In particular the untouched support T has a retained historical sign witness beta outside T. By the literal partition (AC.2),

  beta in X_4.                                               (AC.5)

We now construct an exact singleton-deletion row with long rail exactly the same literal T.

- In profile (1,3), write S={z}; then H-z=J|T and J is a tight trimer.
- In profile (2,2), write S={z,w}. Since J is a dimer, R3 supplies a tight trimer P on V(J) union {w}; then H-z=P|T.
- In profile (3,1), write S={z,w_1,w_2}, J={j}. R3 supplies a tight trimer P on {j,w_1,w_2}; again H-z=P|T.

In every case the displayed two-cover of H-z is exact, because a Hamilton path of H-z together with singleton {z} would two-cover H, and

  V(P) union {z} = X_4.                                    (AC.6)

Apply accepted R594 to this exact singleton-deletion trimer row, using the same literal terminal-frame order

  T=(t_0,...,t_m).

If R594 closes one of its finite opposite-rail cases we are done. Otherwise its surviving normalization gives the simultaneous endpoint reverse stars

  (t_1,t_0,y) tight,    (y,t_m,t_{m-1}) tight              (AC.7)

for every y in X_4. Take y=beta.

If T is head-signed by beta, its retained historical sign is

  (beta,t_0,t_1) tight,

while (AC.7) gives its complete reversal (t_1,t_0,beta) tight. This contradicts R3. If T is tail-signed, its retained historical sign is

  (t_{m-1},t_m,beta) tight,

while (AC.7) gives its complete reversal (beta,t_m,t_{m-1}) tight, again contradicting R3.

Hence none of the three mass-four profiles can occur.

### Clean parent conclusion
Outside a spanning two-cover, every hypothetical smallest counterexample therefore admits an anchored-capacity realization with exactly one of the following residual outputs:

1. the graph-intrinsic R180 capacity collision/contact branch from a reservoir of size at least two; or
2. a terminal one-residual R171 swallow with

     (|S|,|J|) in {(2,3),(3,2),(3,3)}.

This is the full size conclusion of historical R222, with stronger provenance: the universal initial floor is supplied by R654, termination needs only the elementary literal-frame mass floor M>=4, and the three historical R24/R168 exclusions are replaced by the direct R594 endpoint-star contradiction against the retained sign of T.

No step uses R24, R5, R168, R169, R198, or R214.


## Endpoint-selective floor preservation

R224/P586 is the endpoint-selective floor theorem. Let an ancestry-bearing balanced pair contain a signed dimer D=(d_0,d_1) and an opposite-polarity signed support T, disjoint from D. Fix the endpoint z∈{d_0,d_1} to preserve and let d be the other endpoint. Put O=V(H)\\(V(D)∪V(T)). O is nonempty, since otherwise D⊔T already two-covers H.\n\nIf |O|>=2, choose distinct u,v∈O and orient the three-set {d,u,v} as a tight trimer C using R3. C meets D exactly in d and avoids T. Apply R425 after deleting C from the active support bookkeeping. The only surviving interval of D is singleton (z); R425 preserves its sign certificate, using either the old witness or the immediately deleted neighbor d according to which side z occupies. T is untouched. Hence the chosen lineage now has literal singleton support (z).\n\nIf O={u}, then R169 gives |T|>=4. Let q be the unsigned endpoint of the displayed signed path T, so T-q leaves a nonempty signed-side interval. Orient {d,u,q} as a tight trimer C. Again R425 turns D into the signed singleton (z) while rebirthing T as the nonempty signed interval T-q with its original polarity. Thus both cases produce an explicit physical refund certificate preserving exactly z.\n\nNow apply R428. If the other support is already singleton we are at a mass-two floor; otherwise R428 gives a finite certificate-retaining descent to closure or a both-singleton floor while preserving (z). The constructions for d_0 and d_1 are separate alternative continuations and are not simultaneous.\n\nThis is the full displayed P586 argument. The proof text is complete, but the route service still marks the whole dependency closure as not fully reconstructible because R169/P168 remains legacy-dependent. That dependency gap is retained explicitly rather than hidden.

## R24-free entry from a genuine mass-two floor to a fixed turn

**R249 has an R24-free front door.** Let an ancestry-bearing mass-two floor have singleton supports {a},{c}. A counterexample has at least five vertices, since every graph of order at most four can be partitioned into at most two singleton/dimer tight paths. Choose b distinct from a,c. By R3 exactly one of (a,b,c),(c,b,a) is tight; retain it as the proper turn J. Its unordered outer pair is exactly {a,c}.\n\nEnter R172 at this floor with no pre-entry capture credit. Then A_J is empty, so ε_J=2; M=2, so M-2=0; and the floor is already the target outer pair, so δ_J=0. Thus Ψ_J=(2,0,0). R172 says every quiet nonclosing nonexit macro retaining J strictly decreases Ψ_J. Since the second and third coordinates are already zero, the first quiet decrease must lower ε_J, acquiring at least one of a,c as a captured historical signed anchor. This is the fully reconstructible preferred proof P649 and uses only R3 and R172.\n\nThe older P249 route used R198/R169 merely to obtain a third vertex. It remains historically meaningful but is dependency-heavier and should not be used to claim R24 is necessary for fixed-turn entry.

## Certificate-retaining mass descent and arbitrary floor steering

The payment spine is R425 -> R426 -> R427 -> R428/R433 -> R432/R423. R425 is purely local cut memory: a surviving interval of a signed tight path inherits a sign from the old witness if it reaches the signed end, otherwise from the immediately deleted cut neighbor; both cut neighbors remain tight attachments. R426 sandwiches two opposite-polarity nontrivial supports around one outside path. There are three new turns for a singleton middle path and four for a nontrivial one. If all are tight the sandwich participates in a spanning two-cover; if one fails, antisymmetry gives an explicit reverse trimer that clips one or two unsigned support-end vertices, and R425 retains the old signed endpoint/witness. Repeating strictly lowers mass until width at most two. R427 handles the only width-two swallow: choose an outside head distinct from the old witness, reverse the failed seam, use one more antisymmetry test through the witness, and cut exactly one dimer vertex, leaving a singleton. R428 then preserves that singleton while refunding the opposite support to singleton width. R415 is the composed certificate-retaining theorem: every credited decrease has a physical shell/refund certificate and the original pair-birth ancestry remains historical data. R430/R431 show how orientation of a dimer marker chooses the physical captured endpoint. R433 then replaces the opposite singleton by any prescribed x while keeping the chosen singleton fixed, and R432 performs at most two such replacements to steer an ancestry-bearing mass-two floor to any prescribed pair. The word ancestry-bearing is essential. R444 proves that bare singleton signs are vacuous: for distinct p,t the two-vertex path (t,p) simultaneously labels (p) head-signed and (t) tail-signed, with no certified turn. Thus a bare mass-two label is not payment and cannot justify R432. This is exactly the provenance discipline also recorded in D16.

## Fixed-turn endpoint budget and cross-generation interaction

Once a genuine floor exists, R423 fixes a proper turn J=(a,b,c), steers to {a,c}, and repeatedly examines selected predecessor/successor incidence at b in an exact H-{a,c} cover. R434 is the exact incidence ledger. A predecessor yields by antisymmetry a signed dimer anchored at a; a successor gives the dual anchored at c. Actualization either closes or births a balanced pair retaining that anchored dimer. If the endpoint was already completed in an earlier quiet episode, the new nontrivial dimer meets its historical singleton anchor and R436 forces growth, a proper cycle, reverse contact/reversal, or strict signed-side descent. If it is fresh, protect its descendant until it returns as the same singleton coordinate and then restore the other outer endpoint. Therefore each quiet completed episode consumes a fresh member of {a,c}, and at most two are quiet. R437/R439 sharpen this when a both-singleton floor retains the birth certificate of an older balanced pair: steer to the two old signed anchors h,t, choose an internal rail vertex b, and both predecessor and successor channels are immediately nonquiet because they touch old anchors. R440/R449 and R441 supply the four-support/cross-generation analogue: overlapping generations are already paid by R436; disjoint nontrivial supports enter a checkerboard of splice seams in which GG fusion, row/column transfers, and BB reverse-P4 cells all force descent or a typed interaction. R442/R445/R446 specialize the same budget to an internal middle and normalize any surviving geometric output to a proper trimer, then through the mate-or-middle-floor front door. R443 counts n-6 alternative internal-middle packets in one fixed pair-deletion frame.

## Exact-support cross-generation replay does not consume a fresh certificate

Write P=(v_0,...,v_k) with k>=1 and suppose the old certificate is head-signed by z, so (z,v_0,...,v_k) is tight. Set Q=P, viewed as the later support. The hypotheses of R436 hold and Q contains the old signed anchor v_0. Since k>=1, the singleton stationary-replay exception is unavailable. In the accepted proof P449 of R436, when Q begins at v_0 and z is outside Q, the next step tests z v_0 q_1. Here q_1=v_1 and z v_0 v_1 is already tight from the old signed certificate. The tight branch therefore outputs (z,Q)=(z,P) as a strict extension of Q. Every fact used in this discharge was already present before the later pair birth; no new signed witness or certificate carried by Pi_2 is referenced. The tail-signed case is the exact reversal. Now specialize to R458. Its two direct balanced-pair births B_x and B_w have the same nontrivial physical supports M and D, with the distinction lying in the signed certificate on D (witness x versus witness w). Thus R441 necessarily has cross-generation overlap, but on either exact replay M or D its R436 branch admits the certificate-blind discharge just described. Therefore R441/R436 alone cannot logically force an output whose content depends on w, in particular a new literal sibling proposal or the simultaneous endpoint-adjacency cuts required by R461. Any such conclusion requires an additional consumer that explicitly uses both signed certificates or another retained structural coordinate.

## Fixed-trimer remint plus exact replay is witness-role blind

Let the first certificate on D have witness x and the second have witness y distinct from x, with the same tested orientation and polarity. Since D is disjoint from J, and M is the terminal signed dimer of J of opposite polarity, R39 applies to M together with either signed copy of D. Thus B_x=(M,D_x) and B_y=(M,D_y) are direct balanced-pair births. The hypotheses of R160 depend on the same fixed trimer J, one of its terminal signed dimers M, and a partner signed dimer D physically disjoint from J. They do not require the partner witness to lie on a designated residual rail or to come from a splice proposal. Therefore, reading B_x first and B_y second, R160 forces the same nonquiet historical signed-support/anchor or cross-generation pair interaction for every such y. This proves (1).

For (2), both births have exactly the same two nontrivial physical supports M and D. Hence any R441 comparison has cross-generation overlap. Choose either repeated oriented support P in {M,D} and view the later copy as Q=P. Apply R436 to the old signed certificate (z;P) from the first birth and Q=P. Because P is nontrivial, the singleton replay exception is irrelevant. In the at-anchor branch, the already-tight first old signed turn makes R436 return the already-known strict extension (z,P) of Q. This discharge uses only first-birth data and the equality Q=P; the second witness y and its certificate are not referenced. Thus the R441/R436 overlap route can be completed without consuming y.

Consequently the composite remint-plus-overlap argument is invariant under replacing the original R458 witness w by any y that supplies the same-polarity second certificate on D. Any conclusion whose novelty specifically requires w to be an opposite-rail endpoint, or to carry the literal R455 splice provenance, cannot follow from this chain alone. By R461, an exact complementary sibling of a native splice literal must abandon both incident source endpoint adjacencies. Nothing in the witness-substitution-invariant chain constructs such a proposal or uses both endpoint adjacencies, so that two-cut geometry requires an additional consumer.

## Common-polarity family actualization against one opposite support

R40 packages a family version of direct balanced-pair production. Suppose several signed supports carry one common polarity and one disjoint signed support carries the opposite polarity. Pairing the opposite support separately with each common-polarity support yields the corresponding family of direct balanced-pair certificates. The construction is certificate-level: the physical supports, tested orientations, and witnesses remain attached to each birth, while later payment descendants are alternative unless another theorem synchronizes them. This historical interface is useful when a proof needs several alternative paid lineages from one shared opposite support; it does not make pair mass globally monotone or merge the alternatives into one current representative.

## Universal proper-turn front door

Take any three distinct vertices a,b,c. By Boundary Antisymmetry R3, exactly one of abc and cba is tight, so H contains a tight trimer J on those vertices. It remains only to see that J is proper. A graph with at most two vertices has a spanning cover by at most two one- or two-vertex tight paths. A graph on exactly three vertices has a spanning tight trimer by the same antisymmetry argument. Therefore a counterexample has more than three vertices, and J is a proper tight path.

## Distinct payment proofs that preserve different physical information

A few accepted interfaces in this development have mathematically distinct proof routes. They should not be collapsed merely because the conclusion is identical.

**R171, literal signed-pair discharge.** P597 is the preferred full literal-frame proof: reduce cross-support witness positions, split forward/coincident/reverse witness order, write the corresponding block seeds, and use every bad seam as an R3 reverse trimer feeding R425; if no seam is bad, the blocks themselves give a literal spanning two-cover. This route preserves the strongest same-representative geometry, including the support-swallow corner. P559 is a different, more abstract proof: R214 gives initial pair mass at least five and the modern payment theorem drives the ancestry-bearing pair either to closure or strict mass descent. It is shorter and useful when only cover-or-descent is needed, but it does not replace the literal same-frame information. The older P170 interval-peel certificate is also retained historically as the original constructive route; it is compressed and weaker as a modern proof record, but its one-interval-at-a-time surgery explains the later block-seed proof.

**R532, terminal-reversal payment.** P592 records an explicit one-marker signed-interval refund after the terminal attachment/reversal test. P593 factors the same conclusion through endpoint-selective paid-floor continuation. The first route is useful when the exact local refund marker and terminal certificate matter; the second is modular when the paid-floor interface is already present. Both retain ancestry only to the extent stated by R532.

These are alternative methods, not parallel theorem objects. Exact P-ids remain the authoritative routes; this paragraph records why more than one route is mathematically worth keeping.


## Spare-vertex cross-state pair upgrade

Let R be a literal path cover of a residue W and let T be another cover selecting a directed state xy whose endpoints lie in distinct R-components. Choose any spare vertex d outside W. R176/P540 gives the pair birth directly.\n\nLet R_x be the R-component containing x. If R_x is nontrivial, choose the literal R-neighbor p of x. Apply R3 to {p,x,y}. Exactly one of (y,x,p) and (p,x,y) is tight. In the first case the tested dimer (x,p) is head-signed by witness y; the vacuous dimer path (d,y) makes singleton (d) tail-signed by the same witness. In the second case the tested dimer (p,x) is tail-signed by y, while (y,d) makes singleton (d) head-signed by y. Since d lies outside W, the supports are disjoint and oppositely signed.\n\nIf R_x is singleton (x), the selected state xy itself makes singleton (x) tail-signed by y and (y,d) makes singleton (d) head-signed by y. These cases exhaust R_x. The pair birth retains y as common witness, the crossed R-component, and when present the exact old neighbor p. This is the fully reconstructible P540 route; P176 remains only historical compressed provenance.

## Two-witness short-carrier boundary dimer: capture or singleton-width payment

Assume K=(a,b,c) is a tight trimer and its reverse terminal dimer S=(c,b) is head-signed by two distinct exterior witnesses w_1,w_2; the head-end case is dual. Delete D=V(S), and let W=V(H)\\D. The complementary carrier block is singleton {a}. Pair-deletion exactness gives an exact two-cover T of H-D. Apply R508 with deletion D, block {a}, and recompletion path K. T must select a state crossing {a} versus the exterior, hence a physical state {a,y}.\n\nAt most one of the two witnesses equals y, so choose w with w≠y. The selected crossing avoids the exact sign witness w of S. R527 therefore applies in this same deletion cover and actualizes a disjoint marker while retaining S and w. Because S has order two, the aligned payment clause inherited through R526 gives a finite certificate-retaining continuation to either a spanning two-cover or a balanced opposite-sign descendant with a singleton support.\n\nThus the concentration alternative cannot survive once both witnesses are retained: whatever crossing R508 supplies, at least one witness avoids it. This is exactly the fully reconstructible P618 proof of R542.