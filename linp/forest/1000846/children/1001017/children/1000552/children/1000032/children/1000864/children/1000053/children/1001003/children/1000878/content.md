# Separated terminal-only contact intervals are squeezed from both ends

## Statement

In the setting of df8ad4c65be0, let I_e and I_f be the sets of path-edge indices containing the sole terminal contacts u and z, respectively. Thus each I is either {j} or {j,j+1}. Assume
  max I_e < min I_f.
Write
  a=min I_e,  b=max I_f,
and q_e=phi(e), q_f=phi(f).
Then
  a <= q_f-3
and
  b >= p-q_e+3.

## Body

The first inequality is exactly the prefix splice from df8ad4c65be0, because a is the first occurrence index of u and the f-contact lies strictly later.

For the second inequality, consider the reversed suffix
  (g_{p-1},g_{p-2},...,g_b,f,e).
Because b is the last path-edge containing z, f meets this retained suffix only at z in g_b. Because max I_e<min I_f<=b, the sole P-contact u of e lies strictly before g_b and is absent from the retained suffix. The final path edge h=g_p is omitted, so the common terminal v is absent from the suffix. The entrances x,y are absent from P by hypothesis. Hence the displayed sequence is a linear path: consecutive intersections are inherited along the reversed suffix, then z between g_b and f, and v between f and e; all nonconsecutive pairs are disjoint by the single-contact assumptions and linearity.

Its length is
  (p-b)+2.
Its last edge e is entered through terminal v, while the unique entrance x is a physical last vertex. Therefore, as in the prefix argument, its length is at most q_e-1. Thus
  p-b+2 <= q_e-1,
so
  b >= p-q_e+3.