# Clean-prefix sparse-fault charts cannot force general closure

- Stable ID: note_clean_prefix_sparse_fault_chart_obstruction
- Author: unspecified; session provenance retained
- Primary home: subsection:arbitrary_nonlinear_coordinate_faults_and_robust_affine_closure
- Labels: obstruction, partial_argument
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r4593_2
- Updated session: session_nori_r4593_2
- Disposition: none
- Successor: none

## Related references

- subsection:arbitrary_nonlinear_coordinate_faults_and_robust_affine_closure, exact version 1

## Research note

Editorial extraction: precise original proof retained below.

Source: arbitrary_nonlinear_coordinate_faults_and_robust_affine_closure composition v1

## A sharp structural obstruction to completing NORI by sparse-fault clean-prefix charts alone

Fix a distinguished three-coordinate set K⊂[n], let D=[n]\K of size m=n−3>=3, and let \mathscr T be the set of unordered triples of directions inside D on which a proposed clean full-exterior-parity reference MAY fail. The recent robust-root-chart closure results construct actual monochromatic-prefix witness charts ONLY from direction permutations p of D whose every consecutive 3-direction window avoids \mathscr T.

**THEOREM (one-coordinate star destroys every clean full prefix).** Fix ANY direction t∈D, and put
\[
\mathscr T_t=\{T\in\binom D3:t\in T\}.
\]
Then \(|\mathscr T_t|=\binom{m-1}{2}=\Theta(m^2)\). EVERY permutation p=(p_1,...,p_m) of D contains AT LEAST ONE consecutive 3-direction window whose unordered direction set belongs to \mathscr T_t. Consequently there are NO admissible clean-prefix order charts if one insists on avoiding all triples in \mathscr T_t, regardless of the color values, physical faces, or NORI antipodal-reversal law.

**Proof.** The distinguished direction t appears at some position j of the permutation. Because m>=3, at least one consecutive block of three positions contains j (choose the first block if j<=3, the last block if j>=m−2, and any containing block otherwise). That consecutive three-direction set contains t, and so belongs to \mathscr T_t. Since every p has such a window, no clean avoiding permutation exists. The number of forbidden unordered triples is exactly \binom{m-1}{2}. QED.

**THEOREM (single-root-bit polarization stops at exactly r exceptional terminal windows).** More generally, in the ordered-r-face model, appending k exceptional coordinate directions to a clean prefix gives k exceptional r-windows. One of those exceptional directions belongs to ALL k free coordinate sets IF AND ONLY IF k<=r. For k>=r+1 the first and last exceptional windows have DISJOINT exceptional-direction sets. For active NORI r=3, toggling one exceptional root bit can preserve every exceptional suffix window at once when k<=3, but not k>=4. This is the already proved terminal-common-free-coordinate theorem nori_suffix_polarization_terminal_r_window_common_free_direction_sharp_threshold_20261008.

**CONCLUSION (method barrier, NOT conjecture counterexample).** These two elementary facts show why the recent O(n²) arbitrary-fault robustness cannot be promoted to unrestricted NORI merely by tightening the random-order avoidance bound: an explicit O(n²)-size forbidden family blocks ALL clean order witnesses. Furthermore, folding that fourth problematic direction into K and attempting the same single-root-bit suffix-polarization proof fails at exactly four exceptional windows. The *grand conjecture itself* is not contradicted. But unrestricted closure needs genuinely NEW machinery: (i) actual reachability/terminal-memory charts that traverse non-reference windows rather than avoiding them, (ii) a multi-bit or root-mobile polarization allowing four or more exceptional windows, or (iii) a direct topological forcing theorem for exact complementary reversed-tail label intersections with no parity normal form.

**Research priority.** Treat 'extend quadratic r' and 'remove parity reference' as qualitatively different problems. The first cannot logically settle the second. Aim instead at the general NORI exact color-free reversed-tail reachability sets R_J(x), preserving ordered two-direction memory, and force R_(a,b)(x) ∩ complement_D(R_(b,a)(x)) nonempty for some root x.

The rigorous closure theorems apply to the stated number and location of arbitrary faults; sharp obstruction constructions show why the same argument cannot simply be iterated to cover unrestricted colorings.
