# Pedestrian dimension-sweep lemma for cube subgraphs

**Summary:** Put one pedestrian at every vertex and activate edge-permutations one at a time. In an undirected subgraph of Q_n, coordinate-matching swaps give a geodesic of length at least the average degree. In a directed graph with an arc decomposition into directed cycles, cycle rotations give a directed walk of length at least the average outdegree, though the walk need not be geodesic.

## Statement

The pedestrian averaging mechanism has two forms. For an undirected cube subgraph, sweeping coordinate matchings produces a geodesic of length at least the average degree. More generally, for a directed graph whose arc set is partitioned into directed cycles, successively rotating pedestrians around those cycles produces a directed walk of length at least the average outdegree, but without any geodesic guarantee.

## Body

## Undirected cube form

Let \(G=(U,E)\) be any undirected subgraph of the Boolean cube \(Q_n\), with isolated vertices allowed, and let
\[
d=\frac{2|E|}{|U|}
\]
be its average degree.

Fix an arbitrary ordering of the \(n\) cube dimensions. Place one pedestrian at every vertex of \(U\). Process the dimensions in the chosen order. When dimension \(i\) is called, simultaneously swap the pedestrians across every edge of \(G\) in dimension \(i\).

This is well defined because the edges of any fixed cube dimension form a matching.

After all dimensions have been called:

1. every edge of \(G\) has been activated exactly once;
2. each activated edge is crossed by the two pedestrians occupying its endpoints, one in each direction;
3. every pedestrian's walk is a geodesic in \(Q_n\), entirely contained in \(G\);
4. the sum of all pedestrian walk lengths is \(2|E|\).

Indeed, every dimension is called only once, so a fixed pedestrian crosses at most one edge in each cube dimension. Thus no coordinate is flipped twice along that pedestrian's walk. Any cube walk using pairwise distinct coordinate directions is a geodesic. Since the total pedestrian length is \(2|E|\), the mean walk length is
\[
\frac{2|E|}{|U|}=d,
\]
and some pedestrian therefore walks a geodesic of length at least \(d\).

## Monochromatic corollary

For an undirected red-blue edge-coloring of \(Q_n\), regard each color class as a spanning subgraph. If their average degrees are \(d_R,d_B\), then \(d_R+d_B=n\). Hence one color contains a monochromatic geodesic of length at least
\[
\max(d_R,d_B)\ge n/2.
\]

If opposite cube edges are paired antipodally and receive opposite colors, the two color classes have equal size, so \(d_R=d_B=n/2\). Then each color contains a monochromatic geodesic of length at least \(n/2\).

## Directed cycle-decomposition variation

The averaging mechanism is not intrinsically undirected. Let \(D=(U,A)\) be a finite directed graph whose arc set is partitioned into directed cycles
\[
A=A(C_1)\sqcup\cdots\sqcup A(C_t).
\]
Place one pedestrian at every vertex. Declare the cycles in any order. When a directed cycle \(C\) is declared, every pedestrian currently on a vertex of \(C\) traverses the outgoing arc of \(C\) from that vertex. Equivalently, the pedestrians on \(C\) are cyclically rotated by one step.

Each cycle declaration is a permutation of the pedestrians on its vertices, so after every declaration there is still exactly one pedestrian at every vertex. Every arc is traversed exactly once because the cycles partition the arc set. Consequently the sum of all pedestrian walk lengths is \(|A|\), and the average pedestrian walk length is
\[
\frac{|A|}{|U|},
\]
the average outdegree (equivalently, the average indegree). Therefore some pedestrian follows a directed walk of length at least \(|A|/|U|\).

For a directed cube subgraph this does not retain the crucial geodesic conclusion of the coordinate sweep. Different declared cycles may send the same pedestrian through the same coordinate more than once, or even return it to a previously visited vertex. Thus the cycle version preserves the permutation/counting argument but generally produces only a long directed walk, not a geodesic.

A directed cycle decomposition exists in particular for balanced/Eulerian directed edge sets, so this variant may still be useful when such a decomposition arises naturally.

## NOR relevance

The useful abstraction is a pedestrian averaging principle driven by successive local permutations of the vertex occupants. Coordinate matchings are especially strong because their activation schedule certifies that each pedestrian uses every cube coordinate at most once, upgrading the averaged walk to a geodesic. Directed cycle rotations preserve the same occupancy and averaging mechanism, but lose that coordinate monotonicity.

This does not by itself solve the antipodal or spanning NOR problems, but it separates two ingredients that may be reusable independently: (i) permutation-preserving traversal schedules give an exact global averaging identity, and (ii) a no-repeated-coordinate schedule upgrades the resulting walks to cube geodesics.

## Metadata

- ID: pedestrian_dimension_sweep_lemma_for_cube_subgraphs
- Kind: toolkit
- Version: 2
- Math version: 2
- Audit: unaudited
- Refutation: unrefuted
