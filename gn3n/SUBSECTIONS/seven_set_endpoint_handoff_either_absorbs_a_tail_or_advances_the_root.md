# Audit: unoriented endpoint exposure does not give a tail handoff

## Metadata

- ID: seven_set_endpoint_handoff_either_absorbs_a_tail_or_advances_the_root
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 124
- Row version: 2
- Development version: 2
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

The proposed handoff from a seven-set endpoint cover to a fixed tight tail is not justified.

The theorem in [[localextend01]] says that for a seven-set (U) and prescribed (win U), there is a (4|3) cover (K|R) in which a Hamilton order of (K) has (w) as **an endpoint**, and at least three different vertices can occur as its neighbor. It does not say that (w) can be prescribed as the initial endpoint or as the terminal endpoint.

That distinction is essential. A tight Hamilton order cannot in general be reversed. The attempted proof incorrectly took a Hamilton order having (c_2) as an endpoint and “oriented” it so that its final two vertices were (t,c_2). This step is invalid.

There is a simple structural obstruction to any universal terminal-endpoint strengthening. In an edge-orderable boundary tournament, declare all ordinary edges incident with a prescribed vertex (w) smaller than every ordinary edge not incident with (w). Tight paths are increasing edge paths. Any four-path ending
[
(a,b,c,w)
]
would require
[
ab<bc<cw,
]
which is impossible because (cw) is smaller than the two preceding non-(w) edges. Thus (w) may be forbidden as a terminal endpoint even though endpoint-exposure theorems still supply Hamilton paths beginning at (w).

Consequently the earlier claimed implication
[
h(t,c_2,c_3)=1
Longrightarrow
(K,c_3,c_4,ldots)	ext{ tight}
]
is available only when the particular Hamilton order on (K) already **ends** in (t,c_2). The seven-set theorem does not guarantee such an order.

The three-hook conclusion obtained when all proposed terminal handoffs fail is therefore also unsupported, because the three neighbors need not arise on the terminal side of (c_2).

### Correct frontier

The useful local facts remain:

- blocked/no-farther geometry supplies bounded Hamiltonian supports with the corridor vertex as an endpoint;
- seven-set (4|3) covers supply at least three possible neighbors of a prescribed endpoint;
- genuine two-deletion residues supply strong reverse-junction constraints.

What is missing is **oriented endpoint control**. A valid rooted handoff theorem must either

1. produce a Hamilton packet whose displayed tight order has the corridor root on the required side, so it concatenates to the surviving tail; or
2. prove that systematic failure of the required endpoint orientation forces a bounded reverse-junction configuration, an outward buffer, or a farther positive witness.

This orientation issue is not cosmetic. It is the exact obstruction between an endpoint-containing/endpoint-exposed Hamiltonian support and an actual tail absorption.
