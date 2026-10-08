# Lexicographic extremality forces full boundaries on every wide two-change band — preserved pre-item development

## Composition

(none yet)

## Development

## Lexicographic extremality forces full boundaries on every wide two-change band

Work in the coboundary-flat alternating ternary sector. Consider a full order with exactly two changes,
\[
0^A1^B0^C,qquad A,B,C\ge1.
\]
Among all such full orders, fix one maximizing lexicographically \((A,B)\).

Root §254 proves that \(B=1\) is impossible in an extremal order. We extend the same potential to wider bands.

### Left boundary

Assume \(B\ge3\). Let six consecutive coordinates at the left edge of the 1-band be
\[
(a,b,c,d,e,f,\ldots)
\]
with
\[
\alpha(a,b,c)=0,quad
\alpha(b,c,d)=1,quad
\alpha(c,d,e)=1,quad
\alpha(d,e,f)=1
\]
whenever the displayed windows exist; for \(B=3\), the next untouched window after these is the first trailing zero.

Suppose the left transition tetrahedron \((a,b,c,d)\) is flat. Then
\[
\alpha(a,b,d)=0.
\]
Swap only \(c,d\):
\[
(a,b,c,d,e,f,\ldots)\mapsto(a,b,d,c,e,f,\ldots).
\]
The first three new statuses are
\[
\alpha(a,b,d)=0,qquad
\alpha(b,d,c)=0,qquad
\alpha(d,c,e)=0.
\]
The next status \(z=\alpha(c,e,f)\) is arbitrary.

If \(B=3\), the following unchanged status is already 0, so the affected packet is
\[
0,0,0,z,0.
\]
For either \(z\), the 1s form at most one contiguous run; if \(z=0\) NOR closes, and if \(z=1\) the leading zero run strictly increases.

If \(B>3\), the following unchanged status is 1, so the packet is
\[
0,0,0,z,1,
\]
again compatible with a two-change word and with a strictly longer leading zero run.

Thus a flat left boundary contradicts lexicographic maximality. Therefore every extremal band with \(B\ge3\) has a fully-curved left transition.

### Right boundary

Assume \(C\ge2\). Let the last 1-to-0 transition be carried by
\[
(a,b,c,d,e,\ldots)
\]
with
\[
\alpha(a,b,c)=1,qquad
\alpha(b,c,d)=0,qquad
\alpha(c,d,e)=0.
\]

If this transition is flat, then
\[
\alpha(a,b,d)=1.
\]
Swap \(c,d\). The new initial tail is
\[
1,1,1,z,
\]
where \(z\) is the only new farther crossing status; every subsequent untouched status is 0 when present.

Hence the resulting global word is either NOR-good or remains of the form
\[
0^A1^{B'}0^{C'}
\]
with the same \(A\) and
\[
B'>B.
\]
This again contradicts lexicographic maximality.

Therefore every extremal two-change order with \(C\ge2\) has a fully-curved right transition.

### Consequence

A lexicographically maximal two-change order satisfies:

- \(B\ge2\);
- if \(B\ge3\), its left boundary is fully curved;
- if \(C\ge2\), its right boundary is fully curved.

Thus every nonterminal wide extremal band is forced into the full-full barrier regime. The only exceptional geometries left outside that regime are the width-two band \(B=2\) and the terminal trailing case \(C=1\) (together with their reversed counterparts).

This connects the run-potential program directly to the existing width-two/full-barrier machinery of §§219–226: flat boundary behavior is eliminated globally by the same finite lexicographic potential rather than by a separate transport classification.
