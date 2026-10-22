# Root-facet selector freedom and one-edge projective overlap

- Stable ID: note_nori_xvii_root_facet_selector_transport_obstruction_r12147_5
- Author: session_nori_r12147_5
- Primary home: subsection:central_freudenthal_subdivision_and_the_all_root_geodesic_chamber_sphere
- Labels: NORI1, combinatorial-topology, selector, root-facet, integral-decoding, method-obstruction
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r12147_5
- Updated session: session_nori_r12147_5
- Disposition: none
- Successor: none

## Related references

- subsection:central_freudenthal_subdivision_and_the_all_root_geodesic_chamber_sphere
- note:note_nori_xvii_two_minimizer_splice_dichotomy_r12147_5
- note:note_nori_xvii_switch_position_intersection_cut_exchange_r12147

## Research note

# Root-facet selector freedom and one-edge projective incidence

Work with an arbitrary antipodally odd binary coloring of the original undirected edges of \(Q_n\), \(n\ge3\). Write \(c_j(u)=c(\{u,u\oplus e_j\})\), with \(c_j(u\oplus e_j)=c_j(u)\) and \(c_j(\bar u)=1+c_j(u)\). For any rooted direction-simple antipodal geodesic \(P=(x;\pi)\), define its canonical oriented selector by \(q(P)_j=x_j+c_j(e_j(P))\), where \(e_j(P)\) is its unique original direction-\(j\) edge and arithmetic is mod two.

**Theorem (three path-generator laws).** (1) Under cyclic root rotation \(\rho(x;i,\pi')=(x\oplus e_i;\pi',i)\) and antipodal translation \(\tau(x;\pi)=(\bar x;\pi)\),
\[
q(\rho P)=q(P),\qquad q(\tau P)=q(P).
\tag{RF1}
\]
(2) For a swap of consecutive directions \(i,j\) based at the original square vertex \(u\), the selector change is
\[
q(P^{ij})+q(P)=\Delta_j c_i(u)e_i+\Delta_i c_j(u)e_j.
\tag{RF2}
\]
(3) For the Freudenthal root facet \(r_0P=(x\oplus e_i;i,\pi')\), which retains the direction order and changes the root across its first edge,
\[
\boxed{q(r_0P)+q(P)=e_i+\sum_{j\ne i}\Delta_i c_j(e_j(P))e_j.}
\tag{RF3}
\]
Here \(\Delta_i c_j(e)=c_j(e\oplus e_i)+c_j(e)\); the translated edge has the same original direction \(j\).

*Proof.* A root rotation retains the later original edges and moves the first direction-\(i\) edge to its antipodal mate; the root's \(i\)-bit and that edge's color both flip. Antipodal translation flips every root bit and every edge color. These establish (RF1). A square swap changes only the edges in its two participating directions, from \(i\) at \(u\), \(j\) at \(u\oplus e_i\) to \(j\) at \(u\), \(i\) at \(u\oplus e_j\), giving (RF2). The root facet retains the first undirected \(i\)-edge, while translating all subsequent direction-\(j\) edges by \(e_i\). Its root changes only bit \(i\), giving (RF3). \(\square\)

**Uniform independent transverse freedom.** Fix any root, order \(\pi\) beginning with \(i\), and all \(n\) original colors along \(P\). The \(n-1\) transverse derivatives \(\Delta_i c_j(e_j(P))\), \(j\ne i\), can be prescribed arbitrarily and independently by completing the remaining edge-color orbits while preserving antipodal oddness. Indeed for each \(j\ne i\), the translated direction-\(j\) edge belongs to a different antipodal edge orbit from \(e_j(P)\): translating by \(e_i\) is neither zero nor all \(n-1\) exterior bits when \(n\ge3\). Distinct \(j\) give different original edge directions, so their orbits cannot collide. Assign the desired colors to these translated orbits and their complementary colors to their antipodes; then complete every unused orbit arbitrarily. Hence the right side of (RF3) can be any vector whose \(i\)-bit is one.

For an explicit full antipodal jump, fix \(i=0\) and set
\[
c_0(u)=u_1,\qquad c_j(u)=u_0\ \ (1\le j<n).
\tag{RF4}
\]
These functions ignore their own direction bits and complement under global antipodality. For any \(P\) beginning with direction \(0\), every transverse derivative equals one, and
\[
q(r_0P)=\overline{q(P)}.
\tag{RF5}
\]

**Projective overlap theorem.** The projective direction-rainbow cycles represented by \(P=(x;i,j_1,\ldots,j_{n-1})\) and \(r_0P=(x\oplus e_i;i,j_1,\ldots,j_{n-1})\) have precisely two common projective vertices and one common original projected edge, namely their shared first direction-\(i\) edge. To see this, after their initial common edge their remaining lifted vertex sets are respectively \(x\oplus e_i\oplus J_k\) and \(x\oplus J_l\), where \(J_k=\{j_1,\ldots,j_k\}\). Equality of these vertices is impossible because of the \(i\)-bit. Equality modulo antipodality requires \(J_k\triangle J_l=J_{n-1}\); since these sets are nested prefixes of the same order, this happens only for \(\{k,l\}=\{0,n-1\}\), yielding the common endpoints of that projected edge. The same holds for either orientation of the projective cycles.

Consequently, after aligning the two cycles to the same original root and shared projected edge, their common internal port comparisons occur on a shared first or last edge. Their two-path crossing signs vanish at these shared vertices. A single root facet therefore supplies neither the opposite-seam configuration nor the three-way cyclic-matching violation required by the established global-minimizer exchange mechanism.

**Integral decoder and implication.** For any \(P=(x;\pi)\), \(q(P)=x+\mathbf1_B\) where \(B\) is the support of blue directions along \(P\). It lies on the doubled original path \(P\cup\bar P\) if and only if \(B\) is a prefix or suffix of the order \(\pi\), equivalently \(D(P)=1\). Thus incidence of \(q(P)\) with its original projective cycle is a faithful integral certificate. Nevertheless (RF5) shows that convex sign-vector interpolation of \(q\) along a single all-root facet may pass through the origin, even for a legal affine coloring. A nonvanishing continuous selector construction needs additional color-sensitive transport choices, and one-edge common overlap does not activate suffix-splice descent. The result makes no claim that globally minimizing bad paths realize arbitrary transverse derivatives; combining their global inequalities remains the open forcing avenue.
