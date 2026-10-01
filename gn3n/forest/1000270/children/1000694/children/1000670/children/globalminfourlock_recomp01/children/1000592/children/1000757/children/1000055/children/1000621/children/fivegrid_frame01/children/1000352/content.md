# Every endpoint pair at a global five-side minimum gives strict imbalance gain or six-set order disagreement

## Statement

Let H be a minimum counterexample and let X|P|Q be a spanning three-cover minimizing the quadratic potential among all spanning three-covers, with |X|=5 and |P|=m>=r=|Q|>=7. Let e,f be any two distinct displayed endpoints among P and Q. Then there is x in X such that S=(X-{x}) union {e,f} has at least four Hamiltonian vertex deletions. Moreover either: (i) S is Hamiltonian, and every two-cover U|V of H-S, ordered with p=|U|>=q=|V|, satisfies p-q>=m-r+3, q<=r-2, and p>=m+1; or (ii) S is non-Hamiltonian, and arbitrary Hamilton paths chosen on four Hamiltonian deletions of S contain a pair with order disagreement, hence a reversed common ordered edge, a tight triple reversing an ordered edge, or a vertex-simple tight cycle.

## Body

Write d=m-r and s=m+r.

As in the five-side endpoint-pair grid theorem, every displayed endpoint e of P or Q is a bad extension of X: if X union {e} were Hamiltonian, transferring e into X would change path orders 5,t to 6,t-1 for t>=7 and lower the quadratic potential by 2t-12>0.

Fix distinct endpoints e,f. Apply 41a89ea9eacf to the Hamiltonian five-set X and the two bad extensions e,f. It gives a vertex x in X such that
(X-{x}) union {e}
and
(X-{x}) union {f}
are Hamiltonian, and at least two distinct vertices z in X-{x} such that
(X-{x,z}) union {e,f}
is Hamiltonian.

Put
S=(X-{x}) union {e,f}.
Thus S is a six-set with at least four Hamiltonian deletion labels: e, f, and at least two such vertices z.

Suppose first that S is non-Hamiltonian. The certified theorem astra004fourgooddisagree applies to S and any four Hamiltonian deletion labels. For arbitrary Hamilton paths chosen on those four five-vertex deletions, some pair has order disagreement. The certified path-intersection calculus then yields a reversed common ordered edge, a tight triple reversing an ordered edge, or a vertex-simple tight cycle. This is alternative (ii).

Now suppose S is Hamiltonian. Because H is a minimum counterexample, H-S has path-cover number at most two, and it is non-Hamiltonian because otherwise a Hamilton path on S together with one on H-S would two-cover H. Hence H-S has a two-cover U|V.

Apply the certified general complement-imbalance theorem 40c4a8aca820 with c=5 and h=1. If
delta=||U|-|V||,
then
delta^2 >= d^2 + 2s - 23.                         (1)

Since r>=7, s>=14, so the added term is positive and delta>d. Also U|V covers s-1 vertices, so delta has parity s-1, while d=m-r has parity s. Therefore delta-d is a positive odd integer.

We exclude delta=d+1. If equality held, (1) would imply
(d+1)^2 >= d^2+2s-23,
so
2d+1 >= 2s-23,
and hence
2(s-d)<=24.
But s-d=2r, giving
4r<=24,
contrary to r>=7. Thus
delta>=d+3.

Order U,V so p>=q. Since p+q=s-1,
q=(s-1-delta)/2 <= (s-1-(d+3))/2=r-2,
and therefore
p=s-1-q>=m+1.

This is alternative (i), completing the dichotomy. ∎
