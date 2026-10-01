# Every deletion-cover transversal in the sharp half-order shell exposes ordered or support disturbance

## Statement

Let H be a minimum counterexample in the sharp half-order shell n=2lambda+1. Choose arbitrarily one lambda|lambda cover F_v of H-v for every vertex v, form the selected support graph J, and choose arbitrarily one Hamilton order on every support vertex used by J. Then at least one of the following occurs:
(1) some length-two walk of J exposes inherited three-part crossing or relative-order disagreement as in astra004twowalk;
(2) three selected deletion covers induce nonidentical support partitions on their common three-deletion core;
(3) one deletion H-v has two lambda|lambda covers with distinct support partitions, and hence a same-deletion comparison with at least two ordinary path crossings.
Thus no full deletion-cover transversal in the sharp half-order shell can be simultaneously free of local order/crossing disturbance and globally support-coherent.

## Body

By ff3284e79394, J is either a forest or one odd cycle.

If J is cyclic, ff36134f3abb applies. Since the selected edge labels are pairwise distinct, its repeated-label alternative is impossible, so a length-two walk exposes inherited crossing or relative-order disagreement. This is (1).

Assume J is a forest. If any length-two walk is disturbed, again (1) holds. Hence suppose no length-two walk is disturbed.

By 9d79ac6c14d5, every component of J is then a path with at most five edges. Minimum-counterexample calculus gives n>10, so J, which has exactly n selected edges, has at least ceil(n/5)>=3 connected components.

Choose one selected edge label a,b,c from three distinct components. By 5e65e55c7ecd, the corresponding deletion covers F_a,F_b,F_c are pairwise support-incompatible.

Apply d1298d6dcec7. Either two of these covers induce different support partitions on W=V(H)-{a,b,c}, giving (2), or the common-core branch forces a same-deletion pair of lambda|lambda covers with different support partitions. The certified crossing-gap theorem d9ef8e3fe739 then gives at least two ordinary crossings, which is (3).

These alternatives exhaust both the cyclic and forest cases. ∎
