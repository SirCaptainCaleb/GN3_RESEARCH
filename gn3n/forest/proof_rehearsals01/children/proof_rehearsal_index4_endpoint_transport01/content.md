# Proof rehearsal IV — endpoint transport and bounded-window gluing

## Statement

Near-publication rehearsal of the endpoint-transport route. Starting from a reachable Hamiltonian 4/5-window, endpoint-tied crossing, or displayed reversal, certified transport moves the obstruction to a literal component-end reversal; that reversal gives a spanning two-cover, strict same-component Phi-descent, or one neutral singleton transfer. Opposite endpoint phases endpointize the transfer, leaving only coherent same-end or universal-internal locks. Pending Hall and square-normalization theorems compress those locks to classified common-core pc2 shells, a doubled reverse barrier, or a phase-locked same-deletion transfer. The first unsupported implication is global consumption of that positioned bounded shell into a legal splice, terminating descent, or defect span at most two.

## Body


# Endpoint transport and bounded-window gluing

## 1. The proposed proof

Let H be a minimum counterexample. Every one-vertex deletion has an exact two-path cover, and a spanning two-cover is equivalent to a spanning ordering of defect span at most two. This route begins after another argument has produced a **positioned disturbance** beside such a canonical deletion state.

The useful starting configurations retain enough provenance to interact with a displayed two-cover:

- a Hamiltonian four-set W with exact two-path complement P|Q, preferably reachable in the same repartition component as a deletion state;
- an endpoint-aligned Hamiltonian four- or five-support with pc2 complement;
- a deletion-tied mixed-support crossing;
- a reversal of an edge of a displayed path;
- or two nearby Hamiltonian windows sharing a large core.

The aim is to transport the disturbance to a displayed boundary. Once a reversal lies literally on a component-end edge, certified calculus nearly closes the proof. The only surviving local case is a neutral one-vertex transfer. Endpointizing that transfer leaves two phase-locked residues: coherent same-end realization or universal internality. The remaining theorem must break that phase lock globally.

All results below are certified unless explicitly marked **pending**.

## 2. Four-window transport

Suppose

    X | P | Q

is a spanning three-cover, |X|=4, X is Hamiltonian, and P|Q is an exact two-cover of H-X.

The certified theorem 1000911 says, for n>14, that one of the following occurs:

1. strict quadratic-potential descent;
2. another Hamiltonian four-window at distance one, again with pc2 complement;
3. an endpoint-aligned Hamiltonian support of order four or five with pc2 complement.

Thus a four-window cannot remain an isolated witness. It either descends or migrates through a controlled family until a bounded support is aligned with a displayed endpoint.

Shared-endpoint refinements produce two Hamiltonian five-sets with a common core, and certified theorem 1000476 then yields a Hamiltonian six-set or a four-good-deletion transport package. These refinements matter only when their common-core information is retained. Their common purpose is to produce a correlated bounded pc2 shell.

The branch n<=14 left by 1000911 remains a separate finite-order obligation.

## 3. Endpoint Hamiltonicity forces transport or permanent internality

Let

    X | C | D

be a spanning three-cover, with C=(c_0,...,c_m), X Hamiltonian, and X+c_0 Hamiltonian.

The certified theorem endpoint_hamiltonicity_crossing_plus_transport01 has two parts.

First, every exact two-cover of H-c_0 crosses the coarse cut

    X | ((C-c_0) union D).

Thus endpoint Hamiltonicity carries support-mixing information.

Second, if X+c_0 has a Hamilton order placing c_0 at the endpoint compatible with C, append c_1,c_2,... greedily. At the first failed append, the current Hamiltonian support ends in a displayed edge whose reverse occurs in a tight triple forced by boundary antisymmetry. Hence

    endpoint realization
    => maximal greedy absorption
    => literal component-end reversal.

Pending theorem 1000848 strengthens the bookkeeping by carrying the deletion-crossing certificate through every successful transport step.

There is one genuine alternative: c_0 may be internal in every Hamilton order of X+c_0. Then endpoint transport cannot start. The certified theorem routes this **universal-internal** case to fine crossing structure rather than pretending it has been absorbed.

## 4. A literal component-end reversal is almost closure

The certified theorem 1000559 is the central consumer.

Let

    H-x = P | Q

be an exact deletion cover, and suppose an alternative Hamilton order on P contains the reverse of a displayed terminal edge. Write it as

    A, p_m, p_{m-1}, B

and put t=|A|. Boundary antisymmetry supplies the hook needed to place x before the suffix beginning at p_m. The induced repartition has three cases.

If t=0, it gives a spanning two-cover directly.

