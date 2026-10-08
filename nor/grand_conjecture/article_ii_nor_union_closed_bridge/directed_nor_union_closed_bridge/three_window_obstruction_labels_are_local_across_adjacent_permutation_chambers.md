# Three-window obstruction labels are local across adjacent permutation chambers

## Composition

(none yet)

## Development


Fix coordinate arity r and a permutation pi. Let epsilon_i be the sign of the ordered r-window beginning at position i.

Suppose i<j<k and epsilon_i=epsilon_k differs from epsilon_j. This is a three-window witness that the word has at least two changes.

Now swap adjacent coordinates in positions s and s+1. A window can change only if its position interval meets one of those two coordinates. Therefore only window starts in

[s-r+1,s+1]

can change, with endpoint truncation.

Hence any three-window witness whose three start indices lie outside that interval survives unchanged in the adjacent permutation chamber.

So three-window badness labels are locally stable across the Coxeter chamber graph: a chosen witness can disappear only at a wall lying within r positions of one of its supporting windows.

Under order reversal the witness positions are reflected and all three signs are complemented.

This gives a concrete carrier structure for a Connector argument. A witness region propagates freely across all distant adjacent-transposition walls, and its boundary is supported only near the three ranks that carry the witness. The remaining goal is to show that a carrier joining a witness to its reversed partner must pass through a chamber with no witness, which would be a one-change NOR order.
