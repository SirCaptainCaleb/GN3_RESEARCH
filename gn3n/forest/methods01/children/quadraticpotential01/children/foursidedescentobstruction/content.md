# A four-side next to a long path either descends or creates two synchronized middle-path obstructions

## Statement

Let C=X|P|Q be any spanning three-path cover, with X=(x_0,x_1,x_2,x_3) a tight four-path and P=(p_1,...,p_m) a tight path of order m>=6. Then either one legal repartition of X|P strictly decreases quadratic potential by 2m-10, or both x_0 and x_3 fail to Hamiltonize the same inherited middle path M=(p_2,...,p_{m-1}). In the latter branch each of x_0,x_3 is noninsertable into the displayed order of M, so the certified failed-insertion theorem supplies two bounded obstruction windows on one common path.

## Body


Let

C = X | P | Q,

where

X=(x_0,x_1,x_2,x_3)

is a tight four-path and

P=(p_1,...,p_m)

is a tight path with m>=6.

Write

M=(p_2,...,p_{m-1}).

We prove the stated dichotomy.

First inspect the endpoint extensions

X union {p_1},
X union {p_m}.

If either five-set is Hamiltonian, say X union {p_1}, then repartition X|P as

(X union {p_1}) | (p_2,...,p_m).

The old quadratic-potential contribution is

4^2+m^2,

and the new contribution is

5^2+(m-1)^2.

Thus

Phi(C)-Phi(C')
=16+m^2-[25+(m-1)^2]
=2m-10>0.

The same holds using p_m.

Hence assume both five-sets

X union {p_1},
X union {p_m}

are non-Hamiltonian.

Apply the certified repeated-bad-extension lemma from localextend01 to the Hamiltonian four-set X, with its displayed Hamilton order, and exterior vertices p_1,p_m. It forces both crossed five-sets

F_L={x_0,x_1,x_2,p_1,p_m}

and

F_R={x_1,x_2,x_3,p_1,p_m}

to be Hamiltonian.

Now inspect the two complementary supports inside V(X) union V(P).

The complement of F_L is

V(M) union {x_3}.

If this set is Hamiltonian, then X|P can be repartitioned as

F_L | (M union {x_3}),

with component orders 5 and m-1. The same calculation gives the strict drop

2m-10.

Similarly, if

M union {x_0}

is Hamiltonian, use F_R and obtain the same strict descent.

Therefore the only branch in which no strict one-move descent has been found satisfies simultaneously

H[V(M) union {x_0}] non-Hamiltonian
and
H[V(M) union {x_3}] non-Hamiltonian.

Since M is itself the displayed inherited tight path, neither x_0 nor x_3 can be inserted into any position of that displayed order to produce a tight Hamilton path: such an insertion would Hamiltonize the corresponding induced set.

Thus the certified failed-insertion theorem insert01 applies separately to x_0 and x_3 against the same path M. It supplies, for each endpoint label, a bounded obstruction window involving that label and at most four consecutive vertices of M.

Hence every four-side/long-path pair has one of two outputs:

1. an explicit strict quadratic descent in one repartition move, with drop 2m-10; or
2. two synchronized bounded insertion obstructions, for the two endpoints of the four-side, localized on one common inherited middle path.

This is an arbitrary-state statement; no quadratic minimality or trappedness hypothesis is used.
