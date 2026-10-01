# A complete endpoint-pair family of Hamiltonian five-sets contains two members with four common vertices

## Statement

Let H be a minimum counterexample, let D be a three-vertex set, and let E be a four-vertex set disjoint from D. Suppose D union {x,y} is Hamiltonian for every two distinct x,y in E. Then there exist d in D and distinct a,b in E such that both (D-{d}) union (E-{a}) and (D-{d}) union (E-{b}) are Hamiltonian five-sets. These two five-sets meet in four vertices, and each has non-Hamiltonian path-cover-two complement.

## Body

For each a in E, consider the six-set S_a=D union (E-{a}). For every x in E-{a}, deleting x from S_a leaves D together with the other two vertices of E-{a}, which is Hamiltonian by hypothesis. Thus S_a has at least three Hamiltonian one-vertex deletions. By the certified four-of-six theorem smallset01, S_a has at least four Hamiltonian one-vertex deletions, so for some d_a in D the five-set (D-{d_a}) union (E-{a}) is Hamiltonian. There are four choices of a and only three vertices of D, so two distinct a,b have d_a=d_b=d. The corresponding two Hamiltonian five-sets intersect in (D-{d}) union (E-{a,b}), which has order four. Each support is proper; in a minimum counterexample its complement cannot be Hamiltonian, hence has path-cover number two.