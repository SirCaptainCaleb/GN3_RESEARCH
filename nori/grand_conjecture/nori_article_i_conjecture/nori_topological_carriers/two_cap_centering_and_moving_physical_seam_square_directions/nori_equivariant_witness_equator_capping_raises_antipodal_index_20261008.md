# Equivariant equator capping: one-sided witness disks lift genuine spheres and raise antipodal index

# Equivariant suspension-LIFT criterion: witness-compatible fillings generate genuine antipodal cohomological index

Let X be a finite CW complex (e.g. a simplicial/cubical NORI witness complex) with a FREE continuous involution tau, and suppose X=A∪tau(A) for subcomplex A. Write C=A∩tau(A), a tau-invariant genuine intersection subcomplex. Throughout S^k carries the standard antipodal involution and its upper hemisphere in S^(k+1) is a closed (k+1)-ball with equator S^k.

**Theorem 1 (equivariant index LOWER bound from a one-sided filling).** Suppose there exists a continuous equivariant map
  g:S^k -> C,   g(-u)=tau(g(u)),
AND the map g regarded as an ordinary map S^k->A is nullhomotopic, equivalently extends to a continuous map
  G:D^(k+1) -> A
whose boundary restriction is g. Then there exists a continuous tau-equivariant map
  F:S^(k+1) -> X.
In particular, the first Stiefel–Whitney class w∈H¹(X/tau;F2) has
  w^(k+1) != 0.
Thus the cohomological antipodal index of X is at least k+1.

**Proof.** Regard the upper hemisphere H_+ of S^(k+1) as D^(k+1), its equator as S^k, and use G to define F on H_+. On the lower hemisphere H_-= -H_+, define
  F(-z)=tau(G(z))   for z∈H_+.
On the equator, where both hemisphere prescriptions apply, they agree because G(-u)=g(-u)=tau(g(u))=tau(G(u)). Thus the gluing lemma yields a continuous globally equivariant F:S^(k+1)→X. Passing to free-involution quotients gives f:RP^(k+1)→X/tau; the pullback of the cover's w is the tautological generator a∈H¹(RP^(k+1);F2), by equivariance/pullback of principal Z2-bundles. Hence f*(w^(k+1))=a^(k+1)≠0, establishing w^(k+1)≠0. QED.

**Theorem 2 (relative suspension sandwich for CONTRACTIBLE A).** If A is nonempty and contractible (in particular if A is a literal simplex or cone), then every equivariant map g:S^k→C for k>=0 has an ordinary nullhomotopic composite S^k→A, so the suspension lift applies. Consequently
  ind_Z2(C)+1 <= ind_Z2(X)
provided C is nonempty and the index is defined via maximum nonzero w power. The general UPPER index bound from Item nori_equivariant_two_shore_overlap_dimension_bounds_antipodal_index_20261008 says
  ind_Z2(X) <= dim(C)+1.
Thus for a contractible one-shore carrier A,
  ind_Z2(C)+1 <= ind_Z2(X) <= dim(C)+1,
where the left inequality requires an equivariant map from a sphere S^k realizing ind(C); a free complex can have high cohomological index without an equivariant sphere map from that dimension, so in FULL generality replace ind(C) on the left by
  coind(C)=max{k: exists equivariant S^k→C}.
The rigorously valid sandwich is
  coind(C)+1 <= ind(X) <= dim(C)+1.
This proviso distinguishes topological index from coindex; conflating them would be false.

**Corollary 3 (an actionable NORI monochromatic-disk test).** Let X=X_c be the actual cubical center-square witness complex of an active NORI coloring, and A=X_0 be the genuine color-0 certified square subcomplex together with all physical cube vertices. Let C=X_0∩X_1 be its color-overlap subcomplex. Suppose C contains a tau-equivariant closed loop g:S¹→C: geometrically, an antipodally paired physical loop whose full set of edges each admits BOTH-color genuine monochromatic centered four-path certificates. If this loop also bounds a continuous disk in X_0 (for example a finite combinatorial disk tiled by color-0 certified squares with compatible boundaries), then
  w_1(X_c/tau)^2≠0.
This is exactly the missing TOP-DIMENSIONAL counterpart of the previous result: absence of any common-edge certificate forces w1²=0, while the presence of an equivariant common-edge CYCLE which can be capped by honest monochromatic squares forces w1²≠0.

**Important geometric warning.** A cycle being a mod-2 homological boundary in X_0 does NOT automatically give a nullhomotopy; the theorem assumes an actual disk/nullhomotopy. A single isolated common edge, even accompanied by its antipodal mate, gives no equivariant S¹ loop unless there are connecting common edges.

**Corollary 4 (the EXACT root-profile two-shore carrier).** Let K=A∪tau(A) be the exact LABEL-SPACE carrier of nori_reversed_tail_root_profile_nerve_tucker_label_reduction_20261008 and nori_reversed_tail_mixed_profile_interface_equivariant_suspension_20261008, where A=union_x Delta(L_x), C=A∩tau(A). The universal singleton support labels guarantee that A is a CONE, not generally a simplex, hence contractible. Therefore any equivariant map S^k→C caps in A and induces an equivariant S^(k+1)→K; an equivariant loop in C yields nonzero w1² on K. The SIGNED-ROOT NERVE N is a DIFFERENT complex: its positive and negative vertex shore simplices do not themselves cover the mixed faces, and one must NOT write N=A∪tau(A) with only those shore simplices. Rather, the previously proved equivariant nerve equivalence K≃_tau N transfers the resulting cohomological index statement from K to N. The challenge is to build the equivariant loop inside actual mixed-label C, where each simplex has real common-reachability certificates.

**Research strategy: topology first, combinatorics inside it.** Pursue a growing family of genuine root/terminal-memory witness cells to construct an equivariant circle (and higher sphere) in C. The four-edge opposite-color reversed-tail diamonds are local candidate 1-cells, but they prove SAME support for the two reversed tails, whereas the GRAND fixed point needs COMPLEMENTARY support. They cannot be treated as cells of C until that compatibility is established. If a valid equivariant loop in C is established, the index rises through the cone structure. The remaining high-index-to-fixed-point step must then use the root-probability difference field V(a,b)=a-b and the exact deleted-product dimension obstruction: index or coindex at least p−1 (where p is retained profile count) is too high for a hypothetical no-closure carrier Z⊆S^(p−2). No such high-index lower bound is presently proved.

**No grand-closure claim.** This result is a complete general topological lemma and an exact set of sufficient witness conditions. The major combinatorial problem is supplying honest overlap loops and their fillings from the physical ordered-three-face constraints, and then reaching the required index threshold.
