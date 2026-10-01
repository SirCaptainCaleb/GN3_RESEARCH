# Cumulative snake-rank indegree bound

## Statement

Let G be a linear r-uniform hypergraph with snake digraph D. Fix v and q>=1, and let I_q(v)={e : (e,v) is an incoming snake incidence and phi(e,v)<=q}. Then |I_q(v)| <= (q-1)(r-1)+1. In particular, for r=3, |I_q(v)|<=2q-1.

## Body

Proof. If I_q(v) is empty there is nothing to prove. Choose e in I_q(v) maximizing t=phi(e,v), and let P be a t-edge linear path witnessing phi(e,v), ending with e at v. For every other f in I_q(v), f must meet V(P) outside e. Otherwise, since f and e already share v and G is linear, f is disjoint from every other vertex of P and can be appended to P, producing a (t+1)-edge path ending with f at v, contradicting phi(f,v)<=t. Choose one witness x_f in f∩(V(P)\e). Distinct f give distinct witnesses because two such edges both contain v, so sharing x_f would make them intersect in two vertices. Thus |I_q(v)|-1 <= |V(P)\e|=(t-1)(r-1)<=(q-1)(r-1). This controls the entire low-rank cumulative distribution even if higher-rank incoming incidences at v also exist.
