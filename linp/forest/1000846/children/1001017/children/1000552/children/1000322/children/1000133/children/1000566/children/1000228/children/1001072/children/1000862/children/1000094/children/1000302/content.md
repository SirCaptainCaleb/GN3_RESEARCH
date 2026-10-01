# Slack controls forest joints in the extremal critical core

## Statement

In the extremal |D|=k color-complete critical-core normal form, let
sigma=2k-(m+2c)>=0,
where m=|E(H-D)| and c is the number of nonempty forest components. For each color d∈D let J_d be the number of forest-joint endpoints among the d-colored DXX edges, and let T_d be the number of edges through d that are not DXX. Then
J_d+2T_d=sigma
for every d. Consequently, if j=m-c is the total number of forest joints, then
j(k-2)<=k sigma,
so
j<=k sigma/(k-2).
Thus for fixed small sigma and large k, all but O(sigma) components of H-D are single hyperedges.

## Body

Fix d∈D. Every forest-private vertex has exactly one incident edge of color d by c15cf7354428.

Among the k edges through d, classify:
- a_d DXX edges joining two forest-private vertices;
- b_d DXX edges joining one private vertex and one forest joint;
- c_d DXX edges joining two forest joints;
- T_d edges that are not DXX.

Because the d-colored DXX edges form a matching and saturate every forest-private vertex exactly once,
2a_d+b_d = r,
where
r=m+2c=2k-sigma
is the number of forest-private vertices.

The total degree of d is k:
a_d+b_d+c_d+T_d=k.

Multiply by two and subtract the private-saturation equation:
2k-r
 = (2a_d+2b_d+2c_d+2T_d)-(2a_d+b_d)
 = b_d+2c_d+2T_d.

By definition the number of forest-joint endpoints used by d-colored DXX edges is
J_d=b_d+2c_d.
Therefore
J_d+2T_d=sigma.

In particular J_d<=sigma for each d, so summing over the k colors gives at most
k sigma
DXX incidences at forest joints.

On the other hand, 6aa954fe903a gives d_G(x)>=k-2 for every forest joint x, where G is the DXX color graph. Thus the total joint incidence count is at least
j(k-2).

Hence
j(k-2)<=k sigma,
which gives
j<=k sigma/(k-2).

Since a path forest with c components and m edges has exactly j=m-c joints, small slack forces only O(sigma) total excess edge-length beyond one edge per component. Equivalently, near saturation is a matching of single triples with only O(sigma) local longer-component defects.
