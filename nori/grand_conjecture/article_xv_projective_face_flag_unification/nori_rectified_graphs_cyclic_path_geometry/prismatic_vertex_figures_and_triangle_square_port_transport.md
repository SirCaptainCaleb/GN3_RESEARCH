# Prismatic vertex figures and triangle-square port transport

### Prismatic vertex figures and triangle-square port transport

The two rectified carriers from this Article have identical vertex figures in equal dimension. Their polygonal two-faces distinguish the two coloring geometries, while products of simplices provide a common triangle-square transport law and a complete-path shift formula.

**Theorem 1 (prismatic vertex figures).** Let \(d\ge3\). Every vertex figure of the midpoint rectification \(R_d\) of the \(d\)-cube and of the hypersimplex \(H_d=\Delta(2,d+1)\) is
\[
\boxed{\Delta^{d-2}\times\Delta^1.}\tag{1}
\]
Its vertices form two \((d-1)\)-element cliques connected by a perfect matching.

*Proof.* In \(R_d=[-1,1]^d\cap\{z:\sum_i|z_i|\le d-1\}\), choose the edge-midpoint vertex \(v=(0,1,\ldots,1)\). In its tangent cone put \(t=z_1\), \(u_j=1-z_j\) for \(j\ge2\). The inequalities near \(v\) are \(u_j\ge0\), \(|t|\le\sum_{j\ge2}u_j\). The cone section \(\sum_{j\ge2}u_j=1\) is the product of the simplex \(\{u\ge0,\sum u=1\}\) and \([-1,1]\).

For the hypersimplex, at its vertex \(e_a+e_b\), write \(z_a=1-\alpha\), \(z_b=1-\beta\), \(z_c=u_c\) for \(c\notin\{a,b\}\). The tangent inequalities are \(\alpha,\beta,u_c\ge0\) and \(\alpha+\beta=\sum_cu_c\). Intersecting with \(\sum_cu_c=1\) gives a simplex on the \(d-1\) remaining symbols times the segment \(\alpha+\beta=1\). These sections give the two vertex figures. \(\square\)

**Theorem 2 (polygon types encoded on the prism).** In the vertex figure (1), edges within either simplex layer correspond to triangular two-faces in both rectifications. The matching edges correspond to quadrilateral two-faces in \(R_d\), and triangular two-faces in \(H_d\).

*Proof.* The \(2(d-1)\) neighbors of a rectified-cube vertex representing a cube edge \(uv\) are the other \(d-1\) edges at \(u\) and at \(v\). Two from the same endpoint together with \(uv\) form a triangle inside the simplex obtained by rectifying that cube vertex. The matched pair from the two endpoints, in another cube dimension \(j\), lies with \(uv\) in the rectified square face spanning these two dimensions. For \(H_d\), a vertex \(\{a,b\}\) has neighbors \(\{a,c\}\) and \(\{b,c\}\). Within-layer neighbor pairs form triangles in the simplex face fixing \(a\) or \(b\); the matched pair \(\{a,c\},\{b,c\}\), together with \(\{a,b\}\), also forms a triangle. Every two-face of \(\Delta(2,d+1)\) is triangular, since fixing facet entries to zero or one until three entries remain produces a two-dimensional hypersimplex on three symbols. \(\square\)

#### Canonical transport through triangles and induced squares

Put \(P=\prod_{i=1}^r\Delta^{q_i-1}\), \(q_i\ge2\), of dimension \(d=\sum_i(q_i-1)\). Its graph is the Cartesian product \(G(P)=\square_i K_{q_i}\).

**Theorem 3 (port matching).** Every oriented edge \(xy\) of \(G(P)\) carries a canonical bijection
\[
\boxed{\Theta_{xy}:N(x)\setminus\{y\}\longrightarrow N(y)\setminus\{x\}.}\tag{2}
\]
If \(xy\) changes factor \(i\) from symbol \(a\) to symbol \(b\), the matching is given by:
(i) a neighbor \(z\) of \(x\) obtained by changing factor \(i\) from \(a\) to \(c\notin\{a,b\}\) matches \(z\) itself, closing a triangle \(xyz\);
(ii) a neighbor \(z\) obtained by changing another factor \(j\) matches the vertex obtained from \(y\) by making that same change of factor \(j\), closing an induced square. These are respectively \(q_i-2\) triangle pairs and \(d-q_i+1\) square pairs. Also \(\Theta_{yx}=\Theta_{xy}^{-1}\).

*Proof.* Every graph neighbor changes one factor. When that factor is \(i\), the new symbol \(c\) is also adjacent to \(b\), producing the stated triangle. When it is \(j\ne i\), changes in factors \(i,j\) commute, giving the unique opposite corner of their Cartesian square. Both assignments reverse upon interchanging \(x,y\), and exhaust the \(d-1\) outgoing edges other than \(xy\). Their cardinalities are the stated counts. \(\square\)

