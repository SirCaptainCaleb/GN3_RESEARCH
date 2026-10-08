# Corrected positive-word terminal theorem with one unbounded corridor — preserved pre-item development

## Corrected positive-word terminal theorem: one explicit unbounded branch remains

Use the single witness language
\[
\mathcal W_+=\{001,011,0101\}.
\]
This is closed under reverse-complement:
\[
\operatorname{rc}(001)=011,qquad
\operatorname{rc}(011)=001,qquad
\operatorname{rc}(0101)=0101.
\]
Hence the reflected-location witness path and its unsigned depth are antipodally well-defined using only positive witnesses. A two-cover order is exactly a word avoiding \(\mathcal W_+\), so the same predicate is also the one removed by terminal two-cover surgery.

This repairs the polarity mismatch recorded in [[audit_terminal_surgery_and_compression_use_different_witness_polarities]]. However the stronger conclusion asserted in [[positive_only_witness_filtration_is_antipodal_and_surgery_compatible]]—that every terminal support is bounded by ten—is false because of [[positive_reflected_double_carriers_have_unbounded_local_spans]].

The correct classification is:

1. Centered span-two and centered alternating occurrences have bounded determining support.
2. Overlapping reflected windows are bounded by their literal union; the alternating overlap-one residue is eliminated by [[positive_overlap_one_alternating_elimination]].
3. Exclusive disjoint span-two carriers have adjacent determining windows by [[exclusive_disjoint_terminal_windows_are_adjacent_without_dual_polarity]], hence full support of order at most ten.
4. Exclusive disjoint alternating carriers do not occur by [[positive_protection_eliminates_exclusive_disjoint_alternating_carriers]].
5. Reflected alternating double occurrences have support of order at most eight by [[positive_alternating_double_occurrences_have_support_at_most_eight]].
6. Reflected span-two **double** occurrences are the unique unbounded positive terminal geometry. Their middle interval is nevertheless \(\mathcal W_+\)-free and therefore has the exact two-cover corridor form classified in [[complete_positive_span_two_double_corridor_classification]].

Thus the six-word/three-word mismatch is no longer the repair frontier. Compression and surgery can consistently use \(\mathcal W_+\) throughout. The price is that the finite-terminal theorem must be replaced by a finite-plus-corridor theorem:
\[
\boxed{
\text{positive terminal carrier}
\Longrightarrow
\begin{cases}
\text{bounded support of order at most ten},\\
\text{or a reflected span-two double corridor.}
\end{cases}}
\]

For the bounded branch, the existing ten-vertex two-cover surgery is predicate-compatible. For the corridor branch, the full span may be arbitrarily long, so no bounded-support theorem can close it. The remaining local obligation is exactly to produce a \(\mathcal W_+\)-outward repair of the double corridor, with the frozen-window/nesting conditions of [[frozen_window_carriers_and_separator_relabeling_require_precise_invariants]] imposed afterward for the protected carrier recursion.

This statement is compatible with all explicit positive-word counterexamples currently recorded: they lie in the reflected span-two double branch rather than refuting the positive filtration itself.
