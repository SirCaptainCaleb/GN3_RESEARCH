# At p=2q-3 a four-single rank-pair obstruction cannot occupy the right-joint slot

## Statement

Let phi(v)=2q-3 with q>=4 and let four assigned charged ascending edges of ranks in {q,q+1} all be single-contact on a fixed maximum v-path. In the seven-slot odd-central window A,...,G, the rightmost joint G=g_q∩g_{q+1} cannot be occupied. If G were occupied, the clean-joint hole rule and the F,G exclusion force the other contacts to A,B,C with C terminal-only; then g_1,...,g_{q-3},h_A,h_C,g_{q-1},g_q is a (q+1)-edge path ending at G, contradicting phi(G)=q.

## Body

Use the seven-slot notation of 47815dccb8b0:
  A=g_{q-3} cap g_{q-2},
  B=private(g_{q-2}),
  C=g_{q-2} cap g_{q-1},
  D=private(g_{q-1}),
  E=g_{q-1} cap g_q,
  F=private(g_q),
  G=g_q cap g_{q+1},
with p=2q-3 and q>=4.

Assume four assigned charged edges of ranks in {q,q+1} are all single-contact on P and suppose G is occupied.

Since terminal-only contacts cannot occupy G, its edge h_G has G as visible unique entrance and phi(G)=q.

By the clean-joint hole lemma eac2e3da3eea, a clean entrance at G forbids every other single contact whose first-contact cell is q-1. Hence D and E are unoccupied.

There remain only A,B,C,F for the other three contacts. If F were occupied, 47815dccb8b0 already gives a contradiction. Therefore F is also unoccupied, and the remaining contacts are exactly A,B,C.

Again by eac2e3da3eea, C cannot be a visible entrance, since a clean entrance at C would forbid first-contact cell q-3 and hence forbid A. Therefore C is terminal-only. Let h_A and h_C denote the distinct star edges through v whose sole P-contacts are A and C respectively. No assumption on whether A itself is entrance- or terminal-labeled is needed.

Consider
  g_1,...,g_{q-3}, h_A,h_C,g_{q-1},g_q.

This is linear:
- the prefix ends at A on g_{q-3}, and h_A has no other P-contact;
- h_A and h_C meet exactly at v;
- h_C meets g_{q-1} at C and has no other P-contact;
- the omitted edge g_{q-2} separates g_{q-3} from g_{q-1};
- all remaining nonconsecutive intersections are excluded by the single-contact assumption and linearity.

The path has
  (q-3)+2+2=q+1
edges.

Its final edge is g_q. Its predecessor g_{q-1} meets g_q at E, while
  G=g_q cap g_{q+1}
is distinct from E and g_{q+1} is omitted. Hence G is a last vertex. Therefore
  phi(G)>=q+1.

But G is the unique entrance of the rank-(q+1) edge h_G, so phi(G)=q, contradiction.

Thus G cannot be occupied in any four-single charged configuration at p=2q-3.
