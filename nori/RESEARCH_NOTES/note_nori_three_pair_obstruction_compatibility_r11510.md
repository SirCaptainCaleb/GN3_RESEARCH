# Three-pair joint obstruction rigidity and universal activated-cycle dichotomy

- Stable ID: note_nori_three_pair_obstruction_compatibility_r11510
- Author: unspecified; session provenance retained
- Primary home: subsection:obstruction_compatibility_and_a_programme_for_nori1_closure
- Labels: NORI1, paired-flat, joint-compatibility, three-pair, Q6, sensitivity, cyclic-reader, constructive-forcing, local-Jacobian, dimension-uniform, active-cycle
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11510_3
- Updated session: session_nori_r11510_3
- Disposition: none
- Successor: none

## Related references

- note:note_nori_pair_sensitivity_product_irreducible_cycles_r11510

## Research note

# Simultaneous two-pair face obstruction compatibility and active cycles

**Three-pair theorem.** Let c be an arbitrary legal antipodally odd paired-flat edge coloring of Q6 with three direction pairs P_0,P_1,P_2. If no four-dimensional face retaining two whole pairs and freezing the third admits a monochromatic full geodesic, then its three pair gates are signed unary readers arranged around a directed three-cycle. Explicitly, after cyclic relabeling or reversing the cycle, f_i(x)=x_(d_(i-1))+epsilon_i where d_(i-1) is one of the two bits in the previous pair. There are 128 labeled systems of this form (2 cyclic orientations * 2^3 reader choices * 2^3 phases), and every one admits an all-red full antipodal geodesic. Therefore every legal paired-flat Q6 coloring has a constructive red full witness: either extend a red two-pair face by the omitted pair using antipodal oddness, or normalize a reader cycle and use its explicit full red path.

**Proof of rigidity.** For each pair-parity vector p in F2^3, parameterize states by (q_i,q_i+p_i) in each pair. The restricted gate h_i^p(q)=f_i(q,q+p) is independent of q_i and satisfies h_i^p(bar q)=1+h_i^p(q). An odd function of two Boolean inputs is a signed unary reader. Thus each h_i^p reads some q_(sigma_p(i)), with sigma_p(i)!=i. If sigma_p(i)=j and sigma_p(j)=i, then in the four-face on pairs i,j with third pair fixed from that state both gates are nonconstant, so the established R=2E(a)E(b) identity supplies a red full face path. Under the hypothesis this is prohibited. Hence sigma_p is a loopless functional digraph on three labels with no two-cycle, so it is one of the two directed three-cycles.

Because f_i ignores the bits of its own pair, sigma_p(i) is independent of p_i. A change of directed three-cycle orientation changes sigma_p(i) for every i. Thus the orientation is independent of each p_i and is constant over all p. Write sigma(i)=j and sigma(k)=i for the remaining label k. With any fixed assignment of pair j, gate f_k varies under flipping both bits of pair i, because its diagonal restriction reads q_i. The absence of a red two-pair face on i,k then forces f_i to be independent of pair k for every fixed assignment of pair j. It already ignores pair i, so f_i depends only on pair j, and antipodal oddness makes it a signed unary reader of one of the two bits of j. Repeat for all i. Conversely a signed three-cycle has an omitted reader pair in every proper two-pair face, so no such face succeeds.

Swapping labels within direction pairs and translating vertices converts every signed reader three-cycle to f_i=x_(a_(i-1)). From the root with x_(a0)=1 and other bits zero, direction order (b1,a0,a2,a1,b0,b2) is a full all-red antipodal geodesic. This proves the classification and witness statement without solver assumptions.

**All-dimensional active-cycle dichotomy.** For every legal paired-flat Q_(2m), m>=2, and every vector p of pair parities, the induced Boolean network h^p(q)=f_i(q,q+p) is antipodally self-dual and ignores its own component. By the Shih-Dong local-Jacobian fixed-point theorem, some state q has a directed cycle in the local derivative graph: otherwise h^p would have a unique fixed point, impossible because self-duality pairs fixed points antipodally. If no two-pair face succeeds, the local derivative graph has no two-cycle (each such cycle would give mutually nonconstant gates on a common four-face); it has no loops since gates ignore their own pair. Thus every parity fiber contains an active directed cycle of length at least 3. As the derivative graph at q equals that at bar q, there are at least 2^(m+1) distinct (p,q) states with such a cycle. This is an all-dimensional necessary structure for avoiding local two-pair witnesses, not a full geodesic theorem.

**Validation.** A standalone Z3 Boolean encoding of the 24 independent legal pair-gate bits, constrained by failure of every two-pair face, returns UNSAT when any gate is required to be non-unary. A separate independent enumeration validates all 128 three-cycle reader systems, the face obstruction, and existence of a full red geodesic in each. Full detailed proof: /mnt/data/nori_three_pair_global_compatibility.md; verifier: /mnt/data/nori_three_pair_compatibility_verifier.py.

**Scope.** This converts a family of simultaneously failed local forcing conditions into an explicit *globally successful* cycle structure in dimension six. It is an analytic closure proof for the paired-flat Q6 case, independent of earlier exhaustive profile SAT. In higher dimensions, the induced self-dual gates have more inputs and can be nonlinear; local cycles of length at least three do not yet provide a dimension-simple antipodal geodesic. Unrestricted NORI1 remains open.
