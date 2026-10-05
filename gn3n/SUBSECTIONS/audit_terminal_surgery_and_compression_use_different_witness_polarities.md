# Audit: terminal surgery and compression use different witness polarities

## Metadata

- ID: audit_terminal_surgery_and_compression_use_different_witness_polarities
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 34
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## The witness polarity must be fixed before terminal surgery

The proof currently uses two different avoidance predicates. Put
\[
\mathcal W_+=\{001,011,0101\},\qquad
\mathcal W_-=\{110,100,1010\}.
\]
An order satisfying the exact two-cover criterion avoids \(\mathcal W_+\). It need not avoid \(\mathcal W_-\). Complementing the tournament preserves its global path-cover number, but this does not make the two order-relative predicates equivalent on the same chamber.

**Lemma.** A binary word of length at least four avoiding \(\mathcal W_+\cup\mathcal W_-\) is monochromatic.

**Proof.** A nonconstant three-bit word avoiding \(001,011,110,100\) is \(010\) or \(101\). Such a triple has a neighboring fourth bit. Either the neighboring triple is nonalternating and forbidden, or the four-bit interval is \(0101\) or \(1010\), again forbidden. Thus no nonconstant triple can occur. Every adjacent pair lies in a triple, so the word is constant. \(\square\)

Consequently simultaneous six-word avoidance on an entire support of order at least six requires a Hamiltonian order, possibly reversed. A two-cover theorem does not supply that property.

The normalized \(5|5\) repair makes this distinction explicit. Its eight internal statuses have the form
\[
111ab000,\qquad a,b\in\{0,1\}.
\]
For every choice of \(a,b\), this word contains \(110\) or \(100\). Indeed it has both colors and the preceding lemma applies. These words nevertheless avoid all of \(\mathcal W_+\), as the exact cut criterion also shows.

For example \(11110000\) has \(110\) at start 3 and \(100\) at start 4. Both occurrences are internal to the repaired ten-position support. The assertion in [[terminal_support_surgery_gives_a_genuine_outward_escape]] that every internal forbidden witness disappears therefore proves outwardness only for the positive three-word labeling. It does not prove outwardness for a labeling selecting the nearest occurrence among all six words.

This is an obstruction to the inference from the two-cover property, not a counterexample to the grand conjecture or a proof that no specially chosen repair can work at a particular depth. Such a repair would have to show explicitly that every surviving negative-polarity occurrence is farther outward, or that a positive witness-free full spanning order has already been reached. No such comparison is supplied by the current surgery proof.

The alternatives must be kept precise.

1. If depth is selected using only \(\mathcal W_+\), surgery removes the appropriate internal obstructions, but selected-depth protection does not imply avoidance of negative-polarity inward words. The six-word monochromatic-band and disjoint-span-two arguments then require new one-polarity proofs.
2. If depth is selected using both polarities, those local avoidance arguments may be used only after specifying the actual selection rule. The surgery and safe-transport statements must then be reproved for that same rule; a \(5|5\) cover alone is insufficient.
3. If the polarities are separate auxiliary arguments, neither protection nor outwardness can be transferred between their carrier spaces without a proved comparison.

The addendum [[explicit_proofs_for_finite_terminal_compression]] is useful development, but its dual-polarity portions are conditional on genuine six-word protection. The protected rank-two and higher-carrier constructions are likewise conditional on an outwardness theorem for one consistently defined depth.

The repair obligation is earlier than higher-dimensional carrier gluing: specify a single witness-selection/depth rule, then prove both its protected-face compression and its terminal outward replacement. After that, prove nested equivariant protected carriers. The current Article VII closure is not established.
