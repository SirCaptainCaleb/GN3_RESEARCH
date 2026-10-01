# Near the seven-sixths floor, almost all vertices have a special subhypergraph confined to individual potential levels

## Statement

Let H be a finite linear 3-graph with φ(v)≥3 for all v. Define t_ns(v) as the number of nonspecial edges terminal at v, a(v)=2φ(v)-3-t_ns(v), and b(v)=2φ(v)-1-d_D^-(v). Call v Type A when (a(v),b(v))=(2,0). Every Type-A vertex v, writing p=φ(v), has exactly four incident special edges, all of rank p; every nonspecial edge terminal at v has rank at most p-1; and every nonspecial edge whose unique entrance is v is ascending. Thus every special edge whose vertices are Type A has equal vertex ranks, and every ascending arc entering a Type-A terminal raises vertex rank by at least two.

More quantitatively, write Σ_v φ(v)=m+(7/6)n+ηn with η>=0. There is W⊆V(H), with |W|≥(1-66η)n, such that: (i) all vertices of W are Type A; (ii) the hypergraph consisting of the original special edges contained in W has minimum degree at least two and maximum degree at most four; (iii) every component of this special subhypergraph lies in one vertex-rank level; and (iv) every originally nonspecial edge contained in W is ascending, with both terminals of vertex rank at least two greater than its entrance. All ranks and classifications here are evaluated in H, not recomputed after deletion. Also, at most 30ηn special edges meet a non-Type-A vertex.

## Body

First fix a Type-A vertex v and put p=φ(v). Its snake indegree is 2p-1 and its nonspecial terminal count is 2p-5. Subtraction gives exactly four special edges through v.

There is no nonspecial edge of rank p terminal at v: the incident capacity theorem a570ca900001 would give d_D^-(v)≤2p-3, contradicting 2p-1. Therefore every nonspecial terminal edge through v has rank at most p-1.

There must be such an edge of rank exactly p-1. Indeed t_ns(v)=2p-5≥1. For p=3, every nonspecial edge has rank at least two, so rank p-1=2 is forced. For p≥4, if all their ranks were at most p-2, the certified cumulative terminal bound 0e550ff0eadd would give t_ns(v)≤2p-7, a contradiction.

Apply a570ca900001 at q=p-1 to a rank-(p-1) nonspecial terminal edge. The set J_{p-1}(v) has size at most 2p-5 and already contains all 2p-5 nonspecial terminal edges. Consequently there is no special edge through v of rank at most p-1. Every special edge through v has rank at most φ(v)=p, so all four have rank exactly p. The stronger q=3 clause also shows that Type A cannot occur at p=4, although this is not needed below.

Let c(v) count ascending edges whose entrance is v. By the certified local source inequality 22362096041e,
d_H(v)-c(v)≤2p-1.
The 2p-1 snake-incoming edges are all counted on the left. A nonascending nonspecial edge with entrance v would be an additional edge counted there, which is impossible. Thus every nonspecial edge with entrance v is ascending.

If e is special and all its vertices are Type A, the preceding result gives φ(u)=φ(e) for every u∈e. If e has rank q, is ascending with entrance x, and has a Type-A terminal u, then φ(x)=q-1 while q≤φ(u)-1. Hence φ(u)≥φ(x)+2. This proves the local assertions.

Now assume the displayed global potential identity with eta>=0. Let E be the set of non-Type-A vertices and T its complement. By fa7e5e79b905, |E|≤6ηn. Put w(v)=a(v)/2+b(v). Directly counting special and nonspecial snake incidences gives
Σ_v w(v)=n+3ηn.
Since w(v)=1 on T, we have
Σ_{v∈E}w(v)=|E|+3ηn.

The number s_v of special edges through v is
s_v=d_D^-(v)-t_ns(v)=2+a(v)-b(v)=2+2w(v)-3b(v).
The ordinary snake bound gives b(v)≥0. Hence
Σ_{v∈E}s_v≤2|E|+2Σ_{v∈E}w(v)
             =4|E|+6ηn≤30ηn.
Let M be the number of special edges meeting E. Each contributes at least one to this sum, so M≤30ηn.

Keep the special edges wholly contained in T. Every vertex of T had special degree exactly four. Let L be the number of special incidences at T lost by deleting the edges meeting E. Each deleted edge has at most two vertices in T, so L≤2M≤60ηn. If N=|T|, the surviving special subhypergraph therefore has (4N-L)/3 edges and maximum degree at most four.

Repeatedly delete a vertex of current degree at most one, together with its incident edge if present. Suppose k vertices are deleted and W remains. This process deletes at most k edges. Thus its final edge count is at least (4N-L)/3-k. Maximum degree four gives an upper bound 4(N-k)/3. Comparing yields k≤L. Therefore
|W|=n-|E|-k≥n-|E|-L≥(1-66η)n.
The remaining special subhypergraph has minimum degree at least two if nonempty, and maximum degree at most four. All its vertices are Type A; each of its edges has equal vertex ranks, so each component lies in one rank level.

Finally, an originally nonspecial edge contained in W has a Type-A entrance and two Type-A terminals. It is ascending by the local source assertion, and each terminal is at least two rank levels above its entrance. This proves the global decomposition.

This theorem constrains the general near-equality configuration, rather than a fixed small path length. It does not by itself bound the number of ascending edges or change the leading Turán coefficient: the remaining issue is to control the ascending edges joining these level subhypergraphs.