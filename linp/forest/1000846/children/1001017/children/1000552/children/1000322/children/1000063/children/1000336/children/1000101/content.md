# Single blockers give endpoint-preserving rotations, safe below the boundary

## Statement

A single-blocking edge whose blocker w is not the fixed last vertex x gives a length-preserving rotation of a path that still ends at x. Consequently, if e={x,y,z} is ascending nonspecial of rank q and q<=delta-1, then every (q-1)-edge x-ending entrance path avoiding y,z admits a nontrivial single-blocker rotation to another (q-1)-edge x-ending path still avoiding y,z.

## Body

Let Q=(g_1,...,g_t) end at x and let f be single-blocking at the opposite endpoint, with unique blocker w≠x. If w lies only in g_2, use f,g_2,...,g_t. If w lies only in g_j with j>=3, reverse the prefix through g_{j-2}, then use f and the suffix g_j,...,g_t. If w is the joint of g_j,g_{j+1}, omit g_j, reverse through g_{j-1}, then use f and the suffix from g_{j+1}. In every case the inherited intersections plus the opposite endpoint and w are the only consecutive intersections, and linearity excludes nonconsecutive ones. The resulting path has the same length and still ends at x.

For the safe boundary corollary put t=q-1. The single-blocker surplus gives at least
  S>=2(delta-t)=2(delta-q+1)>=4
single blockers at the opposite endpoint. At most one can use x as blocker, at most one can contain y, and at most one can contain z. Hence some single blocker has blocker w≠x and avoids y,z. Applying the rotation above gives another (q-1)-edge x-ending path; since the old path and the new edge both avoid y,z, the rotated path does as well. Thus below q=delta the canonical entrance-path rotation graph has no sink.
