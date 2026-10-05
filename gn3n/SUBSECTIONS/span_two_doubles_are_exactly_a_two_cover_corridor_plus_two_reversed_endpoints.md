# Span-two doubles are exactly a two-cover corridor plus two reversed endpoints

## Metadata

- ID: span_two_doubles_are_exactly_a_two_cover_corridor_plus_two_reversed_endpoints
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 47
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## The unbounded span-two double is exactly a two-cover corridor plus two reversed endpoints

The corridor reduction can be sharpened to an exact two-vertex statement.

Let the two reflected positive span-two occurrences start at status positions
[
a<b.
]
Up to reversal, take the left word to be (011) and the right word to be (001). Their determining vertex windows are
[
[a,a+4],qquad [b,b+4].
]

Protection from every strictly more central positive witness implies that the status interval
[
[a+1,b+1]
]
contains none of
[
001,qquad011,qquad0101.
]
Indeed every positive occurrence wholly in that interval has a start strictly between the reflected starts and hence represents a more central witness edge.

Let
[
C=(v_{a+1},v_{a+2},ldots,v_{b+3}).
]
Its internal status word is exactly the protected interval ([a+1,b+1]), so by the exact inversion-window theorem the induced order (C) admits a two-cover by one cut:
[
C=Pmid Q.
]
Moreover the left occurrence (011) gives
[
(v_{a+2},v_{a+1},v_a)
]
tight, while the right occurrence (001) gives
[
(v_{b+2},v_{b+3},v_{b+4})
]
tight.

Thus the full reflected determining span
[
(v_a,ldots,v_{b+4})
]
differs from the already two-covered corridor (C) by exactly the two endpoint vertices
[
x=v_a,qquad y=v_{b+4}.
]

Because the protected word begins with the two (1)'s supplied by the left (011) and ends with the two (0)'s supplied by the right (001), the canonical cut may be chosen so that both components have order at least two. Writing
[
P=(p_1,p_2,ldots),qquad
Q=(q_1,q_2,ldots)
]
with (Q) in its tight orientation, the two endpoint relations are precisely
[
(p_2,p_1,x)	ext{ tight},qquad
(q_2,q_1,y)	ext{ tight}.
]

So the only genuinely unbounded positive terminal geometry is equivalent to the following interface problem:

> two disjoint tight paths (P,Q), together with two exterior vertices (x,y) that reverse the initial edge of (P) and (Q), respectively.

The lengths of (P,Q) are irrelevant except insofar as a bounded prefix must be preserved for reattachment of their tails.

This formulation is stronger than the earlier “two bounded endpoint neighborhoods plus a corridor” statement: the arbitrary long middle has disappeared entirely from the combinatorial data. A repair may work with bounded prefixes of (P,Q) and the two vertices (x,y), provided it returns two path fragments with the correct ordered terminal pairs for the untouched tails.

A bare six-vertex theorem using only
[
(p_2,p_1,x),qquad(q_2,q_1,y)
]
is not expected: those two relations leave too much boundary-tournament freedom. The next useful finite target should retain at least the first tight triple of each corridor path,
[
(p_1,p_2,p_3),qquad(q_1,q_2,q_3),
]
and seek a repartition of the resulting eight-vertex interface that either absorbs (x,y) or exposes compatible ordered pairs for the two untouched tails.

This is now a bounded interface theorem, independent of the length of the reflected-double span.
