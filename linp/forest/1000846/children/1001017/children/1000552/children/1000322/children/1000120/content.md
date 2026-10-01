# Lexicographically maximal fixed-edge paths push rotations onto maximum-potential private vertices

## Statement

Let H have global maximum path length L and let e be a nonspecial edge of rank L with unique entrance x. Among all globally longest L-edge paths ending in e through x, choose P lexicographically maximizing the sorted multiset of endpoint potentials of the private vertices of its path edges. Suppose a safe opposite-end single-blocker rotation replaces one path edge g_j by an external edge f and thereby imports an outside vertex o while ejecting the private vertex p_j of g_j. Then phi(o)=phi(p_j)=L.

## Body

A safe opposite-end single-blocker rotation remains inside the state space of globally longest L-edge paths ending in the fixed edge e through the fixed entrance x, by fc1f69f1f481.

In the explicit single-blocker rotation, exactly one path edge is omitted and one external edge f is inserted. The two path-joint vertices of the omitted edge remain present in the neighboring path edges, while its private vertex p_j disappears. The inserted edge uses two vertices already on the old path—the rotating endpoint and its blocker—and one vertex o outside the old path. Thus the new path vertex set is obtained from the old one by replacing p_j with o.

Because o is a last vertex of the rotated globally longest L-edge path, phi(o)=L.

Now compare the multisets of endpoint potentials of private path vertices before and after the rotation. All unchanged private vertices retain their values. The only exchanged private vertex is p_j versus the newly imported endpoint/private contribution o of value L. Since P was chosen lexicographically maximal among all fixed-(e,x) longest paths, we cannot have phi(p_j)<L, because the rotated path would then strictly improve the sorted multiset. Global maximality gives phi(p_j)<=L. Hence phi(p_j)=L.

Therefore every safe outside single-blocker rotation from a lexicographically maximal fixed-edge state can eject only a private path vertex of maximum endpoint potential L.
