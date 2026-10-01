# The radius-three deficient-support graph has no closed degree-two component and bounded degree-two corridors

## Statement

In the order-thirteen mu=6 shell, let Gamma be the Johnson-radius-three graph on deficient seven-supports. Gamma has no 2-regular connected component. More quantitatively, there is no simple path R_0,...,R_8 whose internal vertices R_1,...,R_7 all have Gamma-degree two. Hence every maximal chain of degree-two states contains at most six degree-two vertices and is bracketed by degree-at-least-three expansion states. The proof first excludes 3-,4-,5-cycles in the sliding-triple model, then eliminates all longer 2-regular cycles by forcing period three, and finally applies the same odd-neighbor/transfer-clique mechanism at two deep vertices of a hypothetical long degree-two path.

## Body

# The radius-three deficient-support graph has no closed degree-two component and bounded degree-two corridors

Work in the order-thirteen mu=6 shell. Let Gamma be the graph on deficient seven-supports, with adjacency at Johnson distance at most three. We use the certified sliding-triple description of degree-two configurations, the exact odd-graph exchange model, degree-two rigidity, and the single-transfer clique theorem.

## Short 2-regular cycles do not occur

Suppose a 2-regular component is a cycle
R_0,...,R_{m-1},
with Hamiltonian complements
S_i=V(H)-R_i=T_{i-1} disjoint-union T_i,
where every three consecutive T-sets are pairwise disjoint.

For m=3, the triples T_0,T_1,T_2 are pairwise disjoint and leave a four-set
C=V(H)-(T_0 union T_1 union T_2).
Fix c in C. Odd-graph edge-label surjectivity gives disjoint Hamiltonian six-sets A,B with
A union B=V(H)-{c}.
One endpoint, say A, meets S_0 in at least three vertices, so d_J(A,S_0)<=3. Since the Gamma-component of R_0 is the 3-cycle, A must equal one of S_0,S_1,S_2. Then the other endpoint B has the form
(C-{c}) union T_{j+1}
for some j, and satisfies d_J(B,S_{j+1})=3. Its deficient complement is therefore an extra Gamma-neighbor of R_{j+1}, contradicting degree two.

For m=4, the four triples are pairwise disjoint and use twelve vertices; let c be the remaining vertex. For every i,
R_i={c} disjoint-union S_{i+2}.
The sliding-triple theorem supplies Hamiltonian deletions for every vertex of S_{i+2}, and deleting c leaves exactly S_{i+2}, also Hamiltonian. Thus every one of the seven vertices of R_i is Hamilton-removable. The single-transfer theorem gives a K_7 in Gamma, and the transfer at c is R_{i+2}; hence R_{i+2} has degree at least six, contradicting 2-regularity.

For m=5, cyclic distance at most two makes all five order-three T-sets pairwise disjoint, requiring fifteen vertices. So m=5 is impossible.

Thus any hypothetical 2-regular component has length at least six.

## No 2-regular component exists

Assume now a 2-regular cycle of length m>=6. Fix i and let B be any Hamiltonian six-set disjoint from S_i, with odd-edge label c, so
S_i disjoint-union B=V(H)-{c}.

We claim B must itself be one of the cycle supports. Otherwise, for every cycle support S_k we have |B intersect S_k|<=2; if some intersection had size at least three, the deficient complement of B would be a Gamma-neighbor of the degree-two state R_k and therefore would have to be one of its two cycle neighbors.

Hence
|S_k intersect (S_i union {c})|>=4
for every k. For any nonlocal k notin {i-1,i,i+1}, if c were not in S_k then |S_k intersect S_i|>=4, giving d_J(S_k,S_i)<=2 and a forbidden chord of the cycle. Therefore c lies in every nonlocal S_k.

Since m>=6, the three consecutive supports S_{i+2},S_{i+3},S_{i+4} are all nonlocal. Thus
c in S_{i+2} intersect S_{i+3}
and
c in S_{i+3} intersect S_{i+4}.
But adjacent support intersections are
S_j intersect S_{j+1}=T_j,
so c lies in both T_{i+2} and T_{i+3}, contradicting disjointness of consecutive T-sets. The claim follows.

