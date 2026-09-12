# Connected forest-root compatibility is a parity tree and must expose a branching articulation

**Workspace:** D17
**State:** established
**Key:** `singleton-compatibility-parity-articulation`

**Summary:** For a connected chosen singleton-cover compatibility graph in the R926 forest branch, the root is a tree and every port universe is explicit parity-distance data. Two root-port universes satisfy an exact path-parity symmetric-difference formula and are necessarily distinct. Consequently no path root survives: an even-edge root path closes by complementary leaf rails, while an odd-edge root path would give identical endpoint port universes, contradicting the canonical port quotient. Thus every nonclosing forest root genuinely branches and exposes an articulation; the only articulation-free support obstruction is the spanning odd cycle.

### Parity normal form for a connected forest root

Retain a chosen singleton-deletion exact-cover family in a hypothetical counterexample and apply accepted R926 with its actual proof mechanism. Let `G=L(R)` be the compatibility graph and rail-incidence root, with port universes `Omega_P`. Assume `G` is connected and the R926 root is in the forest branch. Since every root vertex is incident with a physical edge, connectedness of the line graph implies that `R` itself is one tree.

Fix a physical label `y`, viewed as root edge `e_y`. R926 constructs the one-defect coloring

`epsilon_y(P)=1` iff `y in Omega_P`.

The two endpoints of `e_y` both have color one, and every other root edge is bichromatic. Because `R` is a tree, deleting `e_y` leaves two rooted tree components, one at each endpoint of `e_y`. Along either component the coloring is forced to alternate with graph distance from that endpoint. Therefore for every root vertex `P`,

`epsilon_y(P)=1` iff `dist_R(P,e_y)` is even,

where `dist_R(P,e_y)` is the minimum graph distance from `P` to an endpoint of `e_y`. Equivalently,

`Omega_P = { y in V(H) : dist_R(P,e_y) is even }`.        (PA.1)

Thus the support partitions are completely determined by the parity geometry of the root tree. If `x=PQ` is a physical root edge, accepted R926 says the two rails of `C_x` have supports `Omega_P-{x}` and `Omega_Q-{x}`. For every other root edge `e_y`, deleting `x` puts `e_y` on exactly one side of the tree cut `R-x`; its distances to `P` and `Q` differ by one. Hence the two rail supports are exactly the odd/even edge-distance classes seen from the two endpoints of `x`.

This is stronger as a representation than merely saying `G` is the line graph of a forest: once the connected root tree is known, there is no further support-partition freedom in the chosen family. Hamilton orders remain separate data and are not synchronized by (PA.1).

### Two-port parity and injectivity of port universes

Let `P,Q` be root vertices at distance `d`, and let `Gamma(P,Q)` be their unique root path. Follow the one-defect coloring `epsilon_y` along this path. Every traversed edge toggles the color except `e_y` itself, when `e_y` lies on the path, because the two endpoints of `e_y` both have color one. Therefore

`epsilon_y(P) xor epsilon_y(Q) = d mod 2` if `e_y` is not in `Gamma(P,Q)`,

and

`epsilon_y(P) xor epsilon_y(Q) = (d-1) mod 2` if `e_y` is in `Gamma(P,Q)`.        (PA.2)

Equivalently,

`Omega_P Delta Omega_Q = E(Gamma(P,Q))` when `d` is even,

`Omega_P Delta Omega_Q = E(R)-E(Gamma(P,Q))` when `d` is odd.                 (PA.3)

The canonical R926 port universes are injective: distinct root vertices cannot have equal universes. To see this directly from the proof mechanism, suppose `Omega_P=Omega_Q=Omega` with `P!=Q`. If `P,Q` are the endpoints of one root edge `x`, then R926 gives `Omega_P intersect Omega_Q={x}`, so equality would force `Omega={x}` and the corresponding rail support would be empty, contrary to the two-nonempty-rail hypothesis. Otherwise choose incident physical edges `x` at `P` and `y` at `Q`; they are distinct. Since incident edge labels belong to their port universes, equality gives `y in Omega_P` and `x in Omega_Q`. The `P`-side rail of `C_x` is `Omega-{x}` and the opposite rail is `V(H)-Omega`; the `Q`-side rail of `C_y` is `Omega-{y}` with the same opposite support. After deleting `x,y`, the two support partitions agree. Hence `x,y` are compatible. In the canonical port quotient their compatibility uses precisely the `P`-port of `x` and the `Q`-port of `y`, so those two ports are one root vertex, contradicting `P!=Q`.

