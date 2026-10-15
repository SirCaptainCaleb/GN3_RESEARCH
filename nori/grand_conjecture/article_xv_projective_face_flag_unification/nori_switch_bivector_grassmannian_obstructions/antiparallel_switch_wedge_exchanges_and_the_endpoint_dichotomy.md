# Antiparallel switch-wedge exchanges and the endpoint dichotomy

### Antiparallel switch-wedge exchanges and the endpoint dichotomy

The quadratic switch-bivector from the preceding Subsection can be replaced by a decomposable extreme-switch wedge. Its comparison under adjacent rank exchanges has a sharp algebraic classification. This yields an unconditional one-skeleton compatibility theorem for arbitrary reversal-odd boundary triple colorings and all but two cube exchange ranks. Importantly, the cube's root-changing rank exchange is compatible even when its cyclic variation jump is large.

#### Extreme-switch wedge and opposition

Let \(n\ge3\), \(s\in\{0,1\}\), \(m=n-2s\ge3\), and let \(\pi\) be an order of \(n\) distinct symbols. Put \(W=\{z\in\mathbb R^n:\sum_i z_i=0\}\) and
\[
Z_0(\pi)=Z_n(\pi)=0,\quad
Z_j(\pi)=\sum_{h=1}^j e_{\pi_h}-\frac jn\mathbf1
\quad(1\le j<n).
\]
For a binary word \(w\) of length \(m\), let \(a(w)\) and \(b(w)\) be the first and last switch positions when at least two switches occur. Define
\[
\boxed{E_s(\pi,w)=
Z_{a(w)+s}(\pi)\wedge Z_{b(w)+s}(\pi)\in\Lambda^2W,}
\tag{1}
\]
and set \(E_s=0\) when the word has at most one switch. The prefix vectors \(Z_1,\ldots,Z_{n-1}\) form a basis of \(W\), so
\[
\boxed{E_s=0\iff\operatorname{sw}(w)\le1.}\tag{2}
\]
If reversal sends \((\pi,w)\) to \((\pi^{\rm rev},\mathbf1+\operatorname{rev}w)\), then
\[
\boxed{E_s(Rg)=-E_s(g).}\tag{3}
\]
Indeed the switch interval endpoints exchange under reversal, the centered prefix \(Z_j\) becomes \(-Z_{n-j}\), and wedge factor order reverses.

#### Algebraic classification of adjacent exchanges

