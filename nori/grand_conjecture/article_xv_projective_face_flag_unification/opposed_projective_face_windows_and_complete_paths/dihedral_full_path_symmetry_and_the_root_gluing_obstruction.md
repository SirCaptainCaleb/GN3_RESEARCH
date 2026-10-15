# Dihedral full-path symmetry and the root gluing obstruction

# Dihedral full-path symmetry and the root-gluing obstruction

The two motivating problems have a common *dihedral* action on their complete paths. It is more extensive than the simple flag rotation, and it is faithful to the original color words. Its limitation is topological: the reflection action preserves the type-A chamber structure at each fixed root of the cube, but not the type-B adjacency that joins different roots.

**Theorem 1 (cube dihedral gallery action).** For every \(n\ge3\), let \(\mathcal G_n=\{(x;\pi):x\in\mathbb F_2^n,\ \pi\in S_n\}\) be the full cube-geodesic flags. Define
\[
T(x;\pi_1,\ldots,\pi_n)
=(x+e_{\pi_1};\pi_2,\ldots,\pi_n,\pi_1),
\qquad
R(x;\pi)=(x;\pi^{\rm rev}).
\]
Then
\[
\boxed{T^{2n}=R^2=1,\quad T^n(x;\pi)=(\bar x;\pi),\quad RTR=T^{-1}.}
\tag{1}
\]
For any antipodally odd undirected-edge coloring, if \(w(g)=(w_1,\ldots,w_n)\) is the true edge-color word of \(g\), then
\[
\boxed{
w(Tg)=(w_2,\ldots,w_n,1+w_1),\qquad
w(Rg)=(1+w_n,\ldots,1+w_1).
}
\tag{2}
\]

*Proof.* After \(n\) root slides the geodesic has used every dimension once as its first dimension, and the order returns, giving \(T^n=(x\mapsto\bar x)\) and \(T^{2n}=1\). Reversal of a complete geodesic followed by antipodal translation starts at its original root and uses the reverse dimension order, giving the second word relation. The first follows because its final edge is the antipodal translate of the initial edge. Direct calculation shows
\[
RTR(x;\pi)
=(x+e_{\pi_n};\pi_n,\pi_1,\ldots,\pi_{n-1})=T^{-1}(x;\pi).
\]
\(\square\)

**Theorem 2 (boundary-tournament dihedral gallery action).** On Hamilton vertex orders \(\pi=(v_1,\ldots,v_n)\), put \(T\pi=(v_2,\ldots,v_n,v_1)\) and \(R\pi=(v_n,\ldots,v_1)\). Then
\[
\boxed{T^n=R^2=1,\quad RTR=T^{-1}.}
\tag{3}
\]
For an arbitrary reversal-odd boundary triple coloring \(b\), define the cyclic triple array
\[
a_j=b(v_j,v_{j+1},v_{j+2}),\quad j\in\mathbb Z/n\mathbb Z.
\]
Every full Hamilton path flag in the cyclic orbit reads \(n-2\) consecutive entries of this array. \(T\) rotates the array, and \(R\) complements it and reverses its circular order, with an index shift.

*Proof.* The dihedral relations follow from operations on an ordered cycle. Cyclically rotating a vertex order rotates all consecutive cyclic triples. Reversing the order sends every ordered triple to its reverse, which changes its color by one, and reverses the cyclic sequence. \(\square\)

**Corollary 3 (opposed fixed-root type-A fibers versus root gluing).** For fixed \(x\), the \(n!\) cube flags \((x;\pi)\) form the chamber set of a type-\(A_{n-1}\) Coxeter sphere. \(R\) acts as its simplicial antipode. Swapping neighboring dimensions is a type-A chamber adjacency, and \(R\) conjugates the swap in position \(i\) to the swap in position \(n-i\).

However, \(R\) does not act simplicially on the ordinary type-B Coxeter sphere incorporating all cube roots. A type-B chamber edge may change the root across the *first* dimension without changing \(\pi\):
\[
(x;\pi)\sim(x+e_{\pi_1};\pi).
\]
Under \(R\), this becomes a root change across dimension \(\pi_1\), which is now *last* in the reversed order; those chambers are not adjacent in the type-B Coxeter complex.

Thus the required symmetry already exists on the full gallery set and on each type-A root fiber, but it is incompatible with the standard gluing between root fibers. A common topological proof could seek an alternative gluing that makes the dihedral reflection continuous without forfeiting the rank-preserving full-geodesic certificates. Simply declaring \(R\) antipodal on the type-B sphere is invalid.

**Scope.** Dihedral gallery symmetry and complemented reversal do not alone imply a low-switch complete path: unrestricted turn colorings and sparse gallery systems give obstructions. The new point is the shared *faithful* symmetry and the identification of the residual obstruction as coherence of fiber gluing rather than of word parity.
