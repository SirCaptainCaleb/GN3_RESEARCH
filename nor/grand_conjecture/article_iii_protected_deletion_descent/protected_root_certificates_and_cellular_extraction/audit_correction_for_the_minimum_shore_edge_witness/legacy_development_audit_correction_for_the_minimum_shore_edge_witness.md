# Audit correction for the minimum-shore edge witness — preserved pre-item development

Section 345 needs a scope correction.

Let u -> v be an oriented edge inside the minimum signature shore A, so t(u,v)=1. Minimality supplies some w in A minus {u,v} with alpha(u,v,w)=1.

Since
alpha(u,v,w)=t(u,v) xor t(v,w) xor t(w,u),
this becomes
t(v,w)=t(w,u).

There are two cases.

If both bits are 1, then
u -> v -> w -> u
is a directed triangle.

If both bits are 0, then
u -> w -> v
and u -> v, so the triple is transitive.

Thus the witness w need not complete u -> v to a directed triangle. The edgewise triangle-coverage claim from §345 does not follow, and neither does strong connectivity of T[A] from that argument.

The later seed remains valid for a different reason. Section 337 gives every vertex of A an in-neighbor and an out-neighbor inside A. Therefore A contains a directed cycle, and a shortest directed cycle in a tournament has length three. Hence A contains at least one directed triangle, which is sufficient for §342 and the five-coordinate connector seed.

Use only:
- existence of a directed triangle in A;
- no edgewise triangle-coverage claim;
- no strong-connectivity claim from §345.
