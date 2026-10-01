# Crossed p=5 rank-five competitors force a reciprocal rank-four tail blocker

## Statement

In the p=5 pattern 4555, use the setup of 5ef77fe98dff. Let
  f={x,v,u}
be the unique rank-four charged edge, with unique entrance x and phi(x)=3.

Let
  h={y,v,z}
be any crossed rank-five charged competitor, where y is the unique entrance of h and z its opposite terminal. Let
  Q=(q1,q2,q3,q4)
be any canonical four-edge entrance path with last vertex y and avoiding the two terminals v,z, so Q,h is a rank-five path ending in h through y.

Then
  V(q3∪q4)∩{x,u} != empty.
In particular every canonical entrance rail for h has a terminal-tail contact with the rank-four edge f in one of its last two precursor edges.

## Body

The path Q,h is a five-edge path ending in the rank-five nonspecial edge h. Since h is entered through its unique entrance y, either of its two terminal vertices can be chosen as the last vertex; choose v.

The rank-four nonspecial edge f shares v with h, and v is a terminal of f. Apply the certified terminal tail-blocker lemma c0798e59ef02 to:
- e=f, of rank q=4;
- the snake-incoming last edge h at v, of rank 5>=q-1;
- the longest rank-five path Q,h ending in h at last vertex v.

The lemma says that f must meet one of the q-2=2 precursor edges immediately preceding h, namely q3 or q4.

Now Q avoids v by construction. Since
  f={x,v,u},
any f-contact on Q must be x or u. Therefore
  V(q3∪q4)∩{x,u} != empty.

This also subsumes the cruder splice observation: if Q avoided f entirely, then Q,h,f would be a six-edge path ending with last vertex x, contradicting phi(x)=3.
