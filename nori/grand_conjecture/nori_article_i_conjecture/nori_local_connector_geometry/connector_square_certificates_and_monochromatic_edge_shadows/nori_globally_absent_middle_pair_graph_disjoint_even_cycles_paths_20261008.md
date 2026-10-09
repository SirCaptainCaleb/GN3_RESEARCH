# Globally uncertified connector direction pairs form disjoint paths and even cycles

# Global classification of coordinate middle pairs never certified by any mono four-edge geodesic

Let n>=5 and let c be a binary coloring of PHYSICAL ORDERED three-faces of Q_n. The first part needs no NORI axiom; the realization part imposes active c(bar F,rev pi)=1-c(F,pi). For z∈Q_n and four pairwise distinct coordinate directions (a,i,j,d), let P_z(a,i,j,d) be the centered four-edge cube geodesic whose central two coordinates are (i,j). Its first and second ordered-three-face colors are the actual physical colors
 A_a(z;i,j)=c(F(z;{a,i,j}),(a,i,j)),
 B_d(z;i,j)=c(F(z;{i,j,d}),(i,j,d)).
They are equal precisely when this genuine four-edge path is MONOCHROMATIC.

Call the UNORDERED direction pair {i,j} globally ABSENT if there is no centered monochromatic four-geodesic with inner two directions either (i,j) or (j,i) at ANY hub z, for ANY distinct outer a,d.

**THEOREM 1 (exact global rigidity).** Suppose that for one fixed ordered middle pair (i,j) there is NO such connector at ANY z. Then a single bit q_(ij) exists, INDEPENDENT of z and of every outer coordinate a∉{i,j}, such that
  c(F(z;{a,i,j}),(a,i,j))=q_(ij),
  c(F(z;{i,j,a}),(i,j,a))=1-q_(ij).
If active NORI antipodal-reversal oddness holds, the automatically implied reversed-middle formulas are
  c(F(z;{a,i,j}),(a,j,i))=q_(ij),
  c(F(z;{i,j,a}),(j,i,a))=1-q_(ij).
Hence absence of connectors with orientation (i,j) is already equivalent to global absence with BOTH inner orders, and q_(ij)=q_(ji).

PROOF. Fix z, let O=[n]\{i,j}, with |O|>=3. Absence means A_a(z)≠B_d(z) for every a,d∈O with a≠d. For any distinct a,a' choose d outside {a,a'}, possible because |O|>=3. Then A_a=A_a'=1-B_d. So all A_a(z) have one common bit q(z), and all B_d(z) have the complementary bit. Because A_a(z) is a physical ordered face whose free coordinates include a,i,j, it is unchanged by flipping ANY of those three coordinates in z. Since q(z)=A_a(z) for every a, toggling i or j leaves q fixed and toggling any other coordinate t leaves q fixed by selecting a=t. Thus q is constant on the connected full cube Q_n. Under active NORI, the antipodal reversal maps (a,i,j) to (j,i,a) and (i,j,a) to (a,j,i) on their antipodal faces; as z ranges the cube, each physical antipodal face occurs, so the two reversed-middle formulas follow. QED.

**THEOREM 2 (global absence graph).** Let M be the graph on the n coordinate directions whose edges are globally absent unordered middle pairs. Under active NORI, M has maximum degree at most TWO; every cycle in M is EVEN. More precisely assign each e={i,j} its invariant binary signature q_e from Theorem1. Whenever two edges e,f of M meet at a direction, their signatures must be OPPOSITE:
   q_e XOR q_f =1.
Therefore components of M are vertex-disjoint PATHS and EVEN CYCLES (including isolated vertices/edges). In particular |E(M)|<=n, and AT LEAST
   C(n,2)-n
unordered direction pairs appear as the middle two directions of some ACTUAL monochromatic 4-edge geodesic somewhere in Q_n. For each individual direction i there are at most TWO partner directions j never certified anywhere.

PROOF. Take incident edges {i,j},{i,k}, with distinct j,k. Examine actual ordered physical face (j,i,k) through any hub z. Absence of pair {i,j} gives c(j,i,k)=1-q_{ij}; absence of pair {i,k} gives c(j,i,k)=q_{ik}. Thus q_{ik}=1-q_{ij}. Three incident absent edges would require three pairwise opposite binary signatures, impossible. Along a cycle consecutive signatures alternate, so odd cycles are impossible. Any finite graph maxdegree2 without odd cycles is disjoint union of paths and even cycles. Maxdegree2 yields |E(M)|<=n. QED.

**THEOREM 3 (sharp logical characterization / realizability).** Conversely, for any graph M on n coordinate directions consisting of disjoint paths and even cycles, there exists a corner-independent direction-order-only coloring h(i,j,k)∈{0,1}, obeying active reversal oddness h(k,j,i)=1-h(i,j,k), for which EVERY pair e∈E(M) is globally absent. (Other pairs may also be absent; no claim of exact equality of absence graph.)

PROOF. Assign edge signatures q_e alternately along each path/even cycle. For every e={i,j}∈M and outer a, prescribe the four order-type colors
  h(a,i,j)=h(a,j,i)=q_e,
  h(i,j,a)=h(j,i,a)=1-q_e.
These instructions are pairwise compatible: one directed triple may contain the same prescribed edge in positions (1,2) and another prescribed edge in positions (2,3) only when the edges share a direction. Their signatures are then opposite, giving exactly matching prescriptions (check orders (i,j,k) and (k,j,i), with remaining orders obtained by reversing). Every forced reversal pair has complementary colors. Complete the values of h arbitrarily on the remaining reversal pairs, always assigning complementary values to reversed triples. This defines a valid active NORI coloring c(F,pi)=h(pi), independent of the exterior face bits. For every e in M, its fixed q_e patterns make all centered four-edge paths with that middle pair have unequal adjacent window colors at every hub, so e is globally absent. QED.

**Significance.** The recent certified middle-square complex has link graphs with independence ≤4, but mere density alone does not rule out a single globally missing pair (as in the documented index-one no-go square complex Y_(i,j)). The present theorem characterizes exactly how a PAIR can fail everywhere and globally constrains ALL such failures to a bipartite degree-two collection. Thus actual NORI colorings have coherent physical-face restrictions not visible in arbitrary square-complex degree estimates. However even a single missing pair is realizable with active NORI oddness, so this theorem does NOT force second equivariant index or grand closure by itself. Additional compatibility of long geodesic witnesses is still needed.
