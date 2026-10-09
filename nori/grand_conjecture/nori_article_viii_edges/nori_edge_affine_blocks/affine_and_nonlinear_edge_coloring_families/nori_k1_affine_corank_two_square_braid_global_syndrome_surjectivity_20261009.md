# All odd affine edge colorings of corank at most two realize every direction-color word via a square-or-braid syndrome certificate

# Every affine antipodally odd edge coloring of corank at most TWO realizes EVERY direction-indexed full-geodesic color vector

**Setting.** Work over F2. Let n>=2, let A∈F2^{n×n} have A_ii=0 for all i and A·1=1 (every row has odd weight), and choose arbitrary b∈F2^n. Color the undirected physical edge in direction i at vertex x by c_i(x)=b_i+(Ax)_i. The zero diagonal makes this independent of which endpoint is used; A1=1 gives the antipodal oddness c_i(bar x)=1+c_i(x). Let W=F2^n/im(A), with quotient projection [·], and let k=dim(W)=n−rank(A).

**THEOREM (all affine corank≤2).** If k<=2, then for EVERY prescribed vector T=(T_1,...,T_n) in F2^n there exist a full direction permutation p and an actual starting root x∈Q_n such that the unique edge of direction i along the full n-edge antipodal geodesic P(x,p) has color T_i. In particular T=0 yields a monochromatic full antipodal geodesic. Rank n and corank1 already follow from the previous affine theorem nori_k1_affine_corank_one_closure; the NEW assertion is the general corank2 case, with no restriction on n.

**Lemma 1 (affine color syndrome and physical adjacent-swap vectors).** Let
  u_i(p)=Σ_{j before i in p} A_{ij}∈F2.
Along the actual full x-rooted geodesic with direction order p the direction-indexed edge-color vector is exactly
  C(x,p)=b+A x+u(p).
