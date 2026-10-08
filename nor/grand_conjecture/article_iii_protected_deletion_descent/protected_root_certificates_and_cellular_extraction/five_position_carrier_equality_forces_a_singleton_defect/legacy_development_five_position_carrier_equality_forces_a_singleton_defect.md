# Five-position carrier equality forces a singleton defect — preserved pre-item development

## Composition

(none yet)

## Development

## Five-position carrier equality forces a singleton defect

For a bad ternary order pi with change positions p_1<...<p_k, recall
C(pi)=sum_j (e_{v_{p_j}}-e_{v_{p_{j+1}+3}}).

Fix five consecutive positions I. Give all coordinates in I one common weight, and give positions outside I strictly increasing weights, using outside packets of size at most four.

Every summand of C(pi) has positional endpoint gap at least four, so its pairing with the weight functional is nonpositive. Equality is possible only when both endpoints lie in I.

If the total pairing is zero, every summand is internal to I. Since I has length five, each such summand must have endpoint gap exactly four. Therefore its two consecutive change positions differ by one, and its endpoints are the two extreme positions of I. There can be only one such consecutive-change pair. Hence pi has exactly two changes, they are consecutive, and C(pi) is the root from the first to the last coordinate of I.

Thus the global ternary word has one isolated one-window run and no other changes.

Consequently, if zero lies in the convex hull of consecutive-change labels from states obtained by permuting only the same five consecutive positions, every state appearing with positive coefficient is of this isolated-singleton type. Size five is therefore the first possible failure of packet-collapse separation, and that failure has a unique word-theoretic species.

For Article III this puts the first possible five-position carrier zero directly into the established singleton-barrier regime. The remaining issue is provenance: show that the flat-boundary repair or the fully-curved singleton resolution stays in the witnessed carrier or yields a strict admissible improvement.
