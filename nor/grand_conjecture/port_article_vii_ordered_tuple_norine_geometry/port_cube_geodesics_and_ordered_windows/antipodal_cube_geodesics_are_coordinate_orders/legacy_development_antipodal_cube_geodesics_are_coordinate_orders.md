# Antipodal cube geodesics are coordinate orders — preserved pre-item development


Let \(Q_V\) be the Boolean cube on an \(n\)-element coordinate set \(V\). If
\[
G=(X_0,X_1,\ldots,X_n),\qquad X_n=V\setminus X_0,
\]
is a geodesic, then \(d(X_0,X_n)=n\), so the length \(n\) path must flip every coordinate exactly once. Writing
\[
X_{i-1}\triangle X_i=\{v_i\},
\]
the sequence
\[
(v_1,\ldots,v_n)
\]
is therefore a permutation of \(V\).

Conversely, for every start vertex \(X_0\subseteq V\) and every permutation \((v_1,\ldots,v_n)\), flipping the coordinates in that order gives an antipodal geodesic from \(X_0\) to \(V\setminus X_0\).

Thus an antipodal cube geodesic carries two independent pieces of data:
1. a starting sign pattern \(X_0\);
2. a coordinate order \((v_1,\ldots,v_n)\).

For ordered-tuple NOR, the second datum is the relevant combinatorial order. The start vertex changes which coordinate flips are upward or downward in Boolean rank, but it does not change the order in which the coordinates are encountered.
