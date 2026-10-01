# Balanced order-nine covers have prescribed four-side vertex and pair mobility

## Statement

Let H be a boundary tournament on nine vertices. For every vertex v, at least six balanced 4|5 partitions have v on the four-side. For every prescribed pair {u,v}, at least two balanced 4|5 partitions have u and v together on the four-side.

## Body

Fix a vertex v. For each w!=v, the fixed pair {v,w} has seven exterior vertices. By 1000615 their two orientation classes yield at least C(3,2)+C(4,2)=9 same-class exterior pairs, hence at least nine Hamiltonian four-sets containing {v,w}. Summing over the eight choices of w gives at least 72 incidences between w and Hamiltonian four-sets containing v. Each such four-set contains exactly three choices of w besides v, so at least 24 Hamiltonian four-sets contain v.

Now work on the eight-vertex set V-v. Count incidences (F,E) with E a six-set and F a Hamiltonian five-set contained in E. There are C(8,6)=28 six-sets and each contains at least four Hamiltonian five-subsets by smallset01, giving at least 112 incidences. Every five-set lies in exactly three six-sets, so at least ceil(112/3)=38 five-subsets of V-v are Hamiltonian. Complementation identifies the 56 four-subsets containing v with the 56 five-subsets of V-v. Inclusion-exclusion therefore gives at least 24+38-56=6 balanced 4|5 partitions with v on the four-side.

Now fix a pair S={u,v}. The seven vertices outside S split into two fixed-pair orientation classes, yielding at least nine Hamiltonian four-sets containing S. On the seven-vertex set V-S, four-of-six double counting gives at least 14 Hamiltonian five-sets: its seven six-subsets contribute at least 28 incidences, and each five-set lies in exactly two six-subsets. There are C(7,5)=21 five-subsets of V-S, in bijection by complementation with the 21 four-subsets containing S. Hence inclusion-exclusion gives at least 9+14-21=2 balanced partitions whose four-side contains both u and v.
