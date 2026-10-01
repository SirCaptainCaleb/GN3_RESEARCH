# In the low-degree branch every deletion state has linearly many uniform disagreements

## Statement

Under the hypotheses of compatdegreefour10, suppose the synchronized endpoint-structure branch does not occur. Then for every deletion label d, the chosen cover F_d has at least m-5 incompatible partners. For each fixed d, at least ceil((m-5)/2) of those partners may be chosen uniformly so that either all are support-incompatible with F_d, each giving a bounded mixed-support transition relative to F_d, or all are support-compatible but order-incompatible with F_d, each giving a reversed common edge, a reversing tight triple, or a vertex-simple tight cycle.

## Body

# Proof

By compatdegreefour10, absence of the synchronized endpoint-structure branch implies Delta(G)<=4 for the compatibility graph G on the m deletion labels.

Fix arbitrary d. Then d has at most four compatible partners among the other m-1 labels, and hence at least m-5 incompatible partners.

Partition these incompatible partners exactly as in the certified uniform-disturbance theorem compatuniformdisturb:

1. support-incompatible with F_d;
2. support-compatible but order-incompatible with F_d.

One class has size at least ceil((m-5)/2).

For a support-incompatible partner e, the support-comparison argument of compatuniformdisturb supplies a bounded mixed-support transition relative to F_d: either an ordinary path edge directly joining the two F_d support classes, or a two-edge passage through the opposite omitted label whose two neighboring vertices lie in different F_d support classes.

For a support-compatible but order-incompatible partner, path-intersection calculus gives a reversed common edge, a reversing tight triple, or a vertex-simple tight cycle.

Because d was arbitrary, this conclusion holds at every deletion state simultaneously. Thus failure of the high-compatibility endpoint branch forces a project-wide dense disagreement regime rather than merely one exceptional incompatible state.