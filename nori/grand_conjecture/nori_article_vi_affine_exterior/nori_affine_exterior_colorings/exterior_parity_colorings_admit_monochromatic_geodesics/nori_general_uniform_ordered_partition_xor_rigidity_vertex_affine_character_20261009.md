# General uniform ordered-partition XOR rigidity forces additive vertex parity

# Partition-parity rigidity for all uniformities and every number of blocks ≥3

Let r≥2, m≥3, n=mr, and let a assign F2-colors to all ORDERED r-tuples of DISTINCT elements of a ground set V of size n. Suppose for some fixed σ∈F2 that EVERY ordered partition (T_1,...,T_m) of V into disjoint ordered r-tuples satisfies

    a(T_1)+⋯+a(T_m)=σ  (mod 2).

**THEOREM (global partition-parity rigidity).** There exist bits d and (w_v)_(v∈V) such that for all ordered distinct r-tuples T,

    a(T)=d+Σ_(v∈T)w_v,

and necessarily m d +Σ_(v∈V)w_v=σ (mod 2). Conversely all such affine vertex-parity functions have constant partition parity. For even m the constant is Σw_v, independent of d.

**Proof.** First vary the internal order of any one r-tuple in a partition, holding all remaining tuples fixed. The partition-parity equality makes a invariant under all permutations of the r entries. Thus write a(S) for the underlying r-element set S.

Fix distinct u,v∈V and disjoint (r−1)-subsets A,B⊂V\{u,v}. Compare the two partitions containing A+u,B+v and A+v,B+u, with all other blocks identical (the  n−2r remaining elements partition into m−2 disjoint r-blocks). The two parity equalities give

    a(A+u)+a(A+v)=a(B+u)+a(B+v).

The Kneser disjointness graph KG(n−2,r−1) is connected because n−2≥2(r−1)+1 for m≥3: indeed any two (r−1)-sets differing in one element have a common disjoint neighbor, as their union has r elements and at least r−1 coordinates remain; Johnson adjacency generates the full vertex set. Therefore δ_uv(A)=a(A+u)+a(A+v) is independent of A. Call it δ_uv.

Given three distinct u,v,w, choose one (r−1)-set A disjoint from them; then δ_uv+δ_vw=δ_uw. Fix z∈V and set w_z=0 and w_u=δ_uz. Thus δ_uv=w_u+w_v for all distinct u,v. Whenever two r-subsets S,S' differ by replacing u with v, their a-values differ by w_u+w_v. Hence b(S)=a(S)+Σ_(v∈S)w_v is constant across the connected Johnson graph J(n,r). Call the constant d. This gives the representation.

Summing a over any r-block partition yields m d +Σ_V w_v=σ. Conversely this identity is immediate for all additive a. QED.

**Application to the active ordered-three-face NORI research.** For n divisible by 3 with n≥9, if the XOR of the local coordinate-triple intercept colors across EVERY partition into n/3 disjoint direction triples is fixed, then the ordered-triple color table is independent of internal ordering and is a vertex-parity character. In particular, at n=12 a failure to find an even-parity four-block partition rigidifies the local intercept table and allows explicit one-switch triple-direction orders. This lemma is independent of any face-color antipodal axiom; transporting it to arbitrary physical NORI faces requires a common actual root/exterior chart. It does not itself establish unrestricted NORI.
