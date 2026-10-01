# Dual slack charges across successful omission replacements

## Statement

Let H be a boundary tournament with a dual-feasible weight function w satisfying w(V(T))<=1 for every tight path T and total weight w(V(H))=2+eta. Assume H-v has a deletion cover P|Q. Put alpha=1-w(V(P)), beta=1-w(V(Q)), and delta(x)=w(x)-eta. Then alpha,beta>=0 and alpha+beta=delta(v). If u in V(P) is such that (V(P)-{u}) union {v} is Hamiltonian, then delta(u)>=beta. Symmetrically, if z in V(Q) is replaceable by v, then delta(z)>=alpha. Consequently, r distinct v-replaceable vertices of P contribute at least r beta total delta-mass, and s such vertices of Q contribute at least s alpha.

## Body

# Proof

By dual feasibility,

w(P)<=1,  w(Q)<=1,

so alpha,beta are nonnegative.

The deletion-cover slack identity 9acf756c30e6 gives

alpha+beta=delta(v).

Now let u in V(P) and suppose (V(P)-{u}) union {v} is Hamiltonian. Let P' be a Hamilton path on this support. Dual feasibility gives

w(P')<=1.

But

w(P')
= w(P)-w(u)+w(v)
= (1-alpha)-w(u)+(eta+delta(v)).

Therefore

(1-alpha)-w(u)+eta+delta(v) <= 1,

so

w(u) >= eta+delta(v)-alpha
      = eta+beta.

Subtracting eta gives

delta(u)>=beta.

The Q-side statement is identical:

if z in V(Q) and (V(Q)-{z}) union {v} is Hamiltonian, then

delta(z)>=alpha.

Summing the pointwise inequalities over any collection of distinct replaceable vertices gives the final counting statements.

Thus successful omission replacement is quantitatively expensive in the dual certificate: every replacement on one component must pay at least the entire slack of the opposite component out of the replacing vertex's excess delta-mass.
