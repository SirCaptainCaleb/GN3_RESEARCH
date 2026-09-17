# A cyclic selected-edge union forces a Hamilton path

**Workspace:** D17
**State:** established
**Key:** `singleton-cover-union-cycle-exclusion`

**Summary:** For n>=9, the selected-edge union U of a singleton-cover family in a counterexample cannot be a simple n-cycle. If U=C_n, each C_x consists of all cycle edges except the two incident with x and one further edge. Record the intrinsic boundary orientation of every consecutive cycle triple. A sign change between consecutive triples forces every cover to omit at least one edge from a fixed three-edge window. Two disjoint sign-change windows are impossible because a deletion vertex outside both windows leaves only one additional omitted edge. Hence all sign changes lie within three consecutive positions; parity leaves zero or two, with the minority orientation on at most two adjacent vertices. Omitting the cycle edge between suitable endpoints then gives a Hamilton tight path. Thus any 2-connected selected-edge union in a counterexample has cyclomatic number at least two.

### Setup
Assume n=|V(H)|>=9 and that the ordinary selected-edge union U of a chosen exact singleton-cover family is the simple cycle

  v_0 v_1 ... v_{n-1} v_0.

Write e_i={v_i,v_{i+1}} with indices modulo n. Since C_{v_j} is an exact two-path cover of H-v_j, it has exactly n-3 selected adjacencies. Every selected adjacency lies in U. The two cycle edges e_{j-1},e_j are unavailable because v_j is deleted, so C_{v_j} selects every cycle edge except

  e_{j-1}, e_j, f_j

for one further cycle edge f_j. Equivalently its two rails are the two path components obtained from the cycle after those three edge deletions and deletion of v_j.

### Intrinsic consecutive-triple signs
For every i define epsilon_i=+ when (v_{i-1},v_i,v_{i+1}) is tight and epsilon_i=- when its complete reversal is tight. Boundary antisymmetry makes this a well-defined binary sign.

Suppose epsilon_i != epsilon_{i+1}. No chosen cover can select all three consecutive cycle edges

  e_{i-1}, e_i, e_{i+1}.

Indeed those three edges would lie consecutively on one rail of that cover. Traversing that rail in either direction forces the two consecutive tight turns centered at v_i and v_{i+1} to have the same cycle orientation, contrary to epsilon_i != epsilon_{i+1}. Therefore for every deletion vertex v_j, at least one of its three omitted cycle edges lies in the window

  W_i={e_{i-1},e_i,e_{i+1}}.

### Two disjoint sign-change windows are impossible
Suppose sign changes occur at i and r and W_i,W_r are disjoint. Each three-edge window has at most four incident vertices, so their union has at most eight incident vertices. Since n>=9 choose v_j incident with no edge of either window. Then neither e_{j-1} nor e_j lies in W_i union W_r. The only remaining omitted edge f_j would therefore have to lie in W_i in order to block the first sign change and simultaneously in W_r in order to block the second. This is impossible because the windows are disjoint.

Hence the three-edge windows of all sign changes pairwise intersect. For n>=9, two such cyclic three-edge windows intersect only when their change positions have cyclic distance at most two. A pairwise-intersecting family therefore has at most three consecutive change positions. The number of sign changes in a cyclic binary word is even, so there are either no sign changes or exactly two. In the latter case the two change positions are at cyclic distance one or two.

### Hamilton path
If there are no sign changes, all epsilon_i have one common sign. Traversing the cycle in that orientation and omitting any one cycle edge gives a tight Hamilton path on all n vertices.

If there are two changes at distance one, the minority sign occurs at one vertex; if they are at distance two, the minority sign occurs at two adjacent vertices. Choose the omitted cycle edge so that the two endpoints of the resulting Hamilton path contain all minority-sign vertices (and, in the one-minority case, one adjacent majority vertex). Every internal vertex of the resulting cycle traversal then has the common majority sign, so every consecutive ordered triple is tight. Thus the traversal is a Hamilton tight path of H.

Therefore U=C_n implies H is Hamiltonian for n>=9. In particular a hypothetical smallest counterexample has no cyclic selected-edge union. Combined with `singleton-cover-union-block-normal-form`, its selected-edge union is connected and bridgeless; if 2-vertex-connected it must contain at least two independent cycles (equivalently |E(U)|>=n+1).

Status: complete elementary working deduction. The n>=9 range comfortably includes the live smallest-counterexample regime; no claim is made here for smaller n.

## References

```json
[
    {
        "role": "Boundary antisymmetry makes the consecutive-cycle triple sign binary and governs reversal in the cycle-orientation argument.",
        "relation": "dependency",
        "revision_id": "R3"
    }
]
```
