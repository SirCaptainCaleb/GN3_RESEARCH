# A longest path has Hamiltonian five-extensions at all but at most two exterior vertices unless a reversal K4 appears

## Statement

Let H be a minimum counterexample and let A=(a_0,...,a_{lambda-1}) be a globally longest tight path. Put
D={a_1,a_0,a_{lambda-1},a_{lambda-2}}
and U=V(H)-V(A).

Then either:

(1) there are distinct exterior vertices w,y,z in U for which a tight triple reverses an internal edge of a tight four-path, so the certified K4 frontier of 53005a4e0315 occurs; or

(2) for all but at most two vertices y in U, the five-set D union {y} is Hamiltonian, with explicit tight order
(a_1,a_0,y,a_{lambda-1},a_{lambda-2}).

Since |U|>=4, alternative (2) supplies at least two distinct Hamiltonian five-sets sharing the same four-vertex core D.

## Body

For every y in U, bcfa72bc175f gives the two tight endpoint triples
(a_1,a_0,y) and (y,a_{lambda-1},a_{lambda-2}).

Call y good if (a_0,y,a_{lambda-1}) is tight. For every good y,
(a_1,a_0,y,a_{lambda-1},a_{lambda-2})
is a tight five-path, so D union {y} is Hamiltonian.

Call y cross otherwise. Boundary antisymmetry gives
(a_{lambda-1},y,a_0)
tight for every cross y.

Suppose there are at least three cross vertices. On the cross set C define an ordinary tournament T by
p -> q iff (p,a_{lambda-1},q) is tight.
Any tournament on at least three vertices contains a vertex y having both an in-neighbor w and an out-neighbor z: if no vertex had both, every vertex would be a source or sink, and a tournament has at most one of each.

Choose w,y,z accordingly. Then
(w,a_{lambda-1},y)
and
(y,a_{lambda-1},z)
are tight, while the cross property of y gives
(a_{lambda-1},y,a_0)
tight. Hence
(w,a_{lambda-1},y,a_0)
is a tight four-path and
(y,a_{lambda-1},z)
reverses its internal displayed edge a_{lambda-1}y. Apply 53005a4e0315 to obtain alternative (1).

Therefore if alternative (1) does not occur, there are at most two cross vertices. Every other y in U is good, proving (2). Minimum-counterexample calculus gives |U|>=4, so at least two good labels remain.

No cyclic rotation and no reversal of a displayed path is used.