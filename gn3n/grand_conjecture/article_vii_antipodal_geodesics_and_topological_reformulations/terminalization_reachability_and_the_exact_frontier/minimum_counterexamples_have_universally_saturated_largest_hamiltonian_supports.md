# Minimum counterexamples have universally saturated largest Hamiltonian supports

## Composition

(none yet)

## Development

## Universal saturation of a largest proper Hamiltonian support

Let (H) be a minimum-order counterexample to spanning two-coverability.

Then every proper induced subtournament of (H) has a spanning two-cover. In particular, if
[
arnothing
e Ksubsetneq V(H)
]
is Hamiltonian, then
[
operatorname{pc}(H-K)le2.
]
In fact equality holds:
[
oxed{operatorname{pc}(H-K)=2.}
]
Indeed, if (H-K) were Hamiltonian, a Hamilton path on (K) together with one on (H-K) would two-cover (H).

Choose a Hamiltonian support (Ssubsetneq V(H)) of maximum cardinality. Then (H-S) has path-cover number exactly two; fix
[
H-S=Pmid Q.
]

Because (S) is a largest proper Hamiltonian support, for every
[
zin V(H)-S
]
the induced subtournament
[
H[Scup{z}]
]
is non-Hamiltonian. This is true for every outside vertex, not merely for displayed endpoints of (P,Q).

Fix any Hamilton order
[
S=(s_1,ldots,s_k).
]
If
[
h(z,s_1,s_2)=1,
]
then (z,s_1,ldots,s_k) would be a Hamilton path on (S+z), contradiction. Boundary antisymmetry therefore gives
[
oxed{h(s_2,s_1,z)=1.}
]
Likewise, if
[
h(s_{k-1},s_k,z)=1,
]
then (s_1,ldots,s_k,z) would be Hamiltonian, so
[
oxed{h(z,s_k,s_{k-1})=1.}
]

Thus every exterior label simultaneously reverses the displayed initial and terminal edges of every chosen Hamilton order of (S).

### Consequences

1. The distinction between “largest Hamiltonian support” and “largest admissible Hamiltonian support with two-coverable complement” disappears in a minimum counterexample: every proper Hamiltonian support is automatically admissible.
2. Every bounded Hamiltonian support produced anywhere in the argument automatically sits in a spanning three-cover.
3. Hereditary-descent alternatives (H-K) with (operatorname{pc}(H-K)ge3) are impossible for every proper Hamiltonian support (K).
4. The deletion-critical-complement theorem for genuine (kappa_2=2) states must **not** be imported here: a minimum counterexample has (kappa_2(H)=1), and (H-S-v) may be Hamiltonian. The valid replacement is the universal two-ended noninsertability above.

This is scale-independent minimum-counterexample structure and does not use any small-order cutoff.
