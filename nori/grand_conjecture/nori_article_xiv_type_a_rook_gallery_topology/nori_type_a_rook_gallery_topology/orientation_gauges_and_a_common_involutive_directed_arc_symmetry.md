# Orientation gauges and a common involutive directed-arc symmetry

# Orientation gauges and a common involutive directed-arc symmetry

Let \(G\) be a finite simple graph with a fixed-point-free vertex involution \(\tau\). For a directed arc \(a=(u,v)\), write \(a^{-1}=(v,u)\). Assume that no undirected edge is fixed setwise by \(\tau\), and choose an orientation \(o\) of every edge such that \(\tau\) reverses these choices. Put \(\theta(a)=0\) if \(a\) agrees with \(o\), and \(\theta(a)=1\) otherwise. Then
\[
\theta(a^{-1})=1-\theta(a),\qquad
\theta(\tau a)=1-\theta(a).
\tag{1}
\]

**Theorem (orientation-gauge equivalence).** The formula
\[
\boxed{\beta(a)=c(\{u,v\})+\theta(a)\pmod2}
\tag{2}
\]
is a bijection from antipodally odd undirected-edge colorings \(c\), meaning \(c(\tau e)=1-c(e)\), to binary directed-arc labels satisfying
\[
\boxed{
\beta(a^{-1})=1-\beta(a),\qquad \beta(\tau a)=\beta(a).
}
\tag{3}
\]

*Proof.* Both identities follow by substituting (1) into (2). Conversely, given (3), define \(c(\{u,v\})=\beta(a)+\theta(a)\) for either directed orientation of the edge. Changing the orientation complements both summands, leaving their sum unchanged. Applying \(\tau\) preserves \(\beta\) and complements \(\theta\), so \(c(\tau e)=1-c(e)\). The two constructions are inverse. \(\square\)

**Cube specialization.** Take \(G=Q_n\) with \(\tau x=\bar x\), \(n\ge2\). Orient each dimension-\(i\) edge from its endpoint with \(x_i=0\) to its endpoint with \(x_i=1\). The orientation is reversed by \(\tau\), and \(\theta(x,x\oplus e_i)=x_i\). Consequently
\[
\boxed{
\beta(x,x\oplus e_i)
=c(\{x,x\oplus e_i\})+x_i\pmod2
}
\tag{4}
\]
gives a faithful representation of every unrestricted NORI1 coloring by the labels (3).

**Boundary-tournament specialization.** Let \(\Omega_V=\{(a,h):a\ne h\}\) be the rook states with involution \(\tau(a,h)=(h,a)\). For distinct \(a,h,c\), define
\[
\beta((a,h),(c,h))
=\beta((h,a),(h,c))
=b(a,h,c).
\tag{5}
\]
A reversal-odd boundary tournament, characterized by \(b(c,h,a)=1-b(a,h,c)\), yields the same directed-arc relations (3). Every such tournament arises this way, with independent choices at distinct middle vertices.

Equations (3) are thus a common intrinsic coloring symmetry for both full classes. Their *observable* path words retain an essential distinction: the cube geodesic reads \(\beta(a)+\theta(a)\), whereas a boundary Hamilton rook gallery reads \(\beta(a)\). The former path traverses each dimension once; the latter requires an alternating rook sequence whose type-A roots form a basis. The shared symmetry by itself does not imply a one-switch complete path, and the cubical orientation correction must be retained.
