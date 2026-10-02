# A fixed pair yields a one-third common-core transport star partitioned into at most 120 coherent path types

## Statement

Let H be a minimum counterexample. Let C be a three-set, let B={u,v} be a two-set disjoint from C, and let A be any finite set disjoint from C union B.

Then there exist a two-set D contained in C and A_0 contained in A with |A_0| >= ceil(|A|/3) such that, with K=D union B, every five-set K union {a}, a in A_0, is Hamiltonian and its complement is non-Hamiltonian with path-cover number two.

For every distinct a,b in A_0, the common-four-core theorem applies to K union {a} and K union {b}. Hence U_ab=K union {a,b} is either Hamiltonian with non-Hamiltonian path-cover-two complement, or is non-Hamiltonian with the four-good-deletion one-/two-label transport package of yield_a_hamiltonian_sixset_or_fourgooddeletion_transport.

Moreover, after choosing one Hamilton path on K union {a} for each a in A_0, the set A_0 can be partitioned into at most 120 classes according to the relative order of K and the insertion slot of a. In every class there is an ordering K=(k_1,k_2,k_3,k_4) and one slot j common to all its leaves. If j is 1 or 3, then K union {a,b} is Hamiltonian for every two distinct leaves a,b in that class. If j=2, then (k_1,k_2,a,k_3,k_4) is a tight Hamilton path for every leaf a in the class. If j=0, then (a,k_1,k_2,k_3,k_4) is a tight Hamilton path for every leaf a, so all leaves are common left extenders of the same ordered four-path K. If j=4, then (k_1,k_2,k_3,k_4,a) is a tight Hamilton path for every leaf a, so all leaves are common right extenders of K. No pairwise Hamiltonicity is asserted for the endpoint slots.

Consequently one class has size at least ceil(|A_0|/120) >= ceil(|A|/360), and it is either a pairwise-Hamiltonian six-set class, a coherent central-gap fan, or a coherent same-end extender family. Every leaf pair in every class retains the six-set transport dichotomy above.

## Body

For each a in A, apply the four-of-six theorem to C union B union {a}. At least four of its six one-vertex deletions are Hamiltonian. Only the three deletions removing one of u,v,a avoid deleting a vertex of C. Therefore some c(a) in C satisfies (C-{c(a)}) union B union {a} Hamiltonian.

Pigeonhole c(a) over C. Some c occurs for at least ceil(|A|/3) labels. Put D=C-{c}, K=D union B, and let A_0 be those labels. Then K union {a} is Hamiltonian for every a in A_0. Each is proper, and minimum-counterexample calculus gives a non-Hamiltonian path-cover-two complement.

Fix distinct a,b in A_0. The Hamiltonian five-sets K union {a} and K union {b} share the four-core K, so yield_a_hamiltonian_sixset_or_fourgooddeletion_transport gives the stated six-set transport dichotomy.

Choose one Hamilton path P_a on K union {a} for each a in A_0. Record the relative order of K and the insertion slot of a. There are at most 4!*5=120 records.

Fix one class and write its common K-order as (k_1,k_2,k_3,k_4).

If the common slot is 1, then P_a=(k_1,a,k_2,k_3,k_4). For distinct a,b, exactly one of (a,k_1,b) and (b,k_1,a) is tight, because these two ordered triples are a reversal pair. In the first case (a,k_1,b,k_2,k_3,k_4) is a Hamilton path; in the second case (b,k_1,a,k_2,k_3,k_4) is. Hence every pair of leaves in a slot-1 class Hamiltonizes with K.

If the common slot is 3, then P_a=(k_1,k_2,k_3,a,k_4). Exactly one of (a,k_4,b) and (b,k_4,a) is tight. Accordingly one of (k_1,k_2,k_3,a,k_4,b) and (k_1,k_2,k_3,b,k_4,a) is a Hamilton path. Hence every pair of leaves in a slot-3 class also Hamiltonizes with K.

If the common slot is 2, then by definition (k_1,k_2,a,k_3,k_4) is a tight Hamilton path for every leaf a, giving the coherent central-gap fan.

If the common slot is 0, then P_a=(a,k_1,k_2,k_3,k_4) for every leaf a. Thus (k_1,k_2,k_3,k_4) itself is a tight path and every leaf is a common left extender through the same initial ordered pair. Boundary antisymmetry does not in general concatenate two such same-end extenders; sameend_extenders_do_not_automatically_concatenate gives an explicit counterexample, so no pairwise-Hamiltonicity conclusion is made here.

The slot-4 case is the corresponding common right-extender family: P_a=(k_1,k_2,k_3,k_4,a) for every leaf a, again with no automatic concatenation claim.

Pigeonholing among at most 120 classes gives one of size at least ceil(|A_0|/120) >= ceil(|A|/360). The pairwise yield_a_hamiltonian_sixset_or_fourgooddeletion_transport transport statement was established before this path-type partition and therefore remains valid for every leaf pair in every class.