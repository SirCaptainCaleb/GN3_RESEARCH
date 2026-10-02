# Fixed-pair orientation gives a three-quarter density theorem for Hamiltonian four-sets

## Statement

Let W be an r-vertex set, r>=4, in a boundary tournament, and let h_4(W) be the number of Hamiltonian four-subsets of W. Put m=r-2 and q=floor(m/2). Then h_4(W) is at least (binom(r,2)/4) times [binom(floor(m/2),2)+binom(ceil(m/2),2)], rounded up to the next integer. In particular h_4(W)>=42 for r=8, >=81 for r=9, and >=135 for r=10; asymptotically the guaranteed Hamiltonian four-set density tends to 3/4.

## Body

Fix an unordered pair T subset W. By bd3c8d17ca06, the other m=r-2 vertices split into two fixed-pair orientation classes C_+,C_-, and every exterior pair contained in one class completes T to a Hamiltonian four-set. If |C_+|=c, this gives binom(c,2)+binom(m-c,2) witness pairs. This convex quantity is minimized when the classes are as balanced as possible, namely at c=floor(m/2) or ceil(m/2). Hence every fixed pair T has at least s_m=binom(floor(m/2),2)+binom(ceil(m/2),2) same-class Hamiltonian witnesses.

There are binom(r,2) fixed pairs, so altogether there are at least binom(r,2)s_m witness incidences (T,F), where F is a Hamiltonian four-set containing T and F-T is a same-class exterior pair. By fourset_fixedpair_witness_bound01, any one four-set F can occur in at most four such incidences. Therefore h_4(W)>=ceil[binom(r,2)s_m/4].

For r=8, m=6 and s_m=6, giving h_4>=28*6/4=42. For r=9, m=7 and s_m=9, giving h_4>=36*9/4=81. For r=10, m=8 and s_m=12, giving h_4>=45*12/4=135. Finally s_m=(1/4+o(1))m^2, while binom(r,4)=(1/24+o(1))r^4 and binom(r,2)=(1/2+o(1))r^2, so the ratio of the lower bound to binom(r,4) tends to (1/8)/4 divided by 1/24 =3/4.