# All-dimensional edge-geodesic closure for 2-junta antipodally odd colorings and arbitrary prescribed direction-color words

# Complete monochromatic antipodal-geodesic closure for functional-dependence edge colorings

**Setting and scope.** Let n>=2. Color the actual undirected edges of Q_n by a binary function c, with c({x,x xor e_i})=:c_i(x). Assume each direction-i edge color depends on EXACTLY ONE OTHER coordinate: for some function j:[n]->[n] without fixed points and arbitrary bits b_i,
  c_i(x) = x_(j(i)) xor b_i.
Because j(i)!=i, this is a well-defined UNDIRECTED physical edge color (independent of x_i). Complementing all physical bits flips x_(j(i)), so c_i(bar x)=1-c_i(x). Thus the active k=1 antipodally odd edge-color hypothesis is satisfied in every dimension.

**THEOREM (universal realization of arbitrary direction-indexed edge-color words).** For EVERY prescribed bit vector t=(t_1,...,t_n) in F2^n, there exist a physical root x in Q_n and a permutation p of ALL n distinct directions such that the genuine full antipodal n-edge geodesic starting at x in order p has color t_i on its UNIQUE edge of direction i. In particular, take all t_i=0 to obtain a monochromatic antipodal geodesic of color zero. Taking all t_i=1 likewise works; these two witnesses are also exchanged under antipodality.

**Proof.**
(1) For any root x and full direction order p, the direction-i edge is traversed after precisely the directions preceding i in p have been flipped. Its actual physical color is
  C_i(x,p)=x_(j(i)) xor b_i xor 1{j(i) appears BEFORE i in p}.       (*)
Set a desired auxiliary bit q_i:=b_i xor t_i. The equations C_i=t_i are therefore equivalent to
  x_(j(i)) = q_i xor 1{j(i) precedes i in p}.                        (**)
(2) Consider the directed functional graph with an arrow i->j(i) for each i. Because every vertex has one outgoing arrow and no loop, each weak connected component consists of one directed cycle of length at least two, with rooted in-trees attached to its cycle vertices; a two-cycle may be represented by two opposite arrows on the same undirected pair.
(3) We construct a strict total order p together with arbitrary root bits x_j satisfying (**). On EACH directed cycle, choose any strict total ordering of the cycle's vertices. For a cycle vertex j, let i be its UNIQUE predecessor on the directed cycle (i.e. j(i)=j on the cycle), and DEFINE
  x_j := q_i xor 1{j precedes i in the chosen cycle order}.
This ensures the equation (**) for EVERY cycle arrow, with an orientation compatible with that chosen strict cycle order. For every NON-CYCLE vertex j, choose x_j arbitrarily (say zero).
(4) For each TREE arrow i->j(i)=j, impose the following ordering relation on its two ends:
  j precedes i  iff  x_j xor q_i = 1;
  i precedes j  iff  x_j xor q_i = 0.
This is an ordinary strict precedence constraint on a single undirected tree edge. The cycle-arrow constraints are consistent with the initially chosen total order of cycle vertices. Because all OTHER underlying edges form trees attached to those cycles, adding their arbitrary orientations creates NO directed precedence cycle. Indeed any directed cycle must be supported by an undirected cycle; every component has only the original cycle (or a two-arrow cycle) and its arcs were oriented consistently with a strict total order. Thus the finite precedence relation is ACYCLIC.
(5) Choose any topological ordering p of this acyclic precedence digraph. Its relative order on every functional arrow i->j is exactly the orientation chosen above, hence equation (**) holds for every i. Substituting into (*) yields C_i(x,p)=t_i for every direction i. The path flips each direction exactly once, so it is a GENUINE full antipodal geodesic. QED.

**Strength and separation from previously known rank arguments.**
Write c_i(x)=b_i+sum_j A_(ij)x_j over F2. The above class has exactly ONE nonzero entry in every row of A, in column j(i); every row sums to one and diagonal entries are zero. Its rank equals the number of DISTINCT coordinates in the image of j, which can be AS SMALL AS TWO for n>=3: take j(1)=2 and j(i)=1 for every i>=2. This yields rank(A)=2 and arbitrarily large corank n-2, beyond the previously saved k=1 affine corank-one closure result nori_k1_affine_corank_one_closure. Moreover the result realizes EVERY prescribed direction-indexed edge-color vector, not only constant words or <=1-switch sequences.

