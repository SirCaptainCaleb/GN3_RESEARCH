# Marked minima are global minima

## Metadata

- ID: longest_paths_and_reversal_structure_reversals_are_unavoidable_subsection_d
- Parent Section: longest_paths_and_reversal_structure_reversals_are_unavoidable
- Position: 4
- Row version: 5
- Development version: 5
- Composition version: None
- Composition stale: False

## Cold composition

(none yet)

## Development


### Endpoint polarities on a three-cover force an anchored four-support

The endpoint-polarity triangle theorem remains valid, with the final carrier chosen from the common component rather than from the two exterior twin labels.

**Lemma 18 (endpoint-polarity triangle).** Let
\[
A=(a_1,\ldots,a_r),\qquad
B=(b_1,\ldots,b_s),\qquad
C=(c_1,\ldots,c_t)
\]
be a spanning three-cover of a minimum counterexample, with all three paths nontrivial. Then the six displayed endpoint edges contain a Hamiltonian four-support.

For each unordered pair of displayed paths, either a Hamiltonian four-set already occurs among their endpoint data, or the pair has one of exactly two coherent polarities:

- **initial polarity:** the initial endpoint of each path reverses the terminal edge of the other;
- **terminal polarity:** the terminal endpoint of each path reverses the initial edge of the other.

**Proof.** The pairwise concatenation analysis is unchanged. For a pair \(A,B\), if both junction triples in one displayed concatenation fail, their boundary reversals concatenate to a Hamiltonian four-path. If exactly one junction triple fails in each concatenation order, the mixed failure patterns are absorbed by the carrier-switch comparison. Hence, outside bounded support, only the two coherent polarities remain.

Color the three pair-edges
\[
AB,\ BC,\ CA
\]
by their polarities. A triangle with two colors has a vertex at which the two incident pair-edges have the same color. Suppose this vertex is \(A\).

If both \(AB\) and \(AC\) have initial polarity, then the initial endpoint \(a_1\) reverses the terminal edge of \(B\) and the terminal edge of \(C\). These are vertex-disjoint displayed edges. By the valid common-reverser lemma, one carrier reversing two disjoint terminal edges forces a Hamiltonian four-support.

If both \(AB\) and \(AC\) have terminal polarity, then the terminal endpoint \(a_r\) reverses the initial edge of \(B\) and the initial edge of \(C\). Again these are vertex-disjoint displayed edges, and the symmetric initial-initial common-reverser lemma gives a Hamiltonian four-support.

Thus every two-coloring of the polarity triangle forces the desired support. \(\square\)

The previous proof error was to use the two exterior labels that both reverse one common edge of \(A\). Same-edge twins do not force bounded support. The correct carrier is the corresponding endpoint of \(A\), which reverses two **different** exposed edges, one in each of the other two paths.

Hence the endpoint-polarity network really does force an anchored Hamiltonian four-support in every nontrivial spanning three-cover.


### Every spanning three-cover is already marked

The distinction between a global (Phi)-minimum and a global marked-reversal minimum disappears.

**Lemma 19.** Let (H) be a boundary (3)-tournament with
[
operatorname{pc}(H)ge3,
]
and let
[
Amid Bmid C
]
be any spanning three-cover. Then some displayed end edge of one component is reversed by a tight triple through a vertex of another component. In particular, every spanning three-cover is a marked reversal state.

**Proof.** At most one component can be a singleton. Indeed, if two components were singletons, their two vertices form a tight two-vertex path, and together with the third displayed component this would give a spanning two-cover.

Hence at least two displayed components are nontrivial; relabel them (A) and (B), with
[
A=(a_1,ldots,a_r),qquad B=(b_1,ldots,b_s),
qquad r,sge2.
]
Their union is non-Hamiltonian, since a Hamilton path on (V(A)cup V(B)), together with (C), would two-cover (H).

Consider the displayed concatenation
[
(a_1,ldots,a_r,b_1,ldots,b_s).
]
Every consecutive triple except the two junction triples
[
(a_{r-1},a_r,b_1),qquad
(a_r,b_1,b_2)
]
is inherited and tight. Since the union is non-Hamiltonian, at least one junction triple is non-tight. Boundary reversal therefore gives respectively
[
(b_1,a_r,a_{r-1})
qquad	ext{or}qquad
(b_2,b_1,a_r)
]
tight. The first reverses the terminal edge of (A) through (b_1); the second reverses the initial edge of (B) through (a_r). (square)

**Corollary 20.** In a minimum counterexample, minimizing
[
Phi=|A|^2+|B|^2+|C|^2
]
over all spanning three-covers is exactly the same optimization problem as minimizing (Phi) over marked reversal states.

Hence all conclusions previously proved for a globally (Phi)-minimal marked reversal state apply to an ordinary global (Phi)-minimum of the three-cover repartition graph. In particular, outside the bounded-support conclusions already obtained, the global minimum has one of the equitable profiles
[
(r,r,r),qquad
(r,r,r+1),qquad
(r,r+1,r+1).
]

This removes any need to preserve a particular reversal certificate while descending in (Phi): every intermediate spanning three-cover automatically carries some displayed end-edge reversal.
