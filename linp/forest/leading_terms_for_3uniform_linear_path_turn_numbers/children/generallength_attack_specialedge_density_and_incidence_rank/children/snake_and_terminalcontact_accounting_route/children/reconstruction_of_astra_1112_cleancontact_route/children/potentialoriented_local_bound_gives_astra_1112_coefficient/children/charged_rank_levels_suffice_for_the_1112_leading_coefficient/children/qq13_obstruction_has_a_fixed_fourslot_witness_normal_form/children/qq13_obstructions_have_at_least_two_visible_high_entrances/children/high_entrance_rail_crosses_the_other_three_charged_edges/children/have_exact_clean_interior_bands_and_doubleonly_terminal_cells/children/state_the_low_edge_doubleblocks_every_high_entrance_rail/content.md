# In the 4555 rank-pair state the low edge double-blocks every high entrance rail

## Statement

In a charged rank pattern (4,5,5,5) at a common terminal v, let e={x,v,u} be the rank-four edge and let h_i be any rank-five high edge. For any canonical four-edge entrance rail Q_i for h_i, both x and u lie on Q_i. Equivalently, the low edge e is a double blocker on every high entrance rail.

## Body

Apply 3e837f0c5fe6 with q=4. A one-contact low blocker would have to lie in the band
  r_3,...,r_{q-2}=r_3,...,r_2,
which is empty.

But 21dfd53c201f/e43d175aa905 guarantee that the low edge e does meet every high entrance rail Q_i. Therefore e cannot have exactly one contact on Q_i.

Since Q_i avoids the common terminal v and e has only the two remaining vertices x,u, the only alternative is that both x and u lie on Q_i.