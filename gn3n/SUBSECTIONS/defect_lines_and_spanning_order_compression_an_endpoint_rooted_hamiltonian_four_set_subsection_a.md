# defect_lines_and_spanning_order_compression_an_endpoint_rooted_hamiltonian_four_set_subsection_a

## Metadata

- ID: defect_lines_and_spanning_order_compression_an_endpoint_rooted_hamiltonian_four_set_subsection_a
- Parent Section: defect_lines_and_spanning_order_compression_an_endpoint_rooted_hamiltonian_four_set
- Position: 1
- Row version: 5
- Development version: 5
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

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

The endpoint-rooted four-support interface can be pushed directly into two positional disturbances.

**Lemma 8.** Let (H) be a minimum counterexample. Let
[
K=(k_0,k_1,k_2,k_3)
]
be a Hamiltonian four-path and suppose
[
H-K=Amid B
]
is a two-cover. Put
[
C={k_1,k_2,k_3},
]
and let (F) be any deletion cover of (H-k_0). Relative to the displayed three-cover
[
Cmid Amid B
]
of (H-k_0), at least one of the following holds.

1. An inherited displayed path is split into at least two (F)-blocks. Consequently either an inherited displayed edge has its endpoints in different paths of (F), or one path of (F) leaves that displayed path through a nonempty exterior segment and later returns.
2. A tight triple reverses an end edge of a displayed block occurring in (F), or the initial edge (k_0k_1) of (K).
3. (H) has a two-cover.

The symmetric statement holds after deleting (k_3).

**Proof.** Let (t) be the number of ordinary edges of (F) whose endpoints lie in different classes of
[
Cmid Amid B.
]
Since (F) has two path components while the displayed cover has three, the component-drop lemma gives (tge1).

If (tge2), cutting all interclass edges of (F) produces
[
2+tge4
]
nonempty monochromatic blocks distributed among only the three nonempty classes (C,A,B). Hence some displayed class occurs in at least two blocks. Along its inherited displayed path, choose a first ordinary edge whose endpoints lie in distinct blocks. If those blocks lie in different path components of (F), the inherited edge is split between the two comparison paths. If they lie in the same path component, maximality of the monochromatic blocks forces a nonempty exterior segment between them. Thus outcome 1 holds.

It remains that (t=1). Cutting the unique interclass edge produces exactly three monochromatic blocks, one from each of (C,A,B). One block is an entire component of (F), and the other two are concatenated in the second component.

If the unique interclass edge joins (A) directly to (B), then (C) is the isolated component and the other component is a Hamiltonian path on
[
Acup B=H-K.
]
Together with the displayed path (K), this gives outcome 3.

Hence (C) is concatenated with one of (A,B); call that class (D), and call the remaining isolated class (E). Let
[
R=(r_1,r_2,r_3)
]
be the order induced by the (C)-block of (F). No agreement with the inherited order ((k_1,k_2,k_3)) is needed.

Suppose first that the mixed component has order
[
R,D.
]
Prepend (k_0). If
[
(k_0,r_1,r_2)
]
is tight, the resulting path covers (Kcup D), because (R) covers the three vertices (K-{k_0}); together with (E) this two-covers (H). If this triple is non-tight, boundary antisymmetry gives
[
(r_2,r_1,k_0)
]
tight, reversing the initial edge (r_1r_2) of the displayed (C)-block. Thus outcome 2 holds.

Now suppose the mixed component has order
[
D,R.
]
Append (k_0). If
[
(r_2,r_3,k_0)
]
is tight, the resulting path on (Dcup K), together with (E), two-covers (H). Otherwise
[
(k_0,r_3,r_2)
]
is tight and reverses the terminal edge (r_2r_3) of the displayed (C)-block. Again outcome 2 holds. (square)

Thus endpoint deletion from a Hamiltonian four-support has only two genuine nonterminal outcomes:
[
	ext{external end-edge reversal}
qquad	ext{or}qquad
	ext{split/leave-and-return}.
]
Neither a direct edge between the complementary supports nor a disagreement in the order of the three-vertex core survives as an independent branch.


### A prescribed complementary endpoint can be exposed on the four-support

The local extension calculus strengthens the endpoint-rooted setup by making the prescribed label an actual endpoint of the Hamilton order.

**Lemma 10 (double endpoint anchor).** Let \(H\) be a minimum counterexample. Then there exist a Hamiltonian four-set \(X\), a two-cover
\[
H-X=P\mid Q,
\qquad
P=(y,p_1,\ldots,p_m),
\qquad m\ge3,
\]
and a Hamiltonian four-path
\[
K=(y,k_1,k_2,k_3)
\]
such that
\[
V(K)-\{y\}\subseteq X
\qquad\text{and}\qquad
\operatorname{pc}(H-K)=2.
\]
Thus \(y\) is simultaneously a displayed endpoint of the complementary path \(P\) and a displayed endpoint of the bounded support \(K\).

**Proof.** Choose four consecutive vertices from a component of any spanning three-cover of \(H\); let their support be \(X\). Then \(X\) is Hamiltonian. Minimum-counterexample calculus gives
\[
\operatorname{pc}(H-X)=2.
\]
Choose a two-cover \(H-X=P\mid Q\) with \(P\) a larger component. Since \(|V(H)|>10\), we have \(|P|\ge4\). Write
\[
P=(y,p_1,\ldots,p_m).
\]

Choose a tight three-vertex subpath \((a,b,c)\) of a Hamilton order on \(X\), and let \(d\) be the fourth vertex of \(X\). The prescribed-endpoint extension theorem in [[localextend01]] applied to \((a,b,c)\) and \(d,y\) gives a Hamiltonian support
\[
S\subseteq X\cup\{y\},
\qquad 4\le |S|\le5,
\]
with a Hamilton order having \(y\) as an endpoint.

If \(|S|=4\), take \(K=S\). If \(|S|=5\), delete from the displayed Hamilton order the endpoint opposite \(y\). The remaining four vertices inherit a Hamilton order still having \(y\) as an endpoint. Thus
\[
K-\{y\}\subseteq X.
\]

The support \(K\) is proper. Minimum-counterexample calculus gives
\[
\operatorname{pc}(H-K)\le2.
\]
If \(H-K\) were Hamiltonian, a Hamilton path on \(K\) together with one on \(H-K\) would two-cover \(H\). Hence
\[
\operatorname{pc}(H-K)=2.
\]
Orient the Hamilton order of \(K\) from \(y\). \(\square\)

Applying Lemma 8 with \(k_0=y\) now produces, unless \(H\) already has a two-cover, either an external end-edge reversal or a split/leave-and-return disturbance while preserving a label \(y\) that was already exposed as an endpoint in the independent cover \(H-X=P\mid Q\).

This supplies a double endpoint anchor for the remaining compression problem: the same vertex is available simultaneously in the old complementary path geometry and in the new four-support comparison geometry.


## Frontier

- Development version when composed: None
- Development version now: 5
