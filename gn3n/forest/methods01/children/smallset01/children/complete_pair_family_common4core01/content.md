# A complete pair-extension family over a three-set contains two five-sets with four common vertices

## Statement

Let D be a three-vertex set in a boundary tournament and let E be a disjoint four-vertex set. Suppose D union {x,y} is Hamiltonian for every two distinct x,y in E. Then there exist d in D and distinct a,b in E such that both (D-{d}) union (E-{a}) and (D-{d}) union (E-{b}) are Hamiltonian five-sets. Their intersection has order four.

## Body

For each a in E, set S_a=D union (E-{a}), a six-set. For each x in E-{a}, deleting x leaves D together with the other two vertices of E-{a}, Hamiltonian by hypothesis. Thus S_a has at least three Hamiltonian one-vertex deletions. By the four-of-six theorem in smallset01 it has at least four, so for some d_a in D, S_a-{d_a} is Hamiltonian. There are four values of a and only three choices in D, so two distinct a,b have d_a=d_b=d. The corresponding Hamiltonian five-sets intersect in (D-{d}) union (E-{a,b}), which has order four. No minimum-counterexample hypothesis is used.
