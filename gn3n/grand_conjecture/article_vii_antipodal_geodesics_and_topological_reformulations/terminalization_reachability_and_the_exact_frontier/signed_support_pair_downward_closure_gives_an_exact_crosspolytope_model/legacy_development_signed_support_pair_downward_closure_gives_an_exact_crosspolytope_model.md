# Signed support-pair downward closure gives an exact crosspolytope model — preserved pre-item development

## Composition

(none yet)

## Development

Let O_n be the boundary complex of the n-crosspolytope, with signed vertices v+ and v-. Define E(H) as the simplicial downward closure of disjoint Hamiltonian support pairs: A+ union B- is a face iff A,B are disjoint and there exist disjoint Hamiltonian supports A' superset A and B' superset B.

E(H) is antipodally invariant under sign swap. It is a genuine simplicial complex even though Hamiltonianity itself is not hereditary, because a subface keeps the same witnessing support pair.

Exact identity:
dim E(H) = n-kappa_2(H)-1.

Proof: each support pair (A',B') contributes a simplex of size |A'|+|B'|. Conversely every face lies in a witnessing support-pair simplex. Hence maximum face size equals max(|A'|+|B'|). The complement of such a pair is a deletion set leaving a two-cover, and every minimum deletion two-cover supplies such a pair. Therefore kappa_2(H)=n-max(|A'|+|B'|).

Consequences:
- kappa_2=0 iff E(H) has an (n-1)-simplex, i.e. a full signed transversal;
- kappa_2=1 iff maximum faces have ambient codimension one;
- kappa_2=2 iff maximum faces have ambient codimension two.

This target is strictly less rigid than the support-pair order complex. It records extendability rather than demanding every intermediate subset itself be Hamiltonian. That is safe: a full n-label face has no unused labels available to extend with, so its witness is an actual spanning support pair.

A minimum pair {x,y} with H-{x,y}=P|Q becomes the codimension-two simplex P+ union Q- and its antipode. Dissimilar deletion covers are therefore glued as codimension-two simplices according only to common support signs, not path-order agreement.

Likewise, if a Hamiltonian support S has complement P|Q, then E(H) contains S+ union P- and S+ union Q- (and antipodes), glued along S+. Thus bounded supports become actual carrier pieces rather than terminal outputs.

Topological closure target: prove the free antipodal complex E(H) has Z_2-index n-1. Since index is at most dimension, this forces dim E(H)>=n-1 and therefore kappa_2(H)=0. More generally an index lower bound d gives kappa_2(H)<=n-d-1.

This is an exact order-free topological model of deletion distance inside the original crosspolytope sphere.
