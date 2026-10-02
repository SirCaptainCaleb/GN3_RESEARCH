# Endpoint minimality blocks every proper Hamiltonian transfer from the mandatory side

## Statement

Let H have a mandatory ordered tight triple T, and choose a spanning two-cover A|B with T consecutive on the displayed path A and |A| minimum. Let X be a nonempty subset of V(A) which does not contain all three vertices of T. If H[V(A)-X] is Hamiltonian, then H[V(B) union X] is non-Hamiltonian. Consequently, writing the displayed path A=(p_0,...,p_r), every nonempty initial or terminal segment X whose removal leaves a nonempty inherited path and which does not contain all of T gives a non-Hamiltonian extension B union X.

## Body

Suppose H[A-X] and H[B union X] are both Hamiltonian, and choose Hamilton paths P and Q on those two disjoint supports.

If X is disjoint from T, then all three vertices of T lie in A-X. If P contains T consecutively, P|Q is a spanning two-cover whose T-containing component has order |A|-|X|<|A|, contradicting the choice of A. If P does not contain T consecutively, then Q contains no vertex of T, so P|Q is a spanning two-cover avoiding the mandatory triple, also a contradiction.

If X meets T but does not contain all of T, then some vertices of T lie in A-X and some lie in B union X. Thus neither support contains all three vertices of T. Hence P|Q cannot contain T consecutively in either component, contradicting mandatoryness.

Therefore H[B union X] is non-Hamiltonian.

For the final assertion, deleting an initial or terminal segment from the displayed tight path A leaves the complementary inherited segment as a tight path, hence Hamiltonian. The first assertion applies whenever the transferred segment is nonempty, the remainder is nonempty, and the transferred segment does not contain all of T. ∎