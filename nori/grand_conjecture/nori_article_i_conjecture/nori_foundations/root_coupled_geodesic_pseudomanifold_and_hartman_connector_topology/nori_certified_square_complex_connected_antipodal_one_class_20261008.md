# Every NORI coloring yields a connected certified-square complex, degree n−1, and nonzero antipodal one-class

# Connected free antipodal complex of certified four-edge NORI connectors

Let \(n\ge5\) and let \(c\) assign bits to actual ordered three-faces of \(Q_n\); assume antipodal-reversal oddness \(c(\bar F,\operatorname{rev}\pi)=1\oplus c(F,\pi)\) only where stated. Recall the **certified-center square complex** \(X_c\) from Item \`nori_certified_center_square_complex_high_degree_eight_components_20261008\`. A physical two-face with free middle directions \(b,c\) lies in \(X_c\) when some genuine centered four-edge geodesic with direction order \((a,b,c,d)\) has its two actual ordered-three-face window colors equal; this certificate is invariant under toggling the center in \(b,c\). Its link \(M_z\) has an edge \(\{b,c\}\) for each certified square at \(z\). An *isolated direction* in \(M_z\) supports no certified square at \(z\).

**Theorem 1 (five-direction seven-cycle exclusion).** For **every binary ordered-three-face coloring**, even without antipodal oddness, \(M_z\) has at most **one isolated direction** at every cube vertex \(z\). Consequently the certified-center graph \(G_c=X_c^{(1)}\) has
\[
\boxed{\deg_{G_c}(z)\ge n-1\quad\text{for all }z,}
\tag{1}
\]
and has at most **two** connected components, each with at least \(2^{n-1}\) vertices.

**Proof.** Suppose two distinct directions \(i,j\) were isolated at \(z\). Choose three other distinct directions \(a,b,d\), possible because \(n\ge5\). For any ordered triple of distinct directions \(T=(u,v,w)\) write \(t(T)=c(F_z(T),T)\), where \(F_z(T)\) is the physical three-face through \(z\) free in the directions of \(T\). For any four distinct directions \((u,v,w,s)\) whose middle pair \(\{v,w\}\) meets \(\{i,j\}\), the centered four-edge path with these directions has unequal window colors: otherwise it would certify a square involving an isolated direction. Hence
\[
t(u,v,w)\ne t(v,w,s)\quad
\text{whenever }\{v,w\}\cap\{i,j\}\ne\varnothing.
\tag{2}
\]

Now consider the following **seven** ordered triples:
\[
(i,d,j),\ 
(d,j,a),\ 
(j,a,b),\ 
(i,j,a),\ 
(b,i,j),\ 
(a,b,i),\ 
(b,i,d).
\tag{3}
\]
Any two consecutive triples in this cyclic list are related by a shift \((u,v,w)\leftrightarrow(v,w,s)\) with four distinct involved directions, and in each case the common middle pair contains \(i\) or \(j\). For the reversed-direction comparisons, the same shift inequality is simply read backward. Equation (2) therefore says that all seven consecutive colors in the cyclic list (3), including the last and first, are different. A binary color sequence cannot alternate around an odd cycle. Contradiction. Thus at most one direction is isolated.

If a direction \(k\) is incident with any link edge \(\{k,l\}\in M_z\), the certified square contains the actual cube edge \(z\leftrightarrow z\oplus e_k\). Hence all but at most one coordinate edge at \(z\) lie in \(G_c\), proving (1).

For any subset \(S\subseteq Q_n\) of size \(s\), the standard elementary cube edge-isoperimetric inequality is \(|E(Q_n[S])|\le s\log_2(s)/2\). For a component \(C\) of \(G_c\), each vertex has at least \(n-1\) certified neighbors inside \(C\), hence \(s(n-1)/2\le |E(Q_n[C])|\le s\log_2(s)/2\), so \(s\ge2^{n-1}\). Since there are \(2^n\) vertices, there can be at most two components. \(\square\)

**Lemma 2 (connected middle-direction shift graph).** Fix any coordinate \(i\). Let \(H_i\) be the graph whose vertices are **all actual ordered three-faces with free direction \(i\)**, with edges joining consecutive ordered-three-face windows of a genuine centered four-edge geodesic whenever \(i\) belongs to the two **middle** directions of that four-edge direction order. Then \(H_i\) is connected for all \(n\ge5\).

**Proof.** Write \(W_z(a,i,b)\) for the actual ordered face containing physical vertex \(z\), with free directions ordered \((a,i,b)\), and similarly for all other orders. If \(a,b,d,h,i\) are five distinct directions, the two-edge walk
\[
W_z(a,i,b)\;-\;W_z(i,b,h)\;-\;W_z(d,i,b)
\tag{4}
\]
allows replacement of the first outer free direction \(a\mapsto d\). Both links are legal shift edges: they arise from centered direction orders \((a,i,b,h)\) and \((d,i,b,h)\). Likewise
\[
W_z(a,i,b)\;-\;W_z(h,a,i)\;-\;W_z(a,i,d)
\tag{5}
\]
replaces the second outer direction \(b\mapsto d\). Choosing the value of a newly fixed exterior bit by choosing \(z\) in the currently free direction, and correcting other exterior bits as below, shows that these replacements connect every ordered *type* \((a,i,b)\) to every other such type. Indeed the graph of injective two-letter words on \(n-1\ge4\) letters under single-letter replacements is connected.

For fixed \((a,i,b)\), any exterior bit \(k\notin\{a,i,b\}\) can be toggled by a **four-edge walk in \(H_i\)**. Choose a helper direction \(h\) distinct from \(a,i,b,k\) and a physical vertex \(z\) in the starting face. Then
\[
\begin{aligned}
W_z(a,i,b)&-W_z(i,b,h)-W_z(k,i,b)\\
&-W_{z\oplus e_k}(i,b,h)-W_{z\oplus e_k}(a,i,b).
\end{aligned}\tag{6}
\]
The middle face has free direction \(k\), so \(W_z(k,i,b)=W_{z\oplus e_k}(k,i,b)\) is *literally the same vertex of \(H_i\)*. All other displayed consecutive pairs are legal four-distinct-direction centered shifts. The last face is the first ordered triple at the physical position with exactly the exterior \(k\)-bit flipped. Repeating (6) gives arbitrary exterior assignments. Thus every ordered face with \(i\) in the middle position lies in one connected component. Every ordered face with \(i\) at either end is adjacent to a face with \(i\) in the middle (choose a fourth distinct direction). Consequently all vertices of \(H_i\) are connected. \(\square\)

**Theorem 3 (antipodal oddness forbids globally missing directions).** Suppose \(c(\bar F,\operatorname{rev}\pi)=1\oplus c(F,\pi)\). Then for **each** cube coordinate direction \(i\), *somewhere* in the cube there is a monochromatic centered four-edge connector with \(i\) in its middle pair. Equivalently, \(G_c\) contains an actual cube edge in every coordinate direction.

**Proof.** Suppose instead every edge of \(H_i\) connects faces with *unequal* colors. On an ordered triple containing \(i\), let \(s_i=1\) when \(i\) occupies the **middle** of its three ordered positions, and \(s_i=0\) when \(i\) occupies either outer position. Every allowed shift edge of \(H_i\) changes \(s_i\), so \(s_i\) is a proper bipartition of \(H_i\). Since \(H_i\) is connected by Lemma 2, the only binary proper colorings of its vertices are \(s_i\) and \(1\oplus s_i\). Thus for some constant \(\varepsilon\), the actual face color is \(c(F,\pi)=s_i(\pi)\oplus\varepsilon\) on the entire \(H_i\).

But antipodal-reversal involution sends the position of \(i\) from \(1\) to \(3\), from \(2\) to \(2\), or from \(3\) to \(1\). In all cases \(s_i(\operatorname{rev}\pi)=s_i(\pi)\), so this formula gives \(c(\bar F,\operatorname{rev}\pi)=c(F,\pi)\), contradicting the odd law. Therefore some shift edge in \(H_i\) has **equal** colors and certifies an \(i\)-middle square. \(\square\)

**Theorem 4 (global connectedness and the nonzero antipodal one-class).** For every active NORI coloring and every \(n\ge5\), its genuine certified-center square complex \(X_c\) is **connected**, and physical antipodal complementation acts freely on \(|X_c|\). Consequently its quotient double cover is connected and nontrivial:
\[
\boxed{0\ne w_1(X_c\longrightarrow X_c/\tau)\in H^1(X_c/\tau;\mathbb F_2).}
\tag{7}
\]
Equivalently, a path composed entirely of **certified center-move cube edges** connects every physical vertex \(z\) to its antipode \(\bar z\).

**Proof.** Theorem 1 gives at most two components. If there were exactly two, each would have exactly \(2^{n-1}\) vertices, and all \(n-1\) certified neighbors of each vertex would remain in its component. Equality holds in the cube edge-isoperimetric bound for each component. Its elementary induction (splitting into the two values of one coordinate and using the strictness of the binary-entropy inequality away from \(0,\frac12,1\)) shows that equality sets of size \(2^{n-1}\) are exactly coordinate \((n-1)\)-faces. Hence the two components must be the two opposite facets perpendicular to *one fixed direction* \(i\), and **no cube edge in direction \(i\)** could be certified anywhere. That contradicts Theorem 3. Thus \(G_c\), and hence \(X_c\), is connected.

Antipodal complementation preserves centered-monochromatic certification by the NORI odd law and has no fixed point in a cubical complex of dimension at most two for \(n\ge5\): its sole fixed point in the ambient geometric \(n\)-cube is the all-\(\tfrac12\) center. So the quotient is a genuine connected two-sheeted covering. A connected double cover cannot have a global section (otherwise it would be two disjoint copies of the base); its class \(w_1\) is therefore nonzero. Connectivity also gives a certified-edge path between any \(z,\bar z\). \(\square\)

**Mathematical significance and remaining obstruction.** This upgrades the earlier \(n-3\) degree and eight-component bounds to **\(n-1\) and complete connectedness**, and yields an unconditional nonzero free-antipodal first cohomology class on a **path-certified** complex for every \(n\ge5\). It is a genuine topological foothold that cannot be obtained from arbitrary dense square subcomplexes such as the no-go example. Nevertheless a certified-edge path between antipodes is not necessarily *one color-coherent geodesic*, and \(w_1\ne0\) does not imply \(w_1^2\ne0\). To close NORI one must transport this nonzero class into an actual root/terminal-memory reachability interface with a valid higher-dimensional cup product or force the exact same-root complementary-support collision (or a nonbipartite cap-memory graph).

## Elevation: classification of the only possible disconnected case (without antipodal oddness)

The preceding connectivity proof admits an exact converse for **arbitrary** binary ordered-three-face colorings, with no antipodal axiom.

**Theorem 5 (sharp disconnection classification).** For \(n\ge5\), the genuine certified-center graph \(G_c\) is disconnected **if and only if** there exist a direction \(i\) and one bit \(\varepsilon\) such that on **every ordered three-face having free direction \(i\)**,
\[
\boxed{c(F,\pi)=\varepsilon\oplus\mathbf1_{\{\text{\(i\) is the middle direction of }\pi\}}.}
\tag{8}
\]
When this happens, \(G_c\) has **exactly two components**, namely the two full opposite \((n-1)\)-dimensional cube facets perpendicular to direction \(i\); every edge inside either facet is certified. The values on ordered faces *not containing* \(i\) need not be restricted by (8).

**Proof.** If \(G_c\) is disconnected, Theorem 1 forces exactly two components of size \(2^{n-1}\). The equality case of edge isoperimetry used in Theorem 4 says they are opposite coordinate facets separated by some direction \(i\). Then no certified square has \(i\) in its middle pair, or it would contain an edge crossing those facets. Thus **every** edge of the entire connected shift graph \(H_i\) joins faces of unequal colors. By Lemma 2, its unique bipartition up to color inversion is precisely \(s_i(\pi)=\mathbf1_{\{\mathrm{position}_\pi(i)=2\}}\). Hence the restriction of \(c\) to all ordered faces containing \(i\) is \(s_i\oplus\varepsilon\), proving necessity.

Conversely suppose (8) holds. Every centered four-connector with \(i\) as a middle direction has two window colors differing by exactly one, because the positional indicator \(s_i\) flips along the shift. Thus no square with \(i\) among its middle directions is certified, and no \(i\)-direction cube edge lies in \(G_c\). But Theorem 1 guarantees each vertex at least \(n-1\) distinct certified coordinate-edge neighbors. All \(n-1\) other directions must therefore be present, making \(G_c\) exactly the disjoint union of the two full opposite coordinate facets. \(\square\)

**Sharpness and the antipodal obstruction.** To realize disconnection without NORI oddness, choose \(c(F,\pi)=s_i(\pi)\) whenever \(i\) is free and assign, for example, zero to other triples. Its square complex is exactly two opposite \((n-1)\)-cube facets. Under reversal of a triple, the predicate \(s_i\) is unchanged, so (8) is intrinsically **reversal-even** on its complete \(i\)-free face class. Antipodal-reversal **odd** NORI excludes it. This yields an exact local-to-global topological dichotomy, not merely a degree bound.
