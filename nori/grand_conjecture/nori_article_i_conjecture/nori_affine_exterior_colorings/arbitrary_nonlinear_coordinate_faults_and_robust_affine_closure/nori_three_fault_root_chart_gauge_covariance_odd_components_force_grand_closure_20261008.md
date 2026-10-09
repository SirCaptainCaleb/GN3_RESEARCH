# Root-chart gauge covariance and odd-component fixed-point criterion for three nonlinear NORI exception directions

# Root-chart gauge covariance and an exact odd-component criterion for three arbitrary nonlinear fault directions

Let n>=8 and choose K⊂[n] of size three, D=[n]\K of size m>=5. Let the ACTIVE NORI coloring agree, on every ordered three-face with all free directions in D, with a full-exterior-parity reference
\[
c_0(F,(i,j,k))=h(i,j,k)\oplus\bigoplus_{t\notin\{i,j,k\}}z_t(F),
\]
where h satisfies the reversal parity forced by the active NORI axiom:
\[
h(k,j,i)\oplus h(i,j,k)=1\oplus(m\bmod2).
\]
All physical ordered three-faces meeting K may be colored ARBITRARILY, even nonlinearly, subject only to the active NORI axiom.

Let Z_h be the physical first-exceptional-face root-chart graph defined rigorously in Item nori_three_fault_reachability_root_chart_antipodal_connection_extraction_20261008. Its vertices G_h⊆F2^D are outside roots S for which some order p of D has a MONOCHROMATIC exterior-parity prefix; two roots are adjacent only when witnessed by orders ending with the SAME last ordered direction pair (u,v), and their bits coincide OUTSIDE {u,v}. Every graph edge is certified by equality of a genuine physical first-exceptional ordered face, not by averaging abstract labels.

**THEOREM 1 (exact gauge covariance of actual root charts).** Fix arbitrary \(\eta\in F_2^D\) and \(q\in F_2\), and define a new reference intercept
\[
h'(i,j,k)=h(i,j,k)\oplus q\oplus\eta_i\oplus\eta_j\oplus\eta_k.
\]
Then the cube-root translation \(T_\eta(S)=S\oplus\eta\) is a graph isomorphism \(Z_h\cong Z_{h'}\). It COMMUTES with outside antipodality:
\[
T_\eta(\bar S)=\overline{T_\eta(S)}.
\]
The uniform intercept q does not change Z at all. The same statement holds for coordinate relabeling: any permutation \(\rho\) of D induces a graph isomorphism between \(Z_h\) and \(Z_{h^\rho}\) with \(h^\rho(\rho i,\rho j,\rho k)=h(i,j,k)\).

**Proof.** Along an outside direction order p, the consecutive-window change equations are
\[
S_{p_{j+3}}=S_{p_j}\oplus 1
\oplus h(p_j,p_{j+1},p_{j+2})
\oplus h(p_{j+1},p_{j+2},p_{j+3}).
\]
Substituting h' cancels q twice and cancels \(\eta_{p_{j+1}},\eta_{p_{j+2}}\) twice, leaving exactly the additional term \(\eta_{p_j}\oplus\eta_{p_{j+3}}\). This is equivalent to the ORIGINAL equation for the root \(S'=S\oplus\eta\). Thus every p-specific 8-root code G_p is translated bijectively, and hence so is their union G. The chart adjacency condition uses one common last ordered pair (u,v) and equality on all other coordinates. A uniform coordinatewise translation preserves that equality exactly, so it is a graph isomorphism. Complement in F2^D is adding all ones, which commutes with translation. Relabeling coordinates transports both equations and physical-face exterior equality verbatim. QED.

**THEOREM 2 (odd-component forcing).** If Z_h is nonempty and has an ODD number of connected components, then the FULL active NORI grand conclusion holds for EVERY coloring C in the stated three-arbitrary-exception class. In particular, no valid grand counterexample in this class can have a root-chart graph with an odd number of components.

**Proof.** Each prefix-code equation contains exactly two S-bits, so complementing all m outside-root bits preserves every G_p. The physical chart-edge relation is complement-invariant as well, so \(\tau(S)=\bar S\) induces an involution of Z_h and permutes its connected components. An involution on a finite set of ODD cardinality has a fixed member; hence some connected component is setwise invariant under tau, containing S and bar S for each S in that component. By the exact root-chart extraction theorem, that antipodal self-connection forces a full at-most-one-switch antipodal NORI geodesic. QED.

**Consequence.** The open universal three-fault forcing task for arbitrary reversal-compatible h is now an exact, finite, antipodal COMPONENT-PARITY problem, invariant under 2^(m+1) separable coordinate-intercept gauges and under direction permutations. Under hypothetical grand failure, the components of Z_h must occur in opposite pairs, providing a literal equivariant zero-dimensional obstruction (an odd locally constant binary potential). The previously proved even-dimensional h=0 theorem establishes that the gauge class of h=0 has ONE connected component. No claim is made that all allowed h have odd component count; this remains an open combinatorial proposition.

**Research conjecture (NOT proved):** For every odd m>=5 and every reversal-even h (the intercept parity relevant for even n=m+3), the graph Z_h has an odd number of components, perhaps is always connected. Direct finite tests for small m support the conjecture but do not establish it. Solving this would extend the even-dimensional three-arbitrary-coordinate nonlinear closure theorem from coordinate-separable h to EVERY allowed affine exterior-parity intercept h.
