# Two bad extensions of a Hamiltonian four-set force overlapping Hamiltonian four-sets through both exterior vertices

## Statement

Let H be a boundary tournament, let X be a Hamiltonian four-vertex set, and let a,b be distinct vertices outside X. If X union {a} and X union {b} are non-Hamiltonian, then the graph K on X, with yz in E(K) exactly when H[{a,b,y,z}] is Hamiltonian, contains two adjacent edges. Equivalently, there are distinct x,y,z in X such that {a,b,x,y} and {a,b,x,z} are both Hamiltonian. In particular the endpoint-rooted Hamiltonian-four graph cannot be a perfect matching.

## Body

Let X be a Hamiltonian four-vertex set and let a,b be distinct exterior vertices such that X+a and X+b are non-Hamiltonian. Define K on X by yz in E(K) exactly when {a,b,y,z} is Hamiltonian. We prove that K has two adjacent edges.

Partition X into Y={y:(a,y,b) is tight} and Z={z:(b,z,a) is tight}. Boundary antisymmetry makes this a partition. Each class is a clique in K, by the parallel-middle four-path lemma in localextend01. If K has no adjacent edges, neither class has order greater than two. Thus |Y|=|Z|=2, K consists of the two internal pairs, and every cross four-set {a,b,y,z}, y in Y, z in Z, is non-Hamiltonian.

Apply opposite_fixedpair_nonham_k4_class01 to each cross four-set. Its cyclic possibility is excluded: the exceptional cyclic four-vertex configuration has cyclic comparison orientation on each three-subset (the four-vertex subclaim in localextend01), whereas its three-subset {a,y,z} lies in the non-Hamiltonian five-set X+a, whose comparison digraph is acyclic by smallset01. Therefore each cross four-set is edge-orderable, with opposite-edge blocks
L={ay,bz}, N={ab,yz}, R={az,by},
where L<R and N lies either before L, between L and R, or after R. All comparisons of incident ordinary edges below are intrinsic comparison arcs, independent of the representing total order used.

The four cross four-sets must use the same placement of N. Indeed, if one uses N<L<R, then ab<ay. Every cross four-set with that same y must also use N<L<R, since its other two placements have ay<ab. This forces ab<bz for both z in Z, which forces N<L<R for both y at each z. Similarly, if one uses L<R<N, then az<ab, forcing L<R<N for both y at that z; this forces by<ab for both y, which forces L<R<N for every z at each y. If neither extreme placement occurs, all four use L<N<R.

The common placement N<L<R is impossible. Take a representing edge order on X+a, which exists by smallset01. Choose z in Z, write Z={z,z'}, and order Y={y_1,y_2} so y_1z<y_2z. The common placement gives
y_1z<y_2z<ay_2<az'.
Thus (y_1,z,y_2,a,z') is a Hamilton path on X+a, a contradiction.

The common placement L<R<N is also impossible. In a representing edge order on X+a, choose y in Y, write Y={y,y'}, and order Z={z_1,z_2} so yz_1<yz_2. Then
ay'<az_1<z_1y<yz_2,
so (y',a,z_1,y,z_2) is a Hamilton path on X+a, again a contradiction.

Consequently every cross four-set has the middle placement
{ay,bz}<{ab,yz}<{az,by}.                 (1)
In particular, for each y in Y,z in Z the incident comparisons give
ay<yz<az and bz<yz<by.                  (2)

No Hamilton order on X can begin with a cross pair: if its first two vertices are y,z, prepend a using (a,y,z); if they are z,y, prepend b using (b,z,y). These triples are tight by (2), contradicting non-Hamiltonicity of X+a or X+b. Hence a Hamilton order on X begins with one whole orientation class and ends with the other. By interchanging a,b and Y,Z if necessary, choose a Hamilton order
(y_1,y_2,z_1,z_2).
In a representing edge order on X+a put h=y_1y_2, k=z_1z_2, r=y_2z_1, p=y_1z_1, q=y_1z_2. Then
h<r<k.

If ay_1<h, prepend a to this order, contradicting non-Hamiltonicity of X+a. Otherwise h<ay_1. If ay_1<ay_2, then
ay_1<ay_2<r<k
by (2), so (y_1,a,y_2,z_1,z_2) is Hamiltonian on X+a. Therefore ay_2<ay_1.

If p<k, (2) gives ay_2<ay_1<p<k, making (y_2,a,y_1,z_1,z_2) Hamiltonian on X+a. Thus k<p. If k<q, the intrinsic comparisons
r<k<q<by_1
make (y_2,z_1,z_2,y_1,b) Hamiltonian on X+b. Hence q<k. Finally (2) gives
ay_2<ay_1<q<k,
so (y_2,a,y_1,z_2,z_1) is Hamiltonian on X+a, the final contradiction.

Therefore K contains adjacent edges. Their Hamiltonian four-sets share a,b and one vertex of X, hence intersect in three vertices. No minimum-counterexample, extremality, ambient-order, or path-position hypothesis is used.