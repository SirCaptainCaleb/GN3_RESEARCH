# Three-level orientations defeat dual-rank galleries in rank-two uniform products

- Stable ID: note_nori_xi_chromatic_orientation_obstruction_for_uniform_rank_two_products
- Author: unspecified; session provenance retained
- Primary home: section:nori_matroid_generalizations_conjectures
- Labels: obstruction, exchange-geometry, chromatic, dual-rank
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r7130_3
- Updated session: session_nori_r7130_3
- Disposition: none
- Successor: none

## Related references

- subsection:fundamental_circuit_pivots_dual_basis_sweeps_and_faithful_ordered_exchanges

## Research note

**Theorem (chromatic-level obstruction for oriented exchange sweeps).** Let \(G\) be any graph admitting a proper vertex coloring \(h:V(G)\to\{0,\ldots,q-1\}\), \(q\ge2\). Orient each edge from its lower \(h\)-value to its higher \(h\)-value and let \(c(u,v)=1\) on forward directed arcs and \(c(v,u)=1-c(u,v)\) on reversed arcs. Along every oriented walk \(P=(v_0,\ldots,v_L)\), each maximal constant run in the color word of its consecutive oriented edges has length at most \(q-1\). Consequently,
\[
\operatorname{sw}_c(P)\ge\left\lceil\frac{L}{q-1}\right\rceil-1,
\]
and a monochromatic oriented path has at most \(q-1\) edges.

*Proof.* A color-one run strictly increases \(h\) at every step, so its length is at most \(q-1\); a color-zero run strictly decreases \(h\) and satisfies the same bound. There are \(\operatorname{sw}_c(P)+1\) constant runs, each of at most \(q-1\) steps, giving the inequality. \(\square\)

**Corollary (failure of power-law dual-rank selectors in simple small-circuit products).** Let
\[
M_m=\bigoplus_{i=1}^{m}U_{2,3},\qquad m\ge2.
\]
All circuits of \(M_m\) have size three; every connected component is simple; \(r(M_m^*)=m\); its basis-exchange graph is the Cartesian product
\[
\Gamma(M_m)\cong K_3^{\square m}.
\]
For each dual basis \(D\), every permutation of its \(m\) elements indexes a complete basis-exchange gallery of \(m\) steps with the fundamental-circuit pivots equal to \(D\) in that order. Nevertheless, the graph has a proper 3-coloring, and there exists a reversal-odd binary coloring of *oriented exchange edges* for which every monochromatic gallery, regardless of length, contains at most two edges, while every complete \(m\)-resource sweep has at least \(\lceil m/2\rceil-1\) color changes.

*Proof.* A factor \(U_{2,3}\) has three two-element bases, with basis graph \(K_3\), and its dual is \(U_{1,3}\). For each factor, choose a dual-basis element \(d_i\), and order the other two elements as \(s_i,t_i\). The factor exchange
\(\{s_i,d_i\}\to\{d_i,t_i\}\) is labeled by the unique retained fundamental-circuit pivot \(d_i\). Since exchanges in distinct summands commute, perform these \(m\) factor exchanges in any specified order to obtain a complete pivot-gallery using the elements of \(D\) once each. This works for every dual basis and every permutation.

Label the three bases in each factor by \(0,1,2\). For a product basis \(B=(B_1,\ldots,B_m)\), define
\[
h(B)=\left(\sum_{i=1}^{m}h_i(B_i)\right)\bmod3\in\{0,1,2\}.
\]
Each basis exchange changes one factor to one of its two other bases, so it changes the residue. Thus \(h\) is a proper 3-coloring. Orient every edge of the product basis graph from smaller to larger residue and set \(c(B,B')=1\) on that orientation, \(c(B',B)=0\). The condition \(c(B',B)=1-c(B,B')\) is the reversal-odd law on oriented fundamental-circuit exchanges; the circuit of every exchange has size three. Apply the theorem with \(q=3\). \(\square\)

**Significance for NORI Article XI.** This family is a counterexample to any proposed universal \(r(M^*)^\alpha\)-length monochromatic coherent exchange gallery or bounded-switch complete gallery for all matroids whose circuits have size at most three, whose components are simple, and whose dual-basis permutation sweeps are complete. It is unbounded in dual rank and requires no finite search. The ordinary boundary target \(U_{2,n}\) has instead the large-clique exchange graph \(J(n,2)=L(K_n)\); its chromatic number grows with \(n\). In the cube target, the coloring is on unoriented edges and has a separate antipodal-complement law, so an arbitrary orientation by a proper vertex coloring is not an admissible substitute. This obstruction identifies a necessary additional quantitative hypothesis controlling the colored transition geometry. It does not refute the two canonical original conjectures or conjectures restricted to their corresponding canonical polarization geometries.

**Proposition (metric failure of bounded twisted closure).** In the same matroid \(M_m=\bigoplus_{i=1}^m U_{2,3}\), use directed basis exchanges as states and let \(J(B,B')=(B',B)\) be their canonical reversal. A complete factor sweep is a sequence \(B_0\to B_1\to\cdots\to B_m\), changing one different direct-sum component at each step. Suppose successive directed-exchange states can transition only when their underlying basis arcs concatenate, as required for a coherent path. Then any continuation from the last state \((B_{m-1},B_m)\) to the involute of the first state \(J(B_0,B_1)=(B_1,B_0)\) uses **at least \(m\) additional transitions**.

*Proof.* Such a continuation is a directed basis-graph walk starting at \(B_m\) and ending at \(B_0\) after \(q\) edges, with \(q\) equal to the number of additional state transitions. The basis graph is \(\Gamma(M_m)=K_3^{\square m}\). The bases \(B_m,B_0\) differ in all \(m\) factor coordinates, so \(d_{\Gamma(M_m)}(B_m,B_0)=m\), yielding \(q\ge m\). \(\square\)

This is the metric reason the canonical arc-reversal polarization of the product obstruction fails Article XI's bounded-seam axiom A4. The boundary model \(\Gamma(U_{2,n})=J(n,2)\) has exchange diameter two and admits the established sharp three-turn reversal closure. The cube model instead uses global basis complementation rather than local arc reversal, and has the established one-turn antipodal closure. Thus a bounded, symmetry-compatible *twisted return distance* is a substantive geometric discriminator, rather than cosmetic decoration. No claim is made that bounded seam alone proves either path theorem; the additional Article XI independence and signed-gallery axioms remain essential.
