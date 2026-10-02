# Research frontier

Repository revision: 6004
Frontier objects: 398

Active theorem-facing terminal research objects that are visible for work: nonhidden, nonfailed, nonblocked, non-superseded leaves of the grand-theorem reasoning tree.

Flat frontier only. After choosing an item, call ancestry() or simplified_ancestry() separately for route context.

## [fourfold_boolean_lift_preserves_even_spanning_additive_paths] If an odd-order Boolean quotient has an even-length spanning additive path, then its full two-bit lift has a spanning path of length four times as large plus three.
focus · lemma · proved · certified · supported
Parent: [carrier_lift_multiplies_longest_additive_paths_by_four_up_to_o1]
**Given:** ["spanning additive path of even length","full 2-dimensional binary lift"]
**Consumer:** ["carrier recursion","longest-path lift bound"]
**Consequence:** Correct four-copy lift: even base path length gives a Hamiltonian two-bit lift; odd base lengths require truncation or additional hypotheses.

## [universal_fourfold_boolean_path_lift_fails_on_the_3point_line] The claimed universal fourfold Boolean path lift is false: the 3-point quotient lifts to PG(3,2), which has no spanning P_7.
focus · theorem · proved · certified · supported
Parent: [case_reduces_to_a_twobit_carrier_after_at_most_five_deletions]
**Consumer:** ["carrier recursion","induced Boolean route"]
**Consequence:** Universal two-bit Hamiltonicity is unavailable; retain the exact additive reductions but re-prove any lift step with correct hypotheses.
**Contradicts:** ["fourfold_boolean_lift_preserves_odd_spanning_additive_paths","localization_of_obstructions_in_exact_binary_carrier_towers","carrier_lift_multiplies_longest_additive_paths_by_four_up_to_o1"]

## [paths_close_the_critical_inducedboolean_construction_route] Among critical induced Boolean Schur systems, strict improvement over the generic density bound occurs only at lengths 3 and 7: all larger projective and two-point-deleted projective candidates are Hamiltonian.
focus · theorem · proved · certified · supported
Parent: [classification_for_induced_boolean_schur_triple_systems]
**Given:** ["near-Steiner classification fb1725da2cc8","set-sequential path theorem for dimension >=5"]
**Consumer:** ["lower-bound strategy","additive construction route","prize classification"]
**Consequence:** Closes the entire critical-size induced x+y construction family: only ell=3 and ell=7 yield strict improvements.

## [nonpath_additive_triple_is_balanced_over_patheven_bit_colorings] For a spanning path P in an additive triple system, the P-even F_2-colorings form a space of dimension r+1, and every additive triple outside P is odd in exactly half of those colorings.
focus · lemma · proved · certified · supported
Parent: [counterexample_contains_a_nonhamiltonian_exact_onebit_core]
**Given:** ["spanning additive quotient path"]
**Consumer:** ["one-bit carrier obstruction","compatible rail criterion 47949910006a"]
**Consequence:** Around any spanning quotient path, all nonpath edges split evenly between odd/even over the family of P-even bit colorings.
**Next Need:** Show that one dense odd half contains a spanning path sharing an endpoint with P, under density hypotheses inherited from a putative lower construction.

## [tworail_criterion_for_hamiltonicity_of_a_onebit_boolean_lift] A full one-bit Boolean lift is Hamiltonian whenever the quotient has two spanning half-length paths with a common endpoint satisfying the stated parity condition; linear independence of their incidence vectors suffices.
focus · lemma · proved · certified · supported
Parent: [counterexample_contains_a_nonhamiltonian_exact_onebit_core]
**Given:** ["two spanning quotient paths with common endpoint","one-bit full Boolean lift"]
**Consumer:** ["one-bit carrier obstruction","induced Boolean lower-bound route","signed carrier route"]
**Consequence:** Reduces one-bit Hamiltonicity to finding a compatible pair of spanning rails; incidence independence is a simple sufficient condition.
**Next Need:** Force such a rail pair in dense additive quotient systems, or characterize the even-subhypergraph obstruction.

## [ranknullity_forces_a_small_zerosum_block_in_the_joint_set] If a zero-sum joint set has size k and rank at most d with k≥d+2, then it contains a proper zero-sum subset of size between 3 and floor(k/2); in PG(3,2) this forces a split into two projective lines.
focus · lemma · proved · certified · supported
Parent: [normal_form_for_spanning_paths_in_boolean_schur_systems]
**Given:** ["joint XOR invariant","ambient binary rank"]
**Consumer:** ["P7 proof generalization","low-rank additive constructions"]
**Consequence:** Explains exactly why six joints in rank four split into two lines, while higher-dimensional projective systems do not inherit that conclusion.

## [crossed_missingcolor_chords_force_the_opposite_endpoint_chord] Crossed missing-color chords force the opposite endpoint chord.
focus · lemma · proved · certified · supported
Parent: [every_ordersix_latin_square_has_a_fullcolor_rainbow_path]
**Given:** ["crossed-chord normal form 8d4230198b1b","no rainbow P6"]
**Consumer:** ["order-six Latin-square humanization"]
**Consequence:** The crossed-chord case forces the used 3x3 color matrix to have rows x0=(1,6,3), x1=(2,3,6), x2=(*,4,5), with *=3 or 6 by properness.
**Next Need:** Exploit the forced 3x3 matrix and the three unused vertices on each side to eliminate *=3 and *=6.

## [every_properly_sixcolored_k66_has_a_rainbow_fiveedge_path] Every properly six-colored K6,6 has a rainbow five-edge path.
focus · lemma · proved · certified · supported
Parent: [every_ordersix_latin_square_has_a_fullcolor_rainbow_path]
**Given:** ["proper 6-edge-coloring of K6,6"]
**Consumer:** ["8d4230198b1b endpoint-chord normal form","3c00d375433a order-six humanization"]
**Consequence:** A hypothetical order-six counterexample necessarily contains a maximal rainbow P5, so the two endpoint-chord normal forms apply unconditionally.

## [normal_forms_for_an_ordersix_rainbowpath_counterexample] Two endpoint-chord normal forms for an order-six rainbow-path counterexample.
focus · lemma · proved · certified · supported
Parent: [every_ordersix_latin_square_has_a_fullcolor_rainbow_path]
**Given:** ["proper 6-coloring of K6,6","rainbow P5","no rainbow P6"]
**Consumer:** ["3c00d375433a order-six humanization"]
**Consequence:** Any order-six counterexample with a rainbow P5 has only two missing-color endpoint normal forms.
**Next Need:** Show every such coloring has a rainbow P5, then eliminate the rainbow-C6 and crossed-chord endpoint configurations by rotations through the unused 3+3 vertices.

## [ordersix_normal_form_forces_a_forbidden_rainbow_cycle] The crossed-chord order-six normal form forces a forbidden rainbow cycle.
focus · lemma · proved · certified · supported
Parent: [every_ordersix_latin_square_has_a_fullcolor_rainbow_path]
**Given:** ["crossed normal form b3cf269da794","rainbow-C6 exclusion f644f80c598e"]
**Consumer:** ["order-six Latin-square/transversal-design result"]
**Consequence:** Closes the final normal form; no enumeration of order-six Latin squares is needed.
**Next Need:** Compose the q=6 human theorem and retire 3c00d375433a computational evidence after preserving the human children.

## [the_rainbowsixcycle_branch_has_one_canonical_chord_matrix] The rainbow-six-cycle branch has one canonical chord matrix.
focus · lemma · proved · certified · supported
Parent: [every_ordersix_latin_square_has_a_fullcolor_rainbow_path]
**Given:** ["closing-chord case of 8d4230198b1b","maximal rainbow P5"]
**Consumer:** ["order-six Latin-square humanization"]
**Consequence:** The rainbow-C6 branch reduces to one canonical 3x3 partial Latin matrix rather than eight chord assignments.
**Next Need:** Use the three unused rows and columns to show the canonical matrix cannot extend to a proper 6-coloring without a rainbow P6.

## [the_rainbowsixcycle_normal_form_forces_a_color_collision] The rainbow-six-cycle normal form forces a color collision.
focus · lemma · proved · certified · supported
Parent: [every_ordersix_latin_square_has_a_fullcolor_rainbow_path]
**Given:** ["canonical closing-chord matrix 81565c9de9a6"]
**Consumer:** ["order-six Latin-square humanization"]
**Consequence:** Any q=6 counterexample must be in the crossed missing-color chord case; the entire rainbow-C6 branch is humanly eliminated.
**Next Need:** Eliminate the crossed-chord case, where b3cf269da794 forces the opposite endpoint chord and the final used entry is 3 or 6.

## [orderfour_transversal_design_has_a_maximumlength_linear_path] Every order-four transversal design has a maximum-length linear path.
focus · lemma · proved · certified · supported
Parent: [latin_transversal_and_blowup_construction_route]
**Given:** ["Latin-square representation of TD(3,4)","row/column/symbol relabeling invariance"]
**Consumer:** ["07a2a6d38eb9 finite evidence","Latin-square/transversal-design lower-bound route"]
**Consequence:** Replaces the order-4 portion of the computational enumeration by a complete human proof.
**Next Need:** Find an equally structural proof for order 5, preferably using isotopy classes or a general near-transversal/connector argument.

## [the_g0_fivecycle_contain_an_almostperfect_packing_of_full_laps] Arbitrary Latin lifts of the G0 five-cycle contain an almost-perfect packing of full laps.
focus · theorem · proved · certified · supported
Parent: [latin_transversal_and_blowup_construction_route]
**Consumer:** ["G0 Latin blow-up route","general leading-coefficient lower-bound construction search"]
**Consequence:** arbitrary Latin squares cannot prevent q-o(q) mutually resource-disjoint full laps; any successful blow-up must obstruct connectivity/chaining rather than packing
**Next Need:** analyze whether o(q) lap components can always be joined using the remaining G0 base edges, or engineer a product gadget whose leftover resource sets forbid such joining

## [transversal_design_has_a_spanning_sevenedge_linear_path] Every order-five transversal design has a spanning seven-edge linear path.
focus · lemma · proved · certified · supported
Parent: [latin_transversal_and_blowup_construction_route]
**Given:** ["Latin-square representation of TD(3,5)","isotopy and transposition preserve linear paths"]
**Consumer:** ["Latin-square/transversal-design lower-bound route","07a2a6d38eb9 finite enumeration"]
**Consequence:** Replaces the order-five exhaustive enumeration by a complete elementary classification and explicit spanning paths.
**Proof Structure:** ["intercalate case gives four normalized completions","intercalate-free case forces cyclic square","explicit P7 in every normalized case"]

## [prize_shelf_exceptional_lowerbound_constructions] Prize shelf: exceptional lower-bound constructions
focus · abstraction · proved · certified · supported
Parent: [general_lowerbound_construction_program]
**Consumer:** ["lower-bound strategy","paper drafting","novelty review"]
**Consequence:** Provides a durable curated entry for the exceptional P7 lower bound and its proof.

## [above_ell3_forces_the_path_weight_in_the_binary_incidence_code] Every finite linear 3-graph with edge density m/n>ℓ/3 has a binary incidence-code word of weight exactly ℓ+2.
focus · theorem · proved · certified · supported
Parent: [defeat_the_missingweight_certificate_in_two_residue_classes]
**Given:** ["binary incidence code of a linear 3-graph","density-core reduction","linearity of a vertex star"]
**Consumer:** ["incidence-code obstruction route","general lower-bound construction search"]
**Consequence:** closes the single-missing-weight incidence-code route for every residue class: density above ell/3 already forces weight ell+2
**Strengthens:** ["defeat_the_missingweight_certificate_in_two_residue_classes","missing_weights_cannot_certify_a_leading_lowerbound_improvement"]

## [proof_of_the_exact_sixblock_deletion_threshold_in_cyclic_sts13] Exactly six blocks must be deleted from the cyclic STS(13) to destroy all spanning P_6, and deleting the six blocks through one point attains this threshold.
focus · theorem · proved · certified · supported
Parent: [sts2ell1_spanningpath_obstruction_route]
**Given:** ["two cyclic 13-block translation orbits in STS(13)","one spanning P6 contained in each orbit"]
**Consumer:** ["STS(13) spanning-path obstruction route","lower-bound construction search"]
**Consequence:** Completely replaces the exhaustive P6 hitting-set computation by a two-orbit translation-incidence argument.
**Supersedes Evidence:** cyclic_sts13_requires_six_block_deletions_to_destroy_all_p6

## [proof_that_every_block_of_cyclic_sts13_is_special_of_rank_six] Every block of the cyclic STS(13) generated by {0,1,4} and {0,2,7} has longest-path rank six and is special.
focus · lemma · proved · certified · supported
Parent: [sts2ell1_spanningpath_obstruction_route]
**Given:** ["cyclic STS(13) generated by two difference-family base blocks","one explicit spanning P6 ending in each translation orbit"]
**Consumer:** ["c95ed9aba8d6 computational calibration","dense-core all-special conjecture"]
**Consequence:** Completely replaces the exact induced-path enumeration for STS(13) by two explicit spanning paths and affine automorphisms.
**Correction:** The first draft incorrectly claimed an affine automorphism swapped the two block orbits. The corrected proof treats one representative in each orbit and uses a separate vertex-cycling affine stabilizer for each.

## [that_the_cyclic_sts13_puncture_is_singleblock_extensiontight] Deleting one point from the cyclic STS(13) is single-block extension-tight: restoring any one of the six deleted incident blocks creates a spanning P_6.
focus · lemma · proved · certified · supported
Parent: [sts2ell1_spanningpath_obstruction_route]
**Given:** ["cyclic STS(13) block description","one-point puncture"]
**Consumer:** ["76f2ea3c3bec computational evidence","near-Steiner spanning-path obstruction route"]
**Consequence:** Replaces the finite-search status of single-star extension-tightness by six explicit human-checkable spanning paths.

## [every_special_globally_toprank_edge_is_alltop] Every special edge of globally maximum rank L has all three vertices of vertex rank L.
focus · lemma · proved · certified · supported
Parent: [nonspecial_edges_are_unique_longestpath_entrance_vertices]
**Given:** ["7235fdc47d1a special iff multiple longest-path entrance labels"]
**Consumer:** ["top-rank rotation output classification","top-potential induced core"]
**Consequence:** At global maximum rank, the special branch is an all-top branch rather than a separate geometric case.

## [weighted_incidencerank_inequality] If edge weights in a linear 3-graph have weighted vertex degrees at most D, then rank(N)≥3W/(D+2), hence W≤(D+2)n/3.
focus · lemma · proved · certified · supported
Parent: [exact_cliquecover_reformulation_of_linear_triple_systems]
**Given:** linear 3-graph and a fractional edge weighting with bounded weighted vertex degrees
**Consumer:** general P_ell upper-bound rank route
**Next Obligation:** find P_ell-free weightings with W>=rho m-O(n) and D<=c ell+O(1); then m <= (c/(3rho)) ell n+O(n)
**Target Scale:** c=rho would yield leading coefficient 1/3

## [maximumdegree_range_of_the_incidencerank_path_inequality] If a linear 3-graph has maximum degree Delta and L>=Delta+2, then L rank_R(N)>=3m; hence any counterexample at path length ell must have Delta>=ell-1.
focus · lemma · proved · certified · supported
Parent: [intersectiongraph_and_incidencerank_route]
**Given:** ["weighted incidence-rank inequality f943915ca731","maximum degree Delta"]
**Consumer:** ["incidence-rank path conjecture","sharp one-third upper-bound route"]
**Consequence:** The sharp rank inequality is automatic whenever Delta<=ell-2; only the high-maximum-degree regime Delta>=ell-1 remains.
**Next Need:** Exploit the star around a vertex of degree at least ell-1 together with P_ell-freeness to extend the rank inequality into the high-degree regime.

## [nullity_control_already_improves_the_leading_coefficient] Any uniform bound nullity(N)≤Cs+Dn with fixed C>0 yields a P_ℓ-free edge bound whose leading coefficient is 2C/(2C+1)<1.
focus · lemma · proved · certified · supported
Parent: [specialedge_nullity_conjecture]
**Given:** ["2m+s<=(2ell-3)n","rank(N)<=n"]
**Need:** it suffices to prove nullity(N)<=Cs+Dn for any absolute C>0,D>=0
**Consumer:** leading-coefficient improvement

## [post4348_proof_rehearsal_paid_strictgap_local_congestion] Post-43/48 proof rehearsal: paid strict-gap local congestion
focus · proof_level · proposal · not_required · unchecked
Parent: [generallength_attack_specialedge_density_and_incidence_rank]
**Given:** ["a57007500001 exact 43/48 rank-sensitive theorem with additive n_+ gap","9fba15f1495c certified strict-two-terminal-gap paid family","7e6abf77cbc5 certified sublinear-congestion reduction"]
**Consumer:** ["post-43/48 leading-coefficient improvement","paid strict-gap local packing route"]
**Consequence:** The proof rehearsal now reaches the narrow local congestion problem; the older generic paid-object congestion gap is no longer the first unsupported step.
**Next Need:** Prove g(p)=o(p), ideally O(log p), for minimum-terminal assignments in the source-clean doubly-terminal-single paid-certified strict-two-terminal-gap class.

## [ascendinglayer_degree_recurrence] Ascending-edge layers satisfy 2(delta-2k+1)(n_k-n_{k+1}) <= (2k+1)n_{k+1} whenever delta>2k-1.
focus · lemma · proved · certified · supported
Parent: [ascendingedge_rainbowlayer_formulation]
**Given:** ["ascending-edge rainbow-layer formulation","minimum degree in the original hypergraph"]
**Consumer:** dense-core all-special and rank-layer expansion routes
**Consequence:** low endpoint-rank vertices in a dense core force quantitative growth into the next path-rank layer
**Recurrence:** 2(delta-2k+1)(n_k-n_{k+1}) <= (2k+1)n_{k+1}

## [control_suffices_for_the_23_leading_coefficient] Sublinear common-last-vertex control suffices for the 2/3 leading coefficient.
focus · lemma · proved · certified · supported
Parent: [ascendingedge_rainbowlayer_formulation]
**Given:** ["ascending-edge accounting","a pointwise common-last-vertex bound"]
**Consumer:** general leading-coefficient improvement
**Consequence:** it is enough to prove any sublinear a(v)=o(phi(v)); logarithmic control is much stronger than necessary
**Fallback Target:** a(v)=O(sqrt(phi(v))) already yields (2ell/3+O(sqrt(ell)))n

## [directed_graph_of_ascending_edges_and_a_levelcut_inequality] Directed graph of ascending edges and a level-cut inequality.
focus · lemma · proved · certified · supported
Parent: [ascendingedge_rainbowlayer_formulation]
**Consumer:** cross-level control of ascending edges
**Limitation:** gives expansion of low-φ vertex sets but not by itself a sharp edge bound

## [characterization_of_ascending_and_nonascending_edges] Maximum-path characterization of ascending and nonascending edges.
focus · lemma · proved · certified · supported
Parent: [entrancevalue_distortion_with_consecutivecontact_correction]
**Consumer:** repeated-blocker uncrossing and location-sensitive Minty arguments
**Consequence:** nonascending behavior is equivalent to a two-vertex transversal of the family of longest paths ending at the entrance; strong decrease forces both vertices onto every such path

## [joint_snakeincidence_and_blocker_budget] Joint snake-incidence and blocker budget.
focus · lemma · proved · certified · supported
Parent: [entrancevalue_distortion_with_consecutivecontact_correction]
**Consumer:** dense-core all-special conjecture and transfer-potential arguments
**Consequence:** large downward changes in φ(f) consume extra units of the same finite witness set

## [cyclictransient_decomposition_for_the_transfer_digraph] Cyclic-transient decomposition for the transfer digraph
focus · proof_level · proposal · not_required · unchecked
Parent: [mintytype_potential_on_the_transfer_digraph_of_nonspecial_edges]
**Need:** ["cyclic estimate A_cyclic<=H_2+O(n)","transient estimate A_transient=O(n)"]
**Consumer:** dense-core all-special conjecture and 2/3 leading coefficient

## [deficit_doubling_implies_logarithmic_commonlastvertex_degree] If the five-edge deficit-doubling inequality holds, then k such edges sharing a last vertex with maximum rank p satisfy k≤3 floor(log2 p)+4.
focus · lemma · proved · certified · provisional
Parent: [fiveedge_deficitdoubling_conjecture]
**Given:** five-edge deficit-doubling conjecture
**Consumer:** logarithmic common-last-vertex conjecture
**Consequence:** a five-edge local inequality is sufficient for the desired O(log φ(v)) bound

## [of_oneprivatecontact_fifth_edges_around_the_11111717_gadget] In the 11,11,17,17 base configuration, no fifth edge with one private precursor contact b_j and one new vertex can keep all five common-terminal edges ascending and nonspecial.
focus · lemma · proved · certified · supported
Parent: [four_commonlast_ascending_edges_can_have_values_11111717]
**Given:** ["e56c6d0fce1a 11,11,17,17 configuration","one private precursor contact b_j and one new vertex"]
**Consumer:** ["bce2e76b5733 computational extension search","five-edge deficit-doubling route"]
**Consequence:** Humanizes the entire one-private-contact subfamily of the 368 candidate fifth edges and identifies four explicit failure mechanisms.
**Next Need:** Handle candidates whose old precursor contact is a joint a_j, or which use two old precursor vertices.

## [to_the_368extension_search_around_the_11111717_gadget] The 11,11,17,17 gadget admits a legal fifth common-terminal ascending nonspecial edge, producing ordered ranks (11,11,14,17,17) and refuting the earlier finite-search exclusion.
focus · lemma · proved · certified · supported
Parent: [four_commonlast_ascending_edges_can_have_values_11111717]
**Given:** ["e56c6d0fce1a base configuration"]
**Consumer:** ["five-edge deficit-doubling route","humanization campaign"]
**Role:** human counterexample to computational evidence
**Consequence:** Shows the 368-extension computation/search statement missed the legal fifth edge G={v,a_13,c_4}; five common-last ascending edges do occur in this extension class.
**Fence:** Does not refute 6cca826aad42; the resulting ranks (11,11,14,17,17) satisfy the deficit-doubling inequality.
**Refutes:** oneedge_extension_search_around_the_11111717_configuration

## [fouredge_spacing_implies_logarithmic_commonlastvertex_degree] If four-edge spacing holds, then k ascending nonspecial edges sharing a last vertex with maximum rank p satisfy k≤3+ceil(log2(p+1)).
focus · lemma · proved · certified · provisional
Parent: [fouredge_spacing_conjecture_at_a_common_last_vertex]
**Given:** four-edge spacing inequality
**Consumer:** logarithmic common-last-vertex conjecture

## [slackcorrected_spacing_for_clean_entrance_contacts] For the stated clean entrance contacts e1,e2,e4 on a common precursor, with s_i=(q_i-1)-j_i and j1+2≤j2, one has 2q2≥q1+q4+3+s2-s1.
focus · lemma · proved · certified · supported
Parent: [fouredge_spacing_conjecture_at_a_common_last_vertex]
**Given:** ["three ascending edges sharing a last vertex","single entrance contacts on the largest edge's precursor"]
**Consumer:** ["four-edge spacing conjecture","logarithmic common-last-vertex bound"]
**Consequence:** the desired four-edge spacing follows in this case whenever s_1<=s_2+2
**Next Obligation:** control large downward jumps of entrance slack, or convert such slack into additional blocker/rotation structure

## [twocontact_counterexample_to_fouredge_spacing] A linear 3-graph exists with four ascending nonspecial edges through one last vertex of ranks 12,16,20,20, violating 2q2≥q1+q4+1.
focus · theorem · proved · certified · supported
Parent: [fouredge_spacing_conjecture_at_a_common_last_vertex]
**Consumer:** ["unrestricted four-edge spacing conjecture"]
**Role:** fence
**Main Route Relevance:** outside the admissible minimum-degree regime; only refutes the universal spacing statement, not a spacing lemma restricted to a smallest counterexample of the 2/3 target
**Minimum Degree:** 1

## [uncrossed_splice_gives_fouredge_spacing] If the natural splice from a longest e1-path into the reversed tail of a longest e4-path is linear, then 2q2≥q1+q4+2, strengthened to +3 when x2 is private to one e4-path edge.
focus · lemma · proved · certified · supported · obstructed
Parent: [fouredge_spacing_conjecture_at_a_common_last_vertex]
**Given:** ["ascending edges at a common last vertex","a longest path for the largest edge","a longest entrance path for the smallest edge"]
**Consumer:** four-edge spacing conjecture
**Consequence:** spacing holds with +2 in every uncrossed splice configuration
**Next Need:** show that with four ascending edges, the intermediate edge e_3 can uncross or charge every obstruction to this splice

## [family_forces_umass_early_triangles_or_early_superlevel_outputs] A linear selected local family forces U-mass, early triangles, or early superlevel outputs.
focus · lemma · proved · certified · dependency_hold
Parent: [large_local_switching_families_into_early_structural_payment]
**Given:** ["cfa68aa6d0c5 logarithmic-plus-prefix-excess bound","5a46bb34148e high-excess certificate conversion"]
**Consumer:** ["7e6abf77cbc5 local congestion route","post-43/48 paid strict-gap analysis"]
**Consequence:** A linear selected local obstruction has only three macroscopic forms: terminal-retained mass, early switcher-triangle mass, or early V_{>=p} output-edge mass.
**Next Need:** Attack the three currencies separately with the hypotheses still unused: source-cleanliness and opposite-terminal singleness. For U use reciprocal terminal-path transversality; for triangles use the two clean source rails and opposite-terminal paths; for superlevel outputs exploit nested potential-core reuse/maximum-rank forest structure.

## [terminal_values_of_an_ascending_edge_are_comparable] Terminal φ-values of an ascending edge are comparable.
focus · lemma · proved · certified · supported
Parent: [logarithmic_commonlastvertex_bound_for_ascending_edges]
**Consumer:** ["global ascending-edge structure","dyadic decomposition of the ascending terminal graph","four-edge spacing route"]
**Consequence:** an ascending terminal pair always joins vertices whose endpoint potentials differ by less than a factor two

## [of_an_ascending_edge_are_at_most_three_times_its_rank] Terminal potentials of an ascending edge are at most three times its rank.
focus · lemma · proved · certified · supported
Parent: [any_long_terminal_path_captures_a_lowerrank_ascending_edge]
**Given:** ["ascending nonspecial edge","long-terminal-path capture lemma"]
**Consumer:** ["potential-oriented local bound","multi-scale ascending-edge arguments"]
**Consequence:** each terminal endpoint potential is at most 3q-3 for an ascending edge of rank q; charged edges have rank at least one third of the charged terminal potential
**Fence:** does not assert q equals the terminal potential; 0e0b0a3c7b04 shows genuine rank drop

## [terminalpotential_rise_forces_a_narrower_upperhalf_rank_band] If e={x,v,u} is ascending nonspecial with edge rank q and φ(v)<φ(u), then q≥ceil((φ(v)+3)/2).
focus · lemma · proved · certified · supported
Parent: [of_an_ascending_edge_are_at_most_twice_its_rank_minus_two]
**Consumer:** ["strict potential-rise terminal-degree conjecture","central-window packing"]
**Consequence:** strict rises miss the bottom charged rank when p is even and always lie in the narrower band ceil((p+3)/2)<=q<=p
**Next Obligation:** combine this narrow band with central-window packing and maximum-path transversals to control strict-rise multiplicity

## [ascending_edge_can_have_rank_below_both_terminal_potentials] A potential-oriented charged ascending edge can have rank below both terminal potentials.
focus · lemma · proved · certified · supported
Parent: [potentialoriented_local_bound_for_ascending_terminal_edges]
**Consumer:** ["potential-oriented local bound","logarithmic oriented-degree route"]
**Role:** fence
**Calibration:** rank 3 versus terminal potentials 4,4
**Consequence:** charged ascending edges need not have full terminal rank; any proof must tolerate genuine rank drop even when both terminal potentials are equal

## [edges_at_potential_four_have_a_unique_universal_middle_entrance] Rank-three charged edges at potential four have a unique universal middle entrance.
focus · lemma · proved · certified · supported
Parent: [potentialoriented_local_bound_for_ascending_terminal_edges]
**Given:** ["0e550ff0eadd certified latest-contact localization","8b1790d79d74 half-path endpoint-potential lemma","charged transversality"]
**Consumer:** ["50b6278b9537 potential-oriented local bound","66cfc745df48 finite evidence"]
**Consequence:** Repairs the p=4 rank-3 uniqueness and universal-middle-joint conclusions without using the disputed central-window packing theorem.
**Next Need:** Rule out four charged edges in the remaining rank patterns (3,4,4,4) and (4,4,4,4) using the universal middle-joint entrance and rank-4 reciprocal blockers.
**Supersedes Working Dependency:** ["109414e163c7 rank-3-count step","four_a_rankthree_charged_edge_is_pinned_by_its_entrance","is_universal_across_maximum_paths_in_the_first_p4_obstruction"]

## [entrance_slots_force_opposite_terminals_into_the_first_edge] Middle entrance slots force opposite terminals into the first edge.
focus · lemma · proved · certified · supported
Parent: [potentialoriented_local_bound_for_ascending_terminal_edges]
**Given:** ["f9e64ea63be0 pure p=4 path setup"]
**Consumer:** ["potentialoriented_local_bound_for_ascending_terminal_edges","falsification_search_for_the_potentialoriented_local_bound"]
**Consequence:** The two middle entrance slots each consume a distinct private vertex of g1 as the opposite charged terminal.
**Next Need:** Use the forced g1 terminals together with the remaining entrance slots r12/private(g3) to eliminate the pure (4,4,4,4) pattern.

## [in_the_pure_p4_obstruction_are_pinned_to_the_first_joint] Absent entrances in the pure p=4 obstruction are pinned to the first joint.
focus · lemma · proved · certified · supported
Parent: [potentialoriented_local_bound_for_ascending_terminal_edges]
**Given:** ["four rank-four charged edges at phi(v)=4","central five-slot localization","two-contact competitor lemma"]
**Consumer:** ["potentialoriented_local_bound_for_ascending_terminal_edges","falsification_search_for_the_potentialoriented_local_bound"]
**Consequence:** On any longest path ending in one member of a pure p=4 obstruction, at least two of the other three unique entrances are visible; an absent entrance is uniquely paired with the first joint.
**Next Need:** Exploit the three or four visible potential-3 entrances in the five-slot window to force a wrong-entrance path or incompatible blocker locations.

## [lowpotential_case_of_the_potentialoriented_local_bound] Certified low-potential case of the potential-oriented local bound.
focus · lemma · proved · certified · supported
Parent: [potentialoriented_local_bound_for_ascending_terminal_edges]
**Given:** ["0e550ff0eadd certified cumulative terminal-incidence bound","charged edge rank at most phi(v)"]
**Consumer:** ["50b6278b9537 potential-oriented local bound","66cfc745df48 finite evidence"]
**Consequence:** Humanizes the entire endpoint-potential p<=3 regime using only certified machinery, independently of the disputed central-packing count.
**Fence:** Do not use 109414e163c7 as the trusted justification for p<=3 until its dependency on 6959dc2c0376 is resolved.

## [middlejoint_entrance_in_the_first_potentialfour_obstruction] In a (3,4,4,4) potential-four obstruction, the rank-three entrance is the same middle joint of every maximum v-path.
focus · theorem · proved · pending · unchecked · pending
Parent: [potentialoriented_local_bound_for_ascending_terminal_edges]
**Given:** ["central-window packing","path-relative witness localization","nonspecial unique-entrance property"]
**Consumer:** ["potential-oriented local bound","charged four-edge spacing route"]
**Consequence:** The first p=4 low-rank obstruction has one universal potential-two entrance serving as the middle joint of every maximum v-path.
**Next Need:** Compare two rank-four longest paths through the universal middle joint x and uncross them.

## [mixed_p4_obstruction_consists_of_commonendpoint_tworail_paths] The mixed p=4 obstruction consists of common-endpoint two-rail paths.
focus · lemma · proved · certified · supported
Parent: [potentialoriented_local_bound_for_ascending_terminal_edges]
**Given:** ["2dbfe112a0fe universal middle entrance","rank pattern (3,4,4,4)"]
**Consumer:** ["50b6278b9537 potential-oriented local bound","66cfc745df48 computational evidence"]
**Consequence:** A mixed p=4 counterexample consists of three rank-four longest paths with common physical endpoints u,v and common middle joint x; this converts the remaining case to a three-rail uncrossing problem.
**Next Need:** Compare two u-x two-edge prefixes and two x-v two-edge suffixes. Since phi(x)=2, any uncrossing that creates a three-edge x-ending path is forbidden; exploit the resulting forced cross-intersections for three rails.

## [to_a_doubleblocked_fork_or_a_fouredge_charged_configuration] Dense equal-potential obstruction reduces to a double-blocked fork or a four-edge charged configuration.
focus · lemma · proved · certified · supported
Parent: [component_forces_two_incident_minimumrank_bicircular_chords]
**Given:** ["dense equal-potential bicircular-chord reduction","terminal adjacency blocker lemma"]
**Consumer:** ["mad(T_=)<=3","charged four-edge spacing","potential-oriented local bound"]
**Consequence:** A density counterexample has only two local forms at a shared terminal: one basis edge simultaneously blocked by two excluded chords, or four charged ascending edges with two paired low-to-high rank inequalities.
**Next Need:** Eliminate the double-blocked fork by a two-blocker splice, or exploit the paired rank inequalities in the four-edge branch using charged spacing/reciprocal tails.

## [equalpotential_ascending_terminal_has_rainbow_fouredge_path] The equal-potential ascending terminal graph can contain a rainbow four-edge path, so equal-potential structure alone does not imply rainbow-P4-freeness.
focus · lemma · proved · certified · supported
Parent: [ascending_terminal_graph_has_maximum_average_degree_three]
**Consumer:** equal-potential ascending-terminal density route
**Role:** fence
**Lesson:** mad(T_=)<=3, if true, requires a density/blocker argument; it cannot follow from forbidding rainbow P4
**Refines:** ascending_terminal_graph_can_contain_a_rainbow_fouredge_path

## [potential_rise_can_occur_above_the_edge_rank_at_both_terminals] Strict potential rise can occur above the edge rank at both terminals.
focus · lemma · proved · certified · supported
Parent: [strict_potentialrise_terminal_degree_is_at_most_two]
**Consumer:** ["strict potential-rise degree conjecture","potential-oriented charging"]
**Warning:** strict-rise edges can have genuine rank drop at the lower terminal; do not assume φ(e)=min terminal potential
**Role:** fence
**Parameters:** edge rank 4, terminal potentials 5 and 6

## [potential_four_satisfies_the_potentialoriented_local_bound] Potential four satisfies the potential-oriented local bound.
focus · theorem · proved · certified · supported
Parent: [potentialoriented_local_bound_for_ascending_terminal_edges]
**Given:** ["07e1382b03d2 mixed-case exclusion","49c24605109f pure-case normal form","aa608665fcba pattern-A exclusion"]
**Consumer:** ["50b6278b9537 potential-oriented local bound","66cfc745df48 finite evidence"]
**Consequence:** Fully humanizes the endpoint-potential p=4 regime: the oriented charged terminal count is at most three.
**Next Need:** Extend the human proof from p<=4 to p>=5, or reduce the finite 2,250-system evidence to bounded-p regimes covered by the theorem.

## [an_endpoint_chord_raises_the_next_joints_vertex_rank] An endpoint chord raises the next joint's vertex rank.
focus · lemma · proved · certified · supported
Parent: [a_fiveedge_path_chord_excludes_the_potentialfive_pattern_4445]
**Consumer:** ["odd central rank window","path-relative ascending terminal bounds"]
**Consequence:** An endpoint chord raises the next joint's rank in the central odd case.

## [4445_triangle_are_universally_pinned_on_highterminal_fivepaths] In the p=5 charged 4445 setting, every five-edge path to a high terminal places the corresponding low joint in the middle two edges, and if the joint itself appears there it is exactly the r₃∩r₄ joint.
focus · lemma · proposal · not_required · unchecked
Parent: [p5_pattern_4445_contains_a_canonical_lowhigh_terminal_triangle]
**Given:** ["0b8e51bfe396 4445 triangle","b5ba2ebc7a66 terminal tail blocker","8b1790d79d74 position-sensitive path potential"]
**Consumer:** ["p=5 4445 elimination"]
**Consequence:** Five-paths to the high terminals are forced to meet the low triangle joints in a tiny central window.
**Next Need:** Complete the exact positional exclusion carefully; current proof draft only establishes b or v lies in r3∪r4, and additional splice justification is needed to pin b uniquely.

