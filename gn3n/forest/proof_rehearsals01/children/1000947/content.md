# Comprehensive rehearsal — defect-span / spanning-order compression

## Statement

INDEX-3 synthesis: minimum defect span three is exactly a deletion-cover state. The route then has two consumers: 101 fixed-label transport and universal four-window/five-side reversal machinery. Pending 1000954-1000956 now push the fixed-label second layer all the way to synchronized descent, a reachable four-side endpoint-edge reversal, or an endpoint-aligned Hamiltonian 4/5 support. The live unsupported step is consumption of those positioned endpoint obstructions into a two-cover or an ordering whose defect-line matching number is at most one.

## Body


# Comprehensive proof-route synthesis — defect-span / spanning-order compression

## 1. Route summary

The route is driven by the defect line of a spanning order. By the certified identity "1000666", the minimum number c(pi) of contiguous tight-path pieces in an ordering pi is 1+nu(L_pi). Thus a spanning two-cover follows once some order has nu(L_pi)<=1.

In a hypothetical minimum counterexample, the best possible order has c(pi)=3. The central theorem "defectspanisdeletion" says that every such span-three order is exactly a one-vertex deletion two-cover written P,x,Q. The local window has only two forms: the 101 / central-three state and the 111 / central-five state ("defectcanonical35_recomp01").

From there there are only two genuinely different continuations:

1. preserve the extra fixed-label structure of 101 and transport the same defect through the graph;
2. forget that extra structure and enter the universal four-window / reversal machinery.

Everything else in this line is best understood as a refinement of one of those two arrows.

## 2. Starting reduction: span three is a deletion state

Assume H is a minimum-order counterexample. Minimum-counterexample calculus gives pc(H)=3 and exact two-covers after every one-vertex deletion ("mincex01").

Choose a spanning order pi minimizing c(pi). Since c(pi)=1+nu(L_pi), the counterexample condition gives c(pi)=3 and nu(L_pi)=2. The target is therefore concrete: reduce the defect-line matching number from two to one.

Now apply "defectspanisdeletion". If i is the leftmost defect center and x=v_{i+1}, then the prefix P and suffix Q are tight and H-x=P|Q. So the defect-span route and the deletion-cover route meet at the same canonical state P,x,Q.

This is the natural starting configuration.

## 3. Canonical normalization: 101 or 111, plus a universal four-window

The middle join through x gives exactly two linear geometries.

**101.** The middle join is tight. The canonical central bridge has order three. This branch retains the omitted label x and inherited orders on P,Q.

**111.** The middle join is defective. Boundary antisymmetry gives the canonical reversed central five-path. This branch retains a positioned five-side and reversal data.

There is also a route-neutral normalization. The isolated three-edge cyclic matching geometry is impossible ("1000006"), so every deletion singleton lift has a double-wrap rotation ("1000458"). Hence every span-three state can expose a Hamiltonian four-window with pc2 complement inside the connected cyclic-interval reconfiguration family ("cyclic_nonmatching_fourwindow_transport01").

Conceptually:

span-three deletion state
→ either exploit 101 fixed-label transport
→ or enter universal bounded-window / reversal transport.

## 4. Branch A: 101 is fixed-label transport

The point of the 101 branch is not merely local swapping; it is preservation of the same omitted label.

**Certified.** "defect101_finite_transport01" says repeated 101 transport ends in exactly one of two useful states:

- a deletion cover H-x=P|Q with one side of order three; or
- a blocked slide exposing a positioned Hamiltonian four-window with inherited two-path complement.

The blocked-slide case has already joined Branch B. Only the three-side endpoint is intrinsically 101.

**Certified.** "threeside01" then gives persistent fixed-label transport: in four overlapping seven-vertex shells, at least two defect labels can each be moved from one end of the long path to the other while the same defect label is preserved.

The strongest current refinement is live but **pending audit**:

- "1000946": the shell transport lies in the same pairwise-repartition component as the original deletion state;
- "1000950": each shell state descends through a 5|2 -> 4|3 diamond;
- "1000951": the lower 4|3 states glue across shells into a left-to-right constant-Phi corridor carrying one persistent label;
- "1000953": a further pending sharpening reduces failure of synchronized second-layer descent to degree-four core graphs 2K2, P4, or K1,3.

So the strongest current picture is

101
→ fixed omitted label
→ finite transport
→ three-side
→ persistent shell transport
→ mobile same-component 4|3 corridor
→ tiny local residue.

The first unsupported implication is:

**TARGET A — fixed-label corridor compression.**
Turn that mobile fixed-label corridor, or the explicit residual core graphs if "1000953" survives audit, into a spanning two-cover or an order with nu(L_pi)<=1.

