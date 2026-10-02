# Proof rehearsal I — deletion-cover compatibility and global obstruction structure

## Statement

Near-publication rehearsal of the deletion-cover route. From a minimum counterexample, selected exact deletion two-covers either glue, expose a positioned order/support disturbance, or enter the balanced odd-cycle support geometry. The local structural theory is complete up to pending audit; the first unsupported implication is to consume the positioned disturbance, or the odd-cycle monodromy it encodes, into a spanning two-cover (equivalently a spanning ordering of defect span at most two).

## Body


# Deletion-cover compatibility and global obstruction structure

## 1. The proposed proof

We seek to prove that every finite 3-uniform boundary tournament has path-cover number at most two. Assume for contradiction that H is a counterexample of minimum order.

The minimum-counterexample calculus is certified. In particular, pc(H)=3, and for every vertex x the deletion H-x has an exact two-path cover. Fix, once and for all, one such cover

    F_x = P_x | Q_x

for each x in V(H). The proof attempts to reconstruct a spanning two-cover of H from the mutual consistency of these deletion states.

Two selected deletion states are **support-compatible** if, on their common domain, they induce the same bipartition into the two path supports. They are **fully compatible** if, in addition, the induced linear orders on the common support classes agree. The central principle is simple: too much compatibility glues to a global two-cover, whereas failure of compatibility must manifest as a controlled order or support defect.

The certified defect-span theorem gives the target in its most useful form. If H-x=P|Q, then the spanning order obtained by inserting x between P and Q has defect span three; conversely, a spanning order has path-cover number at most two precisely when its defect structure can be compressed to defect span at most two. Thus every deletion state is already a canonical width-three approximation to the desired conclusion. The task is to use incompatibility between deletion states to remove one unit of width.

Unless explicitly marked otherwise, the structural statements below are certified. Results marked **pending** have proofs in the database but have not yet passed independent audit; they are used optimistically in the strongest version of the rehearsal.

## 2. What full compatibility implies

The basic gluing theorem (1000694) has two consequences.

First, four pairwise fully compatible exact deletion covers reconstruct a spanning two-cover of H. Therefore a minimum counterexample cannot contain a four-state clique of full compatibility.

Second, the relative geometry of two fully compatible deletion states is completely rigid. Suppose F_a and F_b are fully compatible. After identifying the common ordered support, the omitted labels a and b are inserted into that support in either the same slot or adjacent slots. If the insertion slots are separated by at least two positions, the two insertions can be performed simultaneously and H is already covered by two tight paths. Hence only the same-slot and adjacent-slot cases survive.

In the adjacent-slot case, all consecutive triples in the combined order are certified except one local triple. Boundary antisymmetry then supplies the reverse tight triple at that location. Thus compatibility does not leave an arbitrary local configuration: it leaves a single, explicitly positioned order defect.

A pending global strengthening (1000928) says that the full-compatibility graph of any selected deletion family is K4-minor-free, hence 2-degenerate. This is not needed for the local normal form, but it reinforces the same conclusion: a counterexample cannot hide inside a thick region of mutually compatible deletion states.

## 3. Support compatibility localizes all order variation

Assume now that at least three selected deletion states are pairwise support-compatible. The certified support-localization part of 1000694 gives a fixed Hamiltonian path Q and a set X such that, after relabelling,

    F_t = (X-{t}) | Q

for every relevant deletion label t, each H[X-{t}] is Hamiltonian, and H[X] itself is not Hamiltonian. The Q-side may be given one fixed Hamilton order. All unresolved variation therefore lies in the Hamiltonian orders of the one-hole sets X-{t}.

This is already a substantial reduction: support compatibility cannot create two independently moving path systems. It creates one critical support X whose deletion orders fail to assemble into a Hamiltonian order of X.

The certified endpoint-probe theorem 1000758 then forces structure inside this critical class. Comparing endpoint deletions against the support-compatible family yields either relative-order disagreement or an ordinary edge joining the two support classes of an anchor deletion cover; the nominal three-crossing alternative collapses to such a mixed-support edge by the path-degree argument at the singleton. In particular, a support-compatible family cannot remain both order-coherent and crossing-free.

