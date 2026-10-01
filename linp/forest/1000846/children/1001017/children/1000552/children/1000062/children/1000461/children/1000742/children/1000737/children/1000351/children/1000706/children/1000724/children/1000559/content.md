# Two Type-A top-terminal entrances force a special universal gate two levels below

## Statement

Let v be Type A with p=phi(v)>=5, put q=p-1, and suppose exactly two rank-q nonspecial terminal edges h1,h2 occur through v. Let x1,x2 be their unique entrances, and let g be the universal two-entrance gate from a4df41ae3d99.

Assume x1 and x2 are both Type A.

Then:
1. phi(x1)=phi(x2)=q-1=p-2;
2. phi(g)=q-1;
3. g is special.

Hence g is one of the full-rank special edges in the common Type-A potential level p-2. In particular its third vertex also has potential q-1 whenever that third vertex is Type A.

## Body

Because h_i is nonspecial with unique entrance x_i and x_i is Type A, a57057ab0001 says every nonspecial edge sourced at x_i is ascending. Since phi(h_i)=q,
  phi(x_i)=q-1
for i=1,2.

By a4df41ae3d99, every longest q-edge path ending in h_1 at last vertex v has penultimate edge g containing x1,x2, with g∩h1={x1} and x2 private in g relative to that path. Removing h1 leaves a (q-1)-edge path ending in g with last vertex x2. Hence
  phi(g)>=q-1.

Suppose phi(g)>=q. Take a q-edge path ending in g. Its predecessor meets g in exactly one vertex. Since g contains the two distinct vertices x1,x2, at least one of x1,x2 is not the predecessor contact and therefore can be chosen as a last vertex of this q-edge path. This would give
  max{phi(x1),phi(x2)}>=q,
contradicting phi(x1)=phi(x2)=q-1.
Thus phi(g)<=q-1, and therefore
  phi(g)=q-1.

Finally suppose g were nonspecial. In the (q-1)-edge prefix obtained from an h1-witness, g is the last edge and x2 is a terminal. Thus g is a nonspecial terminal edge at the Type-A vertex x2, of rank
  phi(g)=q-1=phi(x2).
But a57057ab0001 says every nonspecial terminal edge at a Type-A vertex of potential r has rank at most r-1. Applied to x2 this would give
  phi(g)<=q-2,
a contradiction.

Hence g is special.

If its third vertex is also Type A, a57057ab0001 says every special edge incident with that vertex has rank equal to its vertex potential. Since phi(g)=q-1, that third vertex also has potential q-1.
