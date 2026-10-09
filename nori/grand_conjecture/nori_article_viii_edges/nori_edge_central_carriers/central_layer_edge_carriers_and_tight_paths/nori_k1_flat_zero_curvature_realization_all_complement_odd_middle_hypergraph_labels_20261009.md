# Every complementary-odd middle-layer hypergraph labeling extends to a globally flat antipodally odd cube-edge coloring

# Arbitrary complement-odd middle-layer labels embedded in ZERO-CURVATURE odd edge colorings

Fix n=2k EVEN, k>=2. Let lambda assign a bit to every rank-k cube vertex S (equivalently every k-subset of [2k]) such that lambda(S^c)=1+lambda(S) mod2. Define the three-middle-layer EDGE prescription c(S--outer)=lambda(S) for each physical cube edge from rank k to rank k−1 or k+1. This prescribed belt coloring is legal under antipodal oddness, as previously established in Item nori_k1_even_central_vertex_gate_exact_johnson_tight_path_correspondence_20261009.

**THEOREM (globally FLAT odd extension exists for EVERY lambda).** There is a global coloring of EVERY physical undirected edge of Q_(2k) extending that middle-belt prescription and satisfying SIMULTANEOUSLY:
 (i) c(bar e)=1+c(e) for all physical edges;
 (ii) XOR of its FOUR edge colors around EVERY physical square face is ZERO, i.e. delta c=0 identically.
In fact the coloring may be chosen as an exact vertex-potential coboundary c({u,v})=phi(u)+phi(v) for a Boolean phi with a precise antipodal twist.

**Construction and proof.** Put K=1+k mod 2 (same as 1−k modulo2). We require the vertex potential identity
   phi(bar v)=phi(v)+parity(v)+K,                (∗)
where parity(v)=number of 1-bits modulo2. Because n is EVEN, parity(bar v)=parity(v), so applying the identity twice is consistent for every antipodal vertex pair.

On the MIDDLE rank-k vertices, prescribe phi(S)=lambda(S). Since parity(S)+K=k+(k+1)=1 modulo2, condition (∗) here says phi(S^c)=phi(S)+1, exactly the assumed complementary-oddness of lambda. On the two ADJACENT ranks k−1 and k+1, prescribe phi(v)=0 for EVERY vertex. Their antipodal pairing interchanges these two ranks, and parity(v)+K=(k−1)+(k+1)=0 modulo2, so this prescription also satisfies (∗). All remaining antipodal vertex pairs lie outside these three ranks; pick phi at one member arbitrarily and use (∗) to define phi at the other. This is always consistent because complement preserves vertex parity in even dimension.

Now define the full physical edge coloring by
   c({u,v})=phi(u)+phi(v) mod2.
This is a valid undirected edge coloring. Every physical square boundary has each vertex twice, so delta c(F)=0 for ALL squares. For an edge {u,v}, adjacent vertices have opposite parity, and therefore
   c({bar u,bar v})
   =phi(bar u)+phi(bar v)
   =phi(u)+phi(v)+parity(u)+parity(v)+2K
   =c({u,v})+1,
giving antipodal oddness. Finally, if edge {S,v} lies in the three-level belt with S rank k and v rank k−1 or k+1, its color equals lambda(S)+0=lambda(S), exactly the given prescribed belt coloring. QED.

**Exact accompanying classification for all globally FLAT antipodally odd edge colorings.** Conversely, if a global physical edge coloring c satisfies zero square curvature delta c=0 on every square, the simply connected cubical cube has a Boolean vertex potential phi with c({u,v})=phi(u)+phi(v), unique up to a global additive bit. Antipodal oddness then forces the function psi(v)=phi(v)+phi(bar v) to toggle across EVERY cube edge, so psi(v)=parity(v)+K for a unique K in F2. Applying psi at the antipodal vertex gives consistency ONLY when n is even. Thus:
 - for ODD n, globally flat antipodally odd physical edge colorings DO NOT EXIST, in agreement with the sharp odd-curvature flux theorem;
 - for EVEN n, the entire globally flat odd-edge class consists EXACTLY of the gradients of potentials phi satisfying twist (∗), up to the irrelevant global complement phi→phi+1.
The constructed extension is therefore not an isolated trick: it embeds arbitrary k-uniform complementary-odd middle labels inside the FULL flat branch.

**Consequences for topological/tight-path strategy.** Combine with the exact three-way correspondence in Item nori_k1_even_central_vertex_gate_exact_johnson_tight_path_correspondence_20261009. The question of whether every complement-odd labeling lambda has a monochromatic tight k-uniform path on 2k−1 DISTINCT directions is EXACTLY the question of whether the associated central-vertex-sign belt coloring has a monochromatic full antipodal cube geodesic contained in those three rank layers. The current theorem proves that EACH such prescribed belt coloring can be extended to a GLOBAL ZERO-CURVATURE, ANTIPODALLY ODD edge coloring. Thus arbitrary complementary-odd hypergraph complexity remains present even after imposing PERFECT FLATNESS on all physical cube squares. A proposed even-dimensional global proof that rules out only nonzero curvature, or claims that flatness forces a centrally confined geodesic without addressing the tight-path question, is incomplete. The unrestricted edge conjecture may still hold by paths LEAVING the three-level belt; no counterexample to the unrestricted conjecture is asserted.

**Cohomological significance.** This identifies a sharp parity split: odd-dimensional antipodally odd edge colorings have a nonzero primary square-curvature flux of density at least 1/binom(n,2), whereas in even dimensions the primary curvature can vanish ENTIRELY while preserving the full combinatorial richness of complement-odd middle hypersimplex labels. This is a concrete reason to seek a SECONDARY invariant or a root-coupled path-space topology, rather than treating the first curvature obstruction as the global fixed-point proof.