The certified triangle transport theorem gives the same conclusion from another direction: two compatibility neighbors on the same side of an anchor synchronize sufficiently to produce either a mixed-support endpoint edge or an order reversal. Hence, once support compatibility is present, the only issue is not existence of a defect but its eventual consumption.

## 4. Global support geometry

Associate to the chosen family {F_x} the selected support graph whose vertices are selected path supports and whose edge corresponding to x joins the two supports of F_x.

The strongest current global classification is pending audit. Theorems 1000929 and 1000937 imply that the selected support system has only two essential forms:

1. a forest of support relations; or
2. a spanning odd cycle C_{2k+1}, in which every selected support has order k.

The proof therefore divides at this point.

### 4.1 The forest branch

In the forest branch, compatibility blocks carry a fixed Hamilton path/order (pending 1000930). The local compatibility and endpoint-probe lemmas can then be propagated along the support tree.

The pending global reduction 1000942, sharpened by pending 1000948, gives the theorem-facing conclusion for an arbitrary selected transversal of deletion covers. Outside the balanced odd cycle, at least one of the following occurs:

- two selected deletion states are support-compatible but order-incompatible; or
- for some anchor F_x=P|Q and an endpoint y of P or Q, the selected cover F_y contains an ordinary edge joining surviving vertices of P and Q.

These are already positioned disturbances: the disagreement belongs to two deletion states, or the support crossing is tied to an endpoint deletion of a canonical state P,x,Q.

There is one important rounding obstruction inside the forest geometry. Pending 1000938 shows that branching in a reduced support tree can already realize fractional mass two while no pair of selected supports has spanning union. Consequently a proof cannot finish the forest branch merely by choosing two existing selected paths more cleverly. A successful argument must manufacture a new Hamiltonian support, or use the positioned order/crossing data to compress the canonical defect window. This is why the natural consumer is endpoint transport rather than pure support selection.

Thus, subject to the pending global classification, the forest branch reduces to the following statement.

**Forest compression target.**  
Given a canonical deletion state H-x=P|Q together with either a robust order disagreement among selected deletion states or a mixed-support edge exposed by an endpoint deletion, construct a spanning ordering of defect span at most two.

No theorem currently proves this implication in full generality.

### 4.2 The balanced odd-cycle branch

Assume the selected supports form the spanning odd cycle C_{2k+1}. This branch is genuinely global and should not be folded into the tree argument.

It is already known, pending audit, that the cycle cannot be locally featureless. Theorem 1000943 says that some length-two transition has a two-deletion disturbance: deleting an internal exchanged label produces either an inherited three-piece crossing or relative-order disagreement in the endpoint-deleted covers. The strengthened transversal theorem 1000948 packages the same conclusion as a positioned three-piece double-deletion crossing.

If the overlapping cycle states are fully compatible, the compatible-pair normal form from 1000694 identifies every step-two transition with either a same-slot insertion or an adjacent-slot insertion on a common ordered spine. Every adjacent-slot transition carries a reversing tight triple.

Pending theorem 1000936 shows that at least k-1 of the step-two transitions are adjacent-slot reversals. The sharper pending theorem 1000945 says more: every adjacent rank generator occurs at least once, and either exactly k-1 reversals occur, one at each rank boundary, or at least k+1 reversals occur. Thus the cyclic branch already contains a global reversal network; proving the existence of one more reversal cannot close it.

There is an equivalent order-theoretic description. Pending theorem 1000944 says that the pair-order data on the complement of the ground cycle either come from one global linear order or possess a shortest incoherence witness of one of two forms: an odd-gap directed triangle or a directed C4 supported on two disjoint ground-cycle edges. This is a coordinate description of the same monodromy, not a separate proof route.

Finally, pending theorem 1000931 identifies the exact integral object needed for closure. The selected supports satisfy precise incidence identities and already admit the correct fractional mass-two certificate. If a tight-path support T is a vertex cover of the ground cycle with |T|=k+1, then T together with one selected support is a spanning two-cover of H. Hence the cyclic branch has the precise residual problem:

**Odd-cycle rounding target.**  
Use the step-two rank monodromy, or its odd-gap triangle/C4 form, to produce a Hamiltonian minimum vertex cover of C_{2k+1}, or directly a spanning ordering of defect span at most two.