Further descent alone is not enough; the proof must retain enough spanning-order provenance to collapse the defect matching.

## 5. Branch B: bounded windows, five-sides, and reversal

This branch contains the blocked 101 outcome and essentially all of 111.

**Certified.** "1000911" is the clean four-window package. For n>14, a Hamiltonian four-window with pc2 complement yields:

- strict quadratic-potential descent;
- nearby four-window migration; or
- an endpoint-aligned Hamiltonian support of order four or five.

The older six-set menus are ingredients of this one conceptual transport theorem.

The 111 state also retains a five-side. **Certified** "five_side_arbitrary_escape01" says a five-side beside a sufficiently long path yields:

- strict Phi descent;
- an equal-size endpoint/support exchange; or
- a tight triple reversing a displayed edge.

Thus four-window transport and five-side transport are really the same kind of producer: they manufacture a small, positioned obstruction.

The first unsupported implication is:

**TARGET B — bounded obstruction consumption.**
Convert an endpoint-aligned 4/5 support, nearby four-window, or displayed-edge reversal into endpoint absorption, a direct two-cover, or nu(L_pi)<=1.

Three cautions matter.

1. An interior reversal is not yet an endpoint reversal.
2. A nearby Hamiltonian support is not automatically a legal same-component move.
3. Neutral migration needs a well-founded termination measure; strict descent is only a contradiction at a componentwise minimum.

The theorem "1000911" also leaves n<=14 as a separate finite-order residue for this particular route.

## 6. Interfaces with neighboring proof lines

**Quadratic-potential / minimal three-cover reconfiguration.**
This line consumes strict Phi descents and rules out small sides at trapped minima; for example "threeside_trapped_order_le11". But it does not by itself return to nu(L_pi)<=1.

**Endpoint transport / bounded-window gluing.**
This is the natural downstream consumer of endpoint-aligned supports and reversals. INDEX 3 produces the obstruction; INDEX 4 is the natural place for the missing gluing/absorption theorem.

**Deletion-cover compatibility / global obstruction structure.**
Compatibility can inject support crossing and order disagreement when local transport stalls. That is useful input, but not closure. The project already has an unconditional reversing tight triple ("1000164"), so producing another reversal is not enough.

**Three-cover no-trapping.**
This line supplies component-minimality constraints that make descent meaningful, but still needs a defect-compression consumer.

**Longest-path / reversal structure.**
This can provide additional positioned reversal information and then enters the same endpoint-transport interface.

## 7. One failed shortcut worth retaining

Common endpoint barriers do not allow one to cyclically rotate ordered tight triples into the desired Hamiltonian windows. "common_endpoint_barriers_fivewindow_counterexample01" gives arbitrarily long counterexamples.

So orientation must be preserved literally. A reversal or barrier must actually be transported into the needed position; it cannot simply be re-read there.

This explains why the present gap is genuinely a transport/compression gap rather than a shortage of local witnesses.

## 8. Residual obstructions

There are two theorem-level gaps.

### A. Fixed-label 101 gap

Certified mathematics reaches persistent fixed-label shell transport. Pending mathematics strengthens this to a mobile same-component 4|3 corridor.

Missing:
global mobility of one fixed defect
→ defect-line matching number drops from two to one.

The required statement must pull the moving three-side/fixed label back to the boundary of a spanning order, not merely produce more local Hamiltonian supports.

### B. Universal bounded-obstruction gap

Certified four-window/five-side machinery reaches positioned small supports, nearby migration, descent, or displayed-edge reversal.

Missing:
positioned bounded obstruction
→ boundary absorption / two-cover / nu(L_pi)<=1.

If neutral transport is used, it needs a true termination measure. If descent is used, it must be component-respecting and interpreted at a minimum.

## 9. Minimal closure package

The smallest plausible closure package is:

1. **Fixed-label corridor compression.** A reachable end-to-end fixed-label 4|3 corridor of the type supplied by pending "1000951" forces a two-cover or nu(L_pi)<=1. If "1000953" survives audit, it suffices to consume its three degree-four residues together with the synchronized cases.

2. **Bounded obstruction consumption.** A reachable endpoint-aligned 4/5 support or displayed-edge reversal from the certified transport packages forces endpoint absorption or nu(L_pi)<=1; neutral migration must have a well-founded termination rule.

3. **Finite-order residue.** Close, or import from another proof line, the n<=14 branch left by "1000911".

Everything before these statements is normalization and obstruction production.

## 10. Mental model