When p and p' differ by swapping two ADJACENT directions i,j, the difference is exactly
  u(p)+u(p')=v_ij:=A_ij e_i + A_ji e_j.
This is an honest effect on two actual direction-edge colors; all other coordinates' edge colors remain fixed.
Proof: immediately before the direction-i edge, precisely its earlier directions have been toggled, so its color is b_i+(Ax)_i+Σ_{j earlier}A_ij. An adjacent swap changes only the order relation of i and j. QED.

**Lemma 2 (all pair-swap vectors span the cokernel).** For EVERY A with zero diagonal and odd row sums, the quotient classes ell_ij=[v_ij] for unordered pairs {i,j} span W.
Proof. Let a linear functional on W vanish on all ell_ij. Represent it by u∈ker(A^T)⊆F2^n, so u_i A_ij+u_j A_ji=0 for all i≠j. For any fixed j,
  0=(A^T u)_j=Σ_{i≠j}u_i A_ij
    =u_j Σ_{i≠j} A_ji =u_j,
because the last sum is the odd parity of row j. Therefore u=0. The annihilator of the classes ell_ij is trivial; they span W. QED.

**Lemma 3 (local SQUARE certificate).** If two DISJOINT coordinate pairs {a,b},{c,d} have independent quotient effects ell_ab,ell_cd in a 2-dimensional W, then all four W-syndromes are realized by four FULL genuine direction permutations: put (a,b) and (c,d) as two consecutive two-coordinate blocks in a fixed full permutation, and independently swap the order within either block. The four syndromes are
  w, w+ell_ab, w+ell_cd, w+ell_ab+ell_cd,
which exhaust W. Every candidate permutation supplies a literal full x-rooted geodesic after solving Ax from the target syndrome. QED.

**Lemma 4 (local BRAID-HEXAGON certificate and its EXACT failure).** Let a,b,c be three coordinates with ell_ab=A0 and ell_bc=B0 linearly independent in W=F2². Put C0=ell_ac. Fix all other direction coordinates outside one contiguous {a,b,c} block and let the block run through its SIX orderings. Relative to the order abc, their exact quotient-syndrome offsets are
  0, A0, B0, A0+C0, B0+C0, A0+B0+C0.
These SIX offsets cover all FOUR elements of W IF AND ONLY IF A0+B0+C0 !=0.
Proof. Since A0,B0 are a basis, C0∈{0,A0,B0,A0+B0}. For the first three possibilities the displayed six offsets include 0,A0,B0,A0+B0. For C0=A0+B0, the six offsets reduce to 0,A0,B0, with A0+B0 missing. Each offset is obtained by counting actual pair inversions of the three coordinate directions and applying Lemma1. QED.
The same statement holds whenever ANY TWO of the three pair-effects are independent, after relabeling the three directions so the independent effects share their middle named vertex b.

**Lemma 5 (no all-bad square-and-braid labeling can come from odd A).** Suppose k=2. Then there exist EITHER two disjoint pair-effects linearly independent in W, OR a triple of coordinates whose pair-effects include two independent classes and whose sum is nonzero. In other words, the failures of Lemmas3 and4 CANNOT occur globally for a zero-diagonal, odd-row-sum A.

Proof by contradiction, with exact characterization of the only possible abstract obstruction. Assume that no disjoint pair of edges has independent labels, and no triple with two independent pair labels has nonzero total sum. By Lemma2 some pair of labels are independent. Under the first assumption their underlying edges meet. Relabel them as
  ell_12=A0, ell_13=B0
with A0,B0 independent. The second assumption forces
  ell_23=C0:=A0+B0,
the third nonzero vector of W.

Fix any exterior vertex k outside {1,2,3}. Independence against DISJOINT marked edges gives:
  ell_1k ∈{0,C0}, since 1k is disjoint from 23 carrying C0;
  ell_2k ∈{0,B0}, since 2k is disjoint from 13 carrying B0;
  ell_3k ∈{0,A0}, since 3k is disjoint from 12 carrying A0.
The no-good-braid hypothesis on triangle {1,2,k} shows ell_1k and ell_2k must EITHER both vanish OR equal (C0,B0), since A0+C0+B0=0. Applying the same argument to {1,3,k} and {2,3,k} forces:
  (ell_1k,ell_2k,ell_3k) ∈ {(0,0,0),(C0,B0,A0)}.
Call k *active* if the second triple occurs. At most ONE exterior vertex is active: if k,l are distinct active vertices, the DISJOINT edges 1k and 2l carry independent labels C0,B0, contradiction.
Also for any exterior k,l distinct, edge kl is disjoint from BOTH the marked edges 12 carrying A0 and 13 carrying B0, so ell_kl=0. Thus the entire nonzero-label graph is EITHER:
  (I) exactly a colored triangle on vertices 1,2,3 carrying A0,B0,C0, or
  (II) a colored K4 on vertices 1,2,3,k, in which EVERY one of its four vertices has three incident labels A0,B0,C0, with all labels outside this K4 zero.

Now use the actual MATRIX origin of the labels. For every coordinate i the following intrinsic quotient identity holds:
  Σ_{j≠i} ell_ij
   =[Σ_{j≠i}(A_ij e_i + A_ji e_j)]
   =[(Σ_{j≠i}A_ij)e_i + A e_i]
   =[e_i],
since every row sum is1 and [A e_i]=0 in W.

In case (II), each of the four active vertices has incident labels A0+B0+C0=0, and all other vertices are isolated; hence [e_i]=0 for EVERY i. But coordinate classes [e_i] generate W of dimension2, contradiction.

In case (I), the identity gives
  [e_1]=A0+B0=C0,
  [e_2]=A0+C0=B0,
  [e_3]=B0+C0=A0,
  [e_i]=0 for i>=4.
For every matrix column j∈{1,2,3}, its image in W must vanish:
  0=[A e_j]=A_1j C0 + A_2j B0 + A_3j A0.
Because A0,B0,C0 are the three nonzero elements of F2², the ONLY solutions (A_1j,A_2j,A_3j) to this equation are (0,0,0) or (1,1,1). But A_jj=0 by the physical edge-color rule, excluding (1,1,1); hence ALL three coefficients in EACH of the first three columns are ZERO. Thus A_12=A_21=0, giving ell_12=0, contrary to ell_12=A0≠0. Contradiction in both cases. QED.

**PROOF OF THE GRAND AFFINE CORANK-TWO THEOREM.** Given target T, by Lemmas2 and5 and the hypotheses k=2 we have a genuine permutohedral square or three-braid hexagon of FULL direction permutations with quotient syndromes [u(p)] taking EVERY value of W. Therefore choose one p with
  [u(p)]=[T+b].
By definition of W there exists x∈F2^n such that
  A x =T+b+u(p).
By Lemma1 the ACTUAL full antipodal geodesic P(x,p) then has direction-indexed colors C(x,p)=T, as desired. The cases k=0,1 follow from the already proved full-rank and corank-one results, or from Lemma2 plus a single adjacent swap for k=1. QED.

**Additional constructive details.** One can compute a basis of W by Gaussian elimination, enumerate O(n²) pair-effect classes ell_ij, search O(n^4) disjoint pairs for two independent labels or O(n³) triples for a nondegenerate braid, then check at most SIX full direction permutations and solve one linear system Ax=T+b+u(p). Lemma5 guarantees a certificate. This is a finite polynomial-time all-target geodesic algorithm for corank≤2 in EVERY dimension. For corank2 the witness permutation lies inside one genuine square or six-vertex braid face of the permutohedron of all n! direction orders; one need not search the whole symmetric group.

**Boundary and connection with topology.** The braid with three pair-effect labels equal to the three distinct nonzero W elements has only THREE quotient syndromes, an exact genuine local hexagon obstruction. Such bad triangles CAN occur locally, but the odd-row and diagonal conditions force an independent compatible square or a nondegenerate braid elsewhere. This is a complete, rigorously checked low-dimensional *syndrome-certificate patching theorem*. At corank3, a square/hexagon carries at most 4/6 distinct syndromes and cannot cover all 8 by itself. A higher-dimensional coherent arrangement of two-faces, rather than merely independent pair-vector spans, is required. The theorem concerns ORIGINAL k=1 edge coloring, not unrestricted ordered-three-face NORI, and it does not settle arbitrary nonlinear antipodally odd edge colorings.
