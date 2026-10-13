# Parity covers and triangle-rich obstructions to local strengthenings

- Stable ID: note_nori_xiii_parity_cover_and_triangle_rich_obstructions
- Author: Article XIII independent investigation
- Primary home: article:nori_article_xiii_binary_involutive_rainbow_paths
- Labels: counterexample, minimum-color-degree, one-switch, involution, minimal-strengthening
- Lifecycle: active
- Epistemic status: open
- Current version: 3
- Retention: current and at most one previous snapshot
- Created session: session_nori_r7442_3
- Updated session: session_nori_r7442_3
- Disposition: none
- Successor: none

## Related references

- None

## Research note

# Two obstructions to elementary strengthenings of Article XIII

**Status.** The constructions below give proved counterexamples. The suggested compatibility question is exploratory; sufficiency and minimality are open.

**Proposition 1.** For every \(n\ge5\), a connected simple edge-colored graph exists with \(\widehat\delta=n-1\), a label-reversing involution \(\tau\), and \(L_1=3\), although every permutation of the \(n-2\) colors outside a specified ordered pair can be read on a simple rainbow path from any corresponding vertex.

**Proof.** Let \(V=\{(u,v,s):u,v\in[n],\,u\ne v,\,s\in\mathbb F_2\}\). For each distinct \(u,v,w\) and either \(s\), add the undirected edge
\[
e(u,v,w,s)=\{(u,v,s),(v,w,1-s)\},\quad
\lambda(e)=w,\quad\chi(e)=s.
\]
The representation of an edge is unique. Set \(\tau(u,v,s)=(v,u,s)\). Then \(\tau e(u,v,w,s)=e(w,v,u,1-s)\), hence \(\chi(\tau e)=1-\chi(e)\). At \((u,v,s)\), the \(n-2\) incident edges of binary label \(s\) have pairwise distinct ordinary colors \(w\notin\{u,v\}\), while the \(n-2\) edges of binary label \(1-s\) all have ordinary color \(v\). Therefore every vertex has degree \(2(n-2)\) and color degree \(n-1\). Every ordering of the remaining \(n-2\) colors yields a simple forward rainbow path; sheet values alternate. The ordered-pair transition graph is strongly connected for \(n\ge5\), and its three-transition triangle swaps sheets; thus the lifted graph is connected.

Two adjacent binary-\(0\) rainbow edges can meet only at a sheet-\(0\) vertex, while two adjacent binary-\(1\) rainbow edges can meet only at a sheet-\(1\) vertex. Constant-label rainbow runs therefore have length at most two. A four-edge path with at most one switch must have word \(0011\) or \(1100\). Such a word demands opposite sheets at positions \(1\) and \(3\), impossible in this bipartite graph. Hence \(L_1\le3\). For distinct \(t,u,v,w,z\), the path
\[
(u,v,1),(t,u,0),(u,w,1),(w,z,0)
\]
has ordinary colors \(v,w,z\), binary word \(001\), and length three. Thus \(L_1=3\).

The directed three-transition circuit
\((u,v)\to(v,w)\to(w,u)\to(u,v)\)
closes in the ordinary boundary-tournament ordered-pair graph, whereas its lift changes the sheet. This suggests investigating path compatibility along elementary closed walks. It does **not** establish a minimal or sufficient hypothesis.

**Proposition 2.** For every \(n\ge5\), there is also a connected graph with \(\widehat\delta=n\), the same type of binary-label-reversing involution, and \(L_1\le7\), **every edge of which lies in a triangle**.

**Proof.** Starting from the graph in Proposition 1, join every pair of distinct vertices sharing an old neighbor; give all these new edges a single new ordinary color \(\star\). Old edges connect opposite sheets, whereas new edges join vertices in the same sheet, so the graph remains simple. Each new edge lies in a triangle, and each old edge lies in a triangle by choosing another neighbor of one of its endpoints. Every vertex is incident with the new color, hence \(\widehat\delta=n\).

The new edge set is \(\tau\)-invariant. None of its edges is fixed by \(\tau\): if an edge \(\{x,\tau x\}\) were added, \(x=(u,v,s)\) and \(\tau x=(v,u,s)\) would have a common old neighbor. But the neighbors of \(x\) have ordered-pair forms \((v,w)\) or \((t,u)\), and those of \(\tau x\) have forms \((u,w)\) or \((t,v)\), with all indices in each transition distinct; the two neighbor sets are disjoint. Thus assign complementary binary labels to each new \(\tau\)-pair, retaining the old labels on old edges.

A rainbow path contains at most one edge of color \(\star\). Removing that edge leaves at most two old-edge paths; each has at most one binary switch and hence at most three edges by Proposition 1. Therefore \(L_1\le3+1+3=7\).

**Lesson.** Complete availability of ordered colors does not suffice. Even requiring every edge to belong to a triangle does not suffice. The still-open task is to isolate a weak, graph-theoretic condition on \((G,\lambda,\chi,\tau)\) that is satisfied by both NORI1 and boundary 3-tournaments, excludes these examples, and yields \(L_1\ge c\widehat\delta\). A state-graph or matroid presentation is not proposed as an axiom.

ADDITIONAL THEOREM (full S_n symmetry of the ordinary colors). For every permutation pi in S_n, the vertex map Phi_pi(u,v,s)=(pi(u),pi(v),s) is a graph automorphism of the parity-sheet graph of Proposition 1. It permutes the ordinary colors by pi, preserves the binary edge coloring, and commutes with tau(u,v,s)=(v,u,s). The sheet-flip nu(u,v,s)=(u,v,1-s) is a graph automorphism that preserves ordinary colors, globally complements the binary labels, and commutes with both tau and Phi_pi. The group generated by the Phi_pi and nu is vertex-transitive. Thus the previously proved graph with k=n-1, palette size n=k+1, a free parity-reversing vertex involution, and L_1=3 also admits the full symmetric group acting on its palette and a vertex-transitive group preserving chi up to global complement. Complete color symmetry and vertex transitivity cannot yield a linear one-switch bound.

**Square-space obstruction.** The binary edge labeling \(\chi\) on the old two-sheet graph has even sum on every four-cycle. Such cycles project to one of the two ordered-pair square patterns: four forward transitions give labels \(s,1-s,s,1-s\); alternating forward and backward transitions give four labels \(s\). Conversely, an ordered-pair directed triangle lifts to a six-cycle with edge-label word \(010101\), whose sum is odd. Thus its six-cycle lies outside the span of four-cycles. Since the old graph is bipartite, this also proves its cycle space is not generated by triangles and four-cycles. The added vertical matching closes precisely this kind of missing triangular relation.
