# Ternary Hamming turn conservation and linear paths

Let \(G=H(k,3)=K_3^{\square k}\), \(k\ge1\), with canonical edge-resource matroid \(N=N_{\mathrm{sp}}(G)\cong\bigoplus_{j=1}^kM(K_3)\). Let \(c:E(G)\to\mathbb F_2\) and let \(b(u,v,w)\) label ordered two-edge turns under the intrinsic rules
\[
b(u,v,w)+b(w,v,u)=\mathbf1_{\{uw\in E(G)\}}\pmod2,\qquad
b(u,v,w)=c(uv)+c(vw)\quad\text{if }uw\notin E(G).\tag{1}
\]
A path is **accepted** if all internal \(b\)-turns are zero and its edge resources are independent in \(N\).

A **coordinate triangle** arises by fixing all but one coordinate. If its three edges are monochromatic, its three unoriented two-edge walks have one accepted orientation apiece. These orientations induce a tournament on their endpoint pairs. Call the triangle **defective** if this tournament is transitive; let \(B\) be the total number of defective coordinate triangles.

**Theorem (ternary turn conservation).** There exists an accepted monochromatic \(N\)-independent path of length
\[
\boxed{\ell\ge\left\lceil k-\frac{B}{2\cdot3^k}\right\rceil\ge\left\lceil\frac{5k}{6}\right\rceil.}\tag{2}
\]
Consequently the Hamming-root factor-count conjecture \(\ell\ge k\) holds for all \(k\le5\); it also holds for arbitrary \(k\) whenever no coordinate triangle is defective. In particular, it holds whenever every coordinate triangle is bichromatic.

*Proof.* Let \(F\) be any subgraph of a coordinate \(K_3\) whose edges have one fixed color. Let \(D_F(u,v)\) denote the greatest length of an accepted simple \(u\)-to-\(v\) path within \(F\), taking \(D_F(u,u)=0\) and \(-\infty\) for unreachable pairs. Every single edge is accepted. Put \(\delta(F)=1\) if \(F=K_3\) and its accepted two-step endpoint tournament is transitive; put \(\delta(F)=0\) otherwise.

**Local permutation lemma.** There exists a permutation \(\pi\) of the three vertices of \(F\), using only reachable source-target pairs, for which
\[
\sum_v D_F(\pi(v),v)\ge 2|E(F)|-\delta(F).\tag{3}
\]
For zero edges choose the identity; for one edge transpose its endpoints to obtain total length two. For two edges \(F=a-b-c\), reversal oddness on its triangular turn accepts one of \(a-b-c\), \(c-b-a\). If the former is accepted, use the cyclic source-target assignment \(a\to c,\ c\to b,\ b\to a\), giving total length \(2+1+1=4\); reverse it in the other case. For three edges, each ordered pair has a direct path of length one, and one orientation of each two-edge path is accepted. These longer path orientations constitute a tournament on three vertices. Its cyclic case admits a cyclic permutation with three length-two paths, total six. Its transitive case admits a cyclic permutation with two forward arcs of length two and one reverse arc of length one, total five. This establishes (3).

For any real weight function \(w\) on the three vertices, put \(T_F(w)(v)=\max_u\{w(u)+D_F(u,v)\}\). The permutation lemma implies
\[
\sum_v T_F(w)(v)\ge\sum_v w(v)+2|E(F)|-\delta(F),\tag{4}
\]
because \(\sum_vw(\pi(v))=\sum_vw(v)\).

Now choose one edge color \(s\). Process coordinates in order \(1,\ldots,k\), and define \(L_j(x)\) as the largest length of a color-\(s\) accepted path ending at \(x\), whose coordinate indices are nondecreasing and whose successive moves within one coordinate visit distinct symbols. Set \(L_0(x)=0\). For each \(j\)-coordinate triangle fiber, with color-\(s\) edge subgraph \(F\), the dynamic-programming recurrence is
\[
L_j(v)=\max_u\{L_{j-1}(u)+D_F(u,v)\}.\tag{5}
\]
The concatenated path is accepted: turns internal to one coordinate segment are accepted by definition of \(D_F\); turns joining different factors have nonadjacent outer vertices, and their label is \(s+s=0\) by (1). Its edge-resource family is independent because within each coordinate factor it is a simple path in the root \(K_3\), hence a forest in the corresponding direct-sum factor \(M(K_3)\). Nondecreasing factor order also makes the full vertex path simple.

