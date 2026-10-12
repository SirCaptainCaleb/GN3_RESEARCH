## Boundary Tournaments

boundary 3-tournament: A function b on ordered triples of distinct vertices with b(c,b,a)=1−b(a,b,c).
  Note: No global ordering of graph edges is required.

comparison digraph: The digraph on unordered pairs of a boundary 3-tournament's vertices with an arc {a,b}→{b,c} when a,b,c are distinct and b(a,b,c)=1.

direction-only coloring: An ordered-three-face coloring c(F,(a,b,c))=b(a,b,c), independent of the face's fixed coordinates.

edge-orderable boundary tournament: A boundary 3-tournament b for which a strict total order < of unordered vertex pairs satisfies b(a,b,c)=1 if and only if {a,b}<{b,c}.
  Note: Equivalent to acyclicity of the comparison digraph.

monochromatic tight path: A sequence of distinct vertices whose consecutive ordered triples have one common value under a binary boundary 3-tournament coloring.

tight path: A sequence (v_1,…,v_m) of distinct vertices such that every consecutive ordered triple is a hyperedge of the specified directed 3-uniform hypergraph.
  Note: Distinctness is in the original vertex set.

## Conjectures

NORI1: The k=1 case of NORI_K: binary colorings of cube edges with c(bar e)=1−c(e). The open NORI1 full-geodesic conjecture asserts that every such coloring of Q_n admits a monochromatic antipodal geodesic.
  Note: The coloring class NORI1 and the conjecture about it are distinct.

NORI2: The k=2 case of NORI_K: binary colorings of ordered two-faces (F,π) satisfying c(bar F,rev π)=1−c(F,π).
  Note: NORI2 designates the class, not any proposed path-length or switch bound.

NORI3: The k=3 instance of NORI_K: binary colorings c(F,π) of three-dimensional faces with ordered free coordinates and c(bar F,rev π)=1−c(F,π).
  Note: NORI3 names this class, not a conjecture. The original universal assertion that some full antipodal geodesic has at most one color change was refuted in Q9. More strongly, some NORI3 colorings have no monochromatic coordinate-distinct geodesic longer than O(log n), by the two-sentinel antichain theorem valid for each fixed k≥3.

## Constructions

sentinel coordinate: A distinguished cube coordinate whose role in the free directions or fixed bits separates cases of a coloring construction.
  Note: Used in the Q9 counterexample.

## Cube Geometry

antipodal face: The face bar F is obtained from a face F by complementing every fixed coordinate; the free-coordinate set is unchanged.

antipodal geodesic: An n-edge path in Q_n from x to its bitwise complement bar x, changing each coordinate once.
  Note: Specify its start vertex and direction order when needed.

antipodal reversal of a geodesic: The map (x_0,…,x_m)↦(bar x_m,…,bar x_0).
  Note: Reverses direction order and complements the face.

color change: A position between adjacent entries of a binary color word at which the values differ.

color word: The sequence of colors of consecutive ordered k-face windows along a directed cube geodesic.
  Note: For an m-edge path, m−k+1 windows exist when m≥k.

corresponding vertices: Vertices x and y in parallel faces of a cube are corresponding if they differ only in coordinates outside the shared free-coordinate set of those faces. Equivalently, their projections onto the shared free-coordinate set are equal.
  Note: Parallel faces have the same set of free-coordinate directions; their fixed-coordinate assignments may differ in several coordinates.

exterior coordinates: The coordinates fixed on a cube face, complementary to its free-coordinate directions.

k-cp: A path is k-cp (color-partitioned) if its edges admit a partition into at most k consecutive subpaths such that every ordered-face window fully contained within each subpath has the same color. Windows crossing a partition boundary are unrestricted. Equivalently, it is a concatenation of at most k monochromatic subpaths. The color word of the whole path may have more than k-1 changes.
  Note: The parameter k counts monochromatic subpaths, not color changes in the full window word. For an edge coloring, a 2-cp has at most one color change. For ordered higher-dimensional face colorings, boundary-crossing windows may contribute additional color changes. Two monochromatic geodesics from antipodal cube vertices to a common vertex always concatenate into a 2-cp antipodal geodesic, regardless of their colors.

