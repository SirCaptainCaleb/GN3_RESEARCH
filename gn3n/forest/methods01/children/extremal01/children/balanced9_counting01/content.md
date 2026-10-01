# Every nine-vertex boundary tournament has a balanced four-five two-cover

## Statement

Every boundary tournament on nine vertices has a partition into a Hamiltonian four-set and a Hamiltonian five-set. Equivalently, every nine-vertex boundary tournament has a spanning balanced two-path cover of component orders 4 and 5.

## Body

Let H be a boundary tournament on a nine-vertex set V. Let H5 be the family of Hamiltonian five-subsets of V and H4 the family of Hamiltonian four-subsets.

First, extremal01 Section 4 gives the universal Hamilton-five density bound h_5(V)>= [4(r-5)/(5(r-4))] * binom(r,5) at r=9. Hence |H5| >= (16/25)*126 = 80.64, so |H5|>=81.

Second, count Hamiltonian four-sets using fixed-pair orientation classes. Fix an unordered pair T={u,v}. The remaining seven vertices split into the two orientation classes C_+,C_- from bd3c8d17ca06, and any two vertices in the same class complete T to a Hamiltonian four-set. If |C_+|=c, the number of such exterior pairs is binom(c,2)+binom(7-c,2), whose minimum over integers 0<=c<=7 occurs at c=3 or4 and equals 9. There are binom(9,2)=36 choices of T, so there are at least 36*9=324 incidences (T,F) with T subset F, |T|=2, and F in H4. Each Hamiltonian four-set F contains only binom(4,2)=6 possible pairs T, so |H4|>=324/6=54.

Now map every Hamiltonian four-set F to its complementary five-set V-F. If H had no balanced 4|5 cover, then no Hamiltonian five-set could be the complement of a Hamiltonian four-set. Thus H5 and {V-F:F in H4} would be disjoint families of five-subsets of V. But the latter family has size |H4|>=54, so their union would have size at least 81+54=135, exceeding the total binom(9,5)=126 five-subsets. Contradiction. Therefore some Hamiltonian five-set has Hamiltonian four-set complement, giving the desired 4|5 partition.
