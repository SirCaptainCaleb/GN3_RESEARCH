# Reversal-odd transition networks: shared encoding and terminal-support obstruction

- Stable ID: note_reversible_transition_networks_terminal_support_obstruction_20261011
- Author: unspecified; session provenance retained
- Primary home: article:nori_article_ix_unification
- Labels: structural_reduction, obstruction, proved
- Lifecycle: active
- Epistemic status: proved
- Current version: 4
- Retention: current and at most one previous snapshot
- Created session: session_nori_r6176_2
- Updated session: session_nori_r6202_2
- Disposition: none
- Successor: none

## Related references

- article:nori_article_ix_unification

## Research note

Let \(D=(S,A)\) be a finite digraph with an involution \(\tau:S\to S\) satisfying \((u,v)\in A\iff(\tau v,\tau u)\in A\). An arc coloring \(\gamma:A\to\mathbb F_2\) is **reversal-odd** when
\[
\gamma(\tau v,\tau u)=1-\gamma(u,v).
\tag{1}
\]

**Two complete encodings.** For an antipodally odd undirected edge coloring of \(Q_n\), take \(S=Q_n\), replace each edge by both directed arcs, let \(\tau x=\bar x\), and color either traversal of an edge by its underlying color. Then (1) is equivalent to edge antipodal oddness. Full cube geodesics are paths whose direction labels are all distinct; their endpoints are \(\tau\)-paired.

For an arbitrary ordinary boundary 3-tournament \(b\) on \(V\), take \(S=\{(a,b):a,b\in V,\ a\ne b\}\), with arcs \((a,b)\to(b,c)\) whenever \(a,b,c\) are pairwise distinct, let \(\tau(a,b)=(b,a)\), and set
\[
\gamma((a,b),(b,c))=b(a,b,c).
\tag{2}
\]
Then (1) is equivalent to \(b(c,b,a)=1-b(a,b,c)\). A state path
\((v_1,v_2)\to(v_2,v_3)\to\cdots\to(v_{m-1},v_m)\)
decodes to a tight path precisely when \(v_1,\ldots,v_m\) are pairwise distinct; its arc-color sequence equals the triple-color word.

**Splicing with terminal memory.** In any arc-colored digraph, concatenating monochromatic directed paths \(P:a\to z\) and \(Q:z\to d\) produces an 2-cp arc-colored path. For the boundary encoding, if both projected vertex words are simple and have only their common terminal ordered pair in common, concatenation produces a vertex-simple tight path with the same 2-cp color word. For the cube encoding, monochromatic geodesics from antipodal endpoints meeting at \(z\) concatenate (after reversing the second, which preserves undirected edge colors) into a full antipodal geodesic, because the two direction supports are complementary.

**Directional reachability.** Write \(R^\ell_{\rm out}(a)\) for states attainable from \(a\) by monochromatic directed paths of length \(\ell\), with either color permitted, and \(R^\ell_{\rm in}(a)\) for sources of monochromatic paths ending at \(a\). Equation (1) gives
\[
R^\ell_{\rm in}(\tau a)=\tau(R^\ell_{\rm out}(a)).
\tag{3}
\]
Thus an intersection \(R^p_{\rm out}(a)\cap R^q_{\rm in}(\tau a)\) yields an 2-cp directed walk from \(a\) to \(\tau a\), subject to the relevant support constraint.

**Obstruction to an antipodal-state extraction for tournaments.** If \(a=(u,v)\) in the boundary state graph, every directed state path from \(a\) to \(\tau a=(v,u)\) projects to a word beginning with \(u,v\) and ending with \(v,u\). This word repeats both \(u\) and \(v\), so it cannot be a vertex-simple tight path. Hence the common symmetry (1), even when coupled with an antipodal-state reachability intersection, cannot produce the desired tournament witness. A uniform theorem must allow terminal states that are not \(\tau\)-paired and must certify disjointness of projected vertex supports. This is the same support-memory requirement that is automatic for complementary cube geodesics.

**Oddness alone cannot guarantee long monochromatic paths.** Let \(S=U\sqcup W\), with both \(U\) and \(W\) even and nonempty, and let \(D\) be the bidirected complete bipartite graph between them. Choose a fixed-point-free involution separately on each of \(U\) and \(W\). Give every arc \(U\to W\) color \(0\) and every arc \(W\to U\) color \(1\). The involution is an arc anti-automorphism satisfying (1); \(D\) is strongly connected and can have arbitrarily high minimum outdegree. Nevertheless all directed paths of length two have one edge of each color. Therefore the common reversal-odd transition law is insufficient by itself for any long monochromatic-path conjecture.
