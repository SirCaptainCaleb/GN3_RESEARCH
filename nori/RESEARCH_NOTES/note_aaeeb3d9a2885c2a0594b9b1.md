# Antipodally odd Q5 refutes rootwise arbitrary-order paired-sweep completion

- Stable ID: note_aaeeb3d9a2885c2a0594b9b1
- Author: unspecified; session provenance retained
- Primary home: subsection:paired_direction_involutions_and_geodesic_endpoint_matchings
- Labels: NORI1, paired-midpoint, two-sweep, counterexample, balanced-lift, rootwise-obstruction
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r10003_3
- Updated session: session_nori_r10003_3
- Disposition: none
- Successor: none

## Related references

- note:note_e5b581e8e2c4615b297e9252

## Research note

For a binary undirected-edge coloring c of Q_n, let \(U_i\) exchange the endpoints of every color-zero edge in direction i and fix vertices whose i-edge is color one. For a permutation pi of all n directions, put \(F_\pi=U_{\pi_n}\cdots U_{\pi_1}\) and \(H_c(x)=\{F_\pi(x):\pi\in S_n\}\). Let \(G(c)\) denote roots supporting a color-zero full antipodal geodesic and \(W_{\rm pair}(c)=\{x:H_c(x)\cap H_c(\bar x)\ne\varnothing\}\). The gluing argument gives \(W_{\rm pair}(c)\subseteq G(c)\): if the two zero sweeps meet, their traversed direction sets are complementary and the two red paths concatenate into a full antipodal geodesic.

**Theorem (rootwise paired-sweep completion fails in legal Q5).** Index Q5 vertices by integers x=sum_(i=0)^4 2^i x_i. Delete bit i by \(\rho_i(x)=(x\bmod 2^i)+2^i\lfloor x/2^{i+1}\rfloor\). Let \(c_i(x)\) be bit number \(\rho_i(x)\) of the 16-bit table \(T_i\), least significant bit numbered zero, where
\[
\boxed{(T_0,T_1,T_2,T_3,T_4)=
(\mathtt{7331},\mathtt{9966},\mathtt{ACCA},\mathtt{10F7},\mathtt{3B23})_{\rm hex}.}\tag{1}
\]
These are undirected edge colors because each c_i ignores bit i. Each table's entries at complementary four-bit arguments are opposite, so \(c_i(\bar x)=1-c_i(x)\); hence this is a legal antipodally odd coloring.

At root x=14, the order (4,3,1,0,2) gives the color-zero full geodesic
\[
14\to30\to22\to20\to21\to17=\bar {14}.
\]
Nevertheless the complete zero-sweep endpoint sets are
\[
\begin{aligned}
H_c(14)&=\{9,13,16,17,18,21,23,24,26,28,31\},\\
H_c(17)&=\{2,4,6,11,14,20,22,27,29,30\},
\end{aligned}\tag{2}
\]
which are disjoint. Thus this successful root admits no meeting of the two antipodal sweeps, even when the two orders are chosen independently. It also admits no same-order reversible two-sweep witness.

**Finite certificate.** Formula (1) fixes the 80 direction-edge colors on Q5. For each root x and each of 5!=120 orders pi, evaluate the sweep by starting y=x and, successively for i in pi, replacing y by y xor 2^i iff \(c_i(y)=0\). Collect the 120 endpoints into H_c(x); direct enumeration yields precisely the two 11-element and 10-element lists in (2). To check G(c), independently traverse every order while requiring each of the five traversed edges to be color zero. For this coloring,
\[
|G(c)|=28,\qquad |W_{\rm pair}(c)|=26,\qquad
G(c)\setminus W_{\rm pair}(c)=\{14,17\}.
\tag{3}
\]
The reversible same-order root set has 24 elements, another independent check.

**Product and balanced-lift amplification.** For independent Cartesian factors a,d, all sweep maps split on the factors, and any factor orders can be interleaved. Consequently
\[
H_{a\boxtimes d}(x,y)=H_a(x)\times H_d(y),
\quad
G(a\boxtimes d)=G(a)\times G(d),
\quad W_{\rm pair}(a\boxtimes d)=W_{\rm pair}(a)\times W_{\rm pair}(d).
\tag{4}
\]
For the paired balanced lift L(a) on Q_(2n), every lifted sweep projects to an original sweep, and paired-consecutive sweep orders admit the conjugacy \((x,z=x+y)\mapsto(F_\pi(x),\bar z)\). Antipodal lifted roots have the same z, so
\[
\boxed{W_{\rm pair}(L(a))=W_{\rm pair}(a)\times Q_n,
\qquad G(L(a))=G(a)\times Q_n.}\tag{5}
\]
The second identity follows by projecting any color-zero full geodesic, and conversely inserting each dummy step before or after an original full geodesic according to its color.

Apply (4) to r independent copies of the Q5 coloring (1), then apply (5) to its balanced lift b_r on Q_(10r). The resulting antipodally odd balanced coloring satisfies
\[
\boxed{\frac{|W_{\rm pair}(b_r)|}{|G(b_r)|}
=\left(\frac{26}{28}\right)^r=\left(\frac{13}{14}\right)^r.}\tag{6}
\]
Thus even a given root known to support a monochromatic antipodal geodesic need not support any antipodal paired-sweep midpoint, and the fraction of such rooted geodesic witnesses admitting paired-sweep completion can vanish exponentially in dimension. This does not refute the global existential paired-midpoint conjecture or NORI1.
