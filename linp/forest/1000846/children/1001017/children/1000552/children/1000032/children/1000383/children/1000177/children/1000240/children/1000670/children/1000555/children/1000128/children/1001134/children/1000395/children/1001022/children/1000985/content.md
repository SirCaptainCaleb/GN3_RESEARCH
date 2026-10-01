# Overlap-maximal maximum paths contain no clean four-point crossing braid cell

## Statement

Let R be a maximum endpoint path ending at y, and among all maximum endpoint paths ending at x let Q maximize |V(Q) intersect V(R)|. Suppose four common vertices a,b,c,d lie internally on both paths, in the order
  a,b,c,d along Q
and
  a,c,b,d along R.
Assume the six open path segments determined by these four vertices are clean: between a and d, the Q- and R-segment interiors meet the other path only at the displayed common vertices. Then this configuration is impossible.

## Body

Write
  A=|Q[a,b]|, B=|Q[b,c]|, C=|Q[c,d]|,
and
  U=|R[a,c]|, V=|R[c,b]|, W=|R[b,d]|.
The cleanliness hypothesis lets us perform two complementary switches.

First form a path Q' by following Q to a, then R from a to c, then Q backwards from c to b, then R from b to d, and finally Q from d to its last vertex x. All nonconsecutive pieces are vertex-disjoint by cleanliness, and consecutive pieces meet exactly at a,c,b,d. Hence Q' is a linear path ending at x. Its length is
  |Q'|=|Q|+(U+W)-(A+C).
Since Q is maximum at x,
  U+W <= A+C.                                             (1)

Symmetrically form R' by following R to a, then Q from a to b, then R backwards from b to c, then Q from c to d, and finally R from d to its last vertex y. This is a linear path ending at y, with
  |R'|=|R|+(A+C)-(U+W).
Maximality of R gives
  A+C <= U+W.                                             (2)

Thus equality holds in (1) and (2). In particular Q' has the same length as Q and is another maximum endpoint path ending at x.

Now compare its overlap with R. The portions of Q removed in the switch are the open interiors of Q[a,b] and Q[c,d]; by cleanliness neither contains an R-vertex. The inserted R-segments R[a,c] and R[b,d] have interiors disjoint from Q except at the displayed common vertices. Each is a nontrivial path segment between distinct common vertices, so at least one vertex of its interior is new to Q; indeed if a segment consists of one hyperedge, its third vertex is not on Q by cleanliness and linearity. Therefore
  |V(Q') intersect V(R)| > |V(Q) intersect V(R)|,
contradicting the overlap-maximal choice of Q.

Hence no such clean four-point crossing braid cell exists.