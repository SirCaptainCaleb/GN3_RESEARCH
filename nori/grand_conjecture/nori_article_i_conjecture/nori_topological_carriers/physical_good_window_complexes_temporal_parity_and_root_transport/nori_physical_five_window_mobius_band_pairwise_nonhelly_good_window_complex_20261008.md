# Actual good-window complex contains a physically certified Möbius band: pairwise good compatibility is not Helly or flag

# A genuine five-window Möbius band in the good-path complex: pairwise compatibility is not Helly

Let \(n\ge5\) and let \(W_{\mathrm{good}}(c)\) be the ACTUAL physical ordered-three-face window complex of Item \`nori_good_window_set_complex_metric_parity_extension_and_full_span_edge_20261009\`: vertices are genuine ordered physical three-face windows; a set of vertices spans a simplex if all occur along ONE actual geodesic with at most one ordered-window color change (not necessarily as consecutive windows). This complex must NOT be replaced by the flag completion of the graph of pairwise path-compatible windows.

Choose any physical hub \(z\in Q_n\), any FIVE distinct cube directions indexed by \(\mathbb Z/5\mathbb Z\), and let
\[
u_i=\bigl(F_z(\{i,i+1,i+2\}),\ (i,i+1,i+2)\bigr),\qquad i\in\mathbb Z/5\mathbb Z,
\tag{1}
\]
where \(F_z(T)\) denotes the physical coordinate face containing \(z\) and free on \(T\). These are five DISTINCT actual oriented physical window vertices.

**Lemma 1 (cyclic five-window incidence, independent of colors).** For any two distinct indices \(i,j\), exactly one of the directed compatibilities \(u_i\prec u_j\) and \(u_j\prec u_i\) holds, with \(u_i\prec u_j\) precisely when \(j-i\equiv1\) or \(2\pmod5\). The window-position separation is 1 when \(j-i\equiv1\), and 2 when \(j-i\equiv2\). No actual direction-distinct geodesic can contain any triple \(\{u_i,u_j,u_k\}\) whose induced orientation under this regular five-vertex tournament is a directed cycle. The ONLY triples that can occur together are the FIVE cyclically consecutive triples
\[
\{u_i,u_{i+1},u_{i+2}\},\qquad i\in\mathbb Z/5\mathbb Z.
\tag{2}
\]
Each triple in (2) is witnessed by a genuine length-five geodesic with directions \((i,i+1,i+2,i+3,i+4)\), rooted at \(z\oplus e_i\oplus e_{i+1}\); its three ACTUAL physical ordered windows are literally \(u_i,u_{i+1},u_{i+2}\). There is no common geodesic containing four or all five windows.

**Proof.** Two cyclic triples indexed by indices differing by one share their last/two vs first/two ordered directions; indices differing by two share the last vs first ordered direction. Every pair has one of these two forward patterns in exactly one orientation, and all common fixed exterior bits agree because both faces contain z. Apply the exact pairwise ordered-window incidence test from Item \`nori_exact_two_physical_ordered_windows_geodesic_compatibility_unique_full_root_20261008\`. Thus the precedence relation is the regular cyclic tournament with outgoing neighbors \(i+1,i+2\).

Any genuine directed geodesic induces a LINEAR ordering on its included window vertices, hence its pairwise precedence tournament must be transitive. The regular five-vertex tournament has exactly FIVE transitive three-vertex subtournaments: by counting their unique source, each of five vertices has two outneighbors, giving \(\sum_i\binom22=5\); these are exactly (2). It has no transitive four-vertex subtournament, since every four-vertex tournament subset contains a cyclic triangle (equivalently verify the five four-subsets by cyclic symmetry). The explicit five-direction path rooted at \(z\oplus e_i\oplus e_{i+1}\) has its first three windows through z with free triples \((i,i+1,i+2)\), \((i+1,i+2,i+3)\), \((i+2,i+3,i+4)\), giving the claimed certificates. \(\square\)

**Theorem 2 (a physically realizable Möbius strip, with nonzero window parity).** Suppose the FIVE actual window colors \(c(u_i)\) are such that every cyclically consecutive three-bit word
\[
(c(u_i),c(u_{i+1}),c(u_{i+2}))
\]
has at most ONE change. This occurs, for example, when all five are monochromatic, or when their cyclic run lengths are 2 and 3. Then the **INDUCED simplicial subcomplex** of \(W_{\mathrm{good}}(c)\) on \(\{u_0,\ldots,u_4\}\) has:
- five vertices and ALL ten edges;
- exactly the five triangles (2);
- no simplices of dimension three or higher.

It is precisely the classical five-vertex, five-triangle triangulation of a MÖBIUS BAND. Its edge boundary is the single five-cycle of length-two chords \(\{u_i,u_{i+2}\}\). Every adjacent cyclic edge \(\{u_i,u_{i+1}\}\) belongs to two triangles, every chord \(\{u_i,u_{i+2}\}\) to one; vertex links are intervals. Its Euler characteristic is \(5-10+5=0\), and with one boundary component it is the Möbius band, not the cylinder.

Moreover let \(\beta(uv)=d_1(m(F_u),m(F_v))\pmod2\) be the genuine window-distance parity 1-cocycle of the existing good-window complex. Each adjacent cyclic edge has geometric distance 1, so \(\beta\) evaluates to
\[
\sum_{i=0}^4\beta(u_iu_{i+1})=5=1\pmod2
\]
on the Möbius core cycle. Hence its cohomology class is nonzero on this actual induced Möbius band and **remains nonzero in the full \(W_{\mathrm{good}}(c)\)**, regardless of additional cells elsewhere: an extension of a cocycle cannot make its restriction to an existing nonbounding odd cycle evaluate zero. The chord boundary cycle has \(\beta=0\) because all its edges have distance two, compatible with being twice the core loop.

**Theorem 3 (the configuration is consistent with the FULL active NORI antipodal oddness law).** For ANY \(n\ge5\) and chosen z and directions, assign color 0 to all ordered physical three-face windows through z (not only the five \(u_i\)). Assign color 1 to their antipodal-reversed mates through \(\bar z\), and complete remaining ordered-face involution orbits arbitrarily by opposite colors. Since a proper three-face of \(Q_n\) cannot contain BOTH z and \(\bar z\), no involution orbit receives contradictory assignments. This is a valid active NORI coloring admitting the Möbius band of Theorem 2 (and its disjoint antipodal mate). The two bands by themselves are exchanged by the free involution, so on their disconnected union the antipodal covering class \(w\) is TRIVIAL even though \(\beta\) is nontrivial on either individual band.

**Topological lesson.** Pairwise **REAL** geodesic compatibility is not a Helly-3 or flag condition: the three windows \(\{u_0,u_2,u_4\}\) are pairwise compatible (even pairwise co-contained in GOOD monochromatic paths in this example) but CANNOT lie on a common geodesic because their forced precedence is cyclic. Filling every clique in the window graph would insert FALSE 2-simplices and destroy precisely the physical Möbius/parity topology that a fixed-point proof ought to preserve. The good-window complex's unusual higher-dimensional identifications are essential: certificate-preserving simplices, not arbitrary flag fillings, are required. An isolated Möbius band cannot settle the grand conjecture; the outstanding objective is to couple its metric-parity class \(\beta\) with the independent antipodal cover class \(w\) across ROOT-MOVING shared-window cells and force sufficiently high cup powers to reach the maximum-distance good edge.
## Elevation: valid NORI coloring with no cyclic five-window Möbius filling at designated antipodal hubs

The Möbius configuration above is a certified CONDITIONAL construction, not a universal existence assertion. A simple active NORI countermodel rules out the claim that every hub carries such a filled five-cycle.

Fix any EVEN n>=6, a total order on direction names, and assign c(F,(a,b,c)) = (XOR of F_i over fixed exterior directions i not in {a,b,c}) XOR 1[b>max(a,c)]. There are n-3 ODDLY MANY fixed exterior directions, and reversing the free triple preserves the predicate that its middle direction is greatest. Thus c(bar F,rev(a,b,c))=1 XOR c(F,(a,b,c)); the coloring satisfies the FULL active NORI axiom.

At hub z=0^n, take ANY five distinct named coordinate directions p_0,...,p_4 in ANY cyclic order, and the five oriented physical windows u_j through z defined earlier. All exterior bits at z are zero, so c(u_j)=1 precisely when p_(j+1) is a STRICT LOCAL MAXIMUM relative to its two cyclic neighbors p_j,p_(j+2). Every cyclic ordering of five distinct ordered values has at least one local maximum, and NO TWO ADJACENT positions can both be strict local maxima. Consequently some c(u_j)=1 has neighboring window colors both zero, yielding a cyclic 0,1,0 triple with TWO changes. The actual five-edge path certified by that triple is NOT good, so not all five cyclic triangles exist, and this five-window Möbius band NEVER appears at z for ANY choice of five directions/cyclic order.

At the antipodal vertex bar z=1^n, all exterior fixed bits of any three-face through it are 1; their parity is n-3=1 mod2. Hence the five cyclic colors there are the complements of the colors at z (for unchanged direction orders). An isolated local-maximum color 1 becomes an isolated color 0, now with neighbors 1,1, giving a cyclic 1,0,1 pattern with two changes. No cyclic five-window Möbius filling appears at bar z either.

This does NOT say W_good has no Möbius subcomplex elsewhere and does NOT contradict the grand conjecture. The underlying five-edge pentagon survives in the good-window 1-skeleton because EVERY four-edge path has at most one change, and the intrinsic parity cocycle beta still evaluates to 1 around it. Thus the odd metric-parity class and the four-sheeted temporal/antipodal voltage cover are UNIVERSAL, whereas this Möbius filling is not. Higher cup products need genuinely forced higher cell incidence, not an assumed filling of the pentagon.