## [in_the_p5_4445_pattern_must_cross_the_far_end_of_the_fivepath] Canonical entrance paths in the p=5 4445 pattern must cross the far end of the five-path.
focus · lemma · proved · certified · supported
Parent: [both_high_terminals_are_forced_into_the_first_two_path_edges]
**Given:** ["7d676959b033 early high-terminal localization","canonical entrance path for ascending edge"]
**Consumer:** ["p=5 4445 elimination","two-path uncrossing"]
**Role:** p=5 4445 forced cross-contact
**Consequence:** Every maximum b-ending path avoiding u_b is forced to hit the far terminal pair e5∪g4; otherwise it splices to a six-edge path ending at the other low-potential joint c.
**Next Need:** Classify the forced R_b contact with e5∪g4. Since R_b avoids v, only the two non-v vertices of e5 and the three vertices of g4 are available, with d=e5∩g4 shared. Show contacts away from d create a 4-edge b- or c-ending path; reduce to R_b passing through d.

## [in_the_4445_triangle_satisfy_a_threeway_latecontact_alternative] In the 4445 triangle, every five-edge path to a high terminal satisfies a three-way late-contact alternative involving the common terminal, the low joint, or the third middle vertex.
focus · lemma · proposal · not_required · unchecked
Parent: [of_the_4445_triangle_is_suffixblocked_by_the_middle_edge]
**Given:** ["c2e8b77d6c94 suffix trap","8b1790d79d74 positional potential"]
**Consumer:** ["p=5 4445 elimination"]
**Consequence:** Late contacts on high-terminal five-paths are forced into v, the corresponding low entrance joint, or the third middle-edge vertex a.
**Next Need:** Eliminate/absorb the residual case c=r3∩r4 on a path to u_b (and symmetrically b on a path to u_c). Likely use the opposite charged edge f_c: since c is its entrance, appending/replacing f_c should yield a wrong-entrance rank-4 path or a four-edge path ending b.

## [potentialoriented_local_bound_implies_the_23_upper_bound] Potential-oriented local bound implies the 2/3 upper bound.
focus · lemma · proved · certified · provisional
Parent: [potentialoriented_local_bound_for_ascending_terminal_edges]
**Given:** potential-oriented local bound
**Consumer:** general 3-uniform upper bound
**Consequence:** exact leading coefficient 2/3 without a minimum-degree reduction

## [the_mixed_p4_charged_obstruction_is_impossible] The mixed p=4 charged obstruction is impossible.
focus · theorem · proved · certified · supported
Parent: [potentialoriented_local_bound_for_ascending_terminal_edges]
**Given:** ["2dbfe112a0fe universal middle entrance at p=4"]
**Consumer:** ["50b6278b9537 potential-oriented local bound","66cfc745df48 finite evidence"]
**Consequence:** Completely eliminates the mixed p=4 obstruction. Any four-edge counterexample at potential four would have to have ranks (4,4,4,4).
**Next Need:** Eliminate four rank-4 charged edges at a potential-four terminal.

## [the_sentrance_pattern_in_the_pure_p4_obstruction_is_impossible] The S-entrance pattern in the pure p=4 obstruction is impossible.
focus · lemma · proved · certified · supported
Parent: [potentialoriented_local_bound_for_ascending_terminal_edges]
**Given:** ["49c24605109f three-pattern normal form"]
**Consumer:** ["potentialoriented_local_bound_for_ascending_terminal_edges","falsification_search_for_the_potentialoriented_local_bound"]
**Consequence:** Eliminates the S-entrance branch. Any pure p=4 counterexample must have visible entrances T,U,V and either R visible (B) or one absent entrance with opposite terminal R (C).
**Next Need:** Eliminate patterns B and C.

## [threepattern_normal_form_for_the_pure_p4_obstruction] Three-pattern normal form for the pure p=4 obstruction.
focus · lemma · proved · certified · supported
Parent: [potentialoriented_local_bound_for_ascending_terminal_edges]
**Given:** ["f9e64ea63be0 absent-entrance pinning","0feaf8d8f358 middle-slot terminal forcing","five-slot witness localization"]
**Consumer:** ["potentialoriented_local_bound_for_ascending_terminal_edges","falsification_search_for_the_potentialoriented_local_bound"]
**Consequence:** The last p=4 obstruction has only three explicit central-slot patterns A/B/C; T is always an entrance and its opposite terminal is private in g1.
**Next Need:** Eliminate patterns A/B/C using canonical three-edge entrance paths and equal-rank splice blocking.

## [k33_copies_refute_the_ascendingincidence_rank_bound] Three-colored K3,3 copies refute the ascending-incidence rank bound.
focus · theorem · proved · certified · supported · obstructed
Parent: [refuted_incidencerank_bound_for_ascending_edges]
**Consumer:** ["global ascending-edge bound","ascending-incidence rank route"]
**Role:** counterexample and sharpness calibration
**Consequence:** ["refutes rank_R(N_↑)>=2A/3","gives A/n->3/2 with every edge ascending"]
**Parameters:** A=9t, n=6t+3, rank=5t+2

## [unbounded_commonlastvertex_degree_for_ascending_edges] Unbounded common-last-vertex degree for ascending edges.
focus · theorem · proved · certified · supported · obstructed
Parent: [global_bound_for_ascending_edges]
**Consumer:** ["unrestricted pointwise ascending-degree bounds"]
**Role:** fence
**Main Route Relevance:** outside the admissible minimum-degree regime; does not rule out constant or logarithmic local control under the free minimum-degree assumption
**Minimum Degree:** 1
**Parameters:** common last-vertex degree r+1 with L=6*2^(r-1)

## [low_nonspecial_edges_force_larger_adjacency] Low-φ nonspecial edges force larger-φ adjacency.
focus · lemma · proved · certified · supported
Parent: [ascendingedge_rainbowlayer_formulation]
**Consumer:** dense-core and rotation-expansion arguments
**Limitation:** vacuous when t>=(δ+1)/2

## [edges_on_a_linear_cycle_have_rank_at_least_the_cycle_length] Nonspecial edges on a linear cycle have rank at least the cycle length.
focus · lemma · proved · certified · supported
Parent: [parent_ranks_and_lift_unless_they_close_a_linear_cycle]
**Given:** ["linear cycle","nonspecial edge characterized by unique longest-path entrance"]
**Consumer:** ["ordered-shadow cycle obstruction","flat-transfer cycles"]
**Consequence:** Any hidden cycle obstructing a rainbow ordered-shadow lift has length at most the minimum parent rank on that cycle.
**Next Need:** Combine cycle length <= minimum rank with strict ordered-shadow label growth to constrain endpoint ranks and entrance/terminal role patterns.

## [locationsensitive_lift_of_the_minty_walk] Location-sensitive lift of the Minty walk
focus · proof_level · proposal · not_required · unchecked
Parent: [vertexlevel_cyclictransient_minty_strategy]
**Given:** ["first-contact localization","terminal tail-blocker lemma","two-contact path rotation","vertex-level Minty potential"]
**Need:** choose a canonical repair move and score whose closed state-walks have nonpositive total score
**Consumer:** transient ascending-edge bound and repeated-blocker uncrossing
**Relation:** parallel refinement of the direct snake-digraph stepping idea

## [potentialthreshold_terminal_graphs_are_rainbowpathfree] Potential-threshold terminal graphs are rainbow-path-free.
focus · lemma · proved · certified · supported
Parent: [ascendingedge_rainbowlayer_formulation]
**Given:** ["ascending nonspecial edges with unique entrance labels","endpoint potentials phi","linearity"]
**Consumer:** ["multi-scale ascending-edge counting","potential-oriented rainbow/shadow route","2/3-leading-coefficient program"]
**Warning:** By itself, applying only generic rainbow-path extremal bounds to each threshold gives too coarse a sum to prove A=O(n); further coupling across thresholds is required.
**Consequence:** Every potential cut separates low-potential entrance colors from high-potential terminal vertices and produces a properly colored graph with no rainbow path as long as the threshold.

## [competitor_captures_all_vertices_of_a_lower_ascending_edge] High-rank competitor captures all vertices of a lower ascending edge.
focus · lemma · proved · certified · supported
Parent: [refuted_ascending_terminaldegree_conjecture]
**Given:** ["ascending nonspecial edge e of rank q","higher incoming competitor rank p>=2q-1 at a common terminal"]
**Consumer:** repeated-blocker splice and rank-cluster dichotomy
**Consequence:** every longest competitor path contains all three vertices of e

## [four_ascending_edges_can_share_one_last_vertex] Four ascending edges can share one last vertex.
focus · lemma · proved · certified · supported · obstructed
Parent: [refuted_ascending_terminaldegree_conjecture]
**Consumer:** ["unrestricted ascending terminal-degree conjecture","unrestricted compensated terminal-degree conjecture"]
**Role:** fence
**Consequence:** refutes the unrestricted local statements only
**Main Route Relevance:** outside the admissible minimum-degree regime for the exact 2/3 Turan route; does not refute a version assumed only under δ(H)>=floor(2ell/3)+1
**Minimum Degree:** 1

## [highrank_competitors_contain_the_whole_ascending_edge] High-rank competitors contain the whole ascending edge.
focus · lemma · proved · certified · supported
Parent: [refuted_ascending_terminaldegree_conjecture]
**Given:** ["ascending edge e of rank q","competing incoming edge f of rank at least 2q-1","rank-gap terminal blocker lemma"]
**Consumer:** repeated-blocker splice and bounded-charge versions of the ascending-edge route
**Consequence:** large rank separation forces complete three-vertex blocking, not merely one extra intersection

## [rankgap_forces_the_terminal_blocker_for_ascending_edges] Rank-gap forces the terminal blocker for ascending edges.
focus · lemma · proved · certified · supported
Parent: [refuted_ascending_terminaldegree_conjecture]
**Given:** ["ascending nonspecial edge of rank q","competing incoming edge at same terminal"]
**Consumer:** repeated-blocker splice route and ascending terminal-degree conjecture
**Consequence:** rank >=2q-1 forces blocking through the other terminal, not the low-rank entrance

## [firstcontact_localization_for_a_nonspecial_edge] First-contact localization for a nonspecial edge.
focus · lemma · proved · certified · supported
Parent: [splice_obligation_for_four_ascending_terminal_edges]
**Given:** ["nonspecial edge of rank q","arbitrary path meeting it"]
**Consumer:** repeated-blocker splice obligation and rotation route
**Consequence:** the first blocker contact is confined to the first q-1 path edges, or first q-2 if the contact uses a terminal label

## [separation_of_successive_contacts_with_a_nonspecial_edge] Separation of successive contacts with a nonspecial edge.
focus · lemma · proved · certified · supported
Parent: [splice_obligation_for_four_ascending_terminal_edges]
**Given:** ["a path meeting a nonspecial edge in successive distinct vertices"]
**Consumer:** ["repeated-blocker splice obligation","path-rotation arguments"]
**Consequence:** successive contacts are separated by at most q-1 edges, or q-2 when the later contact is not the unique entrance

## [terminal_tailblocker_lemma] Terminal tail-blocker lemma.
focus · lemma · proved · certified · supported
Parent: [refuted_ascending_terminaldegree_conjecture]
**Given:** ["nonspecial edge e of rank q terminal at v","snake-incoming edge f at v of rank at least q-1"]
**Consumer:** ascending terminal-degree, dense-core all-special, terminal-pair blocker arguments
**Consequence:** all blocking occurs inside a bounded q-2 edge tail

## [couples_a_forced_digraph_to_a_proper_colored_graph] Source/non-source decomposition couples a forced digraph to a proper colored graph.
focus · lemma · proved · certified · supported
Parent: [rainbowshadow_formulations_for_3uniform_linear_paths]
**Given:** ["linear triple family with one chosen source per triple"]
**Consumer:** ["directed-or-rainbow path route","general upper-bound strategy"]
**Role:** source-oriented rainbow/digraph coupling
**Consequence:** Splits every local triple degree exactly into source mass and non-source mass, producing complementary directed and properly-colored graph degree resources.
**Provenance:** Mehproof.md

## [potential_cuts_retain_the_exact_inducedcore_density_defects] Summed potential cuts retain the exact induced-core density defects.
focus · lemma · proved · certified · supported
Parent: [cuts_are_controlled_by_the_exact_inducedcore_density_defect]
**Given:** ["repaired exact levelwise potential-cut inequality"]
**Consumer:** ["equality-layer induction","weighted potential methods"]
**Consequence:** Weighted potential cuts remain valid with an exact correction by induced-core density defects; the missing research task is now isolated as control of those defects.
**Next Need:** Bound the aggregate superlevel defect sum_t xi_t from above using the low-degree witnesses forced whenever xi_t>=0.

## [weighted_potentialcut_inequality_for_the_exactdensity_layer] Weighted potential-cut inequality for the exact-density layer.
focus · lemma · proved · certified · supported
Parent: [cuts_are_controlled_by_the_exact_inducedcore_density_defect]
**Given:** ["a05c50b3ab96 levelwise potential-cut inequality"]
**Consumer:** ["E_ell equality layer","rank-distribution duality","weighted snake/rank-capacity route"]
**Role:** weighted equality-layer potential cuts
**Consequence:** All potential-cut constraints combine with arbitrary nonnegative threshold weights; the equality problem can be attacked by choosing a weight profile adapted to local rank-capacity lower bounds.
**Next Need:** Combine with the cumulative incident-rank constraint C_q(v)<=2q-1. Optimize a weight profile W so the resulting lower bound on sum_e W(phi(e)) from degree 3d contradicts the weighted cut upper bound, or classify the equality distributions.

## [special_edge_lies_strictly_below_all_three_endpoint_potentials] In minimum-potential equality, every special edge lies strictly below all three endpoint potentials.
focus · lemma · proved · certified · supported
Parent: [forces_the_specialedge_subhypergraph_to_be_a_cubicgraph_dual]
**Given:** ["148ebd1d1809 local saturation","0e550ff0eadd witness injection"]
**Consumer:** ["equality-layer classification","special-edge cubic skeleton","potential filtration"]
**Consequence:** At the rigid minimum-potential equality point, special edges are strictly submerged: every endpoint has potential at least one larger than the special edge rank. Maximum endpoint paths always finish with nonspecial edges.
**Next Need:** Combine the cubic special skeleton with strict submergence. Along an adjacency of two special edges their common vertex has potential above both edge ranks. Seek a potential orientation/weight on the cubic graph; cycles may force rank descent impossible around a loop unless adjacent special ranks are equal, while equal-rank cycles may yield long alternative-entrance paths.

## [upper_bound_has_an_additional_additive_thetaell_improvement] The (ell-13/6)n upper bound has an additional additive Theta(ell) improvement.
focus · theorem · proved · certified · supported
Parent: [general_upper_bound_improved_to_ell136n]
**Given:** ["7cae1cb001ac dense potential floor","92cce33dd917 near-floor stability","a3bf58adee0d first Type-A level exceptional-set bound","6a4d9b21f0c3 endpoint-potential floor"]
**Consumer:** ["general Turan upper bound","finite equality induction"]
**Role:** quantitative refinement of the new general upper bound
**Consequence:** Strengthens (ell-13/6)n by an additive c_ell asymptotic to ell/6.
**Next Need:** To alter the leading coefficient, replace the first-level exceptional-set lower bound |R|>=Theta(ell) by |R|>=Omega(n), or obtain a local weighted defect growing linearly with phi.

## [potential_layer_forces_distance_from_the_sevensixths_floor] The bottom potential layer forces distance from the seven-sixths floor.
focus · lemma · proved · certified · supported
Parent: [floor_only_oeta_n_vertices_and_edges_are_exceptional]
**Given:** ["fa7e5e79b905 near-floor stability","ascending entrance potential drop"]
**Consumer:** ["equality-layer potential expansion","potential-cut recursion"]
**Role:** bottom-layer stability obstruction
**Consequence:** A near-extremal potential floor requires a sublinear minimum-potential level. Quantitatively eta controls its density.
**Next Need:** Prove the minimum-potential level has positive density in an exact-density minimal obstruction, perhaps via the quadratic degree-potential inequality 6d45cc8708c2 or superlevel cut recursion. Any uniform lower bound |L_h|>=c n yields a uniform improvement above density+7/6.

## [strict_integer_form_of_the_ell_minus_thirteensixths_upper_bound] Strict integer form of the ell minus thirteen-sixths upper bound.
focus · theorem · proved · certified · supported
Parent: [potential_bound_is_never_attained_in_the_dense_regime]
**Given:** ["2ef762a38a25 strict seven-sixths potential theorem","fc68ffc8e4ea density-core reduction","6a4d9b21f0c3 minimum-degree potential floor"]
**Consumer:** ["general linear-path Turan bound"]
**Consequence:** Sharpens the newly proved (ell-13/6)n coefficient to a strict inequality and exact integer correction for every n.
**Next Need:** The asymptotic constant still requires a uniform improvement above seven-sixths. Current level recurrence gives only an additive Theta(delta) total-potential gap; a genuine coefficient gain needs either bounded source-capacity at potential cuts or a density/degree correlation input such as 6d45cc8708c2.

## [typea_potential_level_forces_a_large_exceptional_entrance_set] The lowest Type-A potential level forces a large exceptional entrance set.
focus · lemma · proved · certified · supported
Parent: [vertex_is_type_a_and_almost_every_nonspecial_edge_is_ascending]
**Given:** ["92cce33dd917 near-floor stability","d059bf8631a0 Type-A source orientation","minimum-degree endpoint-potential floor"]
**Consumer:** ["quantitative equality-layer stability","grand Turan induction"]
**Consequence:** The first Type-A level cannot appear without at least 2p0-5 exceptional entrance vertices. Thus the seven-sixths floor has an additive total-potential gap of order the minimum endpoint potential, hence order delta in dense cores.
**Next Need:** Use several consecutive low Type-A levels, not just the first. Each level sends its nonspecial terminal load into lower levels or R. Iterating the pair-capacity argument may force geometric/linear growth of the exceptional lower set and yield eta bounded below independently of n.

## [equality_vertices_have_at_most_one_deficient_special_incidence] Type-A equality vertices have at most one deficient special incidence.
focus · lemma · proved · certified · supported
Parent: [the_onespecial_local_equality_type_is_impossible]
**Given:** ["Type A from 45050da20aaa","672725540541 critical blocker slots","3a0d8866aba9 zero-double-blocker consequence"]
**Consumer:** ["equality-layer Type-A classification","special-edge potential orientation"]
**Consequence:** At a Type-A equality vertex, the four special incidences are almost flat: at least three have rank exactly phi(v), and the only possible defect is a unique edge of rank phi(v)-1.
**Next Need:** Orient a deficient special incidence v->e when phi(e)=phi(v)-1. Since an edge rank is common to its three endpoints, endpoints of a special edge differ in potential by at most one whenever all are Type A. Analyze the resulting level-graded 4-regular special hypergraph; degree/flow across potential levels may force a constant-level component with no deficient incidences.

## [is_a_3regular_special_core_plus_an_allascending_remainder] Minimum-potential equality is a 3-regular special core plus an all-ascending remainder.
focus · theorem · proved · certified · supported
Parent: [improves_average_endpoint_potential_to_density_plus_one]
**Given:** ["eeb9576892 density-plus-one potential floor","419519f0efa5 ascending-edge accounting"]
**Consumer:** ["equality-layer induction","b1fffccc673c source DAG route","special-core decomposition"]
**Role:** minimum-potential equality classification
**Consequence:** At equality sum phi=m+n, every vertex has special degree 3 and every nonspecial edge is ascending. For m=dn, there are n special edges and (d-1)n ascending nonspecial edges.
**Next Need:** Exploit the all-ascending remainder via b1fffccc673c. Couple the height-<ell source DAG with the 3-regular special core; special edges supply three internal rank-supported incidences at every vertex.

## [plus_one_gives_an_exact_threespecialedge_blocker_normal_form] Equality at density plus one gives an exact three-special-edge blocker normal form.
focus · lemma · proved · certified · supported
Parent: [universal_average_endpoint_potential_floor_to_density_plus_one]
**Given:** ["c77c818cf1e9 equality characterization","0e550ff0eadd terminal injection","fe38f0d97e12 snake-indegree saturation"]
**Consumer:** ["equality-layer classification","special-edge level decomposition","grand Turan route"]
**Consequence:** At the density+1 equality point, every vertex lies in exactly three special edges, and all three have rank equal to the vertex potential. Relative to any maximum endpoint path, the special edges occupy exactly the unclaimed blocker slots.
**Next Need:** Propagate equality across a special edge: if e={a,b,c} is special of rank q, then q=phi(a)=phi(b)=phi(c). Therefore the special-edge subhypergraph partitions into constant-potential components. Use 3-regularity plus specialness to constrain these components; seek a cycle/alternating-witness contradiction.

## [sources_are_exactly_the_onestep_incidence_rank_defects] Ascending sources are exactly the one-step incidence rank defects.
focus · lemma · proved · certified · supported
Parent: [directed_paths_lift_through_endpointpotential_growth]
**Given:** ["7235fdc47d1a entrance/special characterization"]
**Consumer:** ["potential-level decomposition","minimum-degree equality layer","source-oriented DAG"]
**Consequence:** The source-oriented DAG records every and only incidence where edge rank exceeds vertex potential. Special edges never create rank defects; they are entirely rank-supported at all three vertices.
**Next Need:** Use degree lower bounds: at a low-potential vertex p, all but the ascending-source edges have rank at most p and hence fit the 2p-1 local incidence capacity. This recovers d_H(v)-c(v)<=2p-1 and suggests sharper equality cases when degree is near d+1.

## [full_shadow_doubles_hypergraph_degree] Full shadow doubles hypergraph degree.
focus · lemma · proved · certified · supported
Parent: [rainbowshadow_formulations_for_3uniform_linear_paths]
**Consumer:** rainbow-path theorems
**Degree Scope:** full properly edge-colored 2-shadow
**Identity:** delta(shadow)=2 delta(H)
**Lifting Fence:** ordinary rainbow is insufficient in the full shadow unless colors avoid path vertices

## [originalhypergraph_densitycore_minimumdegree_reduction] Every nonempty 3-uniform hypergraph has an induced subhypergraph with density at least the original density and minimum degree at least that density; linearity and P_ell-freeness are preserved.
focus · lemma · proved · certified · supported
Parent: [rainbowshadow_formulations_for_3uniform_linear_paths]
**Consumer:** rainbow-shadow route and dense-core special-edge route
**Role:** first minimum-degree normalization; retain for hypergraph-side dense-core and attachment arguments
**Degree Scope:** original 3-uniform hypergraph

## [paths_force_complementary_sourcerainbow_endpoint_degrees] Longest directed paths force complementary source/rainbow endpoint degrees.
focus · lemma · proved · certified · supported
Parent: [rainbowshadow_formulations_for_3uniform_linear_paths]
**Given:** ["source-oriented decomposition","minimum triple degree d"]
**Consumer:** ["directed/rainbow tradeoff","endpoint bootstrapping"]
**Role:** longest-directed-path endpoint coupling
**Consequence:** A short longest directed path forces large source mass at its initial endpoint and large colored-graph degree at its terminal endpoint.
**Provenance:** Mehproof.md

## [sourceoriented_triples_force_a_727scale_directedorrainbow_path] Source-oriented triples force a 7/27-scale directed-or-rainbow path.
focus · theorem · proved · certified · supported
Parent: [rainbowshadow_formulations_for_3uniform_linear_paths]
**Given:** ["minimum triple degree m/n","source/non-source coupling","ergemlidzegyrimethuku_rainbow_path_turn_bound"]
**Consumer:** ["mixed directed/rainbow path problems"]
**Role:** source-oriented path guarantee
**Consequence:** Gives an unconditional 7/27-scale path guarantee in the source-oriented model.
**Provenance:** Mehproof.md
**Relation:** The EGM rainbow theorem was already in LINP; the new content is its direct application to the chosen-source construction.

## [twostage_minimumdegree_normalization_for_the_rainbow_shadow] Two-stage minimum-degree normalization for the rainbow shadow.
focus · lemma · proved · certified · supported
Parent: [rainbowshadow_formulations_for_3uniform_linear_paths]
**Consumer:** minimum-degree rainbow path theorems plus hypergraph dense-core arguments
**Warning:** delta(H0) and delta(J0) are distinct quantities on different objects
**Degree Scopes:** ["original hypergraph H0","properly edge-colored shadow graph J0"]

## [amortized_distinctdeletion_rotation_closure] Conjecturally, terminal degree p+t forces either Ω(t) reachable terminal pairs or a rotation sequence omitting Ω(t) distinct original private path vertices.
focus · lemma · conjecture · not_required · unchecked
Parent: [pscale_rotationclosure_via_deletable_blocker_endpoints]
**Given:** ["a51a7f9cff95 two-contact rotation","d71d4dd81a24 high terminal degree forces singleton expansion","48d3451e7530 p-scale rotation-closure conjecture"]
**Consumer:** ["48d3451e7530 p-scale rotation-closure via deletable blocker endpoints","99239ac0fa0b rotation-expansion route","general leading-coefficient improvement"]
**Falsification:** Exhibit arbitrarily large states with d(v)>=p+t and only o(t) reachable terminal pairs while every rotation sequence can omit only o(t) distinct original private vertices before forced restoration.
**Next Need:** Prove a monotone or amortized rotation sequence lemma giving Omega(t) distinct omitted original private vertices, or derive an alternative Pósa boundary inequality directly from t=d(v)-p.

## [maximumrank_forest_gives_canonical_blocker_chords] A maximum-total-rank spanning forest of the terminal-pair graph represents each unit of cycle rank by a nonforest chord that is minimum-rank on its fundamental cycle and blocks on both terminal sides.
focus · lemma · proved · certified · supported
Parent: [refuted_terminalpair_cycle_rank_is_controlled_by_special_edges]
**Given:** ["terminal-pair graph weighted by edge rank","terminal adjacency forces rank rise or blocker"]
**Consumer:** terminal-pair cycle analysis
**Consequence:** β(T) is represented exactly by nonforest chords, each minimum-rank on its fundamental cycle and forced to block on both terminal sides
**Correction:** removes the earlier unsupported rank-2 exclusion

## [terminal_blocker_contactcount_bound] For a lower-rank nonspecial edge f meeting a longest witness for e in r vertices, p <= r(q-1); in particular p >= 2q-1 forces all three vertices of f onto the witness path.
focus · lemma · proved · certified · supported
Parent: [terminal_adjacency_forces_rank_rise_or_a_blocker]
**Given:** ["terminal adjacency blocker","unique entrance characterization"]
**Consumer:** ["terminal-pair blocker arguments","high-rank competitor capture"]
**Consequence:** p>=2q-1 forces all three vertices of the lower-rank nonspecial edge onto the competitor path
**Correction:** counts distinct contact vertices and allows one contact vertex to lie in two consecutive path edges; replaces the invalid bounds 2q-3 and 3q-5

## [unblocked_sharedlastvertex_extension_raises_by_two] Two nonspecial edges sharing a terminal with no additional blocker contact force the second edge's rank to be at least two larger.
focus · lemma · proved · certified · supported
Parent: [terminal_adjacency_forces_rank_rise_or_a_blocker]
**Given:** ["two nonspecial edges sharing a vertex that is a last vertex for longest paths ending with both edges"]
**Consumer:** ["terminal-pair cycle arguments","transient part of the nonspecial-edge transfer digraph"]
**Consequence:** if the later edge does not meet the witness path elsewhere, φ increases by at least two

## [competitor_either_meets_the_penultimate_edge_or_meets_early] A two-contact competitor to a longest path ending in a nonspecial edge meets either the penultimate edge or an edge at least three positions before the end.
focus · lemma · proved · certified · supported
Parent: [twocontact_rotation_of_a_linear_path]
**Given:** ["a longest path ending in a nonspecial edge","an external edge meeting exactly one precursor edge and the last edge"]
**Consumer:** ["generalization of the P4 special-edge argument","rotation/blocker route"]
**Consequence:** the precursor contact is either the penultimate edge or lies at least three positions before the last edge
**Correction:** the earlier version incorrectly excluded the genuine j=p-1 case

## [rotation_and_forbidden_penultimatepredecessor_slot] A single-blocker edge at the terminal of a longest path gives a length-preserving rotation, and for a globally longest path ending in a nonspecial edge the attachment two positions before the end is impossible.
focus · lemma · proved · certified · supported
Parent: [twocontact_rotation_of_a_linear_path]
**Given:** ["globally longest path","single blocker at a terminal of a nonspecial maximum-rank last edge"]
**Consumer:** ["maximum-rank nonspecial-edge degree conjecture","rotation-expansion route"]
**Consequence:** single blockers rotate to globally longest paths; the attachment slot immediately two edges before the end is forbidden

## [reciprocaltail_uncrossing_for_charged_spacing] Reciprocal terminal-tail constraints on maximum paths at both terminals of a charged edge provide a two-path state for uncrossing and charged-edge spacing.
focus · proof_level · proposal · not_required · unchecked
Parent: [any_ranklong_terminal_path_has_a_terminaltail_blocker]
**Need:** prove a two-path uncrossing inequality or define a stepping score on reciprocal-tail states
**Consumer:** ["charged four-edge spacing","potential-oriented local bound","2/3 leading coefficient"]
**Relation:** direct continuation of the Minty-style stepping idea, now with a concrete reciprocal-tail state

## [endpointstate_minty_walk_for_potentialcharged_edges] The endpoint-state Minty route iterates nondecreasing-potential rotations until equal-potential recurrence must force blocker accumulation or spacing.
focus · proof_level · proposal · not_required · unchecked
Parent: [witness_gives_a_nondecreasingpotential_endpoint_rotation]
**Need:** choose a secondary score for equal-potential rotations and prove a closed-walk inequality or blocker accumulation bound
**Consumer:** ["potential-oriented local bound","charged four-edge spacing","2/3 leading coefficient"]
**Relation:** direct path-state realization of the original Minty stepping intuition

## [centralwindow_packing_for_commonterminal_ascending_edges] Ascending nonspecial edges of rank at most Q sharing a terminal on an r-edge path number at most 4Q-2r-3, yielding explicit lower bounds on their ordered ranks.
focus · lemma · proved · certified · supported
Parent: [blockers_recover_the_sharp_centralwindow_packing_bound]
**Given:** ["ascending nonspecial edges sharing a terminal","arbitrary sufficiently long path ending at that terminal","half-path endpoint-potential bound","terminal-tail blocker lemma"]
**Consumer:** ["charged four-edge spacing","repeated-blocker uncrossing","common-terminal rank clustering"]
**Consequence:** The sharp 4Q-2r-3 packing bound is path-relative; it does not require a maximum endpoint path or potential charging.
**Next Need:** Apply the lemma to a longest path for the largest-ranked edge in a four-edge spacing configuration and combine the resulting nested rank constraints with cross-blocker geometry.

## [fouredge_spacing_violation_is_tailterminal_or_spliceblocked] Any violation of charged four-edge spacing forces either the second edge's opposite terminal into the final q2-2 precursor edges of a longest e4-path, or a failure of the natural splice with a longest e1-path to be linear.
focus · lemma · proved · certified · supported
Parent: [spacing_conjecture_for_potentialcharged_ascending_edges]
**Given:** ["charged four-edge spacing violation","terminal-tail blocker lemma","uncrossed splice lemma"]
**Consumer:** ["charged four-edge spacing","reciprocal-tail uncrossing"]
**Consequence:** Reduces any spacing counterexample to two explicit branches: middle entrance absent with opposite terminal in the final tail, or middle entrance present with every natural low-rank/high-rank splice cross-blocked.
**Next Need:** Use e_3 to eliminate or charge the tail-terminal branch and the forced cross-intersections in the splice-blocked branch.

## [logarithmic_charged_degree_and_the_23_leading_coefficient] If the charged four-edge spacing conjecture holds, then at most 3+ceil(log2 p) qualifying ascending nonspecial edges can share a terminal of rank p, yielding the stated 2/3 leading coefficient bound for P_l^(3)-free linear 3-graphs.
focus · lemma · proved · certified · provisional
Parent: [spacing_conjecture_for_potentialcharged_ascending_edges]
**Given:** charged four-edge spacing
**Consumer:** general linear-path Turan upper bound
**Consequence:** a charged spacing theorem, much weaker than constant potential-oriented degree, already yields ex_L(n,P_ell^(3)) <= (2ell/3+O(log ell))n

## [strictrise_clean_u11_edges_still_violate_fouredge_spacing] For every R≥43 there are four ascending nonspecial edges of ranks (R+1,R+1,R+7,R+7), common-terminal rank R+9, and opposite-terminal ranks R+10 satisfying the stated clean terminal-incidence hypotheses yet violating four-edge spacing.
focus · lemma · proved · certified · supported
Parent: [minimumterminal_edges_violate_spacing_in_two_double_cells]
**Given:** ["74d30147c051 equal-terminal clean U11 spacing counterexample"]
**Consumer:** ["uphill-certificate branch","strict-rise spacing program","edges_split_into_sameterminal_and_uphill_certificate_classes"]
**Consequence:** Strict terminal-potential rise, even together with source-cleanliness and terminal-singleness at both terminals, does not restore four-edge deficit-doubling. The selected higher-terminal common-anchor certificate is genuinely essential in class H.
**Next Need:** Analyze class H using the certificate geometry at the higher terminal; do not reduce it to a generic strict-rise local bound or strict-rise four-edge spacing.

## [pure_rankfive_obstruction_are_pushed_away_from_the_final_joint] In the φ(v)=5 pure rank-five configuration, a competing edge meeting the precursor only at a path joint cannot meet the final precursor joint; if it meets the preceding joint a, then φ(c)≥5.
focus · lemma · proved · certified · supported
Parent: [rankfive_at_potential_five_forces_a_multiprecursor_competitor]
**Given:** ["e2095c60d904 corrected simple/multi-precursor dichotomy"]
**Consumer:** ["p=5 5555 elimination","charged four-edge spacing"]
**Consequence:** A one-vertex joint blocker cannot occur at the final precursor joint c. If it occurs at the middle joint a, it forces the next joint c to endpoint potential at least five.
**Next Need:** Analyze the first joint r and the middle-joint case using entrance/terminal labels. For a joint-only competitor, if the joint is its entrance then that joint has potential 4; if it is its opposite terminal then potential >=5. Combine the middle case phi(c)>=5 with a second competitor or with the fixed entrance d of potential 4.

## [labels_occupy_a_bounded_central_window_on_a_linear_path] Low-vertex-rank labels occupy a bounded central window on a linear path.
focus · lemma · proved · certified · supported
Parent: [a_vertex_on_a_linear_path_has_halfpath_endpoint_potential]
**Given:** ["8b1790d79d74 position-sensitive vertex-rank lower bound on a path"]
**Consumer:** ["same-type entrance-label packet","rank-band common-path packing","post-43/48 local congestion"]
**Consequence:** A path of length L contains at most 4R-2L+1 vertices of vertex rank at most R when R<L; low-rank labels are confined to the central occurrence window.
**Next Need:** Apply to the X-branch of f84b001e0a61 on either higher-rank source path. A linear packet of shared entrances forces the lower half of the edge-rank sequence upward.

## [oddcentral_foursingle_state_is_an_exact_lossone_normal_form] The G-only odd-central four-single state is an exact loss-one normal form.
focus · lemma · proved · certified · supported
Parent: [four_single_contacts_cannot_occupy_both_rightmost_slots]
**Given:** ["47815dccb8b0 excludes F+G","a01ddfa76dc8 terminal-only localization","eac2e3da3eea joint clean conflict"]
**Consumer:** ["a9d95378e855 corrected rank-pair block","Astra conflict-matching reconstruction"]
**Role:** odd-central G-only loss-one normal form
**Consequence:** The G-only four-single obstruction is reduced exactly to A,B,C,G, with C terminal-only and a canonical q-edge wrong-entrance path into h_G one edge short of contradiction.
**Next Need:** Use the A/B edges as blockers of the loss-one state. Split A/B entrance-visible versus terminal-only. Terminal-only cases are equality states for df8/f0 and should admit a canonical rotation; the X-X case has three visible q-potential entrances A,B,G and should yield a distance/cell conflict.

