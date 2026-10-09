# Topological closure forcing via deleted-product near-acyclicity and exponentially many required rooted labels

# Topology-first closure forcing: deleted-product near-acyclicity plus too few literal NORI reachability labels

Let n>=5 and let c be ANY active NORI coloring. Let Omega denote the actual FORMAL reversed-terminal-label alphabet
  Omega={(J,U): J=(a,b) ordered distinct, empty!=U proper subset D_J=[n]\{a,b}},
with free involution tau(J,U)=(rev J,D_J\U). Its size is
  M=|Omega|=n(n−1)(2^(n−2)−2).

For each cube root x let L_x⊆Omega be the EXACT color-free monochromatic terminal-memory profile of the active reversed-tail splice theorem. Let r_1,...,r_p be one representative of every distinct inclusion-MAXIMAL root profile, p>=1. Put L_i=L_(r_i).

Let
  A=union_i Delta(L_i), K=A union tau A, C=A intersect tau A.
The prior proved root-probability interface theorem supplies a finite equivariant product-cell model
  Z = union_{(I,J) allowed} Delta(I)×Delta(J) ⊆ Delta^(p−1)×Delta^(p−1),
where nonempty I,J⊆[p] are allowed iff there is at least one ACTUAL label
  u∈(intersection_{i∈I}L_i) intersect (intersection_{j∈J}tau L_j).
The involution swaps the factors, Z is equivariantly homotopy equivalent to C, and GRAND CLOSURE is equivalent to any diagonal product point (a,a)∈Z.

Assume HYPOTHETIC GRAND FAILURE. Then any allowed I,J must be DISJOINT, since a shared root index gives u and tau u in one profile. Therefore
  Z⊆D_p={ (a,b): supp(a)∩supp(b)=empty }≅_equiv S^(p−2)
for p>=2, with interchange corresponding to the antipodal sphere map. Z is a finite cell SUBCOMPLEX of the standard deleted-product sphere.

**THEOREM 1 (one missing maximal chamber amplifies homology forcing).** Suppose p>=3, the mixed interface C is NONEMPTY, and the reduced mod-2 homology of the mixed interface satisfies
  tilde H_j(C;F2)=0 for all j=0,1,...,p−3.
If SOME NONTRIVIAL ordered partition [p]=I disjoint union J, I,J nonempty, has NO ACTUAL common reachability label satisfying
  u∈L_i for EVERY i∈I; tau u∈L_j for EVERY j∈J,
then the GRAND NORI conjectural conclusion HOLDS.

**Proof by contradiction.** Suppose grand failure. The missing partition is precisely a MISSING top-dimensional product cell Delta(I)×Delta(J) of the deleted-product sphere D_p, of dimension (|I|−1)+(|J|−1)=p−2. Since D_p is a connected finite mod-2 closed (p−2)-dimensional PL sphere and Z is a PROPER subcomplex missing a top cell, we have
  H_(p−2)(Z;F2)=0.
Indeed a mod-2 top cycle supported in D_p has equal coefficients on adjacent top cells, because the codimension-one incidence graph of the sphere is connected and each interior facet belongs to exactly two top cells. Thus any nonzero top cycle uses EVERY top cell of D_p, impossible for proper Z.
Because C is NONEMPTY, the equivariantly equivalent Z is NONEMPTY. The equivariant homotopy equivalence Z≈C and the assumed reduced lower-homology vanishing give tilde H_j(Z)=0 for all j<p−2. The dimension bound eliminates homology j>p−2, and the missing top chamber eliminates the remaining top homology, so Z is F2-ACYCLIC and nonempty. Its Euler characteristic χ(Z)=1.
But swap of probability factors acts FREE on the no-grand deleted product D_p. It is a free cellular involution on Z after equivariant subdivision, pairing every simplex/cell and forcing χ(Z) EVEN. Contradiction. QED.

**THEOREM 2 (universal label-count upper bound if ALL top chambers exist).** Under grand failure, any individual formal label u∈Omega can certify AT MOST ONE nontrivial ordered bipartition (I,J) with I∪J=[p] and I∩J=empty. Consequently, if EVERY top-dimensional chamber of D_p is allowed in Z, then
  2^p−2 <= M=n(n−1)(2^(n−2)−2).

**Proof.** For a formal label u, define its actual maximal-root incidence sets
  P(u)={i:u∈L_i},  Q(u)={i:tau u∈L_i}.
Grand failure says P(u)∩Q(u)=empty for every u. To witness a FULL ordered bipartition [p]=I∪J, require I⊆P(u) and J⊆Q(u). Since I,J partition ALL root indices and P,Q are disjoint, this forces P(u)=I and Q(u)=J, exactly. Thus u can witness NO OTHER full ordered bipartition. The 2^p−2 ordered nontrivial partitions require at least that many distinct u∈Omega, proving the inequality. QED.

