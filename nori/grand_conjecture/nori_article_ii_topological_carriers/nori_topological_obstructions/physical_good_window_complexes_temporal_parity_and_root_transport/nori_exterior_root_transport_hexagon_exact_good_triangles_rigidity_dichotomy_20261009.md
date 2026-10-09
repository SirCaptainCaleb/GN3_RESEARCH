# Genuine exterior-root transport hexagons: selective good triangles and exact rigidity obstruction

# Exact exterior-root transport hexagon: two selective triangles, repair–rigidity, and no automatic prism filling

Let \(n\ge5\), let \(c\) be an arbitrary binary coloring of actual ordered physical three-faces of \(Q_n\) (the active NORI oddness may be imposed but is unnecessary for the main incidence statements). Fix a vertex \(z\) and FIVE distinct directions \(a,b,c,d,e\). Write \(W_z(abc)\) for the actual ordered three-face through \(z\) with free directions \((a,b,c)\). Here the repeated letter \(c\) inside ordered tuples denotes a coordinate, independently of the coloring function. Let \(z'=z\oplus e_e\), and define SIX actual ordered windows
\[
 U_0=W_z(abc),\quad V_0=W_z(bcd),\quad
 M=W_z(cde),\quad V_1=W_{z'}(bcd),\quad
 U_1=W_{z'}(abc),\quad T=W_z(bce).
\]
Because \(e\) lies outside \(\{a,b,c,d\}\), the pairs \(U_0,U_1\) and \(V_0,V_1\) are DISTINCT physical faces, despite having the same ordered direction tuples.

**Theorem 1 (universal literal hexagon).** The six ordered windows are distinct and form a simple six-cycle
\[
\boxed{U_0-V_0-M-V_1-U_1-T-U_0}
\]
in the ACTUAL physical window-shift graph. Every displayed edge is the consecutive pair of ordered faces on a genuine 4-edge direction-distinct cube geodesic. Hence every edge belongs to the genuine good-window complex \(W_{\rm good}\) for EVERY coloring.

*Proof.* Their respective ordered tuples are
\[
 abc,\ bcd,\ cde,\ bcd,\ abc,\ bce.
\]
Adjacent pairs have the exact suffix/prefix two-coordinate overlap (taking the reverse orientation on edges traversed backwards). The relevant physical common hubs are \(z\) for \(U_0,V_0\) and \(V_0,M\); \(z'=z\oplus e\) for \(M,V_1\), \(V_1,U_1\), and \(U_1,T\); and \(z\) for \(T,U_0\). The free coordinate \(e\) of \(M,T\) makes \(W_z(cde)=W_{z'}(cde)\) and \(W_z(bce)=W_{z'}(bce)\). For any such adjacent two-window pair through a common vertex, the four-direction word supplies a real four-edge geodesic: choose its root to make the common hub the position after its first direction. Any length-four path has only two ordered-three-face windows and is automatically <=1-switch. The four different triple types distinguish windows except \(U_0,U_1\), \(V_0,V_1\), and these have exterior \(e\)-bits differing, so all six are distinct. QED.

**Theorem 2 (complete INDuced six-vertex good-window complex).** Among these six actual windows, the only POSSIBLE non-hexagon graph edges in \(W_{\rm good}\) are the two chords \(U_0M\) and \(U_1M\). Moreover:
- \(U_0M\) occurs iff \((U_0,V_0,M)\) is an ACTUAL one-switch five-edge geodesic triple, equivalently iff the three colors do NOT alternate. In that event, the unique corresponding 2-simplex \(\{U_0,V_0,M\}\) occurs.
- \(U_1M\) occurs iff \((U_1,V_1,M)\) is an actual one-switch five-edge geodesic triple, equivalently iff those three colors do NOT alternate. In that event, the 2-simplex \(\{U_1,V_1,M\}\) occurs.
- No other 2-simplex and no 3-simplex on these six vertices occurs.

*Proof.* Apply the exact physical ordered-window incidence test. Overlapping ordered tuples at separation one require literal suffix/prefix length-two agreement and compatible common fixed exterior bits, ruling out \(U_0V_1,U_1V_0\), the parallel pairs \(U_0U_1,V_0V_1\), and pairs involving \(T\) beyond its two hexagon neighbors. The triples \(abc,cde\) share only \(c\), in the last and first positions respectively, so their possible separation is exactly two, and their unique prescribed intermediate tuple is \(bcd\). For \(U_0,M\), the first face fixes exterior \(e\) to the original bit of \(z\); thus the true intervening \(bcd\)-window is exactly \(V_0\). For \(U_1,M\), it is exactly \(V_1\). Each corresponding genuine length-five path is one-switch iff its three colors are not alternating; no alternative physical intermediate face can repair an alternating triple. Any simplex requires a SINGLE common actual good-geodesic witness. The only ordered-three-tuples compatible with three different windows among these six are the displayed two chains \(abc\to bcd\to cde\). Hence precisely these 0, 1, or 2 triangle/chord pairs appear and nothing else. QED.

**Corollary (no automatic good-window prism).** The induced subcomplex on the six windows simplicially collapses to the displayed hexagon: each optional chord belongs to exactly one optional triangle, so the optional triangle/chord pairs can be removed by elementary collapses. Its intrinsic homotopy type is \(S^1\), regardless of the coloring. However its intrinsic temporal parity evaluates to \(\beta(C_6)=6=0\), and this induced \(S^1\) may become nullhomologous through ADDITIONAL physical windows in the full \(W_{\rm good}\). The result alone establishes neither a nontrivial ambient homology class nor an annulus.

**Theorem 3 (exact one-bit repair-versus-rigidity dichotomy).** Denote the six window colors by \(u_0,v_0,m,v_1,u_1,t\in\mathbb F_2\). Both possible good 5-geodesic triangles are ABSENT if and only if
\[
\boxed{u_0=u_1=m,\qquad v_0=v_1=1-m.}
\]
Equivalently, either the exterior-root move \(z\to z'\) gives at least ONE genuine <=1-switch 5-geodesic through \(M\), or it fixes the colors of both endpoint ordered faces \(U_0,U_1\) and \(V_0,V_1\) separately and leaves their same-hub comparison stubbornly bichromatic. In particular, if either ordered face is sensitive to this exterior \(e\)-bit, a literal good 5-geodesic triangle is FORCED. Even when good triangles occur, the preceding corollary shows their presence does not automatically fill the transport hexagon.

*Proof.* A 3-bit word is bad for one-switch exactly when it is alternating, i.e. first and third bits coincide and are opposite the second. The two candidate triangles have respective actual color words \((u_0,v_0,m)\) and \((u_1,v_1,m)\); both alternating gives precisely the boxed identities. QED.

**Local obstruction coloring (shows the rigid case is real under ACTIVE NORI).** Assign color 0 to EVERY physical ordered face whose ordered tuple is \((a,b,c)\), color 1 to EVERY physical ordered face of ordered tuple \((b,c,d)\), and color 0 to EVERY physical ordered face of ordered tuple \((c,d,e)\). The three reversed orientation types \((c,b,a),(d,c,b),(e,d,c)\) are distinct from these three and must get their opposite colors. Complete all other ordered-face antipodal-reversal orbits arbitrarily. This is a globally legal active NORI coloring. Every transport hexagon with this fixed direction word has BOTH candidate triples alternating \(0,1,0\), across every hub. Thus one cannot force a triangle on each prescribed exterior-root transport hexagon by oddness alone.

**Gauge versus genuine root motion.** For a horizontal comparison of ordered triples \(abc\to bcd\), toggling its common free directions \(b,c\) fixes BOTH ACTUAL ordered-face vertices. The four hub-coordinate representatives of that comparison are a PARAMETER-SPACE gauge square mapping to a SINGLE edge of \(W_{\rm good}\); they supply no nondegenerate simplicial two-cell. Toggling an exterior direction \(e\) changes BOTH physical face vertices and produces the genuine hexagon above. This cleanly separates spurious gauge squares from the actual cross-sheet cell structure.

**Open forcing objective.** Under an arbitrary active NORI coloring, identify a collection of these exterior-root transport hexagons whose local good triangles can be glued with OTHER actual good-path triangles to create a certified antipodal pentagon annulus or a cohomology class reaching the corrected degree \(n-4\) threshold. The theorem localizes precisely when a hexagon has missing triangles and proves that independent face-color sensitivity gives a repair, but neither the local dichotomy nor its induced circle proves unrestricted NORI grand closure.

**Corollary (quantitative exterior-influence repair).** Fix ANY ORDERED five-direction support \((a,b,c,d,e)\) and let \(G(x)\in\{0,1\}\) indicate that the actual rooted five-edge geodesic with starting root \(x\) and that direction order has at most one color change. Define
\[
\rho(a,b,c,d,e)=\Pr_{z\ {\rm uniform\ in}\ Q_n}
\big[h_z(abc)\ne h_{z\oplus e}(abc)\ \text{OR}\
     h_z(bcd)\ne h_{z\oplus e}(bcd)\big].
\]
Then, under ANY physical ordered-three-face binary coloring,
\[
\boxed{\Pr_{x\ {\rm uniform}}[G(x)=1]\ge \rho(a,b,c,d,e)/2.}
\]
Proof: pair each full root \(x\) with \(x\oplus e\). Their respective first/second windows are exactly the \(U_0,V_0\) and \(U_1,V_1\) of the hexagon with hub \(z=x\oplus a\oplus b\); their THIRD ordered face is the same physical \(M\) because \(e\) is free there. By Theorem 3 a pair on which at least one of the first two ordered faces changes color has at least one good member. The event defining \(\rho\) is invariant under the involution \(z\leftrightarrow z\oplus e\), so the fraction of sensitive ROOT PAIRS is exactly \(\rho\). There are \(2^{n-1}\) pairs; at least \(\rho\,2^{n-1}\) successful roots exist, proving the claim. In particular complete exterior sensitivity for this ordered five-word forces >=1/2 good rooted five-geodesics. Averaging across direction orders and combining with the independent universal 2/5 theorem gives
\[
\Pr_{x,p}[\text{five-geodesic good}]
\ge \max\big\{2/5,\ \tfrac12\mathbb E_p\rho(p)\big\}.
\]
The new bound improves 2/5 in sufficiently exterior-sensitive regimes (average influence >4/5), but does not improve the arbitrary-coloring universal constant or supply longer compatible paths.