If t=1, it is Phi-neutral and merely transfers one vertex between the two Hamiltonian supports.

If 2<=t<=N-2, the quadratic potential drops by

    2(t-1)(N-t) > 0.

At a componentwise Phi-minimum this is impossible. The initial-edge case is symmetric.

Therefore a literal displayed-end reversal has exactly one nonclosing residue:

    a neutral singleton transfer.

## 5. Endpointizing the neutral singleton transfer

Suppose two three-covers differ only by moving one label x between two Hamiltonian supports. Certified singleton_transfer_endpointization01 compares the Hamiltonian realizations of x on the two augmented supports.

If x is realizable at opposite ends in the two supports, greedy transport gives a displayed component-end reversal, returning to Section 4.

Hence, if no two-cover or displayed reversal occurs, exactly one of the following remains:

1. **universal internality:** on at least one augmented support, x is internal in every Hamilton order;
2. **coherent same-end realization:** whenever x is an endpoint, it always appears on the same side in both augmented supports.

This is the first point where the certified local endpoint calculus stops.

## 6. Why coherent same-end behavior is exceptional

The certified compatible-extension theorem 1000696 gives the exact insertion-gap analysis.

Let K+x and K+y be Hamiltonian and suppose their Hamilton orders induce the same order on K.

- Separated insertion gaps glue to a Hamiltonian K+x+y.
- Adjacent gaps glue or force a reverse cross triple.
- The same internal gap produces a Hamiltonian four-set.
- The only compatible geometry not already consumed is a common endpoint gap.

Thus same-end extension is the unique compatible insertion residue.

The certified theorem three_fourcore_extensions_sync01 then says that three Hamiltonian one-label extensions of one four-core force order disagreement on the core, a Hamiltonian six-set, a Hamiltonian four-set, or an explicit root-core reversal. Even several same-core extensions therefore return to the bounded-window/reversal interface.

## 7. Common-core abundance and square normalization

The route already has abundant bounded families.

Certified 1000863 shows that Hamiltonian four-window structure yields large common-top families and dense pc2 deletion squares unless endpoint exposure, support disagreement, or order disagreement occurs first.

Certified fixed_pair_star_transport_clique01 and pair_centered_central_gap_fan01 show that every prescribed pair belongs to a linear common-four-core family of Hamiltonian five-supports. After fixing one path type, a large coherent subfamily has one of three forms:

- every leaf pair gives a Hamiltonian six-support;
- all leaves insert in one central gap of a fixed four-core;
- all leaves extend the same end of a fixed four-core.

Pending central_gap_large_escape18 eliminates the central-gap branch above order seventeen by producing disagreement or strict descent.

Two pending normalization theorems make the residual bounded state explicit.

**Pending fourset_boolean_pc2_01.**  
For any four-set X, all nontrivial lower extension states in its Boolean cube have path-cover number two whenever the complementary subset of X is Hamiltonian.

**Pending recomp_fourwindow_square_01.**  
A Hamiltonian four-window with pc2 complement reaches one of:

- strict Phi-descent;
- support or order disagreement;
- a full pc2 square with a label internal in every top cover;
- a coherent endpoint square.

At a componentwise Phi-minimum the coherent endpoint-square branch has profile {4,5,n-9} unless disagreement occurs.

Thus universal internality already has a concrete square normal form; it is not merely an informal failure of endpoint realization.

## 8. Pending Hall completion of the coherent same-end branch

The strongest current same-end continuation is pending audit.

Universal same-end extenders force synchronized endpoint reversals through the chain

    same_end_extenders_initial_reversal01
    -> same_end_extenders_double_reversal01
    -> same_end_extenders_four_endpoint_reversal01.

Fix a residual exact two-cover R|S and form the 2-by-2 attachment graph between two extenders {x,y} and {R,S}. A perfect matching restores x and y to different paths and gives a spanning two-cover. Hence Hall failure leaves only two forms (pending same_end_extenders_hall_completion01):

- one residual path is unattached by both extenders, so x and y reverse one common endpoint edge;
- one extender is blocked from both residual paths while the other attaches to both, yielding two covers of the same deletion differing by one singleton transfer.

In the first case, pending shared_edge_double_reversal_sixpackage01 uses the triangle-free bad-extension graphs and R(3,3)=6 to force two Hamiltonian five-sets sharing a four-core.

Pending commoncore_fivepair_sixshell_normal01 classifies their six-vertex union into exactly:

1. a Hamiltonian six-set, hence a full pc2 square;
2. overlapping Hamiltonian four/five-windows;
3. the canonical oriented matching-block shell.

