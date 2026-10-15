# Equivariant component-nerve map and the fixed-incidence-edge threshold

# Equivariant component-nerve map and the fixed-incidence-edge threshold

Let \(K_0,K_1\) be finite simplicial complexes embedded as subcomplexes of a common complex. Let \(K=K_0\cup K_1\) and \(I=K_0\cap K_1\). Assume a simplicial involution \(R\) exchanges \(K_0\) and \(K_1\). For antipodally odd cube-edge colorings, the application is to the red and blue directed geodesic endpoint-poset complexes, with \(R(u,v)=(\bar v,\bar u)\).

Let \(\Gamma\) be the bipartite **component incidence graph**: each vertex is a connected component of one of the two color complexes; for each pair of components that intersect, give \(\Gamma\) an edge joining them. The involution exchanges the two vertex classes. A simplex of \(I\) belongs to one red and one blue component, yielding one incidence edge.

**Theorem 1 (equivariant nerve map).** There is a canonical piecewise-linear map
\[
\boxed{\nu:|K|\longrightarrow|\Gamma|}
\tag{1}
\]
that is \(R\)-equivariant, induces a bijection on connected components, and induces a surjection on the fundamental group and on first integral homology of each connected component.

*Proof.* Use the barycentric subdivision of \(K\). For each nonempty simplex \(\sigma\in K\), assign its barycenter as follows:
- If \(\sigma\in K_0\setminus I\), assign the vertex of \(\Gamma\) representing its component of \(K_0\).
- If \(\sigma\in K_1\setminus I\), assign the corresponding blue vertex.
- If \(\sigma\in I\), assign the midpoint of the incidence edge connecting the red and blue components containing \(\sigma\).

These assignments are compatible with inclusions of simplices. If \(\sigma\subseteq\tau\), then either both are in \(I\), in which case they belong to the same red and blue components and are assigned the same midpoint, or \(\tau\) lies in one color but not in \(I\), in which case the assigned points lie in the closed half-edge incident with its color component. The case of a simplex of one color being a face of a simplex belonging only to the opposite color cannot occur. Affine interpolation over the simplices of the barycentric subdivision therefore defines the continuous piecewise-linear map (1). The rule is symmetric under \(R\), so \(\nu(Rx)=R\nu(x)\).

The component-incidence criterion proved previously establishes that \(\pi_0(K)\cong\pi_0(\Gamma)\). To prove surjectivity on \(\pi_1\), choose a base vertex inside each color component and, for each incidence edge \(e\) of \(\Gamma\), choose a simplex of the corresponding red-blue intersection. A traversal of \(e\) lifts to a path in \(K\) from the chosen base vertex of its red component to that of its blue component, passing through the chosen intersection simplex. Such paths exist because the individual color components are path connected. Their images under \(\nu\) are homotopic relative endpoints to the corresponding incidence edge: within one color component the image stays inside the closed star of its incidence vertex, which is a tree, and the chosen intersection simplex maps to the midpoint of \(e\). Concatenating these lifted paths around any graph loop provides a loop in \(K\) whose image is homotopic to that graph loop. This proves surjectivity of \(\pi_1\), and hence of \(H_1(-;\mathbb Z)\). \(\square\)

**Theorem 2 (free-nerve covering-index collapse).** Suppose \(R\) fixes no incidence edge of \(\Gamma\) setwise. Then it acts freely on \(|\Gamma|\) and on \(|K|\), and the covering class
\[
\alpha=w_1(K\to K/R)\in H^1(K/R;\mathbb F_2)
\]
satisfies
\[
\boxed{\alpha^2=0.}
\tag{2}
\]

*Proof.* The involution exchanges the red and blue vertex sets of \(\Gamma\); hence it fixes no graph vertex. A simplicial involution on a graph without fixed vertices has a fixed point in the realization precisely when some edge is setwise invariant, with its two endpoints exchanged. The hypothesis therefore makes \(\Gamma\) a free \(R\)-graph. Because \(\nu\) is equivariant, any fixed point of \(R\) in \(K\) would map to a fixed point in \(\Gamma\); thus \(R\) is also free on \(K\).

The equivariant map \(\nu\) induces a map \(\bar\nu:K/R\to\Gamma/R\) between orbit spaces, and the cover \(K\to K/R\) is the pullback of the double cover \(\Gamma\to\Gamma/R\). Therefore \(\alpha=\bar\nu^*\beta\), where \(\beta=w_1(\Gamma\to\Gamma/R)\). Since \(\Gamma/R\) is a graph, \(H^2(\Gamma/R;\mathbb F_2)=0\), hence \(\beta^2=0\). Pullback gives (2). \(\square\)

**Corollary 3 (a native red-blue condition for higher covering index).** In an antipodally odd coloring, write \(C_0(p)\) for the red component of a bi-monochromatic endpoint pair \(p\in I\), and let \(A(u,v)=(\bar u,\bar v)\), \(J(u,v)=(v,u)\). An incidence edge is preserved setwise by \(R=AJ\) if and only if
\[
\boxed{C_0(Ap)=J C_0(p).}
\tag{3}
\]
Equivalently, \(p\) and \(Rp\) belong to the same red component and to the same blue component.

If a coloring with no monochromatic full antipodal geodesic has \(\alpha^2\ne0\) on its endpoint quotient, then there must exist a bi-monochromatic pair \(p\) satisfying (3). No other color-incidence configuration can support a nonzero square of the reversal covering class.

*Proof.* Identify blue components with red components by \(A\), as in the preceding odd-walk theorem. An incidence edge is represented by \((C_0(p),0)\sim(C_0(Ap),1)\), while \(R\) maps its endpoints to \((JC_0(p),1)\) and \((JC_0(Ap),0)\). The edge is invariant precisely when \(C_0(Ap)=JC_0(p)\), which also implies the companion equality by applying \(J\) and \(A\). The same condition says the pair \(p,Rp\) lies in each of the red and blue connected components incident with this edge. The final claim is the contrapositive of Theorem 2. \(\square\)

**Research implication.** The equivariant index beyond one is forced to reside near an incidence edge that reversal fixes setwise in the component nerve. Such a fixed *nerve edge* does not mean the original endpoint complex contains a reversal-fixed simplex: distinct intersection simplices may realize the same component incidence and be exchanged freely by \(R\). This distinction prevents a false direct proof of NORI1 from the existence of (3). Theorem 2 nevertheless identifies a precise class of color configurations whose entire endpoint-complex double-cover obstruction collapses in degree two. It refines the general half-dimensional vanishing bound of Article XIV, without claiming that a high index must occur in every coloring.
