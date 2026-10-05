# Introduction

## Cold composition

Let \(H\) be a finite linear \(3\)-graph. For an edge \(e\) and a vertex \(v\in e\), let \(\phi(e,v)\) be the maximum length of a linear path with last edge \(e\) and last vertex \(v\). Put
\[
\phi(e)=\max_{v\in e}\phi(e,v),
\qquad
\phi(v)=\max_{e\ni v}\phi(e,v).
\]
An edge \(e\) is **special** if \(\phi(e,v)=\phi(e)\) for every \(v\in e\). If \(e\) is nonspecial, then all longest paths with last edge \(e\) have the same entrance label; this vertex is the **unique entrance** of \(e\), and the other two vertices are terminal at \(e\). A nonspecial edge \(e\) with unique entrance \(x\) is **ascending** if
\[
\phi(x)=\phi(e)-1.
\]

For a vertex \(v\), let \(T(v)\) be the set of ascending edges at which \(v\) is terminal, and put \(t(v)=|T(v)|\). Write
\[
S=\sum_{v\in V(H)}\phi(v)
\]
and let \(n_+\) be the number of nonisolated vertices.

## Metadata

- ID: snake_accounting_and_the_4348_equality_problem_introduction
- Kind: section
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
- Composition version: 1
- Composition stale: False

## Development tree

- [Subsection 1 — (untitled)](../SUBSECTIONS/snake_accounting_and_the_4348_equality_problem_introduction_subsection_a.md) (`snake_accounting_and_the_4348_equality_problem_introduction_subsection_a`; development v1; composition vNone; stale=False)
