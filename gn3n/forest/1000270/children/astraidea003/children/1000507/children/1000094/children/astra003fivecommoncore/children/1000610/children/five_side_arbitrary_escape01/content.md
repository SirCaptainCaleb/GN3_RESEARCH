# Any five-side beside a long path descends, exchanges support, or forces a displayed-edge reversal

## Statement

Let H be a boundary tournament and let X|P|Q be a spanning three-cover, where |X|=5 and P=(p_1,...,p_m) has m>=7. Then at least one of the following holds: (1) one legal pairwise repartition of X|P strictly decreases the quadratic potential; (2) one legal pairwise repartition of X|P preserves the component-order multiset {5,m} and exchanges one vertex x∈X with one displayed endpoint of P; (3) there is a tight triple containing a vertex x∈X that reverses a displayed edge of P.

## Body

Apply bc48e8bb931a. If its endpoint-transfer alternative occurs, we obtain (1). Otherwise there is x∈X such that, with D=V(X)-{x}, both D∪{p_1} and D∪{p_m} are Hamiltonian.

Fix e∈{p_1,p_m}. If H[(V(P)-{e})∪{x}] is Hamiltonian, then a Hamilton path on D∪{e} together with a Hamilton path on (V(P)-{e})∪{x} gives a two-path repartition of V(X)∪V(P) with component orders 5 and m. Replacing X|P by this pair is a legal equal-Phi support exchange, giving (2).

Suppose neither endpoint gives such an exchange. Then both supports (V(P)-{p_1})∪{x} and (V(P)-{p_m})∪{x} are non-Hamiltonian. Apply two_truncation_blockade_reversal01 to the displayed path P and exterior vertex x. It follows that x is noninsertable in every position of P and that some tight triple involving x reverses a displayed edge of P. This is (3).

No trappedness or Phi-minimality hypothesis is used.
