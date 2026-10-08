# Sparse affine slope perturbations: M exceptional triples guarantee at most floor(M/[n(n−1)]) switches

# Global sparse-slope stability around the full exterior-parity affine coloring

Let n>=4. Consider ANY binary coloring c of physical ordered three-faces of Q_n that is affine in the exterior cube bits, with arbitrary orientation-dependent intercepts. For each ordered triple \(\pi=(a,b,c)\) of distinct coordinates, write its exterior coefficient vector \(A_\pi=(a_{\pi,t})_{t\notin\operatorname{set}\pi}\). Let \(P_\pi\) be the full exterior-parity coefficient vector with ALL entries 1. Let
\[
\mathcal E=\{\pi:A_\pi\ne P_\pi\},\qquad M=|\mathcal E|\le n(n-1)(n-2).
\]
The intercept bits on all triples are unrestricted. Active NORI antipodal-reversal oddness may hold but is NOT REQUIRED for this result.

**Theorem (sparse affine perturbation closure).** There exists a full antipodal directed cube geodesic whose ordered-three-face window colors change at most
\[
\boxed{\left\lfloor\frac{M}{n(n-1)}\right\rfloor}
\]
times (with the trivial cap n-3 if desired). In particular:
- If M<n(n-1), there exists a FULL MONOCHROMATIC antipodal geodesic.
- If M<2n(n-1), there exists a full antipodal geodesic with AT MOST ONE window-color change, proving the active NORI conclusion for this affine class even without imposing its oddness axiom.

**Proof.** Choose a uniformly random permutation p=(p_1,...,p_n). A fixed ordered triple \pi appears as one of its n-2 consecutive three-direction windows with probability
\[
\frac{n-2}{n(n-1)(n-2)}=\frac1{n(n-1)}.
\]
Let K(p) count the windows whose ordered triples belong to \mathcal E. By linearity of expectation,
\[
\mathbb E K(p)=\frac{M}{n(n-1)}.
\]
Therefore SOME order p satisfies K(p)≤floor(M/[n(n-1)]).

For a fixed such p, write the n-2 ordered window colors as the affine vector C_p(x)=h_p+L_p x over F2, where x is the starting root. Let L_0 be the coefficient matrix for the parity-baseline coloring with slope 1 on every exterior coordinate (but the same arbitrary intercepts); L_p-L_0 has nonzero rows at no more than K(p) exceptional windows, so rank(L_p-L_0)≤K(p). Apply consecutive difference operator \partial to obtain the (n-3)×n change matrices M_p=\partial L_p and M_0=\partial L_0. The rows of M_0 are EXACTLY
\[
e_{p_i}+e_{p_{i+3}},\quad 1\le i\le n-3,
\]
because consecutive three-face exterior masks differ only in the exiting direction p_i and entering direction p_{i+3}. These rows form the edge-incidence vectors of three disjoint paths on the coordinate positions modulo 3 and are linearly independent; hence rank M_0=n-3.

By rank perturbation,
\[
\operatorname{rank}M_p\ge n-3-K(p).
\]
The affine syndrome theorem (also proven independently: for any affine map F2^n→F2^{n-3} with rank r, its affine image contains a vector of Hamming weight at most n-3-r) yields a root x for which the full p-geodesic has at most K(p) changes. Combined with the expectation bound, this proves the claimed floor(M/[n(n-1)]) bound and its two threshold corollaries. QED.

**Interpretation.** This is a structural all-dimension closure theorem: an affine NORI coloring may perturb an arbitrary set of up to roughly \(2n^2\) orientation-triple exterior slopes away from the uniform parity baseline and still MUST have a full one-switch antipodal geodesic. The proof has TWO independent ingredients: permutation averaging to avoid most exceptional ordered triples, and a full-rank three-residue incidence matrix on the remaining windows. It is a genuine subclass result, not a proof for arbitrary nonlinear or dense exceptional-slope NORI colorings.