The invariant is nu(L_pi), the matching number of the defect line. A hypothetical counterexample sits exactly one unit above the desired threshold: its best spanning orders have two disjoint defect edges.

The existing theory shows that this two-defect certificate is highly rigid. It is a deletion state; its local window is only 101 or 111; cyclically it always yields a double-wrap four-window; and in 101 one defect label can be transported globally.

So this proof line is fundamentally a **compression problem, not an existence problem**. Reversals, crossings, Hamiltonian windows, and potential descents already exist in abundance. The missing theorem is the mechanism that makes one of those moving local witnesses collide with the spanning-order boundary in a legally controlled way so that the two-edge defect matching collapses to one edge.


## 11. Investigated territory / anti-backtracking map

This section is deliberately broader than the proof spine. Its purpose is to tell a fresh researcher which natural subroutes have already been pushed, what their strongest endpoint is, and why restarting them verbatim is unlikely to help.

### 11.1 Defect-line and canonical-state reductions — settled infrastructure

- **Defect-line optimization (1000666).** The path-cover count of a spanning order is exactly 1+nu(L_pi). Do not rebuild the route around a different local count unless it gives genuinely more information than the defect-line matching number.
- **Span-three = deletion state (defectspanisdeletion).** An optimal three-piece order is already a one-vertex deletion two-cover. Treat deletion-cover and spanning-defect formulations as the same state, not as competing starting points.
- **Canonical 101/111 split (defectcanonical35_recomp01).** The local geometry has already been reduced to central-three or central-five form. Searching for a third generic local pattern is backtracking.
- **Cyclic normalization (1000006, 1000458, cyclic_nonmatching_fourwindow_transport01).** The isolated cyclic matching obstruction has been eliminated and every deletion singleton lift supplies the double-wrap/four-window structure. Re-deriving existence of a generic Hamiltonian four-window is not progress.

### 11.2 101 sliding and fixed-label transport — already pushed to its real bottleneck

- **One-step 101 translation (defect101_slide_or_fourwindow01, certified).** A 101 window either shifts left/right with the same omitted label or immediately exposes a Hamiltonian four-path with explicit inherited two-path complement.
- **Finite transport (defect101_finite_transport01, certified).** Iterating that move already terminates at a three-side deletion cover or the inherited-complement four-window. There is no need to search for a different proof that 101 can be moved toward an endpoint.
- **Persistent three-side transport (threeside01, certified).** Once a side has order three, persistent defect labels can already be transported through the overlapping shell sequence. Merely proving another local fixed-label move is below the present frontier.
- **Shell square/disturbance fork (1000865, pending audit).** Each persistent-defect shell yields either localized order disagreement or a full two-label Hamiltonian-six-set square. This is useful historical territory, but neither output by itself closes defect compression.
- **Degree-counted common-core amplification (1000894, certified).** Two persistent defects have an exact degree-sensitive supply of common-neighbor transport packages; at large order these packages already feed disagreement or strict potential descent. Counting more such local packages is not the missing theorem.
- **Same-component descent corridor (1000946, 1000950, 1000951, pending audit).** The strongest current refinement says fixed-label shell transport stays in the deletion component, every shell edge enters a 4|3 descent diamond, and the lower states glue into a monotone end-to-end 4|3 corridor. If these survive audit, the remaining task is to consume the corridor, not to manufacture another descent layer.
- **Second-layer synchronization (1000953, pending audit).** Failure of synchronized descent is reduced to a degree-four shell whose core graph is 2K2, P4, or K1,3. Do not reopen generic shell synchronization before checking whether the proposed argument already covers the configuration under study.

**Live frontier for this block:** prove TARGET A, i.e. convert the mobile fixed-label corridor (or the explicit degree-four residues) into a spanning two-cover or an order with nu(L_pi)<=1.

### 11.3 Four-window transport — compression theorem already exists

- **Universal four-window transition (1000911, certified).** Above order fourteen, a Hamiltonian four-window with two-cover complement already compresses to strict Phi descent, a distance-one four-window, or an endpoint-aligned Hamiltonian support of order four or five.
- Older six-set menus and intermediate four-window transport chains should normally be read only when proof details are needed; conceptually they have been recomposed into 1000911.
- A new result whose only conclusion is "another nearby four-window exists" is not beyond the present frontier unless it provides a well-founded global termination mechanism or direct boundary absorption.

**Live frontier for this block:** consume endpoint-aligned 4/5 support or give neutral migration a terminating invariant.

### 11.4 Five-side and reversal production — witness existence is not the gap

