# Complete face-flag basis paths and antipodal spheres

# Simple-polytope flags and complete basis paths

Let \(P\subset\mathbb R^d\) be a full-dimensional simple convex polytope. A maximal face flag is \(F_0\subset F_1\subset\cdots\subset F_d=P\), where \(\dim F_j=j\). Put \(v_0=F_0\). For \(j\ge1\), define \(v_j\) as the other endpoint of the unique edge incident with \(v_{j-1}\) that lies in \(F_j\) and leaves \(F_{j-1}\).

**Theorem 1 (complete paths from flags).** The construction produces a vertex-simple \(d\)-edge walk \(v_0,\ldots,v_d\) satisfying
\[
\operatorname{aff}\{v_0,\ldots,v_j\}=\operatorname{aff}F_j.
\]
Its displacement vectors form a basis of \(\mathbb R^d\). Moreover, the correspondence is a bijection between maximal face flags and *face-graded basis paths*, namely graph paths whose first \(j+1\) vertices lie in a \(j\)-face and whose displacements are linearly independent.

*Proof.* Each face \(F_j\) is a simple \(j\)-polytope and \(F_{j-1}\) its facet. At the vertex \(v_{j-1}\) there are \(j\) incident edges within \(F_j\), of which \(j-1\) lie in \(F_{j-1}\). The remaining edge exists uniquely and ends at \(v_j\notin F_{j-1}\). Induction proves the asserted affine spans and the independence of moves. Conversely, the \(j+1\) affinely independent prefix vertices determine a unique containing \(j\)-face: distinct faces of dimension \(j\) intersect in lower dimension. These faces give the flag and its exiting-edge rule recovers the original walk. \(\square\)

**Corollary 2 (two natural cases).** When \(P\) is a \(d\)-simplex, each maximal flag inserts one previously unused vertex, and the induced walk is an arbitrary Hamilton ordering of all \(d+1\) vertices. When \(P=[0,1]^d\), each flag starts at an arbitrary vertex \(x\), frees one previously fixed dimension at every step, and induces the antipodal geodesic from \(x\) to \(\bar x\) traversing all \(d\) dimensions. Every witness in either original class corresponds to a flag. Thus vertex-simpleness and dimension-simpleness are both enforced intrinsically by the same face-graded basis condition.

**Theorem 3 (spherical face-flag carriers).** The order complex of the nonempty proper faces of \(P\) is the barycentric subdivision of \(\partial P\), hence a sphere \(S^{d-1}\). Its maximal simplices are face flags and consequently encode complete basis paths whenever \(P\) is simple. For cubes, central inversion of faces acts antipodally on this sphere. For simplices, face complementation \(S\mapsto V\setminus S\) defines a free simplicial antipodal involution of the type-A Coxeter sphere.

*Proof.* The proper-face order complex is the barycentric subdivision by definition. In a simplex with vertex set \(V\), map each proper nonempty face \(S\) to the ray spanned by
\[
z_S=\mathbf1_S-\frac{|S|}{|V|}\mathbf1
\]
in \(W=\{z:\sum_{v\in V}z_v=0\}\). Chains of subsets yield the standard braid-arrangement triangulation of \(S(W)\). Since \(z_{V\setminus S}=-z_S\), complementation is antipodal. The cube assertion follows from central symmetry of its boundary. \(\square\)

This unified geometric carrier applies to every simple polytope, including products of simplices and permutahedra. It builds maximal-path completeness into the top-dimensional simplices and supplies the same kind of sphere used by chain-level obstruction arguments.

**Open selection problem.** The boundary coloring lives on ordered two-step path windows and is odd under reversal; the cube coloring lives on undirected one-step windows and is odd under central antipodality. A common color-sensitive conjecture needs intrinsic local incidence descent and suitable opposition on the flag observations. Theorems 1–3 settle the common path geometry, without claiming a one-switch color selection theorem.
