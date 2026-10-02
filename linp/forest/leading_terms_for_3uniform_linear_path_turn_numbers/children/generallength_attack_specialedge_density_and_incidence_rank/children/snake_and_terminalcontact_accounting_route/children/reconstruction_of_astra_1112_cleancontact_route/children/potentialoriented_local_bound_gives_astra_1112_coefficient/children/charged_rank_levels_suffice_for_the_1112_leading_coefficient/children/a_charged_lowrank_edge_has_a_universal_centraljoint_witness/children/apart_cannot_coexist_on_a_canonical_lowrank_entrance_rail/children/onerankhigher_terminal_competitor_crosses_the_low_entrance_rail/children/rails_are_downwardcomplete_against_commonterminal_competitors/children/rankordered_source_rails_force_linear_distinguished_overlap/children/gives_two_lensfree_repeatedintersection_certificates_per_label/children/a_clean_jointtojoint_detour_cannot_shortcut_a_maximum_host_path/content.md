# A clean joint-to-joint detour cannot shortcut a maximum host path

## Statement

Let A=(g_1,...,g_L) be a maximum endpoint path ending at a. Let z and u be distinct internal joints of A, with
  z=g_s intersect g_{s+1},
  u=g_t intersect g_{t+1}.
Let B be a linear path from z to u such that
  V(B) intersect V(A)={z,u}.
Then
  |E(B)|<=|s-t|.
Thus a clean detour between two host joints cannot use fewer edges than the corresponding interval of a maximum host path.

## Body

Assume first that s<t. Replace the host interval g_{s+1},...,g_t by B, oriented from z to u. Because z and u are joints of A and V(B) intersects V(A) exactly in {z,u}, the resulting edge sequence
  g_1,...,g_s, B, g_{t+1},...,g_L
is a linear path ending at the same last vertex a as A. Its length is
  L-(t-s)+|E(B)|.
Since A is a maximum endpoint path ending at a, this length is at most L. Hence
  |E(B)|<=t-s.

If t<s, keep the prefix g_1,...,g_t, traverse B in reverse from u to z, and keep the suffix g_{s+1},...,g_L. The same clean-intersection argument gives a linear path ending at a of length
  L-(s-t)+|E(B)|,
so
  |E(B)|<=s-t.

Therefore |E(B)|<=|s-t| in all cases.