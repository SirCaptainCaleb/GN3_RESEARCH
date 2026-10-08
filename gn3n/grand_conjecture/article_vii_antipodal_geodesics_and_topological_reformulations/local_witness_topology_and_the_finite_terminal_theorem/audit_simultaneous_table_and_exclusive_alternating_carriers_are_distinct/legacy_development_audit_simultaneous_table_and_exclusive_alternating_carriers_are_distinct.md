# Audit: simultaneous table and exclusive alternating carriers are distinct — preserved pre-item development

## Development

## A simultaneous-occurrence table proves a different claim

The antipodality observation in [[positive_word_filtration_is_antipodal_and_exclusive_alternating_windows_collapse]] is correct: reverse-complement preserves \(001,011,0101\), so a positive-word filtration is consistent with chamber reversal.

Its displayed four-case table, however, assumes the word segment
\[
0101xy0101.
\]
That segment contains both reflected alternating occurrences in the same chamber. An exclusive carrier instead has exactly one occurrence in each chamber, with the other occurrence appearing in another chamber. The table therefore proves noncoexistence at separation six; it does not by itself eliminate an exclusive carrier.

The exclusive conclusion is nevertheless true. A complete one-polarity face proof is given in [[positive_protection_eliminates_exclusive_disjoint_alternating_carriers]]. It uses the four-vertex coupling block and independently permutes its vertices; no chamber with simultaneous occurrences is assumed.

For example the words \(0101000001\) and \(0111110101\) separately satisfy the inward positive-word exclusions at the relevant starts. The first has only the left terminal alternating occurrence, and the second only the right. Eliminating their realization as an exclusive face requires the block argument, not wordwise noncoexistence.

The reflected-double alternating conclusion is supplied separately, in stronger form, by [[positive_alternating_double_occurrences_have_support_at_most_eight]]. Thus the concurrent addendum's intended compression conclusion can be retained with corrected proof references: the exclusive disjoint alternating branch is impossible, and the alternating double branch has at most eight determining vertices.

The remaining unbounded reflected-double branch is span-two. Protected endpoint transport also has a separate exception on the surviving exclusive disjoint span-two support of order ten, identified in [[balanced_ten_position_repairs_have_explicit_protected_endpoint_orbits]].
