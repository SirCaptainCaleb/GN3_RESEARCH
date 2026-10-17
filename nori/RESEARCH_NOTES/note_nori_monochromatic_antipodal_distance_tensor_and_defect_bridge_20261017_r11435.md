# Quantitative path stretch, one-detour conversion, and a universal root-rotation defect bound

- Stable ID: note_nori_monochromatic_antipodal_distance_tensor_and_defect_bridge_20261017_r11435
- Author: Independent NORI1 mathematician
- Primary home: subsection:full_geodesic_color_profiles_span_the_entire_binary_space
- Labels: NORI1, monochromatic-antipodal-distance, tensor-product, turn-to-defect, unrestricted-quantitative-bound, independent-verification
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11435_1
- Updated session: session_nori_r11435_1
- Disposition: none
- Successor: none

## Related references

- note:note_article_xi_one_detour_monochromatic_path_20261012
- note:note_143f396e6155ca89c587d00f
- note:note_f444f30e8dd9ece68d4b5734

## Research note

Let c be a legal antipodally odd two-coloring of Q_n, n>=2. By Wu–Yang (2026, arXiv:2607.19276), the red spanning subgraph G_0(c) has some antipodal pair at finite distance. Define L(c)=min_x dist_(G_0(c))(x,bar x) and E(c)=(L(c)-n)/2. Antipodal conjugation swaps red and blue and preserves graph distances, so the blue and red minima agree.

THEOREM A (monochromatic antipodal distance tensor law). For any legal colorings c,d in a and b dimensions, L(c box d)=L(c)+L(d) and E(c box d)=E(c)+E(d). Proof: project any red antipodal walk in the product onto each factor, obtaining red antipodal walks with total length equal to the original. This proves the lower bound. Concatenating shortest red antipodal paths in the factors produces a red antipodal product path realizing the sum. Parity gives integer E.

THEOREM B (one-direction padding). Extend c by one new direction t with c_t(x)=x_0, old rules ignoring t. The extension is legal and its shortest red antipodal distance is L(c)+1. Projection gives the lower bound. To realize it, take a shortest red antipodal path in c starting at x; place the new t-step before the old path when x_0=0, and after it when x_0=1. It is red in either case. Hence E(c^+)=E(c).

COROLLARY (linear excess amplification). If a bad coloring exists in dimension d, then for every N>=d there is a legal N-dimensional coloring with E>=floor(N/d). Tensor floor(N/d) copies and pad to N, using the two theorems. Therefore a universal bound max_c E(c)=o(n) would prove unrestricted NORI1. This is a quantitative strengthening target of the known monochromatic-path theorem, NOT a proved sublinear estimate.

THEOREM C (one-detour path-to-defect inequality). For ANY red-blue edge coloring, a red antipodal path of length n+2 entails a full antipodal geodesic with at most floor((n-1)/3) blue edges. Indeed the path direction word is D i A i B i C, with disjoint D,A,B,C partitioning all other directions. Set d=|D|,a=|A|,b=|B|,h=|C|. Three red-preserving replacement geodesics are: from its root x, D i A B C (only B-edge colors unknown), from x, D A B i C (only A unknown), and from x+e_i, D A i B C (only D,C unknown). Hence global minimum minority defect delta(c)<=min(a,b,d+h)<=floor((n-1)/3). If a repeated i-step is immediately undone, remove its two-step backtrack and obtain a red full geodesic. No antipodal oddness is required for this inequality.

AUDIT. Standard-library /mnt/data/nori_path_detour_defect_bridge_verify.py generated 6000 candidate words in each dimension n=5,...,11, found 38232 compatible legal red-path completions, and checked all three full geodesic blue counts. The proof is uniform. Full manuscript /mnt/data/nori_shortest_monochromatic_stretch_defect_bridge.md.

ARCHIVE POSITION. note_article_xi_one_detour_monochromatic_path_20261012 already constructs these three paths and proves color-switch bounds. The new explicit minority-edge estimate extracts their relevance for the global defect program. note_f444f30e8dd9ece68d4b5734 previously proves a more general rootwise padding law; Theorem B is included for a self-contained tensor argument. The metric tensor law addresses shortest monochromatic antipodal PATHS, unlike the earlier full-GEODESIC defect tensor law in note_143f396e6155ca89c587d00f. The remaining obstruction is quantitative: Theorem C gives only a linear deficit bound, and no unrestricted sublinear E estimate has been proved.

THEOREM D (unrestricted turn-to-defect bound). If a legal antipodally odd coloring of Q_n admits a full geodesic with at most s temporal color changes, then its global minority-edge defect satisfies delta(c)<=(n-ceil(n/(s+1)))/2. Proof: take the longest constant-color run of the geodesic's temporal word, of length L>=ceil(n/(s+1)). For each 0<=j<=n, cyclically rotate the first j steps to the end, starting at the vertex after those j steps. The j moved edges are replaced by their antipodal mates, so their colors flip. With signed colors a_k=+1 for red and -1 for blue, the signed excess of the j-rotated path equals F_j=sum_(k>j)a_k-sum_(k<=j)a_k. Across a run of L identical signs, F_j changes by magnitude 2L; at least one boundary value has absolute magnitude >=L, so that path has at most (n-L)/2 minority edges.

Hollom (arXiv:2605.20184, May 2026) proves that EVERY two-coloring of the edges of Q_n admits a full antipodal geodesic with at most (pi/2+o(1))*sqrt(n) color changes. Applying the preceding turn-to-defect bound to arbitrary LEGAL colorings proves the unrestricted inequality

max_(c legal) delta(c) <= n/2 - (1/pi+o(1))*sqrt(n).

This is a nontrivial dimension-uniform gain from an established quantitative path-selection theorem, but remains linear in n and does not settle NORI1. An isolated two-switch word 0^m 1^m 0^m still has minority m out of 3m, so a single short-switch profile cannot yield sublinear minority defect without inter-order compatibility. Full proof appended to /mnt/data/nori_shortest_monochromatic_stretch_defect_bridge.md.
