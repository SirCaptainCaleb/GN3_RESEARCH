# INDEX 1 — Comprehensive deletion-cover compatibility proof rehearsal

## Statement

Researcher-onboarding synthesis for deletion-cover compatibility/global obstruction structure. It gives the complete current route from minimum counterexample through deletion-state consistency, ordinary positioned disturbance, and balanced odd-cycle monodromy; distinguishes certified from pending inputs; records the main fenced/dead approaches; and identifies exactly three live closure interfaces: order-defect placement, crossing synchronization, and odd-cycle integral rounding. Pending theorem 1000948 further shows that every arbitrary selected deletion-cover transversal already exposes a positioned order defect, endpoint mixed-support edge, or inherited three-piece double-deletion crossing; hence the balanced odd cycle is not locally clean, though its integral monodromy/rounding problem remains a distinct global consumer.

## Body

# Route summary

Assume a minimum counterexample H and choose one exact two-path cover F_x of H-x for every vertex x. The deletion-cover route is a local-to-global consistency argument. If sufficiently many deletion states agree, they reconstruct a forbidden spanning two-cover. Therefore a counterexample must carry structured inconsistency. The current theorem package localizes that inconsistency almost completely: every ordinary support configuration produces a support-compatible order defect or a mixed-support edge already tied to an endpoint deletion, while the unique genuinely global residue is a balanced odd support cycle with nontrivial order monodromy and explicit two-deletion disturbance. The deletion-cover line therefore no longer needs more generic disagreement, more generic crossings, or another structural classification. Its live task is to convert already-positioned transition data into the neighboring closure interface: a spanning ordering of defect span at most two. In the odd-cycle branch this becomes a precise integral-rounding problem.

# 0. How a new researcher should use this rehearsal

This document is intended to be sufficient orientation for beginning new work in the deletion-cover compatibility line without first reconstructing its history.

There are three trust levels.

**Certified / established** means the result may be used as settled project mathematics. The main certified inputs in this rehearsal are `mincex01`, `1000694`, `1000758`, `compatibility_triangle_endpoint_transport01`, `compatdegreefour10`, `compatuniformall11`, `1000518`, `1000211`, `1000683`, `double_inward_endhook_not_absorption01`, and `astra003adjacentonedefect`.

**Proved but pending audit** means the result is a live theorem and may be used optimistically for route design, but a claimed final proof of the grand conjecture must either wait for certification or independently re-establish the needed statement. The principal pending package is `1000928`, `1000929`, `1000930`, `1000931`, `1000934`, `1000936`, `1000942`, `1000943`, `1000944`, and `1000945`.

**Targets / proposals** are the unsupported arrows isolated below. They are not facts.

Four pieces of vocabulary are enough to read the route. A deletion state F_x is an exact two-path cover of H-x. Two states are **support-compatible** when they induce the same two support classes on their common domain; they are **fully compatible** when they also induce the same linear order inside those classes. The **selected support graph** has one vertex for each selected path support and one edge for each deletion state joining its two supports. A spanning ordering has **defect span** equal to the width of the interval containing all non-tight consecutive triples; by `1000694`, span at most two is exactly a spanning two-cover.

A researcher entering this line should treat Sections 1–4 as the established/pending architecture, Section 6 as the no-backtracking ledger, and Section 7 as the actual frontier.

# 1. Starting reduction: exact deletion states and the canonical closure interface

Let H be a minimum counterexample.

**Established.** By `mincex01`, pc(H)=3 and every one- and two-vertex deletion has an exact two-path cover. By `1000694`, every exact deletion cover

H-x = P | Q

gives the spanning ordering P,x,Q with defect span exactly three. Conversely, H has a spanning two-cover exactly when some spanning ordering has defect span at most two.

Thus the grand theorem, inside a minimum-counterexample argument, is a one-unit compression problem:

**canonical width three -> width at most two.**

Choose one exact deletion state F_x for every x. The indexed route studies the consistency of this family.

One fact should immediately change how new work is allocated: **bare order disagreement is already settled.** Certified `1000211` proves that every minimum counterexample contains order disagreement. Any argument whose endpoint is merely “two tight paths order a common pair differently” has not advanced this line. The needed output is disagreement with enough support and positional information to interact with the canonical width-three join.

# 2. Consistency package: agreement either glues or localizes to one insertion defect

The first conceptual transformation is

local deletion states -> compatibility structure -> bounded transition defect.

