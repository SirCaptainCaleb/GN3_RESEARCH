# Root-endpoint state torus and geodesic connectors

# Uncolored reachability, terminal memory, and exact topological extraction

We write \(Q_n=\mathbb F_2^n\), and require a *geodesic* to flip every coordinate at most once. The color of a monochromatic witness is forgotten from its reachability label, but the witness itself must be an actual cube path.

## The simpler antipodally odd edge coloring

Let \(c(\bar e)=1-c(e)\) be a binary coloring of cube edges and define
\[
R(x)=\{z:\text{there is a monochromatic geodesic from }x\text{ to }z\},
\]
including the length-zero path. Reversing and complementing witness paths gives \(z\in R(x)\iff x\in R(z)\) and \(R(\bar x)=\overline{R(x)}\).

**Proposition 1 (uncolored overlap).** A full monochromatic antipodal geodesic exists precisely when \(R(x)\cap R(\bar x)\ne\varnothing\) for some \(x\), equivalently when some \(R(x)\) contains an antipodal pair.

**Proof.** If \(z\) belongs to the intersection, monochromatic geodesics \(x\to z\) and \(z\to\bar x\) have complementary direction supports, so they concatenate to a full antipodal geodesic with at most one color change. If their colors are \(q\) and \(1-q\), begin instead at \(z\), traverse the second piece to \(\bar x\), and append the antipodal image of the first piece, which also has color \(1-q\). This gives a full monochromatic geodesic. The converse is immediate. \(\square\)

## The precise ordered-three-face target

Now let \(c(F,\pi)\) satisfy \(c(\bar F,\operatorname{rev}\pi)=1-c(F,\pi)\), where \(F\) is a three-face and \(\pi\) orders its free directions. Fix \(n\ge5\), a root \(x\), and distinct terminal directions \(J=(a,b)\). Put \(D=[n]\setminus\{a,b\}\), and define
\[
R_J(x)=\{\,\varnothing\ne U\subseteq D:
\text{some monochromatic ordered-three-face geodesic from }x
\text{ has direction word }(u_1,\ldots,u_k,a,b),
\ \{u_i\}=U\,\}.
\tag{1}
\]
It is essential to retain the ordered terminal pair: naive joining of arbitrary monochromatic path branches creates uncontrolled junction windows.

**Theorem 2 (exact reversed-two-tail equivalence).** A full antipodal geodesic with at most one change exists **if and only if** for some \(x,a,b\) there are nonempty complementary supports \(U,V\), \(U\sqcup V=D\), such that
\[
U\in R_{(a,b)}(x),\qquad V\in R_{(b,a)}(x).
\tag{2}
\]

**Proof.** Take witnesses \(A\) and \(B\) with direction orders
\((u_1,\ldots,u_k,a,b)\) and \((v_1,\ldots,v_m,b,a)\), respectively. Their monochromatic window colors may differ. The antipodal reversal of \(B\) starts at
\[
\overline{x\oplus\chi_V\oplus e_a\oplus e_b}=x\oplus\chi_U
\]
and follows \((a,b,v_m,\ldots,v_1)\), its window color being the complement of \(B\)'s. Follow the \(U\)-prefix of \(A\) and then this reversed path. The first \(k\) ordered three-face windows are exactly those of \(A\); the final \(m\) are exactly those of reversed \(B\). Since \(k+m=n-2\), there are **no unaccounted seam windows**, and the path uses all directions exactly once. It changes color at most once. Conversely, split any full one-change geodesic immediately between its two monochromatic window blocks. Its prefix ending with the two middle directions \((a,b)\) and its antipodally reversed suffix ending with \((b,a)\) give the witnesses in (2), both rooted at the original start. An entirely monochromatic path admits any interior cut. \(\square\)

For an ordered \(k\)-face coloring the same counting argument uses terminal memory of length \(k-1\). In particular, the edge case has empty terminal memory; the three-face case requires exactly two directions.

## Root moves, geometric sheets, and topological obstructions

If a path \((u_1,\ldots,u_k,a,b)\) certifies \(U\in R_J(x)\), then after deleting its first \(t<k\) moves it certifies
\[
U_t=\{u_{t+1},\ldots,u_k\}\in R_J(x_t),\quad
x_t=x\oplus\{u_1,\ldots,u_t\},
\]
while preserving the **absolute endpoint**
\[
x_t\oplus\chi_{U_t}\oplus e_a\oplus e_b=x\oplus\chi_U\oplus e_a\oplus e_b.
\tag{3}
\]
Thus root-slide chains are certified and acyclic by decreasing support rank. But two witnesses slid separately need not still have the same root. In root/support bits the relation \(y_i=x_i\oplus U_i\) makes legal slides traverse opposite diagonals on the two endpoint sheets. Their crossing is not a certified coincidence, even if a simplicial interpolation identifies the geometric points.

The uncolored edge reachability **nerve** puts a simplex on roots possessing a common physical reachable target. Cube-star simplices and three-corner square simplices always exist, but an antipodally odd affine \(Q_4\) coloring can have a square whose four corners share no target. Hence no generic cubical Sperner carrier may assume that every geometric square is filled in this nerve. Cardinality is equally inadequate: pairing the coordinates in \(Q_{2m}\) and coloring each edge by its partner bit gives
\[
|R(x)|=3^{A+H}+3^{B+H}-2^H
\le 2\cdot3^m-2^m<2^{2m-1}\quad(m\ge5),
\tag{4}
\]
where \(A,B,H\) count starting \(00,11,\) and mixed pairs. Formula (4) follows by counting color-specific product supports, each with three choices on its compatible pairs and an intersection of size \(2^H\). Nevertheless a fully mixed root supports a monochromatic full antipodal geodesic. A large-volume pigeonhole theorem therefore cannot replace a geometry-sensitive argument.

A fixed alphabet of physical targets \(D_0\) that gives all roots nonempty labels \(R(x)\cap D_0\) for every coloring must dominate the cube, and so needs at least \(2^n/(n+1)\) targets. Adaptive equivariant domination folds preserve common-target incidences and the homotopy type of their reachability nerve; they do not yet force the needed intersection. Similarly an origin in the convex hull of noncomplementary bit-string labels need not correspond to a genuine complementary-support witness.

## Two dimension-independent routes to closure

The **primary fixed-point route** is to construct a legal equivariant, root-coupled carrier bearing actually certified labels from \(R_{(a,b)}(x)\) and \(R_{(b,a)}(x)\). Its Tucker/Sperner/Hex/KKM boundary condition must force (2) at a *single* root. An alternating simplex, a balanced vector average, or a crossing between distinct witness sheets does not suffice.

A second proved *conditional* connector uses the **four-facet cap-memory graph**. Fix an \((n-2)\)-coordinate set \(U\), omitted directions \(a,b\), and projected root \(r\). For each \(i\in U\), let \(A_i(r)\) denote the color of the actual face with ordered free triple \((a,b,i)\) and exterior \(U\)-bits determined by \(r\); it is independent of the two omitted-coordinate bits. Join possible first and last directions of monochromatic \(U\)-spanning geodesics across any of the four parallel \(U\)-facets. Under hypothetical failure of NORI every such edge joins \(i,j\) with \(A_i(r)\ne A_j(r)\). Hence **any odd cycle** in this memory graph forces a full one-change antipodal geodesic. The remaining issue is to create such a nonbipartite compatible family of actual paths, not merely to draw one abstractly.

These are exact extraction mechanisms; neither is yet a proof that the requisite configuration exists. The open step is a genuine global fixed-point/connector theorem supplying compatible monochromatic witnesses while preserving root, terminal direction memory, and the physical ordered-face incidence.
