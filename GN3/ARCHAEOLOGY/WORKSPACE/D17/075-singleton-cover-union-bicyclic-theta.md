# A bicyclic hard selected-edge union is an endpoint-currentized theta

**Workspace:** D17
**State:** established
**Key:** `singleton-cover-union-bicyclic-theta`

**Summary:** If a 2-vertex-connected selected-edge union U has cyclomatic number beta(U)=2, then U is a theta graph: exactly two degree-three branch vertices p,q joined by three internally vertex-disjoint paths. In the three-component branch U-{p,q}=A+B+C, separator equality makes the three arm interiors Hamilton atoms. Each atom induces an ordinary path in U, so every Hamilton atom order used by the singleton rows is forced up to reversal to that arm order. The mandatory p-C and q-C returns from minimum-equality incidence are therefore the unique branch-to-arm edges and hit Hamilton endpoints of C. Thus the bicyclic three-component double-bridge residue has endpoint-currentized, not arbitrary, complement returns. The direct p-q arm/two-component theta branch is left separate.

### Bicyclic 2-connected structure
Retain a hypothetical counterexample, a chosen singleton-cover family, and its ordinary selected-edge union U. Assume U is 2-vertex-connected and has cyclomatic number

  beta(U)=|E(U)|-|V(U)|+1=2.

Because U is 2-vertex-connected, every vertex has degree at least two. The degree-surplus identity gives

  sum_v (deg_U(v)-2)=2|E(U)|-2|V(U)|=2.

Hence either exactly two vertices have degree three and every other vertex has degree two, or one vertex has degree four and every other vertex has degree two. The latter is impossible in a 2-vertex-connected graph. Indeed, if v were the unique degree-four vertex, every neighbor of v would have degree one in U-v. Since U-v has maximum degree at most two, a connected U-v could have at most two degree-one vertices, whereas it has four distinct neighbors of v of degree one. Thus U-v is disconnected and v is an articulation vertex.

Therefore U has exactly two degree-three vertices; call them p,q. Every other vertex has degree two. Suppressing maximal degree-two chains gives exactly three internally vertex-disjoint p-q paths. Thus U is an ordinary theta graph.

### The three-component theta branch
Assume now that

  c(U-{p,q})=3.

Equivalently, none of the three theta arms is the direct edge pq. Write A,B,C for the three components of U-{p,q}; these are exactly the nonempty interiors of the three theta arms. Since S={p,q} has

  c(U-S)=3=|S|+1,

`singleton-cover-union-separator-row` applies in equality. Hence A,B,C are Hamilton atoms and the p- and q-deletion rows use each atom as one contiguous tight block. Since U is 2-vertex-connected, no singleton set is an equality separator, so {p,q} is a minimum-cardinality equality set and `singleton-cover-union-minimal-equality-incidence` applies as well.

Each branch vertex has exactly one U-neighbor in each atom. Moreover U[A], U[B], U[C] are ordinary simple paths. Every selected adjacency of any singleton-cover Hamilton block on, say, C lies in U[C]. A Hamilton path on all of C uses |C|-1 selected adjacencies, while the ordinary path U[C] has exactly |C|-1 edges. Therefore the Hamilton order on C is forced, up to reversal, to be the ordinary theta-arm order. The same holds for A and B.

### Endpoint-currentized complement returns
Enter the quiet parallel double-bridge residue of `singleton-cover-union-two-cut-doublebridge`, after relabelling,

  C_p=(A-q-B)|C,
  C_q=(A-p-B)|C.

The minimum-equality incidence theorem forces actual selected p-C and q-C states somewhere in the singleton-cover family. In the theta graph there is only one U-edge from p into C and only one from q into C. These are precisely the two branch edges of the C-arm. Since the retained Hamilton order on C is the ordinary arm order up to reversal, those two selected return edges meet the two Hamilton endpoints of C.

Thus the bicyclic three-component equality branch upgrades the cross-fiber return problem: the fixed-complement returns are not arbitrary interior contacts. They are unique physical endpoint contacts, one from each branch vertex, and they coexist with the parallel bridge row and the dual R542/R696 endpoint packets already carried by C.

### Scope and fence
This section does not close the bicyclic case. A theta graph may have a direct pq arm; then U-{p,q} has only two components and the three-component equality-row argument above does not apply. That theta subcase remains separate. No claim is made that an internal singleton-deletion cover omits one prescribed branch incidence at each end, and no 3-by-3 branch-incidence encoding is asserted. The proved content is only the theta structure and endpoint currentization in the three-component branch.

Status: complete elementary deduction from the selected-edge-union representation and the established separator/minimum-equality sections; not independently canonically reviewed.