Thus

`P!=Q  =>  Omega_P != Omega_Q`.                         (PA.4)

Combining (PA.3) and (PA.4), two root vertices at odd distance can never have their connecting path contain every root edge.

### Articulation-or-odd-cycle consequence

Still assume `pc(H)>2`. Suppose first that the connected R926 root is a tree `R`. If `R` is a star, then `G=L(R)` is a clique. Hence every pair of singleton-deletion support partitions is compatible. The accepted exact codimension-one coherence unit SV4459 then glues those partitions to one global bipartition whose two classes are Hamiltonian, giving a spanning two-cover of `H`, contradiction.

Therefore a nonclosing connected forest-root family has a non-star tree root. Every non-star tree with at least three edges contains an edge `x=PQ` whose two endpoints both have degree at least two: take any longest path and an internal edge between nonleaf vertices. Removing `x` from `R` leaves two components, each containing at least one further root edge. In the line graph `G=L(R)`, deleting the vertex `x` removes the only line-graph adjacency channel between those two edge sets. Thus `x` is an articulation vertex of `G`.

If the R926 root is not a forest, accepted R926 says it is one odd cycle containing every physical edge, and then `G` is that same spanning odd cycle.

Consequently every connected chosen singleton-cover compatibility graph in a hypothetical counterexample satisfies the exact dichotomy

* `G` is the spanning odd cycle from R926; or
* `G` has an articulation vertex.

Equivalently, a connected articulation-free compatibility graph already closes `H` unless it is the spanning odd-cycle exception. In the forest branch, every 2-connected block of `L(R)` is precisely the clique of root edges incident with one root vertex of degree at least two; distinct such cliques meet, when they meet at all, in the single articulation vertex corresponding to the connecting root edge. Thus all nontrivial support holonomy in the connected forest branch is carried by the block-cut tree, not inside a 2-connected nonclique region.

### No path root survives

Suppose the forest root is the path

`v_0 -e_1- v_1 -e_2- ... -e_m- v_m`.

First let `m=2k` be even. In the leaf-deletion cover `C_{e_1}`, use the rail corresponding to the inner port `v_1`. By (PA.1), after deleting `e_1` its support is exactly

`{e_2,e_4,...,e_{2k}}`.

In `C_{e_{2k}}`, the rail corresponding to the inner port `v_{2k-1}` has support

`{e_1,e_3,...,e_{2k-1}}`.

These are retained Hamilton rails, are disjoint, and partition all physical vertices of `H`. They therefore form a spanning two-cover, contradiction.

Now let `m=2k+1` be odd. For every root edge `e_j`,

`dist_R(v_0,e_j)=j-1`,

`dist_R(v_m,e_j)=m-j`.

Their sum is `m-1`, which is even, so the two distances have the same parity for every `j`. By (PA.1),

`Omega_{v_0}=Omega_{v_m}`.

But `v_0` and `v_m` are distinct root vertices, contradicting port-universe injectivity (PA.4). Thus the previously suggested odd balanced path-root residue does not exist: its apparent endpoint partitions would actually make the two leaf labels compatible and identify the endpoint ports in the canonical quotient.

Therefore **no connected path can occur as the R926 forest root of a hypothetical counterexample**. Every nonclosing connected forest root has a genuine branching vertex, hence at least three leaves and some root degree at least three.

### Selection-theorem target exposed by the normal form

For the Integrator moonshot, a connected forest-root obstruction is now a genuinely branching parity block-cut object. Path-like holonomy is gone completely. The natural forest target is an articulation/branch reselection theorem: either one can re-realize the compatibility blocks across a branching articulation so that the glued region expands or the global K-family improves, or the physical failure geometry at that articulation closes `H`. The sole articulation-free support obstruction left by R926 is the spanning odd cycle, where the existing two-sheet monodromy machinery remains the separate consumer.

No general articulation-reselection theorem is proved here. The new proved content is the parity-distance representation (PA.1), the two-port symmetric-difference law (PA.2)-(PA.3), injectivity of port universes, the articulation-or-spanning-odd-cycle dichotomy, and complete exclusion of path roots.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R926"
    }
]
```
