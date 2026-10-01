# Every high competitor in the q,(q+1)^3 pattern has a private-singleton, joint, or two-vertex contact with the low entrance rail

## Statement

Let e={x,v,u} be ascending nonspecial of rank q, with unique entrance x and terminal v, and let R=(r_1,...,r_{q-1}) be a canonical entrance path ending at x and avoiding v,u. Let h={y,v,z} be a distinct ascending nonspecial edge of rank q+1 through the same terminal v. Then h meets R and cannot contain x or u. Writing mu_R(h) for the number of rail edges met by h, exactly one of the following holds:
- mu_R(h)=1, and the unique contact is private in r_j for j in {2,...,q-3} union {q-1};
- h has exactly one vertex on R, that vertex is a joint r_i∩r_{i+1}, and hence mu_R(h)>=2;
- both non-v vertices y,z lie on R, and no rail edge contains both.
The final-edge private-singleton residue j=q-1 remains open.

## Body

First h must meet R. Otherwise
  (r_1,...,r_{q-1},e,h)
is a linear (q+1)-edge path: R,e is the canonical q-edge path ending in e through its entrance x; e and h meet exactly at v; and by assumption h is disjoint from R. The final edge h is entered from e through v. Since v is a terminal of the nonspecial edge h, this would be a longest rank-(q+1) path ending in h through a non-entrance vertex, contradicting uniqueness of h's longest entrance.

Because e and h are distinct and both contain v, linearity gives e∩h={v}. In particular h cannot contain x or u.

Let mu_R(h) be the number of rail edges r_i met by h.

If mu_R(h)=1, let r_j be the unique rail edge met and w the intersection vertex. Then w is private in r_j: a joint belongs to two consecutive rail edges and would give mu_R(h)>=2. The repaired singleton-position lemma c448268039f5 excludes j=1 and j=q-2; the final rail-edge case j=q-1 is not presently excluded. Therefore
  j in {2,...,q-3} union {q-1}.

Now suppose mu_R(h)>=2. Since h has only two vertices besides v, there are two possibilities. If h has only one vertex w on R, then w must belong to at least two rail edges. In a linear path this means w is a joint r_i∩r_{i+1}; this is the joint-contact branch. If h has two distinct vertices on R, then they are exactly its two non-v vertices y,z. No rail edge can contain both y and z, because then h and that rail edge would share two vertices, violating linearity.

These three cases are exhaustive. Thus a high competitor is either a private singleton contact, a joint contact (one rail vertex lying on two consecutive rail edges), or a two-vertex rail chord. The previous version omitted the joint-contact branch.
