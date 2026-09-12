# Every selected-edge union of a counterexample singleton family is bridgeless

**Workspace:** D17
**State:** established
**Key:** `singleton-cover-union-bridgeless`

**Summary:** Let U be the ordinary union of all selected rail adjacencies from any chosen exact singleton-deletion two-cover family. In a hypothetical counterexample U is connected by the coherence/disconnection theorem. In fact U has no bridge. If a bridge uv separates nontrivial sides A,B, the u- and v-deletion covers cannot cross the cut and therefore Hamiltonize B and A respectively, giving a spanning two-cover. If one bridge side is the singleton {u}, then deleting the opposite endpoint isolates u in U-v and forces a forbidden singleton rail. Thus every such U is 2-edge-connected, independently of K-minimality or the chosen representatives.

### Statement
Let H be a hypothetical smallest counterexample, choose arbitrarily one exact two-nonempty-path cover C_x of H-x for every vertex x, and let U be the ordinary selected-edge union from `singleton-cover-union-disconnection`. Then U is connected and has no bridge.

Connectivity is already forced by that section: a disconnected U gives coherent singleton partitions and a spanning two-cover. It remains to exclude a bridge.

### A bridge with two nontrivial sides closes H
Suppose e=uv is a bridge of U. Let A,B be the two components of U-e, with u in A and v in B. First assume |A|>=2 and |B|>=2.

Consider the actual singleton-deletion cover C_u of H-u. Every selected adjacency of C_u belongs to U-u. The bridge e is absent, and by definition of the bridge there is no other U-edge between A and B. Hence no C_u rail can contain vertices from both A-u and B. Both sets are nonempty and the two nonempty rails of C_u span their union. Therefore their supports are exactly

  (A-u) | B.

In particular B has a Hamilton tight path, namely its C_u rail. By the same argument C_v has support partition

  A | (B-v),

so A has a Hamilton tight path. These Hamilton A- and B-paths are vertex-disjoint and span H, contradiction.

### A pendant bridge side also closes H
Suppose instead A={u}; the B-singleton case is dual. Since uv is the only U-edge incident from u to B, deleting v removes that edge and leaves u isolated in U-v. Every selected adjacency of C_v lies in U-v, so the rail of C_v containing u has no selected edge incident with u. Thus that rail is the singleton {u}. The other C_v rail is Hamiltonian on H-{u,v}. But the dimer (u,v) is vacuously tight, so this Hamilton path together with (u,v) is a spanning two-cover of H, contradiction.

Thus U has no bridge in all cases.

### Consequences and scope
For every singleton-cover selection in a hypothetical counterexample, not merely a K-minimizing or edge-minimizing one,

  U is connected and 2-edge-connected.

Hence every selected physical adjacency used anywhere in the family lies on an ordinary cycle of the global selected-edge union, and |E(U)|>=|V(H)|. This is a support/adjacency theorem only: the ordinary cycles of U do not carry synchronized tight path orientation and are not themselves tight cycles. The next separator-level question is whether an articulation vertex or a two-edge cut can likewise be converted into a coherent global support split or a bounded currentization packet.

Status: complete elementary deduction from the working union-disconnection theorem and the singleton-rail closure argument; not independently reviewed or canonically certified.
