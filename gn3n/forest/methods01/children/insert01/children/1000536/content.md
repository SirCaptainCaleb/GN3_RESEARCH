# Order-preserving opposite endpoint replacements splice for longest paths of order at least six

## Statement

Let H be a boundary tournament and let A=(a_0,...,a_{lambda-1}) be a globally longest tight path of order lambda>=6. Let x,y be distinct vertices outside A. Suppose L is a Hamilton tight path on (V(A)-{a_0}) union {x} and R is a Hamilton tight path on (V(A)-{a_{lambda-1}}) union {y}, and each of L,R preserves the relative order of its common A-vertices. Then (V(A)-{a_0,a_{lambda-1}}) union {x,y} is Hamiltonian. More precisely, L is either (x,a_1,...,a_{lambda-1}) or (a_1,x,a_2,...,a_{lambda-1}), while R is either (a_0,...,a_{lambda-2},y) or (a_0,...,a_{lambda-3},y,a_{lambda-2}); splicing the corresponding endpoint-local forms gives a tight path on the double replacement support.

## Body

Let A=(a_0,...,a_{lambda-1}) be globally longest, with lambda>=6.

Because A is globally longest, A union {x} is non-Hamiltonian. Since L preserves the relative order of a_1,...,a_{lambda-1}, it is obtained by inserting x into that displayed order. If x occurred after the second position of L, then L would begin a_1,a_2. Prepending a_0 would give a tight path of order lambda+1: the only new initial triple is (a_0,a_1,a_2), which is tight in A, and every later triple is already tight in L. This contradicts maximality. Hence
L=(x,a_1,...,a_{lambda-1})
or
L=(a_1,x,a_2,...,a_{lambda-1}).

Symmetrically, A union {y} is non-Hamiltonian. Since R preserves the relative order of a_0,...,a_{lambda-2}, if y occurred before the last two positions then R would end in a_{lambda-3},a_{lambda-2}, and appending a_{lambda-1} would give a tight path of order lambda+1. Therefore
R=(a_0,...,a_{lambda-2},y)
or
R=(a_0,...,a_{lambda-3},y,a_{lambda-2}).

There are four combinations. They yield respectively
(x,a_1,a_2,...,a_{lambda-2},y),
(x,a_1,a_2,...,a_{lambda-3},y,a_{lambda-2}),
(a_1,x,a_2,...,a_{lambda-2},y),
(a_1,x,a_2,...,a_{lambda-3},y,a_{lambda-2}).

Each uses exactly (V(A)-{a_0,a_{lambda-1}}) union {x,y}. Every consecutive triple near the left replacement is a consecutive triple of L, every consecutive triple near the right replacement is a consecutive triple of R, and every remaining consecutive triple is inherited from A. In the only tight-overlap case, the fourth form with lambda=6, the central triples are (x,a_2,a_3) from L and (a_2,a_3,y) from R; for larger lambda the two endpoint neighborhoods are farther apart. Thus no new uncertified triple appears.

Hence in every case the displayed sequence is a tight path of order lambda on the double replacement support. ∎
