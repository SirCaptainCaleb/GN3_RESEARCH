# Astra-008 reduces only to the sharp odd half-order shell

## Statement

Let H be a minimum counterexample of order n, let k=floor(n/2), and let lambda be its maximum tight-path order. Suppose the positive-correlation inequality of astraidea008 holds for H. Then necessarily n=2k+1 and lambda=k. Conversely, in that sharp odd half-order shell the larger-half Hamiltonicity marginal in astraidea008 is zero, so the inequality is vacuous. Thus Astra-008, even if true, can at most reduce the grand theorem to the sharp odd half-order shell; it cannot by itself attack that shell.

## Body

# Proof

Let S be a uniformly random k-subset and define

A = {H[S] is Hamiltonian},
B = {H[V(H)-S] is Hamiltonian}.

Because H is a minimum counterexample, it has no spanning two-cover. Therefore A and B can never hold simultaneously, so

Pr(A and B)=0.

By the certified longest-path lower bound, lambda >= ceil((n-1)/2) >= k. Hence H contains a Hamiltonian k-set: take any k consecutive initial vertices of a Hamilton path of order at least k. Thus

Pr(A)>0.

If n is even, say n=2k, then the complement also has order k. The same longest-path bound gives a Hamiltonian k-set, so Pr(B)>0.

If n is odd, n=2k+1, then the complement has order k+1. If lambda>=k+1, H has a Hamiltonian (k+1)-set and hence Pr(B)>0.

In either of those cases the Astra-008 inequality would give

0 = Pr(A and B) >= Pr(A)Pr(B) > 0,

a contradiction.

Therefore, if the inequality holds in a minimum counterexample, the only possibility is

n=2k+1 and lambda=k.

In this sharp odd half-order shell, by definition there is no Hamiltonian (k+1)-set. Hence Pr(B)=0, and since H has no two-cover also Pr(A and B)=0. The asserted inequality becomes

0 >= 0

and contains no additional information.

So Astra-008 has a precise ceiling as a proof strategy: it can eliminate every minimum-counterexample regime except the sharp odd half-order shell, but it is automatically inert once that shell is reached.
