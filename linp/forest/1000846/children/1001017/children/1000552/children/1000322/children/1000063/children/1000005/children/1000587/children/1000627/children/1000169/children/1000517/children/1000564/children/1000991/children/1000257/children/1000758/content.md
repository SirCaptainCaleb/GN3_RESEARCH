# Lexicographically maximal two-hole states push gap-three rotations onto no-better hole pairs

## Statement

Fix a top-rank nonspecial edge e and a wrong entrance x'!=x. Among all (ell-2)-edge paths Q ending in e through x' and having exactly two holes outside their vertex set, choose Q so that the nondecreasing pair of hole potentials
  (min{phi(a),phi(b)}, max{phi(a),phi(b)})
is lexicographically maximal.

Suppose Q admits a gap-three two-hole collision rotation as in 387e8e7dba7c, producing another (ell-2)-edge path Q' with the same final edge e and the same wrong entrance x'. Let {a',b'}=V(H)\V(Q') be its new holes. Then
  sort(phi(a),phi(b)) >=_lex sort(phi(a'),phi(b')).

Moreover a',b' both lie on Q, so
  phi(a'),phi(b') >= ceil((ell-2)/2).
Consequently
  phi(a),phi(b) >= ceil((ell-2)/2).

More generally, the old hole-potential pair lexicographically dominates the potential pair of the two specific path vertices ejected by every available gap-three rotation.

## Body

The first assertion is immediate from the extremal choice of Q: by 387e8e7dba7c, a gap-three collision produces another path of the same length ell-2, ending in the same edge through the same wrong entrance, and again omitting exactly two vertices. Hence Q' belongs to the same admissible state space, so its sorted hole-potential pair cannot lexicographically exceed that of Q.

Because Q' has the same number of vertices as Q and contains the old holes a,b, its two new holes a',b' are vertices that belonged to Q.

Apply the certified half-path endpoint-potential lemma 8b1790d79d74 to the (ell-2)-edge path Q. Every vertex on Q has endpoint potential at least ceil((ell-2)/2). Thus
phi(a'),phi(b')>=ceil((ell-2)/2).

If the sorted old pair had first coordinate below ceil((ell-2)/2), while both coordinates of the new pair are at least this threshold, the new pair would be lexicographically larger, contradiction. Hence the smaller of phi(a),phi(b) is at least the threshold, and therefore both are.
