# Either synchronized endpoint structure occurs or compatibility degree is at most four

## Statement

Let H be a minimum counterexample, let D be a set of m deletion labels, choose one deletion cover F_d of H-d for each d in D, and form the compatibility graph G on D. Then either there is a label d and three compatibility neighbors on one path of F_d, in which case the conclusion of compatthreeoneside09 holds and one obtains synchronized opposite-path endpoint structure—at least three crossing edges, a direct mixed-support edge, or explicit relative-order disagreement—or Delta(G)<=4. Consequently, in the latter branch every chosen deletion cover is incompatible with at least m-5 of the other chosen covers.

## Body

# Proof

Fix d in D and write its chosen deletion cover as F_d=P|Q. Every compatibility neighbor of d is a vertex label of H-d and therefore lies on exactly one of P,Q.

If d_G(d)>=5, then among its at least five compatibility neighbors, at least three lie on the same one of the two paths P,Q. Apply compatthreeoneside09 to those three labels. Its conclusion is precisely the stated synchronized endpoint structure on the opposite anchor path.

Therefore, if no such synchronized endpoint conclusion occurs for any anchor d, every vertex of G has degree at most four. Hence Delta(G)<=4.

In that branch, each d has at most four compatible partners among the other m-1 labels, so it has at least

(m-1)-4 = m-5

incompatible partners.

Thus the compatibility route admits a sharp qualitative split: either five compatible neighbors at one deletion state already feed the certified endpoint-crossing/order-disagreement machinery, or compatibility is uniformly bounded and incompatibility is nearly complete at every label.