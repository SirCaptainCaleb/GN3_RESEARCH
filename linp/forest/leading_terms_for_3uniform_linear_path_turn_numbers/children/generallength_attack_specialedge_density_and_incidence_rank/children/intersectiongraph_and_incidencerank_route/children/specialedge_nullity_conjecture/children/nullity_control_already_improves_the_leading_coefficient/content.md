# Constant-factor nullity control already improves the leading coefficient

## Statement

Let H be an n-vertex P_ell^(3)-free linear 3-graph with m edges, incidence matrix N, and s special edges. If nullity_R(N) <= C s + D n for constants C>0,D>=0 independent of ell, then m <= [C(2ell-3)+D+1]/(2C+1) * n. In particular the leading coefficient is 2C/(2C+1)<1.

## Body

Since rank(N)<=n, nullity(N)=m-rank(N)>=m-n. The assumed inequality gives m-n<=Cs+Dn, hence s>=(m-(D+1)n)/C. The certified special-edge hinge gives 2m+s<=(2ell-3)n. Substitution yields 2m+(m-(D+1)n)/C <= (2ell-3)n. Multiplying by C and rearranging gives (2C+1)m <= [C(2ell-3)+D+1]n. Thus any ell-independent constant-factor nullity control by special edges, even with an additive O(n) error, strictly improves the coefficient 1 in the Devine–Milans general bound. The sharp conjectural C=1,D=0 case gives m<=2(ell-1)n/3.