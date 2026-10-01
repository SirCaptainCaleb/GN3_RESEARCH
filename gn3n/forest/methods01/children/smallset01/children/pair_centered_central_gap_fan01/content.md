# Every prescribed pair has a linear coherent common-core path-type family

## Statement

Let H be a minimum counterexample of order n. Fix a two-set B and a disjoint three-set C, and put A=V(H)-(B union C).

Then there exist a four-set K containing B and a set A_1 contained in A with
|A_1| >= ceil((n-5)/360)
such that K union {a} is Hamiltonian for every a in A_1 and, after labeling K={k_1,k_2,k_3,k_4}, one of the following holds.

(1) For every two distinct a,b in A_1, the six-set K union {a,b} is Hamiltonian. Hence its complement in H is non-Hamiltonian with path-cover number two.

(2) For every a in A_1,
(k_1,k_2,a,k_3,k_4)
is a tight Hamilton path on K union {a}.

(3) Every leaf is a common same-end extender of one ordered four-path: either
(a,k_1,k_2,k_3,k_4)
is a tight Hamilton path for every a in A_1, or
(k_1,k_2,k_3,k_4,a)
is a tight Hamilton path for every a in A_1.

Thus every prescribed pair lies in a linear common-four-core family of one of three coherent types: a pairwise-Hamiltonian six-set family, a central-gap insertion fan, or a common same-end extender family.

## Body

For each a in A, apply the four-of-six theorem to the six-set C union B union {a}. At least four of its six one-vertex deletions are Hamiltonian. Only the three deletions removing one of the vertices in B union {a} avoid deleting a vertex of C. Hence some c(a) in C has
(C-{c(a)}) union B union {a}
Hamiltonian.

By pigeonhole, some c in C works for at least ceil(|A|/3)=ceil((n-5)/3) labels. Put
D=C-{c}, K=D union B,
and let A_0 be the corresponding labels. Then K union {a} is Hamiltonian for every a in A_0.

For each a in A_0 choose one Hamilton path P_a on K union {a}. Record the relative order of the four vertices of K along P_a and the insertion slot of a among those four vertices. There are at most
4! * 5 = 120
such types. Therefore some set A_1 contained in A_0 of size at least
ceil(|A_0|/120) >= ceil((n-5)/360)
has one common type.

Write the common relative order of K as
(k_1,k_2,k_3,k_4)
and let j in {0,1,2,3,4} be the common insertion slot.

If j=2, then by definition
P_a=(k_1,k_2,a,k_3,k_4)
for every a in A_1, giving outcome (2).

If j=1, then
P_a=(k_1,a,k_2,k_3,k_4)
for every a. For distinct a,b, exactly one of
(a,k_1,b), (b,k_1,a)
is tight, since these are a reversal pair. Accordingly one of
(a,k_1,b,k_2,k_3,k_4)
and
(b,k_1,a,k_2,k_3,k_4)
is a Hamilton path on K union {a,b}. Thus every leaf pair Hamiltonizes.

If j=3, exactly one of
(a,k_4,b), (b,k_4,a)
is tight. Accordingly one of
(k_1,k_2,k_3,a,k_4,b)
and
(k_1,k_2,k_3,b,k_4,a)
is a Hamilton path, so again every leaf pair Hamiltonizes. In either j=1 or j=3 we obtain outcome (1). Each such Hamiltonian six-set is proper, and minimum-counterexample calculus makes its complement non-Hamiltonian with path-cover number two.

If j=0, then
P_a=(a,k_1,k_2,k_3,k_4)
for every a in A_1, so the leaves form a common left-extender family. If j=4, then
P_a=(k_1,k_2,k_3,k_4,a)
for every a in A_1, giving a common right-extender family. These are outcome (3). No pairwise Hamiltonicity follows merely from common same-end extension: certified 1000149 gives a counterexample to that concatenation inference.

This exhausts the five insertion slots and proves the corrected three-way conclusion.
