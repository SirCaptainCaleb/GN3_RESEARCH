# Fixed-pair orientation classes are Hamiltonian four-extension cliques

## Statement

Let H be a boundary tournament and let L,R be distinct vertices. Partition the remaining vertices into
C_+={y:(L,y,R) is tight},
C_-={y:(R,y,L) is tight}.
Then for any two distinct y,z in the same class, H[{L,R,y,z}] is Hamiltonian.

Equivalently, if J_{L,R} is the graph on V(H)-{L,R} in which yz is an edge exactly when {L,R,y,z} is Hamiltonian, then C_+ and C_- are cliques of J_{L,R}. Hence alpha(J_{L,R})<=2. In particular, in every boundary tournament of order at least five, every prescribed vertex pair lies in a Hamiltonian four-set; more strongly, among any three vertices exterior to the prescribed pair, some two complete it to a Hamiltonian four-set.

## Body

Boundary antisymmetry gives exactly one of (L,y,R) and (R,y,L) for every y outside {L,R}, so C_+,C_- partition the exterior vertices.

Take distinct y,z in C_+. Thus (L,y,R) and (L,z,R) are tight. On the three-set {y,L,z}, boundary antisymmetry gives exactly one of (y,L,z) and (z,L,y).

If (y,L,z) is tight, then
(y,L,z,R)
is a tight four-path, because its consecutive triples are (y,L,z) and (L,z,R).

If instead (z,L,y) is tight, then
(z,L,y,R)
is a tight four-path, using (L,y,R).

Thus {L,R,y,z} is Hamiltonian.

The proof for y,z in C_- is symmetric without reversing a displayed path: from (R,y,L),(R,z,L), exactly one of (y,R,z),(z,R,y) is tight. These give respectively the tight four-paths
(y,R,z,L) or (z,R,y,L).

Therefore both orientation classes are cliques in J_{L,R}. Any independent set in J_{L,R} contains at most one vertex from each class, so alpha(J_{L,R})<=2.

If at least three vertices lie outside {L,R}, two share an orientation class, proving the prescribed-pair corollary. The same pigeonhole argument inside any chosen exterior three-set gives the stronger local form.

No cyclic invariance or path reversal is used.