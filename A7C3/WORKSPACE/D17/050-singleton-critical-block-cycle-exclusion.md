# A critical block above order four has a tricyclic deletion-path union

**Workspace:** D17
**State:** established
**Key:** `singleton-critical-block-cycle-exclusion`

**Summary:** For a boundary subtournament Omega of order at least five with a Hamilton path after every singleton deletion, the union J of any chosen deletion-Hamilton paths is automatically 2-vertex-connected. If beta(J)=1, J is a cycle; adjacent deletion rows share a turn, R3 synchronizes their cycle directions, and Omega becomes Hamiltonian. If beta(J)=2, J is a theta. Deleting either branch vertex forces one theta arm to be the direct branch edge, so J is a cycle plus one chord. The two branch-deletion Hamilton paths either splice immediately; opposite orientations are impossible on any arm with at least three internal vertices, and the only remaining arm sizes (2,1),(1,2),(2,2) close by direct R3/one-row checks. Hence every non-Hamiltonian deletion-Hamiltonian Omega of order at least five has beta(J)>=3. Applied to each articulation block of a counterexample singleton selected-edge union, every side of order at least five contributes at least three independent cycles; if both sides are at least five the global union has beta at least six.

### Local deletion-path union is automatically 2-connected

Let `Omega` be a boundary subtournament and, for every `z in Omega`, choose one actual Hamilton tight path `P_z` on `Omega-{z}`. Let `J` be the ordinary undirected union of all selected consecutive adjacencies used by these paths.

For every `z`, the graph `J-z` contains the spanning ordinary path underlying `P_z`, so `J-z` is connected. Hence, once `|Omega|>=3`, `J` is 2-vertex-connected. In particular every vertex has ordinary degree at least two and every edge lies on an ordinary cycle.

The question is how small the cyclomatic number

`beta(J)=|E(J)|-|Omega|+1`

can be when `Omega` itself is non-Hamiltonian.

### Unicyclic local union forces a Hamilton path

Assume `r=|Omega|>=5` and `beta(J)=1`. A connected 2-vertex-connected unicyclic graph is one simple cycle, say

`v_0 v_1 ... v_{r-1} v_0`.

For each deletion label `v_i`, the path `P_{v_i}` has `r-1` vertices and `r-2` selected adjacencies. The graph `J-v_i` is an ordinary path with exactly `r-2` edges, so `P_{v_i}` uses every one of them. Thus its literal order is one of the two orientations of the cycle with `v_i` removed. Record that orientation by `s_i in {+,-}` relative to the displayed cyclic order.

For adjacent deletion labels `v_i,v_{i+1}`, the long surviving cycle arc contains at least three consecutive vertices because `r>=5`. The two deletion paths therefore share a consecutive three-vertex turn. Opposite signs would certify that turn and its exact reverse simultaneously, contradicting R3. Hence `s_i=s_{i+1}` for every `i`, so all deletion paths use one common cyclic direction.

Assume it is `+`. Then `P_{v_{r-1}}=(v_0,...,v_{r-2})` certifies every consecutive turn of `(v_0,...,v_{r-1})` except the last, while `P_{v_0}=(v_1,...,v_{r-1})` certifies that final turn. Therefore `(v_0,...,v_{r-1})` is a Hamilton tight path on `Omega`, contradiction. The reverse common sign is identical.

So a non-Hamiltonian deletion-Hamiltonian block of order at least five has `beta(J)>=2`.

### Bicyclic local union is a cycle plus one chord

Assume now `beta(J)=2`. Since `J` is 2-connected, suppressing all degree-two vertices leaves the standard bicyclic 2-connected core: two branch vertices `p,q` joined by three internally vertex-disjoint paths. Thus `J` is a theta graph.

Delete branch vertex `p`. The graph `J-p` contains the Hamilton path `P_p`. If all three theta arms had an internal vertex, `J-p` would have three nonempty branches meeting only at `q`, and no vertex-simple Hamilton path could traverse all three. Hence one theta arm has no internal vertex and is the direct edge `pq`. The other two arms have the form

`A=(p,a_1,...,a_m,q)`,

`B=(p,b_1,...,b_n,q)`,

with `m,n>=1`. Thus `J` is an ordinary cycle formed by `A union B` plus the chord `pq`.

The graphs `J-p` and `J-q` are ordinary paths, so their chosen Hamilton orders are unique up to reversal. Reverse the global display if necessary so

`P_p=(a_1,...,a_m,q,b_n,...,b_1)`.                    (CB.1)

There are exactly two orientations for `P_q`:

`P_q=(b_n,...,b_1,p,a_1,...,a_m)`                     (ALIGNED)

or

`P_q=(a_m,...,a_1,p,b_1,...,b_n)`.                    (OPPOSED)

In ALIGNED, if `m>=2`, append `q` to `P_q`; the only new final turn `(a_{m-1},a_m,q)` is certified by `P_p`. If `m=1`, then `n>=2` because `|Omega|>=5`, and prepending `q` to `P_q` uses only the new initial turn `(q,b_n,b_{n-1})`, again certified by `P_p`. Thus ALIGNED always Hamiltonizes `Omega`.

