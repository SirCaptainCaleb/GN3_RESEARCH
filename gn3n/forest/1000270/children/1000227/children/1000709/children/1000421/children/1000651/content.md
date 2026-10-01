# The commuting endpoint corner is isolated or forces a degree-five Gamma clique

## Statement

In the order-thirteen mu=6 minimal synchronized endpoint-exchange branch with no explicit order disagreement, the two opposite exchanges splice to a Hamiltonian six-set S. Either S is isolated in the Hamiltonian-support odd graph, or its deficient complement T joins the three endpoint-exchange deficient states X,N_a,N_c to form a K4 in Gamma, and all four vertices of this K4 have Gamma-degree at least five.

## Body

# The commuting endpoint corner is isolated or forces a degree-five Gamma clique

Work in the order-thirteen mu=6 shell. Assume the minimal synchronized endpoint-exchange branch of b27f4c1a9e63 and suppose no explicit relative-order disagreement occurs.

Thus there are distinct a,c in X and a Hamilton path Q=(q_0,...,q_5) such that

H-q_0 = (Q-{q_0}+{a}) | (X-{a}),
H-q_5 = (Q-{q_5}+{c}) | (X-{c})

at the support level, and the two replacement Hamilton paths preserve the inherited Q-order. By 70fa2fdc777c the six-set

S = Q-{q_0,q_5}+{a,c}

is Hamiltonian.

Put

T = V(H)-S.

Also put

N_a = (X-{a}) union {q_0},
N_c = (X-{c}) union {q_5}.

By 7ba4686e7ab5, X,N_a,N_c are deficient seven-supports and form a triangle in the radius-three deficient-support graph Gamma.

Then exactly one of the following holds.

1. S is isolated in the Hamiltonian-support odd graph. Equivalently T has no Hamiltonian six-vertex deletion.

2. T is deficient. In this case X,N_a,N_c,T form a K4 in Gamma, and every one of these four Gamma vertices has degree at least five.

## Proof

The first alternative is exactly the negation of T being deficient: an odd-graph neighbor of the Hamiltonian six-set S is a Hamiltonian six-subset of its seven-vertex complement T.

Assume therefore that T is deficient.

Write
B = X-{t,a,c}
for the four-vertex base supplied by the compatible-triangle conclusion of b27f4c1a9e63. Then

X   = B union {t,a,c},
N_a = B union {t,c,q_0},
N_c = B union {t,a,q_5},
T   = B union {t,q_0,q_5}.

Hence
d_J(X,N_a)=1,
d_J(X,N_c)=1,
d_J(N_a,N_c)=2,
d_J(X,T)=2,
d_J(N_a,T)=1,
d_J(N_c,T)=1.

All four supports are deficient, so every pair is adjacent in Gamma. Thus they form a K4.

It remains to prove the degree bounds. We use the neighborhood-capacity theorem e3f0da9ab087: for a deficient support R with Hamiltonian complement C, the acquired sets R' intersect C over Gamma-neighbors R' cover C, and each acquired set has order at most three.

At X the complementary Hamiltonian six-set is Q. The three known neighbors N_a,N_c,T acquire respectively

{q_0}, {q_5}, {q_0,q_5}.

Their union is only {q_0,q_5}. The four vertices q_1,q_2,q_3,q_4 remain uncovered. Since one further Gamma-neighbor can acquire at most three complement vertices, at least two further neighbors are required. Therefore deg_Gamma(X)>=5.

At N_a the Hamiltonian complement is

S_a=(Q-{q_0}) union {a}={a,q_1,q_2,q_3,q_4,q_5}.

The known neighbors X,N_c,T acquire respectively

{a}, {a,q_5}, {q_5}.

Again their union is only {a,q_5}, leaving q_1,q_2,q_3,q_4 uncovered. At least two further neighbors are required, so deg_Gamma(N_a)>=5.

The argument for N_c is symmetric.

Finally the Hamiltonian complement of T is

S={a,c,q_1,q_2,q_3,q_4}.

The known neighbors X,N_a,N_c acquire respectively

{a,c}, {c}, {a}.

Their union is {a,c}, leaving q_1,q_2,q_3,q_4 uncovered. Again at least two further neighbors are necessary. Hence deg_Gamma(T)>=5.

Thus a nonisolated commuting fourth Hamiltonian corner forces a four-clique of deficient states, each of Gamma-degree at least five. ∎
