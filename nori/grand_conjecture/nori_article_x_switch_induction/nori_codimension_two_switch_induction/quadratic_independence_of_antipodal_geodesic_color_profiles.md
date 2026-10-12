# Quadratic independence of antipodal-geodesic color profiles

# Quadratic independence of antipodal-geodesic color profiles

Let \(n\ge2\), and write \(x^i=x\oplus e_i\) and \(\bar x=x\oplus\mathbf1\) for vertices of \(Q_n\). Let \(c_i(x)\in\mathbb F_2\) be the color of the undirected edge \(\{x,x^i\}\), with
\[
c_i(x^i)=c_i(x),\qquad c_i(\bar x)=1+c_i(x).
\tag{1}
\]
For a long geodesic \(P\), define \(w(P)\in\mathbb F_2^n\) by letting \(w_i(P)\) be the color of its unique edge in direction \(i\). Thus the coordinates of \(w(P)\) are indexed by directions, regardless of traversal order. Put
\[
\mathcal W(c)=\{w(P):P\text{ is a long geodesic in }Q_n\}.
\]

**Theorem 1 (quadratic independence).** Suppose a multilinear polynomial
\[
q(Y)=a_0+\sum_{i=1}^n b_iY_i+
       \sum_{1\le i<j\le n}a_{ij}Y_iY_j
\quad\text{over }\mathbb F_2
\tag{2}
\]
vanishes at every \(w\in\mathcal W(c)\). Then every coefficient in (2) is zero.

Equivalently, every nonconstant Boolean polynomial of degree at most two assumes both values on \(\mathcal W(c)\). The coloring in (1) may have arbitrary nonlinear dependence on its exterior coordinates.

We use a consequence of constant geodesic integrals which requires no antipodal condition on the edge weights.

**Lemma 2 (constant antipodal integrals).** Let \(D\) be a nonempty coordinate set, and give each undirected edge of \(Q_D\) a weight \(\omega(e)\in\mathbb F_2\). Suppose the sum of the edge weights on every long geodesic is the same constant \(\kappa\), independently of its root and coordinate order. Then every square has weight sum zero, and
\[
\omega(e)=\omega(e^{*}),
\tag{3}
\]
where \(e^{*}\) is the antipodal edge within \(Q_D\).

*Proof.* Compare two long geodesics which start at the same vertex, traverse two directions in opposite orders, and then follow the same remaining order. Their later edges coincide, so the sum of the four square-edge weights is zero. This holds for every square.

Choose a vertex potential \(\phi\) by integrating \(\omega\) from a fixed vertex. The integral is independent of the chosen path: a cube walk is encoded by coordinate flips, and adjacent exchanges and cancellations of repeated consecutive flips reduce any closed walk to the empty walk. Square sums and the weights of backtracks vanish. Thus
\[
\omega(\{x,x^j\})=\phi(x)+\phi(x^j).
\]
Writing \(x^D\) for the complement within \(Q_D\), the hypothesis implies
\[
\phi(x)+\phi(x^D)=\kappa.
\]
Adding this equation at \(x\) and \(x^j\) proves (3). The same argument applies when \(|D|=1\), with no square condition needed. \(\square\)

*Proof of Theorem 1.* Put \(a_{ji}=a_{ij}\) and \(a_{ii}=0\). Consider a long geodesic whose first direction is \(i\), with profile \(w\). Move its root across its first edge and rotate that direction to the end of the order. All other edges are unchanged, and the new last edge is antipodal to the old first edge. By (1), the new profile is \(w+e_i\). Therefore
\[
0=q(w+e_i)+q(w)=b_i+\sum_{j\ne i}a_{ij}w_j.
\tag{4}
\]

Fix either facet perpendicular to \(i\). Every long geodesic in that facet can be preceded by an \(i\)-edge to obtain a long geodesic of the full cube beginning in direction \(i\). Consequently (4) says that the weights
\[
\omega_j(x)=a_{ij}c_j(x)\qquad(j\ne i)
\tag{5}
\]
have constant long-geodesic integral \(b_i\) on each of the two facets.

