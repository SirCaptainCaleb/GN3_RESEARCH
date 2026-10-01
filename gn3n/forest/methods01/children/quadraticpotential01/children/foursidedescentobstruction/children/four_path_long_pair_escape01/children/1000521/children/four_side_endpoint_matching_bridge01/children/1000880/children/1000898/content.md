# Two bad extensions force adjacency in both complementary endpoint-pair graphs

## Statement

Let H be any boundary tournament, let X be a Hamiltonian four-set, and let a,b be distinct exterior vertices such that X+a and X+b are non-Hamiltonian. Define K on X by yz in E(K) iff {a,b,y,z} is Hamiltonian, and define J on X by xy in E(J) iff {a,b} union (X-{x,y}) is Hamiltonian. Let tau send each two-subset A of X to its complementary two-subset X-A. Then E(J)=tau(E(K)), and tau is an automorphism of the line graph L(K_X). Consequently the induced intersection graphs L(K_X)[E(K)] and L(K_X)[E(J)] are isomorphic via tau: the number of selected pairs and every pairwise overlap/disjointness relation are preserved. The certified two-bad-extension theorem gives two adjacent edges in K, hence also in J. Equivalently, both direct and complementary pair parameterizations contain two overlapping Hamiltonian four-sets through {a,b}, and complementation preserves the entire pairwise incidence pattern among the selected pairs.

## Body

The certified two-bad-extension theorem gives two adjacent edges in K with no minimum-counterexample or extremality hypothesis. Let tau map each two-subset A of X to X-A. By definition, xy is an edge of J exactly when tau({x,y}) is an edge of K, so E(J)=tau(E(K)).

On a four-set, tau preserves incidence of two-subsets: two ordinary edges share one vertex exactly when their complementary edges share one vertex, and they are disjoint exactly when their complements are disjoint. Thus tau is an automorphism of the line graph L(K_X). Therefore tau restricts to an isomorphism between the induced intersection graphs L(K_X)[E(K)] and L(K_X)[E(J)]. In particular the number of selected pairs and every pairwise overlap/disjointness relation are preserved. This does not assert that K and J have the same ordinary degree sequence on X; complementation of pairs can interchange, for example, a three-edge star with a triangle.

Since K contains two adjacent edges, their tau-images are adjacent edges of J. This is the exact combinatorial mechanism behind the endpoint-pair complement parameterization and removes all route-specific hypotheses.
