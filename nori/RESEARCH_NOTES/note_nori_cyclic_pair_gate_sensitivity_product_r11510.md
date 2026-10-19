# All-dimensional cyclic pair-gate sensitivity product and three-pair compatibility forcing

- Stable ID: note_nori_cyclic_pair_gate_sensitivity_product_r11510
- Author: unspecified; session provenance retained
- Primary home: subsection:obstruction_compatibility_and_a_programme_for_nori1_closure
- Labels: NORI1, paired-flat, dimension-uniform, functional-pair-gates, cyclic-sensitivity, multiplicity, constructive-forcing, three-pair, joint-obstructions
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11510_3
- Updated session: session_nori_r11510_3
- Disposition: none
- Successor: none

## Related references

- note:note_nori_fourcycle_parity_sync_r11510
- note:note_nori_rank_four_pointwise_sensitivity_cycle_r11510

## Research note

# Full-cycle sensitivity-product forcing

**THEOREM.** For any m>=2 let an ordinary edge coloring of Q_(2m) have paired directions P_i={a_i,b_i}, with color rules g_i(x|P_(i-1)) and 1+g_i(x|P_(i-1)). The gates g_i:F2^2->F2 are arbitrary. For the fixed pair-label order W=(0,1,...,m-1,0,1,...,m-1), the number of starting roots giving a red full antipodal geodesic is
 R_W=product_i E(g_i),
where E(g_i) counts sensitive undirected edges of its four-vertex input square. If every gate is nonconstant, at least 2^m roots work for W. No legal oddness is required for this ordinary coloring.

**PROOF.** Choose independently one sensitive input edge e_i of each g_i, of direction d_i in predecessor pair P_(i-1). Prescribe the member used at the first visit to each pair as ell_(i-1)=1+d_i for i>=1 and ell_(m-1)=d_0. For i>=1 let t_i be the endpoint of e_i where g_i(t_i)=ell_i; start predecessor pair i-1 at v_(i-1)=t_i+e_(ell_(i-1)). Thus the first visit to gate i sees t_i, while its second visit sees t_i+e_(d_i) because the predecessor's second step occurs between those visits. Its output flips, so both members of pair i are used. For i=0 choose endpoint t_0 of e_0 with g_0(t_0)=ell_0 and initialize the last pair to t_0. Its first traversal, between the two visits of gate zero, flips direction d_0 and changes gate zero's value. This defines a red full path and uniquely determines all initial pair states. Conversely the sensitive edge crossed by each predecessor between the visits of gate i is recoverable from every successful W-path. These constructions are inverse, proving the formula. QED.

**ORDINARY THREE-PAIR COMPATIBILITY LEMMA.** In an ordinary paired-flat Q6 coloring suppose one parity fiber has three signed unary reader gates in a directed 3-cycle, and every two-pair four-face lacks a monochromatic spanning geodesic. Normalize the parity to zero and the gates to h_i^0(q)=q_(i+1) modulo three. On two P0,P1 faces with P2 equal 00 or11, gate f0 varies in P1, forcing f1 independent of P0 there. Its corresponding values are 0 and1. Hence f1 varies in P2 for every P0 assignment, forcing f2 independent of P1 everywhere. By the initial reader-cycle values, f2 then varies between P0=00 and11 for every P1 setting, forcing f0 independent of P2 globally. Cyclic repetition forces f1 independent of P0 globally. Each gate now reads only the preceding pair, and is nonconstant. The product theorem gives a red full Q6 geodesic.

**NORI1 Q8 APPLICATION.** In any legal paired-flat Q8 coloring without successful two-pair faces, a parity fiber having three unary-reader gates and one three-input gate has a reader 3-cycle among its unary gates, by the previously proved pointwise rank-four rigidity. Freeze the fourth pair. The ordinary three-pair lemma supplies a full red geodesic in the remaining six-dimensional face, and paired-endpoint insertion produces a red full Q8 antipodal geodesic. Thus the three-reader-plus-one-extra-gate type is excluded by mathematical forcing. The four-majority type remains an open branch.

**VERIFICATION.** The script paired_cycle_product_verifier.py exhaustively checks 256 two-gate and 4096 three-gate systems and tests additional four- and five-gate systems. Detailed complete manuscript nori_cyclic_pair_sensitivity_product.md. The formula holds in every dimension; it is an unrestricted-dimensional forcing tool for the specified pair-reader structure, and the general NORI1 conjecture remains open.
