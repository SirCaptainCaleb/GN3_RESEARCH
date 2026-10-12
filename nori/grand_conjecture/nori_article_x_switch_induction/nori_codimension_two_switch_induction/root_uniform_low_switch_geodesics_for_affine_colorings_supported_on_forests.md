# Root-uniform low-switch geodesics for affine colorings supported on forests

# Root-uniform low-switch geodesics for affine colorings supported on forests

Let \(G\) be a simple graph on \([m]\), and let \(\varepsilon\in\mathbb F_2^m\). Color the undirected coordinate-\(i\) edges of \(Q_m\) by
\[
d_i(z)=\varepsilon_i\oplus\bigoplus_{j:ij\in E(G)}z_j. \tag{1}
\]
The formula is independent of \(z_i\). No antipodal condition is assumed on these face colorings.

**Lemma 1 (indegree parity in trees).** Let \(T\) be a tree, and prescribe \(b_v\in\mathbb F_2\) for each vertex. There is an orientation with \(\deg^-(v)\equiv b_v\pmod2\) at every vertex if and only if
\[
\bigoplus_{v\in V(T)}b_v=|E(T)|\pmod2. \tag{2}
\]
Each orientation of a tree is acyclic and thus is induced by some vertex ordering.

*Proof.* Summing indegrees proves necessity. For sufficiency, orient the edge at a leaf to realize its prescribed parity, remove the leaf, and adjust the target parity at its neighbor if that edge enters the neighbor. The parity identity persists, so induction applies. Any orientation of a tree has a topological ordering. \(\square\)

**Theorem 2 (rooted paths for a tree).** If \(G=T\) is a tree, then for every root \(x\in Q_m\) there is an antipodal spanning geodesic starting at \(x\) with at most one color change. For odd \(m\), a monochromatic path exists at every root. For even \(m\), set
\[
b_i=\varepsilon_i\oplus\bigoplus_{j:ij\in E(T)}x_j.
\]
A monochromatic path from \(x\) exists precisely when
\[
\bigoplus_i b_i=|E(T)|\pmod2. \tag{3}
\]
If (3) fails, a spanning path with its sole switch before the final edge exists.

*Proof.* Given an order \(\pi\) of the directions, orient every graph edge from its earlier to its later endpoint. The color traversed in direction \(i\) is \(b_i\oplus\deg^-_\pi(i)\pmod2\). To obtain the constant word \(\gamma^m\), apply Lemma 1 with indegree targets \(b_i\oplus\gamma\). This is possible if and only if
\[
\bigoplus_i b_i\oplus(m\gamma\bmod2)=|E(T)|\pmod2.
\]
For odd \(m\), choose \(\gamma\) accordingly; for even \(m\), this is (3). Necessity also follows because every graph edge contributes one to the parity sum of the traversed color word.

Now suppose \(m\) is even and (3) fails. Choose a leaf \(v\), set \(\gamma=b_v\), and delete \(v\). Prescribe indegree parity \(b_i\oplus\gamma\) on every vertex \(i\ne v\). The sum of these targets is
\[
\bigoplus_{i\ne v}(b_i\oplus\gamma)
=\bigoplus_i b_i
=|E(T)|\oplus1
=|E(T-v)|\pmod2.
\]
Lemma 1 supplies an orientation and a topological order of \(T-v\). Traverse these coordinates first, then \(v\). The first \(m-1\) edge colors all equal \(\gamma\). Since \(v\)'s unique neighbor has already been flipped, the final color is \(b_v\oplus1=1\oplus\gamma\). \(\square\)

**Theorem 3 (root-uniform two-switch bound for forests).** If \(G\) is a forest, then
\[
\boxed{\forall x\in Q_m\quad
\min_{P:x\to\bar x}\sigma_d(P)\le2.} \tag{4}
\]
If every component of \(G\) has odd order, the upper bound improves to one. The general bound two is sharp for prescribed roots.

*Proof.* Apply Theorem 2 to each tree component at the restriction of the prescribed root. Each component admits a spanning traversal whose word is \(0^*1^*\), \(1^*0^*\), or a constant word. Because (1) couples only coordinates within a component, these traversals may be interleaved while preserving their internal edge colors. Traverse all zero-prefixes of \(0^*1^*\) blocks first; then all one-suffixes of those blocks, all one-prefixes of \(1^*0^*\) blocks, and all constant-one blocks; finally all zero-suffixes of \(1^*0^*\) blocks and all constant-zero blocks. The resulting word has form \(0^*1^*0^*\) and at most two switches. When all components have odd order, choose monochromatic traversals by Theorem 2 and concatenate them according to color.

For sharpness let \(G\) consist of disjoint edges \(12\) and \(34\), with \(x=0000\) and \(\varepsilon=(1,1,0,0)\). The two local traversals necessarily have respective color words \(10\) and \(01\). A global traversal must contain both as subsequences, requiring at least two switches. \(\square\)

**Corollary 4 (unrestricted corresponding endpoints for two forest couplings).** Suppose \(d,e\) are two independent colorings of \(Q_m\) of the form (1), using potentially different forests and constants. Let \(E_s(d)\) be the set of terminals of spanning antipodal geodesics with at most \(s\) switches. Then
\[
\boxed{E_2(d)=E_2(e)=Q_m.} \tag{5}
\]
If one coupling graph is a tree, its rooted switch bound is one. Coordinate shifts in the two colorings are absorbed into the respective constants.

If \(d,e\) are restrictions of an antipodally odd coloring \(c\) of \(Q_{m+2}\) to adjacent parallel codimension-two faces, coordinate identification yields corresponding terminal vertices for paths with at most two switches. Article VIII's parallel-face bound therefore gives
\[
\boxed{\mu(c)\le2.} \tag{6}
\]

*Proof.* To realize a prescribed terminal \(y\), apply Theorem 3 at root \(\bar y\). Both forest colorings therefore admit paths with terminal \(y\). Apply the parallel-face switch bound. \(\square\)

**Corollary 5 (hereditary rooted closure).** For every face \(H\) of \(Q_m\), every vertex \(x\in H\) starts a geodesic spanning \(H\) with at most two switches under \(d|_H\). Indeed, fixing coordinates outside \(H\) changes only the constants in (1), and the induced graph on its free directions remains a forest. Apply Theorem 3 within \(H\).

This theorem includes arbitrary paths and branching trees as interaction graphs. For example, the four-coordinate path \(1-2-3-4\) gives \(d_1=\varepsilon_1\oplus z_2\), \(d_2=\varepsilon_2\oplus z_1\oplus z_3\), \(d_3=\varepsilon_3\oplus z_2\oplus z_4\), and \(d_4=\varepsilon_4\oplus z_3\), which is beyond disjoint block-radial couplings.
