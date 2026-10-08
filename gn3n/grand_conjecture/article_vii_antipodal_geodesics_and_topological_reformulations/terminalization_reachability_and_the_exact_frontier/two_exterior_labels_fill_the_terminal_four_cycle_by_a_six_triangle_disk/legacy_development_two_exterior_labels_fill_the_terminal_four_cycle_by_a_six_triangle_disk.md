# Two exterior labels fill the terminal four-cycle by a six-triangle disk — preserved pre-item development

## Composition

(none yet)

## Development

## Two exterior labels fill the four-cycle without a universal label

Let B={a,b,c,d}, with mutual-pair graph exactly the chordless cycle a-b-c-d-a. Add two distinct labels g,h. Suppose the enlarged directed relation E^+ restricts to the original relation on B and its mutual graph has the following edges:
\[
ga,gb,gc,\qquad ha,hc,hd,\qquad gh,
\]
in addition to the four cycle edges. No requirement is imposed on the remaining two possible mutual edges gd and hb.

**Theorem.** The enlarged terminal-pair locus C_{E^+} is contractible. Hence it contains the original C_E in a fixed-prefix face {g}|{h}|B and fills its forced circle, together with every other relative extension problem into that pair carrier.

**Proof.** If gd is also present, g is adjacent to every other vertex, so the clique complex is a cone. If hb is present, h is universal and the same conclusion holds.

Otherwise its maximal simplices are exactly the following six triangles:
\[
gab,\quad gbc,\quad gha,\quad ghc,\quad had,\quad hdc.
\]
Here a string denotes its unordered vertex set. The two central triangles gha and ghc form a disk with boundary a-g-c-h-a. Attach the triangle gab along boundary edge ag, then gbc along the adjacent boundary path b-g-c. Their union replaces boundary path a-g-c by a-b-c and remains a disk. Attach had along boundary edge ah, then hdc along boundary path d-h-c; this replaces a-h-c by a-d-c. The resulting simplicial complex is a disk with boundary precisely a-b-c-d-a. These are all cliques: the missing edges ac,bd,gd,hb rule out every tetrahedron and every other triangle. Thus the entire clique complex is contractible.

The terminal-pair homotopy theorem gives contractibility of C_{E^+}. The prefix embedding preserves the old terminal pair and hence embeds C_E. Any contraction of the enlarged locus fills its inclusion and all sphere maps into it. ∎

In the two boundary-path attachment steps above, the second attached triangle meets the existing disk in two consecutive boundary edges; their union is an interval, so the union is still a triangulated disk. This supplies the topological verification rather than only an Euler-characteristic count.

## Translation into boundary-tournament tests

For a terminal-pair absence test E(u,v) equivalent to h(u,v,z)=1, the required mutual edges are the explicit pairs of tests
\[
h(u,g,z)=h(g,u,z)=1\quad(u=a,b,c),
\]
\[
h(u,h,z)=h(h,u,z)=1\quad(u=a,c,d),
\]
and
\[
h(g,h,z)=h(h,g,z)=1.
\]
If the next two determining statuses are 1,1, require also h(g,z,z_1)=h(h,z,z_1)=1. The remaining inward determining statuses must retain their protected values, and the reflected selected-depth test must be absent, as in [[a_mutually_admissible_exterior_vertex_fills_the_terminal_pair_carrier]].

When two exterior singleton positions immediately precede B, merge them and B into one ambient block while keeping the determining slots at its final two positions. Under the stated protection tests, the ambient outward locus is the contractible C_{E^+}, times neutral factors. It contains the entire original outward locus, not just selected repaired chambers.

The single-label necessity theorem [[one_exterior_label_fills_a_four_cycle_only_by_mutual_adjacency_to_every_boundary_label]] shows why this two-label construction is useful: neither g nor h is universal in the six-triangle case, yet together they fill the circle. The construction relaxes the one-label requirements in a precise way.

## Scope

This proves a concrete enlarged protected-carrier mechanism on at most six reservoir labels. It does not prove that the grand-conjecture hypotheses force such labels, nor that independently selected ambient blocks are nested on neighboring separator faces. Those are the remaining forcing and compatibility obligations. The point of the lemma is to give the loop-filling step explicit boundary-triple hypotheses and an explicit finite disk.
