# Defect-free run reversal localizes the joint obstruction — preserved pre-item development

## Defect-free run reversal localizes the joint obstruction

Use the ternary decomposition
[
h(a,b,c)=alpha(a,b,c)oplus 1_{{d({a,b,c})=b}},
]
where (alpha) is alternating and (d) is the optional defect vertex.

Let
[
O=(v_1,ldots,v_n)
]
be a defect-free Hamilton order, so no consecutive triple has its middle vertex marked. Hence the actual NOR word on (O) equals its (alpha)-word.

Suppose the (alpha)-word contains an internal run of color (	au) between runs of the opposite color (sigma). Let that run consist of statuses
[
alpha(v_L,v_{L+1},v_{L+2}),ldots,alpha(v_R,v_{R+1},v_{R+2}),
]
all equal to (	au), with adjacent outside statuses equal to (sigma).

Reverse the vertex interval
[
I=(v_L,ldots,v_{R+2}).
]

### Lemma 1: interior defect-freeness survives

Every consecutive triple wholly inside (I) becomes the reverse of an old consecutive triple:
[
(v_j,v_{j+1},v_{j+2})
longmapsto
(v_{j+2},v_{j+1},v_j).
]
The middle vertex is still (v_{j+1}). Therefore an old triple was defect-free if and only if its reversed copy is defect-free.

Thus every internal new triple remains defect-free.

### Lemma 2: the internal run is erased in orientation sign

Alternation gives
[
alpha(v_{j+2},v_{j+1},v_j)=1-alpha(v_j,v_{j+1},v_{j+2})=sigma.
]
Hence after reversal the whole old (	au)-run becomes (sigma).

Every triple wholly outside (I) is unchanged and remains defect-free of its old color.

Therefore all possible failure of the reversed order to be a defect-free monochromatic-(sigma) order is confined to the two reconnection zones: at most four new consecutive triples.

### Consequence for an extremal defect-free order

Choose a defect-free Hamilton order minimizing the number of changes in its (alpha)-word. If that minimum exceeds one, reverse any internal run.

The reversal destroys two old change boundaries in the interior. Hence extremality forces a local certificate at the reconnections:
- at least one new reconnection triple is defect-unsafe, or
- among the defect-safe reconnection triples, the actual/orientation colors recreate enough variation to prevent a strict decrease.

So a minimum-change defect-free order cannot fail for a diffuse reason. Every internal run carries a bounded endpoint protector consisting only of defect marks and four triangle orientations.

This is the correct block analogue of the failed one-vertex simultaneous-insertion induction. The insertion obstruction can be arbitrarily engineered along a long scan, but block reversal preserves every old middle vertex in the interior and reduces the joint obstruction to bounded reconnection data.

A closure route is now to slide one endpoint of the reversed run. If a protector cannot persist as the endpoint moves, the alpha-variation decreases. If it does persist, the successive endpoint protectors form a chain of marked triangles sharing two coordinates; such a chain is a candidate for a forced shifted two-circuit or centered-triangle obstruction already classified elsewhere in Article II.