**COROLLARY 3 (new finite topology + counting closure criterion).** If C is NONEMPTY and
  2^p−2 > n(n−1)(2^(n−2)−2)
AND
  tilde H_j(C;F2)=0 for every 0<=j<=p−3,
then grand closure is FORCED. Equivalently, under no grand closure, once
  p>log_2(M+2),
the mixed interface MUST possess nonzero reduced mod-2 homology in SOME degree j<=p−3. It is NOT sufficient for a hypothetical counterexample simply to have the full top sphere class: the small exact label alphabet PROHIBITS filling the whole deleted-product sphere at such p.

**EXAMPLE SCALE.** At n=8 the exact formal label count is M=8*7*(2^6−2)=3472. Since 2^12−2=4094>3472, any active Q8 coloring with p>=12 distinct maximal root profiles and vanishing reduced homology through degree p−3 automatically satisfies grand closure. For p smaller or with nonvanishing lower homology this criterion is silent.

**COROLLARY 4 (p=3 topological six-chamber rigidity).** Let p=3. Under hypothetical grand failure, if C is CONNECTED and nonempty, its equivariant deleted-product model Z is also connected. As a nonempty connected tau-invariant subcomplex of D_3≅S¹, it must be the WHOLE six-edge deleted-product circle, so ALL SIX ordered nontrivial bipartitions of three roots admit genuine reachability labels as in Theorem2. Conversely, if ANY one of the six maximal bipartition-label intersections is empty, connected C already forces grand closure. This is the p=3 instance of Theorem1 and translates the needed topological condition to literal physical witness packets.

**CENTRAL RESEARCH USE.** The desired GLOBAL PROOF CAN BE TOPLOGICAL, WITH COMBINATORICS INSIDE THE FRAME:
  (a) establish enough connectedness/low-dimensional homological vanishing in the ACTUAL mixed-profile interface C using local physically certified monochromatic hub squares, reversed-tail root diamonds, rank-six one-switch centers, and compatible repairs;
  (b) invoke the exact deleted-product sphere forcing above;
  (c) invoke the STRICT finite label-incidence bound, or exhibit ONE forbidden root bipartition chamber by color/physical-face structure;
  (d) derive a fixed point of the odd root-probability difference field and extract an ACTUAL same-root complementary-support reversed-tail witness.

This theorem proves the topology-to-combinatorics reduction, including the stronger near-acyclicity criterion and a counting obstruction. It DOES NOT prove universal NORI closure: low-homology vanishing for C is not known, and p may be too small for the label-count threshold. The finite count gives a new constraint on any hypothetical counterexample, rather than excluding them unconditionally.

## Sharpened top-chamber alphabet: ONLY middle-rank labels can participate under no closure

Under hypothetical failure, the previously proved rank restriction on actual profiles excludes all co-singleton supports |U|=n−3, since a monochromatic (n−1)-edge branch would extend to a full one-switch geodesic. The original formal alphabet already excludes empty and full supports, and all SINGLETON labels are universal in every root profile. A singleton label u=(J,{i}) cannot lie in the mixed interface C under no closure: its complement tau u has co-singleton support and appears in NO root profile. By tau symmetry co-singletons likewise cannot lie in C.

Thus every possible vertex of C has support rank
  2 <= |U| <= n−4.
The number of available MIDDLE-RANK formal labels is exactly
  M_mid = n(n−1) * [ 2^(n−2)−2−2(n−2) ]
        = n(n−1) * [2^(n−2)−2n+2].
All labels witnessing complete ordered bipartition cells of Z must be actual C-vertices, hence lie in this smaller alphabet. Therefore Theorem 2 improves to:
  grand failure + Z=D_p
    ==> 2^p−2 <= M_mid.
In particular the quantitative topology+counting criterion of Corollary 3 is valid under the STRICTER sufficient threshold
  C nonempty,   2^p−2 > M_mid,
  and tilde H_j(C;F2)=0 for j=0,...,p−3
    ==> GRAND CLOSURE.
For n=6 one has M_mid=30*6=180, and p>=8 suffices for the missing-cell count (2^8−2=254>180). For n=8 M_mid=56*50=2800 and p>=12 suffices.

This is a genuine improvement: the universal singleton cone vertices are essential to the contractibility of A, but are FORBIDDEN in the cross-root mixed interface under hypothetical no closure. One must not count them as potential top-product-cell witnesses. This provides a natural support-rank filtration for a future relative Tucker/KKM proof.
