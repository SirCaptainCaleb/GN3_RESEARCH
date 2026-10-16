# Balanced Q8 alternating-sign counterexample

- Stable ID: note_balanced_q8_noise_sign_counterexample_20261015
- Author: unspecified; session provenance retained
- Primary home: subsection:odd_girth_and_frustration_of_switch_component_quotients
- Labels: counterexample, noise_trace, balanced_cube
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r10003_1
- Updated session: session_nori_r10003_1
- Disposition: none
- Successor: none

## Related references

- None

## Research note

### Balanced Q8 counterexample to alternating noise coefficients

For a vertex \(x\in\mathbb F_2^8\), define signed direction rules
\[
s_0=(-1)^{x_2},\ s_1=-s_0,\ s_2=(-1)^{x_0},\ s_3=-s_2,\quad
s_4=(-1)^{x_6},\ s_5=-s_4,\ s_6=(-1)^{x_4},\ s_7=-s_6.
\tag{1}
\]
Let \(U=e_4+\operatorname{span}_{\mathbb F_2}\{e_5,e_7\}\). At vertices of \(U\cup\bar U\), reverse both \(s_5\) and \(s_7\); all remaining values stay unchanged. Write \(s'_i\) for the new signed rules.

**Theorem.** The resulting edge coloring is vertex-balanced and antipodally odd, and
\[
\boxed{F_{c'}(t)=40320-53160t^2+17200t^4+216t^6.}\tag{2}
\]
In particular the conjectured sign rule \((-1)^k[t^{2k}]F\ge0\) fails already at \(k=3\) in an admissible balanced \(Q_8\).

*Legality.* Every rule in (1) ignores its own direction bit and is odd under antipodal complementation. The set \(U\cup\bar U\) is invariant under flips of bits 5 and 7 and under antipodal complementation, so these properties persist. At each vertex of \(U\), \((s_5,s_7)=(-1,+1)\), and at each vertex of \(\bar U\), \((s_5,s_7)=(+1,-1)\). Simultaneous reversal preserves their sum, and the original signed incident sum vanishes everywhere.

*Counting certificate.* For each of the 256 roots \(x\), let \(d_x(S,k)\) count directed paths traversing precisely the directions of \(S\), with \(k\) one-colored edges. Start with \(d_x(\emptyset,0)=1\), and for every \(i\notin S\) update
\[
d_x(S\cup\{i\},k+\mathbf 1_{s'_i(x\oplus e_S)=-1})
\mathrel{+}=d_x(S,k).
\tag{3}
\]
Summing \(d_x([8],k)\) over all roots gives
\[
(g_0,\dots,g_8)=(4576,109056,848384,2471424,3455040,
2471424,848384,109056,4576).
\tag{4}
\]
Their sum is \(256\cdot8!\) and they are symmetric under \(k\leftrightarrow8-k\). Substitution into
\(F(t)=\sum_{k=0}^{8}g_k((1+t)/2)^{8-k}((1-t)/2)^k\)
establishes (2). A separate subset recurrence accumulating signed monomials \(\prod(1+t s'_i)\), divided by \(2^8\), confirms (2).

**Both coefficient signs in the interaction-connected class.** The product coloring (1) has \(F(t)=40320-53760t^2+17920t^4\). Instead flipping directions 0 and 1 on the square \(\operatorname{span}\{e_0,e_1\}\) and its antipode yields
\[
F_-(t)=40320-53160t^2+17680t^4-280t^6.
\tag{5}
\]
Both square-traded colorings have connected direction-influence graphs: the original blocks \(\{0,1,2,3\}\) and \(\{4,5,6,7\}\) are each connected, and their antipodally localized square modifications make a signed rule in one block sensitive to a bit in the other. Hence even restricting to the interaction-prime class leaves both signs possible.

**Extension to every even dimension at least twelve.** Let \(c_4\) have signed rules given by the first four directions of (1), with \(F_4(t)=24-16t^2\). Let \(c_6\) have
\(s_{2j}=(-1)^{x_{2((j+1)\bmod3)}}\), \(s_{2j+1}=-s_{2j}\) for \(j=0,1,2\), giving \(F_6(t)=720-720t^2+144t^4\). For \(n=8+4a+6b\), take \(c'\boxtimes c_4^{\boxtimes a}\boxtimes c_6^{\boxtimes b}\). The tensorization theorem gives
\[
F_n(t)=\frac{n!}{8!(4!)^a(6!)^b}F_{c'}(t)F_4(t)^aF_6(t)^b.
\tag{6}
\]
The highest nonzero coefficient occurs in degree \(d=6+2a+4b\) and equals
\[
\frac{n!}{8!(4!)^a(6!)^b}\,216(-16)^a144^b.
\tag{7}
\]
Its sign is \((-1)^a\), opposite to the proposed \((-1)^{d/2}=(-1)^{3+a}\). Every even \(n\ge12\) has the form \(8+4a+6b\). In (2) the coefficient of \((1-t^2)^3\) is \(-216\), also defeating nonnegative coefficients in that basis.

These constructions have monochromatic antipodal geodesics (\(g_0(c')=4576\)); they refute the proposed trace-sign principle and leave NORI1 open.