## [a_foursingle_obstruction_cannot_occupy_the_rightprivate_slot] At the odd central boundary a four-single obstruction cannot occupy the right-private slot.
focus · lemma · proved · certified · supported
Parent: [rankpair_obstruction_cannot_occupy_the_rightjoint_slot]
**Given:** ["8d1adea102fe eliminates G","08f894b8cb5e clean-private hole rule","single-contact seven-slot localization"]
**Consumer:** ["a9d95378e855 corrected consecutive-rank block","Astra 11/12 route"]
**Role:** odd-central corrected rank-pair packing
**Consequence:** At p=2q-3, any four all-single charged contacts in ranks {q,q+1} are confined to the five left/central slots A,B,C,D,E.
**Next Need:** Classify four-of-five occupancy in A..E. Every occupied E must be terminal-only unless B,C are both absent; every occupied C with A also occupied must be terminal-only. Use these forced U-labels and two-star bridge splices to eliminate the five residual missing-slot patterns.

## [rankpair_obstruction_cannot_occupy_the_rightprivate_slot] At p=2q-3 a four-single rank-pair obstruction cannot occupy the right-private slot.
focus · lemma · proved · certified · supported
Parent: [rankpair_obstruction_cannot_occupy_the_rightjoint_slot]
**Given:** ["p=2q-3","four all-single assigned charged edges in ranks {q,q+1}","G already eliminated"]
**Consumer:** ["defect-corrected consecutive-rank block","Astra 11/12 route"]
**Consequence:** The private right slot F is also impossible. Any four-single obstruction is confined to the five left-central slots A,B,C,D,E.
**Next Need:** Classify four-of-five occupancy on A,...,E using clean-joint holes. E as a visible entrance forbids B,C; C as a visible entrance forbids A. The only dense states should force E terminal-only and a short list of label patterns; use two-star bridges to finish.

## [a_onelow_foursingle_obstruction_pins_the_low_witness_to_c] At the odd boundary a one-low four-single obstruction pins the low witness to C.
focus · lemma · proved · certified · supported
Parent: [rankpair_obstruction_cannot_occupy_the_rightprivate_slot_2]
**Given:** ["8d1adea102fe/f378e6022301 right-slot exclusions","a01ddfa76dc8 low terminal-only localization","c448268039f5 one-rank-higher contacts on canonical low entrance rail"]
**Consumer:** ["p=2q-3 one-low defect-corrected block","Astra 11/12 route"]
**Consequence:** Any all-single q,(q+1)^3 obstruction at p=2q-3 has its low edge centered at C=g_{q-2}∩g_{q-1}. The D and E low-entrance branches are eliminated.
**Next Need:** Split the central C-low edge by label. If C is a visible low entrance, its clean-joint hole forces A empty, so the three high witnesses are B,D,E with E terminal-only. If C is terminal-only, its entrance is off P and the high witnesses occupy three of A,B,D,E. Attack these two exact residual states using the canonical low entrance rail / loss-one endpoint rotations.

## [does_not_automatically_block_a_lossone_wrongentrance_precursor] An equal-rank competitor does not automatically block a loss-one wrong-entrance precursor, because the shared terminal already appears in the precursor and prevents the proposed extension.
focus · lemma · conjecture · not_required · unchecked
Parent: [foursingle_state_is_an_exact_lossone_wrongentrance_state]
**Consumer:** ["pure-high odd-boundary 0-1-1 block","Astra 11/12 route"]
**Role:** refuted route
**Lesson:** A wrong-entrance loss-one witness already carries the common terminal v in its final precursor edge. Common-v competitors cannot simply be appended; any valid recovery of the missing edge must omit/rotate that terminal-bearing precursor edge or use a source/terminal contact away from v.

## [nondouble_witnesses_are_pushed_to_the_left_central_slots] At p=2q-3 terminal-only non-double witnesses are pushed to the left central slots.
focus · lemma · proved · certified · supported
Parent: [consecutiverank_block_is_sufficient_for_the_1112_bound]
**Given:** ["phi(v)=2q-3","chosen maximum endpoint path","charged edge non-double on that path"]
**Consumer:** ["defect-corrected two-rank block","Astra 11/12 route"]
**Consequence:** At the first layer below the solved half-rank boundary, terminal-only witnesses are one-sided. A low rank-q terminal-only witness is uniquely pinned, while the two rightmost high-rank witness slots can only be low-potential entrances.
**Next Need:** Assume four non-double edges in ranks {q,q+1}. Use distinct witness packing plus the mixed distance-two rule 08f894b8cb5e. If either rightmost slot is occupied, it is a clean entrance and forbids a same-parity private predecessor; if both are unused, all four witnesses are packed into the five left terminal-capable slots and terminal-order constraints should force collision.

## [p2q3_the_unique_low_edge_cannot_use_the_private_middle_witness] At p=2q-3 the unique low edge cannot use the private middle witness.
focus · lemma · proved · certified · supported
Parent: [consecutiverank_block_is_sufficient_for_the_1112_bound]
**Given:** ["p=2q-3 four all-single state","65894e91ed50 quantitative separation","F,G exclusions"]
**Consumer:** ["one-low q(q+1)^3 corrected block","Astra 11/12 route"]
**Role:** odd-boundary one-low reduction
**Consequence:** In the one-low all-single equality pattern the low rank-q witness is forced to C=g_{q-2}∩g_{q-1}; D is impossible and E was already impossible as a terminal-only low witness.
**Next Need:** Analyze the low-at-C state. Split C entrance-visible versus terminal-only. If entrance-visible, A is empty and the occupied set is B,C,D,E with E terminal-only high. If terminal-only, C is the unique dirty low witness and three high contacts occupy three of A,B,D,E.

## [at_the_odd_boundary_have_reciprocal_centralgate_normal_forms] High 0-1-1 edges at the odd boundary have reciprocal central-gate normal forms.
focus · lemma · proved · certified · supported
Parent: [oddboundary_consecutiverank_fouredge_normal_form]
**Given:** ["rank-(q+1) 0-1-1 edge assigned at potential 2q-3 terminal"]
**Consumer:** ["surviving one-low odd-boundary triangle","all-high p=2q-3 case"]
**Consequence:** Every opposite high terminal supplies a second central coordinate system for its edge; strict terminal rises make this system especially rigid.
**Next Need:** Apply to the forced D-terminal-only high edge in 512f6864eb96. Couple its reciprocal central contact on P_D with the C-D-v triangle on P_v and the clean source rail P_y; seek a three-rail theta or a source contact contradiction.

## [d_contact_forces_the_outer_right_joint_to_top_potential] The terminal-only D contact forces the outer right joint to top potential.
focus · lemma · proved · certified · supported
Parent: [oddboundary_consecutiverank_fouredge_normal_form]
**Given:** ["512f6864eb96 D terminal-only","2e04b9ddaeaf charged endpoint rotation","fb9dfc3b63b8 C rotation"]
**Consumer:** ["p=2q-3 0-1-1 one-low residue","Astra rotation/conflict matching"]
**Consequence:** The sole one-low residual contains two adjacent high-potential rotation endpoints E,G immediately to the right of its adjacent terminal-only contacts C,D.
**Next Need:** Use the 0-1-1 condition at terminals C and D. Their chosen maximum paths are single for the corresponding edges. Since phi(C) is p or p+1 and phi(D) is in [p,2q], path-relative witness localization should force the absent entrances x,y_D into narrow reciprocal windows or force wrong-terminal witnesses; compare with the E/G rotated states.

## [residue_forces_a_completely_toppotential_central_edge] The final odd-boundary residue forces the central edge and all its vertices to top potential.
focus · theorem · proved · pending · unchecked · pending
Parent: [oddboundary_consecutiverank_fouredge_normal_form]
**Consumer:** ["0-1-1 conflict matching","Astra 11/12 route"]
**Consequence:** The final odd-boundary residue manufactures a central edge whose rank and all three vertex potentials are at least p.

## [terminal_paths_have_a_fourlevel_reciprocal_central_normal_form] High 0-1-1 terminal paths have a four-level reciprocal central normal form.
focus · lemma · proved · certified · supported
Parent: [state_creates_a_fourvertex_highpotential_central_packet]
**Given:** ["0-1-1 rank-(q+1) edge","terminal potential at least 2q-3","terminal-potential bound","terminal-tail and half-path localization"]
**Consumer:** ["final one-low odd-boundary state","Astra 11/12 0-1-1 block"]
**Role:** reciprocal high-terminal central normal form
**Consequence:** For q>=5, the chosen path at the high D terminal has only finitely many central contact states; at phi(D)=2q the sole contact is forced to be the entrance at the exact central joint.
**Next Need:** Apply to h_D in 310000f0630b. Compare its reciprocal central state with the explicit P_v rotation ending at G. For s=2q or 2q-1 seek an immediate uncrossing; for s<=2q-2 combine with the analogous C-path normal form 436d55f14de2.

## [raises_the_outer_right_joint_to_full_terminal_potential] The forced middle-private low entrance raises the outer right joint to full terminal potential.
focus · lemma · proved · certified · supported
Parent: [rankq_edges_at_p2q3_have_a_twopattern_middleedge_normal_form]
**Given:** ["35ee7b35de05 forced middle-private low entrance"]
**Consumer:** ["p=2q-3 corrected rank-pair block"]
**Consequence:** Saturating the rank-q capacity forces a full-potential rotation endpoint at the outer right joint. Hence the right-joint rank-(q+1) entrance slot is deleted entirely in every two-low all-single state.
**Next Need:** Classify the two remaining rank-(q+1) single witnesses after deleting D. If private(g_q) is used as an entrance it forbids private(g_{q-2}); combine with the two low witness patterns {A,B}/{B,C}. Remaining all-left states should reduce to terminal-only contacts packed into g_{q-2}∪g_{q-1}, where U-rotation yields another high-potential joint.

## [tworank_block_is_automatic_at_the_halfrank_top_boundary] The defect-corrected two-rank block is automatic at the half-rank top boundary.
focus · lemma · proved · certified · supported
Parent: [consecutiverank_block_is_sufficient_for_the_1112_bound]
**Given:** ["a9d95378e855 corrected rank-pair target","0592bb08cd2d all-visible entrances","cross-cut terminal localization"]
**Consumer:** ["Astra 11/12 route"]
**Consequence:** The former hardest q(q+1)^3 top-boundary gadget is overpaid by double-contact defect: its three high edges are all double on P_v. No elimination/uncrossing of the gadget is needed for the corrected 11/12 route.
**Next Need:** Descend to p<=2q-3. Prove that any four-edge q(q+1)^3 equality pattern either has a double contact on P_v or violates clean-contact spacing. Since only one double is needed to reduce four free edges to three, this should be much easier than outright elimination.

## [defect_is_bounded_by_the_number_of_011_ascending_edges] The clean-minus-double defect is bounded by the number of 0-1-1 ascending edges.
focus · lemma · proved · certified · supported
Parent: [defectcorrected_tworank_block_suffices_for_the_1112_bound]
**Given:** ["4e165e65be58 clean-minus-double contact identity"]
**Consumer:** ["Astra 11/12 route"]
**Consequence:** Only 0-1-1 ascending edges can contribute positively to C-D. The 11/12 problem reduces to a pure packing bound for edges clean at the source and single at both terminals; every other source-clean edge is automatically paid by terminal double-contact defect.
**Next Need:** Assign each 0-1-1 edge to a minimum-potential terminal. Prove the consecutive-rank block n_q^{011}(v)+n_{q+1}^{011}(v)<=3, then pair ranks exactly as in 2665d2c81d39. Reciprocal terminal-path lemmas such as 436d55f14de2 now apply automatically.

## [mutually_blocking_high_entrance_rails_force_a_twovertex_overlap] Four mutually blocking high entrance rails force a two-vertex overlap.
focus · lemma · proved · certified · supported
Parent: [defectcorrected_tworank_block_suffices_for_the_1112_bound]
**Given:** ["four equal-rank ascending nonspecial edges through one common terminal","canonical source-clean entrance rails"]
**Consumer:** ["pure (q+1)^4 odd-central residue","Astra clean-source 11/12 route"]
**Consequence:** Four mutually blocking q-edge source rails cannot form a simple one-intersection braid. Some pair has a genuine two-vertex overlap, without needing any lower-rank edge as a pigeonhole gate.
**Next Need:** Exploit the two-rail theta together with terminal-single placement on P_v. Choose consecutive common vertices on one rail; if segment order agrees, splice unequal segments to exceed endpoint potential q, while reversed order gives a linear cycle. Use the four high-edge labels to rule out the exact coincident-segment residue.

## [edges_must_meet_the_early_part_of_the_low_clean_source_path] Two high edges must meet the early part of the low clean source path.
focus · lemma · proved · certified · supported
Parent: [c_branch_of_the_onelow_oddboundary_obstruction_is_impossible]
**Given:** ["surviving source-clean one-low odd-boundary state","clean low source path of length q-1","three edge-rank-(q+1) high edges through the common terminal"]
**Need:** Combine the two early high contacts on the low source path with their three-of-four contacts A,B,D,E on the v-path, or with the reciprocal flat C-path, to force a forbidden splice.
**Consumer:** ["flat phi(C)=2q-3 branch","0-1-1 consecutive-rank block","Astra 11/12 route"]
**Consequence:** At least two high edges have contacts before the last two edges of the low source path; only one high edge can be confined to its final edge.

## [low_cterminal_rotation_forces_the_next_joint_to_top_potential] The surviving low C-terminal rotation forces the next joint to top potential.
focus · lemma · proved · certified · supported
Parent: [c_branch_of_the_onelow_oddboundary_obstruction_is_impossible]
**Given:** ["fce6ecc978fb surviving C-terminal low edge","2e04b9ddaeaf charged endpoint rotation"]
**Consumer:** ["0-1-1 two-rank block","Astra 11/12 route"]
**Role:** one-low odd-boundary rotation pressure
**Consequence:** The low terminal-only C contact rotates the maximum v-path to a maximum path ending at the next joint E, forcing E to have top potential. Any high edge contacting E must use E as a terminal, never as its entrance.
**Next Need:** Use phi(E)>=p together with the 0-1-1 condition at E: if E is occupied, the corresponding high edge is single at both v and E. Compare the chosen maximum E-path with the rotated E-ending path to force its entrance into a narrow central window. If E is omitted, the three high contacts are A,B,D and the low source rail P_x must be crossed by all three.

## [branch_recreates_an_allvisible_fourslot_crossedchord_gadget] The rising low-terminal branch recreates an all-visible four-slot crossed-chord gadget.
focus · lemma · proved · certified · supported
Parent: [branch_the_three_high_edges_are_disjoint_twosided_chords]
**Given:** ["d734b1420b2f three disjoint two-sided chords","8b1790d79d74 position-sensitive endpoint potential"]
**Consumer:** ["rising branch of one-low odd-boundary 0-1-1 block","Astra 11/12 route"]
**Consequence:** When the low opposite terminal rises to 2q-2, the final residue becomes the same three-of-four central entrance gadget seen at the half-rank boundary, but stronger: every high edge is already a two-contact chord crossing the central cut.
**Next Need:** Exploit the four missing-slot patterns using the fact that the opposite terminals are the second chord contacts, not merely existential blockers. Derive the exact left/right distance bounds from phi(x)=q-1; a left entrance whose right terminal occurs by r_{q+2}, or the symmetric right entrance, immediately yields a q-edge x-ending splice.

## [gadget_orders_the_two_far_terminals_on_its_fully_occupied_side] The rising four-slot gadget orders the two far terminals on its fully occupied side.
focus · lemma · proved · certified · supported
Parent: [lowterminal_branch_has_a_pure_fourslot_crosscut_entrance_gadget]
**Given:** ["33522a8389e9 pure four-slot cross-cut gadget"]
**Consumer:** ["rising low-terminal elimination","Astra 11/12 conflict matching"]
**Role:** ordered conflict matching in rising branch
**Consequence:** On the doubly occupied side of any three-of-four entrance pattern, the remote terminals have forced monotone order: joint-side chord lands no farther from center than private-side chord.
**Next Need:** Bring in the third cross-cut chord. Its entrance lies on the opposite side and its terminal on the doubly occupied side. Use its source-clean entrance rail to derive the reverse inequality between the two same-side chords, or show equality forces a two-cycle/theta. This is now an order-cycle problem rather than arbitrary path geometry.

## [onelow_branch_becomes_a_fourslot_orientedchord_conflict_system] The rising one-low branch becomes a four-slot oriented-chord conflict system.
focus · lemma · proved · certified · supported
Parent: [branch_the_three_high_edges_are_disjoint_twosided_chords]
**Given:** ["rising low terminal phi(C)=2q-2","three two-sided high chords"]
**Consumer:** ["one-low p=2q-3 0-1-1 block"]
**Consequence:** The rising branch reduces to four source-slot patterns with explicit left/right terminal-crossing obligations. The two patterns containing both a joint source and both opposite-side source slots force two terminals completely across the central cut.
**Next Need:** Eliminate the four source-slot patterns. For {L,B,R}, both z_B,z_R lie left; use the two right-source edges consecutively against their ordered left terminals. For {L,A,R}, use the symmetric argument. For missing-joint patterns {A,B,R} and {L,A,B}, use the sole joint source with the opposite private source and the third chord as blocker.

## [the_flat_lowterminal_branch_is_thetaorterminalcentral] The flat low-terminal branch is theta-or-terminal-central.
focus · lemma · proved · certified · supported
Parent: [the_rising_lowterminal_oddboundary_branch_is_impossible]
**Given:** ["surviving one-low 0-1-1 state","phi(C)=phi(v)=2q-3"]
**Consumer:** ["0-1-1 consecutive-rank block","Astra 11/12 route"]
**Consequence:** Three of the four reciprocal central states (those using source x) automatically create a theta between P_C and the clean source rail P_x. The sole non-theta reciprocal state is terminal v at the left central joint of P_C.
**Next Need:** Theta branch: use the three high edges, at least two of which meet the early part of P_x, against an elementary P_C/P_x lens and invoke the no-piercing lemma. Terminal-central branch: exploit the symmetric pair of terminal-only central joints C on P_v and v on P_C.

## [every_foreign_011_contact_manufactures_an_endpoint_lens] Every foreign 0-1-1 contact manufactures an endpoint lens.
focus · lemma · proved · certified · supported
Parent: [rail_in_a_tworank_011_block_crosses_every_foreign_edge]
**Given:** ["complete foreign-edge transversality of 0-1-1 source rails"]
**Consumer:** ["0-1-1 consecutive-rank block","Astra conflict matching"]
**Consequence:** All 12 directed foreign contacts create genuine two-path theta/lens states, either source-source or source-terminal. The obstruction can be viewed as a dense lens network among the chosen maximum endpoint paths.
**Next Need:** Choose a minimal elementary lens in this network. By balanced-lens/no-piercing, every other forced contact path must lie on its boundary or exterior. Use minimality to show two of the remaining eleven forced lenses must pierce it or share a boundary, yielding either a smaller lens or an endpoint-label contradiction.

## [crossedge_cannot_pierce_a_balanced_lens_between_maximum_rails] A third cross-edge cannot pierce a balanced lens between maximum rails.
focus · lemma · proved · certified · supported
Parent: [clean_lenses_between_maximum_source_rails_are_balanced]
**Given:** ["balanced clean internal lens between maximum source rails","one cross-edge through the two lens interiors"]
**Consumer:** ["0-1-1 two-rank block","Astra 11/12 source-rail theta route"]
**Consequence:** The balanced-lens residue cannot be pierced by a foreign offending edge. Since every foreign 0-1-1 edge must meet both source rails, each such edge must place at least one of its two rail contacts outside every elementary internal lens, unless it creates an additional common vertex that refines the lens.
**Next Need:** Take an elementary lens between the overlap pair from f8803379f9a3. The other two offending edges meet both rails. Use the no-cross-edge lemma to force their four contacts into the exterior tails or onto common lens boundaries. With two edges and only two exterior sides, derive either a new common distinguished vertex, an endpoint lens, or an impossible contact ordering.

## [agreements_and_offending_crossedges_are_complementary] Distinguished agreements and offending cross-edges are complementary.
focus · lemma · proved · certified · supported
Parent: [four_source_rails_force_two_units_of_distinguished_overlap]
**Given:** ["four source-rail distinguished transversals"]
**Consumer:** ["balanced-lens non-piercing route","Astra 11/12 source-rail theta route"]
**Consequence:** Distinguished overlap and offending cross-edge count are exact complements on every rail pair: a_ij common distinguished vertices means 4-a_ij offending cross-edges.
**Next Need:** For a pair with at least two common distinguished vertices, pass to elementary balanced lenses. Each of the at most two disagreement edges is a literal cross-edge, so b5d44965d984 forbids it from having its two contacts in the interiors of the same lens. Classify the remaining exterior/boundary placements.

## [imbalance_exactly_measures_excess_distinguished_rail_overlap] Source-hit imbalance exactly measures excess distinguished rail overlap.
focus · lemma · proved · certified · supported
Parent: [four_source_rails_force_two_units_of_distinguished_overlap]
**Given:** ["four source-clean 0-1-1 rails and their distinguished source/terminal transversals"]
**Consumer:** ["0-1-1 consecutive-rank block","Astra 11/12 source-rail route"]
**Consequence:** Distinguished overlap has an exact defect formula: baseline 8 plus quadratic source-hit imbalance. The extremal residual has exactly one foreign source hit at every offending edge.
**Next Need:** Analyze the extremal balanced state s_j=1 for all j as a four-vertex directed source-hit graph. Two-cycles immediately give double-source rail overlaps; in their absence the source-hit arcs are forced into longer directed-cycle structure, which should combine with aligned-joint levels and the two-lens dichotomy.

## [source_block_has_two_lens_cells_and_reciprocal_simple_pairs] Every four-edge two-rank source block has two lens cells and reciprocal simple pairs.
focus · lemma · proved · certified · dependency_hold
Parent: [four_source_rails_force_two_units_of_distinguished_overlap]
**Given:** ["pairwise source-rail intersection","two-unit distinguished overlap","universal aligned-joint rigidity","reciprocal-terminal rule for unique intersections"]
**Consumer:** ["0-1-1 consecutive-rank packing bound","one-low odd-central q,(q+1)^3 residue","Astra 11/12 route"]
**Consequence:** Any four-edge two-rank obstruction has at least two lens cells; all rail pairs outside those multiple-overlap interactions are rigid aligned reciprocal-terminal pairs.
**Next Need:** Eliminate or charge the remaining lens normal forms. Internal clean cells are balanced and cannot be pierced by an offending cross-edge; only endpoint lens cells or exterior cross-edge placements remain. Classify those placements in the one-low q,(q+1)^3 state.

## [extremal_c4_rail_skeleton_carries_two_clean_lengthtwo_bridges] The extremal C4 rail skeleton carries two clean length-two bridges.
focus · lemma · proved · certified · supported
Parent: [the_simple_sourcerail_graph_has_at_most_four_edges]
**Given:** ["C4 simple source-rail skeleton"]
**Consumer:** ["0-1-1 consecutive-rank block","Astra conflict matching"]
**Consequence:** Each of the two theta rail pairs has two labeled terminal boundaries joined by a clean two-edge bridge through v. Any elementary lens on those boundaries must have side length at least two.
**Next Need:** Exploit equality t=2 versus t>=3. If t=2, compare the two rail-side 2-edge paths with the star bridge to get a local three-path theta of length two; source/terminal labels should force a repeated pair. If t>=3, one of the remaining simple rails should meet the long lens side internally, violating no-piercing/minimality.

## [the_c4_sourcerail_residue_forces_a_fourvertex_diagonal_overlap] The C4 source-rail residue forces a four-vertex diagonal overlap.
focus · lemma · proved · certified · dependency_hold
Parent: [the_simple_sourcerail_graph_is_trianglefree]
**Given:** ["C4 simple source-rail skeleton","simple pairs are reciprocal terminal-only","complete source-rail transversality"]
**Need:** Exploit the four-overlap diagonal using endpoint lenses, balanced internal lenses, and no-piercing.
**Consumer:** ["C4 elimination","one-low q,(q+1)^3 residue","Astra 11/12 source-rail route"]
**Consequence:** Every C4 residue contains a diagonal pair of source paths sharing four distinguished vertices, including both source endpoints.

## [pushes_the_flat_terminal_lens_into_the_late_highrail_zone] Terminal-tail blocking pushes the flat terminal lens into the late high-rail zone.
focus · lemma · proved · certified · supported
Parent: [sourcerail_contacts_force_the_balanced_onelow_terminal_lens]
**Given:** ["minimal balanced terminal-terminal lens state","certified terminal tail-blocker lemma"]
**Consumer:** ["flat one-low odd-central uncrossing"]
**Consequence:** All reciprocal terminal contacts relevant to the minimal lens sit in the late zone of the high source rails; the low terminal u_0 is one step more restricted.
**Next Need:** Use the common aligned joint position of u_0 and the late positions of u_1,u_2,u_3 to classify the two exterior endpoint chords e_1,e_2 relative to the balanced u_0-u_3 lens.

## [sourceclean_commonterminal_edges_cross_each_other] Consecutive-rank source-clean common-terminal edges cross each other.
focus · lemma · proved · certified · supported
Parent: [rail_in_a_tworank_011_block_crosses_every_foreign_edge]
**Given:** ["two source-clean ascending nonspecial edges sharing a terminal","edge ranks equal or consecutive"]
**Consumer:** ["odd tight U_11 color-terminal collision","two-rank source-path overlap","0-1-1 local analysis"]
**Consequence:** The complete foreign-edge transversality phenomenon is already a two-edge consecutive-rank fact and does not require assignment or a four-edge block.
**Next Need:** Combine the two mandatory cross-contacts with unique-intersection rigidity. A source hit forces at least two common vertices of the two source paths; if both source paths intersect uniquely, both cross-contacts must be through the opposite terminals.
**Strengthens:** rail_in_a_tworank_011_block_crosses_every_foreign_edge

## [bound_for_011_edges_alone_gives_the_1112_coefficient] A three-per-two-ranks bound for 0-1-1 edges alone gives the 11/12 coefficient.
focus · lemma · proved · certified · supported
Parent: [the_entire_contactsnake_defect_reduces_to_011_ascending_edges]
**Given:** ["certified 0-1-1 defect reduction","potential-oriented terminal assignment"]
**Consumer:** ["Astra 11/12 leading coefficient"]
**Consequence:** Only unpaid 0-1-1 transitions need the three-per-two-ranks packing theorem. All paid clean edges and all double-contact states disappear from the local target.
**Next Need:** Prove the local block for 0-1-1 edges. At p=2q-3 use both terminal paths: each edge is single-contact not merely at assigned v but also at its opposite terminal, while its source is clean.

## [edges_form_a_universal_core_of_all_nonspecial_witness_paths] High-degree-only edges form a universal core of all nonspecial witness paths.
focus · lemma · proved · certified · supported
Parent: [cover_every_offwitness_edge_in_an_edgeminimal_counterexample]
**Given:** ["1e01357bf9c3 threshold-degree cover"]
**Consumer:** ["grand induction","rotation-state compression","critical-set counting"]
**Role:** minimal-counterexample common-core lemma
**Consequence:** All high-degree-only edges form a rigid core common to every bad witness path; all path mobility occurs through edges incident with threshold-degree vertices.
**Next Need:** Bound the size/shape of the common core or show that enough rotations force many distinct D-supported path edges, giving a density contradiction on D.

## [every_equalitylayer_witness_omits_many_abovethreshold_vertices] Every equality-layer witness omits many above-threshold vertices.
focus · theorem · proved · certified · supported
Parent: [bad_witness_omits_a_vertex_of_degree_at_least_d_plus_two]
**Given:** ["exact density m=dn","minimum degree d+1","linearity","path length <=ell-1"]
**Consumer:** ["equality-layer induction","outside-reservoir route","high-degree packet deletion"]
**Consequence:** Every witness misses an Omega(ell)-sized packet of above-threshold vertices: d,d-2,d-1 by residue. The equality obstruction cannot concentrate all degree excess on the witness.
**Next Need:** Apply the vertex-minimal packet inequality to this high-degree outside set. Count edges meeting the packet versus total excess; seek a subset whose shared-edge savings make deletion cost <=d|S|, or show the required anti-sharing forces many distinct attachments/chords into P.

## [chords_through_one_outside_owner_give_an_exact_bridge_splice] Two two-contact chords through one outside owner give an exact bridge splice.
focus · lemma · proved · certified · supported
Parent: [induction_reconciles_turan_and_criticalcore_minimality]
**Given:** ["outside vertex with two two-contact chords into a path"]
**Consumer:** ["equality-layer outside-reservoir route"]
**Consequence:** Pairs of chords owned by one outside vertex can be spliced consecutively; gap two is forbidden on a longest witness and gap three gives a full-length rotation.
**Next Need:** Prove a packing/localization lemma: a family of d-1 pairwise contact-disjoint two-contact chords through one owner either contains such a gap<=3 bridge or all contact pairs obey a nested/separated interval normal form.

## [deletion_kills_the_strict_turan_layer_for_ell_at_least_six] Threshold-cover plus sharp deletion kills the strict Turan layer for ell at least six.
focus · theorem · proved · certified · supported
Parent: [induction_reconciles_turan_and_criticalcore_minimality]
**Given:** ["equality-layer threshold cover","sharp Turan deletion for H-D","rainbow path Turan bound"]
**Consumer:** ["grand Turan induction","dense-core all-special program"]
**Consequence:** For ell>=6 the strict m>dn layer is no longer the hard part: threshold structure forces so many one-D colored edges that the rainbow Turan bound is violated. The proof effort should concentrate on the equality layer m=dn.
**Next Need:** Formulate and prove the equality-layer classification S_ell at m=dn; connect zero/small-slack critical cores to equality configurations. Handle ell=4,5 from existing exact small-length results.

## [equality_obstructions_have_a_huge_outside_reservoir] Exact-density equality obstructions have a huge outside reservoir.
focus · lemma · proved · certified · supported
Parent: [induction_reconciles_turan_and_criticalcore_minimality]
**Consumer:** ["E_ell exact-density induction","top-rank ear/connector route"]
**Role:** equality-layer size separation
**Consequence:** Exact-density obstructions are the opposite of punctured-Steiner cores: every P_ell-free witness path leaves at least about 2ell outside vertices.
**Next Need:** Exploit the large outside reservoir. For a top-rank nonspecial witness, classify outside-vertex attachments to the path; either an outside dense component supplies a splice, or many outside vertices induce ears/chords on the path.

## [equality_forces_a_highdegree_lowpotential_ascending_source] Equality forces a high-degree low-potential ascending source.
focus · theorem · proved · certified · supported
Parent: [exact_turan_density_has_steiner_order_at_least_6d_plus_one]
**Given:** ["exact equality m=dn","P_ell-free","leave parity"]
**Consumer:** ["equality-layer induction","ascending-DAG route","potential-flow route"]
**Consequence:** Equality cannot be degree/potential uniform: it contains a >=3d+1 degree vertex below top potential, forcing 6/4/5 ascending source edges by residue.
**Next Need:** Exploit the 2c(v) distinct higher-potential terminals. If phi(v)=ell-2 they all have potential ell-1; use cumulative terminal capacities/potential cuts to bound such a fan. If phi(v) is lower, iterate upward in the ascending DAG and seek a branching-depth contradiction or a second high-source vertex.

## [maximum_path_omits_a_large_higherpotential_terminal_packet] Every universal-star maximum path omits a large higher-potential terminal packet.
focus · lemma · proved · certified · supported
Parent: [degreepotential_defect_exactly_into_clean_ascending_sources]
**Given:** ["pair-universal vertex","maximum endpoint path"]
**Consumer:** ["s=2 equality layer","common-entrance fan route"]
**Consequence:** Every maximum path at the universal source omits a large disjoint packet of higher-potential terminals; at top-minus-one source potential the omitted packet has size 12/8/10 by residue.
**Next Need:** Exploit repeated maximum paths at v. If the omitted top-potential packets vary, rotations generate many top vertices; if they overlap heavily, one source edge is clean for many distinct entrance rails, inviting a two-rail uncrossing contradiction.

## [p_lfreeness_forces_many_leave_branches_and_universal_vertices] At deficiency two, P_l-freeness forces many leave branches and universal vertices.
focus · theorem · proved · certified · supported
Parent: [two_universal_vertices_exactly_pay_for_leave_branching]
**Given:** ["Steiner deficiency s=2","P_ell-free"]
**Consumer:** ["s=2 equality classification","grand equality induction"]
**Consequence:** Small branching is impossible. Residue 0 needs at least three branch vertices and three pair-universal vertices; residue 2 needs at least two of each.
**Next Need:** Delete only a strategically chosen subset of branch vertices, using their leave degrees to improve the degree-loss estimate. Alternatively exploit the resulting multiple universal stars: in residues 0 and 2 there are at least 3 or 2 perfect star matchings, whose pairwise unions are alternating even cycles.

## [sharp_endpoint_threshold_strengthens_the_equality_leave_spike] Sharp endpoint threshold strengthens the equality leave spike.
focus · theorem · proved · certified · supported
Parent: [obstructions_force_a_leavedegree_spike_in_residues_zero_and_two]
**Given:** ["exact density","P_ell-free","leave parameter"]
**Consumer:** ["s=2 equality classification","leave-deficiency induction"]
**Consequence:** Improves the previous leave spike by two in every residue via the correct minimum-degree threshold 2ell-2.
**Next Need:** Combine the forced high leave-degree vertex with universal-star count. At s=2 the defect conservation ties each high branch to several pair-universal vertices; exploit those multiple stars jointly.

## [packet_deletion_has_an_exact_effectivecharge_formula] Packet deletion has an exact effective-charge formula.
focus · lemma · proved · certified · supported
Parent: [charge_and_density_deficit_obey_an_exact_deletion_recurrence]
**Given:** ["exact-density charge coordinates"]
**Consumer:** ["charge amplification","top-heavy packet deletion","matching/blocker structures"]
**Consequence:** Generalizes the target k_v>=2d: a packet can be deletable through the combined contribution of vertex charge and edges shared inside the packet.
**Next Need:** Apply to the top layer T in 76c961f0dc48. Lower-bound K(T)+A+2B, where A is the top-layer matching flow and B counts internal T-edges. If it reaches 2d|T|, delete T; otherwise the shortfall forces many one-T edges, which should feed a complementary low-layer packet or a path splice.

## [flow_becomes_an_exact_chargepotential_covariance_lower_bound] Quadratic potential flow becomes an exact charge-potential covariance lower bound.
focus · lemma · proved · certified · supported
Parent: [conjecture_is_exactly_a_leavecharge_amplification_to_2d]
**Given:** ["exact density","leave charge coordinates","quadratic potential-flow inequality"]
**Consumer:** ["charge amplification route","weighted potential-cut route"]
**Consequence:** Any equality obstruction must have quantitatively positive covariance between leave charge and excess endpoint potential.
**Next Need:** Combine (1) with lower bounds on average potential and upper bounds phi<=ell-1. Optimize over bounded a_v with k_v<=K<2d and zero-sum k. If the maximum possible covariance under K<2d is below the required right side, charge amplification follows.

## [negative_charge_at_level_p_pays_a_fixed_branching_surcharge] Negative charge at level p pays a fixed branching surcharge.
focus · lemma · proved · certified · supported
Parent: [flow_gives_a_levelwise_chargetosuperlevel_growth_inequality]
**Given:** ["exact-density charge layers"]
**Consumer:** ["charge amplification iteration"]
**Consequence:** Low-potential negative charge is much more expansion-expensive than top-layer negative charge.
**Next Need:** Partition negative charge by potential. Either a positive fraction lies below a chosen cutoff, forcing a large upper superlevel via this lemma, or most negative charge is top-heavy, forcing strong charge-potential covariance and allowing the weighted potential-cut inequalities to attack the top-heavy alternative.

## [every_longest_path_is_toppotential_except_for_a_constant_defect] In the stalled two-level state every longest path is top-potential except for a constant defect.
focus · theorem · proved · certified · supported
Parent: [charge_amplification_obstruction_has_only_two_potential_levels]
**Given:** ["stalled two-level state","top endpoint charge <=kappa+3"]
**Consumer:** ["top-heavy matching elimination","rotation expansion"]
**Consequence:** Every globally longest path is almost entirely contained in the top layer T; the low layer contributes at most 7,11,15,19 vertices according to top charge kappa,...,kappa+3.
**Next Need:** Apply terminal-tail blockers from the many S-sourced rank-L edges to such an almost-all-T path. Since only O(1) source vertices from S can lie on the path, almost every incident ascending edge at its top terminal must place its opposite T-terminal on the path, creating a near-saturated matching/chord system.

