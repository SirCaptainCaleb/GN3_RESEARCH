# Exactly two top terminal edges at a Type-A vertex force a universal two-entrance gate

## Statement

Let v be Type A with p=phi(v)>=5 and put q=p-1. Let T_q(v) be the set of nonspecial terminal edges through v having rank exactly q.

Then |T_q(v)|>=2.

If |T_q(v)|=2, write
  T_q(v)={h1,h2}
and let x1,x2 be their unique entrances. Then there is a unique hyperedge g containing {x1,x2}, and g has the following universal-gate property:

For i=1,2, every longest q-edge path ending in h_i with last vertex v has g as its penultimate edge. On such a path the penultimate edge g meets h_i at x_i, while the other entrance x_{3-i} is the private vertex of g relative to that path.

## Body

The cumulative nonspecial-terminal bound 0e550ff0eadd with threshold q-1=p-2 gives at most
  2(p-2)-3=2p-7
terminal nonspecial edges of rank at most p-2.
A Type-A vertex has exactly 2p-5 nonspecial terminal edges. Hence at least two have rank p-1=q, proving |T_q(v)|>=2.

Assume now that exactly two exist, h1,h2.

Fix i and choose any longest q-edge path
  P=(g1,...,g_{q-1},h_i)
ending in h_i with last vertex v. Apply the saturated-fan propagation theorem a1a7159e2c43 to this path. It produces a second rank-q nonspecial terminal edge f through v, distinct from h_i, whose unique entrance is the private vertex beta of the penultimate edge g_{q-1}.

Since T_q(v) has only two members, f=h_{3-i}. Therefore beta=x_{3-i}.

The same penultimate edge g_{q-1} also contains x_i, because it enters h_i through its unique entrance x_i. Hence
  {x1,x2}⊂g_{q-1}.

Linearity gives at most one hyperedge containing the pair {x1,x2}; call it g. Thus the penultimate edge is forced to be this same g for every choice of longest h_i-witness ending with last vertex v.

The argument is symmetric for i=1,2. In an h_i-witness, g meets h_i at x_i, while x_{3-i} is the private vertex of g: the third vertex of g is the preceding path joint, and h_i cannot contain x_{3-i} because h1,h2 already share v and linearity forbids a second common vertex.
