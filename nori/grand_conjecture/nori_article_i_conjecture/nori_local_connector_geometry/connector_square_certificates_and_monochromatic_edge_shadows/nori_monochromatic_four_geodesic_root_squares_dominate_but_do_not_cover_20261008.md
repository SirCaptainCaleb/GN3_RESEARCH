# Monochromatic four-geodesic root-square union dominates every cube but can omit a prescribed root

# Witness-root cubical domination, and why a global single-valued reachability label is impossible

Let n>=5 and color actual physical ORDERED three-faces of Q_n by bits; antipodal reversal oddness is imposed only for the explicit obstruction example below. Define
  R_4={x in Q_n : there exists a genuine monochromatic FOUR-EDGE directed cube geodesic ROOTED at x}.
No requirement is placed on prescribed terminal directions in this coarse root set.

**THEOREM 1 (root-witness dominating set, all binary colorings).** Every physical cube vertex z has an ACTUAL cube neighbor x∈R_4. Equivalently, R_4 dominates the entire cube graph Q_n. In particular
  |R_4|>=ceil(2^n/(n+1)).
More precisely for each hub z there is a physical 2-dimensional ROOT SQUARE Q_root consisting entirely of starting vertices for the SAME ordered monochromatic four-edge word with identical ordered physical three-face windows, and one of the square's four vertices is a neighbor of z.

**Proof.** The centered five-direction odd-cycle theorem (proved separately in NORI; needs no NORI antipodal oddness) supplies at z some genuine monochromatic CENTERED four-edge path with ordered distinct direction word (a,b,c,d). Its start root is r=z xor {a,b}. Both consecutive physical ordered three-face windows of this path have free coordinates b,c. Therefore as proved in the middle-root-square lemma, the SAME two physical faces in the SAME order are traversed for every starting root
  r xor H, H⊆{b,c}.
All four starting vertices belong to R_4. In particular r xor b=z xor a is a CUBE NEIGHBOR of z. Since z was arbitrary, R_4 is dominating. Each chosen root in R_4 dominates at most n+1 cube vertices including itself, so |R_4|(n+1)>=2^n, yielding the cardinality bound. QED.

**THEOREM 2 (sharp qualitative warning: R_4 need not equal the whole cube even under ACTIVE NORI).** For every n>=6 and every PRESCRIBED physical cube root x, there exists a genuine binary coloring of ORDERED PHYSICAL 3-faces satisfying the active NORI axiom
  c(bar F,reverse pi)=1-c(F,pi)
such that NO FOUR-EDGE ordered cube geodesic rooted at x is monochromatic. In particular x∉R_4.

**Construction and proof.** For each physical ordered three-face (F,pi) let T be its three free coordinates. Define its *exterior Hamming distance from x* as
  d_x(F)=#{i∉T: fixed exterior bit of F in coordinate i differs from x_i}.
There are n−3 exterior coordinates. Prescribe color0 on ALL ordered physical 3-faces with d_x(F)=0, and color1 on ALL ordered physical 3-faces with d_x(F)=1, regardless of the direction order pi. These prescriptions are compatible with NORI antipodal-reversal-oddness when n−3>=3: under the face antipode, d_x(bar F)=(n−3)−d_x(F), so the antipodal mate of a 0-layer face lies at distance n−3>=3 and is unprescribed, while the mate of a 1-layer face lies at distance n−4>=2 and is unprescribed. No prescribed face lies in the reversal orbit of another prescribed face. Complete the remaining antipodal-reversal orbit colors freely, always setting mate colors complementary.

Now take ANY four distinct directions (a,b,c,d) and its genuine rooted four-edge path starting at x. Its FIRST ordered three-face (a,b,c) contains root x, so has d_x=0 and color0. Its SECOND ordered three-face (b,c,d) begins after direction a was flipped; since a lies outside {b,c,d}, the physical face's exterior bits differ from x on EXACTLY coordinate a, so it has d_x=1 and color1. Therefore every rooted four-path at x has the two-window word (0,1), hence NONE is monochromatic. QED.

**Topological architecture implication.** The center-based certified-square complex X_c has ALL physical cube vertices and genuine middle-pair squares and is connected under active NORI; each certified centered four-path also generates a separate FULL 2-face in the space of STARTING ROOTS. The union of these genuine root-squares projects to a DOMINATING vertex set, but not necessarily to all of Q_n. One may therefore build a multivalued/witnessed topological cover using closed vertex stars of these root-squares, rather than assume every physical root has a monochromatic rank-two terminal label. However thickening a witness square to cover an adjacent root does NOT turn that adjacent root into a genuine four-path witness: the combinatorial incidence/face-provenance must be retained in a carrier before applying Tucker, cubical Sperner, or KKM.

**Scope.** This does not force full grand closure; it identifies the precise geometric amount of universal local reachability and disproves the too-strong claim that every root admits even a four-edge monochromatic start in all valid colorings. The correct topological object is a supported/multivalued root-chart complex with honest certificates.
