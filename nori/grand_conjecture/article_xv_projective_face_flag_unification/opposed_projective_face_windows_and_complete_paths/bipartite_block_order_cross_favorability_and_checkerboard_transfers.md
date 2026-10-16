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

## Odd common readers across two blocks: closure by four group orders

Let [n]=J disjoint-union K, both nonempty. Let A:Q_J->F2 and B:Q_K->F2 be arbitrary Boolean functions satisfying A(bar a)=1-A(a) and B(bar b)=1-B(b). For arbitrary fixed offset bits u_j (j in J) and v_k (k in K), define
\[
c_j(x)=u_j+B(x_K),\quad j\in J;\qquad
c_k(x)=v_k+A(x_J),\quad k\in K.
\tag{OR1}
\]
This is a legal antipodally odd cube-edge coloring.

**Theorem (two-block odd common-reader closure).** Every coloring (OR1) has a monochromatic-zero full antipodal geodesic from at least 2^(n-1) distinct starting roots.

*Proof.* Partition J into J_0,J_1 by the offset u_j, and K into K_0,K_1 by v_k. Empty groups are permitted. Choose a root a with A(a)=0 and define d_A=A(a xor 1_(J_0)). For b in Q_K let d_B=B(b) xor B(b xor 1_(K_0)). Oddness makes d_B invariant under b->bar b. Therefore one can select b from any antipodal pair so that
\[
B(b)=1\mathbin{\mathrm{xor}}d_A\mathbin{\mathrm{xor}}d_B.
\tag{OR2}
\]
Traverse all directions in the four groups in the following order, for the four values (d_A,d_B):
\[
\begin{array}{c|c}
(d_A,d_B)&\text{group order}\\
(0,0)&K_0,\ J_1,\ K_1,\ J_0\\
(0,1)&J_0,\ K_0,\ J_1,\ K_1\\
(1,0)&K_0,\ J_0,\ K_1,\ J_1\\
(1,1)&J_1,\ K_0,\ J_0,\ K_1 .
\end{array}
\tag{OR3}
\]
Each group has constant edge color because its own directions do not affect the opposite block's reader. In the four respective cases, A equals (0,1) when traversing (K_0,K_1), and B equals (1,0), (0,1), (0,1), or (0,1) when traversing the relevant (J_1,J_0) or (J_0,J_1) groups. These values follow from (OR2), A(a)=0, d_A,d_B, and the antipodal identities after traversing all directions of either block. Thus every traversed edge has color zero, and all n directions are used once. This constructs a monochromatic antipodal geodesic.

There are 2^(|J|-1) choices of a with A(a)=0. For each, one b from each of the 2^(|K|-1) antipodal pairs satisfies (OR2). Thus there are 2^(n-2) zero-path starting roots with A(a)=0; reversing those paths gives another 2^(n-2) roots with A(a)=1. The root sets are disjoint. \(\square\)

**Corollary (factorial witness count).** The unoriented monochromatic-zero antipodal geodesic count obeys
\[
Z(c)\ge2^{n-2}|J_0|!|J_1|!|K_0|!|K_1|!.
\tag{OR4}
\]
Indeed for each of the 2^(n-2) constructed roots one may independently permute directions inside every block of (OR3); the resulting rooted paths are distinct and their reversed endpoints belong to the other half of the J-root space.

No affinity, locality, or restriction beyond the two common odd scalar readers is assumed. The construction does not imply closure for arbitrary bipartite interaction graphs with unrelated direction functions.


### One-sided common-reader closure with unrelated opposite-block rules

Let \([n]=J\sqcup K\) with \(J,K\ne\varnothing\). For each \(j\in J\), let \(g_j:Q_K\to\mathbb F_2\) be an arbitrary odd Boolean function, so \(g_j(\bar y)=1+g_j(y)\); the functions \(g_j\) may be unrelated. Let \(A:Q_J\to\mathbb F_2\) be any odd Boolean function and \(t\in\mathbb F_2\). Define the legal antipodally odd edge coloring
\[
c_j(x,y)=g_j(y)\quad(j\in J),\qquad
c_k(x,y)=A(x)+t\quad(k\in K).
\tag{OS1}
\]
Every function ignores the bit belonging to its direction. Unlike the earlier two-common-reader theorem, there is no common-reader requirement on the \(J\)-direction rules. The \(K\)-direction rules share the same scalar reader and the same offset.

**Theorem (one-sided common-reader full-geodesic theorem).** Every coloring (OS1) has a monochromatic-zero full antipodal geodesic from at least \(2^{n-1}\) distinct roots. A constructive set of \(2^{n-1}\) roots is available.

*Proof.* For each \(y\in Q_K\) put
\[
T(y)=\{j\in J:g_j(y)=0\}.
\]
Choose any \(x\in Q_J\) satisfying
\[
A(x+\mathbf1_{T(y)})=t, \tag{OS2}
\]
where addition is modulo two. Such \(x\) exist in number \(2^{|J|-1}\), since oddness of \(A\) pairs each argument with its complement and precisely one member of each pair has value \(t\). Starting at \((x,y)\), traverse all \(J\)-directions in \(T(y)\), then all \(K\)-directions, then all remaining \(J\)-directions, with arbitrary order inside each group.