k-splice: In an edge-colored cube, a geodesic decomposed into at most k+1 consecutive monochromatic geodesic subpaths. Equivalently, an edge-colored geodesic with at most k switches.
  Note: The concatenation itself must be a geodesic: its constituent direction supports are pairwise disjoint.

k-switch: In an edge-colored cube, a geodesic whose edge-color word has exactly k changes. The phrase at most k switches permits fewer changes.
  Note: Always refers to a geodesic in NORI usage.

long path: A path in a cube face that traverses every free-coordinate direction of that face. A long geodesic traverses every free direction exactly once and joins antipodal vertices of the face.
  Note: Longness is relative to the containing face; a general long path need not be a geodesic.

ordered three-face: A three-dimensional cube face F together with an ordering of its three free directions.
  Note: No traversal corner is distinguished.

ordered-three-face antipodal coloring: A binary function c(F,π) on ordered three-faces with c(bar F,rev π)=1−c(F,π).
  Note: The NORI3 coloring class.

parallel faces: Two cube faces are parallel if the set of coordinate directions spanned by one is a subset (possibly equal) of the set of coordinate directions spanned by the other, in either order. Equivalently, their free-coordinate sets are comparable by inclusion.
  Note: Parallelism includes equal-dimensional faces and faces with nested free-direction sets; the faces need not be nested as vertex sets.

root: The first vertex of a directed cube geodesic.
  Note: Root-dependent assertions must say whether it is prescribed.

## Cube Models

NORI color-change number S_3(n): S_3(n)=max_c min_P #{i:c_i(P)≠c_{i+1}(P)}, where c ranges over NORI3 colorings and P over antipodal geodesics of Q_n.
  Note: A property of the k=3 coloring class.

NORI_K: For 1≤k≤n, the class of binary colorings c(F,π) of pairs comprising a k-dimensional face F of Q_n and an ordering π of its k free coordinate directions, satisfying c(bar F,rev π)=1−c(F,π). A length-n antipodal geodesic has n−k+1 consecutive ordered k-face windows.
  Note: NORI_K names the coloring class, not a conjecture; NORIK is synonymous. The discarded universal 2-cp assertion concerns the k=3 case. For every fixed k≥3 and n≥k+2, the two-sentinel antichain construction supplies a coloring with no monochromatic coordinate-distinct geodesic longer than 3m+3k−4, where m=min{d≥2: binom(d,floor(d/2))≥n−2}=O(log n). Its proof is preserved in the foundational Section of Article I.

NORIK [alias -> NORI_K]: 
  Note: Short spelling of NORI_K.

## Foundations

length-three cube geodesic: An ordered four-vertex path in Q_n crossing three distinct coordinate directions.
  Note: A colored object is four cube vertices, not a triple of coordinate labels.

## Local Geometry

certified edge: A cube edge lying on at least one monochromatic four-edge geodesic for the specified ordered-three-face coloring.

dead edge: A cube edge lying on no monochromatic four-edge geodesic for the specified ordered-three-face coloring.

## Reachability

monochromatic reachability: R(a) denotes all endpoints of monochromatic geodesics rooted at a, in either color, including a. R^x(a) restricts to length x. When a proof requires color i, write R(a;i) or R^x(a;i).

## Terminology

NORI conjecture [alias -> NORI3]: 
  Note: Historical alias for the refuted unrestricted 2-cp assertion concerning NORI3; it is not synonymous with the class NORI3.

NORI odd coloring: Ambiguous historical term for a coloring of directed three-edge windows rather than of ordered cube faces.
  Note: Specify the model.

## Prohibited

actual [prohibited]: 
  Note: Rhetorical modifier in compositions; express the mathematical claim instead.

concrete [prohibited]: 
  Note: Avoid redundant emphasis in mathematical compositions.

exact [prohibited]: 
  Note: Filler modifier in compositions; specify the equation or hypothesis instead.

genuine [prohibited]: 
  Note: Avoid redundant emphasis in mathematical compositions.

literally [prohibited]: 
  Note: Avoid redundant emphasis in mathematical compositions.

physical [prohibited]: 
  Note: Redundant modifier in compositions; name the face, edge, or path in the definition.

really [prohibited]: 
  Note: Avoid redundant emphasis in mathematical compositions.

truly [prohibited]: 
  Note: Avoid redundant emphasis in mathematical compositions.