## 2a. Full compatibility

**Established: `1000694`.** Four pairwise fully compatible exact two-cover deletion states reconstruct a global two-cover. Therefore a counterexample cannot contain a four-state clique of full compatibility.

The same theorem gives the exact two-state normal form. If F_a and F_b are fully compatible, then the omitted labels a,b must restore into the same common ordered support. Their insertion slots are either identical or adjacent. If the slots are separated by at least two positions, the two insertions can be combined and H is already two-coverable. If they are adjacent, all local triples in the combined order are certified except one, and boundary antisymmetry supplies the reverse tight triple.

This normal form is important because it exhausts the local geometry of a compatible pair. A new researcher should not reopen arbitrary two-cover insertion configurations: after compatibility is known, the only unresolved local states are same-slot and adjacent-slot replacement.

**Pending global strengthening: `1000928`.** The full-compatibility graph of arbitrarily selected deletion states is K4-minor-free, hence 2-degenerate. This does not close the theorem; its role is to show that compatibility cannot form a thick global network.

## 2b. Support compatibility without order compatibility

**Established: `1000694`.** A pairwise support-compatible family with at least three deletion labels localizes to

F_t = (X-{t}) | Q,

where every H[X-{t}] is Hamiltonian, Q is Hamiltonian, and X itself is not Hamiltonian. The Q-side may be normalized to one fixed Hamilton order. Therefore all unresolved variation lies in the ordered Hamilton deletions of the single critical class X.

**Established: `1000758`.** Endpoint probes against such a family cannot remain featureless. They force one of three kinds of output: at least three cross-class path edges, a direct mixed-support edge, or relative-order disagreement. In the three-crossing case, path degree at the singleton forces a direct mixed-support edge, so the operative outputs are endpoint crossing or order disagreement.

These theorems should be viewed as one package: **global support agreement collapses the problem to one critical Hamilton-deletion class; endpoint deletions then expose the order/crossing defect inside it.**

# 3. Global structural reduction: all ordinary configurations already reach positioned disturbance

The next transformation is

sparse support/compatibility geometry -> a positioned endpoint disturbance,

with one genuinely distinct odd-cycle exception.

**Pending: `1000929`.** For an arbitrary selection of one deletion cover per label, the selected support graph is either a forest or one spanning odd cycle on n=2k+1 vertices, with every support in the cycle of order k.

**Pending: `1000930`.** Ordinary compatibility blocks retain a fixed Hamilton path/order. Thus internal block structure is not an independent obstruction.

For the non-cyclic geometry, the important local mechanisms are already known.

**Established: `compatibility_triangle_endpoint_transport01`.** Two compatibility neighbors on the same side of an anchor produce a synchronized family and hence either a direct mixed-support edge at an endpoint deletion or an order-reversal/disagreement output.

**Pending: `1000934`.** Two suitable endpoint-incompatible probes force a direct mixed-support edge or order disagreement.

These are compressed by the strongest current umbrella theorem.

**Pending: `1000942`.** For a minimum counterexample with one chosen deletion cover after every vertex deletion, at least one of the following holds:

(A) two chosen covers are support-compatible but order-incompatible;

(B) for some anchor F_x=P|Q and some endpoint y of P or Q, F_y contains an ordinary path edge joining surviving vertices from the two support classes of F_x;

(C) the chosen supports form the balanced spanning odd-cycle configuration, but some consecutive double deletion already has an inherited three-piece crossing or relative-order disagreement.

This is the correct structural endpoint of ordinary INDEX 1 work. The forest, compatibility-block, triangle, and endpoint-probe subcases should not be separately re-investigated unless one of the pending theorems fails audit.

A certified abundance package explains the remaining difficulty. `compatdegreefour10` and `compatuniformall11` show that either a high-compatibility anchor already yields synchronized endpoint structure, or every deletion state has linearly many incompatible partners of one broad type. Thus the ordinary branch does not suffer from too few disturbances. It suffers from failure to **synchronize** several disturbances at one closure window.

# 4. The genuinely distinct branch: balanced odd-cycle monodromy

The spanning odd support cycle must remain separate because its obstruction is global rather than tree-like.

## 4a. The odd cycle is already disturbed

**Pending: `1000943`.** Any odd cycle of distinct selected Hamiltonian supports whose consecutive double deletions are two-coverable has a non-clean length-two transition: an internal exchanged label gives an inherited three-piece crossing, or the endpoint-deleted inherited covers have relative-order disagreement. No minimum-counterexample, longest-path, or balance hypothesis is required.

