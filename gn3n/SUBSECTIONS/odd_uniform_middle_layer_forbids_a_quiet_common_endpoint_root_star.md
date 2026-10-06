# Odd uniform middle layer forbids a quiet common-endpoint root star

## Metadata

- ID: odd_uniform_middle_layer_forbids_a_quiet_common_endpoint_root_star
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 277
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

Assume n=2r+1 and that every r-set is Hamiltonian while every (r+1)-set is non-Hamiltonian. Let D be a Hamiltonian (r-1)-set with displayed order D=(d_1,...,d_{r-1}), and put Y=V(H)-D.

Suppose that for every y in Y the Hamiltonian support D+y has a Hamilton order obtained by inserting y in one common endpoint gap of this same displayed order. After symmetry, assume
(y,d_1,...,d_{r-1})
is tight for every y in Y.

For distinct y,z in Y, the set D+y+z has order r+1 and is therefore non-Hamiltonian. Hence neither
(y,z,d_1,...,d_{r-1})
nor
(z,y,d_1,...,d_{r-1})
can be tight. All triples after the first are inherited from the displayed D-order, so the failures are exactly
h(y,z,d_1)=0,
h(z,y,d_1)=0.
Boundary antisymmetry gives
h(d_1,z,y)=1,
h(d_1,y,z)=1.
Thus for every ordered pair of distinct roots a,b in Y,
h(d_1,a,b)=1.

Now choose any r-element subset R of Y. By the uniform hypothesis H[R] is Hamiltonian; let
(a_1,...,a_r)
be a Hamilton order. The sequence
(d_1,a_1,...,a_r)
is then tight: its first triple is tight by the preceding complete root relation, and every later triple is inherited from the Hamilton order on R. This is a Hamilton path on an (r+1)-set, contradicting the uniform hypothesis.

The terminal-endpoint version is symmetric.

Therefore the exact odd uniform middle-layer residue cannot realize the quiet common-endpoint alternative of the isolated-root extension-star theorem. For every Hamiltonian (r-1)-core and any attempt to synchronize all of its one-root Hamiltonian extensions, some genuine order disagreement, positioned reversal, or internal Hamiltonian support must occur. This eliminates the quiet branch scale-independently; no bounded support is regarded as terminal progress.

## Frontier

- Development version when composed: None
- Development version now: 1