A better fractional estimate cannot substitute for this step; the obstruction is integral.

## 5. The two branches meet at the same local interface

The forest branch and the disturbed odd-cycle branch both deliver the same kinds of data:

- a support-compatible but order-incompatible pair of deletion states;
- an endpoint deletion whose chosen cover contains a mixed-support edge relative to an anchor P|Q;
- or a double-deletion three-piece crossing/reversal carrying explicit deletion provenance.

These are exactly the forms needed by the defect-span and endpoint-transport lines. In proof language, we have reached the point at which the canonical width-three order P,x,Q is accompanied by an oriented defect that should permit one of its two independent defect edges to be removed.

The desired lemma would be something of the following form.

**Positioned disturbance compression lemma (open).**  
Let H be a minimum counterexample and let H-x=P|Q be an exact deletion cover. Suppose the selected deletion family supplies, relative to this state or to a double deletion derived from it, one of the positioned order/support disturbances above. Then H has a spanning ordering whose defect-line matching number is at most one; equivalently, H has a spanning two-path cover.

This is the first genuinely unsupported implication in the general deletion-cover route.

For the odd-cycle branch one may instead attempt the stronger global rounding target of Section 4.2. The local and global formulations are compatible: the cyclic monodromy may ultimately be useful only because it forces several positioned disturbances to synchronize at one canonical defect window.

## 6. Why the obvious local closures do not work

Several tempting continuations are already ruled out and should be regarded as mathematical obstructions, not historical curiosities.

A bare order disagreement is insufficient: certified theorem 1000211 already gives order disagreement in every minimum counterexample. What is missing is endpoint placement or synchronization with a canonical deletion join.

A single reversal is also insufficient. The certified counterexample double_inward_endhook_not_absorption01 shows that even both canonical inward endpoint hooks can coexist on a non-Hamiltonian four-set. Likewise astra003adjacentonedefect shows that adjacent double insertion gives, in the bad case, only a one-defect ordering with the reverse triple tight. These are local normal forms, not absorption theorems.

Hamiltonicity without order control is insufficient. Certified theorem 1000683 gives a Hamiltonian four-set for which the omitted vertex extends neither endpoint of a displayed Hamiltonian order on the other three vertices. Therefore every gluing argument must preserve the relevant Hamilton order, not merely the support.

Boundary antisymmetry may be used only on a single ordered triple. It does not license reversal or cyclic rotation of an entire tight path. Any proposed splice must verify each newly created consecutive triple.

Finally, the support-tree and odd-cycle fractional certificates do not themselves round. Pending 1000938 shows that even a forest can have fractional mass two while no pair of selected paths spans, and pending 1000931 shows that the odd-cycle branch has already reached the exact fractional optimum. The missing mechanism is creation or certification of the correct new integral support.

## 7. Exact stopping point

The proof is complete through the structural localization of deletion-cover inconsistency, subject to audit of the pending global classification and monodromy theorems.

In the ordinary branch the first unsupported implication is:

    positioned deletion-cover order/crossing disturbance
    => defect-line matching number at most one.

In the balanced odd-cycle branch one may equivalently stop at:

    cyclic rank/order monodromy
    => Hamiltonian minimum vertex cover of the ground cycle
       or defect-line matching number at most one.

Nothing beyond these arrows is presently justified in general.

## 8. Research handoff

The strongest viable next target is a **positioned disturbance compression theorem** that consumes an endpoint-tied mixed-support edge, a robust deletion-order disagreement, or a double-deletion three-piece crossing while retaining the canonical order P,x,Q. Such a theorem would simultaneously close the forest branch and provide a local consumer for the odd-cycle monodromy.

The principal route not to retry without a new ingredient is generic witness production. Order disagreement, reversals, mixed-support crossings, and even linear families of incompatible deletion states are already available. The unresolved mathematics is their synchronized placement and integral consumption.

For the odd cycle specifically, do not spend effort proving merely that the cycle is disturbed or that it has many reversals; those are already pending theorem-level results. The meaningful remaining target is integral rounding or conversion of the monodromy into the positioned compression lemma above.
