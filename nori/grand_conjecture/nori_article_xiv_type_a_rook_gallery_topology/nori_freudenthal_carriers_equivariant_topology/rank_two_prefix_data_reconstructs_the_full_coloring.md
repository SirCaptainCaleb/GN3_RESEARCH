# Rank-two prefix data reconstructs the full coloring

# Rank-two monochromatic prefix triangles determine unrestricted edge colorings

For a binary coloring \(c\) of the undirected edges of \(Q_n\), \(n\ge2\), let
\[
C_x=K_x^0\cup K_x^1
\]
be the union of monochromatic geodesic-prefix Freudenthal subcomplexes rooted at \(x\). Its one-dimensional part includes every cube edge incident to \(x\), irrespective of its color. For distinct dimensions \(i,j\), let
\[
\Delta(x;i,j)=[x,x\oplus e_i,x\oplus e_i\oplus e_j]
\]
be the monotone rooted Freudenthal triangle.

**Theorem 1 (rank-two reconstruction).** Two undirected cube-edge binary colorings \(c,c'\) produce the same two-dimensional prefix triangles \(\Delta(x;i,j)\in C_x\), for all \(x\) and all distinct \(i,j\), if and only if \(c'=c\) or \(c'=1-c\) globally. The result holds without any antipodal assumption and therefore applies to the entire unrestricted NORI1 class.

*Proof.* A rooted two-step triangle occurs in \(C_x\) precisely when its two constituent edges are the same color:
\[
\Delta(x;i,j)\in C_x
\iff
c(\{x,x^i\})=c(\{x^i,x^{ij}\}).
\tag{1}
\]
The two edges in (1) are distinct edges incident at \(x^i\). Conversely, any two distinct incident cube edges have different dimensions and can be arranged in this order along some two-step geodesic, so their color equality is encoded by such a triangle. The line graph of \(Q_n\) is connected because \(Q_n\) is connected. Therefore knowledge of equality versus inequality for each pair of incident edges determines all edge colors relative to the color of one arbitrarily chosen edge. Changing that initial bit complements every edge, giving the only ambiguity. Global color complementation preserves every equality in (1), hence all the triangles. \(\square\)

**Theorem 2 (higher monochromatic prefixes are two-local).** Let
\[
x=v_0,v_1,\ldots,v_k
\]
be a cube geodesic using \(k\) distinct dimensions. For \(k\ge2\), its entire color word is monochromatic if and only if
\[
\boxed{
\Delta(v_{j-1};d_j,d_{j+1})\in C_{v_{j-1}}
\quad(1\le j<k),
}
\tag{2}
\]
where the path changes dimension \(d_j\) between \(v_{j-1},v_j\). Consequently the full family of higher-dimensional monochromatic prefix simplices is determined by the two-dimensional rooted triangle data together with the Boolean lattice's condition that each traversed dimension occurs once.

*Proof.* By (1), membership of the triangle indexed by \(j\) asserts equality of the colors of the consecutive \(j\)-th and \((j+1)\)-st edges. All these equalities hold precisely when the full word is constant. Since the dimensions are pairwise distinct, the path forms a legal geodesic prefix. Its corresponding Freudenthal simplex occurs in \(C_x\) precisely when that path has constant color. \(\square\)

**Minimality and proof direction.** The one-skeleton of the rooted prefix-cone family is color-blind, as demonstrated by the uncolored edge-star model of this Article. The anchored rank-two triangles are already sufficient to reconstruct the entire unrestricted coloring up to the irrelevant global exchange of its two bits; higher monochromatic witnesses introduce no new color comparisons, but do introduce **global compatibility of distinct dimensions**. A Wu–Yang-type chain-map modification can therefore seek a support-graded completion of these rank-two equality tests rather than an unbounded collection of auxiliary component labels. The outstanding theorem is the coherent, equivariant filling/cancellation of the resulting square-exchange defects while retaining dimension-simplicity.
