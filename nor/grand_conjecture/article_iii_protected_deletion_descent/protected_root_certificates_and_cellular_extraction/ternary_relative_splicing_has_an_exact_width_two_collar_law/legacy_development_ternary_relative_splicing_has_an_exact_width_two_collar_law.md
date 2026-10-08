# Ternary relative splicing has an exact width-two collar law — preserved pre-item development

## Development


## Ternary relative splicing has an exact width-two collar law

Let an ambient coordinate order be written as
P M Q,
where M=(m_1,...,m_s) is a contiguous block and ternary window colors are alpha(u,v,w). Replace M by another ordering M'=(m'_1,...,m'_s) of the same coordinates, leaving P,Q fixed.

Only windows meeting the two block boundaries can change outside the interior of M.

Assume both exterior sides contain at least two coordinates. Write the last two coordinates of P as p_1,p_2 and the first two of Q as q_1,q_2.

The left boundary windows are exactly
alpha(p_1,p_2,m_1), alpha(p_2,m_1,m_2).
The right boundary windows are exactly
alpha(m_{s-1},m_s,q_1), alpha(m_s,q_1,q_2).

Hence:

1. If M' has the same first two coordinates and the same last two coordinates as M, every boundary and exterior ternary window is unchanged.

2. If M' has the same first coordinate and the same ordered last pair as M, every boundary and exterior window is unchanged except possibly alpha(p_2,m_1,m_2). Thus the entire external reconnection risk is one bit.

3. Symmetrically, if M' has the same ordered first pair and the same last coordinate as M, every boundary and exterior window is unchanged except possibly alpha(m_{s-1},m_s,q_1).

The endpoint cases with fewer than two exterior coordinates are obtained by deleting the absent windows.

### Proof

Every ternary window wholly outside M is identical before and after replacement. A ternary window can cross a boundary of a contiguous block only if its starting position is one or two slots before that boundary. This gives exactly the four displayed boundary windows. Their dependence on the first two and last two coordinates of M proves the assertions.

### Relative-splice consequence

For Article III, a block merge
P g(A) g(B) Q -> P g(A union B) Q
is boundary-safe once the replacement realizes the same two-coordinate collars on both sides. More importantly, a three-coordinate collar condition—first coordinate plus ordered last pair, or its reverse—reduces the entire compatibility problem to one exported crossing bit.

This is exactly the structural form achieved by the rigid width-two weave of §226: preserving the first coordinate and ordered final pair leaves a unique external bit. The subsequent double-full argument identifies the bad value of that bit with the already-controlled singleton gadget.

Thus the primary relative block-splice theorem can be sharpened. It is enough to construct, for each unresolved merge, a good or locally repairable ordering of the merged block that matches a three-coordinate collar. A four-coordinate collar gives immediate legal replacement; a three-coordinate collar gives a one-bit interface to the existing exported-reconnection machinery.

This isolates the genuinely new content of relative splicing: endpoint/collar attainment inside the merged proper block. Internal window bookkeeping and the number of external defects require no further classification.
