# The antipodal-reversal-odd geodesic conjecture

# Antipodal-reversal-odd geodesics and their topological extraction

Let \(Q_n=\mathbb F_2^n\). An *ordered three-face* \((F,\pi)\) is a three-dimensional coordinate face with an ordering \(\pi\) of its free directions, independent of its initial traversal corner. Its binary color satisfies
\[
c(\bar F,\operatorname{rev}\pi)=1\oplus c(F,\pi).
\tag{1}
\]
The **NORI conjecture** asserts that some full antipodal geodesic has at most one change between its \(n-2\) consecutive ordered-three-face colors. Both the corner-independence and the freedom to choose the root are essential; the stronger arbitrary based-window and fixed-root formulations fail.

**Finite foundations.** For \(Q_5\), even an arbitrary face coloring has a full geodesic with at most one change. Otherwise every three-window word alternates, so its first and last window colors coincide. Their disjoint exterior-bit dependencies force all face colors to depend only on direction triples \(h(a,b,c)\). But \(h(a,b,c)\ne h(b,c,d)\) for every four distinct directions would require binary alternation around five cyclic rotations of a five-set, impossible. For \(Q_6\), antipodal reversal combined with six coupled geodesics lifts a monochromatic four-direction segment from the \(Q_5\) theorem to a full good geodesic. These are established closure theorems; they do not induct directly because restricting to a facet fixes exterior bits and loses the required antipodal pairing.

## Reachability with the correct terminal memory

In an antipodally odd *edge*-colored cube, let \(R(x)\) be the vertices monochromatically geodesically reachable from \(x\), of either color. Reversal and complementation imply \(R(\bar x)=\overline{R(x)}\). A vertex reachable from both \(x\) and \(\bar x\) supplies two monochromatic geodesics with disjoint coordinate supports; concatenate them into a one-switch antipodal geodesic and rotate its unequal-color blocks by antipodal complementation to obtain a full monochromatic geodesic. Hence a monochromatic full geodesic exists **iff** \(R(x)\cap R(\bar x)\ne\varnothing\) for some \(x\).

For ordered three-faces, an arbitrary monochromatic connector produces two uncontrolled seam windows. The exact remedy is terminal memory of **two ordered directions**. Fix \(n\ge5\), a root \(x\), \(J=(a,b)\), and \(D=[n]\setminus\{a,b\}\). Let \(R_J(x)\) contain nonempty supports \(U\subseteq D\) for which some monochromatic geodesic from \(x\) has word \((u_1,\ldots,u_k,a,b)\), \(\{u_i\}=U\). The witness color is intentionally forgotten.

**Theorem (exact reversal-tail equivalence).** There is a full NORI geodesic with at most one change if and only if, for some \(x,a,b\), there are nonempty \(U,V\) with \(U\sqcup V=D\) satisfying
\[
U\in R_{(a,b)}(x),\qquad V\in R_{(b,a)}(x).
\tag{2}
\]

**Proof.** Let \(A\) and \(B\) be witnesses with respective words \((U,a,b)\) and \((V,b,a)\). Antipodally reverse \(B\). It starts at \(\overline{x\oplus\chi_V\oplus e_a\oplus e_b}=x\oplus\chi_U\), follows \((a,b,\operatorname{rev}V)\), and is monochromatic in the complementary color. Concatenate it after the \(U\)-prefix of \(A\). The \(k=|U|\) initial windows coincide with those of \(A\); the \(m=|V|\) last windows coincide with those of reversed \(B\). Since \(k+m=n-2\), these are *all* windows. Thus the full path has at most one switch. Conversely, cutting a good full word between its color blocks, and antipodally reversing the suffix, produces the two witnesses from the original root, with complementary supports and reversed terminal directions. For a monochromatic full path choose any interior cut. \(\square\)

## Geometry and genuinely certified labels

The all-root full-geodesic complex is a connected closed \(n\)-pseudomanifold. Its rooted chambers are balls \(e_x*\operatorname{sd}(\partial\Delta^{n-1})\); its dual moves are adjacent direction exchanges and endpoint root slides. Physical antipodality fixes the midpoint of each endpoint edge, so an ordinary free Borsuk–Ulam theorem on this whole complex is unavailable.

The \(2n\)-bit root–progress cube faithfully places different rooted Freudenthal charts on distinct faces. A second endpoint-pair construction realizes the genuine monochromatic extension states as an \(n\)-torus, not a ball. In NORI, deleting the first move of a monochromatic \((U,a,b)\) witness preserves its endpoint and terminal memory while moving the root and shrinking \(U\). Geometrically the move runs on one of two crossing diagonals of a root/support coordinate square, depending on an endpoint bit. A projected crossing is not a pair of actual path witnesses; independent slides need not preserve a common root.

Two proved examples forbid standard shortcuts. In antipodally odd edge-colored \(Q_4\), the reachability nerve can contain all triangular faces of a cube square while lacking the full four-corner simplex. In paired-coordinate edge colorings of \(Q_{2m}\),
\[
|R(x)|=3^{A+H}+3^{B+H}-2^H\le 2\cdot3^m-2^m<2^{2m-1}
\]
for \(m\ge5\), with \(A,B,H\) the counts of initial \(00,11,\) and mixed pairs. A mixed-pair root nevertheless has a full monochromatic antipodal geodesic. Large cardinality and automatic cubical nerve filling are therefore not universal mechanisms. A convex-hull zero of bit-string labels may likewise be witnessed by noncomplementary labels.

## Two exact topological closure targets

**Reversed-tail carrier.** Build an equivariant simplicial/cubical/Hex carrier whose labels are genuinely witnessed \(R_{(a,b)}(x)\) and \(R_{(b,a)}(x)\), with incidence, boundary conditions, and same-root compatibility sufficient to force (2). An alternating simplex, root-sheet crossing, or balanced interpolation is insufficient unless accompanied by an *actual extraction* of (2).

**Four-facet cap-memory graph.** Fix \(n-2\) directions \(U\), omit \(a,b\), and choose a projected root \(r\) on \(U\). Let \(A_i(r)\) be the color on the physical ordered face \((a,b,i)\). It is independent of fixed \(a,b\) bits. Join first and last directions \(i,j\in U\) of any monochromatic \(U\)-spanning path in one of four parallel facets based at \(r\). The proved two-cap comparison under hypothetical global failure gives, for its witness color \(q\),
\[
q=A_i(r)=1\oplus A_j(r).
\tag{3}
\]
Thus the graph must be bipartite. **Any odd cycle** forces grand closure. The remaining obligation is producing enough compatible near-spanning monochromatic paths to violate this cut.

The conjecture remains open for \(n\ge7\). The present conclusions replace an assortment of low-dimensional cases by two exact dimension-independent extraction targets: a same-root reversed-tail collision, or an odd cycle of physically witnessed cap-memory connectors. A fixed-point proof must now establish the necessary *existence* implication, not merely a topological symmetry of an abstract label space.
