# Astra 008 is exactly a nonnegative complementary-pair determinant

## Statement

Let H have n vertices and k=floor(n/2). For a uniformly random k-set S, classify S by the two indicators X=1[H[S] is Hamiltonian] and Y=1[H[V(H)-S] is Hamiltonian]. Let N_ij be the number of k-sets with (X,Y)=(i,j). Then Astra idea 008 is equivalent exactly to
N_11 N_00 >= N_10 N_01.
If n is even, complementation gives N_10=N_01, so the condition becomes
N_11 N_00 >= N_10^2.
In particular, for even n, if there is any mixed complementary pair then Astra 008 requires both a good-good complementary pair and a bad-bad complementary pair.

## Body

Put N=binom(n,k)=N_11+N_10+N_01+N_00. The proposed positive-correlation inequality is
N_11/N >= ((N_11+N_10)/N)((N_11+N_01)/N).
Multiplying by N^2 and expanding gives
N_11(N_11+N_10+N_01+N_00) >= (N_11+N_10)(N_11+N_01),
which cancels to
N_11 N_00 >= N_10 N_01.
Thus the conjecture is exactly nonnegativity of the determinant of the 2-by-2 complementary Hamiltonicity table.

When n is even, complementation is an involution on k-sets and interchanges the types 10 and 01, hence N_10=N_01. The determinant inequality becomes N_11 N_00 >= N_10^2. Therefore N_10>0 forces both N_11>0 and N_00>0. Equivalently, the presence of even one complementary pair with exactly one Hamiltonian side forces, under Astra 008, the simultaneous existence of a complementary pair with both sides Hamiltonian and another with neither side Hamiltonian. ∎
