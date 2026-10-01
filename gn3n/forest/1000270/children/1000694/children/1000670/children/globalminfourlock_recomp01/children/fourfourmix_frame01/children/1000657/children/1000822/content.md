# A trapped quadratic minimum cannot have profile 4|4|a with a at least six

## Statement

Let H be a boundary tournament and let X|Y|P be a spanning three-path cover that minimizes the quadratic potential Phi within its connected pairwise-repartition component, and suppose that component contains no spanning cover with at most two components. If |X|=|Y|=4 and |P|=a>=6, then a contradiction follows. Hence no Phi-minimal trapped three-cover has component-order profile {a,4,4} with a>=6. This strengthens the corresponding global-minimum exclusion to the local trapped-basin setting.

## Body

Assume for contradiction that
C=X|Y|P
is Phi-minimal in its trapped pairwise-repartition component, with
|X|=|Y|=4
and
|P|=a>=6.

We first claim that
H[V(Y) union {x}]
is non-Hamiltonian for every x in V(X).

Suppose instead that Y union {x} is Hamiltonian for some x in X. Every three-vertex boundary tournament is Hamiltonian, so X-{x} has a Hamilton path. Therefore the pair X|Y admits a legal repartition into component orders 3 and 5:
(X-{x}) | (Y union {x}).
Keeping P fixed gives a reachable spanning three-cover C_1 of profile 3|5|a.

Relative to C, this first move raises the quadratic potential by exactly
(3^2+5^2)-(4^2+4^2)=34-32=2.                       (1)

Now apply threesidedescent6 to the three-vertex component of C_1 and the a-vertex path P. Since a>=6, one further legal repartition produces a spanning three-cover C_2 satisfying either
Phi(C_1)-Phi(C_2)=2a-8
or
Phi(C_1)-Phi(C_2)=4a-20.
For a>=6 both quantities are at least 4. Combining with (1),
Phi(C_2)<Phi(C),
contradicting the Phi-minimality of C in its own connected component.

Thus every x in X is a bad one-vertex extension of Y.

Choose any three distinct vertices of X. The certified mixed-repartition theorem c82e8c6d3016 applies to the disjoint Hamiltonian four-sets X,Y and these three bad labels. It supplies a legal 5|3 two-cover of X union Y. Repartitioning the pair X|Y accordingly yields another reachable spanning three-cover C_1 of profile 5|3|a. Again
Phi(C_1)-Phi(C)=2.

Apply threesidedescent6 once more to the three-side and P. The next move lowers Phi by at least 4, so the resulting reachable three-cover has Phi strictly below Phi(C), again contradicting local minimality.

Therefore no such trapped Phi-minimal profile 4|4|a with a>=6 exists. ∎