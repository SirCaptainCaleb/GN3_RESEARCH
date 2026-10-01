# A locally minimal four-side yields endpoint-grid disagreement, a Hamiltonian endpoint four-set, or four triple enlargements

## Statement

Let H be a minimum counterexample and let W|P|Q be a spanning three-cover minimizing quadratic potential within its connected pairwise-repartition component, with |W|=4 and |P|,|Q|>=6. Let E be the four displayed endpoints of P and Q. Then at least one of the following holds: (1) for some w in W, two Hamilton paths chosen on pair-extension five-sets (W-{w}) union {e,f}, {e,f} subset E, induce different relative orders on their common vertices; (2) H[E] is Hamiltonian; (3) for every w in W there exists a three-set T_w subset E such that H[(W-{w}) union T_w] is Hamiltonian. In outcomes (2) and (3), every displayed Hamiltonian support is proper and therefore has non-Hamiltonian path-cover-two complement.

## Body

By local_four_complete_endpoint_pair_grid01, for every w in W and every pair {e,f} subset E the five-set D_w union {e,f}, where D_w=W-{w}, is Hamiltonian. Fix w and choose one Hamilton path on each of these six pair-extension supports. Apply e48e2aaaf481 with core K=D_w and exterior set E. It yields one of three alternatives: two chosen pair-extension paths disagree in relative order on their common vertices; some triple T subset E makes D_w union T Hamiltonian; or E itself is Hamiltonian.

If the first alternative occurs for any w, outcome (1) holds. If E is Hamiltonian for any w, that conclusion is independent of w and gives outcome (2). Otherwise, for every w the only remaining alternative is a triple T_w subset E with D_w union T_w Hamiltonian, giving outcome (3).

Every support in (2) has order four and every support in (3) has order six. Since |H|>=16, all are proper. Minimum-counterexample calculus gives path-cover number at most two for each complement; the complement cannot be Hamiltonian, since together with the displayed Hamiltonian support that would give a spanning two-cover of H. Thus each complement is non-Hamiltonian with path-cover number two.