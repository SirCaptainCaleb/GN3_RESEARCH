# Equal-support opposite endpoint states force order disagreement

## Statement

Let H be a minimum counterexample and let G_x,G_y be exact two-path covers of H-x and H-y such that y is terminal in its component of G_x and x is initial in its component of G_y. After deleting y from G_x and x from G_y, suppose the resulting exact two-covers of H-{x,y} have the same unordered support partition. Then the two Hamilton orders on the common support to which x and y restore cannot have the same relative order. Consequently the path-intersection calculus yields a reversed common edge, a tight triple reversing an ordered edge, or a vertex-simple tight cycle. Thus the equal-support opposite-end comparison has no order-neutral residue.

## Body

# Equal-support opposite endpoint states force order disagreement

Let H be a minimum counterexample. Let G_x be an exact two-path cover of H-x in which y is terminal in its component, and let G_y be an exact two-path cover of H-y in which x is initial in its component. Delete those displayed endpoints, obtaining exact two-covers T_x and T_y of H-{x,y}, and suppose their unordered support partitions agree.

By the equal-support restoration lemma, x and y restore to the same common support S. After orienting the two restored components according to the endpoint hypothesis, write them as

P,y

in G_x and

x,P'

in G_y,

where P and P' are Hamilton paths on S. Let Q be the other component of T_x, so Q is a tight path on the complementary common support.

Suppose that P and P' have the same relative order on S. Since they have the same vertex set, they are the same displayed order; write

P=P'=(p_0,...,p_k).

The induced tournament on S union {x,y} is non-Hamiltonian by the equal-support restoration lemma. In particular |S|>=2, so k>=1.

Now

(x,p_0,...,p_k)

is tight because it is the restored component of G_y, while

(p_0,...,p_k,y)

is tight because it is the restored component of G_x. Therefore

(x,p_0,...,p_k,y)

is tight: its first consecutive triple is inherited from x,P, its last consecutive triple is inherited from P,y, and every intermediate consecutive triple is inherited from P. Together with Q this is a spanning two-path cover of H, contradicting that H is a counterexample.

Hence P and P' do not have the same relative order on their common vertex set S. The path restriction and intersection calculus therefore yields a reversed common edge, a tight triple reversing an ordered edge, or a vertex-simple tight cycle.

Thus an opposite-end comparison with equal common support partition necessarily exposes explicit order disagreement; there is no separate order-neutral equal-support bridge case. ∎
