# Canonical entrance paths in the p=5 4445 pattern must cross the far end of the five-path

## Statement

In the p=5 charged pattern (4,4,4,5), retain the notation of 7d676959b033. Let R_b be any canonical three-edge entrance path for the ascending rank-four edge
  f_b={b,v,u_b},
so R_b ends at b and avoids both terminals v,u_b.

Then R_b must meet V(e5∪g4). Equivalently, no canonical b-ending entrance path for f_b is disjoint from both the rank-five terminal edge e5 and its predecessor g4.

## Body

Suppose for contradiction that R_b is disjoint from both e5 and g4.

Because R_b is the canonical entrance precursor for f_b, the concatenation
  R_b,f_b
is a four-edge linear path ending in f_b through its unique entrance b, and R_b avoids the two terminals v,u_b. Thus f_b meets R_b only at b.

The edge e5 meets f_b at v. Since R_b avoids v and, by supposition, is disjoint from e5, appending e5 preserves linearity.

The edge g4 meets e5 at the original path joint d=g4∩e5. It is disjoint from f_b: indeed f_b={b,v,u_b}, where b lies in g3 but not g4, v lies only in e5 on P, and u_b lies in g1∪g2 by 7d676959b033, while g4 is disjoint from g1∪g2. By supposition g4 is also disjoint from R_b.

Hence
  R_b,f_b,e5,g4
is a six-edge linear path.

Its last edge is g4, whose predecessor e5 meets it at d. The other path joint of g4 toward g3 is c=g3∩g4, and c!=d, so c can be chosen as a last vertex of this six-edge path. Therefore
  phi(c)>=6.

But 9a7eac176b49 gives phi(c)=3. Contradiction.

Thus every canonical entrance path R_b must meet e5 or g4.
