# Antipodal square rigidity excludes equality in the NORI1 pedestrian bound

- Stable ID: note_pedestrian_square_rigidity_nori1
- Author: independent research session_nori_r4981_1
- Primary home: section:nori_edge_central_carriers
- Labels: proved, approach, stability
- Lifecycle: resolved
- Epistemic status: proved
- Current version: 7
- Retention: current and at most one previous snapshot
- Created session: session_nori_r4981_1
- Updated session: session_nori_r4593_2
- Disposition: Mathematical result preserved as completed background; future use is as evidence or test of a common NORI1/boundary-tournament unification.
- Successor: none

## Related references

- article:nori_article_viii_edges

## Research note

## General equality characterization for the cube-subgraph geodesic bound
Let G be any spanning subgraph of Q_n with integer average degree d, and write L(G) for the greatest length of a geodesic (a path using no cube direction twice) contained in G. Then

**L(G)=d if and only if every connected component of G is an axis-aligned d-dimensional subcube.**

Indeed, the pedestrian dimension sweep gives L(G)>=d. If L(G)=d, every pedestrian in every coordinate order takes precisely d steps because the mean is d. Comparing the two possible last-coordinate orders on an arbitrary square forces the square-completion law: whenever two perpendicular edges incident at one square corner belong to G, the entire square belongs to G. Thus the set of incident edge-directions is invariant along every G-edge; each connected component is precisely the coordinate subcube spanned by its incident directions. A pedestrian within such a component takes one move in each of those directions, so its dimension equals d. Conversely, a union of coordinate d-subcubes has average degree d and contains no geodesic longer than d.

This characterization holds without antipodal symmetry. For n=2d, the NORI1 corollary below follows because antipodal oddness forbids precisely these equality configurations. It identifies **all** equality cases of the average-degree geodesic theorem and suggests a quantitative stability question.

## Theorem (strict even-dimensional pedestrian bound)
Let n=2m>=2. Color the valid undirected underlying edges of Q_n by c_i(x) in {0,1}, with c_i(x+e_i)=c_i(x) and c_i(bar x)=1-c_i(x). Then there exists a monochromatic coordinate-distinct geodesic of length at least m+1. Together with integer rounding of the ordinary pedestrian-averaging bound for odd n, this yields length at least floor(n/2)+1 for every n>=2.

## Proof
Examine the zero-edge subgraph G. Antipodal oddness pairs each underlying direction-i zero edge with a one edge, so G has precisely half the edges of Q_n and average degree m. For any prescribed order of the n coordinate directions, put one labelled pedestrian at each cube vertex, and sweep the directions in that order, swapping pedestrians across all zero edges in the current direction. Every pedestrian follows a valid zero monochromatic geodesic (each direction is swept once), and the sum of all their move counts is 2|E(G)|=m2^n.

Assume all zero geodesics have length at most m. For every coordinate order, then, all 2^n pedestrians move precisely m times.

Fix a underlying square with directions i,j and lower corner v. Suppose its i-edge from v and j-edge from v are both zero. Sweep all directions except i,j first. Since these swaps are bijections, one pedestrian is at vertex v+e_i immediately before the final two sweeps. If the final order is (i,j), this pedestrian takes two moves, first v+e_i -> v, then v -> v+e_j. If the final order is (j,i), it must likewise take two moves: the previous sweeps and this pedestrian's preceding move count are unchanged, while every complete sweep gives count m. Thus the j-edge at v+e_i and the i-edge at v+e_i+e_j are both zero. Therefore **any two adjacent zero edges in a underlying square force the other two zero edges**.

Let D(x) be the set of directions of zero edges incident at vertex x. The completed-square property implies that D(x)=D(x+e_i) whenever i in D(x). It follows that each zero-edge connected component is precisely an axis-aligned coordinate subcube, with its free direction set D constant across that component. A pedestrian starting in a component with d free directions moves precisely once in each of those d directions under any full sweep, hence d=m. In particular, the zero-edge components partition Q_n into m-dimensional subcubes.

Choose one such component C with free-coordinate set I, |I|=m, and put J=[n]\I. In the antipodal image bar C, all I-direction edges are one-colored. Every vertex y in bar C therefore has D(y) subset J, and |D(y)|=m=|J| forces D(y)=J. As y varies over bar C, its I-coordinate vector runs through every possibility. The corresponding zero-edge J-subcube components, one for each I-coordinate vector, are disjoint and cover all Q_n. Consequently every J-direction edge of Q_n is zero-colored everywhere. Since J is nonempty, this contradicts antipodal oddness. So a zero geodesic of length m+1 exists. QED.

## Mathematical implication and limitations
The standard averaging estimate length >=n/2 is not sharp for any legal even-dimensional NORI1 coloring. More significantly, a putative equality case would require a cube tiling by equal-dimensional monochromatic subcubes; antipodal complementarity excludes it. This is a local-to-global rigidity mechanism tied to realized square incidence and underlying edges.

The improvement is only one edge, so it does not make substantial headway toward the full length-n NORI1 conjecture. A consequential next step would be a **quantitative stability theorem**: if every zero geodesic had length at most n/2+t, prove that many squares must violate local closure, and exploit antipodal oddness to derive a lower bound on t growing with n. No such quantitative theorem is claimed here. The argument does not apply directly to ordinary boundary 3-tournaments, whose transitions are ordered triples rather than undirected underlying edges.

Independent proof in research session session_nori_r4981_1. Related established ingredient: Toolkit pedestrian_dimension_sweep_lemma_for_cube_subgraphs.

precise two-color equality theorem: if n=2m and neither color contains an (m+1)-edge geodesic, each color class has average degree m and attains equality in the pedestrian bound. The existing equality-rigidity lemma implies that every underlying square with two incident edges of one color is entirely that color. Hence every square is monochromatic or alternates colors, so every pair of opposite sides has the same color. All edges in a fixed coordinate direction therefore share a color. precisely m directions have each color. Conversely every balanced direction-constant coloring attains L=m. This classifies all extremal two-colorings in even dimension; antipodal oddness excludes the extremizers and forces a geodesic of length m+1 in EACH color.


## Editorial disposition: single unified goal

Complete NORI1-only toy lemma. Retain precise square rigidity and pedestrian geodesic proofs as mathematical background; quantitative stability is a promising NORI1 laboratory for a common underlying-witness rigidity principle. Its potential impact on original-vertex-simple ordered-triple paths provides a natural test of any proposed shared mechanism.