## [charge_forces_a_highdegree_top_star_with_many_single_blockers] Trapped-negative charge forces a high-degree top star and, without kappa+4 amplification, many full-rank single blockers.
focus · theorem · proved · pending · unchecked · pending
Parent: [four_or_all_negative_charge_is_trapped_one_level_below_the_top]
**Given:** ["trapped-negative two-layer charge state","incident capacity","color-class matching lower bounds","terminal-degree/double-blocker inequality"]
**Consumer:** ["charge amplification","charged spacing","Posa rotation"]
**Consequence:** The trapped-negative state forces at least 2kappa+5 negative sources and a top vertex of degree at least 2kappa+5; under no kappa+4 amplification, a maximum path at that vertex has at least 2kappa+1 full-rank single blockers.

## [orientation_is_an_almostregular_selfcolored_matching_graph] Balanced equality orientation is an almost-regular self-colored matching graph.
focus · theorem · proved · certified · supported
Parent: [obstructions_admit_a_balanced_doutregular_incidence_orientation]
**Given:** ["balanced incidence orientation"]
**Consumer:** ["grand equality induction","strong-rainbow rotation route"]
**Consequence:** Transforms the equality obstruction into an almost-regular proper self-coloring with d-edge matching color classes; charge becomes graph degree deficit from 2d.
**Next Need:** Prove a strong-rainbow path theorem exploiting all three extra properties simultaneously: each color has exactly d edges, color x avoids vertex x, and minimum degree is near 2d in the stalled branch. Generic rainbow bounds do not use these features.

## [equality_does_not_by_itself_give_outside_packet_expansion] Vertex-minimal equality does not by itself give outside packet expansion.
focus · lemma · proved · certified · supported
Parent: [cheap_outside_packets_force_a_lowdegree_survivor]
**Consumer:** ["E_ell induction","outside-reservoir Hall route"]
**Role:** logical fence
**Consequence:** The outside Hall assignment is presently unsupported; packet deletion can create the low-degree vertex predicted by the equality theorem.
**Corrects:** cheap_outside_packets_force_a_lowdegree_survivor
**Next Need:** Develop a lift-back lemma: if H-S has a degree<=d vertex after deleting an outside packet S, use the edges from that vertex into S to force a splice/path; or restrict to packets whose deletion provably preserves degree>d.

## [local_degree_would_close_the_zero_residue_equality_layer] Potential-oriented local degree would close the zero residue equality layer.
focus · lemma · proved · certified · supported
Parent: [density_would_reduce_equality_to_the_single_critical_residue]
**Given:** ["50b6278b9537 potential-oriented local bound","f7f7b7e447c8 equality ascending-mass arithmetic"]
**Consumer:** ["grand equality-layer induction"]
**Role:** conditional equality-layer residue reduction
**Consequence:** The local charged-degree conjecture implies 3-degeneracy of T_up and closes the ell≡0 mod3 equality layer.
**Next Need:** For ell≡2 mod3 need A<2n, so 3-degeneracy is insufficient. Seek a sharper decomposition using strict-rise edges (593637dc8b57) plus equal-potential terminal structure.

## [obstructions_have_average_endpoint_potential_d_plus_fivesixths] Exact-density nonspecial obstructions have average endpoint potential d plus five-sixths.
focus · lemma · proved · certified · supported
Parent: [forces_a_potentialdeficiency_surplus_of_upward_011_transitions]
**Given:** ["bbcfa1f0ff1d transition surplus/capacity"]
**Consumer:** ["E_ell equality layer","potential-level induction","ordered-shadow route"]
**Role:** equality-layer potential concentration
**Consequence:** Any exact-density nonspecial obstruction has average endpoint potential at least floor(2ell/3)+5/6, uniformly over ell mod 3.
**Next Need:** Use potential-level concentration together with the acyclic two-branch 0-1-1 orientation. Low levels must emit many transitions but have little total mass; seek a level-set expansion/flow contradiction or force a directed path of length ell.

## [potential_flow_forces_a_quadratic_degreepotential_constraint] Ascending potential flow forces a quadratic degree-potential constraint.
focus · lemma · proved · certified · supported
Parent: [forces_a_potentialdeficiency_surplus_of_upward_011_transitions]
**Given:** ["ascending source-to-terminal orientation","0e550ff0eadd terminal capacity","419519f0efa5 incident low-rank count"]
**Consumer:** ["E_ell equality layer","potential concentration/stability","weighted cut route"]
**Role:** equality-layer potential-flow inequality
**Consequence:** Eliminates ascending count A and imposes a quadratic global constraint coupling endpoint potentials to actual degrees. Near-uniform degree/potential saturation is impossible.
**Next Need:** Combine with average degree 3d and average potential >=d+5/6. Use convexity plus degree-potential correlation bounds, or derive that enough high-degree vertices must have unusually large potential. Feed that high-potential mass into superlevel-cut recursion.

## [strict_counterexamples_are_overwhelmingly_thresholddegree] Equality-layer strict counterexamples are overwhelmingly threshold-degree.
focus · lemma · proved · certified · supported
Parent: [induction_reconciles_turan_and_criticalcore_minimality]
**Given:** ["edge-minimal strict counterexample to equality-layer assertion"]
**Consumer:** ["grand Turan induction","threshold-core stability"]
**Consequence:** Sharp Turan excess plus threshold-cover structure makes the exceptional above-threshold vertex set O(|D|/ell)+O(1), pushing strict counterexamples close to regular threshold cores.
**Next Need:** Exploit the tiny exceptional path forest: delete/absorb its components into D, or show its attachments force a forbidden path; classify the equality layer m=d n separately.

## [turan_equality_layer_forces_residuedependent_ascending_mass] The sharp Turan equality layer forces residue-dependent ascending mass.
focus · lemma · proved · certified · supported
Parent: [induction_reconciles_turan_and_criticalcore_minimality]
**Given:** ["sharp equality m=floor(2ell/3)n","ascending-edge snake inequality"]
**Consumer:** ["equality-layer induction","ascending-edge density route"]
**Consequence:** Equality forces A>=3n,n,2n in residues 0,1,2 respectively; residues 0 and 2 can be closed by equality-layer ascending bounds much weaker than the full global conjecture A<=3n/2.
**Next Need:** Exploit minimum degree >=d+1 and equality-layer structure to prove A<3n (residue 0) and A<2n (residue 2); reserve the harder residue 1 for critical-core/near-spanning methods.

## [blocker_is_a_safe_rotation_of_the_fixed_nonspecial_last_edge] For a longest linear path ending in a nonspecial edge e, any single blocker through an opposite-end free vertex can be rotated to another longest path still ending in e through the same unique entrance.
focus · lemma · proved · certified · supported
Parent: [23_degree_bound_for_longest_paths_ending_in_a_nonspecial_edge]
**Given:** ["globally longest path ending in a fixed nonspecial edge","single blocker at either free opposite endpoint"]
**Consumer:** ["opposite-end degree conjecture","Minty/Pósa rotation-state graph"]
**Consequence:** single blockers at the far end are completely safe: unlike earlier terminal rotations, they never lose the fixed nonspecial last edge or its entrance label
**Next Obligation:** analyze double-blocker-only recurrent states; singles give genuine outgoing moves in the finite state graph

## [degree_bound_proves_the_maximumranknonspecial_branch_of_32l2] Assuming the opposite-end degree bound, any linear 3-graph with a maximum-rank nonspecial edge satisfies 3δ≤2L+2.
focus · lemma · proved · certified · provisional · obstructed
Parent: [23_degree_bound_for_longest_paths_ending_in_a_nonspecial_edge]
**Consumer:** maximum-rank-nonspecial branch of the global nonspecial-edge path-length inequality
**Limitation:** does not handle systems whose globally maximum-rank edges are all special
**Next Obligation:** combine with a dense-minimum-degree propagation lemma, or extend opposite-end control to lower-rank nonspecial edges

## [nonspecial_edge_can_have_no_lowdegree_opposite_endpoint] There is a 9-vertex linear 3-graph with maximum path length 3 and a maximum-rank nonspecial edge for which every longest ending path has both opposite-end free vertices of degree 3>2.
focus · lemma · proved · certified · supported
Parent: [23_degree_bound_for_longest_paths_ending_in_a_nonspecial_edge]
**Consumer:** ["opposite-end rotation route","global nonspecial-edge path-length route"]
**Role:** fence
**Consequence:** opposite-end degree control is false without a global minimum-degree hypothesis, even when the last nonspecial edge has global maximum rank
**Maximum Path Length:** 3
**Minimum Degree:** 1
**Refutes:** 23_degree_bound_for_longest_paths_ending_in_a_nonspecial_edge

## [oppositeend_degree_bound_fails_even_existentially] There is a 13-vertex linear 3-graph with maximum path length 6 and a maximum-rank nonspecial edge whose unique longest ending path has both opposite-end free vertices of degree 5>4.
focus · lemma · proved · certified · supported
Parent: [23_degree_bound_for_longest_paths_ending_in_a_nonspecial_edge]
**Consumer:** ["dense-core all-special strategy","location-sensitive Minty route"]
**Role:** counterexample
**Lesson:** Pósa rotation safety at the far end is true but cannot by itself force a low-degree state; ambient minimum degree away from the chosen longest path is essential
**Maximum Path Length:** 6
**Minimum Degree:** 3
**Refutes:** 75e5875cac45, including its existential weakening

## [reduces_to_two_exceptional_blockerpair_types_per_block_orbit] Matching-deletion specialness reduces to two exceptional blocker-pair types per block orbit.
focus · lemma · proved · certified · supported
Parent: [of_cyclic_sts13_preserve_rank_six_at_every_surviving_block]
**Given:** ["fb007f7c4b89 six endpoint-path families","matching deletion"]
**Consumer:** ["09b3a90c50a9 matching-deletion all-special calibration"]
**Consequence:** Reduces the remaining computational specialness assertion to two local exceptional deletion-pair types in each of the two block orbits.
**Next Need:** For one representative exceptional pair in each stabilizer orbit, construct an additional mixed-orbit spanning path with a different entrance that survives every compatible extension of the deleted matching.

## [generalize_the_p4_specialedge_lemma_to_dense_cores] Generalize the P4 special-edge lemma to dense cores
focus · proof_level · proposal · not_required · unchecked
Parent: [densecore_allspecial_conjecture]
**Given:** ["nonspecial = unique longest-path entrance label","minimum degree >2ell/3","source P4 special-edge pigeonhole argument"]
**Need:** sharp general attachment/rotation inequality
**Consumer:** dense-core all-special conjecture
**Fence:** equality delta=2ell/3 can fail

## [high_terminal_degree_forces_outside_singleblocker_expansion] High terminal degree forces outside single-blocker expansion.
focus · lemma · proved · certified · supported
Parent: [global_nonspecialedge_pathlength_inequality]
**Given:** ["globally longest path ending in a maximum-rank nonspecial edge","linearity"]
**Consumer:** ["020f694f8767 dense-core all-special conjecture","76ef6efb21e7 global nonspecial-edge path-length inequality","Pósa endpoint expansion route"]
**Consequence:** High terminal degree cannot hide entirely in double blockers: excess over L/terminal saturation is paid by distinct single blockers reaching outside the longest path.
**Next Need:** Convert many outside single blockers into many distinct safe rotations/endpoints, or show heavy collisions force alternating blocker cycles of the critical-order type.

## [an_early_endpoint_blocker_forces_oppositeendpoint_prefix_escape] An early endpoint blocker forces opposite-endpoint prefix escape.
focus · lemma · proved · certified · supported
Parent: [twohole_witnesses_force_linearly_many_threecenter_collisions]
**Given:** ["two-hole wrong-entrance witness","64823c8c54de cycle-ear surplus"]
**Consumer:** ["collision path-order expansion","SPANNING-TOP good residues"]
**Consequence:** Endpoint-color blocker contacts obey a monotone prefix-expansion rule: an early blocker at one free endpoint forces many blocker incidences from the other endpoint to cross beyond that prefix.
**Next Need:** Iterate the prefix-escape inequality between u and v. Seek a growth lemma for earliest-contact frontiers; if the frontier reaches within two cells of a hole-pair collision, apply de0c1d15d897 for the full lift.

## [gapthree_twohole_rotations_force_highpotential_omitted_vertices] In a lexicographically maximal two-hole wrong-entrance state, gap-two collisions are impossible and a gap-three cut at i forces both holes to potential at least max{i,s-i-2}.
focus · theorem · proved · pending · unchecked · pending
Parent: [twohole_witnesses_force_linearly_many_threecenter_collisions]
**Given:** ["two-hole collision splice","gap-three state rotation","position-sensitive path-vertex potential floor"]
**Consumer:** ["two-hole recurrence","high-potential hole splice route"]
**Consequence:** Gap-two collisions are forbidden and every gap-three rotation near an end forces both omitted vertices to have nearly full path potential.
**Next Need:** Use maximum paths ending at the forced high-potential holes to obtain a cross-splice or top-rank transfer.

## [witnesses_contain_linearly_many_genuine_twohole_collisions] Good-residue witnesses contain linearly many genuine two-hole collisions.
focus · lemma · proved · certified · supported
Parent: [twohole_witnesses_force_four_large_blocker_matchings]
**Given:** ["two-hole alternate wrong-entrance witness"]
**Consumer:** ["gap-two/gap-three collision route","SPANNING-TOP good residues"]
**Consequence:** Replaces mixed three-center collision density by a linear supply of collisions involving both omitted holes, precisely the configurations addressed by de0c1d15d897 and 387e8e7dba7c.
**Next Need:** Use path order on these collisions. Prove that if every hole-hole collision avoids gap two and all gap-three rotations are non-improving, the two hole matchings must localize/nest in a way incompatible with having 2m-O(1) common covered vertices.

## [either_give_twohole_witnesses_or_fall_exactly_onto_equality] Critical residue deletions either give two-hole witnesses or fall exactly onto equality.
focus · lemma · proved · certified · supported
Parent: [works_after_one_vertex_deletion_in_two_residue_classes]
**Given:** ["induction hypothesis at ell-1","spanning top-rank core","ell=1 mod 3"]
**Consumer:** ["critical-residue SPANNING-TOP induction","equality-stability route"]
**Consequence:** The unique numerically bad residue is reduced to an exact equality-threshold deletion obstruction. A deletion that does not yield an alternate entrance forces the ambient core to have exact minimum degree 2m+1 and exposes a minimum-degree vertex adjacent to the deleted far endpoint.
**Next Need:** Iterate over the two far endpoints and over fixed-edge rotations. Either some deletion becomes special and enters the four-matching two-hole route, or equality neighbors propagate through the rotation closure, potentially forcing a regular/equality design-like core.

## [paths_have_an_exact_alternating_blockermatching_defect_identity] Two-hole alternate paths have an exact alternating blocker-matching defect identity.
focus · lemma · proved · certified · supported
Parent: [works_after_one_vertex_deletion_in_two_residue_classes]
**Given:** ["spanning top-rank core on 2ell-1 vertices","an alternate-entrance (ell-2)-path supplied by deletion induction"]
**Consumer:** ["two-hole lift","SPANNING-TOP induction","alternating blocker stability"]
**Consequence:** The two omitted vertices generate exactly the same alternating-matching defect object as the order-12 terminal-star proof: two edge-disjoint matchings on the path vertices, with the number of open alternating chains given exactly by a degree-defect identity.
**Next Need:** Exploit path order. Show that an alternating component with suitably separated contacts gives an (ell-1)-edge lift preserving the alternate entrance; otherwise all components are path-local, forcing enough local congestion to violate linearity/minimum degree.

## [ears_are_thresholdsupported_in_an_edgeminimal_counterexample] Inductive path-hull ears are threshold-supported in an edge-minimal counterexample.
focus · lemma · proved · certified · supported
Parent: [inductive_pathhull_reduction_for_lowerrank_nonspecial_edges]
**Given:** ["62ebb49a0efa inductive path-hull degree drop","1e01357bf9c3 threshold cover"]
**Consumer:** ["EAR-TO-PROGRESS","critical-set induction","grand dense-core conjecture"]
**Consequence:** Lower-rank induction forces not arbitrary external attachments but a quantitative packet of threshold-supported ears/chords; when the low-degree path-hull vertex is outside D, the packet uses distinct degree-k vertices.
**Next Need:** Use the D-packet to force either a terminal-clean/rank-raising transfer or a second entrance. For low q the packet is large; combine with complete-capture 16d45ad1b1b2 and first-contact localization.

## [reduces_every_bad_path_hull_to_ears_or_a_spanning_toprank_core] Minimal-counterexample induction reduces every bad path hull to ears or a spanning top-rank core.
focus · lemma · proved · certified · supported
Parent: [inductive_pathhull_reduction_for_lowerrank_nonspecial_edges]
**Given:** ["induction on ell below the current parameter","vertex-minimal counterexample at ell"]
**Consumer:** ["grand-conjecture inductive attack","ear-expansion route","top-rank stability"]
**Consequence:** All nonspecial edges reduce to a local ear-rich path-hull obstruction, except a single sharply described base geometry: a spanning top-rank path on 2ell-1 vertices.
**Next Need:** Prove an ear-to-progress lemma: from the forced low internal-degree vertex and its external ears/chords, either create a second entrance into e, raise nonspecial rank, or construct P_ell. Separately analyze the spanning 2ell-1 top-rank core by defect/blocker stability.

## [human_counterexample_at_the_23_equality_threshold] There is an 11-vertex linear 3-graph of minimum degree 4 with no 6-edge linear path and a maximum-rank nonspecial edge whose three vertices all have degree 5.
focus · lemma · proved · certified · supported
Parent: [local_degree_bound_on_a_nonspecial_edge_is_false]
**Consumer:** ["dense-core all-special conjecture","global nonspecial-edge path-length route"]
**Role:** human counterexample and sharpness fence
**Consequence:** Gives a computation-free equality obstruction at ell=6 and a computation-free counterexample to the maximum-rank local degree bound.
**Proof Key:** P6-freeness follows from 11 vertices; one explicit P5 gives rank 5; the four-edge residual intersection graph rules out entrances 2 and 9.
**Refutes:** refuted_maximumrank_nonspecial_edge_degree_conjecture

## [lowdegree_endpoint_in_the_fixededge_rotation_closure] Conjecturally, the fixed-edge rotation closure of a maximum-rank nonspecial edge contains an opposite last vertex of degree at most ⌊2(L+1)/3⌋.
focus · theorem · conjecture · not_required · unchecked
Parent: [densecore_allspecial_conjecture]
**Given:** ["globally longest path ending in a maximum-rank nonspecial edge","safe fixed-edge single-blocker rotations"]
**Consumer:** ["global nonspecial-edge path-length inequality","dense-core all-special conjecture"]
**Fence:** ["single-path opposite-end degree bound is false","local degree bound on the nonspecial edge is false"]
**Next Need:** control reachable states dominated by double blockers; use length-preserving double splices or minimum degree at blocker vertices

## [minimalcounterexample_minimumdegree_reduction] Minimal-counterexample minimum-degree reduction.
focus · lemma · proved · certified · supported
Parent: [densecore_allspecial_conjecture]
**Given:** candidate linear bound |E(H)|<=d|V(H)| for a hereditary class
**Consumer:** all main-line attacks on the candidate bound
**Consequence:** work may begin under δ(H)>d

## [minimumdegree_allspecial_transfer_by_peeling] Minimum-degree all-special transfer by peeling.
focus · lemma · proved · certified · supported
Parent: [densecore_allspecial_conjecture]
**Given:** an all-special theorem above minimum degree k
**Consumer:** global Turan upper bound
**Specialization:** k=floor(2ell/3) gives leading coefficient 2/3

## [linear_triple_system_of_minimum_degree_three_is_allspecial] Every P4-free linear triple system of minimum degree three is all-special.
focus · theorem · proved · certified · supported
Parent: [n12_strict_twothirds_search_reduces_to_three_structural_classes]
**Given:** ["pathmaker lemma","connected cograph characterization","minimum degree at least three","linearity"]
**Consumer:** ["0bc3c18c2692 n<=12 reduction","d9ee4adc37d3 finite strict-threshold evidence","dense-core all-special conjecture at ell=4"]
**Consequence:** Completely closes Class I of the n<=12 finite search, and proves the dense-core all-special conjecture for ell=4.

## [classii_systems_have_no_rankfour_nonspecial_edge] Class-II systems have no rank-four nonspecial edge.
focus · theorem · proved · certified · supported
Parent: [strict_twothirds_allspecial_threshold_for_n12]
**Given:** ["1f16e26bffcf crossed terminal rectangle","4-regularity","12 vertices","linearity"]
**Consumer:** ["d9ee4adc37d3 Class II"]
**Consequence:** Completely eliminates maximum-rank nonspecial edges in Class II by a residual eight-vertex degree contradiction.
**Next Need:** Eliminate rank-three (or lower) nonspecial edges in Class II; then Class II is fully humanized.

## [classiii_nonspecial_edges_have_rank_at_least_four] Class-III nonspecial edges have rank at least four.
focus · lemma · proved · certified · supported
Parent: [strict_twothirds_allspecial_threshold_for_n12]
**Given:** ["Class III: 12 vertices and degree 5","terminal-degree bound"]
**Consumer:** ["d9ee4adc37d3 Class III","8a2c12515954 maximum-rank blocker normal form"]
**Consequence:** Eliminates all rank<=3 nonspecial edges in Class III; only rank 4 and rank 5 remain.
**Next Need:** Eliminate rank-4 nonspecial edges, then apply the one/two-chain blocker normal form to rank 5.

## [classiii_systems_have_no_rankfive_nonspecial_edge] Class-III systems have no rank-five nonspecial edge.
focus · theorem · proved · certified · supported
Parent: [strict_twothirds_allspecial_threshold_for_n12]
**Given:** ["d9c5b28c09a0 failed high-low pair lemma","b9277764ed94 rank >=4","09d85d61b8b0 rank-4 exclusion"]
**Consumer:** ["d9ee4adc37d3 finite strict-threshold evidence","0bc3c18c2692 Class III"]
**Consequence:** Closes the last rank-five branch; Class III is all-special by a purely human residual-one-hole argument.
**Proof Key:** Remove e, obtaining a 9-vertex 7-edge residual system of degrees 3,3,3,2^6. Terminal matchings cannot all suppress three-edge residual precursors; classify the mate pattern of x* and force a wrong terminal entrance.

## [classiii_systems_have_no_rankfour_nonspecial_edge] Class-III systems have no rank-four nonspecial edge.
focus · theorem · proved · certified · supported
Parent: [strict_twothirds_allspecial_threshold_for_n12]
**Given:** ["5cba7c87c67a alternating five-vertex terminal matching","5-regularity","12 vertices","linearity"]
**Consumer:** ["d9ee4adc37d3 Class III"]
**Consequence:** Eliminates the rank-four Class-III branch by an eight-required-versus-seven-available B-pair contradiction.
**Next Need:** Audit the repaired matching lemma and this short pair-count consequence independently.

## [correct_terminalblocker_localization_in_class_iii] Correct terminal-blocker localization in Class III.
focus · lemma · proved · certified · supported
Parent: [strict_twothirds_allspecial_threshold_for_n12]
**Given:** ["Class-III rank-five nonspecial edge","maximum P5","unique entrance"]
**Consumer:** ["8a2c12515954 alternating blocker topology","d9ee4adc37d3 Class III"]
**Consequence:** Correctly localizes terminal blockers: every non-early terminal edge is the unique outside-vertex single blocker at the penultimate cell.
**Correction:** Replaces the overstrong v1 claim that every blocker meets the first two precursor edges; the genuine penultimate j=p-1 exception is retained.
**Next Need:** Split the one/two-chain topology according to whether each single-blocker contact is early or penultimate.

## [defects_reduce_to_one_or_two_explicit_alternating_chains] Class-III blocker defects are explicit alternating chains, with late single blockers pinned to private(g4).
focus · theorem · proved · pending · unchecked · pending
Parent: [strict_twothirds_allspecial_threshold_for_n12]
**Consumer:** ["Class III rank-five nonspecial branch"]
**Consequence:** Class-III terminal defects are explicit one- or two-chain alternating structures, with every genuinely late single blocker pinned to private(g4).

## [every_classii_system_is_allspecial] Every Class-II system is all-special.
focus · theorem · proved · certified · supported
Parent: [strict_twothirds_allspecial_threshold_for_n12]
**Given:** ["d04b5b1b6d44 alternating terminal C6","8f5bb725421d rank-four exclusion","terminal-degree bound"]
**Consumer:** ["d9ee4adc37d3 finite strict-threshold evidence","0bc3c18c2692 Class II","dense-core ell=5 calibration"]
**Consequence:** Completely humanizes Class II: every 12-vertex 4-regular P5-free linear triple system is all-special.
**Next Need:** Only Class III remains from the finite strict-threshold search.

## [of_a_12vertex_5regular_linear_triple_system_has_a_spanning_p5] Every vertex deletion of a 12-vertex 5-regular linear triple system has a spanning P5.
focus · lemma · proved · certified · supported
Parent: [strict_twothirds_allspecial_threshold_for_n12]
**Given:** ["12 vertices","5-regular linear triple system","exact P5 extremal theorem"]
**Consumer:** ["d9ee4adc37d3 Class III","arbitrary STS(13) puncture specialness"]
**Consequence:** Every omitted vertex has a complementary maximum P5 spanning the other eleven vertices; replaces any need to enumerate paths in the Class-III systems.
**Next Need:** Use the twelve spanning deletion paths to force two longest-path entrance labels for every edge.

## [rankfour_nonspeciality_forces_a_crossed_terminal_rectangle] Class-II rank-four nonspeciality forces a crossed terminal rectangle.
focus · lemma · proved · certified · supported
Parent: [strict_twothirds_allspecial_threshold_for_n12]
**Given:** ["Class II: 4-regular P5-free linear triple system","rank-four nonspecial edge"]
**Consumer:** ["d9ee4adc37d3 Class II"]
**Consequence:** Any maximum-rank nonspecial edge forces a unique crossed 2x2 terminal rectangle, replacing arbitrary terminal-blocker behavior by a four-edge K4 gadget.
**Next Need:** Use the third path edge g3 and the remaining terminal edges through r to show the forced K4 either creates a P5 or a second entrance into e; separately eliminate rank-three nonspecial edges.

## [rankthree_nonspeciality_forces_an_alternating_terminal_c6] Class-II rank-three nonspeciality forces an alternating terminal C6.
focus · lemma · proved · certified · supported
Parent: [strict_twothirds_allspecial_threshold_for_n12]
**Given:** ["Class II: 4-regular P5-free system","rank-three nonspecial edge"]
**Consumer:** ["d9ee4adc37d3 Class II"]
**Consequence:** Compresses every rank-three nonspecial obstruction to a unique six-edge alternating terminal-cycle topology.
**Next Need:** Use the three remaining edges through each vertex of g1 (or the two additional x-edges) to show the alternating C6 forces a P5 or a second entrance.

## [at_least_one_classiii_terminal_matching_has_two_highlow_pairs] At least one Class-III terminal matching has two high-low pairs.
focus · lemma · proved · certified · supported
Parent: [reduces_to_a_ninevertex_residual_matching_obstruction]
**Given:** ["213f75e9692a nine-vertex residual matching model"]
**Consumer:** ["Class III rank-five branch","terminal_pair_forces_both_other_high_vertices_onto_the_low_mate"]
**Consequence:** Forces at least one terminal matching into the two-high-low-pair regime where the residual high-low obstruction applies twice.
**Next Need:** Apply d9c5b28c09a0 to the two high-low pairs and use the mutual no-P3 conditions to eliminate that regime.

## [classification_of_the_classiii_ninevertex_residual_obstruction] Triangle-type classification of the Class-III nine-vertex residual obstruction.
focus · lemma · proved · certified · supported
Parent: [reduces_to_a_ninevertex_residual_matching_obstruction]
**Given:** ["213f75e9692a residual model","d9c5b28c09a0 high-low obstruction"]
**Consumer:** ["Class III rank-five branch"]
**Consequence:** Reduces the last rank-five obstruction to three explicit residual triangle types, with exact high-neighbor pattern on every low.
**Next Need:** Eliminate the h=0 types (HHH+6 HLL and LLL+3 HLL+3 HHL), then the h=1 type (5 HLL+2 HHL), using the mutual no-P3 conditions from the terminal matchings.

## [restrictions_for_a_rankfour_nonspecial_edge_against_a_p5] Contact-gap restrictions for a rank-four nonspecial edge against a P5.
focus · lemma · proved · certified · supported
Parent: [strict_twothirds_allspecial_threshold_for_n12]
**Given:** ["rank-four nonspecial edge","a P5 avoiding one terminal"]
**Consumer:** ["d9ee4adc37d3 Class III rank-4 case","29221b7faca3 deletion-path lemma"]
**Consequence:** Correct path-relative restriction: terminal contacts cannot border two unused path edges, and no contact can border three. This is valid for every spanning deletion P5 without assuming it itself witnesses rank four.
**Correction:** Replaces the original overstrong four-word classification, which incorrectly inferred that this particular Q had to contain a rank-four witness.
**Next Need:** Combine the contact-gap restrictions across the spanning P5s supplied by deleting y and z, together with 5-regularity.

## [terminal_pair_forces_both_other_high_vertices_onto_the_low_mate] Failed high-low terminal pair forces both other high vertices onto the low mate.
focus · lemma · proved · certified · supported
Parent: [strict_twothirds_allspecial_threshold_for_n12]
**Given:** ["Class III residual 9-vertex system"]
**Consumer:** ["Class III rank-five branch"]
**Consequence:** Failure of a 3-edge precursor for a high-low terminal matching pair forces the low mate to spend residual adjacency on both other high vertices.
**Next Need:** Apply simultaneously to the two high-low pairs in a terminal matching; use the resulting forced high-low residual adjacencies to construct a terminal-entry P5 or contradict linearity.

## [modthree_strengthened_induction_with_an_equalitystructure_layer] A mod-three induction carrying both strict all-specialness above 2r/3 and an equality-structure classification at multiples of three would absorb the known one-degree induction failures.
focus · theorem · conjecture · not_required · unchecked
Parent: [pathstate_induction_for_the_grand_twothirds_conjecture]
**Given:** ["e6d318739fde path-hull induction","39ff078cd8f1 deletion arithmetic","order-11 equality counterexample","order-12 blocker structures"]
**Consumer:** ["densecore_allspecial_conjecture","induction_scheme_for_the_densecore_allspecial_conjecture"]
**Consequence:** Localizes the genuinely sharp part of the induction to the equality layer r divisible by 3, rather than treating all residues uniformly.
**Next Need:** Formulate and prove the weakest equality-topology theorem at parameters divisible by three sufficient to absorb both the path-hull equality case and the ell≡1 mod3 one-vertex deletion case.

## [decomposition_of_the_general_puncturedsteiner_residual] Colored-complement decomposition of the general punctured-Steiner residual.
focus · lemma · proved · certified · supported
Parent: [and_blocker_normal_form_for_puncturedsteiner_regular_systems]
**Given:** ["efe44a01f2dc universal punctured-Steiner residual"]
**Consumer:** ["punctured-Steiner all-special route","residual matching obstruction","colored-complement formulation"]
**Consequence:** Generalizes the d=5 pair-partition used in the final Class-III proof: the complement of the residual 2-shadow is exactly three terminal-star matchings plus the surviving leave matching.
**Next Need:** Exploit the colored leave graph together with the forbidden endpoint-path condition on F_y,F_z; seek a general expansion/alternating-cycle argument rather than classify residual triples.

## [extremaldeletion_transfer_for_puncturedsteiner_regular_systems] Extremal-deletion transfer for punctured-Steiner regular systems.
focus · lemma · proved · certified · supported
Parent: [and_blocker_normal_form_for_puncturedsteiner_regular_systems]
**Given:** ["d-regular linear triple system on 2d+2 vertices","exact extremal theorem for P_d on 2d+1 vertices"]
**Consumer:** ["punctured-Steiner all-special route","dense-core finite-to-general transfer"]
**Consequence:** Abstracts the order-11 G0 step: equality-profile incompatibility forces a spanning P_d in every vertex deletion of a punctured-Steiner regular system.
**Next Need:** Seek exact or stability results at order 2d+1 with extremal size d(2d-1)/3, or weaken equality-profile uniqueness to a degree-sequence stability statement.

## [localization_of_puncturedsteiner_terminal_defects] General early-or-penultimate localization of punctured-Steiner terminal defects.
focus · lemma · proved · certified · supported
Parent: [and_blocker_normal_form_for_puncturedsteiner_regular_systems]
**Given:** ["efe44a01f2dc maximum-rank punctured-Steiner setup"]
**Consumer:** ["ba1f1d706d77 saturated defect topologies","general punctured-Steiner all-special route"]
**Consequence:** Generalizes the corrected d=5 localization: a terminal single blocker is either early, or uniquely pinned to the private vertex of g_{d-1}; first contact at g_{d-2} is impossible.
**Next Need:** Eliminate the one-chain and terminal-triangle topologies by tracing alternating-chain endpoints against this early/penultimate dichotomy.

## [obstructions_have_one_of_two_saturated_defect_topologies] Punctured-Steiner maximum-rank obstructions have one of two saturated defect topologies.
focus · lemma · proved · certified · supported
Parent: [and_blocker_normal_form_for_puncturedsteiner_regular_systems]
**Given:** ["and_blocker_normal_form_for_puncturedsteiner_regular_systems","puncturedsteiner_terminal_defects_are_exactly_saturated"]
**Consumer:** ["punctured-Steiner all-special conjecture","general maximum-rank nonspecial-edge route"]
**Consequence:** Reduces the infinite punctured-Steiner obstruction to two saturated topologies: one open chain, or two open chains plus a canonical terminal 3-cycle.
**Next Need:** Prove an uncrossing/rotation lemma that eliminates either topology independent of d; this would generalize the entire n=12 Class-III proof.

## [puncturedsteiner_terminal_defects_are_exactly_saturated] Punctured-Steiner terminal defects are exactly saturated.
focus · lemma · proved · certified · supported
Parent: [and_blocker_normal_form_for_puncturedsteiner_regular_systems]
**Given:** ["efe44a01f2dc universal punctured-Steiner blocker normal form","437f531f4ad8 terminal defect accounting"]
**Consumer:** ["punctured-Steiner all-special route","alternating-chain uncrossing"]
**Consequence:** Shows exact saturation for every d: one single-blocker defect and one unused precursor defect per open alternating component.
**Next Need:** Exploit the saturated chain endpoints. A general proof need only understand how the unique single/unused endpoint pair(s) sit relative to the path cells; there are no additional terminal defects.

## [outsidevertex_deficiency_equals_open_blockerchain_deficiency] Outside-vertex deficiency equals open blocker-chain deficiency.
focus · lemma · proved · certified · supported
Parent: [deficiencys_residual_decomposition_around_a_nonspecial_edge]
**Given:** ["d-regular linear 3-graph on 2d+1+s vertices","maximum-rank nonspecial edge","globally longest d-edge path"]
**Consumer:** ["020f694f8767 dense-core all-special conjecture","76ef6efb21e7 global nonspecial-edge path-length inequality","general upper-bound critical-core analysis"]
**Consequence:** Quantifies the order-11/order-12 dichotomy: closed alternating blocker cycles occur exactly at zero outside deficiency; each outside-vertex single blocker opens one chain, with at most 2s chains total.
**Next Need:** Show that in a dense minimal counterexample, either the relevant maximum-rank nonspecial obstruction has small s, or many open chains/deficiency edges force a longer path by endpoint expansion.

## [shadow_formulation_of_the_puncturedsteiner_residual_obstruction] Strong-rainbow shadow formulation of the punctured-Steiner residual obstruction.
focus · lemma · proved · certified · supported
Parent: [puncturedsteiner_boundary_allspecial_conjecture]
**Given:** ["efe44a01f2dc residual normal form","e6c8f5225c3f colored-complement decomposition"]
**Consumer:** ["punctured-Steiner all-special conjecture","rainbow-shadow route","global_nonspecialedge_pathlength_inequality"]
**Consequence:** Recasts the infinite residual obstruction as a near-Hamilton strong-rainbow endpoint problem in an almost-complete properly third-vertex-colored graph: K_(2d-1) minus four matchings.
**Next Need:** Develop Pósa/rotation expansion for strongly-rainbow paths exploiting the Steiner triangle identity c(uv)=w iff {u,v,w} is a triple, rather than generic properly-colored graph bounds.

