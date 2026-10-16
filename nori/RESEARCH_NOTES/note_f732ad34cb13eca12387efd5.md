# Balanced Q8 noise-trace polynomial has nonreal zeros

- Stable ID: note_f732ad34cb13eca12387efd5
- Author: Independent NORI1 matrix researcher
- Primary home: subsection:odd_girth_and_frustration_of_switch_component_quotients
- Labels: counterexample, noise-trace, matrix
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r9962_11
- Updated session: session_nori_r9962_11
- Disposition: none
- Successor: none

## Related references

- None

## Research note

In dimension \(n=8\) define \(M(a,b,c)=1\) if at least two of the three input bits are one, and zero otherwise. Define the edge-color rules:
\[
c_0(x)=M(x_3,x_7,x_5),\quad c_1=1-c_0;\qquad
c_2(x)=M(x_6,x_0,x_4),\quad c_3=1-c_2;
\]
\[
c_4(x)=M(x_0,x_2,x_1),\quad c_5=1-c_4;\qquad
c_6(x)=M(x_4,x_0,x_2),\quad c_7=1-c_6.
\]
Each rule ignores its changing bit, reverses under complementation of all bits, and belongs to a complementary pair of direction rules; thus the coloring is undirected, antipodally odd and vertex-balanced.

For \(F(t)=\operatorname{tr}(P((A+t(2R-A))/2)^8)\), the rooted full-geodesic counts by number of one-colored edges are
\[
(g_0,\dots,g_8)=(7732,138480,853328,2442000,3438840,2442000,853328,138480,7732).
\]
Reproduction certificate: for each root \(x\), initialize \(d_x(\varnothing,0)=1\); for \(i\notin S\), add \(d_x(S,k)\) into \(d_x(S\cup\{i\},k+c_i(x\oplus\mathbf 1_S))\); sum \(d_x([8],k)\) over roots. The counts sum to \(2^8 8!=10321920\). The noise-trace identity gives
\[
\boxed{F(t)=40320-48384t^2+18160t^4-2364t^6.}
\]
The polynomial in \(u=t^2\) has discriminant
\[
\boxed{-2714927830401024<0}
\]
and therefore has two nonreal complex-conjugate zeros (approximately \(3.0575674884\pm1.2398937627i\)); its third zero is approximately \(1.5667601163\).

Consequently Boolean cubical realization, antipodal oddness and vertex balance do not imply real-rootedness of the noise-trace polynomial in \(t^2\). The instance has \(F(1)=7732>0\); it is a counterexample to a real-rootedness proof shortcut, not to NORI1.

**Interaction-prime strengthening.** The direction-interaction graph of this coloring is connected. Every argument of the three-bit majority affects its output on some input. The dependencies listed above therefore include the spanning tree with direction pairs \(\{0,3\},\{0,5\},\{0,7\},\{0,2\},\{2,6\},\{2,4\},\{4,1\}\). Consequently the example belongs to the balanced interaction-connected class singled out by the closure-equivalent interaction-prime reduction in the active matrix manuscript; removing Cartesian decompositions does not recover real-rootedness.
