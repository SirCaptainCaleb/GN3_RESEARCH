# An exceptional leaf label gives disagreement, reversal, or neutral selected-lift recurrence

**Summary:** In a connected minimum-imbalance deletion-support tree, the unique non-mixing leaf exception either creates an order disagreement, forces an end reversal, or connects the two relevant selected singleton lifts by at most two neutral pairwise repartitions.

## Statement

Let H have path-cover number greater than two, let F_x=P|Q be a selected minimum-imbalance deletion cover with P a leaf of a connected selected support tree, and let y in Q be the exceptional label whose selected cover has no consecutive pair joining P to Q-{y}. Fix a Hamiltonian order on Q. Then at least one of the following holds: (i) the equally balanced support-compatible deletion cover at y has an order disagreement on Q-{y}; (ii) there is a tight triple reversing x and y across an endpoint-neighbor of Q; (iii) the selected singleton lifts F_x|{x} and F_y|{y} lie in the same pairwise-repartition component and are joined by a path of at most two neutral pairwise repartitions.

## Body

Let H have path-cover number greater than two. Choose, for every deleted label, a two-cover of minimum component imbalance, and suppose the selected support graph is a connected tree. Let
\[
F_x=P\mid Q
\]
be a selected deletion cover with P a leaf support, and let y\in Q be the unique possible exceptional label whose selected deletion cover F_y contains no consecutive pair joining P to Q-\{y\}. Fix a Hamiltonian order on Q.

By [[exceptional_leaf_label_is_end_local_or_order_disagreeing]], there is an equally balanced deletion cover
\[
G_y=P\mid W,\qquad W=(Q-\{y\})\cup\{x\},
\]
support-compatible with F_x on the common domain. Relative to the inherited order on Q-\{y\}, either G_y already has an order disagreement, or y lies in one of the two end positions of Q. In the second position from an end, the same theorem gives a tight triple reversing x and y across the intervening endpoint vertex.

It remains to consider the order-compatible case in which y occupies an extreme position of Q. Write the common ordered support as B=Q-\{y\}. The path of F_x on Q inserts y into an extreme slot of B. The path W in G_y inserts x into an extreme slot of the same ordered support. The insertion-slot argument used in [[exceptional_leaf_label_is_end_local_or_order_disagreeing]] shows that the slots are equal or adjacent. Since y is itself extreme, the adjacent case is precisely the already-listed second-position case. Hence in the remaining case x and y occupy the same extreme insertion slot.

Now compare the singleton lifts. Repartitioning the pair
\[
Q\mid\{x\}
\]
inside F_x|\{x\} as
\[
W\mid\{y\}
\]
gives G_y|\{y\} in one pairwise repartition. The affected component orders are unchanged, so this move is neutral for the quadratic potential.

By [[exceptional_leaf_transfer_equals_support_order_gap]], G_y and the selected exceptional cover F_y have the same component-order multiset. Therefore repartitioning the two non-singleton paths of G_y|\{y\} into the two non-singleton paths of F_y|\{y\} is a second neutral pairwise repartition. Thus
\[
F_x\mid\{x\}\longleftrightarrow G_y\mid\{y\}\longleftrightarrow F_y\mid\{y\}
\]
is a neutral path of length at most two.

Hence every exceptional leaf label produces an order disagreement, an explicit reversal, or neutral recurrence between the two selected singleton lifts. \(\square\)

## Metadata

- ID: exceptional_leaf_label_gives_disagreement_reversal_or_neutral_recurrence
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
