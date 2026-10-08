# The first five-coordinate carrier failure is exactly an isolated-singleton defect — preserved pre-item development

## Development

## The first five-coordinate failure of packet separation is exactly an isolated singleton defect

Continue with the consecutive-change defect
\[
C(\pi)=\sum_{j=1}^{k-1}(e_{v_{p_j}}-e_{v_{p_{j+1}+3}})
\]
for a bad ternary order \(\pi\), where
\[
p_1<\cdots<p_k
\]
are its change positions.

Fix one packet of five consecutive positions
\[
I=\{r,r+1,r+2,r+3,r+4\}
\]
and keep every position outside \(I\) as a singleton packet. Give all five coordinates occupying \(I\) one common weight and assign strictly increasing weights to the packets from left to right. Let \(w\) be the resulting functional.

Every consecutive-change summand has endpoint-position gap at least four. Therefore
\[
\langle w,e_x-e_y\rangle\le 0
\]
for every summand of every order obtained by permuting the five coordinates inside \(I\).

Equality can occur only when both endpoints lie in \(I\). Since the packet has exactly five positions and the endpoint gap is at least four, equality forces the endpoints to occupy positions \(r\) and \(r+4\). Hence the underlying consecutive change positions are exactly
\[
p_j=r,\qquad p_{j+1}=r+1.
\]
Equivalently, the three consecutive ternary statuses beginning at rank \(r\) are
\[
010\qquad\text{or}\qquad 101.
\]

### Zero-pairing classification

Suppose
\[
\langle w,C(\pi)\rangle=0.
\]
Every summand of \(C(\pi)\) has nonpositive pairing, so every summand must pair to zero.

The five-position packet supports only one consecutive-change pair with both endpoints inside it, namely the pair \(r,r+1\). Therefore \(C(\pi)\) has exactly one summand. Consequently
\[
k=2,\qquad \{p_1,p_2\}=\{r,r+1\},
\]
and
\[
C(\pi)=e_{v_r}-e_{v_{r+4}}.
\]

Thus the entire global status word has exactly two changes, and they are adjacent. The order is an isolated-singleton state:
\[
0\cdots 010\cdots 0
\]
or
\[
1\cdots 101\cdots 1.
\]

Conversely, such a state has exactly one macro-root joining the first and fifth positions of the corresponding five-coordinate packet, so it has zero pairing with the packet-collapse functional.

Hence
\[
\boxed{\langle w,C(\pi)\rangle=0
\iff
\pi\text{ has exactly two adjacent changes supported on }I.}
\]

### Convex-zero consequence

Take any collection of bad orders obtained by permuting the same five-coordinate packet \(I\), and suppose
\[
0\in\operatorname{conv}\{C(\pi_s)\}.
\]
Pair with \(w\). Every label has nonpositive pairing, so every label used with positive coefficient must have zero pairing. Therefore every supporting order is an isolated-singleton state with its two changes at the same two adjacent ranks.

Each supporting label is then a single endpoint root
\[
e_{a_s}-e_{b_s},
\]
where \(a_s\) and \(b_s\) are the first and fifth coordinates of the packet in that state.

Thus every first-support five-coordinate carrier zero reduces to a positive directed circulation on endpoint roots of isolated-singleton witnesses.

### Article III consequence

Combined with §240:

- packets on at most four positions are strictly hemisphere-safe;
- the first packet size at which the symmetric consecutive-change carrier can lose strict separation is five;
- at that first size, every state in the zero support is already one of the isolated-singleton configurations targeted by the flat/full transition and exported-transport machinery.

So the witnessed-degree program reaches the local repair complex without an intermediate arbitrary A3/A4 circuit classification. The remaining five-coordinate extraction problem is precise: resolve a positive endpoint-root circulation whose every vertex is a global isolated-singleton witness, preserving the witness class through flat repair, double-full resolution, or exported transport.
