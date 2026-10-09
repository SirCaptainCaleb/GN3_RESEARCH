# Sharp NORI Helly isolation begins at length six; topology entirely from lengths 3–5

# Exact high-rank isolation of physical two-sided path-root-sheet nerve: every length >=7 good path lies in an antipodally exchanged simplex component

Let n>=8 and let c be ANY active ordered-three-face NORI coloring. Let E be the genuine two-sided coordinate-box HELLY FLAG NERVE of ALL admitted ACTUAL directed cube geodesic path states of length k>=3 whose ordered-three-face window colors change at most once, as precisely constructed in
nori_two_sided_root_sheet_helly_equivariant_exact_grand_fixedpoint_index_four_ceiling_20261008.
Each vertex P has root x(P), used support W(P), length k=|W(P)|, and root-sheet free set M(P) of size max(6-k,0). Its box is B(P)=S(P)×S(ΘP). The exact pairwise test (nori_two_sided_box_exact_root_support_edge_test_high_index_packet_graph_selection_20261008) states
  B(P)∩B(Q) nonempty
iff
  supp(x(P) XOR x(Q)) union (W(P)△W(Q)) subset M(P) union M(Q).

**THEOREM (sharp high-rank disconnection, unconditional).** For every actual admitted path P of length k>=7 and every other admitted path Q, the boxes intersect EXACTLY when
  x(Q)=x(P) AND W(Q)=W(P).
This forces |W(Q)|=k automatically. In particular, the connected component of the HELLY nerve E containing P is precisely the FULL SIMPLEX on all actual <=1-switch path permutations with the fixed SAME pair of geometric data (root x,used direction support W). No simplicial edges connect this component to any path of different root, used support, or length. There are no mixed higher-dimensional simplices either, since E is flag.

**PROOF.** As k>=7, M(P)=empty. If Q has length ell>=6, then M(Q)=empty, so the exact edge criterion reduces to simultaneous equalities x(Q)=x(P), W(Q)=W(P). If Q has length 3<=ell<=5, then |M(Q)|=6-ell, but the symmetric difference of used sets satisfies
  |W(P)△W(Q)| >= |W(P)|-|W(Q)| = k-ell >=7-ell >6-ell=|M(Q)|.
So the edge criterion cannot hold. Conversely if roots and used sets agree then k=ell>=7 and their boxes are the SAME physical POINT (x,x XOR([n]\W)), so they intersect; every collection of such vertices is a simplex. QED.

**ANTIPODAL SPLITTING UNDER HYPOTHETICAL GRAND FAILURE.** Suppose there is NO full n-edge <=1-switch antipodal NORI geodesic. Then every admitted k>=7 path has k<n, so its unused set D=[n]\W is NONEMPTY. The physical reversal Θ sends its pair (x,W) to (x XOR D,W); the two root positions are distinct. Hence Θ exchanges the entire high-rank simplex component C_(x,W) with a DISJOINT high-rank simplex component C_(x XOR D,W). On each two-component union C_(x,W) ⊔ C_(x XOR D,W), the double cover is trivial and its cohomological antipodal index is ZERO.

Consequently under grand failure the full E decomposes equivariantly as
  E = E_<=6  disjoint_union  (disjoint pairs of high-rank simplex components),
where E_<=6 is the full subcomplex on actual admissible paths of lengths 3,4,5,6. The >=7 components contribute no positive powers of the antipodal class, so for each j>=1
  w1(E/Θ)^j !=0 iff w1(E_<=6/Θ)^j !=0.
In particular ind_Z2(E)=ind_Z2(E_<=6) (the short complex is nonempty and has index at least3 from the universal one-window paths). The known universal index-four upper bound arises ENTIRELY from these short length 3..6 root-sheet cells. An arbitrary abundance of longer genuine monochromatic or one-switch partial paths CANNOT raise this static complex's index by even one.

**GENERAL ORDERED-r WINDOW MODEL.** The exact same argument holds for ordered-r-face windows, where the common root-sheet free set has size M_r(k)=max(2r-k,0). Every admitted path of length k>=2r+1 has M_r(k)=empty. An edge to a shorter path of length ell<2r would require |W(P)△W(Q)|>=k-ell>2r-ell=|M_r(Q)|, impossible. An edge to ell>=2r forces identical root and used support. Thus all admissible paths longer than 2r are isolated within their (root,used-support) simplex components in the honest two-sided static Helly nerve. Under nonclosure they pair freely under physical antipodal reversal and have index0.

**CLOSURE CONSEQUENCE / EXACT LIMITATION.** The high-index permutohedral Tucker carrier cannot obtain an equivariant compatible repair lift into E by simply choosing LONG (k>=7) certified partial paths at each actual full-path order vertex, even if those paths have near-spanning length. Under hypothetical nonclosure, a connected Θ-invariant Tucker carrier must hit multiple high-rank root/support simplex components, but E offers NO EDGE between them. A genuine topology-first proof must enrich the witness-space with certified ORDER/PREFIX EXCHANGES, root transport, or seam-repair cells; simply accumulating longer monochromatic paths inside the static two-sided physical-root sheets never builds the missing high index. This is a structural barrier of the carrier, not a counterexample to the unrestricted NORI grand conjecture.

## SHARP ELEVATION: path length SIX is already isolated
The earlier k>=7 theorem is valid but NOT sharp. The exact edge condition gives a stronger result: for ANY admitted ordered-three-face path P of length k>=6, B(P) intersects B(Q) iff x(P)=x(Q) and W(P)=W(Q). Proof: M(P)=empty. Intersection implies W(P) symmetric-difference W(Q) subset M(Q), and M(Q) subset W(Q), whence W(P) subset W(Q). Therefore Q cannot have length <=5. If Q has length >=6, then M(Q)=empty also, forcing equal roots and used sets. Conversely these equalities give identical singleton boxes.
Under hypothetical grand failure, every k>=6 root/support simplex is paired with a DISJOINT antipodal simplex, since its unused set D is nonempty and the antipodal reversal sends root x to x XOR D. Hence E is the disjoint union of E_(3,4,5) and antipodally swapped high-rank simplex pairs, and ind(E)=ind(E_(3,4,5)). Thus NO physical static good path of length SIX OR GREATER supplies additional positive-degree antipodal topology. For ordered-r-face windows, the same sharp isolation holds for lengths k>=2r, since M_r(k)=max(2r-k,0) and M_r(Q) lies inside W(Q). The nontrivial static nerve comes entirely from lengths r through 2r-1.
