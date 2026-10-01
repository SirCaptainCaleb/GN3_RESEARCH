# Edge-orderable eight-vertex unions cannot support a trapped 3|5 pair

## Statement

Let W be an eight-vertex set in an edge-orderable boundary tournament. Then W has a partition W=A disjoint-union B with |A|=|B|=4 such that both induced four-sets are Hamiltonian. Consequently, if X|P|Q is a Phi-minimal three-cover in a trapped Astra-003 component with |X|=3 and |P|=5, then the induced boundary tournament on V(X) union V(P) is not edge-orderable; equivalently its comparison digraph contains a directed cycle.

## Body

# Edge-orderable eight-vertex unions cannot support a trapped 3|5 pair

Let W be an eight-vertex set and assume H[W] is edge-orderable.

By the certified four-set density theorem in smallset01, every edge-ordered complete graph on r >= 5 vertices has at least

h_4(r) >= (3/5) binom(r,4)

Hamiltonian four-subsets. For r=8 this gives h_4(8) >= 42.

Complementation pairs the 70 four-subsets of W into 35 unordered complementary pairs {S,W-S}. If no complementary pair were Hamiltonian on both sides, at most one member of each pair could be Hamiltonian, giving h_4(8) <= 35. This contradicts h_4(8) >= 42. Hence some four-set A and its complement B=W-A are both Hamiltonian, yielding an exact 4|4 two-cover of H[W].

Now let C=X|P|Q be Phi-minimal in a trapped Astra-003 component with |X|=3 and |P|=5. Put W=V(X) union V(P). If H[W] were edge-orderable, the first part would give an exact 4|4 cover A|B of H[W]. Replacing X|P by A|B is one legal Astra-003 pairwise repartition. Its contribution to the quadratic potential changes from 3^2+5^2=34 to 4^2+4^2=32, while Q is unchanged. Thus Phi would decrease by 2, contradicting Phi-minimality.

Therefore H[W] is not edge-orderable. By the comparison representation theorem in smallset01, its comparison digraph contains a directed cycle.
