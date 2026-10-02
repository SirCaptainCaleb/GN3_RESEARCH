# Neutral degree on a local 4|5|a quadratic plateau is large except in two incidence regimes

## Statement

Let H be a boundary tournament and let C=X|Y|P minimize the quadratic potential Phi within its connected component of the pairwise-repartition graph, with |X|=4, |Y|=5, and |P|=a>=7. Put
h=|{y in Y : H[X union {y}] is Hamiltonian}|
and
g=|{y in Y : H[Y-{y}] is Hamiltonian}|.
Then C has at least
max{0,7-2h}+max{0,h+g-5}
distinct nontrivial one-move equal-Phi neighbors obtained by repartitioning the fixed nine-vertex subsystem X union Y into components of orders 4 and 5. In particular g>=2, so for h=0,1,2,3,4,5 the guaranteed neutral degrees are respectively at least
7,5,3,1,1,2.
Consequently a local 4|5|a quadratic-minimum state of neutral degree one can occur only when h is 3 or 4.

## Body

We first show that H[Y union {x}] is non-Hamiltonian for every x in X. Suppose instead that Y union {x} is Hamiltonian. Then
(X-{x}) | (Y union {x})
is a legal repartition of X|Y, with pair sizes 3 and 6 instead of 4 and 5, so Phi increases by 4. The resulting three-cover still contains the a-vertex path P. By threesidedescent6, repartitioning the three-vertex side with P strictly decreases Phi by at least 2a-8>=6. Thus the two moves reach a state in the same connected component with Phi at most Phi(C)-2, contradicting the minimality of C. Therefore
H[Y union {x}] is non-Hamiltonian for all x in X.                    (1)

Define relations A,F subseteq X times Y by
A(x,y) iff H[(X-{x}) union {y}] is Hamiltonian,
F(x,y) iff H[(Y-{y}) union {x}] is Hamiltonian.

Fix x in X. By (1), the six-set Y union {x} is non-Hamiltonian, while deleting x leaves the Hamiltonian five-set Y. The four-of-six theorem gives at least four Hamiltonian one-vertex deletions, so at least three y in Y satisfy F(x,y). Hence
|F|>=12.                                                           (2)

Now fix y in Y. If X union {y} is Hamiltonian, then a Hamiltonian five-set has at most three non-Hamiltonian four-vertex deletions, so among the four pairs (x,y) at most three fail A. If X union {y} is non-Hamiltonian, then a non-Hamiltonian five-set has at most one non-Hamiltonian four-vertex deletion, so among the four pairs at most one fails A. Therefore, if h is the number of y for which X union {y} is Hamiltonian,
|A^c|<=3h+(5-h)=2h+5.                                             (3)

Every pair (x,y) in A intersect F gives a nontrivial equal-Phi neighbor:
(X-{x}) union {y}  |  (Y-{y}) union {x}  |  P.
Distinct pairs give distinct four-vertex supports, hence distinct neighbors. From (2) and (3),
|A intersect F| >= |F|-|A^c| >= 7-2h,
and of course this yields at least max{0,7-2h} such neighbors.        (4)

There is a second, disjoint source of neutral neighbors. Let
T={y in Y : X union {y} is Hamiltonian}
and
G={y in Y : Y-{y} is Hamiltonian},
so |T|=h and |G|=g. For every y in T intersect G,
X union {y}  |  Y-{y}  |  P
is another nontrivial equal-Phi neighbor. These supports are distinct for distinct y, and none coincides with a neighbor counted in (4): its four-vertex side lies wholly in Y, whereas every four-vertex side in (4) contains three vertices of X. Hence these contribute
|T intersect G| >= max{0,h+g-5}                                  (5)
additional neighbors.

Adding (4) and (5) proves the displayed bound.

Finally, because Y is itself a displayed tight path, deleting either endpoint of its displayed Hamilton order leaves an inherited Hamilton path on four vertices. Thus g>=2. Substituting this into the bound gives the lower-degree sequence
7,5,3,1,1,2
for h=0,1,2,3,4,5 respectively. ∎