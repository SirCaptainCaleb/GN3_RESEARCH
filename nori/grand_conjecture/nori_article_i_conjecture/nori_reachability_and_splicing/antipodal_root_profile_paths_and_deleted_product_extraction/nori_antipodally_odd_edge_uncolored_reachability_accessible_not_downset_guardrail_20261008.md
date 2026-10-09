# Odd edge-color reachability sets are geodesically accessible but need not be Boolean downsets

# Geodesic reachability regions are accessible but NOT Boolean downsets, even with antipodal oddness

Let Q_n be an UNDIRECTED binary edge-colored cube satisfying c(bar e)=1−c(e). As usual let R(x) consist of endpoints of monochromatic geodesics from x, allowing either color, including x. For each root x define the reachable coordinate-support family
\[
\mathcal R_x=\{S⊆[n]:x⊕S∈R(x)\}.
\]

**THEOREM 1 (accessibility).** For every nonempty S∈\mathcal R_x, there exists at least one i∈S with S\{i}∈\mathcal R_x. In fact a witness monochromatic shortest path for S certifies every prefix of its specific direction order.

**Proof.** A shortest x→x⊕S path changes every coordinate of S once. Deleting its last edge leaves a monochromatic geodesic from x to x⊕(S\{i}) for the last direction i. Repeat for prefixes. QED.

**THEOREM 2 (explicit counterexample to full downward closure under active edge oddness).** On Q_3 choose the following binary colors for the 12 UNDIRECTED physical edges, written in the convention with coordinate bits (x_1,x_2,x_3) and the displayed bitstrings interpreted as subsets of coordinates, so '100' means e_1:
\[
\begin{array}{c|c}
\text{edge endpoints}&\text{color}\\\hline
000-100&0\\
001-101&0\\
010-110&1\\
011-111&1\\
000-010&0\\
001-011&1\\
100-110&0\\
101-111&1\\
000-001&1\\
010-011&0\\
100-101&1\\
110-111&0
\end{array}
\]
Each physical edge paired with its coordinatewise antipodal image has exactly complementary color, so the coloring is valid.

There is a monochromatic color-0 geodesic
\[
000\to100\to110\to111,
\]
so \(\{1,2,3\}\in\mathcal R_{000}\). But \(101\notin R(000)\): its only two geodesics from 000 are
\(000\to100\to101\), colored (0,1), and \(000\to001\to101\), colored (1,0), neither monochromatic. Thus \(\{1,3\}\notin\mathcal R_{000}\), despite being a subset of \(\{1,2,3\}\).

**CONSEQUENCE.** Even in the simpler edge-colored proving ground, antipodally odd monochromatic-geodesic reachability need NOT be an order ideal of the Boolean lattice. A proof using full downward closure, the ordinary face-KKM covering property for ALL lower-dimensional coordinate faces, or intersections of arbitrary reachable support subsets is INVALID without additional arguments. The TRUE invariant is *geodesic accessibility along SOME prefix chain*, not inclusion of every sub-support. This sharp distinction is essential when trying to extend the proven special parity-root chart connectivity to unrestricted NORI via a general topological reachability theorem.
