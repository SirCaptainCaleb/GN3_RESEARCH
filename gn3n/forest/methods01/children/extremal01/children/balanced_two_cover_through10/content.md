# The balanced two-cover conjecture holds through order ten

## Statement

Every boundary tournament H on 2<=n<=10 vertices has a spanning two-path cover whose component orders are floor(n/2) and ceil(n/2).

## Body

For n<=6 the claim is immediate from the definition and the fact that every three-vertex boundary tournament is Hamiltonian: split into parts of orders floor(n/2),ceil(n/2), noting that paths of order one and two are trivial and every part of order three is Hamiltonian.

For n=7, choose any six-set U. By smallset01, U has a Hamiltonian five-subset F. A Hamiltonian five-set has at most three non-Hamiltonian four-subsets, so F contains a Hamiltonian four-set A. Its complement in V(H) has order three and is Hamiltonian. Thus H has a 4|3 cover.

For n=8, apply the certified structural theorem balanced8_structural01 to obtain a 4|4 partition.

For n=9, apply balanced9_counting01 to obtain a 4|5 partition.

For n=10, apply the certified order-ten theorem in extremal01 that every ten-vertex boundary tournament has a Hamiltonian 5|5 partition.

These are exactly the balanced component orders floor(n/2),ceil(n/2) in every case.