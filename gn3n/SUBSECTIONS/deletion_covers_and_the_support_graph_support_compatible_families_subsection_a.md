# deletion_covers_and_the_support_graph_support_compatible_families_subsection_a

## Metadata

- ID: deletion_covers_and_the_support_graph_support_compatible_families_subsection_a
- Parent Section: deletion_covers_and_the_support_graph_support_compatible_families
- Position: 1
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: True

## Cold composition

(none yet)

## Development

A large support-compatible family has only one varying support.

**Lemma 6 (localization).** Let \(D\subseteq V(H)\), \(|D|\ge3\), and suppose \(\{F_d:d\in D\}\) is pairwise support-compatible. Then there are disjoint sets \(X,Q\) with \(V(H)=X\cup Q\), \(D\subseteq X\), such that
\[
F_d=(X-\{d\})\mid Q
\]
for every \(d\in D\). The set \(Q\) is Hamiltonian, every \(X-\{d\}\) is Hamiltonian, and \(X\) is not Hamiltonian.

**Proof.** For two vertices \(u,v\), choose \(d\in D-\{u,v\}\) and declare \(u\sim v\) when they lie in the same path of \(F_d\). Support compatibility makes the definition independent of \(d\). Transitivity follows by viewing any three vertices in one deletion cover; when the three vertices themselves exhaust \(D\), any vertex outside \(D\) supplies the same comparison. Thus \(\sim\) has two equivalence classes, say \(X,Q\).

The deletion labels cannot occupy both classes. If \(a\in D\cap X\) and \(b\in D\cap Q\), then one selected cover Hamiltonizes \(X\) and another Hamiltonizes \(Q\), giving a two-cover of \(H\). Hence \(D\subseteq X\) after relabeling. The asserted support partitions follow. If \(X\) were Hamiltonian, its Hamilton path together with a Hamilton path on \(Q\) would be a two-cover of \(H\). \(\square\)

The following endpoint comparison will be used repeatedly.

**Lemma 7 (endpoint comparison).** Suppose \(H-x=P\mid Q\) is a deletion cover and \(y\) is an endpoint of the displayed path \(Q\). Let \(G_y\) be a deletion cover at \(y\) that is support-incompatible with \(P\mid Q\) on \(H-\{x,y\}\). Put \(B=Q-\{y\}\). Then \(G_y\) has at least two edges joining distinct classes of
\[
P\mid B\mid\{x\}.
\]
If it has exactly two such edges and none joins \(P\) to \(B\), then \(B\cup\{x\}\) is Hamiltonian.

**Proof.** If there were only one edge joining distinct classes, deleting it from the two paths of \(G_y\) would leave three path blocks. The support partition would be one of
\[
(P\cup B)\mid\{x\},\qquad (P\cup\{x\})\mid B,\qquad P\mid(B\cup\{x\}).
\]
The first gives a two-cover of \(H\) after adjoining the two-vertex path \((x,y)\); the second would make \(P\cup\{x\}\) Hamiltonian and hence give \((P\cup\{x\})\mid Q\); the third is support-compatible with \(P\mid Q\) after deleting \(x\). All are impossible.

Assume there are exactly two interclass edges and neither joins \(P\) to \(B\). Both are incident with \(x\). Cutting them produces four blocks, so precisely one of \(P,B\) is split into two blocks. If \(B\) is split, \(x\) cannot be adjacent in the contracted two-path forest to the unique \(P\)-block, since that would make \(P\cup\{x\}\) Hamiltonian. Hence \(x\) joins the two \(B\)-blocks, making \(B\cup\{x\}\) Hamiltonian. If \(P\) is split, \(x\) cannot join both \(P\)-blocks for the same reason, so it joins the unique \(B\)-block and one \(P\)-block; again \(B\cup\{x\}\) is a tight path. \(\square\)

Applying the lemma at both endpoints of \(Q\) requires one additional case. Put \(Q=(q_0,\ldots ,q_m)\). If neither endpoint deletion cover contains an edge joining a surviving vertex of \(P\) to a surviving vertex of \(Q\), then both endpoint replacements of \(Q\) by \(x\) are Hamiltonian. If either replacement Hamilton path changes the inherited order of the surviving vertices of \(Q\), there is an order disagreement. Otherwise the insertion position of \(x\) in \((Q-\{q_0\})\cup\{x\}\) is either before \(q_1\) or between \(q_1,q_2\), since any later position permits \(q_0\) to be prepended and would make \(Q\cup\{x\}\) Hamiltonian. Symmetrically, the insertion position in \((Q-\{q_m\})\cup\{x\}\) is either after \(q_{m-1}\) or between \(q_{m-2},q_{m-1}\).

An adjacent insertion forces a displayed reversal. If the left replacement begins \((q_1,x,q_2,\ldots)\), then \((q_0,q_1,x)\) must be non-tight, and hence \((x,q_1,q_0)\) is tight. If the right replacement ends \((\ldots,q_{m-2},x,q_{m-1})\), then \((x,q_{m-1},q_m)\) must be non-tight, and hence \((q_m,q_{m-1},x)\) is tight.

The only remaining order-preserving case has replacement orders
\[
(x,q_1,\ldots ,q_m),\qquad (q_0,\ldots ,q_{m-1},x).
\]
Together with \(Q\), these give three deletion covers sharing the fixed support \(P\). Their singleton lifts form a triangle of equal-potential pairwise repartitions, and the two endpoint-replacement paths have an order disagreement on the common support \(\{x,q_1,\ldots ,q_{m-1}\}\). Thus opposite extreme insertion is a concrete recurrence configuration, not a Hamiltonian insertion of \(x\) into all of \(Q\). See [[leaf_endpoint_singleton_triangle01]].
