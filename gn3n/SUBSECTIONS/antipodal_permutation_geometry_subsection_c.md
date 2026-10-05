# Triple colors as antipodal local data

## Metadata

- ID: antipodal_permutation_geometry_subsection_c
- Parent Section: antipodal_permutation_geometry
- Position: 3
- Row version: 3
- Development version: 3
- Composition version: None
- Composition stale: True

## Cold composition

(none yet)

## Development

Write
\[
h(u,v,w)=
\begin{cases}
1,&(u,v,w)\text{ is tight},\\
0,&(u,v,w)\text{ is non-tight}.
\end{cases}
\]
Boundary reversal is
\[
h(w,v,u)=1-h(u,v,w).
\]
For \(\pi=(v_1,\ldots,v_n)\), the consecutive-triple word is
\[
h(v_1,v_2,v_3),\ldots,h(v_{n-2},v_{n-1},v_n).
\]

The color at a triple of successive directions \(u,v,w\) belongs naturally to the tetrahedral face
\[
S,\quad S\cup\{u\},\quad S\cup\{u,v\},\quad S\cup\{u,v,w\}
\]
of the staircase triangulation and is independent of the base subset \(S\). Complementation reverses the successive directions to \(w,v,u\) and therefore complements the color.

This is the precise common structure with antipodal cube-coloring problems such as the Norine line of ideas: geodesics are permutations, opposite geodesics are reversals, and the local datum flips under the antipode. The important difference is that our color is attached to three consecutive directions, not directly to an ordinary cube edge. Any imported antipodal-path theorem must therefore survive this memory requirement rather than silently forgetting it.
