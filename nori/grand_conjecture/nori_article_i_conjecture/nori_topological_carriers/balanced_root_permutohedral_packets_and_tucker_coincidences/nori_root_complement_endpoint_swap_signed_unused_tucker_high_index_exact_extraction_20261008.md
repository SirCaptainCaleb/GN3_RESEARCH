# 2n-bit root/complement-endpoint swap yields canonical unused-sign Tucker carrier and exact index-n closure test

# CANONICAL 2n-BIT ROOT / COMPLEMENT-ENDPOINT SWAP GEOMETRY AND SIGN-COHERENT TUCKER CLOSURE CRITERION

Let Q_n={0,1}^n. A (partial) directed cube geodesic P has starting root x, direction-distinct word pi=(p_1,...,p_k), USED support W={p_1,...,p_k}, physical endpoint y=x XOR W, and UNUSED support D=[n]\W.

Define its 2n-BIT ENDPOINT STATE
  a(P)=x,     b(P)=bar y = (1,...,1) XOR y = x XOR D.
This is an ordered pair (a,b)∈Q_n×Q_n. Its difference is the signed ternary vector
  eta(P)=b−a in {-1,0,1}^n,
  eta_i(P)=0 if i∈W, and eta_i(P)=1−2x_i∈{+1,−1} if i∈D.
Thus support(eta)=D precisely, and eta=0 EXACTLY iff the path uses ALL n directions (its physical endpoint is antipodal to its root).

**THEOREM 1 (canonical actual antipodal reversal is the FACTOR SWAP).** Let Θ(P) be the full physically antipodally complemented and reversed directed geodesic. Its starting root is bar y=b and its endpoint is bar x; its direction word is rev pi. Thus
   (a(ΘP),b(ΘP))=(b(P),a(P)),
   eta(ΘP)=−eta(P).
If c is an ACTIVE NORI ordered-three-face coloring, the Θ path's word of ordered-face colors is the reverse and complement of the original word, preserving the number of switches. Hence the set of monochromatic or at-most-one-switch genuinely witnessed partial paths is invariant under Θ. This is a faithful, single, support-independent involution on the FULL 2n-bit ROOT / COMPLEMENT-ENDPOINT geometry, unlike the awkward support-dependent root-only formula (x,W)->(x XOR D,W).

**THEOREM 2 (extension = monotone erasure of an unused signed coordinate).** If P is extended from its SAME starting root x by a new direction i∈D (at its endpoint), then its endpoint y flips coordinate i while a=x stays fixed. Its signed unused vector eta changes ONLY by setting eta_i to zero, with all other eta_j unchanged. Thus legal monochromatic or one-switch prefix extensions (when the coloring permits them) follow monotone COORDINATE-ERASURE CHAINS in the sign-vector alphabet {-1,0,+1}^n, terminating at the origin exactly on full antipodal geodesics.

**THEOREM 3 (actual deleted-product state geometry is an antipodal (n−1)-sphere).** Consider the continuous endpoint-pair domain
  T={(a,b)∈[0,1]^n×[0,1]^n : a≠b},
with free involution τ(a,b)=(b,a). There is an explicit strong τ-equivariant deformation retraction
  T ≃_τ ∂([-1/2,1/2]^n) ≅_τ S^(n−1).
To see this, write the midpoint m=(a+b)/2 and halfdifference d=(b−a)/2. Coordinate feasibility is
  |d_i|<=m_i<=1−|d_i|.
First continuously move m towards (1/2,...,1/2), keeping d fixed; convexity of the indicated intervals ensures a,b remain in the cube and a≠b. This reaches the centered pair (1/2−d,1/2+d), with nonzero d∈[-1/2,1/2]^n\{0}. Now radially expand d along its line to the boundary by scaling to max_i |d_i|=1/2. Both homotopies commute with swapping a,b, which sends d to −d. Therefore this is a genuine high-index free antipodal S^(n−1), not the index-one simultaneous-complement endpoint torus studied in a DIFFERENT involution earlier in NORI.