- **Five-side escape (five_side_arbitrary_escape01, certified).** A five-side beside a long path already gives strict Phi descent, neutral endpoint/support exchange, or a tight triple reversing a displayed edge.
- **Order disagreement (1000211, certified).** Every minimum counterexample already contains explicit relative-order disagreement between overlapping tight paths.
- **Genuine reversing triple (1000164, certified).** Every minimum counterexample already contains a tight triple reversing an edge of a nontrivial tight path.

Consequently, proving another theorem whose endpoint is merely "there exists order disagreement," "there exists a reversal," or "there exists some small Hamiltonian support" is not a new closure mechanism. The missing information is **position and transport**: the witness must be driven to a deletion-cover/spanning-order boundary where it collapses the two-defect matching.

### 11.5 Endpoint-barrier shortcut — ruled out

- **common_endpoint_barriers_fivewindow_counterexample01 (certified).** Even arbitrarily many common endpoint-barrier triples do not let one cyclically reinterpret the configuration as the desired Hamiltonian five-window. The counterexample family exists at arbitrary length.
- Therefore literal orientation data must be preserved. Do not use an argument that silently rotates or rereads an ordered barrier triple into another position.

This is a genuinely dead shortcut unless additional hypotheses unavailable in that counterexample family are explicitly used.

### 11.6 Potential descent — useful only with the correct global context

Many local routes already yield strict quadratic-potential descent. This is valuable only when the state is known to be a minimum in the relevant pairwise-repartition component. Producing additional local Phi decrease without:
1. component membership,
2. a component-minimality hypothesis, or
3. a pullback to the spanning-order defect invariant,
does not advance INDEX 3.

Similarly, neutral repartition/migration without a well-founded measure may cycle. A fresh researcher should not assume that "keep moving the window" is an argument until termination is supplied.

### 11.7 Small-order residue

1000911 isolates n<=14 as a finite-order residue for the universal four-window route. This is already known as a separate obligation. Do not let a proof for large order silently claim the grand theorem without either closing this residue or importing a certified small-order result from another line.

### 11.8 What counts as genuinely new progress

Before opening a new INDEX-3 branch, check whether its endpoint is already one of the following familiar outputs:

- another 101 slide;
- another fixed-label shell move;
- another Hamiltonian four/five/six support;
- another common-core or two-label square;
- another strict Phi descent lacking component-minimality;
- another order disagreement or reversing triple;
- another neutral nearby-window migration.

If so, the result is probably supporting machinery rather than a new proof route.

The clearest genuinely new contributions would instead do at least one of these:

1. **consume the fixed-label 4|3 corridor** into nu(L_pi)<=1 or a spanning two-cover;
2. **consume an endpoint-aligned bounded support/reversal** into boundary absorption;
3. give neutral transport a **well-founded global termination invariant**;
4. close the explicit **degree-four shell residues** from 1000953 if that result survives audit;
5. close or import the **n<=14 finite-order residue**.

A new researcher can therefore begin at one of these consumers without first re-exploring the local-witness production machinery above.


## Coverage update — the fixed-defect second layer is now consumed to the standard frontier

The pending fixed-label corridor chain has advanced beyond `1000953`.

- **`1000954` (pending).** In each reachable lower 4|3 shell layer, failure of synchronized second-layer descent already yields relative-order disagreement between Hamiltonian four-sides *inside the same fixed-defect component*. The earlier 2K2/P4/K1,3 core graphs are therefore no longer terminal residues.
- **`1000955` (pending).** That same-layer disagreement upgrades to a literal shell-local reversing tight triple on an edge of a reachable Hamiltonian four-side.
- **`1000956` (pending).** The internal-edge reversal cases are then absorbed into the standard small-window machinery. What remains is exactly:
  1. synchronized strict second-layer descent;
  2. a reversal of an **end edge** of the reachable Hamiltonian four-side; or
  3. a proper Hamiltonian 4/5 support with pc2 complement, endpoint-aligned in the matching-block branch.

Thus the current INDEX-3 frontier is sharper than TARGET A as originally stated. One should **not** attack the old degree-four shell graph residues directly. Subject to audit, fixed-label transport already feeds the same bounded-obstruction consumer as Branch B.

The line-specific missing implication is now:

> **reachable four-side endpoint-edge reversal / endpoint-aligned 4/5 window -> boundary absorption or defect-line matching number at most one.**

This is essentially the INDEX-3/INDEX-4 interface. Further shell classification or another layer of local descent is below the current frontier unless it supplies a direct consumer for that endpoint-edge reversal.

Audit concentration: `1000954`-`1000956` are pending. If they fail, fall back to the `1000953` degree-four residue described earlier.
