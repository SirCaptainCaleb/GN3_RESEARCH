# Clean contacts two positions apart cannot coexist on a canonical low-rank entrance rail

## Statement

Let e={x,v,u} be ascending nonspecial of rank q with unique entrance x, and let R=(r_1,...,r_{q-1}) be a canonical entrance path ending at x and avoiding v,u. If two distinct edges through terminal v each meet R in exactly one private contact, on path edges r_a and r_b respectively, then |a-b|≠2. Indeed contacts two positions apart splice through the two common-v edges to form a q-edge path ending at x, contradicting phi(x)=q-1. Adjacent positions are not covered because of the inherited r_a-r_{a+1} intersection.

## Body


Let e={x,v,u} be an ascending nonspecial edge of rank q, with unique entrance x and terminal v. Let
  R=(r_1,...,r_{q-1})
be a canonical entrance path ending physically at x such that R,e is a longest q-edge path ending in e through x; in particular R avoids the two terminals v,u.

Let h_1,h_2 be distinct edges through v, neither equal to e, such that each h_i meets R in exactly one path edge and exactly one vertex. Because a vertex lying at a joint of two consecutive R-edges would make h_i meet two path edges, each such unique contact is private in its path edge.

Suppose h_1 meets R only in a private vertex of r_a and h_2 meets R only in a private vertex of r_b, with b=a+2.

Consider
  r_1,...,r_a,h_1,h_2,r_b,r_{b+1},...,r_{q-1}.       (*)

This is a linear path:
- the prefix r_1,...,r_a and suffix r_b,...,r_{q-1} are separated in R by the omitted edge r_{a+1}, hence every prefix edge is disjoint from every suffix edge;
- h_1 meets the prefix only in its private r_a contact and is disjoint from the suffix by the single-contact hypothesis;
- h_2 meets the suffix only in its private r_b contact and is disjoint from the prefix;
- h_1 and h_2 are distinct edges through v, so by linearity their intersection is exactly {v}; v is absent from R because R avoids the terminals of e.

Thus (*) is a linear path. Its length is
  a + 2 + ((q-1)-b+1)
  = a+2+q-b
  = q
because b=a+2.

The final edge is r_{q-1}, whose physical last vertex is x, and x is absent from h_1,h_2 (otherwise either h_i and e would share both v and x, violating linearity). Hence (*) is a q-edge path ending at x, contradicting
  phi(x)=q-1.

Therefore two clean single contacts through v on a canonical rank-q entrance rail cannot occupy private path-edge positions differing by two.

Remark. The same displayed splice does not cover b=a+1 because r_a and r_{a+1} have their inherited path joint and would become nonconsecutive in (*). This is exactly the adjacent-contact residue; no claim is made there.
