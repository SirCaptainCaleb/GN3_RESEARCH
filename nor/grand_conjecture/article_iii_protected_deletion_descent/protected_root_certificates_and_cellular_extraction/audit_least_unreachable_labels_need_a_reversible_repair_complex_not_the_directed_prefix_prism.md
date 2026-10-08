# Audit: least-unreachable labels need a reversible repair complex, not the directed prefix prism

## Composition

(none yet)

## Development

## Audit: least-unreachable labels need a reversible repair complex, not the directed prefix prism

The Hartman-style least-unreachable idea is promising only after one distinguishes two different notions of reachability.

The exact NOR automaton of the toolkit theorem “One-change NOR is reachability in a two-layer flag prism” is a **directed prefix automaton**. A legal edge appends one unused coordinate and strictly increases support rank.

Hence the automaton is acyclic.

Suppose \(z\to z'\) is an allowed same-phase/same-color edge. Let
\[
T(z)
\]
denote the set of boundary targets reachable *from* \(z\) by directed legal paths. Then
\[
T(z')\subseteq T(z),
\]
because every path from \(z'\) can be prefixed by \(z\to z'\).

Equality need not hold. In particular, two adjacent states of the same ternary color need not have the same least unreachable target.

Likewise, if
\[
R
\]
denotes states reachable *from the global source*, an edge \(z\to z'\) gives only
\[
z\in R\Longrightarrow z'\in R.
\]
It does not make \(z,z'\) equivalent.

Therefore the key Hartman component-invariance step
\[
L(z)=L(z')
\]
for same-color adjacent states is not available on the directed prefix prism.

### Corrected target

A least-unreachable Sperner labeling must instead be built on a **reversible state graph** whose edges are audited full-order repairs/exchanges and whose connected components preserve the intended boundary target data.

Candidates are:

- the flat-repair graph before a protected-root exit;
- a witness-exchange graph with outside collars fixed;
- a same-cut protected \(K_{2,2}\) cell complex.

On such a graph, ordinary undirected component membership can make reachable-target sets constant on components, restoring the Hartman mechanism.

### Consequence

The directed two-layer flag prism remains an exact formulation of NOR, but by itself it does not supply the component invariance required for the proposed least-unreachable labeling.

Any future Hartman-style proof must first exhibit a reversible repair complex and prove the relevant boundary-face reachability inside that complex.
