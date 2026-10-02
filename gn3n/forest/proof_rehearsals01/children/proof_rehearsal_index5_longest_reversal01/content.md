# Proof rehearsal V — longest-path and reversal structure

## Statement

Near-publication rehearsal of the longest-path/reversal route. Certified theory gives two entrances: every minimum counterexample has a genuine reversing tight triple, and every globally longest path has a pc2 exterior with simultaneous reversed endpoint triples. Reversal amplification and longest-path endpoint coupling both produce synchronized common-core Hamiltonian 4/5/6-supports, endpoint deletion disagreement, or a universal endpoint-reversal grid. The first unsupported implication is to consume one of these positioned structures into endpoint absorption, a spanning two-cover, or defect span at most two. The former sharp-shell repeated-cut closure is audit-failed and is retained only as an exact obstruction.

## Body


# Longest-path and reversal structure

## 1. The proposed proof

Assume H is a minimum counterexample to the grand two-cover conjecture.

This route has two certified entrances.

The first is intrinsic. Every minimum counterexample contains relative-order disagreement between overlapping tight paths (1000211). The certified path-intersection calculus localizes such disagreement, and theorem 1000164 concludes:

**Reversal theorem.**  
Every minimum counterexample contains a tight triple reversing an edge of a nontrivial tight path.

The second entrance is global. Choose a tight path

    A=(a_0,...,a_{\lambda-1})

of maximum possible order, and put U=V(H)-V(A). Certified theorem 1000925 gives:

- H[U] is non-Hamiltonian and has path-cover number two;
- for every y in U, both
      (a_1,a_0,y)
  and
      (y,a_{\lambda-1},a_{\lambda-2})
  are tight;
- complements of proper contiguous subpaths of A are also non-Hamiltonian with pc2;
- the two endpoint reversals cannot simply be spliced into one reverse-to-reverse Hamilton path.

Thus a longest path begins with a **bi-anchored pc2 obstruction**.

The route attempts to amplify these reversals until one becomes globally consumable. The existing theory succeeds at amplification and positioning; it does not yet prove the final absorption.

All results below are certified unless explicitly stated otherwise.

## 2. From disagreement to a genuine reversal

The first entrance is short.

Order disagreement between two overlapping tight paths cannot remain purely global. The path-intersection calculus produces a reversed common edge, a reversing tight triple, or a tight cycle. Certified theorem 1000164 also consumes the cycle alternative, using the pc2 complement forced in a minimum counterexample, and again obtains a reversing tight triple.

Consequently no proof effort is needed merely to establish that reversals exist. The mathematical question is where a reversal can be placed and what additional support structure accompanies it.

## 3. Local reversal normalization

Certified endpoint_reversal_obstruction_recomp01 analyzes a genuine displayed-edge reversal.

If the reversal is internal, or has the easier endpoint orientation, it enters a bounded four-vertex frontier: a Hamiltonian K4, the exceptional cyclic non-Hamiltonian K4, or a matching-block K4 with its forced reverse-fan structure.

Otherwise one obtains a maximal unresolved endpoint pair. The hard residue is highly synchronized: every other exterior label satisfies the corresponding reverse relations at both ends, and—unless a small Hamiltonian support appears immediately—also a middle reverse relation.

Certified theorem 1000540 turns this universal family into a complete endpoint-pair grid. Every endpoint-pair four-set is Hamiltonian, one- and two-label exterior deletions retain pc2 structure, and every exterior triple already carries order disagreement.

Thus the difficult endpoint reversal is not a single stubborn local triple. It is a dense, positioned family with pc2 deletion data.

This is one of the two richest certified states from which to attack the final absorption problem.

## 4. Reversal amplification by common-core stars

There is a second certified amplification that starts from any genuine reversing triple.

Let T be the three vertices of the reversal. Form the graph J_T on the remaining vertices, joining y and z when T union {y,z} is Hamiltonian. Certified reversal_dense_fivefamily01 gives

    alpha(J_T) <= 2,

and hence a Mantel-scale lower bound on the number of edges. In particular some exterior vertex y has many neighbors, so at least three Hamiltonian five-supports share one common four-core

    C = V(T) union {y}.

Certified reversal_threeleaf_star01 extracts such a three-leaf star. Synchronizing Hamilton orders on the three five-supports, certified reversal_star_sync01 / reversal_seven_shell_sync01 gives one of:

1. order disagreement on the common four-core;
2. a Hamiltonian six-support with pc2 complement;
3. a Hamiltonian four-support with pc2 complement;
4. a second explicit reversal using two leaves and a core vertex.

Therefore a single reversal expands into a bounded, correlated support shell. The complement information remains part of the state and is essential for any eventual gluing theorem.

## 5. Longest-path endpoint coupling reaches the same frontier

The longest-path entrance produces essentially the same bounded objects, but with stronger endpoint placement.

From 1000925, every exterior label gives reverse hooks at both ends of A. Certified 1000819 then yields either:

- a bi-endpoint Hamiltonian five-path; or
- a four-vertex internal-reversal configuration.

Certified 1000755 strengthens the first branch: unless the reversal K4 already appears, all but at most two exterior labels extend one fixed endpoint four-core to a Hamiltonian five-set.

When the exterior is sufficiently large, certified longest_three_root_star01 gives either:

- a proper Hamiltonian six-support; or
- three Hamiltonian five-supports sharing one common four-core.

Thus the longest-path branch reaches the same common-core star and bounded pc2 shell as the intrinsic reversal branch, but with a remembered maximum-path order and opposite-end provenance.

