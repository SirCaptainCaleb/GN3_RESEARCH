# One exterior label fills a four-cycle only by mutual adjacency to every boundary label — preserved pre-item development

## Development

## Terminal-pair homotopy is natural under prefix enlargement

Suppose B subset B', E' restricts to E on B, and embed P(B) in the face consisting of a fixed ordered prefix on B'-B followed by the free block B. This embeds C_E in C_{E'}.

The homotopy equivalences of [[terminal_ordered_pair_loci_have_the_homotopy_type_of_mutual_pair_clique_complexes]] identify this inclusion, up to homotopy, with the inclusion of the mutual-pair clique complex K(G_E) in K(G_{E'}).

**Proof.** In the cover used in that theorem, each old terminal-label cap C_v maps into the new cap C'_v. Each old suffix-clique face Q_T maps into Q'_T because the added fixed prefix precedes T. Thus the inclusion respects covers with the same old index labels. Their nerves are the order complexes of nonempty mutual cliques, and the nerve map is precisely the inclusion of these clique posets.

For completeness, the nerve argument is natural here: form the incidence space of pairs (x,t), where t is a point of the nerve and x belongs to every cover set indexed by the support of t. Its projections to the covered complex and the nerve are homotopy equivalences for these finite subcomplex covers with contractible nonempty intersections. The cover-respecting inclusion induces an inclusion of incidence spaces, and both projection squares commute. The resulting homotopy-equivalence zigzags identify the induced inclusion maps. ∎

## One added label must cover the whole four-cycle

Let E on B={a,b,c,d} have mutual graph the chordless cycle a-b-c-d-a. Let B'=B union {g}, and let E' restrict to E. Write N for the old labels mutually adjacent to g in the enlarged mutual graph.

**Theorem.** If N is a proper subset of B, the inclusion
\[
C_E\longrightarrow C_{E'}
\]
induces a nonzero map on first homology; in particular it is not null-homotopic. If N=B, C_{E'} is contractible and the inclusion is null-homotopic.

**Proof.** If g is not an active terminal label, the mutual graph is unchanged. If g is active but N is empty, its clique complex adds only an isolated vertex. Both cases leave the original circle untouched.

Otherwise the enlarged clique complex is
\[
K(C_4)\ \cup\ \bigl(g*K(C_4[N])\bigr).
\]
For a proper subset N, the induced subgraph C_4[N] is a forest, so its clique complex has zero first homology. The Mayer–Vietoris sequence shows that the inclusion from the original circle into the union is injective on H_1: the map preceding H_1(K(C_4)) has zero domain. This remains true when the intersection is disconnected. Hence the generator survives. Naturality above transfers this conclusion to the pair loci.

If N=B, the enlarged clique complex is a cone on the cycle, and the terminal-pair classification gives a contractible locus. ∎

Thus the two-direction admissibility condition in [[a_mutually_admissible_exterior_vertex_fills_the_terminal_pair_carrier]] is not merely a convenient sufficient condition for this obstruction. With one added vertex and the old terminal relation unchanged, mutual adjacency to all four labels is necessary to fill the forced cycle.

A one-sided successful-buffer relation gives no mutual edge by itself and may leave the entire original homotopy type unchanged. This distinguishes an outward chamber from a coherent carrier containing all earlier outward choices.
