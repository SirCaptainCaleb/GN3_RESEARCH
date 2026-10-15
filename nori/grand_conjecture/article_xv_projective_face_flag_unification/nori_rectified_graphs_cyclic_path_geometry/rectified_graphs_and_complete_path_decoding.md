# Rectified graphs and complete path decoding

# Rectified graphs and complete path decoding

Rectification gives a natural geometric carrier for both unrestricted original coloring classes. Let \(L(G)\) be the line graph of a simple graph \(G\): its vertices are edges of \(G\), with adjacency whenever the original edges meet.

**Lemma 1 (universal star-alternation).** A line-graph path \(e_1,\ldots,e_m\) whose vertices are distinct comes from a consistently oriented edge-by-edge trail in \(G\) if and only if, for each interior edge \(e_j\), its intersection with \(e_{j-1}\) is the endpoint of \(e_j\) opposite from its intersection with \(e_{j+1}\). The decoded trail is then unique. This is the same local condition for every graph: the incoming and outgoing line-graph edges must meet the two distinct endpoint stars of the interior original edge.

*Proof.* An oriented trail must enter one endpoint of each interior edge and exit the other. Conversely these choices propagate the orientation from its initial edge. \(\square\)

**Theorem 2 (rectified cube).** Let \(Q_n=[-1,1]^n\), \(n\ge3\), and let \(R_n\) be the convex hull of its edge midpoints. Then
\[
\boxed{
R_n=[-1,1]^n\cap\{z:\textstyle\sum_i|z_i|\le n-1\}.
}
\]
Its one-skeleton is \(L(Q_n)\); its two-faces are precisely the star triangles (three cube edges incident at an original cube vertex) and cube-face squares (midpoints of four edges on an original square). Hence the triangle-square complex constructed in the preceding subsection is the two-skeleton of the convex sphere \(\partial R_n\cong S^{n-1}\). Cube antipodality acts as central inversion, so the quotient sphere is \(\mathbb RP^{n-1}\).

*Proof.* The displayed intersection cuts off every cube vertex along the hyperplane through its incident edge midpoints. Its facets are of two kinds: \(z_i=\pm1\), giving copies of \(R_{n-1}\), and \(\sum_i\epsilon_i z_i=n-1\), giving simplices whose vertices are the \(n\) incident edge midpoints at the original cube vertex \(\epsilon\). For \(n=3\) the polytope is the cuboctahedron, with twelve vertices, eight triangles, and six squares, and its graph is the line graph of the cube. Induct on \(n\): all lower-dimensional faces lie in the listed facets. The original-facet recursion yields the cube-square faces, while the cut-off vertex simplices yield all star triangles and adjacency of all pairs of incident cube edges. No other one- or two-faces arise. Central inversion of the original cube preserves this midpoint polytope and is antipodal on its boundary. \(\square\)

**Theorem 3 (rectified simplex).** For a simplex on \(n\ge3\) vertices, its rectification, after rescaling, is the hypersimplex
\[
\boxed{\Delta(2,n)=
\operatorname{conv}\{e_a+e_h:a\ne h\}
=\{z\in[0,1]^n:\sum z_i=2\}.}
\]
Its one-skeleton is the Johnson graph \(J(n,2)=L(K_n)\). An oriented edge
\[
\boxed{\{a,h\}\longrightarrow\{h,c\}}
\]
of the hypersimplex uniquely specifies an ordered triple \((a,h,c)\). Reversing the edge reverses the outer symbols. Therefore **every unrestricted reversal-odd boundary 3-tournament is precisely an arbitrary orientation of the edges of a rectified simplex**.

*Proof.* Hypersimplex vertices sharing the symbol \(h\) lie in the simplex face \(z_h=1\), so their segment is an edge. Vertices corresponding to disjoint pairs cannot be adjacent: their midpoint is also the midpoint of a distinct pairing of the same four symbols. Thus adjacency means sharing one symbol, and the common symbol gives the unique center \(h\). A binary choice on each oriented edge, odd under direction reversal, is the same as independently orienting every undirected Johnson-graph edge. \(\square\)

**Corollary 4 (common complete rectified paths).** A Hamilton order \(v_1,\ldots,v_n\) in the original simplex gives the star-alternating hypersimplex path
\[
\{v_1,v_2\},\{v_2,v_3\},\ldots,\{v_{n-1},v_n\},
\]
whose oriented-edge labels are precisely the tournament's consecutive triple word. A full antipodal cube geodesic similarly yields a star-alternating rectified-cube path of \(n\) vertices, one for each original dimension. Its original edge colors are vertex labels of the rectified cube; taking their chiral-corrected finite difference produces the reversal-odd oriented-edge labels from the preceding subsection. Both families use the same local star-alternation condition, and both retain their original completeness requirements.

**Research direction.** The two unrestricted problems become neighboring degrees of a shared graded incidence setup: NORI1 gives an antipodally odd vertex field on a rectified cube and its reversal-odd turn derivative; boundary tournaments give arbitrary reversal-odd oriented-edge fields on a rectified simplex. Neither arbitrary oriented rectified graphs nor arbitrary projective face-window colorings alone suffice for a low-switch theorem; the complete-path structure and local rank-two relations remain indispensable.
