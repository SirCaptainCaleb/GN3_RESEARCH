# Exact signed-root nerve has no mixed topology unless a monochromatic geodesic reaches at least half the cube

# Half-length threshold: when the exact NORI signed-root reachability nerve has no mixed topology

Fix n>=5 and any binary coloring of physical ordered three-faces of Q_n, with the active antipodal-reversal oddness imposed when relating this statement to the NORI grand conjecture. Let \(M(c)\) be the maximum number of distinct-coordinate edges in a monochromatic ordered-three-face-window geodesic anywhere in the cube. Define the exact color-free terminal-two-tail support families \(\mathcal R_J(x)\) and the signed-root profile nerve N as in Items nori_exact_color_free_reversed_two_tail_complement_reachability_grand_equivalence_20261008 and nori_reversed_tail_root_profile_nerve_tucker_label_reduction_20261008.

**Theorem (necessary long monochromatic carrier for ANY mixed shore edge).** If the signed-root nerve N has ANY mixed edge \((x,+)(y,-)\), even with x≠y, then
\[
\boxed{M(c)\ge\left\lceil\frac{n+2}{2}\right\rceil.}
\]
Consequently, if \(M(c)<\lceil(n+2)/2\rceil\), the entire signed-root nerve is EXACTLY the disjoint union of its two universal full root simplices
\[
\boxed{N=\Delta_+\sqcup\Delta_-},
\]
and is equivariantly homotopy equivalent to \(S^0\), with cohomological \(\mathbb Z_2\)-index zero. The same conclusion holds for the exact formal-label profile carrier K of the cited nerve theorem. In particular, if the ACTIVE NORI grand conjecture holds for c, it necessarily satisfies \(M(c)\ge\lceil(n+2)/2\rceil\).

**Proof.** A mixed edge exists exactly when some ordered pair of tail directions J=(a,b), some nonempty proper U⊊D_J=[n]\{a,b}, and some roots x,y satisfy
\[
U\in\mathcal R_J(x),\qquad
D_J\setminus U\in\mathcal R_{\operatorname{rev}J}(y).
\]
By the definition of these *actual* reachability families, there are monochromatic geodesics of lengths \(|U|+2\) and \(|D_J\setminus U|+2=n-|U|\). Their lengths sum exactly n+2. Hence at least one has length ≥ceil((n+2)/2), proving the bound.

If M is smaller than that threshold, no mixed edge can exist. The positive signed-root vertices form one simplex, and the negative signed-root vertices another, by the universal singleton-support witness common to every root. Every simplex containing both signs would contain a mixed edge, so there are no other simplices. Thus N is precisely two exchanged simplices, and each contracts to a point equivariantly. The formal-label carrier K is equivariantly homotopy equivalent to N by the previously proved nerve equivalence. Finally, a full good NORI geodesic gives a SAME-root mixed edge by the exact reversed-tail splice theorem, so it enforces the same threshold. QED.

**Further sharp threshold.** If M>=n-1, grand one-switch closure follows immediately, WITHOUT antipodal oddness: append the unique unused coordinate to a length-(n-1) monochromatic path. The new full n-geodesic has one additional three-face window, hence at most one color change. Thus the difficult regime is
\[
\lceil(n+2)/2\rceil\le M\le n-2.
\]
In that regime mixed-shore topology becomes possible, but no universal mixed edge is yet forced.

**Research consequence.** A Tucker/KKM/fixed-point proof based specifically on this actual signed-root nerve must first establish a sufficiently long monochromatic geodesic or obtain an independent carrier construction that creates mixed shore simplices without presupposing them. Otherwise the carrier has no positive-dimensional free antipodal topology and cannot support a higher-index forcing argument. This is a concrete dependency, not a proof of the grand conjecture.
