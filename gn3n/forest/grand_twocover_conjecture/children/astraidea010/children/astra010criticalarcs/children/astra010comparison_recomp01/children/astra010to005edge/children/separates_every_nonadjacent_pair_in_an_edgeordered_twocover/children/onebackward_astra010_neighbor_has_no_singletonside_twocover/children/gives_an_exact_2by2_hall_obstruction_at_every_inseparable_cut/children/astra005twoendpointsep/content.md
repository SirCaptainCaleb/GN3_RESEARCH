# A two-vertex companion cannot lock both endpoints of the other path

## Statement

Let G be an edge-orderable boundary tournament with a spanning two-cover A|B, where A=(a_0,...,a_m) is increasing with m>=1 and V(B)={x,y}. Then the distinct endpoints a_0 and a_m are separable by a spanning two-cover of G. Equivalently, an inseparable pair on A cannot consist of both endpoints of A.

## Body

Assume for contradiction that a_0 and a_m are inseparable. Use the Hall sets L_k,R_k from 522bc40f56d4 for every cut k=0,...,m-1.

If m=1, then at the unique cut both formal endpoint conventions apply: L_0=R_0={x,y}. This contains a distinct-label choice, contradicting 522bc40f56d4.

Assume m>=2. At the first cut, the incoming edge is formal -infinity, so L_0={x,y}. The Hall obstruction therefore forces R_0=empty.

We propagate this emptiness. Fix k with 1<=k<=m-1 and suppose R_{k-1}=empty. Write e_{k-1}=a_{k-1}a_k and e_k=a_ka_{k+1}; because A is increasing, e_{k-1}<e_k. For z in {x,y}, the condition z notin R_{k-1} says a_kz is not less than e_k. By strict totality of the edge order, e_k<a_kz, and hence e_{k-1}<a_kz. Thus z belongs to L_k. Therefore L_k={x,y}, and the Hall obstruction at cut k forces R_k=empty.

Induction gives R_{m-1}=empty. But at the final cut the outgoing edge is formal +infinity, so by definition R_{m-1}={x,y}, a contradiction.

Hence a_0 and a_m are separable. ∎