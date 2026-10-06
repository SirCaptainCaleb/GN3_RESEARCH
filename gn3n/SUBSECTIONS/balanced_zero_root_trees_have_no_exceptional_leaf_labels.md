# Balanced zero-root trees have no exceptional leaf labels

## Metadata

- ID: balanced_zero_root_trees_have_no_exceptional_leaf_labels
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 291
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

Let H be a minimum counterexample on n=2r+1 vertices, choose minimum-imbalance deletion covers, and suppose the selected support graph J is a connected tree containing the balanced zero-root edge. By [[the_zero_root_support_component_is_uniformly_balanced]], every support vertex of J has order r.

Fix a leaf support P with neighbor Q and edge label x. In the exceptional non-mixing case of the leaf comparison theorem, Corollary 10 of [[leaf_comparisons_in_deletion_support_forests_subsection_a]] gives a proper support S subset P and transferred block R=P-S with
|R|=|P|-|Q|.
But |P|=|Q|=r, so |R|=0, contradicting the defining nonemptiness of R in the exceptional case.

Hence no exceptional label exists at a leaf. Equivalently, for every y in Q, the selected deletion cover F_y contains a consecutive pair joining P to Q-{y}. In particular both endpoints of every Hamiltonian order on Q are available for the direct-mixing endpoint comparison.

Thus, in the connected-tree branch containing a zero root, all containment and exceptional-transfer alternatives disappear. Every leaf endpoint comparison must exit through genuine order/path disturbance, endpoint reversal, a spanning two-cover, quadratic descent in the three-cover reconfiguration graph, or a balanced neutral omission swap.
