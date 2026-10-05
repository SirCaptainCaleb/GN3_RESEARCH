# Exclusive disjoint terminal windows are adjacent without dual polarity

## Metadata

- ID: exclusive_disjoint_terminal_windows_are_adjacent_without_dual_polarity
- Parent Section: local_witness_topology_and_the_finite_terminal_theorem
- Position: 6
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Cold composition

(none yet)

## Development

## The exclusive disjoint branch has adjacent windows without using dual polarity

The numerical compression of a genuinely exclusive disjoint carrier can be salvaged without declaring that carrier impossible.

**Proposition.** Let \(F\) be an ordered-partition face, and let \(U,V\) be disjoint consecutive positional intervals, with \(U\) to the left of \(V\). Suppose a left indicator depends only on the order in \(U\), a right indicator only on the order in \(V\), exactly one indicator is one in every chamber of \(F\), and each indicator is one in some chamber. Then \(U,V\) are adjacent positional intervals: no vertex position lies strictly between them.

**Proof.** If no face block meets both intervals, the variables determining their indicators belong to disjoint collections of face blocks. Choose the left block orders from a left-positive chamber and the right block orders from a right-positive chamber. Their splice is a chamber with both indicators one, contradiction.

There is therefore a common block \(B\). There can be only one, since \(U,V\) are disjoint intervals and blocks are consecutive. Let \(\alpha=|B\cap U|\) and \(\beta=|B\cap V|\). Fix exterior block orders from a left-positive chamber on the left and a right-positive chamber on the right. These exterior choices concern disjoint blocks and are simultaneously realizable. In this fixed context the two indicators depend on ordered \(\alpha\)- and \(\beta\)-tuples from \(B\), each attains one, and their sum is one on every compatible pair. All compatible pairs extend to a chamber by ordering the unused block vertices in the remaining positions.

The ordered-tuple lemma in [[verified_five_position_obstruction_and_ordered_tuple_compression]] gives
\[
|B|\le\alpha+\beta.
\]
Disjoint occupation gives the reverse inequality. Thus every position of \(B\) belongs to \(U\cup V\). But a consecutive block meeting both intervals contains every position between them. There can therefore be no position between \(U\) and \(V\). \(\square\)

**Corollary.** In a disjoint single-sided terminal carrier satisfying these exclusive-indicator hypotheses, the full determining span has at most ten vertices for span-two witnesses, and at most twelve for alternating witnesses. The span-two case is therefore directly covered by the ten-vertex two-cover theorem; its elimination is unnecessary for the finite-support statement.

For the span-two indicator, \(001\) and \(011\) may be grouped together as the predicate “first bit zero, last bit one.” This does not affect the proposition, which makes no fixed-word assumption.

This replaces the failed one-polarity elimination by a weaker true conclusion. The example in [[positive_protection_allows_a_disjoint_single_sided_span_two_carrier]] attains the adjacent-window span-ten bound.

The corollary does not yet prove outwardness: containment of all at-most-current-depth determining windows in the full central span must be checked for the chosen depth rule, and surgery must preserve that same rule. Nor does it handle carriers in which both indicators occur in the same chamber. Such reflected-double carriers are not exclusive and the tuple argument does not apply.

For the alternating branch the bound is twelve, not ten. Reducing twelve to ten requires a further one-polarity argument or handling the adjacent twelve-position model directly. No twelve-vertex two-cover theorem is asserted here.

The useful repair direction is consequently: work with one positive-word depth; use adjacency compression for exclusive disjoint carriers; analyze reflected-double carriers separately; and then construct nested protected carriers. The six-word band cannot be imported into this route merely because complementing the tournament preserves global path-cover number.
