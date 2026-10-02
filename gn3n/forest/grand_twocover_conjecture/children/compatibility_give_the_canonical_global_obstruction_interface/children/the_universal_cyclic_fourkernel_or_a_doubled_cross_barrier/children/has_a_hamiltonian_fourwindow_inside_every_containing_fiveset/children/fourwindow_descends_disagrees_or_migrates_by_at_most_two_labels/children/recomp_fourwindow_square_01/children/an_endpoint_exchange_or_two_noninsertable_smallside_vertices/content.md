# A Phi-minimal 4|5|m three-cover has an endpoint exchange or two noninsertable small-side vertices

## Statement


Let H be a boundary tournament and let
C=X|Y|P
be a spanning three-cover minimizing the quadratic potential Phi in its connected pairwise-repartition component, where |X|=4, |Y|=5, and
P=(p_1,...,p_m)
has m>=7 vertices.

Then at least one of the following holds.

(1) There is an equal-Phi pairwise repartition exchanging one displayed endpoint e of P with one vertex of X or Y. Concretely, for some Z in {X,Y}, some z in V(Z), and some e in {p_1,p_m}, both
(V(Z)-{z}) union {e}
and
(V(P)-{e}) union {z}
are Hamiltonian; replacing Z|P by these two Hamiltonian supports preserves the two component orders.

(2) There are distinct vertices x in X and y in Y that are both noninsertable into the displayed order of P. Then one of the following holds:
  (a) a Hamiltonian four-set consisting of one of x,y and three consecutive vertices of P;
  (b) a Hamiltonian five-set consisting of x,y and three consecutive vertices of P;
  (c) a tight cross triple (x,p_i,y) or (y,p_i,x) for some p_i in P;
  (d) after possibly interchanging x,y, a tight connector (x,p_{i+1},...,p_j,y) through a nonempty displayed interval of P with j>=i+2.




## Body


Apply 8e138afbc628 to the four-side X. Choose one of the synchronized vertices x in X supplied there. Then for both endpoints e in {p_1,p_m},
(X-{x}) union {e}
is Hamiltonian.

For a fixed endpoint e, if
(P-{e}) union {x}
is Hamiltonian, these two Hamiltonian supports partition V(X) union V(P), have orders 4 and m, and therefore give an equal-Phi repartition of X|P. This is outcome (1).

Assume no such endpoint exchange with X exists. Then both
(P-{p_1}) union {x}
and
(P-{p_m}) union {x}
are non-Hamiltonian.

We claim x is noninsertable into the full displayed order P. Suppose a Hamilton path on V(P) union {x} were obtained by inserting x into that order. If x is inserted before p_1, deleting the opposite endpoint p_m leaves an insertion of x into P-p_m; if x is inserted after p_m, deleting p_1 leaves an insertion into P-p_1. For an insertion between p_i and p_{i+1}, delete p_m when i<=m-2 and delete p_1 when i>=2; the two boundary internal positions i=1 and i=m-1 are covered by the first and second choices respectively. In every case one of the two endpoint-truncation enlargements would be Hamiltonian, contradiction. Hence x is noninsertable into P.

Now apply astra003fivecommoncore to the five-side Y and the same long path P. It supplies y in Y such that
(Y-{y}) union {p_1}
and
(Y-{y}) union {p_m}
are Hamiltonian.

For either endpoint e, if
(P-{e}) union {y}
is Hamiltonian, then replacing Y|P by
((Y-{y}) union {e}) | ((P-{e}) union {y})
is a legal repartition with the same component orders 5 and m, hence the same Phi. Again outcome (1) holds.

Assume no such five-side endpoint exchange exists. Exactly the same endpoint-truncation argument shows that y is noninsertable into the full displayed order P. Since x in X and y in Y, they are distinct exterior vertices.

Apply a8c9883902b1 to P and x,y. It gives a Hamiltonian four-set, the exceptional cyclic non-Hamiltonian four-set with universal exterior extension, a Hamiltonian five-set, a cross triple, or an interval connector. In the exceptional cyclic-four case the other one of x,y is exterior to that four-set, so adjoining it gives a Hamiltonian five-set on x,y and three consecutive vertices of P. Hence that case is absorbed into (2b), leaving the four alternatives in the statement. ∎
