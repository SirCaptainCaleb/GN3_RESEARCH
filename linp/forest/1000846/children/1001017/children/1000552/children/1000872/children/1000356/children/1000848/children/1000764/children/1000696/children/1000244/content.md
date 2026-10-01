# Two non-double rank-q edges at p=2q-3 have a two-pattern middle-edge normal form

## Statement

Let v have phi(v)=2q-3 and fix a maximum path
  P=(g_1,...,g_{2q-3})
ending physically at v.

Suppose two distinct potential-charged ascending nonspecial rank-q edges through v are both non-double on P. Put
  A=g_{q-2}∩g_{q-1},
  B=private(g_{q-1}),
  C=g_{q-1}∩g_q.

Then their two distinct single-contact witnesses are exactly one of
  {A,B} or {B,C}.

Moreover B is necessarily the unique entrance of its rank-q edge, so
  phi(B)=q-1.

## Body

By the rank-q central window at p=2q-3, every selected witness lies in {A,B,C}. Distinct edges have disjoint non-v witness pairs, hence distinct selected witnesses.

By a01ddfa76dc8 (equivalently 967e87e433cb), a terminal-only rank-q witness can occur only at A. Therefore any witness at B or C is a visible entrance.

The pair {A,C} is impossible. Indeed C would then be a clean joint entrance. Apply eac2e3da3eea with the other rank-q edge as the earlier single-contact edge: C is the joint
  g_{q-1}∩g_q,
so it forbids every single contact whose first-contact cell is q-2. But A=g_{q-2}∩g_{q-1} has first-contact cell q-2, contradiction.

Thus the only possible two-element witness subsets are {A,B} and {B,C}.

In either case B is occupied. Since terminal-only rank-q witnesses are confined to A, B must be the unique entrance of its edge. Ascendingness then gives
  phi(B)=q-1.
