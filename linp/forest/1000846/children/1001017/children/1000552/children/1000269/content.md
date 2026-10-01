# Chosen maximum endpoint paths give global double-blocker compensation

## Statement

Let H be an n-vertex P_ell^(3)-free linear 3-graph with m edges, snake digraph D, and s special edges. For each vertex v choose a maximum phi(v)-edge path P_v ending at v, and let h_v be its last edge. Let B_v be the number of snake-incoming incidences (f,v) with f!=h_v such that both vertices of f minus {v} lie in V(P_v) minus h_v. Put B=sum_v B_v. Then d_D^-(v)+B_v<=2phi(v)-1 for every v, and consequently 2m+s+B <= (2ell-3)n.

## Body

Fix v and write p=phi(v). If f is snake-incoming at v and f!=h_v, then f must meet V(P_v) outside h_v. Indeed, if f met P_v only at v, appending f to P_v would give a (p+1)-edge path ending in f at v, so phi(f,v)>=p+1; but incomingness gives phi(f,v)=phi(f), contradicting phi(f)<=phi(v)=p because every path ending in f at v is also a path ending at v. By linearity, as f ranges over the snake-incoming edges distinct from h_v, the sets (f minus {v}) intersect V(P_v) minus h_v in pairwise disjoint vertices. Each such incidence therefore consumes at least one of the 2p-2 vertices of V(P_v) minus h_v, and each incidence counted by B_v consumes one additional vertex. If h_v itself is snake-incoming, there are d_D^-(v)-1 other incidences, giving (d_D^-(v)-1)+B_v<=2p-2. If h_v is not incoming, all d_D^-(v) incidences are distinct from h_v, giving the stronger d_D^-(v)+B_v<=2p-2. In either case d_D^-(v)+B_v<=2p-1. Since H is P_ell-free, p<=ell-1, so the right side is at most 2ell-3. Summing over v gives |E(D)|+B<=(2ell-3)n. Finally |E(D)|=2m+s because each nonspecial edge contributes two snake incidences and each special edge contributes three.
