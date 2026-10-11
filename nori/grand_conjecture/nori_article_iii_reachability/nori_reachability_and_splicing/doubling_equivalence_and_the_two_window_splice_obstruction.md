# Doubling equivalence and the two-window splice obstruction

# What cube doubling does for ordered three-face colorings

## Established one-face theorem: Feder–Subi formulation and Leader–Long equivalence

**Historical attribution (literature, not an original NORI result).** Feder and Subi conjectured that every *arbitrary* binary coloring of the undirected edges of the cube has an antipodal *path* with at most one color change. Their conjecture did not require a shortest path: Tomás Feder and Carlos Subi, *On hypercube labellings and antipodal monochromatic paths*, Discrete Applied Mathematics **161** (2013), 1421–1426, DOI 10.1016/j.dam.2012.12.025. Imre Leader and Eoin Long proposed the corresponding **geodesic** strengthening and established the equivalence below: *Long geodesics in subgraphs of the cube*, Discrete Mathematics **326** (2014), 29–33, DOI 10.1016/j.disc.2014.02.013; Proposition 3.6 in arXiv:1301.2195v1, Proposition 4.6 in a later author version.

Write \(c_i(x)\) for the color of the physical (undirected) edge \(\{x,x\oplus e_i\}\), so \(c_i(x)=c_i(x\oplus e_i)\). An *antipodally odd* coloring satisfies \(c_i(\bar x)=1-c_i(x)\). Define \(A_n\) to mean that every antipodally odd binary physical-edge coloring of \(Q_n\) has a **monochromatic full antipodal geodesic**; define \(B_n\) to mean that every *arbitrary* binary physical-edge coloring of \(Q_n\) has a **full antipodal geodesic with at most one color change**.

**Theorem (Leader–Long, dimension-shift equivalence).** For all \(n\ge2\),
\[
 B_n\Longrightarrow A_n,\qquad A_{n+1}\Longrightarrow B_n.
\]
Consequently \((\forall n\, A_n)\) holds if and only if \((\forall n\, B_n)\). This theorem concerns ordinary physical edges (NORI1).

**Proof, including a concrete legal doubling.** Let \(c\) be any physical edge coloring of \(Q_n\), introduce an extra direction \(s\), and set
\[
 C_i(x,0)=c_i(x),\qquad
 C_i(x,1)=1-c_i(\bar x)\ (i\in[n]),\qquad
 C_s(x,t)=x_1. \tag{E1}
\]
The first two formulas are physical because \(c_i\) is independent of its own \(i\)-bit; the last is independent of the \(s\)-bit. Complementing all \(n+1\) coordinates interchanges the two \(i\)-facets and complements their colors; the \(s\)-edge colors also complement because \(x_1\) does. Thus \(C\) is an honest antipodally odd coloring of every physical edge in \(Q_{n+1}\).

Assume \(A_{n+1}\). Take a \(C\)-monochromatic full antipodal geodesic and reverse its traversal if needed so it crosses \(s\) from 0 to 1. Let \(L:x\to y\) be its lower-facet portion in original-coordinate directions \(U\), and \(R:y\to\bar x\) its upper-facet portion in directions \(V=[n]\setminus U\). Both carry one color \(q\). The original-coordinate antipodal image \(\bar R:\bar y\to x\) is colored \(1-q\) by the upper-facet formula in (E1). Concatenate the reversed paths \(L^{-1}:y\to x\), of color \(q\), and \(\bar R^{-1}:x\to\bar y\), of color \(1-q\). The resulting path \(y\to\bar y\) uses precisely the disjoint coordinate sets \(U,V\), each direction once, and changes color at most once. This proves \(B_n\); an empty segment creates no difficulty.

Conversely, assume \(B_n\) and let \(c\) itself be antipodally odd. Split a full one-switch antipodal geodesic from \(x\) to \(\bar x\) into a \(q\)-monochromatic first portion \(L:x\to y\) and a \((1-q)\)-monochromatic second portion \(R:y\to\bar x\). Antipodality makes \(\bar R:\bar y\to x\) \(q\)-monochromatic. Thus \(L^{-1}:y\to x\) followed by \(\bar R^{-1}:x\to\bar y\) is a monochromatic full antipodal geodesic, using each original direction once. This proves \(A_n\). \(\square\)

