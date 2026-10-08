# Order-nine endpoint exclusion for reflected alternating terminal supports — preserved pre-item development

## Order-nine reflected alternating supports also exclude endpoint sign flips

Consider a reflected alternating terminal witness whose two four-status occurrences start three status positions apart. This is exactly the case in which the union of the two six-vertex determining windows has order nine.

Let the left occurrence be one of
[
0101,qquad 1010.
]
At start distance three, consistency of the one overlapping status forces the right occurrence to have the opposite alternating polarity. Hence any chamber containing both reflected occurrences has, on the seven-status union, one of the two words
[
0101010,qquad 1010101.
]
But then an alternating forbidden word occurs at each intermediate start. In particular there is a (0101) or (1010) occurrence strictly between the two reflected starts, hence represented by a witness-path edge strictly closer to the center. This contradicts protection at the selected edge.

Therefore:

**Order-nine coexistence exclusion.** A protected chamber cannot contain both reflected alternating occurrences when their determining support has order nine.

Now let (E={pi,pi s_k}) be a protected terminal sign-flip edge for such an order-nine reflected alternating edge. If (s_k) is disjoint from one of the two six-vertex determining windows, the truth value of that far occurrence is unchanged across (E). One endpoint of (E) is labeled by that far orientation, so the far occurrence is present at both endpoints. The opposite-labeled endpoint must also contain the near occurrence. Hence that endpoint contains both reflected occurrences, contradicting the coexistence exclusion.

Thus:

**Order-nine endpoint exclusion.** Every terminal sign-flip generator for a reflected alternating support of order nine must meet both six-vertex determining windows. In particular no generator supported near either outer endpoint of the nine-position determining interval can be a terminal sign-flip edge.

This strengthens [[maximal_ten_support_endpoint_braids_are_impossible]]: the same persistence mechanism excludes endpoint terminal sign flips for both the order-ten (start separation four) and order-nine (start separation three) reflected-alternating cases.

For the protected-filtration repair, this removes the only near-maximal endpoint sign-flip sites that motivated switching between the two ten-position normalizations of an order-nine determining interval. Any actual terminal sign-flip edge lies in the overlap of the reflected determining windows and is internal to either normalization window. The remaining global issue is therefore not support exchange at an endpoint sign-flip edge, but proving a compatible protected carrier for larger mixed faces while collapsing sign-neutral directions.
