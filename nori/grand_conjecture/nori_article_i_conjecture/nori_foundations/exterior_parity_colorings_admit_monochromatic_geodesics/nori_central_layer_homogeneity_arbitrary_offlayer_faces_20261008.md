# Two homogeneous central layers force closure despite arbitrary off-layer face dependence

CENTRAL-LAYER HOMOGENEITY SUFFICES; ALL OTHER FACE DEPENDENCE IS FREE.

Let n be even, n>=4, k=(n-4)/2. Let c be an arbitrary binary coloring of ordered three-faces of Q_n satisfying NORI oddness c(bar F,rev pi)=1+c(F,pi). Assume ONLY the following central-layer homogeneity: for each ordered free triple pi there exist bits a(pi),epsilon(pi) such that
 c(F,pi)=a(pi) for EVERY face F whose exterior Hamming weight K(F)=k;
 c(F,pi)=a(pi)+epsilon(pi) for EVERY face F with K(F)=k+1.
The colors of faces at all other exterior Hamming weights may depend arbitrarily on the entire exterior bitstring and on pi, subject only to NORI oddness.

THEOREM (genuinely face-dependent central two-layer reduction). The NORI involution forces epsilon(rev pi)=epsilon(pi) and a(rev pi)=1+a(pi)+epsilon(pi). For every coordinate order p, the constant-central starts and the prescribed central-jump roots of the three-chain theorem yield exactly the same color words as in the radial normal form:
 W_i(p,j)=a(pi_i)+epsilon(pi_i)*1_(i>j),
 Wdown_i(p,j)=a(pi_i)+epsilon(pi_i)*1_(i<=j).
Thus any p,j for which either explicit word has at most one change certifies full NORI closure for this coloring. In particular, if epsilon=1 on all ordered triples and there is an order whose a-word has at most two color changes, then a full one-change antipodal geodesic exists. If epsilon=1 and some a-word has exactly one change, a monochromatic geodesic exists.

PROOF. The antipodal of a k-layer ordered face is a (k+1)-layer face because n-3=2k+1, with free order reversed. Evaluating NORI oddness on the two central weights yields the stated relations. All constructed roots have K_i entirely within {k,k+1}; hence their face colors are determined exactly by (a,epsilon), regardless of the values assigned on every other face. Substitute their weight profiles into the two displayed homogeneous-layer formulas. The resulting binary words are precisely W and Wdown, and the color-change conclusions follow. QED.

ODD-DIMENSION ANALOGUE. If n is odd and m=n-3 is even, impose homogeneity only on the unique self-complementary middle layer K=m/2. NORI then makes the induced coordinate-only triple label a(pi) reversal-odd. A constant-middle-layer start exists for every direction order. Consequently every one-change a-order transfers to a full NORI one-change geodesic, with arbitrary face-dependent values away from the middle layer.

SIGNIFICANCE. Global Hamming-radial dependence is UNNECESSARY: one or two middle layers alone suffice. This is an exact enlargement to true nonlinear and nonradial ordered-face colorings. The unresolved general NORI case is the presence of arbitrary variation WITHIN the central Hamming layers; proving exchange/coherence across their exterior bitstrings is now the precise additional task.
