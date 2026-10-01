# The endpoint-exchange support triangle is uniformly degree-four expanding

## Statement

In the order-thirteen mu=6 shell, keep the singleton endpoint-exchange triangle X,N_a,N_c of 7ba4686e7ab5, with N_a=X-{a}+{q_0} and N_c=X-{c}+{q_5}. Then each of X,N_a,N_c has degree at least four in the Johnson-radius-three deficient-support graph Gamma. More precisely, at X the known neighbors N_a,N_c acquire only q_0 and q_5 from the complementary six-set Q, so at least two additional neighbors are required to cover q_1,q_2,q_3,q_4. At N_a the known neighbors X,N_c acquire only {a} and {a,q_5}, so at least two additional neighbors are required to cover q_1,q_2,q_3,q_4; symmetrically for N_c. If any one of the three vertices has Gamma-degree exactly four, its two unknown neighbors jointly acquire all four of those remaining complement vertices.

## Body

# The endpoint-exchange support triangle is uniformly degree-four expanding

Work in the order-thirteen mu=6 shell and use the notation of 7ba4686e7ab5. Thus

X,
N_a=(X-{a}) union {q_0},
N_c=(X-{c}) union {q_5}

are deficient seven-supports, where Q=(q_0,...,q_5)=V(H)-X, and

d_J(X,N_a)=d_J(X,N_c)=1,
d_J(N_a,N_c)=2.

We use the neighborhood-capacity theorem e3f0da9ab087: if R is a deficient seven-support with Hamiltonian six-complement S, then the acquired sets

Y_R(R')=R' intersect S,   R' in N_Gamma(R),

cover S, and every acquired set has order at most three.

## 1. Expansion at X

Relative to X, the complementary six-set is Q.

The neighbor N_a acquires exactly {q_0}, while N_c acquires exactly {q_5}. Thus the two known neighbors cover only

{q_0,q_5}

of Q.

The remaining four vertices q_1,q_2,q_3,q_4 must also belong to the union of acquired sets of Gamma-neighbors of X. Any one further neighbor can acquire at most three vertices, because Gamma has Johnson radius three. Hence one further neighbor cannot suffice.

Therefore X has at least two Gamma-neighbors other than N_a,N_c, and

deg_Gamma(X)>=4.

If equality holds, the two additional neighbors must jointly acquire all four vertices q_1,q_2,q_3,q_4.

## 2. Expansion at N_a

The complementary six-set of N_a is

S_a=(Q-{q_0}) union {a}
    ={a,q_1,q_2,q_3,q_4,q_5}.

Relative to N_a, the neighbor X is obtained by replacing q_0 with a, so its acquired set is exactly

Y_{N_a}(X)={a}.

Also

N_c=N_a-{q_0,c}+{a,q_5},

so the acquired set of N_c relative to N_a is

Y_{N_a}(N_c)={a,q_5}.

Thus the union contributed by the two known neighbors is only {a,q_5}. The four complement vertices

q_1,q_2,q_3,q_4

remain uncovered. Again a single further Gamma-neighbor can acquire at most three vertices, so at least two further neighbors are necessary. Hence

deg_Gamma(N_a)>=4.

If equality holds, its two additional neighbors jointly acquire q_1,q_2,q_3,q_4.

## 3. Expansion at N_c

This is symmetric. The complement of N_c is

S_c=(Q-{q_5}) union {c}.

The acquired sets of the two known neighbors N_a and X have union {c,q_0}. Hence q_1,q_2,q_3,q_4 must be covered by at least two additional neighbors, and

deg_Gamma(N_c)>=4.

The same equality conclusion holds.

Therefore the singleton endpoint-exchange branch cannot terminate in a weak radius-three triangle: it forces a triangle all three of whose vertices are genuine degree-at-least-four expansion states. ∎
