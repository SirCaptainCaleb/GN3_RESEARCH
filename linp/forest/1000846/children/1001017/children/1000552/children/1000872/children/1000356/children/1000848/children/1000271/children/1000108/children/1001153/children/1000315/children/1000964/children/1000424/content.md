# The rising low-terminal odd-boundary branch is impossible

## Statement

In the surviving one-low p=2q-3 0-1-1 state, the low opposite terminal cannot have phi(C)=2q-2. On its chosen (2q-2)-edge C-path the three high edges are two-sided chords with sources in four central slots L,A,B,R around the low source x. Either joint source L or R directly splices with its opposite-half terminal to give a path of length at least q ending at x, contradicting phi(x)=q-1. Thus only private source slots A,B remain, insufficient for three distinct high sources.

## Body


Retain the rising low-terminal branch:
  R=(r_1,...,r_{2q-2})
is the chosen maximum path ending at C,
  x=r_{q-1} cap r_q
is the unique entrance of the low rank-q edge and satisfies phi(x)=q-1,
and the three rank-(q+1) high 0-1-1 edges are two-sided chords of R.

By 33522a8389e9/fc1f1c4984e9, their three distinct sources occupy three of
  L=r_{q-2} cap r_{q-1},
  A=private(r_{q-1}),
  B=private(r_q),
  R0=r_q cap r_{q+1},
and the opposite terminal of a left source lies in the right half while the opposite terminal of a right source lies in the left half.

We show L cannot be a source.
Suppose
  h={L,v,z}
is a high edge. Let k>=q be the first path-edge index in the right half containing z. Since z is a path vertex it occurs either only in r_k or also in r_{k+1}; by choosing its first occurrence, z does not occur in r_{k-1}.

Consider
  r_1,...,r_{q-2}, h, r_k,r_{k-1},...,r_q.          (*)

The prefix meets h at L. The reversed suffix meets h at z in its first edge r_k; the possible second z-edge r_{k+1} is omitted. The inherited prefix and suffix are separated by omitted central edges and hence have no nonconsecutive intersection. Also h cannot contain x, because h and the low edge already share v. Thus (*) is linear.

Its length is
  (q-2)+1+(k-q+1)=k>=q.
Its final edge is r_q. Since r_{q-1} is omitted, x is a last vertex. Hence
  phi(x)>=k>=q,
contradicting phi(x)=q-1.

Therefore L is not a source.

Symmetrically R0 cannot be a source. For completeness, if
  h={R0,v,z}
and b<=q-1 is the last left-half path-edge index containing z, then
  r_{2q-2},r_{2q-3},...,r_{q+1}, h, r_b,r_{b+1},...,r_{q-1}
is linear and has last vertex x. Its length is
  (q-2)+1+(q-b)=2q-b-1>=q,
again contradicting phi(x)=q-1.

Hence every high source would have to lie in {A,B}. But the three high edges have three distinct sources by linearity, impossible.

Thus the rising branch phi(C)=2q-2 cannot occur.
