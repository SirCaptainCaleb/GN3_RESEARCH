# Three same-path anchor neighbors force a synchronized opposite-path endpoint obstruction

## Statement

Let H be a minimum counterexample, let F_d=P|Q be a deletion cover of H-d, and suppose d has three compatibility neighbors t_1,t_2,t_3 whose labels all lie on P. Then, with X=V(P) union {d}, the three deletion covers F_{t_i} form a pairwise support-compatible family with support partitions (X-{t_i}) | V(Q), H[X] non-Hamiltonian, and H[Q] Hamiltonian. Consequently the certified support-compatible-family theorem applies: after fixing a Hamilton order of Q and choosing deletion covers at its two endpoints, some one F_{t_i} is support-incompatible with both endpoint covers, and these two endpoint probes force either at least three edges crossing the associated three-part partition, a direct mixed-support edge, or explicit relative-order disagreement yielding a reversed common edge, a reversing tight triple, or a vertex-simple tight cycle.

## Body

# Proof

Write D={t_1,t_2,t_3}. Since every t in D is a compatibility neighbor of d and lies on P in the anchor cover F_d=P|Q, apply the compatible-pair normal form to F_d and F_t.

On H-{d,t}, the common ordered support classes are P-t and Q. The restored labels d and t must enter the same common class, because restoring into different classes would give a two-cover of H. Since t belongs to P in F_d, the restored label d belongs to the P-side in F_t. Therefore the support partition of F_t is

(V(P)-{t}) union {d}  |  V(Q)
= (X-{t}) | V(Q).

This holds for every t in D. Hence the three covers are pairwise support-compatible: after deleting any two labels t,u in D, both induce the same two support classes (X-{t,u}) and V(Q).

The path Q is Hamiltonian because it is a path of F_d. The induced subtournament H[X] is non-Hamiltonian; otherwise a Hamilton path on X together with Q would give a two-cover of H.

Thus all hypotheses of the certified support-compatible deletion-family theorem e92b0f47c1a6 hold for the family {F_t:t in D}, with critical class X and fixed complementary path Q. That theorem supplies a label t in D whose deletion cover F_t is support-incompatible with chosen deletion covers at both endpoints of a Hamilton order of Q. Its endpoint analysis then yields the stated alternatives: at least three edges crossing the three-part partition, a direct mixed-support edge, or relative-order disagreement and hence a reversed common edge, reversing tight triple, or vertex-simple tight cycle.

The same argument is symmetric when three compatibility neighbors of d lie on Q.