Every first-group edge has color \(g_j(y)=0\). The first group changes the \(J\)-bits to \(x+\mathbf1_{T(y)}\), so every middle-group edge has color \(A(x+\mathbf1_{T(y)})+t=0\). After the middle group the \(K\)-bits equal \(\bar y\). For a final-group direction \(j\notin T(y)\), oddness gives \(g_j(\bar y)=1+g_j(y)=0\). Thus every traversed edge is zero and each direction occurs once. There are \(2^{|K|}\) choices of \(y\) and \(2^{|J|-1}\) compatible choices of \(x\), proving the root assertion. \(\square\)

**Corollary (factorial witness count).** If \(Z_0(c)\) counts unoriented zero full geodesics, then
\[
\boxed{
Z_0(c)\ge 2^{|J|-2}|K|!
\sum_{y\in Q_K}|T(y)|!\bigl(|J|-|T(y)|\bigr)!
\ge 2^{n-2}|K|!\lfloor |J|/2\rfloor!\lceil |J|/2\rceil!.
}
\tag{OS3}
\]
*Proof.* For every compatible root in (OS2), the constructed paths permit arbitrary permutations inside the three direction groups, yielding \(|T(y)|!|K|!(|J|-|T(y)|)!\) distinct rooted full geodesics. Sum over the \(2^{|J|-1}\) roots for each \(y\) and divide by two, because each unoriented full geodesic has at most its two orientations counted. Finally \(r!(|J|-r)!\ge\lfloor |J|/2\rfloor!\lceil |J|/2\rceil!\). \(\square\)

### One-sided common-reader closure with arbitrary direction offsets

The common-reader hypothesis may retain different fixed offsets on each direction of its block. Let \([n]=J\sqcup K\), both blocks nonempty, and prescribe
\[
\boxed{c_j(x,y)=g_j(y)\quad(j\in J),\qquad
c_k(x,y)=A(x)+v_k\quad(k\in K),}
\tag{OS4}
\]
where \(A:Q_J\to\mathbb F_2\) and all \(g_j:Q_K\to\mathbb F_2\) are arbitrary odd Boolean functions and the bits \(v_k\) are unrestricted constants.

**Theorem (arbitrary-offset one-sided common-reader closure).** Every legal coloring (OS4) admits a monochromatic-zero full antipodal geodesic in every dimension. The \(J\)-direction rules can be unrelated; there is no affine or locality assumption.

*Proof.* Define \(K_t=\{k\in K:v_k=t\}\) for \(t\in\mathbb F_2\). If one set is empty, the preceding theorem applies. Assume both are nonempty.

Because \(A\) is odd, some \(j\in J\) influences \(A\): there is \(u\in Q_J\) with \(A(u)\ne A(u+e_j)\). Because \(g_j\) is odd, it cannot be invariant under both translations \(\mathbf1_{K_0}\) and \(\mathbf1_{K_1}\): their sum is \(\mathbf1_K\), which complements its value. Consequently there is \(t\in\mathbb F_2\) and \(y\in Q_K\) for which \(g_j(y)\ne g_j(y+\mathbf1_{K_t})\). By replacing \(y\) with \(\bar y\) when needed, oddness permits
\[
g_j(y)=1,\qquad g_j(y+\mathbf1_{K_t})=0. \tag{OS5}
\]
Similarly, complementing the chosen \(u\) when needed permits
\[
A(u)=t,\qquad A(u+e_j)=1+t. \tag{OS6}
\]

Set \(T=\{i\in J:g_i(y)=0\}\); equation (OS5) ensures \(j\notin T\). Choose the starting \(J\)-bits \(x=u+\mathbf1_T\) and starting \(K\)-bits \(y\). Traverse the five consecutive direction groups
\[
\boxed{T,\quad K_t,\quad\{j\},\quad K_{1-t},\quad J\setminus(T\cup\{j\}).}
\tag{OS7}
\]
Every first-group edge has color \(g_i(y)=0\). Afterwards the \(J\)-bits equal \(u\), so the \(K_t\)-edges have color \(A(u)+t=0\). After the \(K_t\)-steps, the \(j\)-edge has color \(g_j(y+\mathbf1_{K_t})=0\). It changes the \(J\)-bits to \(u+e_j\), making the \(K_{1-t}\)-edges zero by (OS6). Finally all \(K\)-bits have been complemented, so every remaining \(J\)-edge has color \(g_i(\bar y)=1+g_i(y)=0\). The five groups partition all directions, giving a monochromatic full antipodal geodesic. \(\square\)

**Closure role.** The unrestricted-offset theorem removes the common-reader restriction on an entire side of a bipartite interaction system, retaining only a single shared odd reader up to direction-dependent constants on the other side. Its proof uses one influential direction of that reader as a separator between the two offset groups. Fully unrelated reader families on both sides, or interactions within either block, remain the unclosed branches. The theorem is dimension-uniform and applies to arbitrary nonlinear odd reader functions.