In the same-deletion transfer case, opposite endpoint phases are consumed by the certified endpointization theorem. If the transfer remains coherently same-end, pending blocked_extender_coherent_sameend_escape01 gives a positioned Hamiltonian five-window, a doubled reverse barrier, or again the common-core six-shell.

Thus, subject to audit, the coherent same-end branch is already reduced to a finite Hall/common-core endgame.

## 9. The universal-internal branch

Suppose instead that the relevant label remains internal in every Hamilton order of an augmented support.

The pending square package gives lower deletion states automatically. Pending universal_internal_pair_doublecross01 then says that two universally internal labels force at least two cross-fragment edges unless they are adjacent; in the adjacent sparse case every lower cover must bypass the deleted block directly while leaving the opposite top component fixed.

The pending theorems adjacent_internal_square_bypass_ladder01 and adjacent_internal_square_sync01 synchronize the three singleton/double-deletion states. If all sparse bypasses occur, they either yield order disagreement or form a coherent internal-deletion square preserving the inherited top order and the opposite component.

Thus universal internality is also reduced to an explicit bounded shell. What is not known is how to turn that shell into endpoint realization, a legal splice, or strict same-component descent.

## 10. The first unsupported implication

After the certified transport and the pending normalizations, every difficult branch reaches a **positioned bounded pc2 shell** of one of the following kinds:

- a coherent endpoint square;
- a coherent internal-deletion square;
- a common-core six-shell;
- overlapping Hamiltonian four/five-windows;
- an oriented matching-block shell;
- a doubled reverse barrier;
- or a phase-locked same-deletion singleton transfer.

The desired theorem is therefore:

**Bounded-shell consumption lemma (open).**  
Let H be a minimum counterexample and let a reachable bounded shell of one of the types above arise from a canonical deletion state. Then H has a spanning two-cover, or the same repartition component contains a strict Phi-descent, or the shell admits a legal move into a certified terminating corridor that yields defect span at most two.

No such theorem is presently known in full generality.

A companion entry theorem is also needed for the most generic disturbances exported by other routes:

**Generic disturbance entry lemma (open).**  
A positioned order disagreement, mixed-support crossing, or bounded local defect from a deletion state enters the displayed-end reversal calculus, one of the bounded shells above, or the certified deficit-one longest-path corridor.

This is the content sought by proposal 1000771.

## 11. Why the obvious shortcuts fail

Same-end extenders do not concatenate automatically. Certified 1000149 gives a four-vertex counterexample, and certified 1000364 gives arbitrarily large families of common same-end extenders with no pairwise concatenation. Extra cross-triple, common-core, or deletion structure is indispensable.

Two inward hooks do not force absorption. Certified double_inward_endhook_not_absorption01 gives a non-Hamiltonian four-set with both hooks.

Hamiltonicity does not imply endpoint realization. That is exactly why the transport theorem has a permanent-internal branch.

Boundary antisymmetry reverses one ordered triple only. The retracted same-slot endpoint-replacement arguments 1000244 and 1000470 failed by implicitly rotating or reversing more order than the axiom permits.

An unpositioned Hamiltonian five-set is also not closure. Pending unpositioned_fiveside_vacuous01 formalizes that in the bounded-square setting: such five-sets are automatic. Position, common-core data, deletion provenance, or endpoint alignment is the useful information.

Finally, neutral migration does not terminate merely because the state space is finite. A proof needs a monotone invariant, a no-trapping theorem, or a contradiction from recurrence.

## 12. Exact stopping point

The certified proof reaches:

    positioned small support
    -> endpoint transport
    -> displayed component-end reversal
    -> two-cover / strict descent / neutral singleton transfer
    -> coherent same-end or universal-internal phase lock.

Pending mathematics further reaches:

    phase lock
    -> classified bounded pc2 shell / doubled barrier / same-deletion transfer.

The first unsupported arrow is

    Hall/square-normalized positioned shell
    => legal global splice, same-component strict descent,
       certified terminating corridor, or defect span at most two.

The n<=14 residue of the four-window theorem remains separate.

## 13. Research handoff

The strongest next target is a bounded-shell gluing theorem. The most informative test cases are the common-core six-shell, coherent internal-deletion square, and doubled reverse barrier, because they preserve complement and deletion provenance rather than merely asserting that some small Hamiltonian set exists.

The principal routes not to retry without a new ingredient are generic reversal existence, generic K4/K5/K6 production, same-end concatenation from extension alone, and neutral migration without a well-founded measure.

Endpoint transport has already done its local job. The frontier is global:

    place the disturbance at the boundary
    -> preserve its provenance
    -> make the local move irreversibly reduce the global defect.