## [rankband_decomposition_for_the_grand_twothirds_conjecture] The grand two-thirds conjecture can be organized into low, boundary, and top rank bands, with each nonspecial state either eliminated locally or transferred to a strictly higher band.
focus · theorem · proposal · not_required · unchecked
Parent: [densecore_allspecial_conjecture]
**Consumer:** ["densecore_allspecial_conjecture","global_nonspecialedge_pathlength_inequality"]
**Role:** grand-conjecture strategy
**Consequence:** Replaces the vague maximum-rank reduction by a rank-band program: low ranks are rotation-rich and globally captured, q=delta has exact saturated fans, and only the top band requires punctured-Steiner-style stability.
**Next Need:** ["Find a monotone transfer invariant that raises q when a rotation-rich band fails to contradict.","Develop a path-relative defect identity for q<L analogous to U-S=2(L-d(v)).","Prove strong-rainbow/alternating-blocker stability in the top band."]

## [clean_entrance_replacements_stay_at_maximum_rank] Clean entrance replacements stay at maximum rank.
focus · lemma · proved · certified · supported
Parent: [refuted_maximumrank_nonspecial_edge_degree_conjecture]
**Given:** ["globally maximum-rank nonspecial edge","clean incident replacement at its unique entrance"]
**Consumer:** ["maximum-rank nonspecial-edge degree conjecture","dense-core all-special route"]
**Calibration:** c3e95f4ce77d exhibits large low-degree entrance clusters
**Consequence:** every clean entrance replacement is maximum-rank; if nonspecial it belongs to the same entrance cluster

## [twoterminal_rank_ascent_from_a_lowrank_nonspecial_edge] Two-terminal rank ascent from a low-rank nonspecial edge.
focus · lemma · proved · certified · supported
Parent: [densecore_allspecial_conjecture]
**Given:** ["nonspecial edge rank t","terminal degrees"]
**Consumer:** dense-core all-special and special-density routes
**Consequence:** below half the minimum degree, nonspecial edges branch to two distinct higher-rank neighbors

## [boosters_preserve_an_ascending_edge_at_minimum_degree_four] Affine-plane boosters preserve an ascending edge at minimum degree four.
focus · theorem · proved · certified · supported
Parent: [degree_four_does_not_eliminate_ascending_nonspecial_edges]
**Consumer:** minimum degree four eliminates ascending nonspecial edges
**Role:** fence
**Consequence:** fixed minimum degree 4 is insufficient; the live route must use the ell-dependent threshold δ>=floor(2ell/3)+1
**Path Free Parameter:** H_L is P_{L+7}-free with δ=4

## [minimumdegree_local_bound_implies_the_23_upper_bound] Minimum-degree local bound implies the 2/3 upper bound.
focus · lemma · proved · certified · provisional
Parent: [minimumdegree_local_ascendingneighbor_bound]
**Given:** minimum-degree local ascending-neighbor conjecture
**Consumer:** general 2/3-leading-coefficient theorem
**Consequence:** exact bound m<=2ell n/3

## [fixedhole_edge_through_the_alternate_hole_restores_full_length] In the canonical loss-one two-cycle, an external edge through the fixed hole and the alternate omitted vertex restores a full (q−1)-edge x-ending path.
focus · lemma · proved · certified · supported
Parent: [chords_either_bridge_or_collapse_to_one_twoedge_window]
**Given:** ["canonical loss-one two-cycle","completely external fixed-hole edge relative to P_1"]
**Consumer:** ["fixed-hole window state","sharp ascending-rank conjecture"]
**Consequence:** an external b-edge is trapped only if it also avoids the alternate omitted endpoint a-second; otherwise it restores the full q-1 entrance length
**Next Need:** analyze external b-edges disjoint from both P_0 and P_1

## [fixedhole_window_state_for_the_final_lossone_obstruction] The residual loss-one obstruction can be encoded by the fixed omitted vertex together with the minimal two-edge window containing all of its non-x one-contact chords.
focus · proof_level · proposal · not_required · unchecked
Parent: [chords_either_bridge_or_collapse_to_one_twoedge_window]
**Given:** ["fixed-hole residual dichotomy","corrected two-chord bridge","canonical loss-one two-cycle"]
**Consumer:** ["sharp ascending-rank conjecture","dense-core all-special conjecture"]
**Missing Obligation:** define a canonical move for the external-edge and two-edge-concentration branches and prove strict progress or contradiction on closed walks
**Motivation:** ["Minty-type state potential","Tucker/Hex only after finite-state reduction"]

## [double_blockers_form_an_alternating_pathcycle_system] The double-blocker matchings at the two terminals of a longest-path last edge form an edge-disjoint alternating path-and-even-cycle system.
focus · lemma · proved · certified · supported
Parent: [sharp_minimumdegree_lower_bound_conjecture_for_ascending_edges]
**Given:** ["globally longest path ending in a nonspecial maximum-rank edge","common precursor for the two terminal choices"]
**Consumer:** ["maximum-rank nonspecial-edge degree conjecture","two-terminal Pósa/blocker coupling"]
**Consequence:** the two terminal double-blocker systems compress to alternating paths/even cycles with exact defect count p=2L-2-B_y-B_z
**Next Obligation:** couple the open-chain defects to single-blocker rotations; many singles should expand endpoints, while few defects should force a cycle-topology contradiction

## [boundary_entrancepath_rotation_graph_has_no_sinks] Every state in the boundary fixed-target entrance-path rotation graph has positive outdegree, so the finite directed rotation graph contains a directed cycle.
focus · lemma · proved · certified · supported
Parent: [ear_and_forces_a_targetpreserving_maximum_rotation]
**Given:** ["ascending nonspecial rank-q edge","minimum degree at least q","entrance potential q-1"]
**Consumer:** ["flat-transfer recurrence","boundary q=delta attack","dense-core all-special conjecture"]
**Consequence:** every fixed target edge has a finite recurrent class of maximum entrance-ending paths preserving that target edge
**Next Need:** find a secondary statistic that cannot return unchanged around a rotation cycle; compare blocker locations or incoming-transfer memory

## [every_qstep_flat_transfer_walk_contains_a_labeled_linear_cycle] Every q consecutive flat equal-rank ascending transfers contain a labeled linear cycle of length at most q.
focus · lemma · proved · certified · supported
Parent: [in_a_flat_transfer_walk_lifts_to_a_labeled_linear_cycle]
**Given:** ["q consecutive flat rank-q ascending transfers","R_q has no rainbow P_q"]
**Consumer:** ["flat-transfer cycle reduction","dense-core all-special conjecture"]
**Consequence:** the residual flat-transfer obstruction is bounded: within q steps it closes into an explicit labeled linear cycle
**Next Need:** use short-cycle ear surplus for c<q-O(1), and equality/rail geometry when c is close to q

## [privatevertex_ear_surplus_on_a_short_linear_cycle] For a private vertex of a c-edge linear cycle in minimum degree q, the ear counts satisfy 2C₀+C₁≥2q−2c+1.
focus · lemma · proved · certified · supported
Parent: [in_a_flat_transfer_walk_lifts_to_a_labeled_linear_cycle]
**Given:** ["linear c-cycle","minimum degree q"]
**Consumer:** ["first-repetition transfer-cycle route","cycle-ear packing route","dense-core all-special conjecture"]
**Consequence:** an early transfer repetition forces substantial mobile-ear surplus at every private entrance; only cycles of length close to q can have near-minimal mobility
**Strengthens:** every_private_vertex_of_a_minimumdegree_cycle_has_a_mobile_ear

## [transfer_triangles_force_all_three_entrances_onto_every_rail] In a flat-transfer triangle of entrance-joint type, every entrance-to-entrance rail contains all three entrance vertices.
focus · lemma · proved · certified · supported
Parent: [in_a_flat_transfer_walk_lifts_to_a_labeled_linear_cycle]
**Given:** ["flat terminal transfer triangle","entrance-joint transfers","one-edge blocker memory"]
**Consumer:** ["short flat-cycle elimination","three-rail overlap route","dense-core all-special conjecture"]
**Consequence:** the c=3 repetition cycle is highly rigid: each q-2 rail contains all three low-potential entrances
**Next Need:** show three near-maximal rails on the same entrance triple force a q-edge endpoint path, a long global path, or a saturated theta normal form

## [every_private_vertex_of_a_minimumdegree_cycle_has_a_mobile_ear] Every private vertex of a linear q-cycle in minimum degree at least q has a noncycle ear meeting the cycle in at most one additional vertex.
focus · lemma · proved · certified · supported
Parent: [a_terminalclean_boundary_transfer_closes_a_qcycle]
**Given:** ["linear q-cycle","minimum degree at least q"]
**Consumer:** ["cycle-ear packing route","Aharoni-Haxell connector route","dense-core all-special conjecture"]
**Consequence:** every private cycle vertex exposes an edge with at most one further cycle contact
**Next Need:** pack many mobile ears with compatible outside resources/contact order and convert them into a path of length near 3q/2

## [flattransfer_cycle_chain_as_the_residual_boundary_obstruction] The residual flat-transfer obstruction consists of chains or cycles of equal-rank ascending terminal edges glued by extremal q-cycles.
focus · proof_level · proposal · not_required · unchecked
Parent: [a_terminalclean_boundary_transfer_closes_a_qcycle]
**Given:** ["far-end transfer lemma","equal-rank transfer terminal adjacency","transfer q-cycle equality geometry"]
**Consumer:** ["dense-core all-special conjecture","global nonspecial-edge path-length route"]
**Fence:** mobile ears alone do not automatically lengthen a path; clean ears are pendant and single-contact ears require global compatibility
**Missing Obligation:** eliminate a closed chain of flat equal-rank ascending transfers, or prove consecutive distinct transfer cycles splice past the 3q/2 scale

## [carry_a_oneedge_blocker_memory_into_the_next_longest_witness] In a flat equal-rank transfer e→f, every longest witness for f ending at the shared terminal must carry one of the two nonshared vertices of e in its final q−2 precursor edges.
focus · lemma · proved · certified · supported
Parent: [forces_motion_rank_progress_or_a_flat_terminal_adjacency]
**Given:** ["equal-rank flat transfer","terminal tail-blocker lemma"]
**Consumer:** ["flat-transfer cycle chain","dense-core all-special conjecture"]
**Consequence:** flat transfer has one-step memory: every next longest witness through the shared terminal contains the previous entrance or previous opposite terminal in its final q-2 precursor
**Next Need:** iterate this memory around a flat transfer cycle and show accumulated forced contacts either splice to a long path or violate linearity/minimum-degree saturation

## [indexgraph_normal_form_for_a_saturated_boundary_fan] The double blockers of a saturated boundary fan form a maximum-degree-two index multigraph with one path component when S=2 and two path components when S=3, all other components being cycles.
focus · lemma · proved · certified · supported
Parent: [saturated_blocker_fan_at_the_boundary_q]
**Consumer:** ["sharp ascending-rank conjecture","second-level Pósa expansion"]
**Consequence:** the no-safe-rotation boundary obstruction is encoded by cycles plus only one open chain when S=2, or two open chains when S=3
**Next Obligation:** exploit a cycle or one of the few chain endpoints to force a second-level rotation/alternative entrance using minimum degree at blocker vertices

## [through_a_common_entrance_or_form_a_rainbow_terminal_triangle] A flat Type-A boundary sink either has two branches with a common unique entrance or yields a rainbow terminal triangle of equal-rank ascending edges.
focus · lemma · proved · certified · supported
Parent: [lossone_case_a_forms_a_terminal_theta]
**Given:** ["loss-one Type-A sink","both clean branches flat equal-rank ascending"]
**Consumer:** ["branching flat-transfer system","potential-threshold terminal graph"]
**Consequence:** fully flat Type-A sink is either a two-way outward branch with common low-potential entrance or a rainbow triangle in R_q
**Next Need:** couple repeated Type-A branching with color repetition/blocker memory; a long simple branch must either become rainbow or expose repeated entrance colors that create spliceable hypergraph contacts

## [unsafe_clean_terminal_branches_are_special_or_do_not_drop_rank] A clean terminal branch from a deficiency-two path is either special or has rank at least the source rank q.
focus · lemma · proved · certified · supported
Parent: [lossone_case_a_forms_a_terminal_theta]
**Given:** ["loss-one clean terminal branch","unique-longest-entrance characterization"]
**Consumer:** ["special-edge density route","sharp ascending-rank conjecture","boundary loss-one analysis"]
**Consequence:** a trapped terminal clean edge either contributes a special edge immediately or transfers to an edge of rank at least the original ascending rank

## [private_single_blockers_can_occur_on_a_longest_endpoint_path] There is a linear 3-graph with a longest 3-edge path ending at x whose opposite endpoint supports two single-blocking edges with blockers in consecutive private slots.
focus · lemma · proved · certified · supported
Parent: [consecutive_private_single_blockers_need_not_force_an_extension]
**Consumer:** ascending-edge minimum-rank and Posa routes
**Role:** fence
**Invalidates Dependency:** proposed_47_minimumdegree_floor_for_ascending_edge_rank
**Lesson:** two single blockers cannot be spliced by reversing the prefix without accounting for inherited path intersections
**Refutes:** consecutive_private_single_blockers_need_not_force_an_extension

## [rotation_state_has_endpoint_deficiency_at_most_three] If a terminal-safe rotation state has no safe clean edge and no safe single blocker, then its endpoint deficiency satisfies δ−s≤3.
focus · lemma · proved · certified · supported
Parent: [deficiency_pays_for_clean_extensions_and_single_rotations]
**Consumer:** ["sharp ascending-rank conjecture","nonlocal double-blocker branch"]
**Consequence:** a double-blocker splice losing at least three edges cannot land in a local state with neither a safe extension nor a safe single rotation
**Next Obligation:** analyze the remaining loss-1/loss-2 chords or iterate the forced safe move after larger losses

## [paths_push_rotations_onto_maximumpotential_private_vertices] Lexicographically maximal fixed-edge paths push rotations onto maximum-potential private vertices.
focus · lemma · proved · certified · supported
Parent: [defectstability_route_to_the_twothirds_turan_upper_bound]
**Given:** ["fc1f69f1f481 safe fixed-edge opposite-end rotation","globally longest path"]
**Consumer:** ["grand dense-core induction","fixed-edge rotation closure","lowdegree_endpoint_in_the_fixededge_rotation_closure"]
**Role:** inductive rotation invariant
**Consequence:** Single-blocker mobility from a lexicographically maximal state can only move through internal private vertices that themselves have maximum potential L, creating recursive L-path subproblems.
**Next Need:** For an internal private vertex p with phi(p)=L, analyze a longest p-ending path against the two sides of P and either splice to length L+1 or recurse into a strictly shorter interval.

## [maximum_endpoint_paths_give_global_doubleblocker_compensation] Chosen maximum endpoint paths give global double-blocker compensation.
focus · lemma · proved · certified · supported
Parent: [snake_and_terminalcontact_accounting_route]
**Given:** ["snake digraph","one chosen maximum endpoint path at each vertex"]
**Consumer:** ["ascending-defect compensation","general upper-bound leading coefficient","potential-oriented charged-edge route"]
**Consequence:** every chosen-path double-blocking snake incidence pays one extra unit beyond the special-edge hinge
**Relation:** path-dependent strengthening of de68cff626e0; the latter identifies rank-gap incidences that are forced to be double blockers

## [general_snake_upper_bound_improved_to_ell2n] General snake upper bound improved to (ell-2)n.
focus · theorem · proved · certified · supported
Parent: [terminal_nonspecial_saturation_forces_doubleblocker_excess]
**Given:** ["terminal saturation/double-blocker lemma","chosen-path compensation 3a0d8866aba9"]
**Consumer:** ["grand upper-bound target","generalized snake program"]
**Consequence:** Unconditional n/2 additive improvement over the supplied general upper bound.
**Next Need:** A leading-coefficient improvement requires iterating the stateful snake idea so that high terminal capacity forces linearly many further rotations/contacts rather than only O(1) extra blocker units.

## [entrance_supports_at_most_four_typea_ladder_vertices] One exceptional entrance supports at most four Type-A ladder vertices.
focus · lemma · proved · certified · supported
Parent: [branch_or_form_an_exact_ladder_down_to_an_exceptional_entrance]
**Given:** ["1e24a8fe7b2a branch-or-ladder dichotomy","ca5f7dc68b1a weighted nonascending entrance budget"]
**Consumer:** ["near-floor Type-A stability","grand 2/3 route"]
**Consequence:** The entire nonbranching Type-A population is controlled linearly by the exceptional set: one exceptional entrance certifies at most four ladder vertices. Thus if |E|<=6eta n, ladder vertices occupy at most 24eta n.
**Next Need:** Control BRANCH Type-A vertices. If the branch population is also O(|E|), the near-seven-sixths structure has no room for a positive-density Type-A core when eta is small, yielding a uniform improvement above 7/6. Use the first rank r with n_r>=3 and the cumulative deficit below r to force either multiple exceptional entrances or a lower-level branching gate.

## [layer_is_either_upperhalf_or_exposes_an_exceptional_entrance] A Type-A branching layer is either upper-half or exposes an exceptional entrance.
focus · lemma · proved · certified · supported
Parent: [branch_or_form_an_exact_ladder_down_to_an_exceptional_entrance]
**Given:** ["1e24a8fe7b2a branch layers","a57057ab0001 Type-A source edges are ascending","a570b0ad0001 odd central window"]
**Consumer:** ["BRANCH population control","near-floor stability"]
**Consequence:** Branching cannot hide at low ranks inside the Type-A core. Every branch below the upper-half threshold directly exposes an exceptional entrance; branch layers with all-Type-A entrances must occur at rank at least ceil((p+4)/2).
**Next Need:** Split BRANCH vertices into low-branch and upper-half-branch. Bound multiplicity of low-branch exceptional entrances using ca5f7dc68b1a weighted nonascending budget. For upper-half branches, exploit that three Type-A entrances lie at potential r-1 >= roughly p/2 and combine with the special-level/rotation expansion machinery.

## [potential_levels_have_a_twolevel_predecessorcapacity_recurrence] Type-A potential levels have a two-level predecessor-capacity recurrence.
focus · lemma · proved · certified · supported
Parent: [a_special_subhypergraph_confined_to_individual_potential_levels]
**Given:** ["a57057ab0001 Type-A rank jump"]
**Consumer:** ["near-floor stability","potential-level induction","grand 2/3 route"]
**Consequence:** Every occupied Type-A level p needs at least 2p-5 distinct predecessor vertices at least two potential levels below, or exceptional. Consecutive Type-A levels cannot supply one another.
**Next Need:** Exploit special components inside each T_p. If one exceptional/lower source supplies many vertices of a same-level special component, its terminal matching crosses a connected 2..4-regular linear special component; seek a rainbow/alternating path inside that component to combine two source edges into a longer hypergraph path. A uniform bound on source multiplicity per special component would turn this recurrence into a linear exceptional-density gap.

## [linearly_many_neartoppotential_vertices_on_one_witness_path] Type-A rotation expansion forces linearly many near-top-potential vertices on one witness path.
focus · lemma · proved · certified · supported
Parent: [fan_has_at_least_p_minus_five_genuine_early_private_rotations]
**Given:** ["a9ce4e3cd5da genuine early private rotations","a51a7f9cff95 two-contact rotation"]
**Consumer:** ["Type-A Posa expansion","near-floor stability","grand 2/3 route"]
**Consequence:** Every Type-A vertex of potential p>=7 forces a linear-size packet (at least 2p-12 vertices) of near-top potential >=p-1 on a single rank-(p-1) witness path.
**Next Need:** Combine with near-floor Type-A prevalence: if most of this packet is Type A, recurse one level down; if many are exceptional, the packet itself gives a lower bound on exceptional mass. Iterating should yield a branching/exception dichotomy.

## [edges_at_a_typea_vertex_force_a_universal_twoentrance_gate] Exactly two top terminal edges at a Type-A vertex force a universal two-entrance gate.
focus · lemma · proved · certified · supported
Parent: [forces_rankpreserving_propagation_to_a_second_terminal_edge]
**Given:** ["0e550ff0eadd cumulative terminal rank bound","a1a7159e2c43 rank-preserving propagation"]
**Consumer:** ["Type-A equality classification","general potential-oriented local bound","grand 2/3 conjecture"]
**Role:** universal gate in the minimal top-rank Type-A fan
**Consequence:** Every Type-A vertex has at least two rank-(p-1) nonspecial terminal edges. If there are exactly two, all longest witnesses for both edges pass through one fixed penultimate gate containing their two entrances.
**Next Need:** Analyze the universal gate. If both entrance vertices are Type A, show the gate is a special rank-(q-1) edge in their common potential level. Then propagate these gates through the large Type-A special subhypergraph; alternatively show a third rank-q terminal edge is forced.

## [conflict_matching_sharpens_the_fixedentrance_incidentrank_bound] Full endpoint conflict matching sharpens the fixed-entrance incident-rank bound.
focus · lemma · proved · certified · supported
Parent: [firstedge_contacts_sharpen_the_eleventwelfths_bound]
**Given:** ["ascending last edge","linearity","fixed entrance phi(x)=q-1","419519f0efa5 ascending-incidence inequality"]
**Consumer:** ["grand general-length upper bound","Astra fixed-entrance route"]
**Consequence:** Adds the missing first-end conflict pair and yields a rank-parity-sensitive additive improvement.
**Next Need:** Determine the exact weighted cover number of the full singleton-contact conflict graph and whether double-contact geometry forces further savings.

## [windows_give_a_twoenvelope_local_bound_in_every_uniformity] Single-contact central windows give a two-envelope local bound in every uniformity.
focus · theorem · proved · certified · supported
Parent: [snake_and_unpaidedge_reduction_extend_to_arbitrary_uniformity]
**Given:** ["6c9c2c5a0fcb general-r contact multiplicities","a570a11f0001 fixed-entrance capacity","linearity and unique entrance of nonspecial edges"]
**Consumer:** ["general-r coefficient improvement","rank-gap shell","N_{0,1^{r-1}} unpaid-edge reduction"]
**Consequence:** For arbitrary r, multiplicity-paid terminal incidences obey a path-relative central-window envelope; combined with fixed-entrance capacity, only the rank ratio q/p above 8(r-1)/(10r-9) remains asymptotically dangerous to this local method.
**Generalizes:** 49080cbf1371 r=3 single-contact central window
**Next Need:** Attack the near-top band q/p>8(r-1)/(10r-9), especially q=p-O(1), by transferring fixed-entrance nonsingleton contacts into the chosen maximum-path excess multiplicity.

## [packets_obey_both_centralwindow_and_fixedcapacity_rank_profiles] Terminal-single packets obey both central-window and fixed-capacity rank profiles.
focus · lemma · proved · certified · supported
Parent: [assignment_forces_quadratic_offcenter_rank_in_every_uniformity]
**Given:** ["a570a11f0001 general-r fixed-entrance capacity","6af906e32265 single-contact central window","linearity"]
**Consumer:** ["general-r unpaid-edge packet bounds","minimum-terminal global reuse","dense near-top terminal families"]
**Consequence:** A dense terminal-single family cannot realize the central-window extremal rank profile all the way to its top: once the family passes the crossover index, fixed-entrance capacity forces faster rank growth.
**Next Need:** Use the combined profile, rather than either quadratic packet separately, in a global rank-budget or superlevel argument for minimum-terminal-assigned unpaid edges.

## [split_into_retained_pairs_or_external_threevertex_bridges] General-r switching hyperedges split into retained pairs or external three-vertex bridges.
focus · lemma · proved · certified · supported
Parent: [linear_anchortomaximum_symmetric_difference_in_every_uniformity]
**Given:** ["80e2e6b25cab general-r switching family","linearity"]
**Consumer:** ["general-r near-top uncrossing","switching-hyperedge path-order analysis","coefficient improvement beyond c_r"]
**Consequence:** The lost r=3 edgewise crossing matching is replaced by an exact dichotomy: either many genuine retained crossing pairs survive, or many disjoint 2-to-1 external bridges join anchor-only vertices to maximum-path-only vertices.
**Next Need:** Prove a path-order obstruction for one of the two large alternatives. The external-bridge branch is the genuinely new r>=4 phenomenon.

## [bound_from_ascending_incidence_and_fixedentrance_transfer] Global r-uniform bound from ascending incidence and fixed-entrance transfer.
focus · theorem · proved · certified · supported
Parent: [conflict_transfer_extends_to_linear_runiform_paths]
**Given:** ["dcf886f98a51 r-uniform fixed-entrance transfer","endpoint-path witness counting"]
**Consumer:** ["general r-uniform linear path Turan bounds"]
**Consequence:** The 3-uniform 43/48 coefficient is the r=3 specialization of (8r^2-10r+1)/(8r(r-1)).
**Next Need:** Exploit higher contact multiplicity or destroy the four-state extremal cycle to improve this coefficient.

## [windows_sharpen_the_astra_multiplicity_master_inequality] For the chosen maximum endpoint paths, the central-window bounds imply 3m <= 2S-n_+ +(1/2)sum_v B(v), with B(v) determined by the terminal rank profile.
focus · theorem · proved · certified · dependency_hold
Parent: [contacts_on_a_maximum_path_lie_in_one_central_rank_window]
**Given:** ["contacts_on_a_maximum_path_lie_in_one_central_rank_window","exact_transfer_solution_gives_a_ranksensitive_4348_bound","cleanminusdouble_identity_for_the_contact_snake"]
**Consumer:** ["post-43/48 optimization","rank-gap shell reduction"]
**Consequence:** Misaligned vertices pay the minimum of the short-anchor Astra cost and the maximum-path singleton-window cost; p>=2q-1 costs zero.
**Next Need:** Attack q=p-O(1), beginning with q=p-1.

## [doubled_rotation_packets_halve_the_endpointcongestion_penalty] Doubled rotation packets halve the endpoint-congestion penalty.
focus · theorem · proved · certified · dependency_hold
Parent: [singleblocker_cells_yield_two_toppotential_rotation_endpoints]
**Given:** ["465568d6d8dc doubled endpoint packet","a57007500001 exact defect identity","b032348c1a8a switching family"]
**Consumer:** ["post-43/48 coefficient improvement","global endpoint-congestion route"]
**Consequence:** The doubled packet halves the old congestion penalty: m<=19S/24+(K/6)n+o(S), rather than +(K/3)n.
**Next Need:** Prove an aggregate reuse bound sum_v |R(v)| <= K n_+ with K<(5/8-o(1))S/n_+. Pointwise bounded reuse is unnecessary. Split endpoint certificates by special versus nonspecial host edge; for nonspecial hosts all maximum rotations enter through the unique gate.

## [continuous_trianglelenssource_frontier_at_top_centers] Continuous triangle-lens-source frontier at top centers.
focus · theorem · proved · certified · dependency_hold
Parent: [cell_dispersion_forces_a_sourcemass_switchertriangle_tradeoff]
**Given:** ["b032348c1a8a dense switching theorem","9586a4d2317f one-eighth paid-cell theorem","98152151c212 cell-dispersion source-mass theorem"]
**Consumer:** ["global post-43/48 optimization","triangle/lens/source weighted charging","near-extremizer stability"]
**Consequence:** Exact continuous local frontier: D+Y >= L/8-o(L) and M/L^2 >= 5/16+(5/8-D/L)^2/4-o(1). Triangle concentration is the unique way to suppress source mass, and below density 1/8 it forces a complementary paid-output/lens packet.
**Next Need:** Find global capacities/reuse bounds for any two of the three currencies. The continuous form permits optimization against imperfect global bounds rather than requiring one branch to be eliminated completely.

## [is_exactly_internal_superlevel_edges_or_switcher_triangles] One-eighth payment is exactly internal superlevel edges or switcher triangles.
focus · theorem · proved · certified · supported
Parent: [center_pays_oneeighth_into_progress_or_local_obstruction]
**Given:** ["9586a4d2317f arbitrary-p one-eighth paid-cell theorem","321022a601f7 potential superlevel cut classification"]
**Consumer:** ["nested-core recursion","post-43/48 coefficient improvement","potential-level charging"]
**Consequence:** At threshold p, paid rotation outputs are exactly the output edges internal to V_p. Thus every low-defect p-center forces p/8-O(eta) units split between switcher triangles and distinct edges of H[V_p].
**Next Need:** Control reuse of these induced-core output edges across dangerous centers, or show the double-cell triangle alternative itself injects into cycle-rank/defect. This is now a pure nested-core/global-multiplicity problem.

## [from_one_interior_pair_force_a_superlevel_rotation_output] Two selected contacts from one interior pair force a superlevel rotation output.
focus · lemma · proved · certified · supported
Parent: [paid_mass_yields_onesixteenth_distinct_certified_switcher_edges]
**Given:** ["c8d14f7306ab cellwise injective selection of D+Y units","39d0d99258db characterization of Y by the rotation output lying in the vertex-rank superlevel"]
**Consumer:** ["same-terminal selected four-edge spacing","mixed-contact overlap states","counterexample-fence elimination"]
**Consequence:** The explicit four-edge fence with two doubly occupied flat cells cannot select both occupants of either cell. More generally, any selected double occupancy forces a distinct rotation output edge lying entirely in V_{>=p}.
**Next Need:** Combine with 6bea6cbb3741: mixed unique-entrance/opposite-terminal overlap at the equality boundary already forces a selected double or adjacent occupied pair with superlevel output. Extend this to every spacing-violating four-edge contact pattern, or isolate a same-type residual.

## [mass_lies_on_distinct_edges_with_strict_rankascent_certificates] One-sixteenth of near-extremal potential mass lies on distinct edges with strict rank-ascent certificates.
focus · lemma · proved · certified · supported
Parent: [paid_mass_yields_onesixteenth_distinct_certified_switcher_edges]
**Given:** ["c8d14f7306ab distinct paid-certified switchers","b032348c1a8a misaligned switching families","6205fe95ecf8 rotation-output rank lower bound"]
**Consumer:** ["post-43/48 rank-layer charging","strict rank-ascent congestion","weighted edge-rank flow"]
**Consequence:** Upgrades the distinct paid-edge family to explicit strict edge-rank ascent witnesses on a linear-sized set of distinct ascending edges.
**Next Need:** Bound how many distinct lower-rank certified switchers can feed the same higher-rank output layer. A weighted rank-layer inequality that charges each certificate by a positive function of phi(h)-phi(f) would convert this linear family into a strict global defect.

## [paid_edges_have_fundamental_cycles_inside_the_clean_u_11_graph] Paid edges have fundamental cycles inside the clean U_11 graph.
focus · theorem · proved · certified · dependency_hold
Parent: [011_edges_are_overwhelmingly_canonical_terminalcycle_chords]
**Given:** ["7ac951de82f4 distinct paid-certified source-clean U_11 edges","94c19ac52776 certified terminal-adjacency blocker lemma","S/n_+ -> infinity"]
**Consumer:** ["post-43/48 terminal-cycle coupling","paid 0-1-1 source-rail route","rank-flow along terminal cycles"]
**Consequence:** Omega(S) distinct paid edges can be chosen as minimum-rank fundamental-cycle chords in a maximum-rank forest of the cleaned U_11 graph itself; their entire canonical cycles remain ascending/source-clean/terminal-single, with blocker obligations on both sides.
**Next Need:** Split a clean fundamental cycle at a paid minimum-rank chord by equal-rank versus strict-rise neighbors. Equal-rank neighbors are candidates for flat-transfer/source-rail lens geometry; repeated strict rises around many paid chords should be charged to rank variation in the maximum-rank forest.

## [rankgap_families_force_a_disjoint_twotier_rank_packet] Minimum-terminal rank-gap families force a disjoint two-tier rank packet.
focus · lemma · proved · certified · supported
Parent: [on_the_paid_twoterminalgap_subclass_breaks_4348_saturation]
**Given:** ["220a14637b5f path-relative central-window packing","linearity","ascending nonspecial edges assigned to a minimum-rank terminal"]
**Consumer:** ["7e6abf77cbc5 paid two-terminal-gap local bound","post-43/48 global reuse route","vertex-rank superlevel packing"]
**Consequence:** A linear local rank-oriented family cannot be hidden in one resource: it simultaneously consumes k distinct vertices of rank at least p and a disjoint unique-entrance packet with a quadratic-in-k vertex-rank bonus.
**Next Need:** Globalize reuse of the two packets for the paid source-clean doubly-terminal-single subclass. If high-rank opposite terminals are heavily reused across assigned vertices, combine their terminal-capacity/blocker structure with unique-entrance-packet reuse; if either packet has low reuse, obtain expansion.

## [at_least_host_rank_plus_four_without_a_contacttype_hypothesis] Separated singleton contacts force rank sum at least host rank plus four without a contact-type hypothesis.
focus · lemma · proved · certified · supported
Parent: [singleton_contacts_force_rank_sum_at_least_host_rank_plus_four]
**Given:** ["49080cbf1371 singleton central-window localization","two contact-multiplicity-one ascending terminal edges with separated contact intervals"]
**Consumer:** ["U_11 color-terminal collision analysis","common-terminal singleton packing","paid strict-gap local analysis"]
**Consequence:** The rank-sum p+4 cost of separated singleton contacts is universal; entrance/terminal contact type is irrelevant.
**Next Need:** Replace uses of the mixed-only separated-contact lemma by this contact-type-free form. For two exact U_11 collision contacts, separated intervals now force adjacent rank sum at least r_i+3; overlapping intervals give a host linear 3-cycle.
**Strengthens:** singleton_contacts_force_rank_sum_at_least_host_rank_plus_four

## [forces_repeated_intersections_below_the_ranksum_threshold] Complete reciprocal transversality below the rank-sum threshold forces repeated intersections among opposite-terminal maximum paths.
focus · theorem · proved · pending · unchecked · pending
Parent: [singleton_contacts_force_rank_sum_at_least_host_rank_plus_four]
**Given:** ["singleton central-window bounds","terminal-singleness","linearity","Mantel theorem"]
**Consumer:** ["terminal-retained strict-gap branch","paid local congestion"]
**Consequence:** Low rank-sum reciprocal terminal paths cannot remain pairwise singly intersecting; four owners already force a repeated intersection and larger families force quadratically many.
**Next Need:** Exploit the forced repeated-intersection pair by path order/uncrossing without relying on automatic lens production.

## [types_have_rank_sum_p_plus_three_only_with_a_superlevel_output] Opposite singleton-contact types have rank sum p plus three only with a superlevel output.
focus · lemma · proved · certified · supported
Parent: [overlapping_singleton_contacts_have_two_exact_boundary_forms]
**Given:** ["e9fc907b07c9 separated mixed singleton-contact rank-sum bound","6bea6cbb3741 overlapping mixed singleton-contact classification with selected-certificate equality output"]
**Consumer:** ["same-terminal selected local congestion","four-edge spacing-or-progress reduction","contact-type packet decomposition"]
**Consequence:** After excluding the explicit superlevel-output event, every selected pair with opposite singleton-contact types has edge-rank sum at least p+4. Hence any low-rank-sum concentration is confined to one contact type.
**Next Need:** Use the p+4 cross-type barrier with the ordered ranks q_1<=...<=q_k. Either cross-type pairs are sparse by rank, or one contact type contains a large consecutive rank packet; attack the entrance-contact packet by source-path overlap and the opposite-terminal packet by reciprocal maximum paths.

## [strictgap_paid_mass_survives_as_clean_fundamentalcycle_chords] Local one-eighth strict-gap paid mass survives as clean fundamental-cycle chords.
focus · lemma · proved · certified · dependency_hold
Parent: [many_paidcertified_edges_have_strict_rank_gap_at_both_terminals]
**Given:** ["e6137a4bc902 local one-eighth paid-certified source-clean doubly-terminal-single families","9fba15f1495c center-incidence strict two-terminal edge-rank gap outside o(S)","94c19ac52776 terminal-adjacency blocker lemma","maximum-total-edge-rank spanning-forest exchange"]
**Consumer:** ["7e6abf77cbc5 sublinear local-congestion route","post-43/48 paid strict-gap terminal-cycle coupling","clean U_11 rank-flow and forest-branch packing"]
**Consequence:** The post-43/48 obstruction can be kept at full local density p/8-o(p) while simultaneously imposing strict rank gap, paid certification at the same center, clean U_11 membership, and a canonical minimum-rank fundamental-cycle blocker certificate.
**Next Need:** At a vertex v, partition H_v by the first forest edge on each chord's fundamental cycle. All chords in one branch block the same maximum terminal witness for that forest edge, while their paid-cell certificates are centered at v. Combine this shared-witness packing with 59c5795520ff and the paid-cell geometry; a sublinear branch bound or an expansion-versus-reuse dichotomy would close 7e6abf77cbc5.

