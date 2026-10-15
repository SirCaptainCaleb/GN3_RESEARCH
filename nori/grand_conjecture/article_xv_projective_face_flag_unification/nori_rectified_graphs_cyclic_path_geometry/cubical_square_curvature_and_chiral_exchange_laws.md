# Cubical square curvature and chiral exchange laws

# Cubical square curvature and chiral exchange laws

Let \(c\) be any antipodally odd binary undirected-edge coloring of \(Q_n\), and choose an antisymmetric chirality bit \(\chi(i,j)\) on ordered distinct dimensions, so \(\chi(j,i)=1+\chi(i,j)\). For a square face with initial vertex \(x\) and dimensions \(i\ne j\), write
\[
a=c(\{x,x+e_i\}),\quad
b=c(\{x+e_i,x+e_i+e_j\}),\quad
a'=c(\{x,x+e_j\}),\quad
b'=c(\{x+e_j,x+e_i+e_j\}).
\]
Put
\[
\boxed{\kappa_{ij}(x)=a+b+a'+b'.}
\tag{1}
\]
The bit \(\kappa_{ij}\) is attached to the undirected square face and does not depend on the choice of its initial vertex or order of \(i,j\).

**Theorem 1 (chiral turn exchange).** The two ordered turns that run across opposite corners of the square have labels
\[
B_x(i,j)=a+b+\chi(i,j),\qquad
B_x(j,i)=a'+b'+\chi(j,i),
\]
and satisfy
\[
\boxed{B_x(i,j)+B_x(j,i)=1+\kappa_{ij}(x).}
\tag{2}
\]
Thus changing the order of two dimensions complements their local reversal-odd turn bit precisely when the square has zero curvature; it preserves the bit when curvature is one. Moreover \(\kappa_{ij}\) equals the XOR of the two underlying uncorrected switch indicators for the opposite two-step routes.

*Proof.* Add the two equations and use antisymmetry of \(\chi\); the sum of the four edge colors is (1). The two original switch indicators are \(a+b\) and \(a'+b'\), whose sum is \(\kappa_{ij}\). \(\square\)

**Theorem 2 (three-dimensional Bianchi relation).** For pairwise distinct dimensions \(i,j,k\), the six square faces of their three-dimensional subcube obey
\[
\boxed{
\kappa_{ij}(x)+\kappa_{ij}(x+e_k)
+\kappa_{ik}(x)+\kappa_{ik}(x+e_j)
+\kappa_{jk}(x)+\kappa_{jk}(x+e_i)=0.
}
\tag{3}
\]
Further,
\[
\boxed{\kappa_{ij}(\bar x)=\kappa_{ij}(x).}
\tag{4}
\]

*Proof.* Each of the twelve undirected edges of the three-dimensional subcube occurs in precisely two of the six square boundaries. Summing their edge-color sums modulo two therefore gives zero. Under antipodal translation, the four edge colors of a square are all complemented, so their XOR is unchanged. \(\square\)

**Corollary 3 (linear curvature versus monochromatic square defects).** Write \(\delta_{ij}(x)=a+b\) and \(\delta_{ji}(x)=a'+b'\) for the adjacent switch indicators of the two opposite routes across the square. Then
\[
\boxed{\delta_{ij}(x)+\delta_{ji}(x)=\kappa_{ij}(x).}
\tag{5}
\]
Consequently zero square curvature means the two routes have the same switch status (both monochromatic or both mixed), whereas curvature one means precisely one route is monochromatic. Unlike the previously studied nonlinear color-specific square defect, this linear curvature records exchange compatibility of the switch predicate itself, without choosing a preferred color.

**Structural implication.** The curvature \(\kappa\) is the cubical two-coboundary of the underlying edge-color one-cochain \(c\); its Bianchi relation is the cochain identity \(d^2c=0\). The local chiral turn law (2) makes the same curvature govern adjacent dimension exchanges on complete geodesic flags. The identity holds for every unrestricted NORI1 coloring, independent of its geodesic existence status.

A boundary tournament has arbitrary local reversed-triple bits and hence need not have vanishing triangle curvature after subtracting a reference chirality. The challenge for a unified chain argument is therefore to use (2)–(3) where the carrier possesses square exchanges, while permitting unrestricted triangular reversal data in its simplex realization. Requiring all chiral turn cochains to be flat would discard ordinary boundary tournaments.
