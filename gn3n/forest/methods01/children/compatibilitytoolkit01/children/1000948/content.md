# Every selected deletion-cover transversal forces a positioned transport disturbance

## Statement

Let H be a minimum counterexample and choose one exact two-cover F_v of H-v for every vertex v. Then at least one of the following holds: (A) two selected covers are support-compatible but order-incompatible; (B) for some anchor F_x=P|Q and an endpoint y of P or Q, F_y contains an ordinary edge joining surviving P- and Q-vertices; (C) the selected supports form the balanced spanning odd cycle, and for some consecutive double deletion H-{a,b}, an exact two-cover crosses two of the three nonempty inherited path pieces created by deleting an internal exchanged label. Thus an arbitrary selected deletion family always exposes a positioned input to endpoint transport/defect compression; the balanced odd cycle is not a featureless terminal branch.

## Body

Choose one exact deletion two-cover F_v of H-v for every v in V(H).

Apply 1000942. If its first alternative occurs, there is a selected pair of covers that is support-compatible but order-incompatible, giving outcome (A). If its second alternative occurs, there is an anchor F_x=P|Q and an endpoint y of P or Q such that the chosen cover F_y contains an ordinary edge joining surviving vertices of P and Q, giving outcome (B).

It remains to treat the third alternative of 1000942. Then n=2k+1 and the selected support graph is a spanning odd cycle whose supports all have order k. Write the support cycle as S_0,S_1,...,S_{n-1}, with edge S_iS_{i+1} the selected cover F_{x_i} of H-x_i.

If two consecutive selected covers are support-compatible but order-incompatible, outcome (A) already holds. Hence assume (A) is absent. Consecutive covers on the support cycle are support-compatible on their common double-deletion domain, so they are then fully compatible. In particular their common support orders agree, and one may choose one canonical Hamilton order on each support S_i that is used by both incident selected covers.

Now apply 1000943 to this balanced odd support cycle. For arbitrary exact two-covers T_i of H-{x_i,x_{i+1}}, some length-two transition S_i-S_{i+1}-S_{i+2} has a non-clean endpoint-trichotomy outcome. The relative-order-disagreement branch of 1000943 is impossible here, because the two consecutive selected covers are fully compatible and therefore their endpoint-deleted restrictions to H-{x_i,x_{i+1}} have the same ordered support data. Consequently the non-clean outcome is an inherited three-part crossing: one exchanged label is internal in its selected-cover component, and T_i contains an ordinary edge crossing two of the three nonempty inherited path pieces left after its deletion. This is outcome (C).

Thus every arbitrary selected deletion-cover transversal in a minimum counterexample exposes at least one of the three positioned disturbance types (A)–(C). The earlier fractional odd-cycle residue remains useful quantitatively, but it is no longer a branch in which the selected deletion family is structurally clean.