# An endpoint-rooted Hamiltonian four-set

## Body

Suppose
\[
W\mid P\mid Q
\]
is a three-cover with \(|W|=4\), and let
\[
P=(p_1,\ldots,p_m),\qquad m\ge2.
\]

**Lemma 7.** There are distinct vertices \(x,y\in W\) such that
\[
\{p_1,p_m,x,y\}
\]
is a Hamiltonian four-set. Its complement is non-Hamiltonian and has path-cover number two.

**Proof.** Choose any three distinct vertices \(a,b,c\in W\). In the five-set
\[
F=\{p_1,p_m,a,b,c\},
\]
apply the endpoint-pair Hamiltonicity theorem with prescribed pair \(\{p_1,p_m\}\). Some Hamiltonian four-subset of \(F\) contains both prescribed vertices, so it has the form
\[
\{p_1,p_m,x,y\}
\]
for distinct \(x,y\in\{a,b,c\}\). The third cover component \(Q\) is nonempty, so this Hamiltonian four-set is proper. Minimum-counterexample calculus therefore gives a two-cover of its complement. \(\square\)

Thus every four-set state beside a nontrivial path already contains a bounded Hamiltonian support carrying both displayed endpoints of that path. No lower bound such as \(m\ge6\), endpoint-extension case split, or finite-order remainder is needed.

### Endpoint deletion exposes a comparison disturbance

The endpoint-rooted four-support interface can be pushed directly into the comparison-cover interfaces.

**Lemma 8.** Let \(H\) be a minimum counterexample. Let
\[
K=(k_0,k_1,k_2,k_3)
\]
be a Hamiltonian four-path and suppose
\[
H-K=A\mid B
\]
is a two-cover. Put
\[
C=(k_1,k_2,k_3),
\]
and let \(F\) be any deletion cover of \(H-k_0\). Relative to the displayed three-cover
\[
C\mid A\mid B
\]
of \(H-k_0\), at least one of the following holds.

1. \(F\) has an ordinary edge joining a vertex of \(A\) to a vertex of \(B\).
2. An inherited displayed path is split into at least two \(F\)-blocks. Consequently either an inherited displayed edge has its endpoints in different paths of \(F\), or one path of \(F\) leaves that displayed path through a nonempty exterior segment and later returns.
3. The order induced by \(F\) on the contiguous \(C\)-block disagrees with the inherited order \((k_1,k_2,k_3)\).
4. A tight triple reverses an end edge either of \(K\) or of the other displayed block meeting \(C\) in \(F\).
5. \(H\) has a two-cover.

The symmetric statement holds after deleting \(k_3\).

**Proof.** Since \(F\) has two path components while
\[
C\mid A\mid B
\]
has three, the component-drop lemma gives at least one ordinary edge of \(F\) whose endpoints lie in different displayed classes.

Suppose first that \(F\) has at least two such interclass edges. Cutting all interclass edges of \(F\) produces
\[
2+t\ge4
\]
nonempty monochromatic blocks, where \(t\) is the number of interclass edges. If no edge joins \(A\) directly to \(B\), outcome 1 is absent. The three displayed classes are nonempty, so at least one of \(C,A,B\) occurs in at least two blocks. Along its inherited displayed path, choose a first ordinary edge whose endpoints lie in different blocks. If those blocks belong to different paths of \(F\), the inherited edge is split between the two comparison paths. If they lie in the same path of \(F\), maximality of the blocks forces a nonempty exterior segment between them. Thus outcome 2 holds.

It remains to suppose that \(F\) has exactly one interclass edge. Cutting it produces exactly three blocks. Since the three displayed classes are nonempty, each of \(C,A,B\) is one contiguous block. One block is an entire component of \(F\), and the other two are concatenated in the other component.

The isolated block cannot be \(C\). Otherwise the other component is a Hamilton path on \(A\cup B=H-K\); replacing the isolated path on \(C\) by the displayed path \(K\) gives a two-cover of \(H\), outcome 5.

Hence \(C\) is concatenated with one of \(A,B\); call the other block \(D\), and call the isolated block \(E\). If the order induced on \(C\) differs from
\[
(k_1,k_2,k_3),
\]
then two common vertices occur in opposite relative order and outcome 3 holds. Assume therefore that the \(C\)-block has exactly the inherited order.

If the mixed component has order
\[
C\,D,
\]
prepend \(k_0\). Every consecutive triple is then either inherited from \(K\), inherited from the old mixed component, or wholly inside \(D\). Hence \(K\cup D\) is Hamiltonian, and together with \(E\) gives outcome 5.

Thus the only remaining orientation of the mixed component is
\[
D\,C.
\]
Write its final \(D\)-block as
\[
(d_1,\ldots,d_t),
\]
so the comparison path ends
\[
(d_1,\ldots,d_t,k_1,k_2,k_3).
\]
Insert \(k_0\) between \(d_t\) and \(k_1\). If all newly created consecutive triples are tight, the resulting path on \(D\cup K\), together with \(E\), two-covers \(H\). Otherwise boundary antisymmetry reverses a failed joining triple. If
\[
(d_t,k_0,k_1)
\]
fails, then
\[
(k_1,k_0,d_t)
\]
is tight and reverses the initial edge \(k_0k_1\) of \(K\). If \(t\ge2\) and
\[
(d_{t-1},d_t,k_0)
\]
fails, then
\[
(k_0,d_t,d_{t-1})
\]
is tight and reverses the terminal edge of the displayed \(D\)-block. Thus outcome 4 holds. \(\square\)

So an endpoint-rooted Hamiltonian four-support is not a separate terminal obstruction: endpoint deletion converts it into a direct mixed edge, a split/leave-and-return disturbance, an order disagreement, an external end-edge reversal, or a two-cover.

## Metadata

- ID: defect_lines_and_spanning_order_compression_an_endpoint_rooted_hamiltonian_four_set
- Kind: section
- Version: 2
- Math version: 2
- Audit: unaudited
- Refutation: unrefuted

## Authoring state

- Subsection 1 — HOT, version 2: (untitled)
