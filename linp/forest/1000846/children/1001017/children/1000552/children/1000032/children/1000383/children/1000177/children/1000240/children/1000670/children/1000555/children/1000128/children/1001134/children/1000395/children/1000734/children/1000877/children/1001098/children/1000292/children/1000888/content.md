# Earlier first contact of two common-hub double chords is bounded by the later chord rank

## Statement

Let P=(g_1,...,g_L) be a linear path avoiding a vertex v. Let f and h be distinct nonspecial edges through v, each having exactly two vertices on P, and assume v is terminal at h (equivalently, v is not the unique entrance of h). Let i_f and i_h be the first path-edge indices meeting f and h, respectively. If i_f<i_h and r=phi(h), then i_f<=r-3.

In particular, for any family of pairwise distinct nonspecial edges through an external hub v that each double-contact P and at which v is terminal, ordering the edges by strictly increasing first-contact indices forces every earlier first-contact index to be at most the rank of every later edge minus three.

## Body

Let w be the f-contact on g_{i_f} witnessing the first occurrence. Because f has exactly two P-contacts and H is linear, its second P-contact cannot lie on g_{i_f}: otherwise f and g_{i_f} would share two vertices and hence be the same edge, impossible since v is not on P. Thus the prefix g_1,...,g_{i_f}, viewed with last vertex w, meets f only at w. Since i_f<i_h, the same prefix is disjoint from h. Also f and h meet exactly in v by linearity. Therefore g_1,...,g_{i_f},f,h is a linear path of length i_f+2 ending in h, and it enters h through v.

By hypothesis v is terminal at the nonspecial edge h, so v is not its unique entrance. Hence the displayed path is a wrong-entrance h-path. By definition of r=phi(h), its length cannot exceed r; equality is also impossible because every longest h-path must use the unique entrance of h. Hence i_f+2<=r-1, i.e. i_f<=r-3.
