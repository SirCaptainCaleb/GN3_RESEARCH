# Certified center-square NORI dichotomy: opposite-color common edge or an exact antipodally odd edge-color shadow

# Edge-shadow dichotomy for genuine monochromatic centered 4-path witnesses in ACTIVE NORI

Fix n>=5 and let c be an active NORI binary coloring of physical ordered 3-faces, c(bar F, rev pi)=1−c(F,pi). For any physical cube edge e, let K(e)⊆{0,1} be the set of monochromatic colors q for which there exists an ACTUAL MONOCHROMATIC CENTERED FOUR-EDGE geodesic P_z(a,b,c,d) of color q whose certified physical MIDDLE PAIR square Q(z;b,c) contains e among its four boundary edges. Thus the color certificate's middle directions include the physical direction of e. This definition is physically invariant: the same square can be certified at each of its four vertex centers with the same ordered window faces.

Theorem nori_certified_square_complex_connected_antipodal_one_class_20261008 gives the certified-square graph G={e:K(e)≠empty}; G is connected, spanning, and has degree >=n−1 at every cube vertex. The complement M=E(Q_n)\E(G) is a matching. The antipodal NORI axiom implies K(bar e)={1−q:q∈K(e)}.

**THEOREM (sharp edge-shadow dichotomy).** For EVERY active NORI coloring, at least one of these alternatives holds:

(A) Some physical cube edge e has K(e)={0,1}: two GENUINE mono 4-geodesic square certificates of opposite colors both CONTAIN that same physical cube edge as an edge of their middle-pair squares. This is stronger than merely two opposing-color connectors sharing a center.

(B) There exists an antipodally odd UNDIRECTED binary edge coloring sigma:E(Q_n)→{0,1}, sigma(bar e)=1−sigma(e), satisfying sigma(e)=q for ALL edges e with K(e)={q}. The only choices arise on the matching M of un-certified square edges, and each antipodal orbit of these missing edges may be assigned one bit arbitrarily.

**Proof.** If (A) fails, every nonempty K(e) is a singleton. Declare sigma(e) to be that unique color for e∈G. Antipodal oddness of K makes sigma(bar e)=1−sigma(e) on G. The missing-edge set M is invariant under physical antipodality and forms a matching. Since the cube antipodal involution fixes no UNDIRECTED physical edge for n>=3, its action on M has two-element orbits. Assign one bit to an arbitrary representative and the complementary bit to its mate, for each orbit, producing a full antipodally odd edge coloring sigma. The definition is consistent and exhausts the cube edges. QED.

**Local witness preservation.** In case (B), for EVERY genuine centered mono four-edge geodesic
  z⊕{a,b} → z⊕{b} → z → z⊕{c} → z⊕{c,d}
with its two ordered-three-face windows equal to q, the two MIDDLE PHYSICAL cube edges
  {z⊕e_b,z} and {z,z⊕e_c}
have sigma-color q. Indeed the certified square Q(z;b,c) contains both edges and has color-q certificate, forcing q∈K(e) for each, hence sigma=q there. Thus each honest monochromatic ordered-face four-path projects to a same-color TWO-EDGE walk in the derived antipodally odd undirected edge-colored cube.

**Additional fact:** By the proved hub theorem nori_antipodal_square_connectedness_forces_bichromatic_connector_hub_20261008, either case (A) holds or in case (B) there exists a physical cube vertex incident with square-certified edges of BOTH sigma colors, witnessed by genuine opposite-color centered four-geodesics. No global monochromatic edge coloring can arise from the projection under active NORI.

**Precise missing lifting theorem.** To use a hypothetical result guaranteeing a long monochromatic GEODESIC in the derived ordinary edge coloring sigma to solve NORI, one must produce ordered-face-window geodesic witnesses that glue across its consecutive edges. A sigma-monochromatic path is NOT automatically a NORI monochromatic or one-switch path: individual edges may have entirely DIFFERENT centered 4-geodesic certificates, with different outer directions and physical faces. The shadow theorem creates an exact, physically genuine reduction of local TWO-EDGE witness data and isolates the necessary coherence obligation, but by itself neither proves the original edge-colored Norine conjecture nor the active NORI grand conjecture.
