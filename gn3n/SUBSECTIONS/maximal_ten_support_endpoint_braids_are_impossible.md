# Maximal ten-support endpoint braids are impossible

## Metadata

- ID: maximal_ten_support_endpoint_braids_are_impossible
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 20
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False
- Provisional declared dependencies: ["rank_two_normalization_squares_close_and_only_the_inside_boundary_braid_remains", "local_witness_topology_and_the_finite_terminal_theorem", "minimal_separator_faces_and_terminal_edge_surgery_coherence", "audit_the_external_gauge_does_not_by_itself_close_rank_two_coherence"]

## Cold composition

(none yet)

## Development

## Maximal ten-support endpoint braids are impossible

The sole braid left by [[rank_two_normalization_squares_close_and_only_the_inside_boundary_braid_remains]] cannot actually occur as a terminal sign-flip residue.

A reflected alternating witness is represented by one of the two dual-polarity words
[
0101,qquad 1010.
]
Its determining window uses six consecutive vertex positions. The only way for a reflected alternating pair to have a ten-vertex determining span is for the two status-word starts to differ by exactly four. Thus, after translating indices, the two four-bit witness windows occupy positions (1,ldots,4) and (5,ldots,8) in the status word.

**Lemma (no chamber carries both maximally separated alternating orientations).**
A protected chamber cannot contain alternating witness occurrences at both of those starts.

**Proof.**
There are four possible concatenations of the two dual-polarity alternating patterns. Each creates a forbidden witness strictly between the two reflected starts:
[
egin{array}{c|c}
	ext{two displayed occurrences}&	ext{strictly closer occurrence}\ hline
0101,0101&1010	ext{ starting one step inward},\
1010,1010&0101	ext{ starting one step inward},\
0101,1010&011	ext{ starting two steps inward},\
1010,0101&100	ext{ starting two steps inward}.
end{array}
]
All four resulting words belong to the six-pattern dual-polarity witness language (001,011,0101,110,100,1010). Their start lies strictly closer to the status-word center than either endpoint of the maximally separated reflected pair. This contradicts protection from every witness edge preceding the selected edge. (square)

Now let (E={pi,pi s_k}) be a protected terminal sign-flip Coxeter edge whose selected unsigned witness edge is such a maximal ten-support reflected alternating edge. Suppose the adjacent transposition (s_k) is disjoint from the left six-vertex determining window. Then the left witness occurrence has the same truth value in (pi) and (pi s_k).

Because the two chamber labels on (E) are opposite orientations of the same unsigned witness edge, one endpoint is labeled by the left orientation and the other by the right orientation. A chamber labeled by the left orientation necessarily contains the left occurrence (possibly together with the right occurrence, with the tie broken by the external antipodal sign). Hence the left occurrence is present at both endpoints. The endpoint labeled by the right orientation also contains the right occurrence. It therefore contains both maximally separated alternating occurrences, contradicting the lemma. The same argument applies with left and right interchanged.

Consequently:

**Endpoint exclusion lemma.**
For a terminal sign-flip edge with ten-vertex reflected alternating support, its Coxeter generator must meet both six-vertex determining windows. In particular it cannot be supported near either endpoint of the ten-position span.

This removes exactly the last residue left by the rank-two normalization. In the unresolved (A_2) braid, after reversal if necessary, the ten-position span is (J=I), one generator swaps the last two positions of (I), and the adjacent generator swaps the last position of (I) with the first position outside (I). Both generators are disjoint from the far six-vertex determining window. By the endpoint exclusion lemma, neither generator can support a terminal sign-flip edge of the maximal ten-support type. Hence that purported residual braid contains no terminal surgery site at all, so its compatibility condition is vacuous.

Combining this with the previous rank-two normalization gives the terminal edge-surgery coherence lemma:

1. every commuting square is coherent by internal collapse and safe disjoint-swap transport;
2. every braid whose terminal determining span has order at most nine is coherent after shifting the ten-position normalization window toward the braid, making both generators internal (or by safe transport when both are outside/boundary);
3. the only braid not covered by that shift would have ten-vertex determining span, but the endpoint exclusion lemma shows that such an endpoint braid contains no terminal sign-flip edge.

Reversal gives the identical statement at the opposite endpoint. Therefore the bounded terminal surgery choices are coherent across every rank-two Coxeter residue. Together with the existing acyclic-carrier reduction, they extend equivariantly over the separator (S_r) into (Y_{r+1}).

This closes the finite square/hexagon compatibility frontier without same-face escape, minimum-counterexample arguments, or disturbance arguments.
