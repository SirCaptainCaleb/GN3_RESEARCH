# Strict two-thirds all-special threshold for n<=12

## Statement

Let H be a positive-minimum-degree linear triple system on 6<=n<=12, with minimum degree delta and maximum linear-path length L. If 3delta>2L+2, then every edge of H is special. Equivalently, if H has a nonspecial edge then 3delta<=2L+2.

## Body


Let H be a linear 3-uniform hypergraph on n vertices, with 6<=n<=12, positive minimum degree delta, and global maximum linear-path length L. Suppose
  3 delta > 2L+2.
We prove that every edge of H is special.

Assume instead that H has a nonspecial edge. By the structural reduction 0bc3c18c2692, H must belong to one of exactly three classes:

(I) L=3 and delta=3, with H P_4-free;
(II) n=12, L=4, and H is 4-regular with 16 edges and P_5-free;
(III) n=12, L=5, and H is 5-regular with 20 edges, equivalently a one-point puncture of an STS(13).

Class (I) is impossible by 4218a20eafe9, which proves that every P_4-free linear triple system of minimum degree at least three is all-special.

Class (II) is impossible by 8fad0bbb69b6, which proves that every 12-vertex 4-regular P_5-free linear triple system is all-special.

Class (III) is impossible as follows. By b9277764ed94 every nonspecial edge in such a system has rank at least four. The rank-four case is excluded by 09d85d61b8b0. The rank-five case is excluded by ffa00b5a307c, via the nine-vertex residual matching argument. Since the global maximum path length is five, no larger edge rank is possible. Hence Class (III) is all-special as well.

All three alternatives contradict the assumed nonspecial edge. Therefore every edge of H is special.

Equivalently, for every positive-minimum-degree linear triple system on 6<=n<=12, the existence of a nonspecial edge forces
  3 delta <= 2L+2.
This is exactly the strict-threshold assertion previously supported only by the finite search d9ee4adc37d3.
