# Every local 4|5|a quadratic minimum has a nontrivial equal-potential 4|5 repartition

## Statement

Let H be a boundary tournament and let X|Y|P be a spanning three-cover minimizing Phi within its connected pairwise-repartition component, with |X|=4, |Y|=5, and |P|=a>=7. Then H[Y union {x}] is non-Hamiltonian for every x in X. Moreover the nine-vertex subsystem X union Y has a second two-cover of component orders 4 and 5, different from X|Y. Replacing X|Y by that cover is a nontrivial one-move equal-Phi transition inside the same component. Thus no local quadratic-minimum 4|5|a state is isolated on its equal-potential 4|5 plateau.

## Body

Let C=X|Y|P minimize Phi in its connected pairwise-repartition component, with |X|=4, |Y|=5 and |P|=a>=7.

First we show that Y union {x} is non-Hamiltonian for every x in X. Suppose Y union {x} were Hamiltonian. Since every three-vertex boundary tournament is Hamiltonian, X-{x} is Hamiltonian. Hence X|Y can be legally repartitioned as

  (X-{x}) | (Y union {x}),

changing the pair orders 4,5 to 3,6. This raises Phi by

  3^2+6^2-(4^2+5^2)=4.                              (1)

The resulting three-cover has a three-vertex component and still has the a-vertex component P. By threesidedescent6, because a>=7, one further legal repartition of that three-side with P lowers Phi by at least

  2a-8 >= 6.

Together with (1), the two moves reach a state in the same connected component with Phi at most Phi(C)-2, contradicting the minimality of C. Therefore

  H[Y union {x}] is non-Hamiltonian for every x in X.       (2)

For x in X and y in Y define two incidence relations:

  F(x,y): H[(Y-{y}) union {x}] is Hamiltonian,
  A(x,y): H[(X-{x}) union {y}] is Hamiltonian.

Fix x. By (2), Y union {x} is a non-Hamiltonian six-set. The four-of-six theorem gives at least four Hamiltonian one-vertex deletions. Deleting x leaves Y, which is Hamiltonian, so at least three y in Y satisfy F(x,y). Hence

  |F| >= 4*3 = 12.                                  (3)

Now fix y in Y. Consider the five-set X union {y}.

If X union {y} is Hamiltonian, a Hamiltonian five-set has at most three non-Hamiltonian four-subsets, so at least one x in X satisfies A(x,y).

If X union {y} is non-Hamiltonian, a non-Hamiltonian five-set has at most one non-Hamiltonian four-subset, so at least three x in X satisfy A(x,y).

Let h be the number of y in Y for which X union {y} is Hamiltonian. Then the number of A-bad pairs is at most

  3h + (5-h) = 2h+5.                                (4)

If some pair (x,y) belongs to A intersect F, then

  (X-{x}) union {y}
  and
  (Y-{y}) union {x}

are disjoint Hamiltonian supports of orders 4 and 5 partitioning X union Y. They give a nontrivial 4|5 repartition of X|Y, and therefore an equal-Phi one-move transition. We are done.

Assume instead A intersect F is empty. Then F is contained in the A-bad pairs. By (3) and (4),

  12 <= 2h+5,

so h>=4.                                                (5)

Because Y itself is a Hamiltonian five-set, at most three of its four-vertex deletions are non-Hamiltonian. Thus at least two vertices y in Y satisfy

  H[Y-{y}] Hamiltonian.                               (6)

There are five vertices in Y. By (5), at least four satisfy H[X union {y}] Hamiltonian, while by (6) at least two satisfy H[Y-{y}] Hamiltonian. These two subsets of Y intersect. Choose y in their intersection. Then

  X union {y}
  and
  Y-{y}

are disjoint Hamiltonian supports of orders 5 and 4 partitioning X union Y. Again they give a nontrivial 4|5 repartition of X|Y, and its squared-size contribution is unchanged.

Thus every local Phi-minimum of profile 4|5|a with a>=7 has a nontrivial equal-Phi 4|5 neighbor inside the same pairwise-repartition component. ∎
