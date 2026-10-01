# Singleton-swap adjacency lies between full and support compatibility

## Statement

Let H be a boundary tournament with pc(H)>2, let D be a set of deletion labels, and choose one two-cover F_v of H-v for each v in D. Let G be the full-compatibility graph on D, let B be the support-compatibility graph, and let M join distinct a,b when the singleton lifts F_a|{a} and F_b|{b} are adjacent by one pairwise repartition that changes the singleton label a to b. Then
E(G) subseteq E(M) subseteq E(B).
Moreover, for an edge ab of M, one component path is unchanged by the repartition; on the other common support, F_a and F_b are fully compatible exactly when their induced relative orders agree. Thus every edge of M is either a full-compatibility edge or a support-compatible/order-incompatible edge.

## Body

The inclusion E(G) subseteq E(M) is exactly 10e82bd852dc.

Now let ab be an edge of M. Write the singleton lifts as
C_a=F_a|{a},
C_b=F_b|{b}.
One legal pairwise repartition transforms C_a into C_b while changing the singleton label from a to b.

A pairwise repartition leaves one component unchanged. That unchanged component cannot be the singleton, since {a}!={b}. Hence it is one non-singleton component, say Q, appearing as the same ordered tight path in both F_a and F_b.

Let P_b be the other component of F_a and P_a the other component of F_b. The repartition replaces
P_b | {a}
by
P_a | {b}
on the same vertex union. Therefore
V(P_b) union {a}=V(P_a) union {b}.
Deleting a and b from this equality gives
V(P_b)-{b}=V(P_a)-{a}.
Together with the unchanged support V(Q), this shows that F_a and F_b induce the same unordered support partition on V(H)-{a,b}. Thus they are support-compatible, proving E(M) subseteq E(B).

On the unchanged component Q, the induced order is identical. Hence the only possible failure of full compatibility is on the other common support
V(P_b)-{b}=V(P_a)-{a}.
The two deletion covers are fully compatible exactly when the restrictions of P_b and P_a to that common support induce the same relative order. If those orders differ, the pair is support-compatible but order-incompatible. ∎
