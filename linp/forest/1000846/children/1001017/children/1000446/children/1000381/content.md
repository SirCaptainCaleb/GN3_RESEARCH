# Source-oriented triples force a 7/27-scale directed-or-rainbow path

## Statement

In the source-oriented setup on n vertices, assume every vertex lies in at least m/n triples. Then the associated properly edge-colored graph H contains a rainbow path of length q with
q > 7m/(27n) - 14/9.
Consequently the maximum of the longest directed path in the forced digraph D and the longest rainbow path in H exceeds the same bound.

## Body

Every triple contributes exactly one edge to H and distinct triples contribute distinct edges, so |E(H)|=|F|. By incidence counting and the minimum triple-degree hypothesis,
3|F|=Σ_x d_F(x)≥m,
hence |E(H)|≥m/3.

Let q be the maximum rainbow-path length in H. Then H contains no rainbow P_{q+1}. The certified Ergemlidze–Győri–Methuku rainbow path Turán bound e4fb292edb26 gives
|E(H)| < (9q/7+2)n.
Combining with |E(H)|≥m/3 gives
m/3 < (9q/7+2)n,
so
q > (7/9)(m/(3n)-2)
  = 7m/(27n)-14/9.

A rainbow path of that length already supplies one of the two desired outcomes, so the same lower bound holds for max{L_D,L_R}.
