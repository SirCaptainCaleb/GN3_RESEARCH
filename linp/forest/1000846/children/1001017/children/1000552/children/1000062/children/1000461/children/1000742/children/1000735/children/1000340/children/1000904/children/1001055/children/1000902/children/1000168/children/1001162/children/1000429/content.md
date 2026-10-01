# A large gap-one switching family forces a linear packet of top-potential rotation endpoints

## Statement

Let P be a maximum p-path ending at v and F a family of distinct edges through v that are single blockers on P. Apart from O(1) boundary contacts, grouping precursor contacts into cells {private(g_i), g_i∩g_{i+1}} shows that each occupied cell yields a p-edge Posa rotation whose opposite endpoint can be the private vertex of g_{i+2}. Thus F forces at least |F|/2-O(1) distinct vertices of endpoint potential at least p. Applied to the gap-one switching family, local slack delta forces at least (5/16)q-O(1)-delta/2 high-potential rotation endpoints.

## Body

Let P=(g_1,...,g_p) be a maximum p-edge linear path ending at v. Let F be a family of distinct edges f through v such that each f has exactly one contact vertex with V(P)\g_p. By linearity these contact vertices are distinct.

For 1<=i<=p-2 define the two-slot cell
  C_i={b_i,z_i},
where b_i is the private vertex of g_i and z_i=g_i cap g_{i+1}. (At i=1 use the chosen private b_1; the second private vertex of g_1 can be handled as an O(1) boundary slot.)

Suppose a blocker contact c lies in C_i.

If c=b_i is private in g_i, the standard two-contact rotation gives
  g_1,...,g_i,f,g_p,g_{p-1},...,g_{i+2},
a p-edge linear path.

If c=z_i is the joint g_i cap g_{i+1}, the same displayed sequence is still linear: g_{i+1} is omitted, so the second old occurrence of c disappears; f meets the retained prefix only in g_i at c and the reversed suffix only in g_p at v. Thus again we obtain a p-edge path ending with g_{i+2} on the reversed side.

In either case the private vertex b_{i+2} of g_{i+2} is not in its predecessor in the rotated path, so it can be chosen as a last vertex. Hence
  phi(b_{i+2})>=p.                                  (1)

A given cell C_i contains at most two possible contact vertices, and distinct blockers use distinct contacts. Therefore if s_int members of F contact one of the interior cells C_1,...,C_{p-2}, the number of occupied cells is at least ceil(s_int/2). The corresponding private vertices b_{i+2} are distinct, so P contains at least ceil(s_int/2) distinct vertices of endpoint potential at least p.

The remaining possible unique-contact positions are O(1) boundary slots near the first and penultimate path edges. The penultimate private-contact case uses the endpoint version of the rotation and produces instead an outside endpoint of potential at least p. Absorbing boundary cases into an additive constant gives:
  number of distinct forced p-potential rotation endpoints
  >= |F|/2-O(1).                                    (2)

Apply this to the switching family from fecba48a3ffd. If the gap-one local slack is delta, then
  |F| >= gamma(q)-ceil((3q-4)/4)-delta
       =(5/8)q-O(1)-delta,
with p=q+1.
Hence one near-saturated gap-one state forces at least
  (5/16)q-O(1)-delta/2
distinct vertices that occur as endpoints of p-edge rotations and therefore have potential at least p.
