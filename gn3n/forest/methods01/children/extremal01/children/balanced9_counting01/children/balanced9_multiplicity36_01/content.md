# Every nine-vertex boundary tournament has at least thirty-six balanced four-five partitions

## Statement

Every boundary tournament on nine vertices has at least thirty-six distinct partitions into a Hamiltonian four-set and a Hamiltonian five-set.

## Body

Let V have order nine. As in balanced9_counting01, extremal01 gives at least 81 Hamiltonian five-sets.

For Hamiltonian four-sets, fix each of the binom(9,2)=36 unordered pairs T. The seven exterior vertices split into two fixed-pair orientation classes. The number of same-class exterior pairs is at least binom(3,2)+binom(4,2)=9, and every such exterior pair together with T is Hamiltonian by bd3c8d17ca06. Hence there are at least 36*9=324 same-class witness incidences (T,F).

By fourset_fixedpair_witness_bound01, any fixed four-set F can receive at most four such witness incidences. Therefore the number of Hamiltonian four-sets is at least 324/4=81.

Complement the Hamiltonian four-sets to a family C4 of at least 81 five-subsets. The Hamiltonian five-set family H5 also has size at least81. Since there are only binom(9,5)=126 five-subsets total, inclusion-exclusion gives |H5 intersect C4|>=81+81-126=36. Each member is a Hamiltonian five-set whose four-vertex complement is Hamiltonian, hence gives a balanced 5|4 partition. Distinct five-sides give distinct partitions.