**THEOREM 4 (rigorous no-SPURIOUS-ZERO principle for certified path cells).** Let E be any finite simplicial complex whose vertices are ACTUAL monochromatic or <=1-switch directed partial path STATES P, with an involution Θ induced by their physical antipodal reversal. Suppose E is Θ-simplicial and every simplex satisfies the following literal SIGN-COHERENCE condition:
  for every coordinate i, no two vertices of the simplex have eta_i=+1 and eta_i=−1 simultaneously.
Define f:E→R^n by affine extension over simplices of the vertex vectors eta(P)∈{-1,0,1}^n. Then f is Θ-ODD and obeys the EXTRACTION PROPERTY:
  if f(z)=0 for any point z∈|E|, some vertex P of the smallest supporting simplex has eta(P)=0, hence P is a REAL FULL ANTIPODAL geodesic witnessing the SAME <=1-switch path property.
More strongly, every vertex of that smallest simplex has eta(P)=0.

**Proof.** For a point z in the relative interior of its minimal simplex σ, all barycentric coefficients λ_P are strictly positive. In each coordinate i, all nonzero eta_i(P) have one COMMON sign by sign-coherence. Therefore ∑ λ_P eta_i(P)=0 can hold only if eta_i(P)=0 for EVERY P∈σ. Doing this in every coordinate forces each eta(P)=0. Physical Θ maps eta to −eta, so f is odd. QED.

**COROLLARY 5 (an EXACT topology-first grand NORI forcing criterion).** Suppose a genuine sign-coherent, Θ-invariant *witness state carrier* E as in Theorem4 is constructed from actual <=1-switch NORI geodesic paths and its free equivariant cohomological index satisfies
  w1(E/Θ)^n !=0.
Then ACTIVE NORI GRAND CLOSURE HOLDS.

**Proof.** If no full <=1-switch antipodal path exists, all eta(P) are nonzero, and Theorem4 says f is nowhere zero on |E|. Normalizing gives an equivariant continuous map E→S^(n−1). Such a map forces w1(E/Θ)^n=0 because the tautological class of RP^(n−1) has zero nth power. Contradiction. A full path with <=1 switch is therefore witnessed at some literal E-vertex. QED.

**ESSENTIAL LIMITATIONS / CHALLENGE.**
(1) High index n is NOT automatically supplied by the continuous all-pairs domain T, which has index exactly n−1; building the extra topology must use bona fide color-admissible path/repair incidence, not merely all conceivable root/endpoint states.
(2) Sign-coherence is STRICT. An arbitrary simplicial join or affine convexification of opposite unused-direction signs would produce a SPURIOUS center zero, invalidating any 'closure' claim. Path witness cells must preserve compatible exterior/root coordinate assignments (the exact root-sheet Helly nerve is one safe source of honest root-coherent faces).
(3) The full path state can have eta=0 while the same geometric endpoint pair might have different ordered-face switch counts; the path MEMORY and actual color-word certificate must remain attached to the vertex.
(4) The Θ involution on full n-edge paths may fix the endpoint-state pair but not the direction-distinct path order, so the witness-state involution remains free for length>=2; vertex labels zero and endpoints diagonal may occur, and are EXACTLY the desired extraction.
(5) At a full root-slice permutohedron the signed-unused vector is identically zero on EVERY full geodesic regardless of its switches. Thus the carrier E for THEOREM4 MUST be built ONLY FROM ACTUALLY <=1-SWITCH PATH WITNESSES; including arbitrary bad full paths would give false extraction. Under grand failure, no vertices with eta=0 exist.

**RESEARCH DIRECTION.** This is the desired high-dimensional TOPOLOGICAL FRAME WITH COMBINATORICS INSIDE: construct certified compatible path-state cells, with literal root/path provenance, preserving coordinatewise sign-coherence and Θ equivariance, and prove they have cohomological index>=n (or construct an actual equivariant S^n inside E). The exact ternary unused-direction signature and factor-swap involution provide a CANONICAL Tucker sign labeling, avoiding the previously identified error of treating USED support as antipodally complemented. The global existence of such a sufficiently high-index E remains the GRAND OPEN GAP; this theorem is a rigorous CONDITIONAL closure mechanism, not a claimed proof.