Two additional certified theorems are useful at this interface.

Theorem 1000494 says that arbitrary two-covers of the two endpoint deletions of a longest path cannot remain mutually support- and order-neutral: they expose support or order disagreement.

Theorem 1000536 gives a positive gluing result: if opposite endpoint replacements preserve the order of a longest path of order at least six, they splice to a Hamiltonian double replacement. Hence the unresolved longest-path branch is precisely the **disturbed, non-order-preserving** endpoint-replacement case.

## 6. Convergence to the endpoint-transport interface

Both entrances now give one of the following positioned structures:

- the universal endpoint-reversal grid of 1000540;
- a common-four-core star of Hamiltonian five-supports with pc2 complements;
- a Hamiltonian four- or six-support with pc2 complement;
- endpoint deletion disagreement tied to a longest path;
- or a second explicit reversal with common-core provenance.

The desired theorem is therefore not another reversal lemma.

**Positioned reversal consumption lemma (open).**  
In a minimum counterexample, any of the positioned reversal/common-core states above forces one of:

1. a displayed component-end reversal that is consumable by the endpoint-transport theorem;
2. a spanning two-path cover;
3. a spanning ordering of defect span at most two.

This is the bridge represented by proposal 1000741.

Equivalently, one may ask for a theorem that takes a bounded Hamiltonian support carrying a positioned order defect together with its pc2 complement and produces boundary absorption. Such a theorem would simultaneously consume the endpoint grid and the common-core star.

## 7. The bi-anchored longest-path target

The longest-path entrance carries one additional global feature that is worth preserving.

The state from 1000925 has simultaneous reverse hooks at both ends of one globally longest path, while the exterior is pc2. Combined with 1000494, opposite endpoint deletion covers always contain support/order disturbance.

The order-preserving subcase is already solved by 1000536. Thus a particularly clean route-specific target is:

**Bi-endpoint absorption lemma (open).**  
Let A be a globally longest path in a minimum counterexample, with the bi-anchored pc2 exterior supplied by 1000925. Then the disturbed opposite-end replacement states force a direct two-cover, an absorbable component-end reversal, or defect span at most two.

This target is stronger in placement than the generic reversal-consumption lemma and may therefore be easier.

## 8. The optional sharp half-order branch

There is a distinct equality-shell formulation when

    n = 2\lambda + 1.

Certified theorem 1000613 identifies the D=1 support-reconfiguration graph exactly with the disjointness graph on Hamiltonian \lambda-subsets, with omitted vertices as edge labels. Certified astra004globalfork then says that the longest-path complement is either rich in Hamiltonian deletions, forcing intrinsic order disturbance, or deletion-sparse, in which every bad deletion cover has substantial crossing.

This support-graph branch retains genuine global parity and exchange information. It is not, however, a completed route to closure.

The historical repeated-neutral-cut theorem astra004repeatcutdisturb failed audit. Its proof treated (u,v,z) and (v,u,z) as the boundary-flip pair; the actual reverse of (u,v,z) is (z,v,u). The argument therefore used an invalid cyclic reinterpretation of ordered triples. Downstream claims 1000578 and 1000545 are blocked for the same reason.

A second theorem, astra004sparsebridge, also failed audit in its stated form: it bounded the size of an exceptional block in a deletion-cover path but did not prove that the vertices form an interval in the displayed longest-path order.

Hence the sharp-shell route may be revived only by repairing the exact orientation-valid repeated-cut residue. It must not be used as a black-box closure theorem.

## 9. Mathematical obstructions that delimit the route

Two inward endpoint hooks do not imply absorption. The certified counterexample double_inward_endhook_not_absorption01 has both hooks but is non-Hamiltonian.

Balanced repartition need not preserve an old terminal pair. Certified fixed_terminal_pair_balancing_counterexample01 gives a uniform counterexample family. Any gluing theorem must permit the attachment data to change or use an additional hypothesis.

Boundary antisymmetry does not permit cyclic rotation of an ordered tight triple or reversal of a whole tight path. This is the exact error that invalidated the sharp-shell repeated-cut argument.

Finally, repeated endpoint replacement or support exchange does not terminate by finiteness alone. A neutral sequence may cycle. Any iterative proof needs a monotone invariant, a no-trapping theorem, or a contradiction from a return state with preserved oriented data.

## 10. Exact stopping point

The certified proof gives:

    minimum counterexample
    -> genuine reversal or bi-anchored longest-path obstruction
    -> synchronized endpoint grid or common-core bounded shell.

The first unsupported implication is

    positioned reversal/common-core shell
    => displayed boundary absorption, two-cover,
       or defect span at most two.

For the longest-path-specific branch it may be sharpened to

    disturbed bi-endpoint replacement state
    => absorbable endpoint reversal or two-cover.

The sharp-shell neutral-cut branch remains open at its failed repeated-cut step and is optional.

## 11. Research handoff

The strongest certified launch states are the hard endpoint grid of 1000540, the three-leaf reversal star, and the bi-anchored longest-path state 1000925 together with 1000494. Each contains repeated synchronized structure and pc2 complement information.

The principal route not to retry without a new ingredient is witness existence. Reversals, order disagreement, small Hamiltonian supports, and common-core stars are already abundant.

The unresolved mathematics is endpoint accessibility:

    local oriented inconsistency
    -> synchronized bounded structure
    -> one disturbance reaches the displayed boundary
    -> global defect collapses.

The first two arrows are established. The third is the frontier.
