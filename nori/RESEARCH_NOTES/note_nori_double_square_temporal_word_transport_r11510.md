# Two-hit temporal-word transport and strictly internal critical square boundary

- Stable ID: note_nori_double_square_temporal_word_transport_r11510
- Author: unspecified; session provenance retained
- Primary home: subsection:gauge_critical_switches_and_clustered_witnesses_on_full_paths
- Labels: NORI1, unrestricted, square-switch, antipodal, root-order-exchange, double-hit, temporal-word, involution, balanced-criticality, critical-pivot, proved
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11510_3
- Updated session: session_nori_r11510_3
- Disposition: none
- Successor: none

## Related references

- None

## Research note

# Two-hit temporal-word transport under antipodal alternating-square switches

Let N>=3, and let c be an arbitrary legal antipodally odd undirected-edge coloring of Q_N. Let F be an alternating square on dimensions i,j and let Fbar be its globally antipodal square. Define c'=T_F(c) by complementing all eight edges of F and Fbar. A full rooted geodesic meets the switched set in h=0,1, or 2 edges. Its temporal word lists colors in traversal order.

**THEOREM.** There is an explicit involutive bijection between h=2 full rooted geodesics in c and in c', preserving the complete temporal word position by position.

**Proof.** If the two hits lie in the same square, they must be consecutive: an outside direction can never be crossed twice. Swap the two consecutive face directions i,j. Since the face alternates, the alternate two-step route has the complemented pair of colors before the switch and therefore the original ordered pair after the switch. All other path edges remain unchanged. Swapping back restores the original path.

If the hits lie in F and Fbar respectively, every outside direction must be traversed between the hits. Thus the hits are the first and last edges, in dimensions i and j. With root x and order (i,rho,j), the path is x --i--> u --rho--> v --j--> bar(x), where u=x+e_i and v=bar(x)+e_j. Take root x'=x+e_i+e_j and order (j,rho,i); the resulting path is x' --j--> u --rho--> v --i--> bar(x'). Its interior edges coincide, and each endpoint edge belongs to the alternate direction in the appropriate square; after the color switch these two endpoint colors match the originals position by position. The operation is involutive. Symmetric orders and opposite face orientation follow identically. The cases exhaust h=2. QED.

**COROLLARY 1 (word-sector conservation).** For every temporal binary word w of length N, the number of h=0 paths with word w is preserved by the switch, as is the number of h=2 paths with word w. All changes in the full temporal-word enumerator therefore lie in the h=1 sector.

**COROLLARY 2 (one strictly internal switch hit).** Suppose c has an all-red full geodesic and c' has none of either monochromatic color. Every red full geodesic of c meets the switched squares in precisely one edge, strictly internally. Indeed, zero-hit red paths remain red, and two-hit red paths map to red paths in c'. A one-hit red path in c becomes a one-blue path in c'; if that blue edge occurs at an endpoint, cyclic root rotation replaces it by its red antipodal mate, making the path entirely red. Contradiction.

**IMPLICATION FOR ARTICLE XVI.** The archived Article XV paired-flat square-boundary theorem already proves that failure of NORI1 yields a good and a bad perfectly vertex-balanced paired-flat legal coloring differing by one antipodal alternating-square switch. Combining that reduction with Corollary 2 gives the stronger necessary boundary: every red good-coloring witness uses just one switched edge in its interior, while the adjacent bad coloring carries the corresponding path with one internal blue edge. The formerly permitted red two-hit endpoint case is excluded through the joint exchange of root and endpoint directions.

**SCOPE.** A new dimension-uniform geodesic transport identity, stronger than the previously established one-Lipschitz defect bound. The remaining all-single-internal-hit configuration has not been contradicted; NORI1 remains open.

**VERIFICATION.** The self-contained proof is preserved as nori_double_square_endpoint_exchange.md and executable checker as nori_double_square_endpoint_exchange_verifier.py. All 64 legal Q3 colorings and sampled Q4/Q5 colorings yielded 440,576 matching two-hit temporal words, with inverse checks.