## [flat_rotation_outputs_are_impossible_at_every_potential_level] Consecutive flat rotation outputs are impossible at every potential level.
focus · lemma · proved · certified · supported
Parent: [rank_rise_specialness_flat_orientation_or_a_highpotential_joint]
**Given:** ["6205fe95ecf8 general four-way rotation-output theorem"]
**Consumer:** ["multi-level switching iteration","post-43/48 progress packing"]
**Consequence:** The unpaid flat-output branch is an independent set on every maximum host path, not only at global maximum potential.
**Next Need:** Use with mixed X/U separation to force a uniform one-eighth paid branch at every low-defect misaligned center.

## [occupied_switching_cells_give_edgedisjoint_local_triangles] Distinct doubly occupied switching cells give edge-disjoint local triangles.
focus · lemma · proved · certified · supported
Parent: [lensfree_exact_dy_cell_payment_theorem]
**Given:** ["9a6be27912e0 double-cell triangle fact","one-contact switching family on one maximum path"]
**Consumer:** ["lens-free D+Y payment","post-43/48 cycle-packing route","certificate-centered local congestion"]
**Consequence:** The D part of local D+Y payment is already a cycle-packing currency with no constant-factor loss.
**Next Need:** Combine with D+Y>=p/8-eta-O(1). If D is a positive fraction of the selected payment, the center produces linearly many edge-disjoint local 3-cycles; otherwise most payment is in distinct paid single cells and must be charged through their progress outputs.

## [payment_splits_into_cycle_packing_or_distinct_progress_outputs] One-eighth certificate payment splits into cycle packing or distinct progress outputs.
focus · lemma · proved · certified · dependency_hold
Parent: [oneeighth_local_payment_at_lowdefect_misaligned_centers]
**Given:** ["614c7d2d181a lens-free one-eighth D+Y payment","9a6be27912e0 paid-cell output classification","33be3532211b edge-disjoint double-cell triangles"]
**Consumer:** ["certificate-centered local congestion","post-43/48 global charging"]
**Consequence:** The supported local payment mechanism reduces theorem-scale progress to exactly two quantitative global reuse problems.
**Next Need:** Globalize one of the two currencies across many low-defect centers: bound reuse of paid progress outputs, or charge the locally edge-disjoint triangle packets across centers. Either route now has linear local density with an explicit 1/16 coefficient.

## [a_multipleoverlap_pair_among_its_three_maximum_endpoint_paths] An all-top edge forces a multiple-overlap pair among its three maximum endpoint paths.
focus · lemma · proved · certified · supported
Parent: [nonascending_toprank_rotation_outputs_are_alltop_edges]
**Given:** ["57d5e4c71035 all-top rank-L rotation outputs","5854d853a44b unique-intersection alignment"]
**Consumer:** ["post-43/48 nonascending top-output branch","top-potential induced core","endpoint-lens packing"]
**Consequence:** Every all-top output edge forces a nontrivial overlap/lens state among maximum endpoint paths at its three vertices; the nonascending top branch cannot consist of three mutually simple endpoint states.
**Next Need:** Apply the multiple-overlap pair to many all-top output edges. Seek an injective or bounded-congestion choice of the resulting second common vertex/lens, or show repeated choices force a dense common maximum-path braid.

## [force_one_globally_linear_enriched_payment_currency] Near 43/48, one of terminal-retained, switcher-triangle, or superlevel-output currency has Omega(S) center-indexed mass, with clean minimum-rank fundamental-cycle certificates retained.
focus · theorem · proved · pending · unchecked · pending
Parent: [monotonepayment_charging_would_force_a_leadingcoefficient_gain]
**Given:** ["1000409 clean fundamental-cycle normalization","1000836 local U/triangle/superlevel-output trichotomy","near-extremal strict-gap paid extraction"]
**Consumer:** ["post-43/48 leading-coefficient improvement"]
**Consequence:** The leading-coefficient problem reduces to three globally linear, structurally enriched currencies with explicit asymptotic constants; no lower-order refinement is relevant.
**Next Need:** For each of the three enriched currencies, prove a global bounded-reuse or defect-charging inequality. Since one currency has Omega(S) center-indexed mass, it is enough to rule out linear global reuse in each branch separately. The fundamental-cycle certificate is available in every branch and should be used to control reuse.

## [oneeighth_into_terminal_retention_or_monotone_output_progress] Every low-defect misaligned center pays one-eighth into terminal retention or monotone output progress.
focus · theorem · proved · certified · supported
Parent: [toplayer_switching_packets_force_oneeighth_paid_structure]
**Given:** ["b032348c1a8a dense switching family","3c0ac5d646f1 flat outputs independent at every level","eac2e3da3eea clean joint exclusion","65894e91ed50 quantitative separation","6205fe95ecf8 output classification","465568d6d8dc doubled rotation endpoints"]
**Consumer:** ["post-43/48 rank-flow route","multi-level switching stability","potential-superlevel recursion"]
**Consequence:** At every low-defect misaligned center, at least one-eighth of the host scale is forced into a bounded-reuse terminal-retained edge or a monotone rank/special/superlevel output.
**Next Need:** Globalize the paid branches across potential levels. U-type switchers have hyperedge multiplicity at most two across centers and obey c48823eea604. Strict-rank-rise outputs should be charged across superlevel cuts; special outputs feed the special-edge hinge; equal-rank nonascending outputs remain entirely inside V_{>=p} and should recurse into the superlevel core.

## [edge_manufactures_an_endpoint_lens_on_the_maximum_path] Every gap-one switching edge manufactures an endpoint lens on the maximum path.
focus · lemma · proved · certified · supported
Parent: [have_linear_symmetric_difference_and_a_dense_switching_matching]
**Given:** ["gap-one switching matching","maximum endpoint path P"]
**Consumer:** ["r=3 post-43/48 improvement","minimal-lens uncrossing"]
**Consequence:** Near saturation forces about 5q/8 distinct endpoint labels on one maximum path, each supporting a second maximum path and hence a lens with P.
**Next Need:** Choose elementary endpoint lenses for all retained vertices. Prove a clean endpoint-lens balance lemma (the endpoint analogue of 390e818020e1), then use no-piercing/laminarity to bound how many distinct balanced lenses can attach to one maximum path without forcing extra intersections or multiplicity.

## [only_odelta_slots_for_onerankhigher_nonspecial_terminal_edges] Near saturation leaves only O(delta) slots for one-rank-higher nonspecial terminal edges.
focus · lemma · proved · certified · supported
Parent: [into_anchor_slack_foreign_lowrank_edges_and_maximumpath_doubles]
**Given:** ["f6c9ded0ae63 gap-one local slack","88db9b4e8337 fixed-entrance unused-slot bound","1c8aac8aa4dd downward-complete canonical source rail","linearity"]
**Consumer:** ["post-43/48 top-layer output branch","all-top nonspecial edge packing","potential-superlevel recursion"]
**Consequence:** A gap-one terminal star that nearly saturates the 11/8 fixed-entrance system has only O(delta) room for nonspecial competitors one rank above the anchor. Exact saturation permits at most one.
**Next Need:** Apply at global top L with q=L-1. A nonspecial all-top rank-L edge has two top-potential terminal incidences. If those terminals are low-defect gap-one vertices, each such incidence consumes one of only O(delta) one-rank-higher slots. Combine this with the Y-output branch and control output-edge reuse across centers; special top-rank outputs remain the parallel branch.

## [endpoint_lenses_yields_two_new_maximum_hostendpoint_paths] A clean intersection of crossing balanced endpoint lenses yields two new maximum host-endpoint paths.
focus · lemma · proved · certified · supported
Parent: [endpoint_lenses_on_one_maximum_path_must_intersect_off_the_host]
**Given:** ["two crossing balanced endpoint lenses on one maximum host path","clean auxiliary-side intersection"]
**Consumer:** ["gap-one endpoint-lens packing","lexicographic maximum-path state graph"]
**Consequence:** Crossing lenses cannot remain a static obstruction: their forced auxiliary intersection produces two alternative maximum v-paths by exact cross-splicing.
**Next Need:** Choose P lexicographically among maximum v-paths to maximize retained switching endpoints and/or anchor overlap. Show one of the two cross-spliced maximum paths improves this score unless the switching endpoints satisfy a rigid rectangle equality pattern. This can force the large lens family to become laminar.

## [its_omitted_entrance_or_the_host_endpoint_on_every_maximum_path] A terminal-retained switching endpoint recaptures its omitted entrance or the host endpoint on every maximum path.
focus · lemma · proved · certified · supported
Parent: [linearly_many_balanced_endpoint_lenses_on_one_maximum_path]
**Given:** ["gap-one switching edge","retained endpoint is the opposite terminal"]
**Consumer:** ["gap-one endpoint-lens packing","terminal/entrance type split"]
**Consequence:** Every auxiliary maximum path at a terminal-retained switching endpoint is forced to recapture either the omitted entrance mate or the common host endpoint v. Terminal-retained lens sides cannot behave as unconstrained off-host detours.
**Next Need:** Split the large switching family into entrance-retained and terminal-retained edges. If terminal-retained density is linear, use the recapture dichotomy plus linearity to force many auxiliary paths through v or many distinct omitted entrances. If entrance-retained density is linear, use canonical entrance rails and crossing-lens conflict geometry.

## [no_balanced_internal_lens_and_at_most_one_internal_lens_total] Overlap-maximal gap-one path pairs have no balanced internal lens and at most one internal lens total.
focus · lemma · proved · certified · supported
Parent: [path_pairs_have_at_most_one_unbalanced_elementary_lens]
**Given:** ["gap-one q versus q+1 endpoint paths","overlap-maximal choice of maximum path","deficiency-one lens budget"]
**Consumer:** ["gap-one switching matching","post-43/48 path uncrossing"]
**Consequence:** After choosing the maximum path to maximize anchor-edge overlap, all balanced internal lenses disappear and at most one unbalanced internal lens remains. The large switching matching must therefore live on an essentially single-defect Q/P geometry.
**Next Need:** Classify the remaining overlap-maximal geometry including the initial prefix fork. Show the q/8 cross-period switching edges cannot all connect retained common vertices to omitted vertices inside the one defect region/prefix without producing an endpoint-preserving rotation that increases Q-overlap.

## [fixedentrance_incidence_coefficient_is_asymptotically_sharp] The eleven-eighths fixed-entrance incidence coefficient is asymptotically sharp.
focus · theorem · proved · certified · supported
Parent: [has_a_fivefourths_integrality_gap_over_fractional_packing]
**Given:** ["explicit path plus incident-edge construction","human classification by number of v-incident edges on a linear path"]
**Consumer:** ["43/48 strengthening attempt","fixed-entrance local capacity","multiple-path refinements"]
**Consequence:** The 11/8 leading local coefficient is attained asymptotically by actual hypergraphs; universal J_q bounds cannot improve it.
**Fence:** Does not prove global 43/48 sharpness or a sharp bound on ascending-only terminal incidence counts.
**Proof Key:** Repeat singleton pattern (b,z),(b),empty,empty; pair remaining internal positions with translated copies four k indices away. All paths have length at most q; no q-path ends at the fixed entrance.

## [nearequality_forces_linearly_many_crossperiod_double_contacts] Near-equality forces linearly many cross-period double contacts.
focus · lemma · proved · certified · supported
Parent: [near_equality_has_a_periodic_fourcell_contact_normal_form]
**Given:** ["r=3 periodic near-equality contact normal form","gap-one switching matching"]
**Consumer:** ["post-43/48 improvement","gap-one path uncrossing","long-range double-contact geometry"]
**Consequence:** Near equality does not merely force many doubles: linearly many doubles must cross the boundaries of the period-four contact blocks. In a gap-one near-extremizer, q/8-O(delta) of these are genuine anchor-to-maximum switching edges.
**Next Need:** Exploit cross-period switching edges on the deficiency-one Q/P decomposition. Their omitted Q-vertex and retained common vertex cannot both stay inside one local periodic cell; combine with 32ea928e6ffd to force repeated crossings of balanced lenses or many distinct maximum rotations.

## [shortcut_map_and_amplification_program_from_astra_direct_proof] The recovered direct proof suggests improving the post-capacity step by strengthening path-contact counting with ascendingness; the existing conflict-graph mechanism already reaches the 43/48 coefficient.
focus · theorem · conjecture · not_required · unchecked
Parent: [contactconflict_graph_improves_the_leading_coefficient_to_4348]
**Given:** ["Astra recovered direct proof"]
**Consumer:** ["general upper-bound strategy","proof architecture"]
**Consequence:** Identifies the earliest shortcut, removes unnecessary intermediate machinery from the 11/12 route, and isolates three genuine avenues for improving beyond 43/48.
**Next Need:** Audit caeba14e4f6b. Then test additional ascending-label constraints against the 3/4-cycle extremal pattern of the local contact transfer process; any reduction in that cycle mean immediately improves 43/48.

## [nonspecial_terminal_vertices_have_density_at_most_three_eta] Near the seven-sixths floor, full-rank nonspecial terminal vertices have density at most three eta.
focus · lemma · proved · certified · supported
Parent: [terminal_of_rank_q_reduces_the_entire_incident_lowrank_capacity]
**Given:** ["a570ca900001 full-rank nonspecial terminal capacity","9fe13355ecae local weighted defect","global slack identity"]
**Consumer:** ["near-floor stability","charged-edge obstruction control","grand 2/3 route"]
**Consequence:** Near the seven-sixths floor, full-rank nonspecial terminal behavior is twice as expensive locally as Type A. Only 3eta n vertices can support it; elsewhere every nonspecial terminal edge drops rank by at least one.
**Next Need:** Combine with a57057ab0001: on the large Type-A core the drop is already known, while this lemma controls the remaining near-floor full-rank terminal sites. Refine the exceptional decomposition by separating full-rank sites from other non-Type-A defects.

## [upper_bound_improved_to_ell116n_by_terminalsnake_localization] General upper bound improved to (ell-11/6)n by terminal-snake localization.
focus · theorem · proved · certified · supported
Parent: [nonspecial_terminal_snake_incidences_have_cumulative_bound_2q3]
**Given:** ["special-edge hinge 699ece64f652","terminal cumulative lemma above"]
**Consumer:** ["grand upper-bound target","generalized snake program"]
**Consequence:** Unconditional additive n/3 improvement of the current internal general upper benchmark.
**Next Need:** Use deeper blocker/contact multiplicity or stateful snakes to turn the constant improvement into a leading-coefficient improvement.

## [between_an_earlier_single_blocker_and_a_later_clean_entrance] Quantitative separation between an earlier single blocker and a later clean entrance.
focus · lemma · proved · certified · supported
Parent: [reconstruction_of_astra_1112_cleancontact_route]
**Given:** ["maximum endpoint path","earlier arbitrary single contact","later clean entrance contact"]
**Consumer:** ["p=2q-3 corrected rank-pair block","Astra conflict matching"]
**Role:** quantitative clean-contact separation
**Consequence:** The nearby-contact splice has a quantitative slack form: a later clean entrance must lie p-rank+O(1) cells after any earlier single contact. At p=2q-3 and high rank q+1, the required gap is q-1 for a private entrance and q-2 for a joint entrance.
**Next Need:** Apply to the seven-slot p=2q-3 witness window. It immediately removes the rightmost entrance-only slots F,G from any four-single packing; continue shrinking the remaining A-E states, then handle all-terminal-only states with the terminal-order inequalities.

## [positions_apart_sum_to_at_least_the_host_potential_plus_five] Terminal-only singleton ranks two positions apart sum to at least the host potential plus five.
focus · lemma · proved · certified · supported
Parent: [singleton_ranks_sum_to_at_least_the_host_potential_plus_four]
**Given:** ["three ordered terminal-only singleton ascending edges"]
**Consumer:** ["ascending-only singleton transfer","near-half-rank terminal-only packing"]
**Consequence:** Terminal-only ranks obey a stronger distance-two constraint: positions two apart pay p+5 rather than p+4. Thus three rank<=q terminal-only singles are impossible already at p>=2q-4.
**Next Need:** Iterate the ordered-contact inequalities as a weighted sequence problem. Determine the minimum possible average rank of a long terminal-only singleton family; combine that rank mass with the exact rank-sensitive terminal count rather than replacing every rank by q.

## [terminalonly_contact_intervals_are_squeezed_from_both_ends] Separated terminal-only contact intervals are squeezed from both ends.
focus · lemma · proved · certified · supported
Parent: [earlier_terminalonly_contact_is_bounded_by_the_later_edge_rank]
**Given:** ["two terminal-only single-contact ascending edges with separated contact intervals"]
**Consumer:** ["0904073d4cbf Astra route","U-edge rank clustering"]
**Consequence:** Separated U-contacts are simultaneously constrained by the later rank from the left and the earlier rank from the right. Dense terminal-only families must therefore either have near-top ranks or heavily overlap path-edge cells.
**Next Need:** Count overlapping contact intervals: since every path edge has only three vertices and distinct U-edges have distinct opposite terminals, heavy overlap has bounded multiplicity. Combine with the two-sided squeeze to bound U outside a short near-top rank band.

## [terminal_chords_satisfy_the_threehalves_pathslot_bound] Clean entrance-only ascending terminal chords satisfy the three-halves path-slot bound.
focus · lemma · proved · certified · supported
Parent: [distancetwo_private_clean_entrance_contacts_are_incompatible]
**Given:** ["c265aa8ded39 distance-two private clean-contact exclusion"]
**Consumer:** ["0904073d4cbf Astra 11/12 reconstruction","clean-contact packing"]
**Consequence:** This rigorously recovers the screenshot coefficient 3/2 for the clean entrance-only subclass: joint slots contribute at most p-2 and distance-two pairing cuts the p private slots to at most ceil(p/2)+1.
**Fence:** This does NOT yet imply t_up(v)<=3phi(v)/2 or A<=3/4 sum phi. Terminal-only single contacts and double contacts remain to be globally charged/compensated.
**Next Need:** Show that after a suitable global choice/rotation of maximum endpoint paths, every ascending edge can be charged to one clean entrance-only terminal state with bounded multiplicity, or prove a global clean-minus-double inequality that absorbs terminal-only U states via their nondecreasing endpoint rotations.

## [entrance_forbids_the_immediately_preceding_firstcontact_cell] A clean joint entrance forbids the immediately preceding first-contact cell.
focus · lemma · proved · certified · supported
Parent: [reconstruction_of_astra_1112_cleancontact_route]
**Given:** ["maximum endpoint path","earlier arbitrary single contact","later clean joint entrance"]
**Consumer:** ["0904073d4cbf Astra 11/12 reconstruction","cell-level clean-contact packing"]
**Role:** joint clean-contact packing
**Consequence:** If a clean entrance first appears as the joint g_{j+1}∩g_{j+2}, then the entire first-contact cell at index j must be empty of other single-contact ascending terminal edges.
**Next Need:** Combine with 08f894b8cb5e in an oriented-cell packing. Private clean entrances forbid the cell two indices earlier; joint clean entrances forbid the immediately previous cell. Quantify collision of these hole charges and then isolate the residual terminal-only mass.

## [forbids_every_private_single_contact_two_positions_earlier] A clean private entrance forbids every private single contact two positions earlier.
focus · lemma · proved · certified · supported
Parent: [reconstruction_of_astra_1112_cleancontact_route]
**Given:** ["maximum endpoint path","earlier arbitrary single private contact","later clean private entrance contact"]
**Consumer:** ["0904073d4cbf Astra 11/12 reconstruction","0-1-1 terminal packing"]
**Role:** mixed clean-contact packing
**Consequence:** A private clean entrance at index j+2 forces the private slot at index j to be completely unused by any other single-contact ascending terminal edge, not merely unused by another entrance-visible edge.
**Next Need:** Use weighted parity-chain packing: each clean private entrance consumes its own slot plus forbids the preceding same-parity private slot. Combine with terminal-only rank/interval squeeze to bound the remaining occupied slots.

## [joint_or_twovertex_contact_with_the_low_entrance_rail] Every high competitor in the q,(q+1)^3 pattern has a private-singleton, joint, or two-vertex contact with the low entrance rail.
focus · lemma · proved · certified · supported
Parent: [pattern_forces_tailterminal_or_crosssplice_obstructions]
**Given:** ["canonical low rank-q entrance rail","rank-(q+1) common-terminal competitor","repaired c448268039f5 singleton-position localization"]
**Consumer:** ["q,(q+1)^3 two-rank block","Astra 11/12 route"]
**Consequence:** Each high competitor is either a private singleton chord at j in {2,...,q-3} union {q-1}, or a two-contact chord using both non-v vertices. The last-edge singleton is an explicit unresolved residue.
**Next Need:** Resolve the surviving final-edge singleton j=q-1 or carry it through the three-chord packing. For double-contact chords, bound their span using path splices, then combine three pairwise-disjoint chords with the distance-two singleton exclusion.

## [contact_is_bounded_from_the_right_by_the_earlier_edge_rank] A later terminal-only contact is bounded from the right by the earlier edge rank.
focus · lemma · proved · certified · supported
Parent: [single_contacts_avoid_the_first_and_penultimate_rail_edges]
**Given:** ["two terminal-only single-contact ascending edges on one maximum terminal path"]
**Consumer:** ["half-rank four-slot classification","Astra local 3/4 route"]
**Consequence:** Together with df8ad4c65be0, two terminal-only contacts are squeezed simultaneously from the left and right. The formulation uses last-occurrence coordinates and therefore avoids the joint off-by-one issue.
**Next Need:** Apply at p=2q-2 to the four central high-edge witness slots. Two absent-entrance rank-(q+1) competitors must have slot pattern {left joint,right private} or {left joint,right joint}; three absent entrances are impossible.

## [graph_of_arbitrary_commonterminal_source_rails_is_trianglefree] The simple-intersection graph of arbitrary common-terminal source rails is triangle-free.
focus · theorem · proved · certified · supported
Parent: [commonterminal_ascending_edges_are_pairwise_intersecting]
**Given:** ["universal pairwise intersection of common-terminal canonical source rails","universal aligned-joint rigidity","downward-complete rail-edge contacts"]
**Consumer:** ["ascending-only fixed-entrance improvement","post-43/48 strengthening","source-rail lens density"]
**Consequence:** A common-terminal ascending family of size k forces quadratic multiple-overlap mass: asymptotically at least k^2/4 rail pairs share two or more vertices. The simple-intersection pairs form a triangle-free graph.
**Next Need:** Convert quadratic multiple-overlap pairs into a linear local deficit. Analyze concentration on common gates: either many pairs use genuinely distinct elementary lenses, or many rails share the same two gates, which should itself force a common balanced segment or a splice contradiction.

## [maximum_path_pairs_admit_no_clean_complementary_switch] Overlap-maximal maximum path pairs admit no clean complementary switch.
focus · lemma · proved · certified · supported
Parent: [force_a_macroscopic_lensfree_overlap_of_neartop_maximum_paths]
**Given:** ["two maximum endpoint paths","Q chosen overlap-maximal relative to R","complementary endpoint-preserving clean switch"]
**Consumer:** ["two-path braid classification","clean alternating-cycle elimination","post-43/48 overlap rigidity"]
**Consequence:** All clean braid obstructions can be attacked through one criterion: if the Q- and R-pieces can be complementarily toggled while preserving both endpoint paths, maximality balances their lengths and overlap-maximality gives the contradiction.
**Next Need:** Encode the common-vertex braid as switchable alternating cycles. Any internally clean alternating cycle whose symmetric toggles remain endpoint paths is forbidden at once; only non-switchable order patterns or shared-core structure can survive.

## [length_deficit_or_saturate_the_qsegment_with_common_vertices] Adjacent R-contacts either pay length deficit or saturate the Q-segment with common vertices.
focus · lemma · proved · certified · supported
Parent: [maximum_paths_contain_no_clean_fourpoint_crossing_braid_cell]
**Given:** ["overlap-maximal maximum path Q relative to maximum path R","two consecutive common vertices on R"]
**Consumer:** ["two-path braid classification","post-43/48 overlap rigidity"]
**Consequence:** Every R-adjacency in the common-vertex skeleton is either metrically strict or maps to a Q-segment all of whose internal vertices are common.
**Next Need:** Sum or pack the strict-deficit intervals, and analyze overlap among the zero-deficit saturated Q-spans. A positive density of disjoint zero-deficit spans yields a common-vertex core; otherwise many R-adjacencies pay at least one edge of Q-distance deficit and should force high total variation in the common-vertex permutation.

## [unlabeled_lensfree_overlap_of_maximum_paths_can_be_complete] Unlabeled lens-free overlap of maximum paths can be complete.
focus · lemma · proved · certified · supported
Parent: [force_a_macroscopic_lensfree_overlap_of_neartop_maximum_paths]
**Given:** ["unlabeled maximum endpoint paths only"]
**Consumer:** ["post-43/48 braid strategy","near-dangerous gap-one classification"]
**Consequence:** The current research target is genuinely labeled: generic two-longest-path braid rigidity cannot by itself improve 43/48.
**Fence:** Do not try to deduce a long shared-edge core, a clean lens, or a longer path from macroscopic vertex overlap and overlap-maximality alone. The generic statement is false even at complete vertex overlap.
**Next Need:** Use the retained distinguished common-terminal pairs {x_i,u_i}, their common outside terminal v, ascending ranks, and source/terminal orientation. Those labels are essential extra structure absent from this construction.

## [endpoint_lenses_from_one_source_rail_are_at_most_halfrank] Two separated endpoint lenses from one source rail are at most half-rank.
focus · lemma · proved · certified · supported
Parent: [rails_retain_a_linear_family_of_whole_distinguished_chords]
**Given:** ["one maximum source rail S ending at x","two clean balanced endpoint lenses from S to host maximum paths Q,R","host lens sides otherwise disjoint"]
**Consumer:** ["whole-pair three-rail fan","post-43/48 labeled braid","endpoint-lens packing"]
**Consequence:** Two independent endpoint lenses from the same source rail cannot both extend beyond half the source rank; a longer lens forces a second Q-R intersection inside the two host-side lens paths.
**Next Need:** Apply to each of the 25/88 whole pairs. If many source lenses are long, they force extra Q-R common vertices inside their host intervals. If most are short on both hosts, pack the resulting short endpoint intervals at the distinct entrance labels and combine with the paired terminals.

## [chords_pay_quadratic_deficit_or_sourcerail_reintersection] Forward common-anchor chords pay quadratic deficit or source-rail reintersection.
focus · lemma · proved · certified · supported
Parent: [or_its_clean_source_rail_reintersects_the_opposite_side]
**Given:** ["ed412ed8e3b1 endpoint-slack/reintersection dichotomy","common rank-q anchor precursor containing every whole chord","source-clean maximum paths"]
**Consumer:** ["same-terminal certificate class S","common-anchor deficit recurrence","paid strict-gap local congestion"]
**Consequence:** Forward whole chords without a second source/anchor intersection have ordered anchor deficits growing at least one per two edges, hence quadratic total deficit; top two anchor-rank levels force reintersection.
**Next Need:** Use near-top rank concentration or selected-cell geometry to show the quadratic-deficit alternative is too expensive; otherwise exploit the many forced source/anchor reintersections, whose first return arcs satisfy the cycle budget ebd43314756d.

## [chords_are_controlled_by_oppositeend_excess_plus_return_cycles] Top-band common-anchor chords are controlled by opposite-end excess plus return cycles.
focus · lemma · proved · certified · supported
Parent: [whole_chords_pack_into_two_endpoint_vertexrank_zones]
**Given:** ["df81004a830d two-endpoint whole-chord packing","common rank-q anchor precursor","anchor entrance endpoint has potential q-1"]
**Consumer:** ["same-terminal certificate class S","paid common-anchor congestion","return-cycle packing"]
**Consequence:** Top-band common-anchor chords have only 2E+4D+O(1) unobstructed capacity, where E is the single opposite-anchor-end potential excess; all additional chords force distinguished source/anchor returns.
**Next Need:** Either globally charge large opposite-end excess E at many dangerous centers, or prove a packing/uncrossing bound for the forced return cycles. Combining either with rank-band mass in the selected S-family would give an o(p) local bound.

## [wholechord_reintersection_pays_a_nonspecial_cycle_budget] A forward whole-chord reintersection pays a nonspecial cycle budget.
focus · lemma · proved · certified · supported
Parent: [or_its_clean_source_rail_reintersects_the_opposite_side]
**Given:** ["ed412ed8e3b1 forward whole-chord deficit-or-reintersection dichotomy","f2925a904b8e nonspecial cycle-rank bound"]
**Consumer:** ["common-anchor deficit recurrence","paid strict-gap four-edge spacing","whole-pair braid classification"]
**Consequence:** The reintersection escape branch carries an explicit rank budget a+b<=r-1.
**Next Need:** Use several selected whole chords on one common anchor: either many are deficit-shallow and pack into short terminal end-zones, or many create budgeted source/anchor cycles whose first reintersection arcs must overlap or nest.

## [retracted_lowrank_residue_from_the_lensfree_wholepair_braid] The claimed low-rank residue from the lens-free whole-pair braid is invalid because the cumulative fixed-entrance bound was used with the inequality direction reversed.
focus · lemma · proposal · not_required · unchecked
Parent: [rails_retain_a_linear_family_of_whole_distinguished_chords]
**Consumer:** ["post-43/48 labeled braid"]
**Role:** retracted_claim
**Lesson:** The cumulative fixed-entrance rank bound controls low-rank counts from above, so near saturation at rank q does not force a low-rank prefix. Do not infer a positive-density uniformly lower-rank subfamily from the 25/88 whole-pair count alone.
**Replacement Target:** Use chord order, contact multiplicity, or an independent lower-rank distribution theorem; do not reuse the reversed cumulative-rank inequality.

## [whole_chord_spans_another_common_vertex_in_the_lensfree_braid] Every retained whole chord spans another common vertex in the lens-free braid.
focus · lemma · proved · certified · supported
Parent: [rails_retain_a_linear_family_of_whole_distinguished_chords]
**Given:** ["3ef8a7c2d941 lens-free near-top rails with 25/88 whole distinguished pairs"]
**Consumer:** ["post-43/48 labeled braid classification","common-hub chord interval packing"]
**Consequence:** The retained 25/88 whole chords cannot appear as elementary cells of the common-vertex skeleton; every one participates in a higher-order nesting/interleaving pattern.
**Next Need:** Exploit the resulting family of Omega(q) paired common vertices, each of whose pair-intervals is pierced by another common vertex. Classify whether many intervals are nested, crossing, or aligned simultaneously in the two rail orders; combine with c7a91e54b028 and 25f8bd73849e.

## [a_linearsize_matching_of_repeated_endpointpath_intersections] M interior U₁₁ color-terminal collisions force at least ⌈M/13⌉ endpoint-disjoint pairs of chosen maximum endpoint paths, each pair sharing at least two vertices.
focus · theorem · proved · certified · supported
Parent: [forces_a_second_intersection_with_its_own_maximum_endpoint_path]
**Given:** ["U_11 terminal-singleness on globally chosen endpoint paths","bd1e5cb6641b non-endpoint vertex forces a second endpoint-path intersection","simple rainbow terminal-pair path"]
**Consumer:** ["strong-rainbow terminal-pair path route","color-terminal collision congestion","post-43/48 U_11 analysis"]
**Consequence:** Every interior U_11 collision yields one genuine exact adjacent-edge contact after avoiding the unique last edge; bounded parent-edge reuse gives a matching of size at least M/13.
**Next Need:** Exploit the endpoint-disjoint repeated-intersection pairs quantitatively. The repaired extraction loses only a constant factor and avoids all exact-contact boundary conventions.

## [a_sharedentrance_packet_forces_the_lowerhalf_edge_ranks_upward] A shared-entrance packet forces the lower-half edge ranks upward.
focus · lemma · proved · certified · supported
Parent: [gives_two_lensfree_repeatedintersection_certificates_per_label]
**Given:** ["f84b001e0a61 same-type shared-entrance packet","5cee9bfe483f central-window capacity"]
**Consumer:** ["same-terminal strict-gap local congestion","rank-band reduction before braid analysis","four-edge and median-rank recurrence routes"]
**Consequence:** In the entrance-label branch, a large packet shared by two higher-rank source paths forces the lower-half maximum edge rank close to the host edge ranks; a wide median rank gap permits only a small packet.
**Next Need:** Combine with the lower bound M>=k/8-O(1) from f84b001e0a61. Either this rank inequality itself pays enough rank growth, or the family lies in a narrow edge-rank band where f61701327e20 and the inversion-deficit machinery apply.

## [uniqueentrance_edges_form_one_consistently_oriented_block] If two oriented linear paths have cycle-free union, their common edges form a contiguous block; under common unique-entrance traversal that block has the same orientation in both paths.
focus · lemma · proved · certified · supported
Parent: [force_cyclebearing_edges_or_common_uniqueentrance_traversal]
**Given:** ["two linear paths with no linear cycle in their union","one shared internal nonspecial edge traversed toward both last vertices through its unique entrance"]
**Consumer:** ["common-unique-entrance branch of dedf810e10a7","type-U same-terminal strict-gap branch"]
**Consequence:** Cycle-free path unions have a contiguous common-edge block, and one selected common edge with matching unique-entrance traversal synchronizes the orientation of the entire block.
**Next Need:** In dedf810e10a7 the E-type subfamily therefore lies in a consistently ordered common block. Exploit positions of many selected E-type edges inside this synchronized block; each selected edge either is nonascending or forces its immediate successor to have smaller edge rank.

## [propagates_forward_with_loss_at_most_one_or_creates_a_cycle] An internal edge above the endpoint-path rank propagates forward with loss at most one or creates a cycle.
focus · lemma · proved · certified · supported
Parent: [return_unless_the_path_leaves_through_its_unique_entrance]
**Given:** ["0000bd602854 higher-rank internal-edge return lemma","41100a9882dd repeated endpoint-on-path topology","the incident-edge bound phi(e)<=phi(a)+1 at a vertex a"]
**Consumer:** ["common high-rank edges on shorter source paths","type-U same-terminal strict-gap branch","rank-position congestion on maximum endpoint paths"]
**Consequence:** In the absence of a cycle, edge rank can fall by at most one each time the obstruction moves strictly forward along a maximum endpoint path; hence a rank-r internal edge must occur by position 2L+1-r.
**Next Need:** Apply simultaneously to the two source paths in the common-edge residue. Combine the two rank-position localizations with the known first-contact positions of the opposite-terminal labels, or show that many propagation chains must merge and thereby create bounded-reuse cycle/common-edge certificates.

## [boundary_the_lowrank_entrance_is_universally_the_central_joint] At the half-rank boundary the low-rank entrance is universally the central joint.
focus · lemma · proved · certified · supported
Parent: [a_charged_lowrank_edge_has_a_universal_centraljoint_witness]
**Given:** ["351720508b02 half-rank central witness"]
**Consumer:** ["two-rank block q,(q+1)^3 top-boundary case","Astra 11/12 route"]
**Consequence:** At phi(v)=2q-2 a charged rank-q edge has a universal entrance: on every maximum terminal path its unique entrance is exactly the central joint g_{q-1}∩g_q. This generalizes the p=4 universal middle entrance.
**Next Need:** Use three rank-(q+1) charged competitors against maximum (2q-2)-paths through the universal central entrance. Each competitor must cross both sides of the central cut or create a q-edge x-ending path. Derive a bounded central two-pole normal form analogous to p=5 4555.

## [edge_has_the_same_universal_central_entrance_at_both_terminals] A half-rank charged edge has the same universal central entrance at both terminals.
focus · lemma · proved · certified · supported
Parent: [charged_edges_are_reciprocally_central_at_both_terminals]
**Given:** ["cf6ab8703be5 universal central entrance","equal terminal potentials at half-rank boundary"]
**Consumer:** ["q,(q+1)^3 top-boundary elimination","Astra 11/12 two-rank block"]
**Consequence:** The top-boundary low edge has a genuine two-terminal central gate: every maximum path to either terminal passes through the same entrance x at the exact middle.
**Next Need:** Uncross a maximum v-path and maximum u-path through the common central gate x. Rank-(q+1) competitors charged at v and u must cross the corresponding entrance rails; compare those cross-contacts to force a q-edge path ending at x or a wrong entrance into a high edge.

