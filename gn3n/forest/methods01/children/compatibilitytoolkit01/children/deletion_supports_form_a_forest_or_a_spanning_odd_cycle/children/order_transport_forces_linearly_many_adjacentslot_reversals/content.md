# Odd support-cycle order transport forces linearly many adjacent-slot reversals

## Statement

Assume the selected deletion-support graph is the spanning odd cycle from deletion_supports_form_a_forest_or_a_spanning_odd_cycle, with n=2k+1 support vertices S_i and deletion labels d_i, and assume that whenever two selected deletion covers are support-compatible they are fully compatible. Let P_i be the resulting canonical Hamilton order on S_i. For each i, the compatible-pair localization applied to the consecutive covers F_{d_i}=P_i|P_{i+1} and F_{d_{i+1}}=P_{i+1}|P_{i+2} shows that P_i and P_{i+2}, on their common support S_i∩S_{i+2}, differ by inserting d_{i+1} and d_i in identical or adjacent slots. Around the whole odd cycle, at least k-1=(n-3)/2 of these transitions are adjacent-slot transitions. In particular at least one adjacent-slot transition exists, and each such transition yields the local reversing triple supplied by the compatible-pair localization theorem.

## Body

Write the support cycle as S_0,S_1,...,S_{2k}, with edge S_iS_{i+1} labeled d_i (indices modulo 2k+1). Because the two deletion covers incident with S_i are support-compatible and, by hypothesis, not order-incompatible, they induce one canonical Hamilton order P_i on S_i.

The explicit support formula from deletion_supports_form_a_forest_or_a_spanning_odd_cycle gives
S_i∩S_{i+2}=S_i-{d_{i+1}}=S_{i+2}-{d_i}.
The consecutive deletion covers
F_{d_i}=P_i|P_{i+1}
and
F_{d_{i+1}}=P_{i+1}|P_{i+2}
are fully compatible. Applying the compatible-pair localization theorem to this pair shows that P_i and P_{i+2} arise from one common order on S_i∩S_{i+2} by inserting d_{i+1} and d_i, respectively, either in the same slot or in adjacent slots. In the adjacent-slot case the theorem supplies the associated reversing triple through the intervening common vertex.

To count adjacent-slot transitions, follow the k position strands under the step i→i+2. If every transition were same-slot, the replacement d_{i+1}→d_i would preserve all positions. More generally, each adjacent-slot transition performs one adjacent transposition of the position strands, while each same-slot transition performs none. After one complete circuit of the support cycle, the labels return to the starting support but the deterministic replacement rule induces a k-cycle on the strands. Therefore the product of the transpositions supplied by the adjacent-slot transitions must undo a k-cycle.

A k-cycle requires at least k-1 transpositions in any factorization. Hence the number t of adjacent-slot transitions satisfies
t≥k-1=(n-3)/2.
Also t≡k-1 mod 2 by parity. Thus at least one adjacent-slot transition exists, and in fact there are linearly many such local reversal events.

The argument uses only the spanning odd support-cycle structure of deletion_supports_form_a_forest_or_a_spanning_odd_cycle, canonical order agreement on support-compatible pairs, and the compatible-pair localization theorem. It does not by itself glue these reversals into a spanning two-cover.