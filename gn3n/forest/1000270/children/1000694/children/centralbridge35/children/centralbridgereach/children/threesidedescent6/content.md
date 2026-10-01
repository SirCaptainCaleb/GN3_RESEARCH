# Every three-side next to a path of order at least six has a strict one-move quadratic descent

## Statement

Let C=X|P|Q be any spanning three-path cover of a boundary tournament, where X is a tight path of order three and P=(p_1,...,p_m) has m>=6. Then one legal pairwise repartition of X|P produces another spanning three-path cover C_prime with strictly smaller quadratic potential. More precisely, either X union {p_1} or X union {p_m} is Hamiltonian, yielding component orders 4 and m-1 and potential drop 2m-8; or both four-sets are non-Hamiltonian, in which case X union {p_1,p_m} is Hamiltonian by localextend01 and yields component orders 5 and m-2 with potential drop 4m-20.

## Body

Let

C = X | P | Q

be a spanning three-path cover, where |X|=3 and

P=(p_1,...,p_m)

has m>=6. Write

Phi(C)=sum_i |P_i|^2.

We inspect the two endpoint extensions

X union {p_1},
X union {p_m}.

If at least one is Hamiltonian, say X union {p_1}, repartition the pair X|P as

(X union {p_1}) | (p_2,...,p_m).

Both displayed parts are tight paths: the first by hypothesis, the second as an inherited contiguous subpath of P. The old contribution of X|P to Phi is

3^2 + m^2,

while the new contribution is

4^2 + (m-1)^2.

Hence

Phi(C)-Phi(C')
= 9+m^2 - [16+(m-1)^2]
= 2m-8 > 0.

The same argument applies if X union {p_m} is Hamiltonian.

It remains to suppose that both endpoint four-sets

X union {p_1}
and
X union {p_m}

are non-Hamiltonian.

Apply the certified local-extension lemma from localextend01, “Two bad four-extensions force a controlled five-path,” to the fixed tight three-path X and the exterior vertices p_1,p_m. It gives a Hamilton tight path on

X union {p_1,p_m}.

Therefore X|P can be repartitioned as

(X union {p_1,p_m}) | (p_2,...,p_{m-1}).

The second part is again an inherited contiguous path and is nonempty because m>=6.

The old Phi contribution is again

9+m^2,

whereas the new contribution is

5^2+(m-2)^2.

Thus

Phi(C)-Phi(C')
=9+m^2-[25+(m-2)^2]
=4m-20 >0

for m>=6.

Hence in every case a single legal repartition move strictly decreases Phi.

No trappedness or Phi-minimality assumption is used. The theorem is an arbitrary-state descent rule.

Consequently, whenever the canonical central-bridge construction produces a three-vertex path component, that component can coexist with a path component of order at least six only transiently: the state has an immediate strict quadratic descent involving those two path components.