## [have_reciprocal_centraljoint_constraints_at_both_terminals] Half-rank boundary edges have reciprocal central-joint constraints at both terminals.
focus · lemma · proved · certified · supported
Parent: [a_charged_lowrank_edge_has_a_universal_centraljoint_witness]
**Given:** ["351720508b02 half-rank central witness"]
**Consumer:** ["two-rank block top-boundary case","Astra 11/12 route"]
**Consequence:** The terminal-witness alternative is not one-sided: a half-rank edge with equal-potential terminals forces reciprocal exact-middle placement on maximum paths at both terminals.
**Next Need:** If both terminals admit maximum paths avoiding x, uncross the two p-edge paths whose opposite terminals sit at their central joints. Seek a (q)-edge path ending at x or a second rank-q entrance. If one side always contains x, exploit the universal entrance-central branch instead.

## [onerankhigher_charged_competitor_blocks_the_low_entrance_rail] Every one-rank-higher charged competitor blocks the low entrance rail.
focus · lemma · proved · certified · supported
Parent: [charged_rank_levels_suffice_for_the_1112_leading_coefficient]
**Given:** ["canonical entrance rail of rank-q ascending edge","rank-(q+1) nonspecial competitor at same terminal"]
**Consumer:** ["critical q,(q+1)^3 two-rank block"]
**Consequence:** In the sole unresolved two-rank pattern, all three upper-rank edges are forced blocker chords of the same low entrance rail. The problem reduces to classifying three one- or two-contact chords through a common outside terminal.
**Next Need:** Show three such rank-(q+1) chords cannot coexist. Clean one-contact chords obey c448268039f5 and 990186a1aaa6; classify two-contact chords and adjacent clean pairs.

## [high_entrance_pushes_the_low_terminal_to_the_first_path_edge] A right-joint high entrance pushes the low terminal to the first path edge.
focus · lemma · proved · certified · supported
Parent: [qq13_obstruction_has_a_fixed_fourslot_witness_normal_form]
**Given:** ["top-boundary four-slot normal form","visible right-joint entrance d"]
**Consumer:** ["q,(q+1)^3 top-boundary elimination"]
**Consequence:** The low terminal cannot serve as an arbitrary cross-blocker for a right-joint entrance. If it blocks from the left at all, it is forced to the private slot of the very first path edge.
**Next Need:** Combine with cad178c6e7ff. For a d-entrance, either u is private in g1 or the high opposite terminal crosses the central cut. If both c and d are entrances, compare their two left-side blockers; if only d is right-visible, the other two witnesses occupy a,b and their entrance/terminal labels should conflict with u private in g1.

## [leftprefix_recoil_and_unconditional_lowrail_crossing] Right-side high entrances obey a conditional left-prefix recoil and unconditional low-rail crossing.
focus · lemma · proved · certified · supported
Parent: [qq13_obstruction_has_a_fixed_fourslot_witness_normal_form]
**Given:** ["28445330afcc four-slot normal form","7c02145677de competitor-crossing"]
**Consumer:** ["two-consecutive-rank block","Astra 11/12 reconstruction"]
**Role:** corrected critical equality rail localization
**Consequence:** Right-slot witnesses are entrances. They force their high edge across every canonical low rail, but identification of the crossing with the opposite terminal requires the high entrance to be absent from that rail; on the displayed left prefix the same recoil holds when the low edge has no second prefix contact.
**Fence:** Do not identify an arbitrary canonical low entrance rail with the left half of the chosen 2q-2 terminal path.

## [can_meet_a_high_entrance_rail_late_only_as_a_double_blocker] A low edge can meet a high entrance rail late only as a double blocker.
focus · lemma · proved · certified · supported
Parent: [high_entrance_rail_crosses_the_other_three_charged_edges]
**Given:** ["21dfd53c201f high entrance rail transversality","terminal tail-blocker lemma"]
**Consumer:** ["q,(q+1)^3 elimination","Astra clean-contact counting"]
**Role:** low-edge blocker localization on high rails
**Consequence:** On every high entrance rail the low edge is either a clean single blocker in the strict interior band 3..q-2 or a double blocker. Together with f4011e425d67, all three foreign charged edges obey the same late-double rule.
**Next Need:** Count the low edge plus two high competitors on one q-edge high rail. If all three are single blockers, their contact intervals lie in the first q-2 cells and can be subjected to distance-two clean-contact conflicts. If any are double, charge the extra contact as Astra's paid defect.

## [can_meet_a_high_entrance_rail_late_only_as_a_double_blocker_2] A competing high edge can meet a high entrance rail late only as a double blocker.
focus · lemma · proved · certified · supported
Parent: [high_entrance_rail_crosses_the_other_three_charged_edges]
**Given:** ["two rank-(q+1) high edges through one terminal","canonical q-edge entrance rail for one high edge"]
**Consumer:** ["q,(q+1)^3 elimination","Astra conflict-matching reconstruction"]
**Role:** high-rail contact localization
**Consequence:** On a high entrance rail, a competing high edge cannot be a one-contact blocker in the last two cells. Any such late competitor must consume both of its non-v vertices on the rail.
**Next Need:** Apply simultaneously to the two competitors on each high rail. If both competitors reach the tail, both are double blockers and exhaust four distinct rail vertices; combine with the low edge's mandatory tail contact to force a bridge/overlap. If one competitor is early, splice two rails at its early contact.

## [blockers_are_incompatible_on_every_canonical_entrance_rail] Distance-two single blockers are incompatible on every canonical entrance rail.
focus · lemma · proved · certified · supported
Parent: [have_exact_clean_interior_bands_and_doubleonly_terminal_cells]
**Given:** ["canonical entrance rail","two foreign single blockers through target terminal"]
**Consumer:** ["Astra conflict matching","q,(q+1)^3 high-rail packing"]
**Role:** universal rail conflict
**Consequence:** On any canonical entrance rail, private single-contact blockers through the target terminal cannot occupy cells at distance two. This applies simultaneously on all three high rails in a q,(q+1)^3 block.
**Next Need:** Combine across the three high rails with 3e837f0c5fe6. If a rail has no double blocker, its three foreign contacts are interior private cells avoiding distance two. Compare the three resulting contact orders; seek a cyclic-order contradiction or show one rail must contain a double blocker, furnishing the paid conflict Astra's count needs.

## [state_the_low_edge_doubleblocks_every_high_entrance_rail] In the 4555 rank-pair state the low edge double-blocks every high entrance rail.
focus · lemma · proved · certified · supported
Parent: [have_exact_clean_interior_bands_and_doubleonly_terminal_cells]
**Given:** ["3e837f0c5fe6 exact rail bands"]
**Consumer:** ["rank-pair block q=4","Astra 11/12 route"]
**Role:** small-rank anchor for conflict matching
**Consequence:** The first unresolved general two-rank case above q=3 has every high entrance rail passing through both low-edge vertices x,u.
**Next Need:** Classify four-edge paths Q_i through both x and u with phi(x)=3 and ending at a rank-five entrance y_i of potential 4. Two or three such rails, together with pairwise high-edge transversality, should force a repeated two-edge segment or a four-edge x-ending uncrossing.

## [three_critical_high_entrance_rails_force_a_twovertex_overlap] Three critical high entrance rails force a two-vertex overlap.
focus · lemma · proved · certified · supported
Parent: [of_two_equalpotential_entrance_rails_is_an_aligned_joint]
**Given:** ["21dfd53c201f complete charged-edge transversality of high rails","a15746990e9b unique-intersection alignment"]
**Consumer:** ["q,(q+1)^3 elimination","Astra rail conflict matching"]
**Consequence:** The three high rails cannot form a simple single-intersection braid. At least one pair has two distinct common vertices, so the residual obstruction contains a genuine two-rail theta/overlap.
**Next Need:** Analyze two q-edge entrance rails with endpoint potentials q and at least two common vertices. Choose two consecutive common vertices along one rail. If their order agrees on the other rail, compare the two alternative segments; if the order reverses, the union contains a linear cycle. Use mandatory target labels to rule out complete segment coincidence and force a q+1 endpoint path or a short cycle with an ear.

## [collapses_to_a_left_blocker_or_the_missing_rightprivate_slot] Joint-pair conflict collapses to a left blocker or the missing right-private slot.
focus · lemma · proved · certified · supported
Parent: [gadget_has_a_threeedge_conflict_graph_with_forced_crossblockers]
**Given:** ["all-visible four-slot gadget","a and d occupied"]
**Consumer:** ["top-boundary q,(q+1)^3 elimination"]
**Consequence:** The ad conflict has only two realizations: d sends its terminal left, or a sends its terminal exactly into the missing right-private slot c. Pattern acd therefore forces the left-crossing branch outright.
**Next Need:** In acd combine z_d left with z_a right and the c-edge. In abd analyze the exceptional closure h_a={a,v,c}; since c is missing as entrance, use h_b and h_d to show this closure either gives a q+1 path ending at b or forces z_b,z_d into opposite far tails.

## [corrected_acd_topboundary_blocker_moat] Corrected acd top-boundary blocker moat.
focus · lemma · proved · certified · supported
Parent: [gadget_has_a_threeedge_conflict_graph_with_forced_crossblockers]
**Given:** ["872bb5f4effc conflict graph","8479f1cdc5d5 left-joint cross-cut terminal"]
**Consumer:** ["q,(q+1)^3 elimination","Astra 11/12 route"]
**Role:** corrected top-boundary acd moat
**Consequence:** In acd, z_d is forced through q-4, z_c through q-3, while z_a starts no earlier than q+1. The q+1 boundary case remains because d cross-blocks the naive reverse splice.
**Next Need:** Analyze the exact boundary case z_a∈g_{q+1}. If absent, there is a genuine two-cell gap; if present, h_a and h_d together with g_{q+1} form a local two-contact obstruction. Classify that obstruction and use h_c.

## [a_rankmixed_central_triangle_orders_its_two_far_high_terminals] A rank-mixed central triangle orders its two far high terminals.
focus · lemma · proved · certified · supported
Parent: [gadget_contains_a_rankq_base_with_two_rankq1_entrance_sides]
**Given:** ["38957884d5a6 rank-mixed central triangle","cross-cut terminal localization"]
**Consumer:** ["top-boundary q,(q+1)^3 elimination"]
**Consequence:** A fully occupied central base imposes a monotone order on the two remote high terminals: joint-side terminal is no farther from the center than private-side terminal (in the appropriate orientation).
**Next Need:** Compare this forced P-order with canonical entrance rails of h_a,h_b (or h_c,h_d). Each rail crosses the other high edge and the low gate. Show reciprocal blocking forces the opposite terminal order, yielding contradiction or an equality two-cycle.

## [high_terminals_have_reciprocal_central_entrance_structure] Strict-rise high terminals have reciprocal central entrance structure.
focus · lemma · proved · certified · supported
Parent: [qq13_pattern_contains_a_genuine_crossed_highedge_pair]
**Given:** ["rank-(q+1) ascending high edge","entrance potential q","base terminal potential 2q-2","charged opposite terminal"]
**Consumer:** ["top-boundary crossed-pair uncrossing","Astra 11/12 route"]
**Consequence:** A crossed high terminal can exceed the base potential by at most two. At +2 its high entrance is universally the central joint on every maximum terminal path; at +1 only one exceptional y-absent state remains, with the common terminal v pinned to the central joint.
**Next Need:** Use this on the crossed pair. If either far terminal has strict rise, compare its reciprocal central path with the original P and the other high edge. The remaining flat case has both far terminals exactly 2q-2 and should admit a symmetric half-rank-style two-path uncrossing.

## [patterns_reduce_to_crossed_terminals_plus_two_exact_closures] The four top-boundary missing-slot patterns reduce to crossed terminals plus two exact closures.
focus · lemma · proved · certified · supported
Parent: [gadget_has_a_threeedge_conflict_graph_with_forced_crossblockers]
**Given:** ["all-visible top-boundary four-slot gadget","q>=4"]
**Consumer:** ["q,(q+1)^3 elimination","Astra 11/12 route"]
**Consequence:** The four missing-slot states are no longer generic. Each has a forced high-terminal crossing from one side of the central block to the other; the only exact local escape states are z_a=c in abd and z_a=d in abc, where the a-edge closes onto the unique missing slot.
**Next Need:** Attack the two exact closures first. They are finite local triangles/rectangles. Then treat the genuine crossed-terminal states by reciprocal maximum paths at the left/right high terminals.

## [the_bcd_topboundary_pattern_forces_a_threeedge_blocker_moat] The bcd top-boundary pattern forces a three-edge blocker moat.
focus · lemma · proved · certified · supported
Parent: [gadget_has_a_threeedge_conflict_graph_with_forced_crossblockers]
**Given:** ["high_entrance_excludes_the_low_terminal_from_the_left_half","gadget_has_a_threeedge_conflict_graph_with_forced_crossblockers","all-visible four-slot normal form"]
**Consumer:** ["q,(q+1)^3 elimination","Astra 11/12 route"]
**Role:** corrected top-boundary bcd moat
**Consequence:** In bcd, z_c and z_d are forced through q-4 and z_b is strictly right of g_q. The prior q+2 assertion had an unhandled g_{q+1} cross-block and is withdrawn.
**Next Need:** Analyze z_b on g_{q+1}. If present, h_b,g_{q+1},h_d create the same local cross-block gadget as the acd boundary state. If absent, the stronger two-cell right moat holds.

## [dfree_abc_topboundary_pattern_also_has_a_crossed_blocker_moat] In the d-free abc top-boundary pattern, two opposite terminals lie to the right of the central block and the third lies strictly to its left, giving a crossed blocker moat.
focus · lemma · proposal · not_required · unchecked
Parent: [a_leftjoint_high_entrance_cannot_close_onto_the_central_edge]
**Given:** ["4b2eb2497cf0 no central closure for a","eddd8ad49835 left-central crossing","872bb5f4effc ac conflict"]
**Consumer:** ["top-boundary q,(q+1)^3 elimination"]
**Fence:** The z_b=d exclusion in the draft proof is not yet fully checked; do not use the full statement until repaired.
**Next Need:** Either prove z_b!=d cleanly or weaken statement to z_a right and z_c<=q-4. Then unify with d22fb281de15.

## [every_topboundary_pattern_contains_a_far_crossed_pair] Every top-boundary pattern contains a far crossed pair.
focus · lemma · proved · certified · supported
Parent: [a_leftjoint_high_entrance_cannot_close_onto_the_central_edge]
**Given:** ["4b2eb2497cf0 strict-right a-edge","872bb5f4effc conflict graph","94bd984bc952 right-joint pressure","cad178c6e7ff conditional c-recoil"]
**Consumer:** ["q,(q+1)^3 top-boundary elimination","Astra 11/12 crossed-rectangle route"]
**Consequence:** All four central slot patterns contain a uniform far crossed pair. Every occupied right entrance c/d has a high terminal whose first path contact is at most q-4; a suitable occupied left entrance has its high terminal strictly after g_q.
**Next Need:** Exploit a far crossed pair. The natural object is the theta formed by the two high edges and the two P-segments. Use canonical q-edge entrance rails: each must cross the low gate {x,u} and the third high edge. Seek a contact-order uncrossing theorem in first/last coordinates.

## [high_entrance_sends_its_opposite_terminal_across_the_cut] Every left-central high entrance sends its opposite terminal across the cut.
focus · lemma · proved · certified · supported
Parent: [top_boundary_every_high_competitor_has_a_visible_entrance]
**Given:** ["top-boundary all-visible four-slot form"]
**Consumer:** ["abc/abd/acd elimination","Astra conflict matching"]
**Role:** left-central cross-cut rule
**Consequence:** Both left slots a and b behave uniformly: an occupied high entrance forces its opposite terminal to the right half.
**Next Need:** Combine with 94bd984bc952 for patterns containing d. Then every d-pattern is a crossed orientation: left-slot high edges point right, h_d points left, and if c is occupied its terminal also points left.

## [rail_in_the_critical_tworank_pattern_crosses_the_low_edge] Every high entrance rail in the critical two-rank pattern crosses the low edge.
focus · lemma · proved · certified · supported
Parent: [top_boundary_every_high_competitor_has_a_visible_entrance]
**Given:** ["rank-q low edge","three rank-(q+1) high competitors with canonical entrance rails"]
**Consumer:** ["q,(q+1)^3 elimination","Astra 11/12 conflict-matching reconstruction"]
**Consequence:** Every canonical high entrance rail must cross one of the two non-common vertices of the low edge. Three high rails therefore create a repeated gate contact at x or u.
**Next Need:** Uncross two q-edge high entrance rails meeting the same gate vertex. If the common gate is x, its potential is only q-1, so any splice making x a physical endpoint of q edges is impossible; if the common gate is u, use phi(u)=2q-2 and reciprocal centrality to transfer to x or obtain a second entrance of e.

## [topboundary_dpatterns_have_a_forced_crossedterminal_orientation] Every top-boundary q,(q+1)^3 pattern containing d has a forced left/right crossed-terminal orientation.
focus · theorem · proved · pending · unchecked · pending
Parent: [qq13_obstruction_has_a_fixed_fourslot_witness_normal_form]
**Given:** ["top-boundary four-slot normal form","right-joint blocker localization","left/right conflict-pair bounds"]
**Consumer:** ["top-boundary q,(q+1)^3 elimination","Astra 11/12 route"]
**Consequence:** Every top-boundary triple containing d has terminals forced to opposite sides of the central entrance.
**Next Need:** Prove one crossed-rectangle uncrossing lemma eliminating the three d-containing patterns simultaneously.

## [refuted_route_topboundary_mutualblocking_rails] The proposed general-q mutual-blocking-rail lemma is false because a rank-(q+1) edge cannot terminate a maximum (2q−2)-edge path when q>3; the argument only applies at q=3.
focus · lemma · conjecture · not_required · unchecked
Parent: [charged_rank_levels_suffice_for_the_1112_leading_coefficient]
**Consumer:** ["Astra 11/12 route"]
**Role:** refuted route
**Lesson:** The p=4 proof uses the accidental equality q+1=phi(v). For general q at the half-rank boundary, high edges cannot serve as last edges of maximum v-paths. Work on one arbitrary maximum v-path via the four-slot normal form instead.

## [upper_consecutive_rank_lies_below_the_odd_central_threshold] Any four-edge counterexample with occupied upper consecutive rank lies below the odd central threshold.
focus · lemma · proved · certified · supported
Parent: [charged_rank_levels_suffice_for_the_1112_leading_coefficient]
**Given:** ["a570b0ad0001 odd-central-window bound","a4fb7e7b171e strict-rise rank floor"]
**Consumer:** ["two-consecutive-rank block","Astra 11/12 route"]
**Consequence:** A two-rank-block counterexample is confined to q+1<=phi(v)<=2q-2. At the top boundary only the general 4555/5555 analogues survive; any bottom-rank edge there joins equal-potential terminals.
**Next Need:** Attack p=2q-2 first. Generalize the p=5 4555 crossed-rectangle reduction to pattern (q,q+1,q+1,q+1), and separately handle four rank-(q+1) edges. Then descend p.

## [charged_threequarters_bound_via_consecutive_rank_pairs] A consecutive-rank bound of at most three charged ascending edges in each pair {q,q+1} would imply c₊(v)≤⌊3φ(v)/4⌋ and hence the 11/12 leading coefficient.
focus · theorem · proposal · not_required · unchecked
Parent: [potentialoriented_local_bound_gives_astra_1112_coefficient]
**Given:** ["user screenshots of interrupted Astra work","419519f0efa5 ascending accounting","a7b7670e955a charged rank floor","2665d2c81d39 rank-pair arithmetic","990186a1aaa6/08f894b8cb5e/eac2e3da3eea clean-contact splices"]
**Consumer:** ["11/12 leading coefficient","general linear-path Turan upper bound"]
**Role:** reconstructed Astra route
**Consequence:** Corrects the earlier factor-two guess in 0904073d4cbf. The natural local quantity is charged degree c_+(v), targeted at 3phi(v)/4.
**Next Need:** Prove the consecutive-rank block n_q(v)+n_{q+1}(v)<=3. Focus first on q,(q+1)^3 and (q+1)^4; clean singleton chords are controlled, while residual two-contact chords must be closed using the third competitor and tail/cross-splice obstruction abeab7363c1a.

## [and_the_twothirds_ceiling_of_unweighted_snake_counting] Special-edge accounting criterion and the two-thirds ceiling of unweighted snake counting.
focus · lemma · proved · certified · supported
Parent: [snake_indegree_lemma]
**Consumer:** ["general leading-coefficient improvement","weighted snake routes"]
**Consequence:** Positive special-edge density improves the coefficient, but unweighted snake counting has an intrinsic 2/3 floor.

## [devinemilans_general_linearpath_upper_bound] Devine–Milans general linear-path upper bound.
focus · theorem · proved · certified · supported
Parent: [snake_indegree_lemma]
**Given:** P_ell^(r)-free linear r-graph
**Need:** improve the leading coefficient for r=3
**Consumer:** grand target
**Working Route:** refine snake-incidence counting beyond the baseline r-1 contributions per edge

## [the_fixedtarget_singleblocker_rotation_graph_is_k4free] The fixed-target single-blocker rotation graph is K4-free.
focus · lemma · proved · certified · supported
Parent: [snake_and_terminalcontact_accounting_route]
**Given:** ["exact rotation-triangle normal form f173a72fd8b2"]
**Consumer:** ["boundary q=delta attack","rotation-state block decomposition"]
**Consequence:** Rules out K4 as a finite short-cycle closure after triangle/square escape; remaining recurrent short-cycle structures must be cactus/block-like rather than clique-like.
**Next Need:** Analyze leaf triangle/square blocks in the rotation graph and show their forced external exits propagate to a nonlocal cycle or rank progress.

## [current_conjecture_proposal_and_numericalevidence_map] Current conjecture, proposal, and numerical-evidence map
focus · abstraction · proposal · not_required · unchecked
Parent: [project_guidance_literature_and_proofreplacement_program]
**Consumer:** all workers entering the current general-length frontier
**Role:** team_visibility_index
**Instruction:** Fetch exact objects before relying on mathematical details.

## [current_project_guidance_general_length_postp4] Current project guidance: general length, post-P4
focus · abstraction · proposal · not_required · unchecked
Parent: [project_guidance_literature_and_proofreplacement_program]
**On Demand Ids:** ["devinemilans_general_linearpath_upper_bound","specialedge_accounting_hinge_inequality","literature_state_for_linear_hypergraph_paths"]
**Working Route:** general ell; snake deficit/nonspecial-edge sparsity

## [residuefree_ell13_lower_construction] For every ℓ≥2 there is a P_ℓ-free linear triple-system component of density exactly (ℓ-1)/3, yielding ex_L(n,P_ℓ^(3)) ≥ ((ℓ-1)/3)n-O(ℓ^2).
available · lemma · proved · certified · supported
Parent: [general_lowerbound_construction_program]
**Given:** exact MPTS sizes and admissible Steiner triple systems
**Consumer:** general lower benchmark
**Role:** precise all-residue cleanup; no leading-coefficient improvement

## [longestpath_paircapacity_reduction_with_outside_extremal_defect] Inductively, the 1/3 target reduces exactly to paying edges meeting a longest path from path-pair capacity, path-length slack, and the outside extremal defect.
available · lemma · proved · pending · unchecked · pending
Parent: [leading_terms_for_3uniform_linear_path_turn_numbers]

## [families_with_only_lengths_3_and_7_surviving_through_15] If a critical induced Boolean Schur system is P_ℓ-free and beats density (ℓ-1)/3, then it is projective or two-point-deleted projective; for 2≤ℓ≤15 only the Fano case ℓ=3 and PG(3,2) case ℓ=7 survive.
available · lemma · proved · certified · supported
Parent: [classification_for_induced_boolean_schur_triple_systems]
**Consumer:** ["lower-bound construction search"]
**Consequence:** Critical induced-Boolean lower-bound candidates are projective or two-point-deleted projective; through length 15 only ell=3 and 7 survive.

## [squares_admit_long_coprimeorbit_paths_and_stay_below_one_third] For every d≥3, PG(d-1,2) tensor-squared has a linear path of length (2^d-1)(2^{d-1}-1)-1, and its normalized density at the first forbidden length is below 1/3.
available · lemma · proved · certified · supported
Parent: [boolean_additive_and_projective_construction_route]
**Consumer:** ["diagonal-product lower-bound route","binary-projective construction search"]
**Consequence:** Every binary-projective diagonal tensor square is fenced strictly below one third.

## [and_fixedmultiplicity_sharedcolor_lifts_cannot_beat_one_third] Static transversals and fixed-multiplicity shared-color lifts cannot beat one third.
available · lemma · proved · certified · supported
Parent: [latin_transversal_and_blowup_construction_route]
**Consumer:** ["general lower-bound construction search"]
**Role:** construction-route fence
**Consequence:** Static global covers are capped below 1/4, repeated one-factorization lifts realize the same obstruction, and fixed-multiplicity shared-color complete-graph lifts are capped at 1/3+o(1).
**Next Need:** Any >1/3 construction using pinning or color sharing must make the controlling resources path-state-dependent, hierarchical, or otherwise escape fixed-multiplicity shared-color geometry.

## [blowups_lift_every_fixed_base_cycle_to_an_almost_qfold_path] Characteristic-two additive blow-ups lift every fixed base cycle to an almost q-fold path.
available · lemma · proved · certified · supported
Parent: [latin_transversal_and_blowup_construction_route]
**Consumer:** ["general lower-bound construction search"]
**Consequence:** Characteristic-two finite-field additive blow-ups obey the same asymptotic base-cycle fence as odd-order additive lifts.

## [latin_blowups_lift_base_cycles_to_nearspanning_route_paths] If a fixed linear 3-graph contains a linear cycle of length s, then every arbitrary TD(3,q) blow-up contains a linear path of length sq−o(q), so the normalized density is at most m/(vs)+o(1).
available · lemma · proved · certified · supported
Parent: [latin_transversal_and_blowup_construction_route]
**Given:** ["fixed base linear cycle","arbitrary TD(3,q) filling on each base edge"]
**Consumer:** ["general lower-bound construction search","fixed-template Latin blow-up route"]
**Consequence:** Every fixed base cycle lifts to a path of asymptotic length sq, reducing the construction coefficient to the finite circumference ratio m/(vs).
**Next Need:** Find a finite linear triple-system template with circumference below 3m/v, or prove a general circumference-density inequality.

## [affineplane_blowups_have_a_4qcycle_and_cannot_beat_one_third] Additive affine-plane blow-ups have a 4q-cycle and cannot beat one third.
available · lemma · proved · certified · supported
Parent: [oddorder_additive_latin_blowups_lift_every_base_linear_cycle]
**Given:** ["AG(2,3) parallel classes","additive cycle-lift lemma"]
**Consumer:** ["general lower-bound construction search"]
**Consequence:** kills the additive affine-plane blow-up exactly at the 1/3 barrier
**Next Need:** analyze non-additive Latin fillings of the affine-plane line gadgets

## [pg32_contains_a_sevenedge_linear_cycle] PG(3,2) contains a seven-edge linear cycle.
available · lemma · proved · certified · supported
Parent: [oddorder_additive_latin_blowups_lift_every_base_linear_cycle]
**Given:** ["PG(3,2) point-line Steiner triple system","additive Latin blow-up cycle-lift lemma"]
**Consumer:** ["PG(3,2) blow-up lower-bound route","general lower-bound construction search"]
**Consequence:** kills the natural additive blow-up of the P7 extremizer as a >1/3 construction
**Next Need:** only non-additive local Latin squares could evade this specific lifted-cycle obstruction

## [paths_give_a_onethird_ceiling_for_full_transversal_designs] Schrijver rainbow paths give a one-third ceiling for full transversal designs.
available · theorem · proved · certified · supported
Parent: [latin_transversal_and_blowup_construction_route]
**Given:** ["Schrijver rainbow-path theorem d-o(d) for properly d-edge-colored d-regular graphs","Latin-square representation of TD(3,q)"]
**Consumer:** ["Latin-square/transversal-design lower-bound route","general lower-bound construction search"]
**Consequence:** full transversal designs are asymptotically capped at normalized coefficient 1/3
**Next Need:** any 3-partite >1/3 construction must use genuinely partial/nonregular Latin structures rather than a full TD(3,q)

## [missing_weights_cannot_certify_a_leading_lowerbound_improvement] If a linear 3-graph has maximum degree at least floor((ℓ+2)/2), its ternary incidence code contains a word of weight ℓ+2, so missing-weight ternary certificates cannot beat the one-third coefficient.
available · lemma · proved · certified · supported
Parent: [defeat_the_missingweight_certificate_in_two_residue_classes]
**Given:** ["linear paths","incidence-code support cancellation","high-degree star"]
**Consumer:** ["incidence-code obstruction route","general lower-bound construction search"]
**Consequence:** single missing-weight certificates over F_3 are useless for any >1/3 construction
**Next Need:** if codes remain useful, exploit binary-specific structure in ell=0,3 mod4 or constraints beyond one missing Hamming weight

## [incidence_sums_give_a_supportell2_codeword_over_any_field] Over any field, a linear P_ℓ yields an alternating incidence sum with support exactly ℓ+2, so missing support size ℓ+2 certifies P_ℓ-freeness.
available · lemma · proved · certified · supported
Parent: [a_missing_incidencecode_weight_forbids_a_linear_path]
**Given:** ["edge-incidence span over an arbitrary field"]
**Consumer:** ["general lower-bound construction search","algebraic incidence-code obstruction route"]
**Consequence:** allows q-ary/algebraic design codes, not only binary codes, to certify P_ell-freeness
**Next Need:** find dense linear triple-system families whose incidence spans omit support size ell+2

## [affine_f3_jointsum_obstruction_for_spanning_paths] Any spanning path in AG(d,3) has joint vectors summing to zero in F_3^d; in particular this algebraically forbids a spanning P_4 in AG(2,3).
available · lemma · proved · certified · supported
Parent: [sts2ell1_spanningpath_obstruction_route]
**Consumer:** ["STS spanning-path obstruction route","algebraic lower-bound construction search"]
**Consequence:** recovers the P4-free affine plane conceptually; supplies a necessary moment condition in all affine dimensions
**Limitation:** condition is not sufficient for d=3

## [ag33_has_a_spanning_p13] AG(3,3) contains a spanning 13-edge linear path, so the non-Hamiltonicity obstruction seen in AG(2,3) does not extend to dimension three.
available · lemma · proved · certified · supported
Parent: [sts2ell1_spanningpath_obstruction_route]
**Consumer:** ["affine lower-bound route","STS spanning-path obstruction route"]
**Role:** fence
**Consequence:** AG(d,3) is not uniformly non-Hamiltonian; AG(2,3) does not extrapolate to d=3

## [edgetransitive_steiner_systems_have_a_sharp_deletion_barrier] In an edge-transitive STS on v=2ℓ+1 vertices containing a spanning P_ℓ, every block set meeting all spanning P_ℓ has size at least v/3.
available · theorem · proved · certified · supported
Parent: [sts2ell1_spanningpath_obstruction_route]
**Given:** ["edge-transitive STS(2ell+1)","one spanning P_ell"]
**Consumer:** ["STS spanning-path obstruction route","general lower-bound construction search"]
**Consequence:** Hamiltonian symmetric designs cannot be sparsely modified into a >1/3 construction

## [give_a_13_ceiling_for_steinersystem_lower_constructions] Almost-spanning hypertree results imply that Steiner triple systems contain linear paths on nearly all vertices, so STS-based lower constructions have asymptotic coefficient at most 1/3.
available · theorem · proved · certified · supported
Parent: [sts2ell1_spanningpath_obstruction_route]
**Given:** ["Elliott-Rodl hypertree embedding theorem for STS"]
**Consumer:** ["general lower-bound construction search","STS spanning-path obstruction route"]
**Role:** asymptotic fence
**Consequence:** full Steiner triple systems have asymptotic normalized path-density coefficient at most 1/3

## [incidencecode_constraint_for_a_spanning_linear_path] For a spanning P_ℓ in a 3-graph on 2ℓ+1 vertices with joint set J, the binary incidence code contains 1_V+1_J, imposing parity constraints against every dual codeword.
available · lemma · proved · certified · supported
Parent: [sts2ell1_spanningpath_obstruction_route]
**Consumer:** ["STS spanning-path obstruction route","lower-bound construction search"]
**Consequence:** turns spanning-path nonexistence into a binary-code necessary condition on the joint set
**Next Need:** identify infinite STS families whose dual-code constraints exclude path-compatible joint sets

## [cartesian_products_multiply_available_linearpath_lengths] If linear 3-graphs H and K contain paths of lengths a and b, then H□K contains a path of length (a+1)(b+1)-1, so repeated Cartesian powers cannot yield a positive asymptotic path-density coefficient.
available · lemma · proved · certified · supported
Parent: [lifts_are_asymptotically_inefficient_for_path_lower_bounds]
**Given:** ["linear paths in two Cartesian factors"]
**Consumer:** ["general lower-bound construction search"]
**Consequence:** fixed-component Cartesian powers have multiplicative path growth but only additive density growth
**Fence:** rules out Cartesian powering as a way to scale the P5 extremal density/path advantage

## [propercolor_lifts_have_a_onequarter_asymptotic_ceiling] Any repeated shared-color lift of a fixed properly edge-colored graph has asymptotic path lower-bound coefficient at most one quarter.
available · theorem · proved · certified · supported
Parent: [lifts_are_asymptotically_inefficient_for_path_lower_bounds]
**Given:** ["arbitrary properly edge-colored graph","arbitrarily many private copies sharing the color vertices"]
**Consumer:** ["general lower-bound construction search","strong-independent-separator gluing route"]
**Consequence:** cross-edge-only shared-separator constructions have asymptotic coefficient at most 1/4
**Strengthens:** ["lifts_asymptotically_saturate_the_transversal_path_ceiling","fixed-multiplicity one-factorization fences"]

## [parity_constraint_for_spanning_paths_in_low2rank_sts] In any low-2-rank Steiner triple system with carrier labels h(x), a spanning path joint set J must satisfy XOR_{x∈J} h(x)=0.
available · lemma · proved · certified · supported
Parent: [sts2ell1_spanningpath_obstruction_route]
**Given:** ["low binary rank STS carrier theorem","incidence-code spanning-path constraint"]
**Consumer:** ["STS spanning-path obstruction route","low-rank design construction search"]
**Consequence:** every spanning path has a zero-sum carrier-parity profile
**Limitation:** PG(4,2) shows this linear parity condition alone is not sufficient

## [parity_obstruction_for_spanning_paths_in_binary_projective_sts] If PG(d-1,2) has a spanning linear path with joint set J, then every projective hyperplane meets J evenly, equivalently the vector sum of J is zero.
available · lemma · proved · certified · supported
Parent: [sts2ell1_spanningpath_obstruction_route]
**Consumer:** ["binary-projective non-Hamiltonicity route","P7 construction"]
**Consequence:** reduces any spanning-path search in PG(d-1,2) to zero-sum joint sets meeting every hyperplane evenly
**Limitation:** for d>4 this parity condition alone does not classify the joint set

## [p7_twosubspace_grid_obstruction_is_dimensionfour_exceptional] The complementary-two-subspace joint-set obstruction used for P_7 in PG(3,2) is dimension-four exceptional and cannot recur in the same form in other binary projective dimensions.
available · lemma · proved · certified · supported
Parent: [pg32_gives_a_73_lower_bound_for_p7]
**Given:** ["new P7 additive proof","Boolean projective STS"]
**Consumer:** ["binary-projective lower-bound route","generalization analysis"]
**Consequence:** isolates the generalizable dependence lemma and proves the endpoint-grid obstruction itself is unique to r=4
**Fence:** full PG(r-1,2) is Hamiltonian for r>=5

## [twopoint_split_of_a_projective_sevencycle_is_hamiltonian] Splitting a projective seven-cycle in PG(3,2) across two new points produces a 17-vertex, 42-edge system that nevertheless contains a spanning P_8.
available · lemma · proved · certified · supported
Parent: [pg32_gives_a_73_lower_bound_for_p7]
**Given:** ["PG(3,2) P7-free construction","seven-cycle split across two new vertices"]
**Consumer:** ["near-projective lower-bound construction search","fixed P8 lower bound"]
**Warning:** do not iterate this split construction computationally without a new structural invariant
**Consequence:** the natural 42-edge two-point cycle-splitting modification does not improve the P8 lower bound

