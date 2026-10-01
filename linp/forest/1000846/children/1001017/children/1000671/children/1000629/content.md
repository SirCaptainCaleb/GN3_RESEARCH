# Terminal-pair cycle-rank reduction

## Statement

Let H be an n-vertex P_ell^(3)-free linear 3-graph with m edges, s special edges, and b=m-s nonspecial edges. For each nonspecial edge e with unique entrance u(e), put the terminal pair e\{u(e)} as an edge of a simple graph T. If the cycle rank beta(T)=|E(T)|-|V(T)|+c(T) satisfies beta(T)<=C s+D n for constants C,D>=0 independent of ell, then m <= [2(C+1)ell-3(C+1)+D+1]/(2C+3) * n. Hence every fixed C,D gives leading coefficient 2(C+1)/(2C+3)<1.

## Body

Proof. Distinct nonspecial triples give distinct terminal pairs by linearity, so T is simple and |E(T)|=b. Writing v_T=|V(T)| and c(T) for the number of nonempty connected components, b=v_T-c(T)+beta(T)<=n+beta(T). Thus b<=C s+(D+1)n. Since m=b+s, we obtain m<=(C+1)s+(D+1)n, hence s>=(m-(D+1)n)/(C+1) when C+1>0. The certified special-edge hinge gives 2m+s<=(2ell-3)n. Substitution yields 2m+(m-(D+1)n)/(C+1)<=(2ell-3)n. Multiplying by C+1 and rearranging gives (2C+3)m<=[(C+1)(2ell-3)+D+1]n, as claimed. For C=1,D=0 this becomes m<=(4ell-5)n/5.
