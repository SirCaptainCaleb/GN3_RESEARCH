# The physical square loop can remain nontrivial in the honest target carrier

# A successful edge coloring whose reachable-target carrier does not fill a physical 2-face

The genuine reachability target complex K=union_(z,q) K_q(z) contains the entire physical Q_n edge graph G via crossed diagonal-fiber edges. A tempting proof of high equivariant index would extend this physical graph face-by-face over the boundary of a physical cube. The following exact example shows the necessary two-face filling statement already fails for an antipodally odd coloring with monochromatic antipodal geodesics.

Work in Q_2. Assign red (0) to edges 00--10 and 10--11; assign blue (1) to edges 11--01 and 01--00. Opposite edges have opposite colors, so the coloring is antipodally odd. Both 00--10--11 and 00--01--11 are monochromatic antipodal geodesics, respectively red and blue. Define K(z)=K_0(z) union K_1(z) inside affine target fiber F_z, using witnessed monochromatic prefix-chain simplices.

**Theorem (the embedded physical 4-cycle survives in first homology).** In this coloring:
- K(00)=F_00 is a full triangulated 2-disk: the two monochromatic two-edge orders triangulate the two halves of F_00.
- K(11)=F_11 is likewise a full 2-disk.
- K(10) is a V-shaped tree of two 1-simplices, both red and based at the apex for 10.
- K(01) is a V-shaped tree of two 1-simplices, both blue and based at the apex for 01.

Distinct target-fiber intersections obey:
K(00) intersect K(11)={o} (the common center);
each K(10),K(01) intersects each of K(00),K(11) in precisely the midpoint of their common physical cube edge;
K(10) intersect K(01)=empty.
There are no triple intersections. Thus these four contractible subcomplexes form a good cover (after a common PL subdivision) with nerve the graph on vertices A=00,B=11,C=10,D=01 with edges AB,AC,BC,AD,BD. Its first homology has rank 2, and the embedded physical square G traces the cycle A--C--B--D--A. That 4-cycle is nonzero in H_1(K;F2) and therefore cannot bound a disk in K.

Proof of intersection pattern: F_z intersect F_z' imposes r_i=s_i=1/2 for each coordinate where z,z' differ. Opposite target cubes F_00,F_11 meet only at o; both full disks contain o. A one-step star K(10) or K(01) lies on one coordinate at a time and misses o. For an adjacent full disk and star, the sole matching radial segment meets the common target hyperplane once, at the crossed-edge midpoint. The remaining assertions and nerve computation follow.

**Dimension-independent local obstruction.** For any n>=3, choose valid antipodally odd edge colors c_1(x)=x_2 and c_2(x)=1+x_1; for each k>=3 choose c_k(x)=x_1. Every c_k is independent of x_k and flips under full vertex complementation. On any 2-face with free coordinates 1,2, the color pattern is exactly the displayed red-red-blue-blue square. Restrict the global diagonal-fiber cross X_n to its two-coordinate target subcross with all other root bits fixed and other support coordinates zero. The intersection with K is precisely the above Q_2 carrier: any path-prefix simplex meeting that subcross contributes only prefixes using directions 1,2. Hence the physical square boundary remains non-nullhomologous IN THAT FACE CARRIER. A proof extending the physical cube graph over each physical square by a map landing in its two-coordinate reachable-label carrier is impossible even in instances already satisfying the conjecture.

The result does NOT rule out global fillings that leave the physical face, nor more sophisticated color-dependent chains. It explains why extending the physical cube's antipodal boundary map cell-by-cell with an overly restrictive geometric carrier is an unjustified shortcut.
