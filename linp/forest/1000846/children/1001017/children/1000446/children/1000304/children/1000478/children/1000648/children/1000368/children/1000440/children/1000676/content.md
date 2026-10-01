# In the p=5 pattern 4445, two middle-edge witnesses are forced entrances

## Statement

Let phi(v)=5 and suppose four potential-charged ascending nonspecial edges through v have ordered ranks (4,4,4,5). Fix a maximum five-edge path
  P=(g1,g2,g3,g4,e5)
ending in the rank-five charged edge e5 at v. Write
  a=g2∩g3,
  b=the private vertex of g3,
  c=g3∩g4.

Then among the three rank-four charged edges, the witnesses b and c are necessarily their unique entrances. In particular
  phi(b)=phi(c)=3.
Only the left joint a can possibly be realized as an opposite-terminal witness of a rank-four charged edge whose entrance is absent from P.

## Body

By 6244cba591da, the three rank-four path-relative witnesses are exactly the three vertices a,b,c of g3.

Consider one of the rank-four charged edges
  f={x,v,u},
with unique entrance x and opposite terminal u, and suppose its selected witness on P is u because x is absent from P.

The path-relative witness proof 220a14637b5f shows that if u lies privately in g_i, then
  g1,...,g_i,f
is a linear path, and likewise if u is the joint g_i∩g_{i+1}. In either case, if i=q-1=3 for q=4, the sequence
  g1,g2,g3,f
is a four-edge linear path ending in f and entering f through u.

But f is nonspecial with unique longest-path entrance x, and x!=u. This is impossible.

Therefore an opposite-terminal witness for a rank-four charged edge cannot occur in an index-3 slot.

In the three-vertex middle edge g3:
- the private vertex b is the private slot of index 3;
- the right joint c=g3∩g4 is the joint slot of index 3;
- only the left joint a=g2∩g3 has joint index 2.

Hence b and c cannot be terminal witnesses. Since all three witness slots are occupied by the three rank-four charged edges, b and c must be entrance witnesses.

For an ascending rank-four edge, the unique entrance x satisfies
  phi(x)=phi(edge)-1=3.
Thus
  phi(b)=phi(c)=3.

The left joint a remains the only slot that may be either an entrance witness or an opposite-terminal witness.
