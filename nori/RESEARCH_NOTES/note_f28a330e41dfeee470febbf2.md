# Exponential directed-hexagon traps for monotone antipodal square flips

- Stable ID: note_f28a330e41dfeee470febbf2
- Author: unspecified; session provenance retained
- Primary home: subsection:paired_direction_involutions_and_geodesic_endpoint_matchings
- Labels: eulerian, large-square-flip-trap, all-dimensional
- Lifecycle: active
- Epistemic status: proved
- Current version: 3
- Retention: current and at most one previous snapshot
- Created session: session_nori_r10487_3
- Updated session: session_nori_r10487_3
- Disposition: none
- Successor: none

## Related references

- None

## Research note

### Antipodal directed hexagons give strict local minima for square-only descent

Work in \(Q_6\), with original bits \(x_0,x_1,x_2\), dummy bits \(y_0,y_1,y_2\), and direction indices \(0,1,2,3,4,5\). Define the legal balanced coloring \(a\) by
\[
a_i(x,y)=x_{i+1\pmod3},\qquad
a_{3+i}(x,y)=1\oplus x_{i+1\pmod3}\quad(0\le i<3).
\tag{HX1}
\]
This is the complementary paired lift of the unary cycle \(c_i=x_{i+1\pmod3}\) on \(Q_3\).

**Theorem (six-cycle obstruction to monotone square descent).** Let \(C\) be the directed six-cycle in the canonical orientation of \(a\), beginning at \(v=(x,y)=(001,000)\) when \(x_0\) is the low-order bit, with direction word
\[
\boxed{(2,0,1,2,0,1).}
\tag{HX2}
\]
Let \(b\) be obtained from \(a\) by reversing the edge colors on the twelve-edge set \(F=E(C)\cup E(\tau C)\), where \(\tau(x,y)=(\bar x,\bar y)\). Then \(b\) remains perfectly balanced and antipodally odd and differs from \(a\) on twelve edges, four in each original direction and none in dummy directions. However, every legal antipodal directed-square flip of \(a\) increases its edge-disagreement distance to \(b\) from twelve to at least sixteen. Consequently the strictly decreasing paired-cycle descent theorem cannot in general be implemented using directed square flips alone.

*Proof.* Vertex balance and antipodal oddness of \(a\) follow from the complementary paired rules (HX1). Starting at integer \(x=1\) with \(y=0\), the cycle (HX2) runs through the distinct old vertices
\[
1\to5\to4\to6\to2\to3\to1,
\]
all with dummy state \(y=000\). Its edge colors are \(1,0,1,0,1,0\), respectively. The starting vertex has odd parity, so these colors are precisely the outward arrows of the canonical orientation at their successive tails; \(C\) is directed. Its antipodal mate lies in the disjoint face \(y=111\) and is directed with reversed cyclic order. Flipping the two directed cycles preserves indegree and outdegree at all vertices and maintains the antipodal relation, so \(b\) is balanced and legal. Each of directions \(0,1,2\) occurs twice in \(C\) and twice in \(\tau C\), proving the disagreement counts.

There are no directed squares using only two original directions. Indeed, among any two distinct original indices \(i,j\), one is the cyclic successor of the other; hence one of the edge rules \(a_i=x_{i+1}\), \(a_j=x_{j+1}\) changes when the other bit is flipped. Its two opposite edges around that square have different colors. A directed square in the canonical orientation would instead need its two opposite edges to have the same color (the square colors must alternate cyclically). Thus each directed square uses at least one dummy direction.

The disagreement set \(F\) consists solely of original-direction edges contained in the two opposite fixed-dummy facets \(y=000\) and \(y=111\). A square involving a dummy direction contains at most one original-direction edge in either one of these facets, and it cannot meet both facets, whose dummy states differ in three bits. Hence every directed square shares at most one edge with \(F\), and every antipodal pair of directed squares shares at most two edges with \(F\).

Each permitted paired-square flip toggles eight distinct edges. If \(h\le2\) of them already disagree with \(b\), the new disagreement count is
\[
12+8-2h\ge16.
\]
Therefore no such flip decreases, or even preserves, the disagreement potential. Reversing the antipodal pair of directed hexagons transforms \(a\) into \(b\) in one legal cycle operation. \(\square\)

