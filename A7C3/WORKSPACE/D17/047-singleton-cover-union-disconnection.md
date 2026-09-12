# Singleton-fiber coherence is exactly disconnection of the selected-edge union

**Workspace:** D17
**State:** established
**Key:** `singleton-cover-union-disconnection`

**Summary:** For a chosen exact singleton-deletion two-cover C_x for every vertex x, let U be the ordinary graph formed by the union of every selected rail adjacency used anywhere in the family. The support partitions are pairwise overlap-coherent iff U is disconnected. In a counterexample, any disconnected U has exactly two nontrivial components, and each C_x has those two components restricted to V-x as its rail supports; hence the two global components are Hamiltonian by choosing one deletion from the opposite component. Thus the global conjecture would follow from the parent theorem that some singleton-cover family has disconnected selected-edge union.


### Setup
Let H be a hypothetical smallest counterexample. For every physical vertex x choose one actual exact cover

  C_x=P_x | Q_x

of H-x by two nonempty tight paths. Let U be the ordinary undirected graph on V(H) whose edge set is the union of all physical adjacencies selected along all rails P_x,Q_x, over all deletion labels x. No orientation or multiplicity is retained in U.

Recall the elementary singleton-rail fence: no exact two-cover of H-x can have a singleton rail {y}, because the other rail would be Hamiltonian on H-{x,y} and the vacuous dimer (x,y) would complete a spanning two-cover of H.

### Coherence implies disconnection
Assume the support partitions sigma_x of the chosen covers are pairwise overlap-coherent as in `codimension-one-coherence`. That section produces global classes A|B such that for every x the two rail supports of C_x are exactly the nonempty restrictions of A|B to V(H)-{x}. Every selected adjacency of every C_x therefore has both endpoints in A or both endpoints in B. Hence U has no A-B edge and is disconnected.

### Disconnection implies coherence
Conversely suppose U is disconnected, with connected components K_1,...,K_r. Every selected edge of every C_x lies inside one K_i. Since C_x consists of exactly two path components spanning V(H)-{x}, the set V(H)-{x} meets at most two components of U for every x.

We claim r=2. Certainly r>=2. If r>=3 and some K_i has at least two vertices, choose x in K_i. Then K_i-{x} is nonempty and at least two other U-components remain, so V(H)-{x} meets at least three U-components, impossible. Hence under r>=3 every K_i is a singleton. But then choosing any x leaves r-1 components, so r-1<=2 and n=r<=3, impossible in the present smallest-counterexample setup. Thus r=2.

Write the two U-components as A,B. Neither is a singleton. If A={a}, choose any x in B. Then every selected edge of C_x lies in U-x, so the rail containing a has no selected adjacency incident with a and is the forbidden singleton rail {a}. The B-singleton case is dual. Hence |A|,|B|>=2.

Now fix x in A. Both A-{x} and B are nonempty. Since the two rails of C_x are connected by selected edges, every rail lies in one U-component. Two nonempty rails span (A-{x}) union B, so their supports are exactly

  (A-{x}) | B.

For x in B the dual support partition is

  A | (B-{x}).

Therefore the chosen singleton partitions are pairwise overlap-coherent.

### Closure
Choose a in A. In C_a, the entire B-support is one Hamilton rail. Choose b in B; in C_b, the entire A-support is one Hamilton rail. These two Hamilton paths are disjoint and span H, contradiction.

Hence, for chosen singleton covers in a hypothetical counterexample,

  pairwise support coherence
    <=> U is disconnected,

and either condition closes H.

### Parent formulation
The grand conjecture would therefore follow from the stronger selection theorem:

  For every smallest counterexample candidate H, one can choose one exact singleton-deletion two-cover C_x for each x so that the union U of all selected rail adjacencies is disconnected.

This formulation replaces all pairwise support comparisons by one physical graph. It does not claim that minimizing |E(U)|, connectivity, cyclomatic number, or any other simple graph statistic automatically yields such a family. Existing same-union recombination fences concern extracting a two-cover from a fixed selected-edge union and do not refute the possibility of choosing a different singleton family whose union is disconnected.

Status: complete elementary equivalence and closure deduction, working exposition. The disconnected-union selection theorem is open.

