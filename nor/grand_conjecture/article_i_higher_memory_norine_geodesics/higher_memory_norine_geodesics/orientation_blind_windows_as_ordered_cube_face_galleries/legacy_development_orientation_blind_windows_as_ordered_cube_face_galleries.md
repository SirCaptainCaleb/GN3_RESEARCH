# Orientation-blind windows as ordered cube-face galleries — preserved pre-item development


## Orientation-blind windows are ordered cube faces

The support-orientation-blind repair has a cleaner geometric formulation.

Represent a geodesic \(r\)-segment by
\[
(X;v_1,\ldots,v_k),
\]
where the successive flipped coordinates \(v_i\) are distinct and
\[
K=\{v_1,\ldots,v_k\}.
\]
Support-orientation blindness means that toggling any subset of the used coordinates before traversing the segment does not change its color:
\[
\chi(X\triangle T;v_1,\ldots,v_k)=\chi(X;v_1,\ldots,v_k)
\qquad (T\subseteq K).
\]

Therefore the color depends only on:

1. the \(r\)-dimensional cube face
   \[
   F=\{Y\subseteq V:Y\setminus K=X\setminus K\},
   \]
   whose free coordinate set is \(K\); and
2. the ordering
   \[
   (v_1,\ldots,v_k)
   \]
   of the coordinate directions of that face.

Thus the repaired local datum is naturally a binary coloring of **ordered \(r\)-faces** of \(Q_V\).

For \(r=1\), an ordered one-face has no nontrivial axis ordering, so this is exactly an ordinary undirected cube-edge coloring. For the translation-invariant GN3 subclass at \(r=3\), the color further forgets the location of the 3-face and depends only on its ordered coordinate directions.

### Sliding galleries induced by antipodal geodesics

Let
\[
G=(X_0,\ldots,X_n)
\]
be an antipodal geodesic with flip order
\[
(v_1,\ldots,v_n).
\]
For each
\[
0\le i\le n-r
\]
let \(F_i\) be the ordered \(r\)-face with free directions
\[
(v_{i+1},\ldots,v_{i+r})
\]
and with outside coordinates fixed as in \(X_i\).

Then consecutive faces \(F_i,F_{i+1}\) meet in the \((r-1)\)-face whose free directions are
\[
(v_{i+2},\ldots,v_{i+r}).
\]
Indeed \(F_{i+1}\) fixes the departing coordinate \(v_{i+1}\) to its value after the geodesic crosses it, while \(F_i\) fixes the entering coordinate \(v_{i+r+1}\) to its value before it is crossed; all other fixed coordinates agree. Their intersection is therefore exactly a codimension-one common face.

Hence every antipodal cube geodesic canonically determines a **sliding ordered-\(r\)-face gallery**
\[
F_0,F_1,\ldots,F_{n-r}.
\]
The repaired one-change problem asks for such an antipodal sliding gallery whose face-color word changes at most once.

Under complement-plus-reversal, an ordered face
\[
(F;v_1,\ldots,v_k)
\]
is sent to the antipodal face with reversed ordered directions
\[
(\bar F;v_k,\ldots,v_1),
\]
and the color is complemented.

### Why this abstraction matters

This is the direct higher-dimensional analogue of the original edge problem:

- \(r=1\): colored cube edges along an antipodal geodesic;
- general \(r\): colored ordered \(r\)-faces along the sliding gallery cut out by an antipodal geodesic.

The object being colored is no longer an oriented path fragment with an accidental choice of starting corner. The entire \(2^r\)-vertex face is the local cell, while the axis order records the directed memory that is essential for GN3.

This face-gallery formulation preserves both intended anchor cases and removes the uniform rank-parity defect. It is therefore a stronger candidate for the corrected NOR grand conjecture than full translation invariance.
