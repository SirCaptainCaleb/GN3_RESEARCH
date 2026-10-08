# Theorem 5

\[
6|E(H)|
=
\sum_v\bigl(4p_v-2+\beta(p_v)\bigr)
-D-\eta-2(A-C)-2R. \tag{13}
\]

#### Proof
For a fixed \(v\), the path \(P_v\) has \(2p_v-2\) vertices outside its last edge. Distinct incident edges can use each such vertex at most once, so (12) is nonnegative.

Summing the multiplicities \(\mu_{P_v}(e)\) over all incidences, an ordinary incidence contributes \(1\), a zero-intersection incidence contributes \(0\), and a double-intersection incidence contributes \(2\). Hence
\[
3m-C+D=2S-n_+-R. \tag{14}
\]

A zero-intersection incidence can occur only at the unique entrance of an ascending edge; otherwise the incident edge could be appended to the chosen maximum path. Therefore
\[
C\le A. \tag{15}
\]
Every ascending edge has two terminal vertices, so
\[
\sum_v t(v)=2A. \tag{16}
\]
By (11),
\[
\sum_v\beta(p_v)=2A-D+\eta. \tag{17}
\]
Substituting (17) into twice (14) gives (13). ∎