There are three consequences.

First, complementing every vertex of a full geodesic complements every entry of its profile and preserves its first direction. Adding (4) for a path and its antipodal image gives
\[
\sum_{j\ne i}a_{ij}=0\qquad(i\in[n]).
\tag{6}
\]

Second, apply (3) to (5) within an \(i\)-facet. Its antipodal map is \(x\mapsto\bar x^i\), so
\[
a_{ij}c_j(x)=a_{ij}c_j(\bar x^i)
           =a_{ij}\bigl(1+c_j(x^i)\bigr).
\]
For the Boolean difference \(\Delta_i c_j(x)=c_j(x^i)+c_j(x)\), this gives
\[
a_{ij}=1\quad\Longrightarrow\quad
\Delta_i c_j(x)=1\text{ for every }x.
\tag{7}
\]

Third, square closedness in the same facet gives, for distinct \(i,j,k\),
\[
a_{ij}\Delta_k c_j(x)=a_{ik}\Delta_j c_k(x).
\tag{8}
\]

Form a simple graph on \([n]\), placing an edge \(ij\) precisely when \(a_{ij}=1\). If \(ij\) and \(jk\) are edges with \(i,j,k\) distinct, (7) gives
\(\Delta_k c_j=\Delta_j c_k=1\). Equation (8) then forces \(a_{ik}=1\). Every connected component of this graph is therefore a clique. By (6), all its vertex degrees are even, so each clique has odd order.

Suppose a component \(B\) has at least two vertices. Fix \(j\in B\) and choose \(i\in B\setminus\{j\}\). Equation (7) gives
\[
\Delta_k c_j=1\quad(k\in B\setminus\{j\}).
\]
For \(k\notin B\), equation (8), with \(a_{ij}=1\) and \(a_{ik}=0\), gives \(\Delta_k c_j=0\). Also \(\Delta_j c_j=0\) by undirectedness. Hence, for some constant \(\gamma_j\),
\[
c_j(x)=\gamma_j+\sum_{k\in B\setminus\{j\}}x_k.
\tag{9}
\]
Indeed, subtracting the displayed coordinate sum leaves a function with zero difference in every coordinate, which is constant on the connected cube. Since \(|B|\) is odd, (9) is invariant under complementing all coordinates. This contradicts (1).

Thus the coefficient graph has no edges, and every \(a_{ij}\) vanishes. Equation (4) now gives \(b_i=0\) for every \(i\). Since at least one long geodesic exists, evaluating \(q\) on its profile gives \(a_0=0\). \(\square\)

**Corollary 3 (dimension and profile count).** The vectors
\[
\left(1,\ (w_i)_{i\in[n]},\
                (w_iw_j)_{1\le i<j\le n}\right),
\qquad w\in\mathcal W(c),
\tag{10}
\]
span \(\mathbb F_2^{\,1+n+\binom n2}\). In particular,
\[
|\mathcal W(c)|\ge 1+n+\binom n2.
\tag{11}
\]
Since \(\mathcal W(c)\) is closed under complementation, its cardinality is even; consequently (11) may be rounded up to the next even integer.

*Proof.* A proper linear span in (10) would admit a nonzero annihilating linear functional. Its coefficients would define a nonzero polynomial (2) vanishing on every profile, contrary to Theorem 1. A spanning family has at least as many vectors as the dimension. Complementation has no fixed point on \(\mathbb F_2^n\), proving the final assertion. \(\square\)

The theorem strengthens the affine-span conclusion of Article VIII by including all pair products of direction colors, even when their coefficients involve arbitrarily many directions. Its proof uses compatible edges on every coordinate square and both facets perpendicular to each direction. It provides a restriction on the full profile family of any hypothetical counterexample: every nonzero multilinear polynomial vanishing on that family must have degree at least three.

The statement concerns direction-indexed profiles over all long geodesics. It does not specify traversal orders, guarantee either constant profile, or establish a two-switch path. Those existence questions remain open.
