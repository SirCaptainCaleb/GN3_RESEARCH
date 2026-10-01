# A disturbance-free forest transversal is a union of support paths of length at most five

## Statement

Let H be a minimum counterexample in the sharp half-order shell n=2lambda+1, and choose one lambda|lambda deletion cover for each omitted vertex, forming the selected support graph J of ff3284e79394. Choose one Hamilton order on every support vertex of J. Suppose J is a forest and no length-two walk inside J exposes inherited three-part crossing or relative-order disagreement in the sense of astra004twowalk. Then every connected component of J is a path with at most five edges. Consequently J has at least ceil(n/5) connected components and at least 2ceil(n/5) leaf supports.

## Body

Because J is a transversal with one selected edge for each ground vertex, all edge labels of J are pairwise distinct.

First suppose some support S has degree at least three in J. Choose any three distinct incident neighbors. The certified degree-three star lemma 1ab58c346404 says that, for the chosen Hamilton orders, one of the three length-two walks through S exposes inherited three-part crossing or relative-order disagreement. This contradicts the hypothesis. Hence Delta(J)<=2.

Since J is a forest with maximum degree at most two, every connected component is a path.

Now suppose one path component contains at least six edges. Take six consecutive edges to obtain a simple support path
S_0-S_1-...-S_6.
Apply astra004sixcorridor. Its repeated-label alternative is impossible because the six selected edges have distinct omitted-vertex labels. Therefore one of the three jump-two subwalks exposes inherited three-part crossing or relative-order disagreement, again contradicting the hypothesis.

Thus every component has at most five edges. J has exactly n selected edges in total, so at least ceil(n/5) path components are needed. Every nontrivial path component has two leaves. Since every component contains at least one edge—isolated support vertices are not vertices of the selected edge graph—J has at least 2ceil(n/5) leaf supports. ∎
