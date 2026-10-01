# A local 4|5|a quadratic minimum has two labels extending both long endpoints

## Statement

Let H be a boundary tournament and let C=X|Y|P be a three-cover minimizing the quadratic potential Phi within its connected component of the pairwise-repartition graph. Suppose |X|=4, |Y|=5, and P=(p_1,...,p_a) has a>=7 vertices. Then there are at least two distinct vertices x in X such that both H[(X-{x}) union {p_1}] and H[(X-{x}) union {p_a}] are Hamiltonian, H[Y union {x}] is non-Hamiltonian, and at least three vertices y in Y are Hamiltonian deletions of Y union {x}; equivalently, H[(Y-{y}) union {x}] is Hamiltonian for at least three y in Y.

## Body

Let e be either endpoint p_1 or p_a of P. We first show that H[X union {e}] is non-Hamiltonian. If it were Hamiltonian, then replacing the pair X|P by a Hamilton path on X union {e} and the inherited path P-e would be a legal pairwise repartition. The contribution of this pair to Phi would change from

4^2+a^2

to

5^2+(a-1)^2,

a decrease of 2a-10>0. This contradicts the assumed minimality of C in its connected component of the pairwise-repartition graph.

For e in {p_1,p_a}, define

I_e={x in X : H[(X-{x}) union {e}] is Hamiltonian}.

The five-set X union {e} is non-Hamiltonian, and the certified five-set deletion theorem in smallset01 says that at most one of its four-vertex induced subtournaments is non-Hamiltonian. Hence |I_e|>=3. Since X has four vertices,

|I_{p_1} intersect I_{p_a}|>=2.

Fix x in this intersection. We claim that H[Y union {x}] is non-Hamiltonian. Suppose instead that Y union {x} is Hamiltonian, and choose either endpoint e in {p_1,p_a}. Because x is in I_e, the set (X-{x}) union {e} is Hamiltonian.

Starting from X|Y|P, first repartition X|Y as

(X-{x}) | (Y union {x}).

The three-set X-{x} is Hamiltonian, and Y union {x} is Hamiltonian by assumption, so this is a legal pairwise repartition. It changes the pair sizes 4,5 to 3,6 and therefore raises Phi by 4.

Next repartition the pair (X-{x})|P as

((X-{x}) union {e}) | (P-e).

Both displayed supports are Hamiltonian: the first by x in I_e, and the second because e is an endpoint of the displayed tight path P. This changes the pair sizes 3,a to 4,a-1. Relative to the original cover, the resulting three-cover has component orders 4,6,a-1, so

Phi(new)-Phi(C)
 = [4^2+6^2+(a-1)^2]-[4^2+5^2+a^2]
 = 12-2a
 <= -2

because a>=7. The two legal pairwise repartitions therefore reach a cover in the same connected component with strictly smaller Phi, a contradiction. Thus H[Y union {x}] is non-Hamiltonian.

Finally apply the certified four-of-six theorem from smallset01 to the six-set Y union {x}. At least four of its one-vertex deletions are Hamiltonian. Deleting x leaves Y, which is already Hamiltonian, so at least three vertices y in Y satisfy that H[(Y-{y}) union {x}] is Hamiltonian.

The argument applies to every x in I_{p_1} intersect I_{p_a}, and that intersection has size at least two. This proves the claim.