**Algorithm.** Find functional directed cycles and their in-trees in linear time O(n); choose a total order for each cycle; assign x to satisfy cycle arrows; orient every tree edge by the displayed rule; topologically sort (linear time); return root x and permutation p. No search over 2^n roots or n! orders is required.

**Exact open boundary.** The proof crucially uses that every edge-color equation depends on ONE root bit. For general antipodally odd affine edge colorings c_i(x)=b_i+sum_j A_ij x_j (each row having an odd number of nonzero exterior coefficients), the simultaneous support dependencies form a hypergraph and the tree orientations no longer decouple. Corank-one and nonsingular matrices are already solved separately. A possible next generalization is to identify sparse directed hypergraph classes where variable elimination plus acyclic ordering works. Unrestricted arbitrary (nonaffine) odd edge coloring and active ordered-three-face NORI remain open.

**Corollary (every antipodally odd edge 2-junta coloring closes in all dimensions).** Suppose, for EACH direction i, the actual physical edge color c_i(x) depends globally on AT MOST TWO of the other n−1 vertex coordinate bits, with the relevant set permitted to depend on i. Assume c_i(bar x)=1−c_i(x). Then every direction-i function is necessarily a projection or complemented projection onto ONE exterior coordinate: c_i(x)=x_(j(i)) xor b_i. Hence the theorem applies, realizing any prescribed full direction-indexed color vector and in particular a monochromatic antipodal geodesic.

Proof. An anti-complementary Boolean function g on ONE input obeys g(1−u)=1−g(u), so g(u)=u or 1−u. For a function g of TWO bits, the four values are determined by g(0,0)=a and g(0,1)=b, since g(1,1)=1−a and g(1,0)=1−b. If a=b then g depends only on the FIRST bit; if a!=b it depends only on the SECOND bit. A constant zero-input function is incompatible with antipodal oddness. Thus any <=2-junta satisfying oddness collapses to a single-bit projection, and the theorem completes the proof. QED.

**First genuine nonlinear frontier.** A coordinate-edge color must depend on at least THREE other cube-coordinate bits to be a genuinely nonlinear antipodally odd Boolean function. For example, majority of three exterior bits obeys f(bar y)=1−f(y) and depends essentially on all three. This identifies 3-junta antipodally odd edge colorings as the first subclass outside both the present elementary functional-digraph theorem and arbitrary affine linear-algebra closure. This does not assert that all 3-juntas are hard: affine parity of three exterior bits may already be covered by rank-based criteria.


**Exact classification of the first nonlinear three-bit edge functions.** A Boolean function f:{0,1}^3->{0,1} obeying f(bar u)=1−f(u) has 2^4=16 possibilities, since each of four antipodal input pairs contributes one independent value. Exactly EIGHT are affine (a parity of either one or all three variables, plus optional global complement). The remaining EIGHT are the functions
  f(u_1,u_2,u_3)=majority(u_1 xor s_1,u_2 xor s_2,u_3 xor s_3),
  (s_1,s_2,s_3)∈{0,1}^3.
These are distinct self-dual nonlinear functions. To verify: majority of three binary bits is self-dual and nonlinear, independent signed input flips preserve both properties, and the 8 choices are distinct; counting completes the classification. Consequently the first genuinely nonlinear edge-junta case is exactly signed three-input majority. Any 3-junta k=1 theorem can focus on how such majority gates couple across directions and may use the affine-row results for parity gates.

**Position in the program.** This is a genuine all-dimensional solved subclass of the ORIGINAL edge-color Norine conjecture, separate from ordered-three-face NORI. The algorithm constructs a single full good path and therefore certifies the exact uncolored antipodal-reachability overlap R(x)∩bar(R(x)) directly. It does not by itself transfer through the two seam windows of active ordered-three-face NORI.
