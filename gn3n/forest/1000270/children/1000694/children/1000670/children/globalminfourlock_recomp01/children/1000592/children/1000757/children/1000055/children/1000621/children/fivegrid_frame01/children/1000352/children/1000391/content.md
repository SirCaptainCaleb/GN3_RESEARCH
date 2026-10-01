# From lambda fourteen onward a normalized sharp-shell five-side forces order disagreement at every endpoint pair

## Statement

Let H be a minimum counterexample in the sharp half-order shell |V(H)|=2lambda+1 with lambda>=14. Among all spanning three-covers minimizing the quadratic potential, choose one whose minimum path order is as large as possible. If its minimum path order is five, write the cover X|P|Q with |X|=5 and |P|=m>=r=|Q|. Then for every pair e,f of displayed endpoints of P and Q there exists x in X such that S=(X-{x}) union {e,f} is non-Hamiltonian with at least four Hamiltonian deletions, and the Hamiltonian deletion paths of S necessarily expose order disagreement. Consequently the normalized global minimum either has all three path orders at least six, or a five-side produces explicit order-disagreement witnesses at all six endpoint pairs.

## Body

By the certified secondary-normalization theorem bee85c525fb5, the chosen global quadratic minimum has minimum path order at least five. Assume it is exactly five and write the cover as
X|P|Q,
with |X|=5 and m=|P|>=r=|Q|.

Since
5+m+r=2lambda+1,
we have
m+r=2lambda-4.                                      (1)
Because lambda is the maximum tight-path order,
m<=lambda.
Together with m>=r, equation (1) gives
m in {lambda-2, lambda-1, lambda}.
Since lambda>=14, in every case r>=lambda-4>=10, so the preceding five-side endpoint-pair dichotomy applies.

Fix any pair e,f of displayed endpoints. Let S be the associated six-set from that theorem. We show its Hamiltonian alternative is impossible.

Case 1: m=lambda.
The Hamiltonian alternative would produce a complementary two-cover with a path of order at least m+1=lambda+1, contradicting the definition of lambda.

Case 2: m=lambda-1.
Then r=lambda-3. In the Hamiltonian alternative, the complementary two-cover U|V has larger path order p>=m+1=lambda. Hence p=lambda, because no path is longer than lambda. Since H-S has order
2lambda-5,
the other path has order q=lambda-5.
Thus the resulting spanning three-cover has path-order multiset
{6,lambda,lambda-5}.

The original multiset is
{5,lambda-1,lambda-3}.
Their quadratic potentials differ by
[6^2+lambda^2+(lambda-5)^2]
-
[5^2+(lambda-1)^2+(lambda-3)^2]
=26-2lambda.
For lambda>=14 this is negative, contradicting global quadratic minimality.

Case 3: m=lambda-2.
Then r=lambda-2. The Hamiltonian alternative gives p>=lambda-1, while p<=lambda. If p=lambda-1, then q=lambda-4 and the new multiset is {6,lambda-1,lambda-4}; its quadratic potential minus the original {5,lambda-2,lambda-2} potential is
20-2lambda<0.

If p=lambda, then q=lambda-5 and the new multiset is {6,lambda,lambda-5}; the potential difference is
28-2lambda.
For lambda>=15 this is negative. At lambda=14 it is zero, so the new cover is also globally quadratic-minimal, but its minimum path order is
min{6,14,9}=6,
strictly larger than five. This contradicts the secondary choice maximizing the minimum path order among global minima.

Thus in all three possible profiles and every lambda>=14, the associated six-set S cannot be Hamiltonian.

Therefore S is non-Hamiltonian. By the first theorem it has at least four Hamiltonian deletions, and arbitrary Hamilton paths on four such deletions contain a pair with order disagreement, yielding the standard reversed-edge, reversing-triple, or vertex-simple tight-cycle witness.

Since e,f were arbitrary, every one of the six endpoint pairs yields such a bounded order-disagreement witness. Hence either the normalized global minimum has minimum path order at least six, or a five-side forces endpoint-pair order disagreement everywhere. ∎