**Scope.** Both colorings are legal balanced cubes of dimension six; neither is asserted to be bad for NORI1. This is a rigorous barrier to a specific proof strategy: monotone descent toward an arbitrary balanced target under *square-only* directed-cycle flips. The general antipodal directed-cycle reconfiguration theorem remains valid.

**Extension to every even dimension at least six.** Let \(N=2m\ge6\). On \(Q_m\) take the legal coloring \(c_0=x_1,c_1=x_2,c_2=x_0\), and \(c_i=x_0\) for \(3\le i<m\). Let \(a\) be its standard complementary paired lift to \(Q_{2m}\). In the three-face where all bits except original dimensions \(0,1,2\) are zero, the closed word \((2,0,1,2,0,1)\) from the vertex with \(x_0=1\) is a directed hexagon. Recolor that hexagon and its antipodal directed mate to obtain \(b\). It is balanced and odd and differs from \(a\) on twelve edges.

Every original pair of directions from \(\{0,1,2\}\) includes a rule that reads the other bit, so no square using two such directions is directed. All changed edges lie in the selected three-face and its antipodal face, whose fixed exterior bits differ in \(N-3\ge3\) positions. Any other square has at least one exterior direction, intersects either of these three-faces in at most one core edge, and cannot meet both. Thus an antipodal directed-square pair intersects the disagreement set in at most two edges. Flipping any such square pair changes eight edges and increases disagreement from twelve to at least sixteen. This proves the strict monotone-square-descent obstruction in every even dimension \(N\ge6\), while reversing the hexagon pair reaches \(b\) in one step.

**Exponentially extensive trap for square-only descent.** For every even \(N=6+2k\ge8\) there are perfectly balanced antipodally odd colorings \(a,b\) with
\[
\boxed{|\{e:a(e)\ne b(e)\}|=12\cdot2^{2k-1}=6\cdot2^{N-6}}
\tag{HX3}
\]
such that every antipodal directed-square flip of \(a\) increases its edge-disagreement distance to \(b\) by at least four.

*Construction and proof.* Start from the six-dimensional coloring \(a^{(6)}\) in (HX1). Adjoin \(2k\) spectator directions in complementary pairs, with rules
\[
a_{6+2j}(x,y,z)=x_0,\qquad
a_{7+2j}(x,y,z)=1\oplus x_0\quad(0\le j<k).
\]
The old six edge rules ignore the new \(z\)-bits. The enlarged coloring remains legal and balanced because each added pair contributes one edge of each color at every vertex.

Let \(C\) and \(\tau_6 C\) be the two directed hexagons from the six-cube construction, regarded in the \(Q_6\) factor. For each spectator state \(z\in Q_{2k}\) of even Hamming parity, include *both* six-cycles \(C\times\{z\}\) and \(\tau_6 C\times\{z\}\) in a set \(F\). They are directed because the spectator parity is even, and no two cycles share an edge. Since \(2k\) is even, antipodal complementation preserves the parity of the spectator state, and exchanges the two hexagon types; thus \(F\) is antipodally invariant. There are \(2^{2k-1}\) selected states and twelve edges per state, giving (HX3). Flip all edges of \(F\) to obtain \(b\); each flipped directed cycle preserves balance, and antipodal invariance preserves legal oddness.

Every directed square of the original \(Q_6\) coloring intersects \(E(C)\cup E(\tau_6 C)\) in at most one edge, as proved above. Thus a directed square entirely in old directions meets \(F\) in at most one edge, occurring only at an even spectator state. A square using one old and one spectator direction has two old parallel edges at spectator states of opposite parity; at most one lies in \(F\). A square in two spectator directions meets no changed edge. Therefore *every* directed square in the enlarged cube meets \(F\) in at most one edge, and its antipodal partner in at most one additional edge. A paired-square flip toggles eight edges with at most two already disagreeing, so changes distance by \(8-2h\ge4\).

The construction provides strict local minima for the square-flip disagreement potential at exponentially large disagreement distance. It does not imply any of the constructed colorings is bad for NORI1; it is a method obstruction for monotone square-only reconfiguration.

Finite checks for \(N=8,10\) verified both legal balanced colorings and the bound of one disagreement edge per directed square, with disagreement counts \(24\) and \(96\), respectively.
