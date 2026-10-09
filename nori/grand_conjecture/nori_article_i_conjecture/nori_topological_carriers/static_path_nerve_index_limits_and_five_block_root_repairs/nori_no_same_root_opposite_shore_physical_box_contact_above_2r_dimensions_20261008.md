# In n>2r, opposite-shore actual path boxes at one root cannot meet unless both paths are full

# PHYSICAL ROOT MOBILITY IS MATHEMATICALLY NECESSARY: NO SAME-ROOT OPPOSITE-SHORE BOX CONTACT ABOVE DIMENSION SIX

Retain the genuine two-sided physical root-box carrier of
nori_two_sided_root_sheet_helly_equivariant_exact_grand_fixedpoint_index_four_ceiling_20261008,
and the exact pairwise box edge test of
nori_two_sided_box_exact_root_support_edge_test_high_index_packet_graph_selection_20261008.

Let r>=2, n>2r, and let P,Q be ACTUAL admitted <=1-switch directed geodesic PATH STATES for a binary physical ordered-r-face coloring, with SAME starting root x∈Q_n. Their lengths k_P,k_Q are at least r and at most n; their used sets W_P,W_Q, unused D_P,D_Q, and common r-window free-coordinate sets M_P,M_Q are as usual, with
  |D_P|=n−k_P, |M_P|=max(2r−k_P,0)
and likewise Q. Physical antipodal complement+path reversal maps P to ΘP whose new root is x XOR D_P, and whose exact root sheet has the same middle free-coordinate set M_P.

**THEOREM 1 (EXACT cross-shore same-root criterion).** The two boxes B(P) and B(ΘQ) have a common actual source-target root pair if and ONLY if
  D_Q ⊆ M_P
AND
  D_P ⊆ M_Q.
This is an exact physical-face criterion, independent of ordered face colors once P,Q have been admitted.

PROOF. The source factor of B(P) is S(P)=x+span M_P, and that of B(ΘQ) is S(ΘQ)=(x XOR D_Q)+span M_Q. Their intersection is nonempty precisely when D_Q⊆M_P∪M_Q; since unused D_Q is disjoint from its own used M_Q, this means D_Q⊆M_P. The target factor of B(P) is S(ΘP)=(x XOR D_P)+span M_P and that of B(ΘQ) is S(Q)=x+span M_Q. Their intersection is nonempty precisely when D_P⊆M_P∪M_Q; since D_P∩M_P=empty, this is equivalent to D_P⊆M_Q. Both factors must intersect, proving the equivalence. QED.

**THEOREM 2 (NO SAME-ROOT MIXED CONTACT IN n>2r EXCEPT FULL GRAND WITNESSES).** If n>2r and B(P)∩B(ΘQ) is nonempty, then BOTH P and Q must be FULL n-edge geodesics. Consequently, under hypothetical GRAND FAILURE, there is NO opposite-shore mixed box edge of this form at any common physical root.

PROOF. If P is full then D_P=empty, and because n>2r its middle common set M_P=empty. Theorem1 forces D_Q=empty, so Q is full also. Similarly with P,Q exchanged.

Now suppose both P,Q are incomplete. By Theorem1,
  n−k_P=|D_P| <= |M_Q|<=max(2r−k_Q,0),
  n−k_Q=|D_Q| <= |M_P|<=max(2r−k_P,0).
Since both left sides are POSITIVE, both right sides are positive, so k_P,k_Q<2r and the maxima can be dropped. Adding gives
  (n−k_P)+(n−k_Q) <= (2r−k_Q)+(2r−k_P),
i.e. n<=2r, contradicting n>2r. QED.

**NORI SPECIALIZATION (r=3).** In EVERY dimension n>=7, suppose P,Q are genuine <=1-switch partial geodesics from the SAME physical cube root x. Then their two-sided product boxes B(P),B(ΘQ) CAN meet only if P,Q are ALREADY full good antipodal geodesics. In particular, among the universal single-window monochromatic THREE-EDGE paths at one root, the full 'positive' clique and its reflected negative clique have NO cross edge in the two-sided Helly nerve. Merely taking all local path branches from ONE physical root and their Θ-images can never provide the mixed-face topology required for grand closure in n>=7.

**CROSS-ROOT TRANSPORT IS REQUIRED.** If P is rooted at x and Q at y (possibly distinct), the exact general cross-shore box compatibility test is
   supp(x XOR y XOR D_Q) ⊆ M_P∪M_Q,
   supp(x XOR y XOR D_P) ⊆ M_P∪M_Q.
Equivalently the ROOT DISPLACEMENT mask x XOR y must agree with BOTH unused support masks D_P and D_Q OUTSIDE the tiny union M_P∪M_Q. In particular, if k_P,k_Q>=6 for ordered three-face NORI, then both middle common sets are empty, so compatibility requires
  x XOR y = D_P = D_Q.
This is a genuinely large, support-dependent PHYSICAL root shift, not a local root slide.

**TOPOLOGICAL INTERPRETATION.** The high-index global program cannot be carried by sign-complementing LOCAL witnesses at one fixed root. Equivariant mixed-carrier faces beyond the universal low-rank skeleton necessarily use different physical roots with exterior differences synchronized to the UNUSED direction masks. This is an exact local-to-global obstruction in the honest double Helly nerve, and explains why a high-dimensional Tucker proof must incorporate root transport/path order exchanges INSIDE its topological framework. It does NOT prove that such transport always exists and does not close the unrestricted NORI grand conjecture.
