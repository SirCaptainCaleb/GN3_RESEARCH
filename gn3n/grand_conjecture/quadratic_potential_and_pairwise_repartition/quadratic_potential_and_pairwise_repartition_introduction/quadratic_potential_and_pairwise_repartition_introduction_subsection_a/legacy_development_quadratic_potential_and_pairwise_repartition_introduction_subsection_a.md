#  — preserved pre-item development

## Development

Let \(H\) be a minimum counterexample to \(\operatorname{pc}(H)\le2\). For each \(x\in V(H)\), choose a deletion cover
\[
H-x=P\mid Q.
\]
The singleton lift \(P\mid Q\mid\{x\}\) is a three-cover of \(H\).

Let \(\mathcal R(H)\) be the graph whose vertices are three-covers of \(H\). Two three-covers are adjacent when one is obtained from the other by a pairwise repartition: two displayed paths are replaced by a two-cover of their union and the third path is unchanged. Since \(H\) has no two-cover, every such repartition again has three nonempty paths.

For a three-cover \(C=P_1\mid P_2\mid P_3\), define
\[
\Phi(C)=|P_1|^2+|P_2|^2+|P_3|^2.
\]
Fix a connected component of \(\mathcal R(H)\) containing a singleton lift and choose \(C\) in that component with minimum \(\Phi\).
