# Balanced cubes with exponentially sparse two-sweep roots among monochromatic-geodesic roots

- Stable ID: note_cbff1d0ca5b44250a00331ce
- Author: unspecified; session provenance retained
- Primary home: subsection:paired_direction_involutions_and_geodesic_endpoint_matchings
- Labels: NORI1, two-sweep, balanced, rootwise-obstruction, Cartesian-products
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r10003_3
- Updated session: session_nori_r10003_3
- Disposition: none
- Successor: none

## Related references

- note:note_e5b581e8e2c4615b297e9252

## Research note

For a legal antipodally odd binary edge-coloring c of Q_n, let \(G(c)\) denote the roots admitting a color-zero full antipodal geodesic, and let \(W_2(c)\) denote the roots admitting an order pi for which \(U_\pi^2(x)=\bar x\). Every root in \(W_2(c)\) lies in \(G(c)\).

**Theorem (exponentially sparse two-sweep roots conditioned on monochromatic-geodesic roots).** For every integer r>=1 there is a balanced antipodally odd coloring b_r of Q_(8r) for which
\[
\boxed{|G(b_r)|=2^{4r}14^r,\qquad |W_2(b_r)|=2^{4r}12^r,\qquad
\frac{|W_2(b_r)|}{|G(b_r)|}=(6/7)^r.}\tag{1}
\]
Thus even conditioned on the existence of a monochromatic full antipodal geodesic at a prescribed root, the probability that the same root supports a reversible two-sweep witness can decay exponentially with dimension.

*Proof.* Begin with the affine antipodally odd coloring a of Q_4 defined by bit-indexed rules
\[
c_0(x)=x_1,\quad c_1(x)=x_2,\quad c_2(x)=x_3,\quad c_3(x)=x_0+x_1+x_2\pmod2.
\]
Each rule ignores its own bit and changes under total bitwise complementation. A finite enumeration of the 16 vertices and 24 direction orders gives
\[
G(a)=\{1,2,\ldots,14\},\qquad
W_2(a)=G(a)\setminus\{6,9\},
\]
using integer vertices x=sum_i 2^i x_i. For reproducibility, for each root x and order pi, compute the successive original path colors \(c_{\pi_j}(x+\sum_{\ell<j}e_{\pi_\ell})\); x lies in G(a) if some order gives four zeros. Compute \(F_\pi(x)\) by scanning pi and flipping bit i whenever its incident c_i value is zero; x lies in W_2(a) if \(F_\pi(F_\pi(x))=x+1111\) for some order. The resulting rooted full-geodesic counts at vertices x=0,...,15 are (0,1,2,1,3,2,1,2,2,1,2,3,1,2,1,0). The two-sweep witness counts per root are (0,2,1,1,2,2,0,4,4,0,2,2,1,1,2,0). These displayed 16-entry arrays provide independent certificates of the root sets. In particular the zero geodesic 6 -> 2 -> 0 -> 8 -> 9 in order (2,1,3,0) starts from root 6 even though none of the 24 sweep orders succeeds twice from root 6.

For any independent product of colorings a,d, a full color-zero antipodal geodesic projects onto a color-zero full antipodal geodesic of each factor, and conversely factor paths concatenate. Therefore \(G(a\boxtimes d)=G(a)\times G(d)\). Every full sweep on the product factors as the two corresponding factor sweeps, because swaps in disjoint blocks commute; any factor orders admit an interleaving. Therefore \(W_2(a\boxtimes d)=W_2(a)\times W_2(d)\). For the r-fold product c=a^(box r) on Q_(4r), these laws give |G(c)|=14^r and |W_2(c)|=12^r.

Finally apply the paired balanced lift L(c) on Q_(8r). The established rootwise lift identities give \(G(L(c))=G(c)\times Q_{4r}\) and \(W_2(L(c))=W_2(c)\times Q_{4r}\). The first follows by projecting all original-direction moves and placing every dummy move before or after the full zero geodesic according to its color; the second follows from the paired-sweep conjugacy \(T\tilde F_\rho T^{-1}(x,z)=(F_\pi(x),z+\mathbf1)\), plus projection for arbitrary lifted orders. The lift is antipodally odd and balanced. Thus b_r=L(c) satisfies (1). QED.

The theorem rules out any rootwise conversion of monochromatic antipodal geodesics into reversible two-sweep witnesses, even with vertex balance. It does not refute the existential two-sweep conjecture, which requires only one successful root somewhere.