## [pg42_has_a_spanning_15edge_linear_path] PG(4,2) contains a spanning 15-edge linear path, so the PG(3,2) non-Hamiltonicity phenomenon does not persist in the next binary projective dimension.
available · lemma · proved · certified · supported
Parent: [sts2ell1_spanningpath_obstruction_route]
**Given:** ["binary projective STS PG(4,2)"]
**Consumer:** ["STS(2ell+1) spanning-path obstruction route","binary-projective lower-bound route"]
**Consequence:** the PG(3,2) P7-free construction does not extend by simply taking PG(d-1,2) for d=5; the hyperplane parity condition is not sufficient to forbid spanning paths

## [pg42_has_a_spanning_p15] PG(4,2) contains a spanning P_15 on its 31 points, ruling out a direct extension of the PG(3,2) lower-bound obstruction.
available · lemma · proved · certified · supported
Parent: [sts2ell1_spanningpath_obstruction_route]
**Consumer:** ["binary-projective lower-bound route","general lower-bound construction search"]
**Role:** fence
**Consequence:** PG(d-1,2) is not uniformly non-Hamiltonian; the P7 construction does not extrapolate directly to ell=15

## [sts_doubling_cannot_beat_the_onethird_leading_coefficient] For all sufficiently large doubled Steiner triple systems, mixed blocks alone contain a linear path of length at least u-1, so ordinary STS doubling cannot beat the asymptotic one-third lower-bound coefficient.
available · theorem · proved · certified · supported
Parent: [reduces_spanning_paths_to_additive_rainbowforest_accounting]
**Consumer:** ["recursive doubling lower-bound route","hierarchical one-factorization constructions","general lower-bound construction search"]
**Role:** fence
**Consequence:** any >1/3 construction must avoid a full linear-size one-factorization layer whose rainbow paths lift directly

## [signed_carrierchain_identity_for_a_spanning_path] A spanning path in the signed-projective normal form induces quotient data satisfying A_Q y=p and a switching-invariant signed parity identity.
available · lemma · proved · certified · supported
Parent: [signed_projective_normal_form_one_rank_above_minimum]
**Given:** ["t=1 signed-projective normal form","spanning linear path"]
**Consumer:** ["signed low-rank STS obstruction route"]
**Consequence:** a spanning path induces a signed quotient line-chain with prescribed boundary and switching-invariant evaluation
**Next Need:** find a switching class sigma for which no path-compatible pair (y,p) and joint-bit assignment can satisfy the identity

## [fence_is_a_direct_test_case_of_the_incidencerank_conjecture] Regular path-length fence is a direct test case of the incidence-rank conjecture
available · abstraction · proposal · not_required · unchecked
Parent: [incidencerank_path_conjecture]
**Given:** ["d-regular linear 3-graph","incidence-rank path conjecture"]
**Consumer:** ["regular lower-bound construction search","incidence-rank route"]
**Role:** route equivalence / difficulty calibration
**Consequence:** a regular counterexample with L<=d-2 refutes the incidence-rank conjecture; the conjecture implies L>=d-1

## [matching_number_gives_only_a_onequarter_path_lower_coefficient] A bounded matching number alone yields only an asymptotic ℓ/4 coefficient for P_ℓ-free linear 3-graphs, so it cannot beat the one-third lower-bound coefficient.
available · theorem · proved · certified · supported
Parent: [incidencerank_path_conjecture]
**Given:** ["linear 3-graph = maximum codegree at most one","matching-number certificate for P_ell-freeness"]
**Consumer:** ["general lower-bound construction search","matching-number route"]
**Role:** asymptotic fence
**Consequence:** any construction relying on matching number below ceil(ell/2) has asymptotic coefficient at most 1/4

## [of_any_lower_construction_above_the_onethird_coefficient] Any P_ℓ-free linear 3-graph with density above ℓ/3 must be large, high-degree, have large transversal and matching numbers, contain a dense minimum-degree subgraph, and violate the incidence-rank conjecture.
available · lemma · proved · certified · supported
Parent: [incidencerank_path_conjecture]
**Given:** ["P_ell-free linear 3-graph","density strictly above ell/3"]
**Consumer:** ["general lower-bound construction search","incidence-rank route"]
**Consequence:** any >1/3 construction must have n>2ell, average degree>ell, tau=Omega(ell), nu=Omega(ell), a dense minimum-degree core, and must refute the incidence-rank conjecture

## [incidencerank_spectral_identity] For a linear 3-graph with incidence matrix N and intersection adjacency matrix A, N^T N=3I+A, so rank(N)=m-mult_A(-3)≤n.
available · lemma · proved · certified · supported
Parent: [exact_cliquecover_reformulation_of_linear_triple_systems]
**Given:** intersection graph F of a linear triple system
**Need:** lower-bound rank(3I+A) for induced-P_ell-free realizable F
**Consumer:** spectral/rank route to upper bounds
**Target Scale:** rank about 3m/ell would match the conjectural ell*n/3 scale

## [fences_force_cyclerich_leadingscale_constructions] In a linear 3-graph, chordal intersection graphs have at most 3n/2 hyperedges, and any excess over 3n/2 forces proportionally many pairwise edge-disjoint linear cycles.
available · lemma · proved · certified · supported
Parent: [lemma_linear_paths_are_induced_paths_in_the_intersection_graph]
**Given:** ["linear 3-graph","intersection graph","P_ell-freeness"]
**Consumer:** ["general lower-bound construction search","cycle-rich counterexample anatomy","upper-bound cycle-packing route"]
**Consequence:** Chord-rich intersection-graph constructions have bounded density; any leading-scale P_ell-free system must contain linearly many edge-disjoint linear cycles.
**Next Need:** Exploit the forced cycle packing rather than pursue nearly chordal lower-bound constructions.

## [k33_family_refutes_the_specialedge_nullity_conjecture] There is a family with no special edges but positive incidence-matrix nullity, refuting the special-edge nullity conjecture.
available · lemma · proved · certified · supported
Parent: [specialedge_nullity_conjecture]
**Consumer:** ["incidence-rank upper-bound route","special-edge strategy"]
**Consequence:** Closes the unconditional nullity<=special-edges branch.
**Surviving Target:** Use maximum-degree localization 76a914294ba8, path-specific rank inequalities, or compensated ascending-edge structure.

## [k33_nonspecialcolumn_dependence_obstruction] Nonspecial-edge incidence columns need not be independent: an explicit six-edge configuration with intersection graph K_{3,3} has a nontrivial signed column dependence.
available · lemma · proved · certified · supported · obstructed
Parent: [specialedge_nullity_conjecture]
**Consumer:** special-edge nullity conjecture
**Warning:** nonspecial incidence columns can support dependence entirely among themselves
**Role:** fence

## [ascending_terminal_graph_can_contain_a_rainbow_fouredge_path] The ascending terminal graph can contain a rainbow four-edge path, so the global ascending-edge bound cannot follow merely from rainbow-P4-freeness.
available · lemma · proved · certified · supported
Parent: [ascendingedge_rainbowlayer_formulation]
**Consumer:** global ascending-edge bound
**Warning:** do not try to prove the global ascending-edge bound by claiming that the ascending terminal graph has no rainbow four-edge path
**Role:** fence

## [ascending_terminal_graph_need_not_be_a_pseudoforest] Ascending terminal graph need not be a pseudoforest.
available · lemma · proved · certified · supported
Parent: [ascendingedge_rainbowlayer_formulation]
**Consumer:** ascending-edge structural route
**Warning:** do not try to prove the ascending terminal graph is a forest or pseudoforest
**Role:** fence

## [nonascending_badload_blocker_bound] Nonascending bad-load blocker bound.
available · lemma · proved · certified · supported
Parent: [entrancerank_distortion_by_blockers]
**Given:** ["entrance-rank distortion by blockers"]
**Consumer:** bad-load truncation and dense-core routes
**Consequence:** bad load splits into ascending load plus a path-blocked component of size at most 2a(x)-2

## [falsification_search_for_the_potentialoriented_local_bound] Finite falsification search for the potential-oriented local bound.
available · lemma · evidence · certified · evidence
Parent: [potentialoriented_local_bound_for_ascending_terminal_edges]
**Consumer:** potential-oriented local bound
**Observed Max Oriented Terminal Count:** 3
**Scope Fence:** finite generated samples only

## [ascending_edges_at_one_last_vertex_can_have_unbounded_gap] Ascending edges at one last vertex can have unbounded φ-gap.
available · lemma · proved · certified · supported
Parent: [refuted_ascending_terminaldegree_conjecture]
**Consumer:** ascending terminal-degree conjecture
**Warning:** do not assume ascending edges sharing a last vertex have adjacent or bounded-difference φ-values
**Role:** fence
**Sharpness:** φ-ratio can approach 2 from below

## [refuted_compensated_terminaldegree_conjecture] The inequality a(v)≤3+h(v) is false: a certified example has a(v)=4 and h(v)=0.
available · theorem · conjecture · not_required · unchecked · obstructed
Parent: [refuted_ascending_terminaldegree_conjecture]
**Role:** refuted_conjecture
**Lesson:** The favorable H_2 term does not locally compensate all excess ascending last-vertex incidences.
**Refuted By:** four_ascending_edges_can_share_one_last_vertex

## [shadowrainbow_reduction_and_its_blackbox_23_ceiling] Shadow-rainbow reduction and its black-box 2/3 ceiling.
available · lemma · proved · certified · supported
Parent: [rainbowshadow_formulations_for_3uniform_linear_paths]
**Consumer:** general upper-bound strategy
**Role:** alternative reduction plus route ceiling
**Gap:** improvement below 2/3 requires structure beyond generic properly colored graphs

## [rank_controls_nonspecial_incidence_nullity_up_to_entrance_rank] For nonspecial edges, nullity_R(N_ns) <= β(T)+h, and for the full incidence matrix nullity_R(N) <= β(T)+h+s.
available · lemma · proved · certified · supported
Parent: [rotationexpansion_route_for_forcing_specialedge_density]
**Given:** ["unique entrance for nonspecial edges","terminal-pair graph T","incidence matrix"]
**Consumer:** ["special-edge nullity route","terminal-pair cycle-rank route"]
**Consequence:** terminal-cycle control automatically yields incidence-nullity control, with an additive entrance-support term
**Next Need:** reduce the entrance-rank term h or prove β(T)+h<=Cs+Dn with constants strong enough for a coefficient gain

## [terminalpair_cyclerank_reduction] If the terminal-pair graph satisfies β(T) <= C s + D n, then m <= [2(C+1)ℓ-3(C+1)+D+1]/(2C+3) · n, giving a leading coefficient below 1 for fixed C,D.
available · lemma · proved · certified · supported
Parent: [rotationexpansion_route_for_forcing_specialedge_density]
**Given:** ["unique entrance for each nonspecial edge","special-edge hinge 2m+s<=(2ell-3)n"]
**Need:** bound the cycle rank of the terminal-pair graph in terms of s and n
**Consumer:** general leading-coefficient improvement
**Calibration:** beta(T)<=s implies coefficient 4/5; beta(T)=O(n) implies coefficient 2/3

## [crossblocker_reduction_for_charged_fouredge_spacing] Under the stated canonical-entrance disjointness hypotheses for e1,e2,e4, one has 2q2≥q1+q4+2.
available · lemma · proved · certified · supported
Parent: [spacing_conjecture_for_potentialcharged_ascending_edges]
**Given:** ["ascendingness of e_1,e_2,e_4","canonical entrance path for e_1","a largest-edge precursor Q"]
**Consumer:** ["charged four-edge spacing conjecture","location-sensitive uncrossing route"]
**Consequence:** a spacing counterexample must violate at least one of the explicit disjointness conditions: e_2 has an additional Q-contact, e_1 hits the x_2-tail, or the canonical entrance witness R for e_1 hits e_4 or that tail

## [path_refutes_automatic_production_of_a_genuine_endpoint_lens] A loose path refutes automatic production of a genuine endpoint lens.
available · lemma · proved · certified · supported
Parent: [a_maximum_endpoint_path_manufactures_a_balanced_endpoint_lens]
**Given:** ["explicit acyclic linear 3-graph"]
**Need:** Establish actual divergence and rejoining and both legal exchanges before using a genuine balanced lens.
**Consumer:** ["paid four-edge source-rail route","automatic balanced endpoint lens"]

## [cumulative_snakerank_indegree_bound] Cumulative snake-rank indegree bound.
available · lemma · proved · certified · supported
Parent: [snake_and_terminalcontact_accounting_route]
**Given:** linear r-graph; snake digraph; terminal rank phi(e,v)
**Need:** exploit rank distribution rather than only total indegree
**Consumer:** special-edge density / weighted snake counting
**Strengthening:** low-rank cumulative control independent of higher-rank incidences

## [matchings_in_each_cyclic_sts13_orbit_have_two_affine_types] Three-block matchings in each cyclic STS(13) orbit have two affine types.
available · lemma · proved · certified · supported
Parent: [each_cyclic_sts13_block_orbit_has_matching_number_three]
**Given:** ["0d23d6f61838 orbit matching-number lemma","cyclic affine automorphisms"]
**Consumer:** ["09b3a90c50a9 robust specialness under matching deletions"]
**Consequence:** The heavy side of every 3+1 deletion matching reduces to two canonical affine matching types.
**Next Need:** For each heavy matching type, quotient the possible single opposite-orbit deletion by its residual stabilizer and construct two-entrance spanning paths for each surviving edge; separately handle the 2+2 split.

## [endpoint_paths_do_not_survive_arbitrary_matching_deletions] Three affine endpoint paths do not survive arbitrary matching deletions.
available · lemma · proved · certified · supported
Parent: [every_matching_deletion_of_cyclic_sts13_is_allspecial]
**Consumer:** all_matching_deletions_of_cyclic_sts13_are_allspecial
**Role:** route fence
**Next Need:** Construct additional A0-ending spanning paths beyond the C3 affine-stabilizer orbit, or use a structural minimum-degree/rotation proof.

## [rank_floor_and_layer_recurrence_have_disjoint_support] Minimum-degree rank floor and layer recurrence have disjoint support.
available · working_unit · proved · certified · supported
Parent: [densecore_allspecial_conjecture]
**Given:** ["b3f79b5fc50d/e4d8031f23a1 minimum-degree ascending-rank floor","e766796773d9 ascending-layer recurrence"]
**Consumer:** ["dense-core all-special route","rank-layer expansion"]
**Consequence:** the two tools have no forcing overlap; iterating the current recurrence after the rank floor is vacuous

## [nonspeciality_need_not_propagate_to_maximum_path_rank] Nonspeciality need not propagate to maximum path rank.
available · lemma · proved · certified · supported
Parent: [refuted_maximumrank_nonspecial_edge_degree_conjecture]
**Consumer:** unrestricted propagation of nonspeciality to maximum edge rank
**Role:** fence
**Main Route Relevance:** outside the admissible minimum-degree regime; dense minimum degree may still force propagation
**Minimum Degree:** 1

## [star_obstruction_to_unrestricted_allspecialness] Star obstruction to unrestricted all-specialness.
available · lemma · proved · certified · supported
Parent: [densecore_allspecial_conjecture]
**Consumer:** dense-core all-special conjecture
**Warning:** minimum-degree hypothesis is essential
**Role:** fence

## [minimum_degree_forces_ascending_edges_to_have_large_2] Minimum degree forces ascending edges to have large φ.
available · lemma · proved · certified · supported
Parent: [minimumdegree_local_ascendingneighbor_bound]
**Consumer:** ["minimum-degree local ascending-neighbor bound","dense-core all-special route"]
**Correction:** statement restored with a correct opposite-endpoint proof; c3e95f4ce77d was never a counterexample because its global minimum degree is 3
**Proved By:** minimum_degree_forces_ascending_edges_to_have_large

## [minimum_degree_forces_ascending_edges_to_have_large_3] Minimum degree forces ascending edges to have large φ.
available · lemma · proved · certified · supported
Parent: [minimumdegree_local_ascendingneighbor_bound]
**Consumer:** ["minimum-degree local ascending-neighbor bound","dense-core all-special route"]
**Correction:** statement restored with a correct opposite-endpoint proof; c3e95f4ce77d was never a counterexample because its global minimum degree is 3
**Proved By:** minimum_degree_forces_ascending_edges_to_have_large

## [alternate_break_forces_a_nonlocal_blocker_or_terminal_theta] A Type-B loss-one alternate break forces either a nonlocal double blocker or a terminal theta containing cycles of lengths q−1, q, and 3.
available · lemma · proved · certified · supported
Parent: [sharp_minimumdegree_lower_bound_conjecture_for_ascending_edges]
**Given:** ["boundary q=delta","loss-one Type-B sink","exact Type-B saturation","deficiency-two sink normal form"]
**Consumer:** ["Type-B boundary elimination","unified loss-one theta obstruction","sharp ascending-rank conjecture"]
**Consequence:** The canonical Type-B alternate break exposes either a nonlocal final-cell blocker or a terminal theta with branch lengths q-2,1,2.
**Next Need:** Exploit the nonlocal blocker or derive a common minimum-degree escape lemma for the resulting theta.

## [always_escapes_and_loss_one_has_exactly_two_exceptional_forms] Boundary states with loss at least two always admit further safe motion, while loss-one sinks have exactly two exceptional forms.
available · lemma · proved · certified · supported
Parent: [sharp_minimumdegree_lower_bound_conjecture_for_ascending_edges]
**Consumer:** ["sharp ascending-rank route","loss-one terminal-theta route"]
**Consequence:** Loss two cannot be a sink; loss one has only two exact exceptional blocker/clean-edge configurations.

## [blocker_system_with_terminalpair_control_on_clean_replacements] Around a maximum-rank nonspecial edge, terminal blockers form three edge-disjoint matchings, while clean entrance replacements have rank L and controlled interaction with the original terminal pair.
available · lemma · proved · certified · supported
Parent: [sharp_minimumdegree_lower_bound_conjecture_for_ascending_edges]
**Consumer:** ["three-color blocker route","dense-core all-special route"]
**Consequence:** Double blockers form a proper three-color matching system, and special clean entrance replacements have all alternate longest witnesses hit {y,z}.

## [defect_accounting_and_oppositeterminal_splice_dichotomy] Two-terminal blocker systems satisfy exact defect identities, and opposite-terminal single blockers either form a 3-cycle, give a bridge splice, or meet at a consecutive-edge joint.
available · lemma · proved · certified · supported
Parent: [sharp_minimumdegree_lower_bound_conjecture_for_ascending_edges]
**Given:** ["two-terminal alternating blocker matching system","globally longest path"]
**Consumer:** ["maximum-rank nonspecial-edge degree conjecture","Posa endpoint expansion","alternating blocker defect route"]
**Consequence:** Open alternating components are exactly terminal single/unused defects, terminal degree is their signed defect balance, and opposite-terminal single defects obey a bridge/joint/triangle dichotomy.
**Next Need:** Apply the splice dichotomy to alternating-component endpoints and control terminal triangles and joint-forced adjacent pairs.

## [defects_and_their_ordered_locations_in_saturated_boundary_fans] In a saturated boundary fan, open-chain endpoints are exactly the singleton or uncovered blocker defects; X-type defects lie in the final cell while Y/Z defects lie earlier.
available · lemma · proved · certified · supported
Parent: [sharp_minimumdegree_lower_bound_conjecture_for_ascending_edges]
**Consumer:** ["second-level Pósa expansion","sharp ascending-rank route"]
**Consequence:** Open chains carry exactly the exceptional defects, with X pinned to the final cell and Y/Z strictly earlier.

## [endpointpotential_floor_and_a_stronger_ascendingedge_rank_floor] Every vertex satisfies φ(v)≥⌈(δ+1)/2⌉, so every ascending nonspecial edge satisfies φ(e)≥⌈(δ+3)/2⌉.
available · lemma · proved · certified · supported
Parent: [sharp_minimumdegree_lower_bound_conjecture_for_ascending_edges]
**Consumer:** ["dense-core all-special route","minimum-degree rank layers"]
**Consequence:** Every endpoint has potential at least about delta/2, and every ascending nonspecial edge starts one rank higher.

## [fans_are_degreetwo_cell_graphs_with_rigid_adjacentcell_blockers] A saturated boundary fan yields a degree-two cell multigraph, and every adjacent-cell double blocker is forced through the forward joint of the later cell.
available · lemma · proved · certified · supported
Parent: [sharp_minimumdegree_lower_bound_conjecture_for_ascending_edges]
**Consumer:** ["second-level Pósa expansion","sharp ascending-rank route"]
**Consequence:** The saturated sink is a degree-two defect graph, and every adjacent-cell edge is forced to point through a specific forward joint.

## [fans_form_alternating_blocker_systems_with_defects_pinned_at_x] Two deficiency-two safe sinks induce edge-disjoint blocker matchings whose union is alternating cycles together with at most one nontrivial alternating path, with defects pinned at x.
available · lemma · proved · certified · supported
Parent: [sharp_minimumdegree_lower_bound_conjecture_for_ascending_edges]
**Given:** ["common deficiency-two path","both opposite endpoints are safe sinks"]
**Consumer:** ["Type-B alternate-break comparison","boundary Posa expansion","alternating blocker uncrossing"]
**Consequence:** Two simultaneous sink fans reduce exactly to edge-disjoint alternating matchings whose only open defects are pinned at x and at most two secondary vertices.
**Next Need:** Identify the secondary defects forced by the Type-B alternate break and uncross the remaining open alternating chain into a safe rotation or terminal transfer.

## [flat_chains_require_labeled_overlap_not_generic_twopath_overlap] An all-entrance flat-transfer chain supplies consecutive (q−2)-edge entrance-to-entrance paths, so any closure argument must exploit their labeled overlap and inherited blocker memory rather than generic path overlap alone.
available · proof_level · proposal · not_required · unchecked
Parent: [flattransfer_joint_classification_and_entrancetoentrance_path]
**Given:** ["entrance-to-entrance transfer paths","one-edge blocker memory","potential classification of cycle joints"]
**Consumer:** ["flat-transfer chain route"]
**Fence:** do not claim two bounded-cross-degree induced paths automatically contain a path of length 3q/2
**Missing Obligation:** prove a labeled overlap/uncrossing lemma using blocker identities or endpoint potentials; generic bounded-degree overlap is insufficient

## [forces_high_degree_in_the_fixedentrance_rotation_graph] If an ascending edge has rank q≤δ−1, every fixed-entrance rotation state has at least 4(δ−q)−2 distinct safe-rotation neighbors.
available · lemma · proved · certified · supported
Parent: [give_endpointpreserving_rotations_safe_below_the_boundary]
**Given:** ["endpoint deficiency blocker inequality","safe single-blocker rotation","ascending edge canonical entrance path"]
**Consumer:** ["minimum-degree all-special route","rotation-state expansion","sharp ascending-rank conjecture"]
**Consequence:** Any ascending edge lying d=delta-q below the minimum-degree boundary generates a fixed-entrance rotation state of degree at least 4d-2; only the near-boundary band can have low branching.
**Next Need:** Exploit high rotation-state degree globally, e.g. by forcing nonlocal cycles, terminal-label switches, or blocker accumulation.

## [has_a_fixed_hole_with_unavoidable_external_attachment_surplus] A canonical loss-one two-cycle has a fixed omitted vertex with enough external incidence to force either a disjoint external edge or at least two one-contact external chords.
available · lemma · proved · certified · supported
Parent: [sharp_minimumdegree_lower_bound_conjecture_for_ascending_edges]
**Consumer:** ["fixed-hole escape","sharp ascending-rank route"]
**Consequence:** The canonical loss-one two-cycle has one fixed omitted vertex whose star necessarily escapes the original path.

## [corrected_fixedhole_twochord_bridge] Two suitably separated one-contact chords through a fixed external hole splice into the path and can restore full length in the loss-one setting.
available · lemma · proved · certified · supported
Parent: [two_fixedhole_onecontact_chords_give_an_exact_bridge_splice]
**Given:** ["two one-contact external chords through an omitted vertex","right contact is not the prescribed last vertex"]
**Consumer:** ["loss-one fixed-hole escape","sharp ascending-rank conjecture"]
**Consequence:** the bridge formula survives; only a right-hand contact at x destroys the prescribed x-ending orientation

## [index_graphs_forcing_a_nonlocal_blocker_or_lossless_rotation] A loss-one safe sink has a saturated maximum-degree-two blocker index graph and must expose either a lossless double-blocker rotation or a nonlocal double blocker.
available · lemma · proved · certified · supported
Parent: [sharp_minimumdegree_lower_bound_conjecture_for_ascending_edges]
**Given:** ["boundary q=delta","loss-one sink normal form"]
**Consumer:** ["sharp ascending-rank conjecture","Type-B alternate break","second-level Posa expansion"]
**Consequence:** Every loss-one sink has an exact saturated cell-index graph and therefore exposes either a lossless double rotation or a nonlocal blocker.
**Next Need:** Analyze the minimal-loss nonlocal blocker; distance-two/private is the only nonlocal pattern producing loss one.

## [saturated_boundary_fans_force_a_nonlocal_blocker] A saturated boundary fan either has a lossless consecutive double-blocker splice or contains a nonlocal double blocker; two simultaneous sink fans cannot both avoid such a nonlocal blocker.
available · lemma · proved · certified · supported
Parent: [sharp_minimumdegree_lower_bound_conjecture_for_ascending_edges]
**Consumer:** ["sharp ascending-rank conjecture","location-sensitive Minty/Posa route","second-level Posa expansion"]
**Consequence:** A two-sided canonical sink at q=delta>=5 cannot remain in nearest-neighbor ladder geometry; some endpoint exposes a lossy nonlocal splice.
**Next Need:** Combine nonlocal splice loss with deficiency-surplus control and close the remaining small-loss cases.

## [structure_and_escape_in_the_boundary_fixedtarget_rotation_graph] The boundary fixed-target rotation graph has minimum degree at least two; its triangles and chordless 4-cycles have rigid local normal forms and always admit an external noninverse exit.
available · lemma · proved · certified · supported
Parent: [sharp_minimumdegree_lower_bound_conjecture_for_ascending_edges]
**Given:** ["boundary fixed-target entrance paths","endpoint-preserving single-blocker rotation formula","minimum degree at least q"]
**Consumer:** ["quotiented rotation-state route","boundary q=delta attack","cube/square obstruction route","flat-transfer recurrence"]
**Consequence:** The fixed-target rotation graph has genuine branching; its triangle and chordless-square gadgets are bounded-depth far-end phenomena and cannot be closed recurrent components.
**Next Need:** Suppress or quotient the local triangle/square gadgets and analyze the first remaining nonlocal cycle or block.

## [switch_cycles_force_rankq_commonentrance_escape_structure] A terminal-label switch closes a rank-q linear cycle, and favorable ears at its private entrance have rank q with controlled entrance structure.
available · lemma · proved · certified · supported
Parent: [sharp_minimumdegree_lower_bound_conjecture_for_ascending_edges]
**Given:** ["boundary fixed-target entrance rotation graph","terminal-label switch"]
**Consumer:** ["switch-cycle residual classification","same-entrance branching route","dense-core all-special conjecture"]
**Consequence:** A label switch creates a q-cycle with private entrance x; minimum degree then forces either a favorable rank-q ear or at least two one-contact ears.
**Next Need:** Control the residual one-contact ears whose contacts avoid both neighboring private slots.

## [graphs_are_rainbowpathfree_and_have_logarithmic_reciprocal_mass] Positive potential-gap terminal graphs are rainbow-path-free and have logarithmic reciprocal mass.
available · lemma · proved · certified · supported
Parent: [snake_and_terminalcontact_accounting_route]
**Consumer:** ["rank-cluster dichotomy","general upper-bound program"]
**Consequence:** Positive entrance-to-terminal potential gaps have globally bounded harmonic mass.

## [longestpath_terminal_degree_with_exact_doubleblocker_slack] Longest-path terminal degree with exact double-blocker slack.
available · lemma · proved · certified · supported
Parent: [snake_and_terminalcontact_accounting_route]
**Consumer:** ["terminal defect accounting","maximum-rank blocker route"]
**Consequence:** The standard terminal-degree bound has an exact extra penalty for double blockers.

## [does_not_yet_supply_payment_at_the_minimumrank_terminal] Payment at one terminal does not yet supply payment at the minimum-rank terminal
available · working_unit · proposal · not_required · unchecked
Parent: [on_the_paid_twoterminalgap_subclass_breaks_4348_saturation]
**Given:** ["many_paidcertified_edges_have_strict_rank_gap_at_both_terminals","on_the_paid_twoterminalgap_subclass_breaks_4348_saturation"]
**Need:** Transfer payment to a minimum-rank terminal or retain positive linear mass of such certificates.
**Consumer:** ["four-edge spacing with payment at the common terminal"]

## [rotation_terminal_incidences_are_globally_paid_by_local_defect] Distinct flat rotation terminal incidences are globally paid by local defect.
available · lemma · proved · certified · dependency_hold
Parent: [outputs_with_no_endpoint_rise_land_at_aligned_defect_vertices]
**Given:** ["631ebe3d4728 flat-output aligned-sink lemma","b032348c1a8a aligned defect bound","fixed-entrance terminal count"]
**Consumer:** ["e233684ca13b endpoint-congestion route","post-43/48 rotation packing"]
**Consequence:** Distinct flat ascending no-rise outputs no longer require endpoint-reuse control: after deduplication by (edge,last vertex), they are at most 4eta+O(n_+). Only repeated production of the identical terminal incidence remains.
**Next Need:** Bound how many different source vertices can produce the same flat certificate (h,w). Any O(1), or sufficiently small aggregate, bound now charges the entire flat branch to eta+O(n_+).

## [singleton_transfer_is_periodic_away_from_few_defects] If a singleton-transfer walk is within D of the 3/4-per-column optimum, all but at most 4D+6 transitions follow the unique period-four pattern 2,1,0,0.
available · lemma · proved · pending · unchecked · pending
Parent: [contactconflict_graph_improves_the_leading_coefficient_to_4348]
**Given:** ["1000904 singleton-column transfer automaton and potential function"]
**Need:** Independent verification of the exact defect count and period-four decoding.
**Consumer:** ["near-equality analysis of terminal contact patterns"]

## [rankthree_incoming_localization_is_sharp_at_rank_four] Rank-three incoming localization is sharp at rank four.
available · lemma · proved · certified · supported
Parent: [snake_and_terminalcontact_accounting_route]
**Consumer:** ["special-edge density","ascending terminal-degree route"]
**Consequence:** Low-rank nonspecial incoming degree is at most two through rank 3, and rank 4 is the first unrestricted obstruction.

## [reciprocal_stretch_bound_for_ascending_edges] Reciprocal stretch bound for ascending edges.
available · lemma · proved · certified · supported
Parent: [snake_and_terminalcontact_accounting_route]
**Given:** ["potential-threshold rainbow graphs","terminal potential band","rainbow path Turan bound"]
**Consumer:** ["multi-scale ascending-defect control","2/3-leading-coefficient program"]
**Consequence:** The factor-two threshold band and all rank layers combine into the unconditional reciprocal-stretch bound 5n/4.
**Limitation:** Nearly rank-tight ascending edges can still contribute very little, so this alone does not change the Turan leading coefficient.

## [force_a_cycle_or_adjacent_sourcepath_lastedge_containment] Endpoint-retaining repeated intersections force a cycle or adjacent source-path last-edge containment.
available · lemma · proved · certified · supported
Parent: [intersection_gives_a_linear_cycle_or_a_shared_last_edge]
**Given:** ["endpoint-retaining repeated intersections x_j,x_{j+1} in V(R_i)","41100a9882dd cycle-or-shared-last-edge lemma","source-clean chosen paths R_j,R_{j+1}"]
**Consumer:** ["hard residue of U_11 color-terminal collisions","foreign-last-edge containment route","post-43/48 source-path structure"]
**Consequence:** Two endpoint-retaining repeated source-path intersections force cycles or containment of the two adjacent source-path last edges.
**Next Need:** Use this only when the repeated-intersection mechanism also retains the smaller path endpoint on R_i; bare two-vertex overlap is insufficient.

## [weighted_badload_truncation_by_edge_potential] Weighted bad-load truncation by edge potential.
available · lemma · proved · certified · supported
Parent: [snake_indegree_lemma]
**Consumer:** ["distribution-sensitive incidence-rank bounds","general leading-coefficient improvement"]
**Consequence:** Bad-load truncation extends to arbitrary monotone phi-weights; the unweighted inequality is a specialization.

## [to_neartop_clean_chords_and_highpotential_rotation_endpoints] Ascending-edge defect reduces to near-top clean chords and high-potential rotation endpoints.
available · lemma · proved · certified · supported
Parent: [snake_and_terminalcontact_accounting_route]
**Given:** ["joint snake-incidence and blocker budget","charged-path local structure"]
**Consumer:** ["general upper-bound leading coefficient","sublinear charged-degree program","Pósa endpoint expansion"]
**Consequence:** All leading-order ascending difficulty is localized to near-top-rank clean entrance chords and terminal-only rotations that generate large high-potential endpoint sets.
**Next Need:** Control overlap or merging of the high-potential endpoint sets across charged terminals, or force a positive fraction into double blockers or rank-deficient clean chords.

## [the_fiveregular_sts13_puncture_contains_a_linear_fivecycle] The 12-vertex punctured cyclic STS(13) contains a linear 5-cycle, so its finite-field additive blow-ups have paths of length 5q-O(1) and cannot improve the asymptotic one-third lower-bound coefficient.
available · lemma · proved · certified · supported
Parent: [proof_for_the_punctured_cyclic_sts13_allspecial_calibration]
**Given:** ["cyclic STS13 block description","additive cycle-lift lemmas"]
**Consumer:** ["general lower-bound construction search"]
**Consequence:** the 5-regular P6-free calibration does not provide a circumference-deficient additive blow-up seed

## [2020_minimum_degree_and_long_linear_paths_in_general_3graphs] Ma–Hou–Gao (2020): minimum degree and long linear paths in general 3-graphs.
available · theorem · proved · certified · supported
Parent: [literature_state_for_linear_hypergraph_paths]
**Consumer:** minimum-degree-first route
**Role:** minimum-degree path literature and endpoint-neighborhood methodology
**Limitation:** general-3-graph thresholds scale as k n and are not directly useful for linear 3-graphs

## [ergemlidzegyrimethuku_rainbow_path_turn_bound] Ergemlidze–Győri–Methuku rainbow path Turán bound.
available · theorem · proved · certified · supported
Parent: [literature_state_for_linear_hypergraph_paths]
**Consumer:** ["potential-threshold rainbow graphs","multi-scale ascending-edge bounds"]
**Role:** average-degree/rainbow-Turan path bound

## [gyrfsruszinksrkzy_2022_acyclic_triple_systems] Gyárfás–Ruszinkó–Sárközy (2022): acyclic triple systems.
available · theorem · proved · certified · supported
Parent: [literature_state_for_linear_hypergraph_paths]
**Role:** historical general upper and exact P2-P4 baseline

## [gyrisalia_2025_linear_3graphs_without_long_berge_paths] Győri–Salia (2025): linear 3-graphs without long Berge paths.
available · theorem · proved · certified · supported
Parent: [literature_state_for_linear_hypergraph_paths]
**Role:** Erdos-Gallai-style method and factor-of-two comparison

## [ramani_2026_fouredge_paths_via_incidence_rank] Ramani (2026): four-edge paths via incidence rank.
available · theorem · proved · certified · supported
Parent: [literature_state_for_linear_hypergraph_paths]
**Role:** current sharp P4 theorem; cograph/incidence-rank toolkit

## [tangwuzhang_2026_exact_p5_and_general_conjectural_scale] Tang–Wu–Zhang (2026): exact P5 and general conjectural scale.
available · theorem · proved · certified · supported
Parent: [literature_state_for_linear_hypergraph_paths]
**Role:** exact P5 calibration; conjectural asymptotic target; MPTS lower construction

## [zhouyuan_2025_general_runiform_path_upper_bound] Zhou–Yuan (2025): general r-uniform path upper bound.
available · theorem · proved · certified · supported
Parent: [literature_state_for_linear_hypergraph_paths]
**Role:** published general-r comparison benchmark
