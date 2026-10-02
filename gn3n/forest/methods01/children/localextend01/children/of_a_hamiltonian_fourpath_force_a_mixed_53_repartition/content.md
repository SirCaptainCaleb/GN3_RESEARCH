# Three bad extensions of a Hamiltonian four-path force a mixed 5|3 repartition

## Statement

Let A and B be disjoint Hamiltonian four-vertex subtournaments of a boundary tournament, and fix a Hamilton order B=(b_0,b_1,b_2,b_3). Suppose there are three distinct vertices r_1,r_2,r_3 in A such that B union {r_j} is non-Hamiltonian for j=1,2,3. Then for every pair {r_i,r_j}, both five-sets {b_0,b_1,b_2,r_i,r_j} and {b_1,b_2,b_3,r_i,r_j} are Hamiltonian. Consequently A union B has a two-cover with component orders 5 and 3; indeed the three bad labels give six such 5|3 repartitions.

## Body

Fix distinct r_i,r_j among the three bad extension labels. The four-set B is Hamiltonian with displayed order (b_0,b_1,b_2,b_3), while both B union {r_i} and B union {r_j} are non-Hamiltonian. The repeated-bad-extension theorem in localextend01 therefore gives Hamilton paths on both five-sets {b_0,b_1,b_2,r_i,r_j} and {b_1,b_2,b_3,r_i,r_j}.

For the first five-set, its complement inside A union B consists of b_3 together with the two vertices of A not among {r_i,r_j}. Every three-vertex boundary tournament is Hamiltonian, so this gives a 5|3 cover of A union B. For the second five-set, the complement is b_0 together with those same two remaining vertices of A, again a Hamiltonian three-set. Thus each unordered pair of the three bad labels gives two 5|3 covers, for six in total. ∎