**Implication and strict boundary of transfer.** Solving the unrestricted NORI1 monochromatic full-geodesic conjecture in all dimensions is *equivalent* to solving the arbitrary-edge one-switch **geodesic** conjecture. The original Feder–Subi arbitrary-edge one-switch **path** conjecture is a separately stated, weaker goal. The direct argument relies on a single edge-color junction between two blocks. For ordered physical three-face colorings, two additional splice windows arise, and reversal of the ordered free triple matters. The counterexample and obstruction below rigorously explain why the one-face proof does not transfer verbatim.

Primary sources: https://arxiv.org/pdf/1301.2195 ; https://doi.org/10.1016/j.disc.2014.02.013 ; https://theory.stanford.edu/~tomas/antipod.pdf ; https://doi.org/10.1016/j.dam.2012.12.025

---

Let b be an arbitrary binary coloring of ordered three-faces in Q_n. Form Q_(n+1)=Q_n x {0,1} with new direction g. On faces omitting g, define C((F,0),pi)=b(F,pi) and C((F,1),pi)=1-b(bar F,rev pi). On g-containing ordered faces choose colors in arbitrary complementary antipodal-reversal pairs. Then C(bar E,rev pi)=1-C(E,pi), so this is the exact ordered-three-face analogue of the antipodally odd doubled edge coloring. The naive formula C((F,1),pi)=1-b(F,pi) generally violates NORI oddness: reversal of the ordered triple is mandatory.

LEMMA (two new splice windows). Suppose b is reversal-blind, meaning b(F,rev pi)=b(F,pi). Let an antipodal full geodesic in the doubled cube start in the lower facet, cross g once, and have a monochromatic C-word of color q. Let its pre-g direction list be U and its post-g list V, with starting lower vertex x and crossing vertex y (in Q_n coordinates). Complement every Q_n vertex of its upper-facet suffix, giving a directed path from bar y to x in direction order V; concatenate the original lower prefix x to y in direction order U. The resulting Q_n path from bar y to y is a full antipodal geodesic with order (V,U). Every triple completely inside V has b-color 1-q; every triple completely inside U has b-color q. The only unprescribed triples are the two windows straddling the V|U splice (or fewer when one block is short). Thus the decoded b-word has the form (1-q,...,1-q, z_1,z_2,q,...,q) and may have THREE color changes. When both long constant flanks exist it has at most one change exactly when (z_1,z_2) is NOT (q,1-q). The forbidden pair creates (1-q,q,1-q,q) with three changes.

For a general ordered b without reversal-blindness, an additional obstruction arises: the upper-facet induced color at order pi is 1-b(bar F,rev pi), whereas the decoded upper suffix requires b(bar F,pi). Thus the doubled monochromatic path need not even control its decoded suffix colors. Ordered-face reversal and the two splice windows are independent obstructions to the straightforward Feder-Subi/Norine equivalence argument.

SHARP EXAMPLE (dimension six). Partition six directions into marked m1,m2 and unmarked a1,a2,a3,a4. Define the reversal-even, position-independent coloring
b(F,(u,v,w))=1 iff v is unmarked and at least one of u,w is marked; otherwise b=0.
For every six-direction order its four b-window colors have at least two changes. Indeed if marker positions are i<j, then the color of the triple centered at position t (t=2,3,4,5) is (1-z_t)(z_(t-1) OR z_(t+1)), where z_s indicates a marked position. Up to reversing the six positions, the nine marker pairs and their four-bit words are
(1,2):0100; (1,3):1010; (1,4):1101; (1,5):1010; (1,6):1001; (2,3):0010; (2,4):0101; (2,5):0110; (3,4):1001.
Each has at least two changes.

