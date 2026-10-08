# An odd violation vector whose chamber zeros are one-change words — preserved pre-item development

## Development


A useful construction survived in the GN3 brainstorm archive.

Suppose a binary chamber word is organized around a distinguished center so that violations of the desired directed one-change pattern occur in paired left/right positions. For each distance \(d\), let
\[
x_d\in\{0,1\}
\]
record a left violation and
\[
y_d\in\{0,1\}
\]
record the reflected right violation. Reversal exchanges \(x_d\) and \(y_d\).

Choose any antipodal sign \(g\in\{\pm1\}\), so \(g(\pi^{\mathrm{rev}})=-g(\pi)\), and define
\[
F_d=x_d-y_d+g\,x_dy_d.
\]
Then
\[
F_d(\pi^{\mathrm{rev}})=-F_d(\pi),
\]
and \(F_d=0\) precisely when neither violation occurs at distance \(d\).

Hence the vector \(F=(F_1,\ldots,F_D)\) is odd and vanishes on a chamber precisely when the centered directed one-change condition holds.

A particularly local gauge is the relative-order sign of two fixed labels \(a,b\). This gauge changes under an adjacent transposition only when that transposition swaps \(a,b\).

The construction is not yet a direct formulation of unrestricted NOR because it uses a chosen center. Its value is as a template for building odd defect maps whose chamber zeros coincide with the desired word condition.
