# A three-way local alternative

## Cold composition

Fix \(v\), put \(p=\phi(v)\), and let \(F\subseteq H_v\) contain \(k\) edges that meet the chosen maximum \(p\)-edge path \(P\) in exactly one off-\(v\) vertex.

Separate \(F\) into \(U\) and \(X\), where an edge belongs to \(U\) if that intersection is its opposite terminal and belongs to \(X\) if that intersection is its unique entrance.

For \(e\in X\), let \(a(e)\) be the first edge of \(P\) containing its unique entrance and put
\[
\sigma(e)=\phi(x_e)-a(e).
\]
The path-splice recurrence for ordered entrance intersections gives, for every integer \(s\ge0\),
\[
k
\le
|U|+
|\{e\in X:\sigma(e)>s\}|+
4s+O(\log p). \tag{38}
\]

Take \(s=\lfloor k/16\rfloor\). If \(|U|\ge k/2\), at least half of the family meets \(P\) at its opposite terminal. Otherwise
\[
|\{e\in X:\sigma(e)>s\}|
\ge
k/4-O(\log p). \tag{39}
\]
Linearity places these edges in at least
\[
k/8-O(\log p)
\]
distinct interior pairs. By Lemma 8, at least half of those pairs either are doubly occupied and therefore determine a \(3\)-edge linear cycle, or have a distinct output edge contained in \(V_{\ge p}\).

We have proved:

## Theorem 10

Outside a set of vertices of total vertex rank \(o(S)\), every high-rank vertex \(v\) has a family \(H_v\) satisfying Lemma 9 and at least one of the following:

1. at least
   \[
   (1/16-o(1))\phi(v)
   \]
   members meet the chosen maximum path at their opposite terminal;
2. at least
   \[
   (1/128-o(1))\phi(v)
   \]
   distinct \(3\)-edge linear cycles arise from doubly occupied interior pairs;
3. at least
   \[
   (1/128-o(1))\phi(v)
   \]
   distinct path edges lie entirely in
   \[
   V_{\ge\phi(v)}.
   \]

Partitioning the vertices according to one alternative shows that one of the three alternatives has total vertex-indexed multiplicity \(\Omega(S)\).

## Metadata

- ID: snake_accounting_and_the_4348_equality_problem_a_three_way_local_alternative
- Kind: section
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
- Composition version: 1
- Composition stale: False

## Development tree

- [Subsection 1 — (untitled)](../SUBSECTIONS/snake_accounting_and_the_4348_equality_problem_a_three_way_local_alternative_subsection_a.md) (`snake_accounting_and_the_4348_equality_problem_a_three_way_local_alternative_subsection_a`; development v1; composition v1; stale=False)
- [Subsection 2 — Theorem 10](../SUBSECTIONS/snake_accounting_and_the_4348_equality_problem_a_three_way_local_alternative_subsection_b.md) (`snake_accounting_and_the_4348_equality_problem_a_three_way_local_alternative_subsection_b`; development v1; composition vNone; stale=False)
