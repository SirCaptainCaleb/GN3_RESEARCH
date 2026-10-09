# Central exterior-weight jump repairs odd nonlinear two-mark twists

Let n=2r>=6, k=(n-4)/2, and write x_i for the start bits in an arbitrary coordinate order p. Let K_i be the number of exterior one-bits in its i-th three-face window. Then K_(i+1)-K_i=1-x_i-x_(i+3).

CENTRAL JUMP LEMMA. There is a start with (K_1,...,K_(n-2))=(k,k,k+1,...,k+1).

PROOF. Impose x_2=x_5=0, x_4=1-x_1, and x_(i+3)=1-x_i for all i>=3. The displayed K-profile follows once K_1=k. Its initial exterior positions 4,...,n split into the three modulo-three chains C0=(6,9,...), C1=(4,7,...), C2=(5,8,...), of lengths L0,L1,L2 with sum 2k+1. The bits on C0 and C1 alternate with independent initial choices x_3,x_1, so each chain can contribute either floor(L_j/2) or ceil(L_j/2) ones. Chain C2 alternates beginning with zero, contributing floor(L2/2). An odd number of L0,L1,L2 is odd. If exactly one is odd, the lower choices give k ones. If all three are odd, the lower choices give k-1 ones and increasing either adjustable chain gives k. Thus K_1=k. QED.

SPIKE-REPAIR THEOREM. Let c(F,pi)=h(pi) XOR f(K(F)), where h is an arbitrary coordinate-triple label and f(k+1)=1 XOR f(k). If some order p has h-word (q,1 XOR q,q,...,q), then c has a full antipodal geodesic with exactly one change.

PROOF. Take the central-jump start. The f-word is (a,a,1 XOR a,...,1 XOR a), where a=f(k). Its XOR with the h-word is (q XOR a,1 XOR q XOR a,1 XOR q XOR a,...), with exactly one change. QED.

COROLLARY. For n even, partition directions A union M, |M|=2, and set h(a,b,d)=1 precisely if b lies in A and at least one of a,d lies in M. If f(n-3-t)=1 XOR f(t), then c(F,pi)=h(pi) XOR f(K(F)) is antipodal-reversal odd and has a one-change antipodal geodesic. Indeed h is reversal-even and antipodal complementation sends K to n-3-K; the order with both M directions first has h-word (0,1,0,...,0). Apply the theorem. This proves closure for every nonlinear antisymmetric exterior-Hamming-weight twist of the sharp two-mark unrestricted obstruction.
