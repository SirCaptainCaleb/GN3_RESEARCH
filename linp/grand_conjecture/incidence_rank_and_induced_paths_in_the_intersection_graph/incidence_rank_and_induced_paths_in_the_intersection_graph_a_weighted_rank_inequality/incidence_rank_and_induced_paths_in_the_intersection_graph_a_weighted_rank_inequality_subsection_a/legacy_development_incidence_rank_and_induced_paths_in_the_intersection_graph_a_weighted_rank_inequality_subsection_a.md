# Theorem 4 — preserved pre-item development

## Development

Assign weights \(0\le w_e\le1\) to the edges of \(H\). Put
\[
W=\sum_e w_e,
\qquad
d_w(v)=\sum_{e\ni v}w_e.
\]
If
\[
d_w(v)\le D
\qquad\text{for every }v,
\]
then
\[
\operatorname{rank}N\ge \frac{3W}{D+2}. \tag{6}
\]

#### Proof
Let
\[
R=\operatorname{diag}(w_e)
\]
and
\[
Q=R^{1/2}N^TNR^{1/2}.
\]
Then \(Q\) is positive semidefinite and
\[
\operatorname{rank}Q\le\operatorname{rank}N.
\]
Since every hyperedge has size three,
\[
\operatorname{tr}Q=3W.
\]

By linearity,
\[
Q_{ee}=3w_e,
\]
and for \(e\ne f\),
\[
Q_{ef}=
\begin{cases}
\sqrt{w_ew_f},&e\cap f\ne\varnothing,\\
0,&e\cap f=\varnothing.
\end{cases}
\]
Hence
\[
\operatorname{tr}(Q^2)
=
9\sum_e w_e^2
+
2\sum_{e<f,\ e\cap f\ne\varnothing}w_ew_f. \tag{7}
\]

On the other hand,
\[
\sum_v d_w(v)^2
=
3\sum_e w_e^2
+
2\sum_{e<f,\ e\cap f\ne\varnothing}w_ew_f, \tag{8}
\]
because every intersecting pair has a unique common vertex. Combining (7) and (8),
\[
\operatorname{tr}(Q^2)
=
6\sum_e w_e^2+\sum_v d_w(v)^2.
\]
Since \(0\le w_e\le1\),
\[
\sum_e w_e^2\le W.
\]
Also,
\[
\sum_v d_w(v)^2
\le
D\sum_v d_w(v)
=
3DW.
\]
Therefore
\[
\operatorname{tr}(Q^2)\le 3(D+2)W.
\]
For a positive semidefinite matrix,
\[
\operatorname{rank}Q
\ge
\frac{(\operatorname{tr}Q)^2}{\operatorname{tr}(Q^2)}.
\]
Substituting the preceding estimates gives
\[
\operatorname{rank}N
\ge
\operatorname{rank}Q
\ge
\frac{9W^2}{3(D+2)W}
=
\frac{3W}{D+2}.
\]
∎
