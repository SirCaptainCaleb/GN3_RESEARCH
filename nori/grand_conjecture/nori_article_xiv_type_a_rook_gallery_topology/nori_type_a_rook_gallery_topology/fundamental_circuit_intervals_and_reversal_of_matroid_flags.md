# Fundamental-circuit intervals and reversal of matroid flags

# Fundamental-circuit intervals and reversal of matroid flat flags

Let \(M\) be a loopless rank-\(n\) matroid with basis \(B\). For \(e\in B\), set \(D_B(e)=\{e\}\); for \(e\notin B\), take \(D_B(e)\) to be the basis elements in the unique circuit of \(B\cup\{e\}\). These sets are nonempty by looplessness. For any ordering \(\pi\) of \(B\), let \(a_\pi(e)\) and \(b_\pi(e)\) be the minimum and maximum positions of the members of \(D_B(e)\), and let \(w_\pi(e)=b_\pi(e)-a_\pi(e)\).

**Theorem (two-end reversal and exchange).** The matroid-Sperner labeling induced by the nested flats \(F_j^\pi=\operatorname{cl}_M\{\pi_1,\ldots,\pi_j\}\) satisfies
\[
\boxed{\ell_\pi(e)=b_\pi(e),\quad
\ell_{\pi^{\rm rev}}(e)=n+1-a_\pi(e),\quad
\ell_\pi(e)+\ell_{\pi^{\rm rev}}(e)=n+1+w_\pi(e).}
\]
For adjacent Coxeter exchange \(\pi'=\pi s_j\),
\[
\boxed{|w_{\pi'}(e)-w_\pi(e)|\le1.}
\]
Under reversal, the support interval \([a_\pi(e),b_\pi(e)]\) becomes \([n+1-b_\pi(e),n+1-a_\pi(e)]\). Scalar reversal complementarity \(\ell_{\pi^{\rm rev}}(e)=n+1-\ell_\pi(e)\) holds precisely when \(D_B(e)\) is a singleton.

*Proof.* For \(A\subseteq B\), one has \(e\in\operatorname{cl}_M(A)\) if and only if \(D_B(e)\subseteq A\), by uniqueness of the fundamental circuit (and independence when \(e\in B\)). Thus \(e\) first enters the nested flat chain at its last support position \(b_\pi(e)\). Reversing the basis order sends each position \(j\) to \(n+1-j\), proving both label identities and interval reflection. An adjacent exchange either swaps two support members, swaps two nonsupport members, or moves a single support member by one position. In the first two cases the interval is unchanged. In the third, at most one interval extreme moves when the support contains at least two elements; if the support is singleton both extremes move together. Hence its width changes by at most one. The width is zero if and only if its support has one member. \(\square\)

**Partition-matroid specialization and NORI caveat.** In the signed-dimension partition matroid \(\bigoplus_i U_{1,2}\), every element has singleton fundamental support, so the scalar Sperner label obeys simple reversal complementarity. In a general matroid, circuits supported on multiple basis elements create the positive reversal defect \(w_\pi(e)\). Complete Boolean-flat flags are indexed by permutations: basis relabeling acts on the left, while flag reversal acts on the right by the longest permutation \(w_0\); they commute. The latter reverses flat ranks and is not a rank-preserving basis permutation. Thus the 2015 matroid-Sperner theorem supplies a useful ordered-flat-chain mechanism but not automatically the antipodal oddness or the compatible monochromatic path data required by the preceding Bockstein chain-transfer criterion.
