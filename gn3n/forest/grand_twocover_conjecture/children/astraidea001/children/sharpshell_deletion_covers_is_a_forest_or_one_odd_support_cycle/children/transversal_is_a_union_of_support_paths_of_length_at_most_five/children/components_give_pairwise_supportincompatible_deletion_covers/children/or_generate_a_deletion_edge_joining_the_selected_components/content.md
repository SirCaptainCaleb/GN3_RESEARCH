# Sharp half-order shell support-incompatible pairs are crossed or generate a deletion edge joining the selected components

## Statement

Let H be in the sharp half-order shell n=2lambda+1, and let F_a=P_a|Q_a and F_b=P_b|Q_b be lambda|lambda covers of H-a and H-b. On U=V(H)-{a,b}, let A|B and C|D be their induced unordered support partitions. If these partitions differ, then after relabeling the classes exactly one of the following holds:
(i) all four intersections A∩C,A∩D,B∩C,B∩D are nonempty;
(ii) there is a single vertex x in U such that C=A union {x} and D=B-{x}. In case (ii), necessarily
F_a=(A union {b}) | B
and
F_b=(A union {x}) | ((B-{x}) union {a}),
up to swapping the two components, and therefore
(A union {b}) | ((B-{x}) union {a})
is a lambda|lambda cover of H-x.
Consequently, if F_a and F_b are selected edges in distinct components of a deletion-cover transversal, the singleton-transfer case creates an unselected Hamiltonian-support edge labelled x joining support vertices from those two selected components.

## Body

Restrict each lambda|lambda cover to U by deleting the other omitted label. Exactly one component of F_a contains b, so the two induced class sizes are lambda and lambda-1. Thus {|A|,|B|}={lambda,lambda-1}. Likewise {|C|,|D|}={lambda,lambda-1}.

If all four intersections are nonempty, (i) holds. Otherwise relabel so A∩D is empty. Then A subseteq C and D subseteq B. Since the unordered partitions differ, A is a proper subset of C. But both |A| and |C| belong to {lambda-1,lambda}, so necessarily
|C|=|A|+1
and C=A union {x}
for a unique x. Complementing inside U gives D=B-{x}. This proves the support normal form.

In this labeling |A|=lambda-1 and |B|=lambda. To recover F_a from its restriction to U, the vertex b must be adjoined to the smaller class A, giving
F_a=(A union {b}) | B.
Similarly |C|=lambda and |D|=lambda-1, so restoring a in F_b gives
F_b=C | (D union {a})=(A union {x}) | ((B-{x}) union {a}).

Both A union {b} and (B-{x}) union {a} are therefore Hamiltonian supports of order lambda: the first is a component of F_a and the second a component of F_b. They are disjoint, and their union is
A union B union {a,b} minus {x}=V(H)-{x}.
Hence they form a lambda|lambda cover of H-x.

If F_a,F_b are selected edges from different transversal components, the support A union {b} is a vertex of the first selected component and (B-{x}) union {a} a vertex of the second. Their disjointness therefore gives a Hamiltonian-support edge labelled x joining those components. ∎