Apply (4) to weights \(L_{j-1}\) in every fiber of coordinate \(j\), and sum over the \(3^{k-1}\) fibers. Then
\[
\sum_{x\in V(G)}L_j(x)\ge\sum_xL_{j-1}(x)+2|E_s^{(j)}|-B_s^{(j)},
\]
where \(E_s^{(j)}\) comprises the color-\(s\) edges of the \(j\)-factor and \(B_s^{(j)}\) its defective monochromatic triangles. Summing across coordinates gives
\[
\sum_x L_k^{(s)}(x)\ge 2|E_s|-B_s.\tag{6}
\]
Summing (6) over the two colors gives
\[
\sum_x\bigl(L_k^{(0)}(x)+L_k^{(1)}(x)\bigr)
\ge 2|E(G)|-B=2k3^k-B.
\]
Thus some color and some terminal vertex satisfy
\[
L_k^{(s)}(x)\ge k-\frac B{2\cdot3^k}.
\]
There are \(k3^{k-1}\) coordinate triangles, so \(B\le k3^{k-1}\), and (2) follows. For \(k\le5\), \(\lceil5k/6\rceil=k\); if \(B=0\), the first inequality gives \(\ell\ge k\). \(\square\)

**Interpretation.** The local weighted transfer contribution equals \(2|E(F)|\) except for a transitive monochromatic coordinate triangle, which can lose one unit. Every other fiber, including a bichromatic triangle, conserves the full weighted transfer budget. This gives the first linear-in-\(k\) bound for arbitrary polarized ternary Hamming systems, establishes the full factor-count guarantee in dimensions \(k\le5\), and reduces the unrestricted ternary gap to controlling global compensation for transitive monochromatic triangles. The binary endpoint remains the NORI1 antipodal spanning problem.

**Corollary (critical six-factor rigidity).** If a triangular-turn system on \(H(6,3)\) has no accepted monochromatic resource-independent path of length six, then (i) all \(6\cdot3^5=2\cdot3^6\) coordinate triangles are defective, hence monochromatic with transitive accepted-turn tournaments; (ii) there are \(3^6\) defective triangles of each color; and (iii) for every permutation \(\sigma\) of the six factor indices, each color \(s\), and each terminal vertex \(x\), the longest accepted color-\(s\) path whose coordinate segments occur in order \(\sigma\) and do not revisit a symbol within one segment has length five.

*Proof.* Put \(V=3^6\). The bound (2) forces \(B\ge2V\) if no length-six path exists, while the total number of coordinate triangles equals \(2V\). Thus every coordinate triangle is defective. Let \(B_s\) count the defective triangles of color \(s\). Every edge of color \(s\) lies in one of these monochromatic coordinate triangles, so \(|E_s|=3B_s\). The transfer inequality (6) gives
\[
\sum_x L_6^{(s)}(x)\ge2|E_s|-B_s=5B_s.
\]
Since every terminal length is at most five, the sum is at most \(5V\), hence \(B_s\le V\). As \(B_0+B_1=2V\), equality holds: \(B_0=B_1=V\). Therefore \(\sum_xL_6^{(s)}(x)\ge5V\) while each summand is at most five, so every \(L_6^{(s)}(x)=5\). The dynamic-programming proof is invariant under permutations of the coordinate order, giving the terminal conclusion for every \(\sigma\). \(\square\)

This isolates the equality case: a perfectly balanced system of transitive monochromatic coordinate triangles with flat five-edge terminal profiles under all \(6!\) factor orders.

**Lemma (forced predecessor profile in the critical case).** In the hypothetical six-factor counterexample of the preceding corollary, fix any order of factors, its final factor \(j\), and a coordinate-\(j\) fiber. If the fiber is monochromatic in color \(s\), then the three values of \(L_5^{(s)}\) just before processing that fiber are, in some order,
\[
\boxed{(3,3,4),}\tag{7}
\]
with the value four located at the sink of the fiber's accepted two-step endpoint tournament. For the other color, whose fiber edge subgraph is empty, all three predecessor values are five.

*Proof.* By the corollary, for both colors and every terminal vertex, \(L_6^{(s)}=5\). Equality also holds in every summed local transfer inequality (4): the two colors' total transfer lower bounds sum to the maximum possible \(10\cdot3^6\), and each of their terminal outputs is at most five. Thus on a defective color-\(s\) triangle, with input weights \(w\), the transfer output \(T_F(w)\) is the constant vector \((5,5,5)\) and \(\sum w=10\).

Relabel the triangle so its accepted length-two endpoint tournament is transitive \(a\to b\), \(a\to c\), \(b\to c\). Every direct edge has length one; the accepted length-two arcs have length two. Therefore
\[
T_F(w)(a)=\max\{w_a,w_b+1,w_c+1\},\quad
T_F(w)(b)=\max\{w_b,w_a+2,w_c+1\},\quad
T_F(w)(c)=\max\{w_c,w_a+2,w_b+2\}.
\]
To reach output five at \(a\), some predecessor other than \(a\) must have weight four (the possibility \(w_a=5\) would force the output at \(b\) to be at least seven). Weight four at \(b\) would force output at \(c\) to be at least six. Hence \(w_c=4\). The output constraints at \(b,c\) give \(w_a,w_b\le3\), and the sum \(\sum w=10\) forces \(w_a=w_b=3\). When the fiber has no edges of color \(1-s\), its transfer map is the identity, so the opposite-color predecessor vector is \((5,5,5)\). \(\square\)

Thus a six-factor counterexample would force a specific \((3,3,4)\) profile around every last-factor monochromatic triangle, in every permutation of the six factors.