A product of segments has only square pairs; a single simplex has only triangle pairs. Mixed products have both types, providing one intrinsic family for the two local exchange laws.

#### Full-path dynamics in the same family

Every complete face-graded path in \(P\) corresponds to a cyclic listing \(A_i=(a_{i,0},\ldots,a_{i,q_i-1})\) of all symbols of each factor, and an interleaving word \(\sigma\) containing symbol \(i\) precisely \(q_i-1\) times. Starting with symbol \(a_{i,0}\) in each factor, its successive occurrences in \(\sigma\) advance along the corresponding \(A_i\). This is the product-flag factorization proved earlier in this Article.

**Theorem 4 (rotor description of the Petrie shift).** If \(\sigma=i\sigma'\), the universal full-path rank-flip shift satisfies
\[
\boxed{T(A_1,\ldots,A_r;i\sigma')
=(A_1,\ldots,\operatorname{rot}(A_i),\ldots,A_r;\sigma'i).}\tag{3}
\]
Let \(N_i(t)\) count symbol \(i\) in the first \(t\) letters of the periodic repetition of \(\sigma\). Then \(T^t\) rotates \(\sigma\) by \(t\) positions and \(A_i\) by \(N_i(t)\) positions. If \(p\) is the least positive rotation period of \(\sigma\), and \(m_i\) counts symbol \(i\) in its first \(p\) positions, then
\[
\boxed{|\mathrm{Orb}_T|=p\,\mathrm{lcm}_{1\le i\le r}
\left(\frac{q_i}{\gcd(q_i,m_i)}\right).}\tag{4}
\]
For a simplex this yields its Hamilton-order rotation period \(q_1\); for a \(d\)-cube it yields the full antipodal root-slide period \(2d\).

*Proof.* Dropping the first move of \(\sigma\) advances the root one step in factor \(i\). It leaves the remaining \(d-1\) moves in the original order. Rotating \(A_i\) makes the former initial factor symbol the new last symbol, supplying the one additional final step. This gives a complete face-graded walk with the required common suffix; uniqueness of the rank-flip shift proves (3). Iteration proves the count \(N_i(t)\). Returning to the same shuffle requires \(t=kp\); it then rotates \(A_i\) by \(km_i\) positions. All factor lists return precisely when \(q_i\mid km_i\) for every \(i\), whose least positive solution is \(k=\mathrm{lcm}_i(q_i/\gcd(q_i,m_i))\). \(\square\)

**Mathematical scope.** The common prism links, triangle-square port matching, and skew-product shift hold throughout the product-of-simplices family and preserve the original complete-path witnesses at its two extremes. The opposing color fields still have different observational degrees: unrestricted cube edge colors are antipodally odd vertex fields on a rectification, whereas unrestricted boundary triples are arbitrary reversal-odd oriented-edge fields. Theorem 2 shows why polygon lengths and incidence descent must remain visible in a color-sensitive argument. No mixed-product one-switch assertion is established here. The permutahedral counterexamples in this Article rule out promoting the local prismatic geometry alone to a universal one-switch condition.

**Proposition 5 (universal polygonal port matching).** Let \(P\) be any simple convex \(d\)-polytope, \(d\ge2\), with graph \(G\). Every oriented edge \(xy\) admits a canonical bijection \(\Theta_{xy}:N(x)\setminus\{y\}\to N(y)\setminus\{x\}\): for an edge \(xz\ne xy\), take the unique two-face \(F\) containing both \(xy\) and \(xz\), and let \(\Theta_{xy}(z)\) be the other neighbor of \(y\) on the boundary of \(F\). These maps are inverse under reversal. The corresponding polygonal residue has three vertices precisely when \(z=\Theta_{xy}(z)\), four precisely when \(x,z,\Theta_{xy}(z),y\) form an induced square, and otherwise five or more vertices.

*Proof.* The vertex figure of a simple \(d\)-polytope is a \((d-1)\)-simplex. Its edges correspond bijectively to the two-faces containing a given pair of incident original edges. In particular the \(d-1\) other edges at \(x\) correspond bijectively to the \(d-1\) two-faces containing \(xy\). The same two-faces correspond to the \(d-1\) other edges at \(y\), yielding the bijection and its reversal law. The polygon lengths give the final assertions. \(\square\)

Theorem 3 is the triangle-square specialization of Proposition 5. **In particular, the existence of a prismatic port matching alone does not exclude the permutahedral counterexamples from this Article:** they have the same local matching mechanism, with longer polygonal residues. This identifies the two-face length decoration, rather than the bare port matching, as necessary information for any strengthening along this route.
