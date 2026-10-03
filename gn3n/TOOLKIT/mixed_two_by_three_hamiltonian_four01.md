# Every two-by-three split contains a mixed Hamiltonian four-set

**Summary:** If a five-set is partitioned into parts of sizes two and three, some Hamiltonian four-subset meets both parts.

## Statement

Let H be any boundary tournament, and let A,B be disjoint vertex sets with |A|=2 and |B|=3. Then H[A union B] contains a Hamiltonian four-vertex induced subtournament U such that U meets both A and B. In fact every four-subset of A union B meets both parts, while every five-set has at least three Hamiltonian four-subsets.

## Body

Let
\[
F=A\cup B,
\qquad |A|=2,
\qquad |B|=3.
\]
Every four-element subset of \(F\) meets both \(A\) and \(B\): omitting one vertex from a \(2+3\) partition leaves either a \(1+3\) or a \(2+2\) split.

By the endpoint-pair Hamiltonicity theorem, every five-vertex boundary tournament has at least three Hamiltonian four-subsets. Hence at least one four-subset
\[
U\subset F
\]
is Hamiltonian, and the preceding observation shows automatically that
\[
U\cap A\ne\varnothing,
\qquad
U\cap B\ne\varnothing.
\]
Thus \(U\) is a Hamiltonian four-set meeting both sides of the prescribed \(2+3\) partition.

## Metadata

- ID: mixed_two_by_three_hamiltonian_four01
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
