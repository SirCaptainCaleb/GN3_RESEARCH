# Bipartite block-order cross-favorability and checkerboard transfers

### Bipartite block-order synchronization of two arbitrary cube colorings

Let \(f,g\) be arbitrary binary edge colorings of \(Q_d\). Suppose the union of their undirected direction-interaction graphs is bipartite with a common partition \([d]=U\sqcup V\). Therefore each \(U\)-direction edge color depends only on the starting \(V\)-bits, and each \(V\)-direction color depends only on the starting \(U\)-bits. Neither coloring is assumed affine or antipodally odd.

Write a starting vertex as \((a,b)\in Q_U\times Q_V\), and let \(\bar a,\bar b\) denote bitwise complements within those blocks. Define four Boolean feasibility predicates:
\[
\begin{aligned}
A(b)&:\ f_u(b)=0\quad\text{for all }u\in U,\\
B(a)&:\ f_v(\bar a)=1\quad\text{for all }v\in V,\\
C(a)&:\ g_v(a)=1\quad\text{for all }v\in V,\\
D(b)&:\ g_u(\bar b)=0\quad\text{for all }u\in U.
\end{aligned}
\tag{1}
\]
Here \(f_u(b)\) means the color of a direction-\(u\) edge at any vertex whose \(V\)-bits equal \(b\). Define the solution sets of these four predicates by the same capital letters.

**Theorem 1 (two opposite block orders).** A root \((a,b)\) admits a nondecreasing full \(f\)-geodesic with all \(U\)-steps before all \(V\)-steps, and a nonincreasing full \(g\)-geodesic with all \(V\)-steps before all \(U\)-steps, if and only if
\[
\boxed{(A(b)\lor B(a))\ \land\ (C(a)\lor D(b)).}
\tag{2}
\]
Consequently, such a common root exists if and only if at least one of the following four conditions holds:
\[
\boxed{
(A\ne\varnothing\land C\ne\varnothing)
\ \lor\ (A\cap D\ne\varnothing)
\ \lor\ (B\cap C\ne\varnothing)
\ \lor\ (B\ne\varnothing\land D\ne\varnothing).
}
\tag{3}
\]
If \(N\) denotes the number of roots supplied by this pair of block-order strategies, then
\[
\boxed{N\ge\max\{
|A||C|,\quad 2^{|U|}|A\cap D|,
\quad2^{|V|}|B\cap C|,\quad |B||D|
\}.}
\tag{4}
\]

*Proof.* In an \(f\)-path taking all \(U\) directions first, every \(U\)-edge color is determined by the unchanged \(V\)-bits \(b\), regardless of the order of the \(U\)-steps. We can sort these first-block colors increasingly. Afterwards the \(U\)-bits have all toggled to \(\bar a\). Every \(V\)-edge color is then determined by \(\bar a\), and can again be sorted increasingly. The concatenated word is nondecreasing precisely when no color-one first-block edge precedes a color-zero second-block edge, equivalently all first-block colors are zero or all second-block colors are one. This is \(A(b)\lor B(a)\).

The \(g\)-path taking \(V\) first and \(U\) second behaves dually. Sort each block decreasingly. The complete word is nonincreasing precisely when the first block is entirely one or the second block entirely zero, giving \(C(a)\lor D(b)\). Both paths start at \((a,b)\) and use every direction once. Expanding the conjunction of the two disjunctions yields four sufficient alternatives. Their free variables separate into the \(a\) and \(b\) blocks, proving both the nonemptiness criterion (3) and the four cardinality lower bounds (4). QED.

**Theorem 2 (linear-time checkerboard transfer for two even-cycle colorings).** Suppose \(d=2r\ge4\) and the union interaction graph is contained in the direction cycle \(C_{2r}\). Choose \(U\) to be the even directions and \(V\) the odd directions. Nonemptiness of each of the six sets
\[
A,\quad B,\quad C,\quad D,\quad A\cap D,\quad B\cap C
\tag{5}
\]
can be decided using a product of \(2\times2\) Boolean relations around one \(r\)-variable cycle. Hence the criterion (3) and a witnessing common root, whenever it holds, are computable in \(O(d)\) operations from the local four-bit truth tables.

*Proof.* For example \(A\) requires \(f_i(b_{i-1},b_{i+1})=0\) at each even \(i\). The participating variables are precisely the odd starting bits, and successive constraints join consecutive odd variables around their parity cycle. Each local truth table therefore gives a binary relation \(R_i\subseteq\{0,1\}^2\). There exists a cyclic assignment satisfying all these relations if and only if their Boolean relation product has a diagonal entry, equivalently nonzero Boolean trace. The same construction applies to \(B,C,D\), with appropriate complements of their variables. For \(A\cap D\), the local relation at even site \(i\) is the conjunction \(f_i(b_{i-1},b_{i+1})=0\) and \(g_i(1-b_{i-1},1-b_{i+1})=0\); for \(B\cap C\), make the analogous conjunction at odd sites. Each is still an arbitrary four-pair binary relation. Products of \(2\times2\) Boolean matrices and backtracking a successful two-state cycle take linear time. The case \(r=2\) simply has a two-edge parallel constraint cycle and is covered by the same product. QED.

**Corollary 3 (a no-overlap sufficient condition).** In the even-cycle setting, suppose every even-direction local function of \(f\) has at least three of four neighbor inputs giving color zero, and every odd-direction local function of \(g\) has at least three inputs giving color one. Then \(A,C\) are both nonempty and the two colorings have a common opposite-orientation root. The same conclusion holds with even and odd interchanged.

*Proof.* The binary relations for each of \(A,C\) omit at most one of their four possible pairs. Their cyclic Boolean composition also omits at most one pair, hence contains a diagonal pair. Apply Theorem 1. QED.

**Example 4 (all local simultaneous-opposite sets may be empty).** Let \(d\ge4\) be even, and set \(f=g\), with \(f_i(x)=x_{i+1}\) for every cyclic direction \(i\). Then the local sets \(\{(a,b):f_i(a,b)=0,\ g_i(a,b)=1\}\) are all empty. Nevertheless take a root whose even bits are one and odd bits zero. In the \(f\)-path with even directions first, all traversed edges have color zero. In the \(g\)-path with odd directions first, all edges have color one. Both are full dimension-simple antipodal geodesics from the same root. Thus Theorem 1 supplies compatibility unavailable to a method that requires shared opposite-color local inputs at every site.

**Proof-closure use.** The current unrestricted even-cycle cross-favorability question would be solved if one could prove that either these checkerboard conditions, or a bounded set of exchange repairs starting from them, succeeds for every pair of cyclic-local colorings. Theorem 2 isolates the failure of the two block-order strategies in a constant-size Boolean relation algebra, allowing explicit obstruction certificates for those strategies. It does not assert that the block orders suffice for every cyclic coloring: independent six-direction tests find pairs with compatible full paths but neither checkerboard strategy succeeds. The theorem instead supplies a second all-dimensional forcing mechanism orthogonal to the existing local-overlap and pendant-tree interface arguments.
