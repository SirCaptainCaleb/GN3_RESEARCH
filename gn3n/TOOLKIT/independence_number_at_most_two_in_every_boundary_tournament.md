# Endpoint-pair Hamiltonicity graphs have independence number at most two in every boundary tournament

**Summary:** Every prescribed pair has a Hamiltonian four-extension inside every exterior triple; therefore every five-set has at least three Hamiltonian four-subsets.

## Statement

Let H be any boundary tournament and fix distinct vertices L,R. On any set W disjoint from {L,R}, define a graph J on W by yz in E(J) exactly when H[{L,R,y,z}] is Hamiltonian. Then alpha(J)<=2. Consequently e(J)>=binom(|W|,2)-floor(|W|^2/4). In particular, inside every five-vertex set F and for every prescribed pair {L,R} subset F, some Hamiltonian four-subset of F contains L and R; hence every five-set has at least three Hamiltonian four-subsets.

## Body

Take any three distinct x,y,z in W. For each t in {x,y,z}, boundary antisymmetry gives exactly one of (L,t,R) and (R,t,L) as a tight triple. Two labels, say x,y, have the same type.

If (L,x,R) and (L,y,R) are tight, boundary antisymmetry on the ordered triple (x,R,y) gives exactly one of (x,R,y) and (y,R,x). In the first case (L,x,R,y) is a tight Hamilton path on {L,R,x,y}; in the second case (L,y,R,x) is.

If instead (R,x,L) and (R,y,L) are tight, apply boundary antisymmetry to (x,L,y). One of (R,x,L,y) and (R,y,L,x) is a tight Hamilton path.

Thus every three vertices of W span an edge of J, so alpha(J)<=2. Equivalently the complement of J is triangle-free, and Mantel's theorem gives the edge bound.

For the five-set corollary, take W=F-{L,R}, which has three vertices. Hence some Hamiltonian four-subset contains the prescribed pair. Let G be the set of vertices d in F for which F-{d} is Hamiltonian. The prescribed-pair conclusion says that for every pair {L,R} subset F there is d in G outside {L,R}. If |G|<=2, choose a pair containing all vertices of G, a contradiction. Therefore |G|>=3.

## Metadata

- ID: independence_number_at_most_two_in_every_boundary_tournament
- Kind: toolkit
- Version: 2
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
