# Binary-projective diagonal tensor squares admit long coprime-orbit paths and stay below one third

## Statement

For every d>=3, let P_d=PG(d-1,2). Then P_d tensor P_d contains a linear path of length (2^d-1)(2^{d-1}-1)-1. If r=2^{d-1}-1 is the degree of P_d, the tensor square is 2r^2-regular and its normalized density at its first forbidden path length is less than 1/3. For d=4 this is the explicit 104-edge path in PG(3,2) tensor PG(3,2).

## Body

Identify the first F_2^d with F_{2^d} additively and the second with F_2 direct-sum F_{2^{d-1}}. Let M=2^d-1 and N=2^{d-1}-1, and choose multiplicative generators alpha,beta of orders M,N. Since gcd(M,N)=1, their paired motion has period MN.

For nonzero x,z put q_i=(alpha^i x,(1,beta^i z)), 0<=i<=MN-1, and d_i=q_{i-1}+q_i for 1<=i<=MN-1. The q_i are pairwise distinct, the d_i are pairwise distinct, and the q-set is disjoint from the d-set because the distinguished F_2 coordinate in the second factor is 1 for q_i and 0 for d_i. Thus E_i={q_{i-1},q_i,d_i} form a linear path of length MN-1.

Now r=N and the tensor square is 2r^2-regular, hence has density 2r^2/3. Since MN=(2r+1)r=2r^2+r, the first forbidden length is at least 2r^2+r and the normalized density is at most 2r/[3(2r+1)]<1/3. At d=4, M=15,N=7 and MN-1=104.
