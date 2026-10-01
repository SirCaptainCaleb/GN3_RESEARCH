# Many backward collisions through one cut contain a large crossing or nested family

## Statement

Let v_0v_1...v_k be a rainbow terminal-pair path, and suppose M color-terminal collision chords x_i=v_j all cross one fixed cut between path edges E_t and E_{t+1}; thus j<t<i for every such chord.

Then these M chords contain a subfamily of size at least ceil(sqrt(M)) that is pairwise crossing, or a subfamily of size at least ceil(sqrt(M)) that is pairwise nested.

More explicitly, after ordering the chords by increasing left endpoint
j_1<...<j_M,
their right edge indices i_1,...,i_M are distinct. An increasing subsequence of the i_s gives pairwise crossing chords, while a decreasing subsequence gives pairwise nested chords.

## Body

Because the terminal path is rainbow, distinct parent edges have distinct unique entrances. Hence two collision chords cannot hit the same terminal vertex: if x_i=v_j and x_h=v_j, then x_i=x_h, contradicting rainbowness. Their right indices are distinct because they come from distinct path edges. Thus, after ordering the M chords by their distinct left indices j_1<...<j_M, the associated right indices i_1,...,i_M form a sequence of M distinct integers.

By the Erdős-Szekeres monotone subsequence theorem, this sequence has an increasing or decreasing subsequence of length at least ceil(sqrt(M)).

All left endpoints lie before the fixed cut and all right endpoints lie after it. Therefore for two selected chords with j_a<j_b, if i_a<i_b then
j_a<j_b<t<i_a<i_b,
so the endpoints interleave and the chords cross. If i_a>i_b, then
j_a<j_b<t<i_b<i_a,
so the second chord is nested inside the first. Hence a monotone subsequence gives the asserted pairwise crossing or pairwise nested family.
