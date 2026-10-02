# Unique endpoint crossings synchronize onto one complementary component

## Statement

Let H be a boundary tournament with pc(H)>2, let A=(a_0,...,a_m) be a tight path with m>=3, and put U=V(H)-V(A). Suppose exact two-covers of H-a_0 and H-a_m each have exactly one ordinary edge across the surviving-A | U cut, and in each cover the surviving vertices of A form one block in the inherited order. Then the left endpoint cover has the form (R,A[1,m])|S and the right endpoint cover has the form (A[0,m-1],T)|T', where R|S and T|T' are exact two-covers of U. If these two U-covers have different support partitions or different orders on a common support, they expose the usual crossing/order-disagreement witness. Otherwise their attached blocks must be the same component of the common ordered U-cover: attaching opposite components would directly give a spanning two-cover of H. In the remaining identical same-component case, writing M=A[1,m-1], both RM and MR are tight, so the synchronized component and M form the certified cycle-or-wrap obstruction.

## Body

# Unique endpoint crossings synchronize onto one complementary component

Let H be a boundary tournament with pc(H)>2. Let
A=(a_0,a_1,...,a_m),  m>=3,
be a tight path and put U=V(H)-V(A).

Choose exact two-covers G_0 of H-a_0 and G_m of H-a_m. Assume:

- each cover has exactly one ordinary edge between the surviving vertices of A and U; and
- in each cover the surviving A-vertices occur as one path block in the inherited order.

Then the unique-crossing block count gives two nonempty U-blocks in each cover. The restoration obstruction fixes the crossing orientation. Thus, after naming the U-blocks,

G_0=(R,a_1,...,a_m)|S
and
G_m=(a_0,...,a_{m-1},T)|T',

where R|S and T|T' are exact two-path covers of H[U].

Indeed, if the mixed component of G_0 had the form
(a_1,...,a_m,R),
then prepending a_0 would preserve tightness and, together with S, would two-cover H. Hence the U-block must precede the inherited A-block. The argument at a_m is symmetric: the U-block in G_m must follow the inherited A-block.

Compare the two exact U-covers R|S and T|T'. If their unordered support partitions differ, the exact-cover disagreement theorem gives reciprocal support-crossing edges inside U. If the support partitions agree but the corresponding Hamilton orders differ, it gives the usual order-disagreement witness on a common support.

It remains to consider the case in which the two U-covers agree as ordered covers up to component names. Suppose first that the block attached on the left and the block attached on the right are different components. Rename so that R is attached on the left and T is the other component, attached on the right. Put
M=(a_1,...,a_{m-1}).
Since m>=3, M has at least two vertices.

The sequence
(R,M,T)
is tight. Every triple at its left junction occurs in
(R,a_1,...,a_m),
every triple at its right junction occurs in
(a_0,...,a_{m-1},T),
and every remaining triple lies inside R, M, or T. The two paths R and T partition U, so
(R,M,T) | (a_0,a_m)
is a spanning two-path cover of H. This contradicts pc(H)>2.

Therefore, in the no-disagreement branch, the same component R of the common ordered U-cover attaches at both ends:
(R,a_1,...,a_m)
and
(a_0,...,a_{m-1},R)
are tight. Hence both
(R,M)
and
(M,R)
are tight. By the opposite-concatenation theorem, if R has at least two vertices the cyclic ordering RM is a tight cycle; if R is a singleton, either that cyclic ordering is tight or the corresponding wrap triple through the two ends of M is tight.

Thus two clean unique endpoint crossings cannot wander independently through the complementary two-cover. Either they already create support/order disagreement inside U, or they synchronize on one complementary component and enter the explicit cycle-or-wrap obstruction. ∎