# Proposition 5 — preserved pre-item development

## Development

The affine plane \(A_2\) contains no spanning \(4\)-edge linear path.

#### Proof
A spanning \(4\)-edge path on nine vertices has three joints. By Lemma 4, their sum is zero. Three distinct points of \(\mathbb F_3^2\) sum to zero exactly when they form an affine line. But then the edge determined by two consecutive joints contains the third joint as well, contradicting the intersection pattern of a linear path. ∎

This obstruction is not stable with dimension. In \(A_3\), the following thirteen affine lines form a spanning \(13\)-edge path:
\[
\begin{aligned}
&\{000,100,200\},\ \{000,001,002\},\ \{001,010,022\},\\
&\{010,110,210\},\ \{011,110,212\},\ \{012,112,212\},\\
&\{012,102,222\},\ \{021,120,222\},\ \{120,121,122\},\\
&\{101,111,121\},\ \{020,111,202\},\ \{202,211,220\},\\
&\{201,211,221\}.
\end{aligned}
\]
Consecutive lines meet once, nonconsecutive lines are disjoint, and their union is all \(27\) points. Thus the joint-sum condition alone cannot yield an infinite affine family.
