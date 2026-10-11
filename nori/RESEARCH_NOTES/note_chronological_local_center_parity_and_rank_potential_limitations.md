# Chronological center-transitivity and parity synchronization limitations

- Stable ID: note_chronological_local_center_parity_and_rank_potential_limitations
- Author: unspecified; session provenance retained
- Primary home: subsection:endpoint_tournament_factorization_and_monochromatic_orders
- Labels: obstruction, partial_argument
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r4593_2
- Updated session: session_nori_r4593_2
- Disposition: none
- Successor: none

## Related references

- subsection:endpoint_tournament_factorization_and_monochromatic_orders, exact version 6

## Research note

Editorial extraction: precise original proof retained below.

Source: endpoint_tournament_factorization_and_monochromatic_orders composition v6

**First obstruction: transitivity really matters for prescribed chronology.** Take \(X=\{0,1,2\}\). Let \(T_1\) be the directed triangle \(0\to1\to2\to0\), and \(T_2\) its reversal. There is no ordering \(a,b,c\) of the three distinct vertices with \(a\to b\) in \(T_1\) and \(b\to c\) in \(T_2\): the latter would give \(c\to b\) in \(T_1\), but \(b\) has exactly one inneighbor in \(T_1\), namely \(a\). Thus a chronologically prescribed Hamilton path need not exist for arbitrary tournaments, even though ordinary transversal tournament-path results can freely permute the assignments of tournaments to edge positions.

**Second obstruction: transitive local centers still need not synchronize the two parities.** On \(V=\{0,1,2,3\}\), partition the six edges of \(K_4\) into its three perfect matchings:
\[
 M_0=\{\{0,3\},\{1,2\}\},\quad
 M_1=\{\{0,1\},\{2,3\}\},\quad
 M_2=\{\{0,2\},\{1,3\}\}.
\]
Give every edge in \(M_j\) weight \(j\), and for pairwise distinct \(a,b,c\) put
\[
 h(a,b,c)=\mathbf1_{\{w(ab)<w(bc)\}}.
\]
At each middle vertex \(b\), the three incident edge weights are \(0,1,2\) in some order. Hence \(T_b\) is transitive, and \(h(c,b,a)=1-h(a,b,c)\). For any vertex-simple spanning tight path \(p_1,p_2,p_3,p_4\), its first and last graph edges \(\{p_1,p_2\}\) and \(\{p_3,p_4\}\) are disjoint; they therefore belong to the **same** perfect matching and have the same weight. The two successive triple comparisons cannot both be increasing (or both decreasing). Indeed, since the middle edge shares a vertex with each outer edge, its matching is different, so the two triple colors are opposite for **every** spanning order. Thus this ordinary boundary 3-tournament has no monochromatic spanning tight path, despite all four local comparison tournaments being transitive. This example is even induced by a global edge weighting; ties occur only between disjoint edges and can be broken arbitrarily to obtain a strict edge order. Its direction-only physical cube realization is legal under antipodal-reversal oddness and fails the monochromatic *full* geodesic property in dimension four.

**Exact scope.** The rank-potential theorem settles the chronological path problem for transitive time-indexed tournaments and proves a valid half-window realization theorem. The \(K_4\) example blocks the inference from *separate* chronological solvability on the two parity classes to simultaneous spanning tight-path solvability, even for globally edge-ordered boundary tournaments. It does not challenge the established \(\Omega(\sqrt n)\) lower bound for ordinary boundary tournaments, the nearly-linear edge-ordered altitude bound, or the separate unrestricted NORI1 physical-edge conjecture. Any successful use of time-indexed orders for the full boundary problem needs a joint coupling mechanism stronger than the one-parity rank potential.
