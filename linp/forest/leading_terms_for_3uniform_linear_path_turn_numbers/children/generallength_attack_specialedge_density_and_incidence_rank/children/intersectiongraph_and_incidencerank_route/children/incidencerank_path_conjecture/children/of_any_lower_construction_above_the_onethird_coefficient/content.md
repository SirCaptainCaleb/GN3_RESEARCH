# Necessary anatomy of any lower construction above the one-third coefficient

## Statement

Let ell>=2 and let H be an n-vertex, m-edge linear 3-graph with no P_ell and m/n>ell/3. Then: (i) n>=2ell+2; (ii) the average vertex degree is >ell, hence Delta(H)>=ell+1; (iii) every vertex cover has size tau(H)>2ell n/[3(n-1)], and therefore the matching number nu(H)>2ell n/[9(n-1)]; (iv) H has an induced subhypergraph H0 with density at least m/n and minimum degree delta(H0)>ell/3; and (v) H violates the incidence-rank path conjecture, since ell rank_R N <3m. Thus any genuine leading-coefficient lower-bound improvement must be simultaneously large, high-degree, large-transversal, large-matching, and rank-exceptional.

## Body


Because H is linear, every unordered pair of vertices lies in at most one hyperedge. Hence
  3m <= C(n,2),
so
  m/n <= (n-1)/6.
If m/n>ell/3, then n-1>2ell, giving n>=2ell+2.

The average vertex degree is 3m/n>ell, so Delta(H)>ell and therefore Delta(H)>=ell+1.

Let C be any vertex cover of size t. For each v in C, linearity gives d(v)<=floor((n-1)/2), because the pairs e\{v} over edges e containing v are pairwise disjoint subsets of V(H)\{v}. Counting every edge at least once through C,
  m <= sum_{v in C} d(v) <= t(n-1)/2.
Thus
  t >= 2m/(n-1) > 2ell n/[3(n-1)].
So tau(H) satisfies the stated lower bound. If M is a maximal matching of size nu, then the union of its 3nu vertices is a vertex cover; hence tau(H)<=3nu and
  nu(H)>=tau(H)/3>2ell n/[9(n-1)].

By the standard density-core peeling lemma ec94a7e47f72, H has a nonempty induced subhypergraph H0 with
  |E(H0)|/|V(H0)| >= m/n > ell/3
and
  delta(H0) >= |E(H0)|/|V(H0)| > ell/3.
Since P_ell-freeness and linearity are hereditary, H0 remains an admissible counterexample candidate.

Finally let N be the real vertex-edge incidence matrix of H. Always rank_R N<=n, so
  ell rank_R N <= ell n < 3m.
Therefore H violates the incidence-rank conjecture 6bea43f4bc16, which asserts ell rank_R N>=3m for every P_ell-free linear triple system.

These conclusions are necessary conditions only; they do not prove the one-third upper bound. Their role is to fence off low-transversal, hub-dominated, small-component, and rank-generic construction strategies for a >1/3 lower coefficient.
