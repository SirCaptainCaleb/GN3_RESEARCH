# Second antipodal index forces a physical antipodal path of doubly monochromatic-certified edges

# Higher-index NORI forcing is an ANTIPODAL PATH of doubly certified physical edges, not merely one overlap edge

Let X be a finite regular CW (in particular simplicial/cubical) complex with a free cellular involution τ, and suppose X=A∪τ A, for subcomplex A; put C=A∩τA (automatically τ-invariant).

**GENERAL THEOREM (componentwise equivariant two-shore bridge).** If every CONNECTED COMPONENT of C is distinct from its τ-image, then there is a τ-equivariant continuous map X→S¹ (target antipodal). Consequently w_1(X/τ)²=0. Its contrapositive is
  w_1(X/τ)² !=0
    => SOME connected component of C is τ-INVARIANT.
This conclusion is strictly stronger than the preceding theorem nori_equivariant_two_shore_overlap_dimension_bounds_antipodal_index_20261008 when C contains many edges and cells yet its components all occur in antipodal pairs. No upper dimension bound on C is needed.

**Proof.** The finite complex C has finitely many connected components, each a closed and open subcomplex. By hypothesis τ pairs them with no fixed component. Choose one component from each τ-pair and assign constant value +1 to all its points; assign −1 on the image component. This is a continuous equivariant map g:C→S^0={−1,+1}. Embed S^0 as the two boundary endpoints of a closed upper semicircle H_+⊂S¹. Because H_+ is homeomorphic to an interval, the map g extends continuously from C to A with image in H_+ (either by barycentric interpolation on a triangulation of A or the elementary Tietze theorem for finite polyhedra). Write G:A→H_+ for this extension. On τA define F(x)=−G(τx), mapping to the opposite lower semicircle. On C the prescriptions agree: −G(τx)=−g(τx)=g(x)=G(x). The gluing lemma gives continuous F:X→S¹, satisfying F(τx)=−F(x). Pulling back the antipodal S¹ double cover implies w_1²=0 on X/τ. QED.

**NORI APPLICATION (actual two-color overlap geometry).** In an active NORI coloring n>=5, let X=X_c be the genuinely certified-center square complex, let A=X_0 be the subcomplex containing all physical cube vertices and all actually color-0-certified middle-pair squares and their boundary edges, and τA=X_1 be the corresponding color-1 complex. The overlap
  C=X_0∩X_1
contains ALL cube vertices; its one-skeleton consists EXACTLY of physical cube edges e for which K(e)={0,1}, i.e. edges lying in honest centered mono-four middle-pair squares of BOTH colors. A square of X is in C iff it has both color certificates; any such square has all boundary edges doubly certified. Therefore connectivity of C is equivalent to connectivity of this PHYSICAL BICHROMATIC COMMON-EDGE GRAPH H whose vertex set is all physical cube vertices and whose edge set is {e:K(e)={0,1}}.

**COROLLARY (higher index forces an antipodal chain of genuine color-flexible edges).**
If
   w_1(X_c/τ)^2 !=0,
then for some actual cube vertex z, there is a sequence
  z=z_0,z_1,...,z_m=bar z
of adjacent physical cube vertices such that EVERY physical edge {z_(j−1),z_j} is certified by a genuine monochromatic centered four-edge geodesic of color0 AND (possibly different) one of color1. As z and bar z differ in ALL n coordinates, necessarily m>=n. The chain can reuse coordinate directions; it is NOT automatically geodesic or witness-compatible.

**Proof.** The general theorem supplies a τ-invariant connected component C0 of C. Pick any physical vertex z in C0 (every nonempty subcomplex component contains vertices). Because τC0=C0, its antipode bar z also lies in C0. Connectivity of a finite CW complex implies connectivity of its 1-skeleton: cell attachments of dimension at least2 cannot connect distinct 1-skeleton components. Thus z and bar z are joined by a path in the 1-skeleton C0^(1), precisely the doubly-certified physical edges. Hamming distance between endpoints is n, so every such edge path has length >=n. QED.

**Position in the NORI program.** This isolates a very tangible topological-to-combinatorial task. A proof forcing w_1² nonzero would guarantee a FULL ANTIPODAL CHAIN of opposite-color certificates, not only a local bichromatic edge. To close the GRAND geodesic conjecture, one would still need a directional-no-repeat, ordered-terminal-memory coherent extraction from that chain (or find a different higher-index carrier if the actual X_c has index one, as the valid coordinate-only no-go example shows). No universal positive w_1² is claimed.
