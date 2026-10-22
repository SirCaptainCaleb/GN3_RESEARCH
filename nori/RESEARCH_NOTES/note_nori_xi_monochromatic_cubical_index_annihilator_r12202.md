# Monochromatic cubical fillings annihilate the higher antipodal cup products

- Stable ID: note_nori_xi_monochromatic_cubical_index_annihilator_r12202
- Author: session_nori_r12202_1
- Primary home: subsection:paired_direction_involutions_and_geodesic_endpoint_matchings
- Labels: NORI1, topology, CDC, mixed-square, relative-cohomology, method-obstruction
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r12202_1
- Updated session: session_nori_r12202_1
- Disposition: none
- Successor: none

## Related references

- None

## Research note

# Monochromatic cubical fillings annihilate higher antipodal cup products

Session session_nori_r12202_1. In any antipodally odd binary edge coloring of Q_n, n>=3, let H=Q_n^(1)/tau and B=boundary([0,1]^n)/tau = RP^(n-1). Let M0 consist of H and the images of all cubical faces with only one edge color. Each such face orbit has one all-red original representative and one all-blue antipodal representative. Select any finite collection D of closed red edge walks and attach disks along their projections to M0 and B, giving M subset Y. The antipodal double cover extends over these disks because their attaching loops have closed lifts.

**Theorem.** The covering class w in H^1(M;F2) is nonzero, but
\[
\boxed{w\smile u=0\quad(\forall u\in H^k(M;F2),\ k>=1).}\tag{MA1}
\]
Thus w^r=0 for every r>=2, including after attaching a cycle double cover, all all-red and all-blue cubical cells, and any other red closed-walk disks.

*Proof.* Let S contain all original cube vertices, all red edges, every all-red proper cubical face, and one disk attached along each walk D. The quotient projection q:S->M identifies antipodal vertex pairs, while mapping every open cell of positive dimension bijectively. Indeed each antipodal edge orbit has one red edge, each monochromatic face orbit has one red face, and each extra red disk is matched to a single quotient disk. The cellular cochain complexes of S and M agree in every degree >=1, with the same coboundaries in degrees >=1. Hence q^*:H^j(M;F2)->H^j(S;F2) is an isomorphism for j>=2. But q lifts continuously into the extended antipodal cover of M by choosing the original red vertex, edge, face, and disk, so q^*w=0. Injectivity in degree >=2 now gives w cup u=0 for each positive-degree u. Finally w|H is nonzero, as the quotient of an uncolored full antipodal direction-once path has monodromy one. QED.

**Relative mixed-cell theorem.** Let w_Y in H^1(Y;F2) extend the covering class. For every 2<=r<=n-1,
\[
\boxed{w_Y^r\ne0,\quad w_Y^r|_M=0,\quad
\exists\eta_r\in H^r(Y,M;F2)\text{ mapping to }w_Y^r.}\tag{MA2}
\]
The relative cellular cochains C^r(Y,M) for r>=2 have one generator for each antipodal pair of mixed-color r-faces in the original cube boundary. In degree two, eta_2 admits a nonzero representative supported on mixed-color square orbits, whose coefficients satisfy the cellular cocycle parity condition on the boundary of each mixed three-face.

*Proof.* Restriction of w_Y to B=RP^(n-1) is the standard generator, whose powers through degree n-1 are nonzero. Its powers restrict to zero on M by MA1. The cohomology sequence of the pair (Y,M) gives eta_r. Quotient cells outside M are precisely the nonmonochromatic faces, and all extra disks lie in M. Since all one-cells are in M, the relative degree-two cocycle statement follows. QED.

**Forcing gap and decision.** Every mixed-cell relative class described here exists for good and hypothetical bad colorings. It supplies no defect-reducing square exchange by itself. The relative lift eta_r may be modified by a class coming from H^(r-1)(M), so its support has no canonical red-blue incidence choice. A NORI1 proof using the CDC must connect mixed-color cells to simultaneous globally minimizing paths, or find a different color-sensitive integral decoding operation. Purely monochromatic CDC surfaces and cubical faces cannot carry the higher projective cup powers.