In OPPOSED, if `m>=3`, the two paths certify opposite orientations of an internal consecutive `A`-triple, contradicting R3. If `n>=3`, the same argument applies on `B`. Hence an OPPOSED survivor must have `m,n<=2`. Since `m+n+2>=5`, only `(m,n)=(2,1),(1,2),(2,2)` remain.

For `(2,1)`, write

`A=(p,a_1,a_2,q)`, `B=(p,b_1,q)`.

Then (CB.1) and OPPOSED give tight paths

`(a_1,a_2,q,b_1)`,

`(a_2,a_1,p,b_1)`.

R3 chooses exactly one of the reversal pair `(q,b_1,p)` and `(p,b_1,q)`. In the first case

`(a_1,a_2,q,b_1,p)`

is Hamilton; in the second

`(a_2,a_1,p,b_1,q)`

is Hamilton. Thus `(2,1)` is impossible, and `(1,2)` is its exact dual.

For `(2,2)`, write

`A=(p,a_1,a_2,q)`, `B=(p,b_1,b_2,q)`.

The two branch-deletion paths are

`P_p=(a_1,a_2,q,b_2,b_1)`,

`P_q=(a_2,a_1,p,b_1,b_2)`.                            (CB.2)

Inspect the required Hamilton path `P_{a_1}` inside the ordinary graph `J-a_1`. The vertex `a_2` is a leaf there, so every Hamilton path starts or ends at `a_2`. Up to reversal there are only two underlying possibilities:

`a_2,q,b_2,b_1,p`,

`a_2,q,p,b_1,b_2`.

The first orientation is impossible because its final turn `(b_2,b_1,p)` is the exact reverse of the tight turn `(p,b_1,b_2)` in `P_q`; its reverse orientation is impossible because it contains `(b_1,b_2,q)`, the exact reverse of the tight `(q,b_2,b_1)` in `P_p`. The reverse of the second underlying path is likewise blocked by `(b_2,b_1,p)`. Therefore the actual tight `P_{a_1}` must be

`(a_2,q,p,b_1,b_2)`.

It certifies `(a_2,q,p)` and `(q,p,b_1)`. Together with `(a_1,a_2,q)` from `P_p` and `(p,b_1,b_2)` from `P_q`, these turns give the Hamilton path

`(a_1,a_2,q,p,b_1,b_2)`

on all of `Omega`, contradiction.

Therefore a non-Hamiltonian deletion-Hamiltonian boundary subtournament of order at least five cannot have `beta(J)=2` either. We have proved the local bound

`beta(J) >= 3`.                                         (CB.3)

Equivalently, every chosen complete singleton-deletion Hamilton family on such a block uses at least

`|E(J)| >= |Omega|+2`

distinct ordinary selected adjacencies.

The order-four exception remains real: the shared-turn synchronization used above disappears, and the familiar non-Hamiltonian four-cell is deletion-Hamiltonian.

### Application to an articulation block of the global singleton selected-edge union

Retain the accepted exact cut-vertex normal form `singleton-cover-union-block-normal-form` SV3086 and the accepted bridgeless union theorem SV2736. Let `U` be the selected-edge union of a chosen singleton-cover family in a hypothetical counterexample, let `w` be an articulation, and write

`U-w=A disjoint_union B`.

Put

`Omega_A=A+{w}`, `Omega_B=B+{w}`.

SV3086 retains, for every `x in A`, the contiguous `(A-x)+w` portion of the actual `x`-deletion cover as a Hamilton tight path on `Omega_A-x`; for deletion `w`, the literal `A` rail of `C_w` is a Hamilton path on `Omega_A-w`. Every one of these selected adjacencies lies in `U[Omega_A]`. Hence the local union of these chosen deletion paths is a spanning subgraph of `U[Omega_A]` and is 2-connected by the first paragraph. The dual statement holds for `Omega_B`.

If `|Omega_A|>=5`, applying (CB.3) to that retained local family gives

`|E(U[Omega_A])| >= |Omega_A|+2`,                       (CB.4)

and dually for `Omega_B`. This improves the mere bridgeless lower bound by two full cycle-rank units on every large critical side.

There are no `A-B` edges in `U`, the two induced blocks share only `w`, and their edge sets partition `E(U)`. Writing `beta_A=|E(U[Omega_A])|-|Omega_A|+1` and similarly for `B`, one has exactly

`beta(U)=beta_A+beta_B`.                                (CB.5)

Therefore every critical side of order at least five contributes at least three to the global cyclomatic number. In particular, if both sides have order at least five then

`beta(U)>=6`.

If exactly one side has order at least five, that side contributes at least three while the other connected bridgeless side contributes at least one, so `beta(U)>=4`. No use of R24 is made.

### Scope

This is still a union-complexity theorem rather than the desired articulation-absorption theorem. Its value is that a large double-critical overlap cannot be supported by a cycle or a theta on either side: each large side already contains at least three independent ordinary cycles in the actual selected-edge reservoir. The next consumer should exploit the first extra ear beyond the theta floor to reselect a singleton row across the articulation or force a current order discrepancy. No anonymous R176/R435 payment is taken here.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    }
]
```
