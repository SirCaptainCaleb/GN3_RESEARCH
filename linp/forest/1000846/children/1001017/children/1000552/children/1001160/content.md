# Snake indegree lemma

## Statement

Let G be a linear r-graph with snake digraph D. For every vertex v, d_D^-(v) <= (phi(v)-1)(r-1)+1. Moreover, if e contains v and phi(e,v) >= phi(f) for every other edge f containing v, then d_G(v) <= (phi(e,v)-1)(r-1)+1.

## Body

Ported from the supplied Devine–Milans source linear_paths.tex. Proof. Let e be an incoming snake edge at v maximizing phi(e,v), and let P be a maximum path ending with e at v. Every other incoming edge f at v must meet V(P) outside e; otherwise f can be appended to P, contradicting maximality of phi(e,v). By linearity these witness vertices are distinct. Thus if k=d_D^-(v), then |V(P)| >= (k-1)+r, while |V(P)| <= phi(v)(r-1)+1, giving k <= (phi(v)-1)(r-1)+1. The second assertion is the same argument with every edge at v in place of every incoming snake edge.