Consequently “prove the exceptional odd cycle cannot remain completely clean” is already done, subject to audit.

## 4b. In the no-order-disagreement subbranch, compatibility produces rank monodromy

Assume the selected cycle states are fully compatible where their supports overlap. Then `1000694` turns each step-two replacement into one of two moves on a common ordered spine: same-slot replacement or adjacent-slot replacement. An adjacent-slot move supplies a reversing triple.

**Pending: `1000936`.** On n=2k+1 labels, at least k-1=(n-3)/2 of the step-two transitions are adjacent-slot reversals.

**Pending refinement: `1000945`.** Every adjacent rank generator occurs at least once, and parity gives a sharp dichotomy. Either there are exactly k-1 reversals, each rank generator appears exactly once, and k+2 transitions are same-slot; or there are at least k+1 reversals, a strict majority. Thus proving “there is at least one reversal” or even “there are linearly many reversals” is no longer new progress.

**Pending complementary coordinate system: `1000944`.** The pair-order data induced on the complement of the ground odd cycle are either restrictions of one global linear order, or a shortest incoherence witness is an odd-gap directed triangle or a directed C4 on the endpoints of two disjoint ground-cycle edges. This should be treated as another description of the same global order obstruction, not as a separate proof route.

## 4c. The integral target is exact

**Pending: `1000931`.** For the ground odd cycle C_{2k+1}, the selected supports satisfy exact incidence identities. In particular, if a tight-path support T is a vertex cover of the ground cycle and |T|=k+1, then T and one selected support form an integral spanning two-cover. The theorem also gives the exact fractional mass-two criterion and dual slack description.

Hence the actual odd-cycle closure problem is:

**ODD-CYCLE ROUNDING.** Use the global same-slot/adjacent-slot monodromy, or the equivalent global-order/odd-gap-triangle/C4 obstruction, to produce a Hamiltonian minimum vertex cover of the ground cycle, or directly a span-two ordering.

The fractional theorem already identifies the correct integral object. Merely improving tau*(H) toward two is not the missing step.

# 5. Natural interfaces with neighboring proof lines

INDEX 1 intrinsically ends when it has produced sufficiently positioned transition data. Two neighboring lines are the natural consumers.

**INDEX 3: defect-span / spanning-order compression.** `1000694` makes this the theorem-level closure interface. A successful consumer must take the order defect, mixed-support crossing, or odd-cycle composite witness and remove one center from the canonical span-three window.

**INDEX 4: endpoint transport / bounded-window gluing.** Mixed-support edges, reversing triples, and inherited three-piece crossings are precisely the local data this line should consume. The key issue is not producing another local gadget but proving that two or more gadgets can be made compatible at one endpoint/join.

Other proof families may be imported when they improve positioning or give a well-founded transport measure, but the synthesis should not silently turn into quadratic-potential, longest-path, or three-cover dynamics.

# 6. No-backtracking ledger: questions already answered or routes already fenced

This section is deliberately operational. A new researcher should not spend a research cycle on any item below unless challenging the cited theorem itself.

## 6a. “Can we at least force order disagreement?”

Yes. `1000211` proves it in every minimum counterexample. Generic disagreement existence is closed. New work must add **position, synchronization, or consumability**.

## 6b. “Can many compatible deletion states coexist?”

Not in a way that directly helps a counterexample. Four mutually fully compatible states glue globally by `1000694`. Pending `1000928` strengthens this to K4-minor-free/2-degenerate compatibility. Do not search for a high-density compatibility regime as a new structural branch; high compatibility is already a route to gluing or endpoint synchronization.

## 6c. “Maybe a compatible pair can have complicated relative insertions?”

No. `1000694` reduces a compatible pair to identical or adjacent insertion slots on one common ordered support. Separated slots already close the theorem. The adjacent case has exactly one uncertified local cross triple and a forced reverse tight triple.

## 6d. “Maybe one reversing triple or two inward endpoint hooks force absorption?”

No. `double_inward_endhook_not_absorption01` gives an explicit non-Hamiltonian four-vertex configuration with both inward hooks. A local reversal gadget by itself is not a closure theorem.

Likewise `astra003adjacentonedefect` shows exactly what adjacent double insertion gives: a Hamiltonian enlargement if the cross triple is tight, otherwise only a one-defect ordering / two-path cover with the reverse triple tight. This is a useful normal form, not a finished splice.