Let \(\pi'=\pi s_i\) exchange consecutive entries in positions \(i,i+1\). All centered prefixes except the \(i\)-th remain unchanged, and
\[
\boxed{Z_i(\pi')=Z_{i-1}(\pi)+Z_{i+1}(\pi)-Z_i(\pi).}\tag{4}
\]

**Theorem 1 (only terminal pairs can be antiparallel).** Choose arbitrary index pairs \(1\le a<b<n\), \(1\le a'<b'<n\), and write
\[
U=Z_a(\pi)\wedge Z_b(\pi),\quad
U'=Z_{a'}(\pi')\wedge Z_{b'}(\pi').
\]
Then \(U'\) is a negative real multiple of \(U\) if and only if one of these situations holds:
\[
\boxed{
\begin{array}{c|c|c}
i&(a,b)&(a',b')\\ \hline
1&(1,2)&(1,2)\\
n-1&(n-2,n-1)&(n-2,n-1).
\end{array}}
\tag{5}
\]
In both situations \(U'=-U\). For every \(2\le i\le n-2\), antiparallelity is impossible for all choices of the two index pairs.

*Proof.* Work in the exterior basis \(Z_j(\pi)\wedge Z_k(\pi)\), \(j<k\). The first bivector \(U\) is a single positive basis vector. If neither of \(a',b'\) equals \(i\), the second is also a positive basis vector and hence cannot be a negative multiple of \(U\).

Suppose the second pair contains \(i\). By (4), its wedge expression is the sum of up to three basis terms coming from \(Z_{i-1},Z_{i+1},-Z_i\). If \(2\le i\le n-2\), the first and second neighboring prefix vectors are nonzero and distinct. Wedging with an index other than \(i\) gives at least two nonzero distinct exterior basis terms, including when the other index is \(i-1\) or \(i+1\). Thus it cannot be collinear with \(U\). For \(i=1\), the only possibility of a single negative basis term is the pair \((a',b')=(1,2)\), giving \((Z_2-Z_1)\wedge Z_2=-Z_1\wedge Z_2\). For \(i=n-1\), the symmetric possibility is \((a',b')=(n-2,n-1)\), giving \(Z_{n-2}\wedge(Z_{n-2}-Z_{n-1})=-Z_{n-2}\wedge Z_{n-1}\). Matching with the first positive basis vector forces the index pairs in (5). \(\square\)

**Corollary 2 (boundary-tournament exchange compatibility).** For \(n\ge5\), let \(b\) be an arbitrary reversal-odd boundary 3-tournament on \(n\) vertices. Suppose two Hamilton orders \(g,g'\) differ by an adjacent transposition and both have at least two triple-word switches. Their extreme-switch bivectors \(E_1(g),E_1(g')\) are never antiparallel.

*Proof.* The triple-color word has length \(n-2\), so the switch prefix indices \(a+1,b+1\) always lie in \(\{2,\ldots,n-2\}\). Neither terminal possibility (5) can arise. No property beyond the existence of those full words is required. \(\square\)

**Corollary 3 (cube root exchanges are compatible).** For an arbitrary antipodally odd cube-edge coloring, two full geodesic flags related by the root-changing type-B exchange \(r_0(x;\pi)=(x+e_{\pi_1};\pi)\), and having at least two internal switches each, have non-antiparallel extreme-switch bivectors \(E_0\). The same holds for the added last-dimension root exchange \(r_n(x;\pi)=(x+e_{\pi_n};\pi)\) in the endpoint-symmetric affine chamber geometry. For neighboring dimension orders, antiparallelity is possible only at rank \(i=1\) or \(i=n-1\), and then only with consecutive switches at the corresponding pair of endpoint positions.

*Proof.* Either root exchange leaves \(\pi\) unchanged. Both wedges are positive elements of the same exterior basis, so they cannot be antiparallel. For exchanges changing the dimension order, apply Theorem 1 with \(s=0\). \(\square\)

**Proposition 4 (terminal exceptions occur with legal flat-square colorings).** For every \(n\ge3\), a legal antipodally odd cube-edge coloring realizes antiparallel wedges across an adjacent exchange of the first two dimensions. Take the full orders \(\pi=(1,2,3,\ldots,n)\) and \(\pi'=(2,1,3,\ldots,n)\), both rooted at zero. Prescribe color words
\[
w(0;\pi)=w(0;\pi')=(0,1,0,\ldots,0).
\]
These prescriptions agree on the common suffix and assign the first square's two routes the same successive colors \(0,1\). All prescribed edges lie in distinct antipodal edge orbits, except where the two paths share an edge with identical prescribed color, so the prescriptions extend to a legal antipodally odd coloring. Both have switches at positions \(1,2\), and (4) gives
\[
E_0(0;\pi')=-E_0(0;\pi).
\]
The initial square's four edge colors are \(0,1,1,0\) in cyclic order, whose square curvature is zero. Thus even square flatness cannot exclude this seam. The final-two-dimension exception follows by the symmetric construction at the terminal square.

#### A universally chosen lower-dimensional edge extension

**Theorem 5 (generic projection and equivariant one-skeleton map).** Fix \(n\ge5\). There is a linear map
\[
L:\Lambda^2W\longrightarrow\mathbb R^{n-2}
\tag{6}
\]
chosen independently of the boundary-tournament coloring, such that for *every* reversal-odd tournament in which each Hamilton order has at least two switches, the normalized labels
\[
\boxed{g\longmapsto \frac{L(E_1(g))}{\|L(E_1(g))\|}\in S^{n-3}}
\tag{7}
\]
extend by normalized straight-line interpolation over all adjacent-transposition edges in the dual type-A Coxeter complex, equivariantly under order reversal.

*Proof.* As \(\pi\) varies and \(a<b\) vary over the allowed prefix indices, the set \(\mathcal S=\{Z_{a+1}(\pi)\wedge Z_{b+1}(\pi)\}\) is finite. Choose a linear map \(L\) that takes every member of \(\mathcal S\) to a nonzero vector and takes every linearly independent pair of members to linearly independent vectors. Such maps form a nonempty Zariski-open subset: for each specified nonzero vector or independent pair, the unwanted rank-drop is a proper algebraic condition on linear maps to a real vector space of dimension at least two, and there are finitely many conditions. By Corollary 2, labels of adjacent flags are never on negative rays in \(\Lambda^2W\). Under the chosen projection their images also are never on negative rays, since noncollinear labels remain noncollinear and positive proportional labels remain positive proportional. Their straight-line segments avoid the origin. Normalize these segments and apply (3); reversal maps edges to edges and negates their endpoint labels, so the extension is equivariant. \(\square\)

**Status and obstruction.** Theorem 5 proves one-skeleton compatibility in the complete unrestricted boundary class under the hypothetical no-good-path assumption, while Corollary 3 resolves the cube's root-changing exchanges at this linear level. Higher-dimensional face fillings are still open. The examples in Proposition 4 demonstrate that normalized *straight-line* interpolation across all cube rank exchanges fails without endpoint corrections. Since the target sphere \(S^{n-3}\) is path-connected, the endpoint defects may be bypassed on edges; coherently filling rank-two and higher residues while preserving coloring remains the substantive equivariant obstruction.