Make the doubled C on Q_7 using the formula above; since b is reversal-even and position-independent, C=b in the lower facet and C=1-b in the upper facet. Consider the seven-direction order
(m1,a1,a2,g,a3,m2,a4)
from any chosen initial vertex with g-bit zero. Its first window (m1,a1,a2) is in the lower facet and has C-color 1. Its last window (a3,m2,a4) is in the upper facet and has C-color 1. Prescribe color 1 on the three intervening ordered faces with free triples (a1,a2,g), (a2,g,a3), (g,a3,m2) reached by the path, and color 0 on their antipodal reversals. These six ordered-face objects are pairwise distinct; complete all other g-face reversal pairs arbitrarily. This constructs a legitimate NORI-odd C with a MONOCHROMATIC seven-edge antipodal geodesic.

But its decoded Q_6 direction order is (a3,m2,a4,m1,a1,a2), with b-word (0,1,0,1), realizing all three changes. In fact no Q_6 full geodesic is one-change for b, by the marker-pair argument. Therefore a monochromatic doubled NORI geodesic does NOT imply an unrestricted one-change geodesic downstairs. The elementary doubling proof of the edge-color equivalence fails sharply for ordered three-face colors.

SCOPE. The example refutes the putative implication for this doubled coloring, and the unrestricted spanning one-change three-face statement is already false in Q_6. It does not settle whether every NORI-odd three-face coloring has a monochromatic antipodal geodesic. The all-dimensional NORI one-change conjecture remains separate.

---

# Exact antipodal pairing of facet one-change geodesics

Let c be an antipodal-reversal-odd ordered-three-face coloring of Q_(n+1), and let H_0,H_1 be opposite n-facets normal to direction g. If a full n-edge geodesic P inside H_0 has direction order p=(p_1,...,p_n) and ordered-three-face color word w=(w_1,...,w_(n-2)), its antipodal reversal J(P) in H_1 has direction order rev(p) and color word
J(w)=(1-w_(n-2),...,1-w_1).
This is immediate from the defining NORI oddness involution, applied to each ordered face.

In particular, if w=0^r 1^s has one change then J(w)=0^s 1^r still has one change (the change orientation remains 0-to-1); likewise if w=1^r 0^s, the dual is 1^s 0^r. Hence antipodal face symmetry by itself preserves the number of changes; it does NOT turn a one-change facet geodesic into a monochromatic geodesic in the opposite facet.

EXACT ENDPOINT EXTENSION CRITERION. Suppose P has exactly one change and appending the as-yet-unused direction g produces a full (n+1)-edge geodesic P*g. Let beta be the color of its one new ordered-three-face window (p_(n-1),p_n,g), taken at the actual face. Then P*g is one-change if and only if beta=w_(n-2), the terminal old-window color. Otherwise it has exactly two changes. The antipodal reversal J(P*g), which begins with g and follows J(P), has exactly the same number of changes: its word is the reversed complement of (w,beta). Therefore passing to the antipodal partner duplicates this endpoint match/mismatch without resolving it.

This identifies a concrete induction invariant: seek one-change facet geodesics with *terminal extension compatibility* for at least one omitted direction g, or prove a witness-exchange operation forcing compatibility among candidate paths. Pairing a single path with its antipodal dual is insufficient. Any stronger argument must compare genuinely different facet geodesics, change their endpoints, or exploit additional face overlaps.

The result is elementary, requires no information about colorings outside the chosen path and its dual, and applies to any n>=4 for which two or more face windows occur.

---

SHARED-TAIL TERMINAL EXCHANGE. Let c be any binary ordered-three-face coloring of Q_(n+1). Fix an n-dimensional facet normal to g. Suppose P and P' are two full n-edge geodesics in the facet, each with exactly one color change. Assume they share the same final vertex y and the same ordered last two directions (a,b), and that their final three-face colors are different. Then one of P*g or P'*g is a full antipodal geodesic with at most one change. PROOF. The added last window in both extensions is the identical ordered three-face with free-direction order (a,b,g) and exterior bits prescribed by their common endpoint y. It therefore has one common color beta. Exactly one of the two old terminal colors equals beta, so appending g adds zero changes to that geodesic. QED. More generally it is enough that the extensions use the same final ordered three-face and the old terminal colors differ. This is an exact sufficient condition with no antipodal symmetry hypothesis. For NORI induction the open obligation is to create two such compatible one-change facet witnesses by exchanging directions or changing the path. Antipodal reversal preserves extension mismatch and does not itself create the needed pair.

## Recent witness refinement

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
