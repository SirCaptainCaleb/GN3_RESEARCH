# Anchor-neighborhood compatibility paths have bounded positional speed

## Statement

Let F_d=P|Q be an anchor deletion cover with P=(p_1,...,p_m). Consider the compatibility graph induced by deletion covers F_{p_i} that are compatible with F_d. If F_{p_{i_0}},F_{p_{i_1}},...,F_{p_{i_r}} is a path in this induced compatibility graph, then |i_r-i_0|<=3r. Consequently transporting full compatibility by L positions along one anchor path requires at least ceil(L/3) compatibility edges.

## Body

Every edge F_{p_i}F_{p_j} of the induced compatibility graph joins two covers that are each compatible with F_d and compatible with one another. The positional localization theorem 42f1d61694cb therefore gives |i-j|<=3 for each edge. Summing the successive index differences along a compatibility path and applying the triangle inequality gives |i_r-i_0|<=3r. This turns the order-disagreement interval theorem into a coarse metric obstruction: compatibility cannot jump arbitrarily far along the anchor order in one step.