## 6e. “Maybe Hamiltonicity of a small enlargement lets us restore the omitted vertex at an endpoint of the displayed order?”

No. Certified `1000683` gives a Hamiltonian four-set whose omitted vertex extends neither endpoint of a particular Hamiltonian order on the remaining three vertices. Any gluing theorem must use order compatibility, not Hamiltonicity alone.

## 6f. “Can boundary antisymmetry justify reversing or rotating an entire tight path?”

No. Boundary antisymmetry reverses a single ordered triple. It does not give path reversal, cyclic rotation, or arbitrary reordering. Any proof using such a move must certify every new consecutive triple.

## 6g. “Maybe the ordinary branch just needs more crossings or more disagreement witnesses?”

No. `compatdegreefour10` and `compatuniformall11` already give either synchronized endpoint structure or linearly many incompatible partners at every state. `1000942` already reduces the arbitrary selected family to positioned disturbance. The residual issue is **common placement and joint consumption**, not witness abundance.

## 6h. “Maybe the odd cycle only needs one reversal, or a proof that it is not clean?”

No. Pending `1000943` already forces two-deletion disturbance. Pending `1000936` and `1000945` already give a global reversal network, including every rank boundary. New odd-cycle work must compose those events into an integral/spanning consequence.

## 6i. “Maybe a better fractional estimate closes the odd cycle?”

No. Pending `1000931` already supplies exact fractional mass-two criteria and the dual description. The grand theorem is integral. The missing statement is a rounding/gluing theorem producing a Hamiltonian minimum ground-cycle vertex cover or a span-two ordering.

## 6j. “Maybe repeated local transport is enough by recurrence?”

Not without a strict measure or analyzed terminal state. Moving the unique defect without proving descent merely changes its location. Any iterative transport proposal must exhibit a well-founded potential, a no-trapping theorem, or a finite recurrence whose return is itself contradictory.

# 7. Current frontier: three legitimate starting points

A researcher can begin new work at any of these three interfaces without first redoing the structural theory.

## Frontier A — order-defect placement

**Starting data.** A support-compatible but order-incompatible pair F_a,F_b. Certified `1000518` says the pair-state defect survives every further deletion except possibly two labels; if two exceptional labels exist, the entire disagreement is concentrated on that pair.

**What is already available.** Generic order disagreement, robustness under deletion, local reversed edges/reversing triples from path-intersection calculus, and the canonical span-three state P,x,Q.

**Missing implication.**
A robust deletion-cover order defect can be synchronized with some canonical state P,x,Q so that the defect occurs in an endpoint-adjacent bounded window and literal triple checks yield span at most two.

**What would count as real progress.** A theorem that moves or selects the robust defect into the canonical join with a proved invariant; a theorem that two robust disagreement states must share a consumable endpoint pattern; or a direct bounded-window compression theorem using the concentrated exceptional-pair case.

**What would not count as progress.** Another proof that disagreement exists, another unpositioned reversing triple, or another small Hamiltonian window without a gluing statement.

## Frontier B — crossing synchronization

**Starting data.** An anchor F_x=P|Q and endpoint deletion y for which F_y contains a direct ordinary edge between the surviving P- and Q-classes, or the stronger certified high-/low-compatibility abundance supplied by `1000758`, `compatdegreefour10`, and `compatuniformall11`.

**What is already available.** Many individual mixed-support transitions, synchronized endpoint probes in the high-compatibility branch, and linear families of uniform disturbances in the low-compatibility branch.

**Missing implication.**
Two or more such disturbances can be forced onto the same anchor/end with compatible boundary orientations, yielding either a legal splice or a transport step with a strict well-founded descent.

**What would count as real progress.** A common-end/common-anchor synchronization theorem; a two-crossing bounded-window splice with complete consecutive-triple verification; or a monotone support-migration invariant that cannot cycle.

**What would not count as progress.** Producing one more mixed edge, classifying one more local crossing pattern without a consumer, or asserting eventual termination from repetition alone.

## Frontier C — odd-cycle integral rounding

**Starting data.** The balanced selected support cycle S_i, exact support identities, same-slot/adjacent-slot step-two transport, at least k-1 adjacent reversals with every rank boundary represented, and the exact `1000931` criterion that a Hamiltonian minimum vertex cover of the ground cycle closes the branch.