Now the sliding-triple theorem gives at least three Hamiltonian deletion labels for every R_i, so S_i has an odd-graph neighbor. By the claim that neighbor is a cycle support disjoint from S_i. The single-transfer clique theorem inside a 2-regular component then forces
deg_G(S_i)=3
and, because both T_{i-2} and T_{i+1} are three-sets of Hamiltonian deletion labels,
T_{i-2}=T_{i+1}.
Hence
T_{i+3}=T_i
for every i.

If 3 does not divide m, repeated addition of three modulo m runs through every index, forcing all T_i equal and contradicting disjointness of consecutive triples. If 3 divides m, then m>=6 and
S_{i+3}=T_{i+2} disjoint-union T_{i+3}
       =T_{i-1} disjoint-union T_i
       =S_i,
so R_{i+3}=R_i, contradicting simplicity of the cycle.

Therefore Gamma has no 2-regular connected component.

## Long degree-two corridors are impossible

Suppose for contradiction that
R_0,R_1,...,R_8
is a simple Gamma-path with
deg_Gamma(R_j)=2
for j=1,...,7.
Let S_j=V(H)-R_j. Degree-two rigidity makes every path edge have Johnson distance three. Put
A_j=R_j-R_{j+1},
B_j=R_{j+1}-R_j;
all are three-sets.

At a degree-two state, the two acquired triples from its neighbors partition the complementary Hamiltonian support. Hence
S_j=A_{j-1} disjoint-union B_j
for 1<=j<=7.
Reversing the swap across R_jR_{j+1} gives
S_{j+1}=A_{j-1} disjoint-union A_j.
Comparing with the degree-two decomposition at R_{j+1} yields
B_{j+1}=A_{j-1}.
Thus, for 2<=j<=8,
S_j=A_{j-2} disjoint-union A_{j-1},
and every three consecutive A-sets are pairwise disjoint. In particular
S_k intersect S_{k+1}=A_{k-1}
for k=1,...,7.

We next show that every odd-graph neighbor of the deep support S_5 is one of the displayed path supports S_0,...,S_8. Let C be Hamiltonian and disjoint from S_5, with omitted label c:
S_5 disjoint-union C=V(H)-{c}.
If C were not a path support, then for k=1,2,3 we would have |C intersect S_k|<=2, because otherwise the deficient complement of C would be an extra Gamma-neighbor of the degree-two state R_k. Hence
|S_k intersect (S_5 union {c})|>=4.
The indices 1,2,3 are nonlocal to 5, so avoiding a forbidden chord forces
c in S_1 intersect S_2 intersect S_3.
But
S_1 intersect S_2=A_0
and
S_2 intersect S_3=A_1,
so c lies in A_0 intersect A_1, contradicting their disjointness. Thus every odd neighbor of S_5 is a path support. The identical argument with nonlocal states R_2,R_3,R_4 shows the same for S_6.

Degree-two rigidity around R_5 supplies the three-set A_2 from the left and A_5 from the right as Hamiltonian deletion labels of R_5, so deg_G(S_5)>=3. Since every odd neighbor of S_5 is a path support and at most S_0,S_8 have complements of unknown Gamma-degree, one odd neighbor has a degree-two complement. The single-transfer clique theorem then gives
deg_G(S_5)<=3.
Therefore deg_G(S_5)=3 and the two three-sets of deletion labels coincide:
A_2=A_5.

Applying the same argument at R_6 gives
A_3=A_6.

Consequently
S_4=A_2 disjoint-union A_3
   =A_5 disjoint-union A_6
   =S_7,
hence R_4=R_7, contradicting simplicity of the path.

So no such nine-vertex path exists.

Combining the two conclusions, every maximal degree-two corridor in Gamma is finite, contains at most six degree-two vertices, and is bracketed by states of degree at least three. Expansion is therefore not merely eventual: from a degree-two state, nonbacktracking traversal reaches a genuine expansion state after uniformly bounded distance.
