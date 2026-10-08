# Lemma 4

For every nonisolated \(v\),
\[
t(v)-D_v\le \beta(p_v). \tag{6}
\]

#### Proof
If \(T(v)=\varnothing\), the assertion is immediate.

Suppose first that \(q(v)=p_v\). Choose \(P_v\) with last edge an ascending edge of rank \(p_v\). Lemma 1, with the double intersections removed, gives
\[
t(v)-D_v
\le
1+\left\lceil\frac{3p_v-8}{4}\right\rceil
=
\left\lceil\frac{3p_v-4}{4}\right\rceil . \tag{7}
\]

Now suppose \(q(v)<p_v\). Corollary 2 gives
\[
t(v)\le \gamma(q(v))\le \gamma(p_v-1). \tag{8}
\]
After the \(D_v\) double intersections are removed, every remaining member of \(T(v)\) has one off-\(v\) intersection with \(P_v\). Lemma 3 gives
\[
t(v)-D_v
\le
\max(0,4q(v)-2p_v-3)
\le
\max(0,2p_v-7). \tag{9}
\]
Thus
\[
t(v)-D_v
\le
\min\{\gamma(p_v-1),\max(0,2p_v-7)\}. \tag{10}
\]
Comparing (7) and (10) with (5), directly for \(p_v\le7\) and by the floor formula for \(p_v\ge8\), gives (6). ∎

Define the local nonnegative quantity
\[
\eta_v=\beta(p_v)-t(v)+D_v. \tag{11}
\]
Let
\[
D=\sum_vD_v,\qquad \eta=\sum_v\eta_v.
\]
Let \(C\) be the number of incidences \((v,e)\) for which \(\mu_{P_v}(e)=0\), and let
\[
R=\sum_v\left(2p_v-1-\sum_{e\ni v}\mu_{P_v}(e)\right). \tag{12}
\]
Linearity gives \(R\ge0\).

Let \(A\) be the number of ascending edges.
