# Minimum-imbalance two-covers forbid every balance-improving Hamiltonian exchange

## Statement

Let K be a boundary tournament admitting a spanning two-cover. Choose a two-cover with Hamiltonian supports A,B minimizing the component-size imbalance, and write d=|A|-|B|>=0. Let X subseteq A and Y subseteq B, and put s=|X|-|Y|. If 0<s<d, then the two exchanged supports
(A-X) union Y
and
(B-Y) union X
cannot both be Hamiltonian.

## Body

Assume both exchanged supports are Hamiltonian. They partition V(K), so Hamilton paths on them form a spanning two-cover.

Their orders are
|A|-|X|+|Y| = |A|-s
and
|B|-|Y|+|X| = |B|+s.
Thus the new component-size imbalance is
|(|A|-s)-(|B|+s)| = |d-2s|.

Because 0<s<d, we have |d-2s|<d. This contradicts the choice of A|B as a spanning two-cover of minimum imbalance.

Therefore no support exchange with net transfer s strictly between 0 and d can Hamiltonize both exchanged sides. ∎