**What is already available.** Two-deletion disturbance (`1000943`), reversal monodromy (`1000936`, `1000945`), the global-order versus odd-gap-triangle/C4 description (`1000944`), and the exact fractional/dual identities (`1000931`).

**Missing implication.**
The global transition word forces a Hamiltonian (k+1)-vertex cover of the ground cycle, or directly forces span at most two.

**What would count as real progress.** A composition rule showing that several adjacent-slot reversals can be realized simultaneously in one support order; an argument that one of the minimum ground-cycle covers inherits a Hamilton order from the monodromy; or a proof that the odd-gap triangle/C4 obstruction feeds Frontier A or B.

**What would not count as progress.** Proving another lower bound on the number of reversals, identifying another single reversal gadget, or sharpening tau* without integral rounding.

# 8. Minimal closure package

At present the route closes if one proves the following package.

**A. Positioned order-defect consumption.** Robust selected order disagreement -> endpoint-adjacent span-two compression.

**B. Synchronized crossing consumption.** Endpoint-local mixed-support disturbances -> legal splice or well-founded transport -> span at most two.

**C. Odd-cycle rounding.** Balanced-cycle monodromy -> Hamiltonian minimum ground-cycle vertex cover or span at most two.

A and B may ultimately be one endpoint-transport theorem. C is genuinely global unless its monodromy can first be converted into A or B.

# 9. Compact dependency map for further reading

A researcher should not need to read the historical tree in order to start. If exact proofs are needed, the shortest useful lookup order is:

`mincex01` gives the minimum-counterexample deletion regime.

`1000694` is the central dictionary: defect span, global gluing, support-family localization, and same/adjacent compatible-pair insertion.

`1000942` is the current global deletion-family reduction, pending audit.

For ordinary branches, `1000758`, `compatibility_triangle_endpoint_transport01`, `compatdegreefour10`, `compatuniformall11`, `1000518`, and pending `1000934` explain exactly what disturbance is available and why abundance is not the missing issue.

For the odd cycle, pending `1000929` gives the support-cycle structure; `1000943` gives unavoidable disturbance; `1000936` and `1000945` give rank monodromy/reversal density; `1000944` gives the global-order obstruction menu; and `1000931` gives the exact integral/fractional target.

The principal fences worth reading before proposing a local splice are `1000683`, `double_inward_endhook_not_absorption01`, and `astra003adjacentonedefect`.

Everything else in the historical compatibility subtree should be treated as implementation detail or provenance unless a proof of one of these package theorems is under audit.

# 10. Mental model

Think of the selected deletion covers as local coordinate charts on H.

If the charts agree too much, they glue to the forbidden global two-cover. Therefore a counterexample must have nontrivial transition maps between charts. The compatibility machinery has already done almost all of the localization: ordinary transition inconsistency becomes endpoint crossing or order defect, while the only global holonomy is the balanced odd cycle.

The research frontier is therefore not “find inconsistency.” It is:

**take transition inconsistency that is already known to exist, synchronize it with the canonical span-three join, and make it delete one global defect rather than merely move that defect.**

That is the invariant picture a new researcher should preserve.

## Coverage update — arbitrary transversals now force positioned disturbance

**Pending: `1000948`.** This should be read as the current theorem-facing strengthening of the global INDEX-1 reduction. For an arbitrary choice of one deletion cover after every vertex deletion, one gets at least one of:

1. a support-compatible but order-incompatible selected pair;
2. an anchor F_x=P|Q and an endpoint deletion whose chosen cover contains an ordinary edge joining the surviving P- and Q-classes;
3. in the balanced spanning odd support cycle, a consecutive double deletion whose two-cover crosses two of the three inherited path pieces created by deleting an internal exchanged label.

So the balanced odd cycle is **not** a featureless terminal branch. Its monodromy/fractional structure remains a useful global coordinate system, but every selected transversal already contains a positioned disturbance suitable for INDEX 3/4 consumption. A new researcher should therefore not treat “eliminate the clean odd cycle” as an open task.

This sharpens the frontier map above as follows:

- **Frontier A/B** already occur for every selected transversal outside the genuinely global monodromy packaging.
- **Frontier C** remains relevant only when one wants to exploit the stronger cyclic structure integrally; it is no longer needed merely to prove the cycle has a local defect.

Audit risk is concentrated in `1000948` and its pending inputs `1000942`/`1000943`. If any of those fail audit, revert to the earlier three-frontier description.
