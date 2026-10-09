# Valid parity NORI coloring forbids any equivariant Helly graph selection restricted to packet subpaths

# A VALID NORI COLORING DISPROVES EVERY UNIVERSAL PACKET-SUBPATH EQUIVARIANT GRAPH SELECTION IN EVEN DIMENSION

Let n>=8 be EVEN and fix a distinguished cube root rho. Use the fully VALID active NORI physical ordered-three-face parity coloring from proved item nori_even_parity_bad_root_maximal_permutohedral_index_linear_radius_no_go_20261008:
  c(F,(i,j,k)) = sum_(t outside{i,j,k}) (z_t(F) XOR rho_t)  (mod2).
Since n−3 is odd, physical antipodal complementation reverses this bit, so the active NORI antipodal-reversal law holds. For EVERY direction permutation pi, the full actual rho-rooted n-edge geodesic has consecutive window word
  0,1,0,1,...,1
of length L=n−2. All n−3 color changes occur.

Let K_rho be the honest endpoint-opposed FULL-PERMUTOHEDRAL FACE NERVE at root rho, with one vertex for each full direction order pi and simplices consisting of orders lying in one common proper permutohedron face. Here EVERY full direction order is endpoint-opposed, so K_rho is the full face-nerve of the standard (n−1)-permutohedron boundary and
  ind_Z2(K_rho)=n−2 >=6.
The involution is full order reversal pi->rev pi, rooted at the SAME rho.

**THEOREM (UNCONDITIONAL NO-GO FOR SUBPATH-CONFINED GRAPH SELECTION).** There is NO assignment pi↦P(pi) satisfying ALL of:
 (i) P(pi) is a GENUINE contiguous directed SUBPATH of the actual rho-rooted full geodesic with direction word pi and length at least3;
 (ii) P(pi)'s ordered-three-face window word has <=1 change;
 (iii) P(rev pi)=Theta(P(pi)) is exact physical antipodal reversal;
 (iv) along EVERY abstract edge pi--sigma of K_rho, the selected genuine two-sided physical root sheets B(P(pi)),B(P(sigma)) intersect (equivalently the exact root/support/middle-set compatibility criterion holds).

**Proof.** Along the parity full path the color word strictly alternates, hence any contiguous k-edge subpath has exactly k−3 changes. Condition(ii) forces k<=4. Therefore every selected P(pi) is a length-THREE or length-FOUR actual one-switch path. Let E_{<=4} be the genuine two-sided root-box HELLY flag nerve formed by ALL actual admitted paths of lengths3 and4, over every physical cube root (not just rho). This is free under Theta: no length<=4 path is full when n>=8, and any two-sided box B(P) is disjoint from its Theta-swap (unused directions give mutually opposite fixed bits). The proved static-box index ceiling theorem nori_two_sided_root_sheet_helly_equivariant_exact_grand_fixedpoint_index_four_ceiling_20261008 gives
  ind_Z2(E_{<=4})<=4;
and the team's refined static-index theorem nori_exact_static_two_sided_helly_antipodal_index_three_all_no_grand_colorings_20261008 in fact computes index3 for these universal length3/4 boxes.

Because E_{<=4} is FLAG, condition(iv) extends the assignment of K_rho vertices to a SIMPLICIAL map K_rho→E_{<=4}, automatically compatible across EVERY higher-dimensional simplex. Condition(iii) makes that map equivariant. Naturality of the antipodal-cover Stiefel–Whitney class would imply
  ind_Z2(K_rho)<=ind_Z2(E_{<=4})<=4,
contradicting n−2>=6. QED.

**Crucial distinction from the earlier EXACT graph-selection reformulation.** The previous criterion nori_two_sided_box_exact_root_support_edge_test_high_index_packet_graph_selection_20261008 allows assignment of ANY genuine admissible partial-path witness from ANY physical root. Its converse may simply assign a known FULL grand witness from some other root to every source-vertex pair; hence that earlier equivalence remains true. The NEW theorem rules out the MUCH STRONGER and seemingly natural intermediate lemma that the assigned witness can always be taken INSIDE each endpoint-balanced source geodesic (or obtained merely by shortening it). This intermediate lemma is FALSE in a genuine active coloring which itself does satisfy the global grand conjecture from OTHER roots.

**Physical meaning.** The permutohedral high index at a BAD root cannot be continuously transported into the short-witness HELLY root-sheet carrier through subpaths of those bad full paths, even with arbitrary window choice at each permutation vertex. Thus a successful global topological proof MUST allow a selection to JUMP TO OTHER physical roots and/or produce NEW physical direction orders not confined to the original packet geodesic. The first five-direction central-window crossing obstruction of item nori_odd_n_central_three_window_selection_safe_permutohedron_faces_five_block_first_obstruction_20261008 is the minimal geometric obstruction for a fixed canonical window selection, but freely changing the window within each path STILL does not solve global equivariant gluing: this parity no-go excludes all such subpath-only choices at once.

This is a fully proved obstruction, not a counterexample to grand NORI; the coloring has abundant full good geodesics rooted elsewhere by the common exterior-parity three-chain theorem.
