# Article III — Monochromatic reachability and antipodal splicing

## Article synopsis and main argument

# Complementary reachability and antipodal extraction

Let c be a reversal-odd coloring of ordered physical three-faces of Q_n. A geodesic of length k has k-2 consecutive ordered-window colors. It is monochromatic when this word is constant, and good when the word changes at most once. The central question is to extract a full good path from two genuinely monochromatic branches whose coordinate supports are complementary.

## Reversed-two-tail criterion

Fix an ordered terminal pair J=(a,b) and D=[n] without {a,b}. For a cube root x, define R_J(x) as the family of supports U subset D for which some monochromatic direction-distinct path starts at x, uses precisely U and then the final ordered directions (a,b). The monochromatic color is existential. The exact reversed-tail extraction theorem states that a complementary pair U in R_(a,b)(x) and D without U in R_(b,a)(x), from the same root, yields a full antipodal geodesic with at most one change.

The physical terminal order matters. Ordinary concatenation of arbitrary monochromatic three-window paths creates two new ordered windows at the seam, and the colors of those windows are not determined by the two interior monochromatic colors. In the reversed-two-tail construction, the actual common root, complementary supports, and reversed terminal pairs provide the special face identifications that make extraction valid. Thus a topological coincidence of support labels is useful precisely when it retains these data.

## Accessibility and state carriers

For an undirected edge coloring, let E_q(x,S) assert existence of a q-monochromatic geodesic from x with direction support S. For nonempty S, deleting its first direction proves

E_q(x,S) iff there exists a in S such that c({x,x xor e_a})=q and E_q(x xor e_a,S without {a}).

The converse prepends the edge. The union E_0 union E_1 is accessible under deletion of at least one direction, but need not be a Boolean downset. Its collision with the same-root complementary-support transform is equivalent to a one-switch antipodal edge geodesic. Under antipodal oddness, the standard rotation converts such an existential one-switch edge witness into a monochromatic antipodal witness.

Root-endpoint states (x,y), ranked by the number of differing coordinates, admit covers by extending either endpoint in an unused direction. Every monochromatic cover-chain from a diagonal state is an actual monochromatic geodesic. Coordinatewise the order complex is a circle, so the full state complex triangulates an n-torus, with restricted equivariant index. Barycentric reachability carriers also encode exact targets: the center of the support face D lies in the simplex complex genuinely witnessed by q-paths from x exactly when x can reach x xor D monochromatically. Nestedness forces the carrier simplex to contain both empty and D supports.

## Signed profile topology

For NORI use label pairs (J,U), and let the involution send (J,U) to (rev J,D without U). At each root x retain only labels of actual monochromatic witnesses. Their signed nerve has two complete shores because every three-edge path is automatically monochromatic. Mixed shore intersections at distinct roots can form equivariant four-cycles even under failure of the grand conjecture. The missing same-root diagonals are exactly the desired complementary-terminal coincidences.

A reduced two-ended path memory records the two endpoints, first and last direction pairs, and switch-state information. At rank six distinct histories can share one such memory state, so a quotient-level intersection must be lifted using actual seams and roots. This identifies the exact gap: a topological theorem must force a diagonal signed-root intersection with complementary reversed terminal memory, rather than a generic equivariant label coincidence.

## Doubling, complementary reachability, and geodesic splicing

# Complementary monochromatic reachability and two-window splicing

Write \(c(F,\pi)\in\mathbb F_2\) for an antipodal-reversal-odd coloring of physical ordered three-faces of \(Q_n\), so \(c(\bar F,\operatorname{rev}\pi)=1+c(F,\pi)\). Any directed geodesic has its actual consecutive three-face colors. A monochromatic directed geodesic is one whose entire window word has a constant bit, of either color. The difficulty with joining arbitrary monochromatic branches is that their junction creates two new ordered-three-face windows.

## The exact two-tail extraction theorem

For two distinct directions \(a,b\), let \(D=[n]\setminus\{a,b\}\). Define the *color-free terminal reachability family*
\[
\mathcal R_{(a,b)}(x)=\left\{U\subseteq D,\ |U|\ge1:
\begin{array}{l}
\exists\text{ a monochromatic directed geodesic from }x\\
\text{with direction order }(u_1,\ldots,u_s,a,b),\\
\{u_1,\ldots,u_s\}=U
\end{array}\right\}.
\]
The monochromatic bit is deliberately forgotten; the ordered two-direction terminal memory is retained.

**Theorem 1 (exact grand equivalence).** A full antipodal geodesic with at most one ordered-three-face color change exists if and only if for some common root \(x\), some ordered pair \((a,b)\), and nonempty complementary supports \(U,V\subseteq D\),
\[
U\sqcup V=D,\qquad
U\in\mathcal R_{(a,b)}(x),\quad
V\in\mathcal R_{(b,a)}(x).
\tag{1}
\]

**Proof.** Suppose (1) holds, and choose two monochromatic \(x\)-rooted witnesses with direction words
\[
A=(u_1,\ldots,u_s,a,b),\qquad
B=(v_1,\ldots,v_t,b,a),
\]
of colors \(q,r\), respectively. Antipodal reversal of \(B\) begins at
\[
\overline{x\oplus(V\cup\{a,b\})}=x\oplus U,
\]
has direction word \((a,b,v_t,\ldots,v_1)\), and has all window colors \(1+r\). Retain the first \(s\) moves of \(A\), ending at \(x\oplus U\), and then follow this reversed \(B\). The concatenation is a full path changing each coordinate once. Its first \(s\) ordered-face windows are precisely those of \(A\), and its last \(t\) are precisely those of the reversed \(B\). Since \(s+t=n-2\), these blocks exhaust every window and have word \(q^s(1+r)^t\), containing at most one change.

Conversely, let \(P\) be a good full order \((p_1,\ldots,p_n)\) from root \(x\). Choose a cut between positions \(s\) and \(s+1\) in the \(n-2\) window word where both nonempty sides are constant; if \(P\) is monochromatic any interior cut works. Set \(a=p_{s+1},b=p_{s+2}\), \(U=\{p_1,\ldots,p_s\}\), and \(V=\{p_{s+3},\ldots,p_n\}\). The initial \((s+2)\)-move subpath with terminal directions \((a,b)\) is monochromatic, witnessing \(U\in\mathcal R_{(a,b)}(x)\). Reversing and antipodally complementing the terminal subpath gives an \(x\)-rooted monochromatic witness ending in \((b,a)\) with support \(V\). These supports are nonempty, disjoint, and complementary. \(\square\)

The proof works for ordered \(k\)-faces with a common terminal memory of \(k-1\) directions. The two-tail overlap (1) is therefore a faithful, color-free target for a topological or combinatorial proof of NORI.

## Why direct cube doubling requires care

Let \(b\) be any binary coloring of ordered three-faces of \(Q_n\), and introduce a new coordinate \(g\). On faces omitting \(g\), color the lower facet by \(b(F,\pi)\) and the upper by
\[
1+b(\bar F,\operatorname{rev}\pi).
\]
Choose values on \(g\)-containing faces in complementary antipodal-reversal pairs. This defines a legal NORI coloring of \(Q_{n+1}\). The reversal and physical complementation in the upper formula are both necessary.

Suppose \(b\) is reversal-blind, \(b(F,\operatorname{rev}\pi)=b(F,\pi)\), and a monochromatic full doubled geodesic crosses \(g\) once. After decoding its lower and upper portions into a full path in \(Q_n\), the windows lying completely on the two sides have constant complementary colors. At their splice exactly two three-direction windows remain uncontrolled. With long flanks the resulting word may be
\[
(1+q)^{\,t},z_1,z_2,q^{\,s},
\]
which can have three changes, for example when \((z_1,z_2)=(q,1+q)\). Without reversal-blindness even the decoded upper-flank colors need not be controlled. Thus the direct edge-color doubling argument does not automatically establish the ordered-three-face NORI conjecture. This is a precise two-window obstruction, not a counterexample to the grand assertion.

## Codimension-two cap rigidity

Fix a set \(U\) of \(n-2\) directions, with omitted directions \(a,b\), and a projected root \(r\) on \(U\). For \(i\in U\) define physical cap bits
\[
A_i=c(F(r;\{a,b,i\}),(a,b,i)),\qquad
B_i=c(F(r;\{a,b,i\}),(b,a,i)).
\]
Because \(a,b\) are free on those physical faces, these bits are the same across the four parallel \(U\)-facets.

If a monochromatic \(U\)-spanning geodesic of color \(q\) begins with direction \(i\) and ends with \(j\), inspect completions by placing the two missing directions in either order at the beginning or end. Under hypothetical failure of grand closure, all these completions must fail. The first cap must then be stable and agree with \(q\): \(A_i=B_i=q\); the terminal cap must be stable and opposite: \(A_j=B_j=1+q\). Otherwise one of the full completions has at most one change. Accordingly, the *color-free* graph on \(U\) whose edges join witnessed first and last directions in any of the four facets must be bipartite across the stable cap classes. An odd cycle or an unstable incident direction certifies grand closure.

This cap criterion is a positive extraction theorem conditional on near-spanning monochromatic witnesses. Such witnesses need not exist in a prescribed \(U\)-facet; valid NORI colorings can make the whole four-facet near-spanning memory graph empty. Hence a global proof must force either the complementary two-tail reachability coincidence (1) or sufficiently rich compatible near-spanning cores. Current local cap rigidity does not furnish that existence theorem.\n\n## Refined physical reachability\n\nThe exact two-tail closure criterion requires a common root, complementary used-direction supports, and reversed terminal two-direction memories. Monochromatic basin convexity or a Tucker label collision without those witnesses is insufficient. The new subsections establish maximal support bounds, barycentric carrier obstructions, root-profile interface conditions, and exact codimension-two cap compatibilities under this same physical extraction requirement.

### Doubling equivalence and the two-window splice obstruction

# What cube doubling does for ordered three-face colorings

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


### Exact target reachability and antipodal intersection extraction

# Exact target reachability and antipodal intersection extraction

For a fixed root, monochromatic geodesic reachability records genuine terminal vertices together with the path support. Antipodal overlap of this color-free set has a direct gluing meaning in the classical edge setting, and analogous target-pair criteria exist for physical ordered faces only when sufficient terminal-memory data is kept.

## Antipodal reachable-target labels: exact support/face intersection formulation (edge analogue)

Fix an antipodally odd undirected binary edge coloring c of Q_n. For q in {0,1}, let R_q(x) be the set of physical cube vertices z connected to x by a monochromatic q-geodesic (including the empty path); let F_q(x)={S subseteq [n] : x XOR S in R_q(x)}.

**Theorem 1: exact target coincidence.** The following are equivalent:
(1) There exists a monochromatic antipodal geodesic.
(2) There exist x, q,r, and an actual cube vertex z in R_q(x) intersect R_r(bar x).
(3) There exist x,q,r and exact reachable direction supports S in F_q(x), T in F_r(bar x) satisfying T=[n]\S.
(4) For some x and q, R_q(x) contains an antipodal pair z,bar z.
(5) For some x and q, F_q(x) contains complementary subsets S,[n]\S.

Proof: For (2), concatenate the q-geodesic x->z with the reverse of the r-geodesic bar x->z. For each coordinate exactly one branch uses it, so the concatenation is a full antipodal geodesic with zero/one change. If r!=q, cyclically rotate the path at z by appending the antipodal image of its first monochromatic block after the second; oddness makes both resulting blocks color r, giving a monochromatic antipodal geodesic. The converse picks z=x on an existing monochromatic antipodal geodesic. (3) is the exact equation x XOR S=bar x XOR T. For (4), reverse a q-geodesic x->z and follow a q-geodesic x->bar z; their direction supports are complementary, producing a q-geodesic z->bar z. Conversely any monochromatic antipodal geodesic witnesses (4) at its starting root. (5) translates (4) into supports. Moreover F_q(bar x)=F_(1-q)(x), R_q(bar x)=overline{R_(1-q)(x)}.

**Theorem 2: honest convex target labels.** Let V=Q_n, and let Delta^V be the simplex with one affinely independent basis vertex e_z for each *actual physical target* z in V. Associate to a root/color pair its reachable-target FACE
P_q(x)=conv{e_z : z in R_q(x)}.
Then P_q(x) intersects P_r(bar x) if and only if R_q(x) intersects R_r(bar x): two faces of an ordinary simplex intersect in exactly the face on their shared vertex labels. In particular, a BU/KKM/Sperner mechanism forcing intersection of these actual target faces gives an immediate monochromatic antipodal geodesic.

**Why this does not yet prove closure.** The honest simplex has dimension 2^n-1, much larger than the dimension n-1 of the local antipodal link spheres. Replacing e_z by the physical cube vectors z in R^n destroys the exact intersection property: in Q_2, conv{00,11} and conv{01,10} meet at (1/2,1/2) although the underlying vertex sets are disjoint. Thus equality of low-dimensional barycentric averages / coordinatewise reachability is not enough. One needs a coloring-sensitive carrier, a restricted face-Helly property, or a topological index argument respecting the full combinatorial target support.

**Labeling research program (not a proved topological theorem).** Give a state with antipodal root label x an *actual realizable witness* (q,S), meaning a q-monochromatic geodesic from x to x XOR S. Under the antipodal root involution the companion root is bar x. A successful topological coincidence must force labels S and [n]\S, or equivalently the same actual target z, and it must ensure both certificates refer to the same antipodal root pair. Construct local transition/carrier rules respecting jointly realizable entire geodesics; prove a specific antipodal-label/coincidence theorem from them. Arbitrary selections including the always-reachable empty support S=empty can avoid the desired coincidence, so ordinary equivariance alone cannot force it. The required additional hypothesis must come from growth, maximality, or color-consistent repairs. For ordered-three-face NORI, retain the user's shared physical-target idea as the outer target while adding a separate two-window seam certificate before final extraction.

## Fixed-target local-index no-go: sparse reachable cones in an antipodally odd coloring

For every even n>=4 take the antipodally odd exterior-parity edge coloring c_i(v)=sum_(j neq i) v_j mod2. Fix physical target z=0^n. Every edge incident with z is color zero. After traversing the first edge to e_j, each unused-direction edge e_j->e_j XOR e_i (i neq j) has color one. Therefore every monochromatic geodesic starting at z has length at most one. In the affine root-target fiber F_z,
K_0(z) is exactly the n-legged star of simplex edges from the diagonal root corner (z,empty support) to the n neighboring root corners; K_1(z) contains only its apex. The union K(z) is the same star.

Under beta simultaneous root and support complement, beta K(z) is the opposite n-legged star at the antipodal corner of F_z. For n>=4 the two stars have no common Boolean vertices (one uses roots of Hamming weight 0 or1, the other roots of weight n or n-1). In their common simplicial triangulation they are disjoint subcomplexes.

Nevertheless the coloring has a monochromatic antipodal geodesic: choose an initial root with n/2 zero-bits and n/2 one-bits and traverse the directions in an alternating zero/one pattern. By the direct color formula c_(p_k)=P(x) XOR(k-1) XOR x_(p_k), all traversed edges then have equal color.

Thus the antipodal S^(n-1) link of a SINGLE fixed-target fiber and the fact that its reachable sets contain all n one-step rays cannot, by themselves, force antipodal reachable-root coincidence. A forcing proof must choose the target globally, couple several target fibers through the actual colored-edge facet transport, or use a different genuinely color-dependent boundary condition. This provides an explicit obstruction to applying a fixed-target Borsuk--Ulam theorem without verifying its hypotheses, not a counterexample to the global conjecture.

## Near-complementary monochromatic branches: the one-coordinate completion law

Let \(Q_n\) have an antipodally odd binary UNDIRECTED edge coloring \(c(\bar e)=1-c(e)\). Let x be a root. Suppose two monochromatic geodesics \(P_S:x\to x\oplus S\) and \(P_T:x\to x\oplus T\) use DISJOINT coordinate supports, and
\[
S\cap T=\varnothing,\qquad S\cup T=[n]\setminus\{i\}.
\]
Thus the two paths form a geodesic from \(x\oplus S\) to \(x\oplus T\) of length n-1 through x, with a single missing direction i. Denote its two end-edges toward antipodal completion by
\[
e_S=\{x\oplus S,\overline{x\oplus T}\},\qquad
e_T=\{x\oplus T,\overline{x\oplus S}\}.
\]
They are antipodal edges and have complementary colors.

**Theorem (same-color case).** If \(P_S\) and \(P_T\) have the SAME monochromatic edge color q, then a monochromatic full antipodal geodesic exists. Precisely one of the two completion edges has color q. Appending that edge to its corresponding monochromatic branch from x reaches the antipode of the other branch's endpoint. Thus the uncolored region R(x) contains an antipodal pair and yields closure.

**Theorem (opposite-color case).** If the branch colors are q and \(1-q\), then the \((n-1)\)-geodesic through x has exactly one switch (assuming both paths have positive length). Its two full antipodal completions either BOTH have at most one switch or BOTH have two switches. The former occurs iff \(c(e_S)=q\), equivalently \(c(e_T)=1-q\). In the latter case \(c(e_S)=1-q\) and \(c(e_T)=q\). This isolates a SINGLE binary obstruction at the exposed coordinate i.

**Proof.** The disjointness of supports makes the two-arm concatenation a geodesic, and omission of only i makes both e_S and e_T legitimate geodesic endpoint extensions. The edges are antipodes because \(\overline{x\oplus S}=(x\oplus T)\oplus e_i\) and \(\overline{x\oplus T}=(x\oplus S)\oplus e_i\), so their colors are opposite. When branch colors match, precisely one edge extends the corresponding branch monochromatically; the new endpoint is antipodal to the other reachable branch endpoint. When colors differ, adding e_S before the q-block preserves one switch exactly when it has color q; adding e_T after the (1-q)-block preserves one switch exactly when it has color 1-q. The antipodal oddness makes these conditions equivalent. QED.

**Interpretation respecting COLOR-FREE R.** The main reachability set remains \(R(x)=R_0(x)\cup R_1(x)\), with no color specified in its topological labels. If two representatives of R(x) have disjoint supports covering n-1 coordinates, examining the EXISTENCE of same-color witnesses or the unique exposed bridge bit provides an exact extraction. Any reachability-label coincidence that forces same-color witnesses for such a near-partition immediately proves grand closure in the edge case. The full antipodal-support partition (covering n coordinates) already yields closure for arbitrary witness colors.

The distinction between a genuine reachable antipodal pair and an intersection of convex or simplicial relaxations is indispensable. Only the former supplies the compatible geodesic witnesses needed for extraction.

### Codimension-two reachability facets and terminal cap rigidity

# Codimension-two reachability facets and terminal cap rigidity

Consider path families occupying a codimension-two coordinate facet while two exterior directions remain available for completion. The terminal ordered-pair memory determines the colors of the first and last newly formed windows. This gives an exact cap-compatibility problem, together with missing-facet and isoperimetric restrictions if global closure is assumed to fail.

## Target-fiber carrier transport along a colored physical edge

In the ordinary edge-colored hypercube, write A_q(z)={r in Q_n : there exists a monochromatic q-geodesic from r to z}; by reversing the path, A_q(z) is also the q-geodesic reachability star rooted at z. For each physical target z, let K_q(z) be the union of all witnessed monochromatic q prefix-chain simplices on its affine root-target fiber F_z, identified with the r-cube and triangulated by relative support S=r XOR z.

**Theorem (two-sided facet nesting).** If i in [n], z'=z XOR e_i, and c({z,z'})=q, then
(1) A_q(z) intersect {r:r_i=z_i} subseteq A_q(z') intersect {r:r_i=z_i};
(2) A_q(z') intersect {r:r_i=z_i'} subseteq A_q(z) intersect {r:r_i=z_i'}.
Both inclusions hold with witness-compatible SIMPLEX carriers, not only pointwise reachable root labels: the identity correspondence on physical root vertices maps each q-monochromatic-prefix simplex on the specified facet of F_z to a simplex of K_q(z') in (1), and symmetrically from F_z' to F_z in (2).

Proof. For (1), any q-geodesic z->r with r_i=z_i never traverses i. Prefix it by the q-colored edge z'->z. Since i was unused in the old geodesic, the resulting path z'->z->r is a q-monochromatic geodesic (its length is d(z',r)=d(z,r)+1). On relative supports its nested prefix chain S_0 subset ... subset S_k, all avoiding i, becomes the actual prefix chain {i} subset {i} union S_0 subset ... subset {i} union S_k from root z', so the image of every old chain simplex is a witnessed face in K_q(z'). The root-label identity sends the Boolean corner (r,r XOR z) in F_z to (r,r XOR z') in F_z', and preserves inclusions as claimed. The reverse statement (2) is the same argument with z and z' interchanged.

**Interpretation as face-local monotonicity.** Across a physical q-colored target edge, the q-reachable-root region expands from target z into z' on the root facet r_i=z_i and expands from target z' into z on the opposite facet r_i=z_i'. Because every physical edge has one of the two colors, each neighboring pair of target fibers has a precisely specified two-sided carrier inclusion for that color. Antipodal oddness makes the analogous opposite-target edge colored 1-q. These constraints couple otherwise independent target fibers and are much stronger than requiring each reachability set to contain the target root and its one-step neighbors.

**Exact topological objective.** Establish an n-dimensional cubical KKM/Hex/Tucker intersection theorem for the families K_0(z),K_1(z) satisfying these facet transfers, full path-prefix coherence, and physical-edge antipodal color oddness. The required conclusion is a Boolean corner (r,r XOR z) in K_q(z) and its beta-antipode (bar r, bar r XOR z) in K_p(z) for some z and colors q,p. Such a collision is an actual monochromatic antipodal geodesic certificate. The carrier inclusions above are proved; a topological forcing theorem from them is still OPEN. The geometric crossings F_z intersect F_z' at fractional points and do not themselves count as collisions.

For ordered-three-face NORI, extending a path across the first two edges does not yet create a colored three-window; an analogous carrier theorem must be formulated on the exact two-ended finite-memory path-state lift, with two seam windows checked at final extraction.

## Codimension-four universal incoming reachability and density of monochromatic four-edge roots

Let c be ANY binary coloring of physical ordered three-faces in Q_n, n>=5, without requiring antipodal oddness. For r∈Q_n define
\[
I(r)=\{i\in[n]:\text{there exists a monochromatic four-edge geodesic }
(r\oplus e_i)\to r\to\cdots\},
\]
where its first step uses direction i and its next three steps are along distinct other coordinates. Let
\[
X=\{x\in Q_n:\text{some monochromatic four-edge geodesic starts at }x\}.
\]

**Theorem (at most four prohibited incoming directions per vertex).** For every vertex r,
\[
\boxed{|I(r)|\ge n-4.}
\]
Consequently,
\[
\boxed{|X|\ge 2^n\left(1-\frac4n\right).}
\]
More quantitatively, at least \((n-4)2^n\) directed cube edges \(x\to r\) can serve as the FIRST edge of some monochromatic four-edge geodesic.

**Proof.** If [n]\I(r) contained five distinct directions, take them as a cyclic 5-tuple. The universal odd-cyclic monochromatic seed theorem gives a four-edge monochromatic geodesic whose first edge arrives at r along one of those five directions. This would put that direction into I(r), contradiction. Hence at most four directions are excluded.

There are 2^n vertices r and at least n-4 good incoming directed edges into each, totaling at least (n-4)2^n such edges. Let B=Q_n\X be roots having NO monochromatic four-edge path. Every one of their n outgoing directed edges must be bad (cannot extend to a monochromatic length-four path), and these bad directed edges have distinct tails, so n|B| is at most the total number of bad directed edges, which is at most 4·2^n. Thus |B|≤4·2^n/n and the asserted root-density bound follows. QED.

**Antipodal-pair corollary.** For n>=9, |X|>2^{n-1}. Since the cube's antipodal involution partitions its 2^n vertices into 2^{n-1} pairs, at least one such pair is fully contained in X. More quantitatively the number of antipodal root pairs with BOTH roots in X is at least \(|X|-2^{n-1}\ge 2^{n-1}(1-8/n)\).

**Uniform k-face generalization.** Let k>=1 and m be the least odd integer >=k+1. For arbitrary binary ordered-k-face coloring of Q_n with n>=m, define I_k(r) as incoming directions of a monochromatic (k+1)-edge geodesic whose first step arrives at r. The same odd-cycle proof yields
\[
|I_k(r)|\ge n-m+1,\qquad
|X_{k+1}|\ge 2^n\left(1-\frac{m-1}{n}\right).
\]
The active k=3 case has m=5.

**Research link.** This imposes a strong necessary local reachability coverage on any hypothetical counterexample to full NORI: almost all roots (proportion at least 1-4/n) possess nontrivial monochromatic terminal-two-tail reachability labels of support rank 2. The next closure obligation is to use antipodal symmetry, root mobility, and the exact REVERSED-TWO-TAIL complementary-support equivalence to turn this abundant low-rank reachability into a complementary high-rank collision. The density bound by itself does not supply that collision.

## Valid NORI coloring with NO monochromatic spanning geodesic in any of four parallel codimension-two facets

Fix n>=7, choose U⊆[n] of size m=n-2>=5, and let [n]\U={a,b}. Mark any two distinct coordinate directions u*,v* inside U, and call all other directions of U unmarked. For every ordered triple (i,j,k) of distinct directions FROM U define
\[
f(i,j,k)=
\begin{cases}
1,& j\text{ is unmarked and at least one of }i,k\text{ is marked},\\
0,&\text{otherwise}.
\end{cases}
\]
This f is reversal-even, f(k,j,i)=f(i,j,k). Define colors on ALL physical ordered three-faces whose free directions lie in U by
\[
c(F,(i,j,k))=f(i,j,k)\oplus t_a(F),
\]
where t_a(F) is the fixed exterior a-bit. Since a lies outside U, it is fixed on each such face. If \bar F is antipodal, t_a(\bar F)=1-t_a(F), and reversal-evenness gives
\[
c(\bar F,(k,j,i))=f(k,j,i)\oplus(1-t_a(F))=1-c(F,(i,j,k)).
\]
Thus this partial coloring respects the active NORI axiom. Extend arbitrarily, orbit by orbit, to all ordered faces with at least one free direction outside U; the involution (F,pi)↦(\bar F,rev pi) is free so this always yields a globally valid NORI coloring.

**THEOREM.** For this full valid coloring, NONE of the FOUR parallel U-facets contains a monochromatic complete U-geodesic, in EITHER traversal orientation or from ANY projected root. Consequently the color-free four-facet first–last direction graph H_U(r) of the canonical cap theorem is EMPTY for every r∈Q_U.

**Proof.** Fix a permutation p=(p1,...,pm) of U and any facet exterior bits. Its m-2 ordered-three-face window colors equal
\[
f(p_i,p_{i+1},p_{i+2})\oplus t_a,\qquad 1\le i\le m-2.
\]
The physical U-exterior bits do not appear in f, so the word is root-independent inside the facet up to the fixed global flip t_a.

We prove its f-word contains BOTH symbols 0 and1. If either marked coordinate appears in an internal position 2,...,m-1, the window centered there has f=0, since the middle direction is marked. If instead both marked positions are endpoints 1,m, the window (p2,p3,p4) consists entirely of unmarked directions for m>=5, so again f=0.

For f=1, it suffices to find two adjacent positions k,k+1, with one position marked and the other unmarked, such that the unmarked position is internal (2,...,m-1). Such a pair must exist: otherwise any marked-to-unmarked boundary could only have its unmarked position at one of the endpoints, forcing the entire interval of internal positions to be marked or all transitions to occur only at ends. The first is impossible since m-2>=3 but only two marked directions exist. The latter possibility would make the marked positions consist only of a subset of the two endpoints, with both marks at endpoints; then positions 1 and 2 form a boundary whose unmarked index 2 is internal, a contradiction. More directly, if the marks are adjacent at positions 1,2 or m-1,m, the boundary at positions 2,3 or m-2,m-1 works; in all other arrangements at least one marked coordinate has an internal unmarked neighbor. Choose the triple centered at this internal unmarked position and having the marked adjacent position as an endpoint; then f=1.

Hence the f-word contains 0 and1 for EVERY direction permutation, so no full U-geodesic is monochromatic. Complementing the word by t_a does not change this. There are no actual monochromatic U-spanning witnesses in any of four facets, and H_U(r) has no edges. QED.

**Important strategic guardrail.** A dimension-independent proof of grand NORI closure CANNOT begin by claiming that for every (or every prescribed) n-2 support U the four-facet memory graph H_U(r) is nonempty or nonbipartite. This fully legal coloring annihilates that graph for the selected U, while grand closure itself may hold elsewhere. Thus the cap-cycle extraction theorem, although correct, must be combined with a global support-selection argument or with shorter monochromatic reachability. The example is direction-only within U plus one exterior-bit affine twist, so it is not an exotic nonlinear obstruction.

Under hypothetical failure the cap conditions force a rigid bipartition on available near-spanning cores. A valid construction must still prove those cores exist in the required parallel facets.

### Maximal reachability supports and antipodal missing-facet bounds

# Maximal reachability supports and antipodal missing-facet bounds

A monochromatic geodesic from a root has a support consisting of the coordinates it traverses. Among all such supports, the inclusion-maximal ones determine facets and filter regions of the Boolean lattice. Their geometry is constrained by antipodal oddness: a hypothetical failure of the corresponding closure statement forces missing antipodal support pairs and quantitatively sparse accessible facets.

## One-switch thickening of exact reachable-target flags: all physical square faces are filled

Let c be any binary coloring of the undirected edges of Q_n. Let A_t(c) be the simplicial subcomplex of the usual barycentric subdivision sd(Q_n) generated by all rooted face flags arising from geodesic-prefix direction sequences whose consecutive EDGE colors change at most t times; include all faces of each witnessed flag simplex. For t=0 this is the previously constructed monochromatic flag reachability complex A.

**Theorem 1 (exact face-witness filtration).** A_0 subset A_1 subset ... subset A_(n-1)=sd(Q_n). A_t contains the ENTIRE barycentric subdivision of the geometric cubical (t+1)-skeleton of Q_n: every physical face of dimension at most t+1 and every flag inside it is realized by a path using at most t changes. This does NOT assert that A_t contains the abstract simplicial (t+1)-skeleton of sd(Q_n): a short flag may jump immediately to a high-dimensional physical face and still require a long geodesic.

Proof. A rooted flag ending at a d-face gives an ordered d-direction path. Its color word has d edges and at most d-1 changes. For d<=t+1 every such rooted path qualifies. Every barycentric flag in a physical d-face is a face of some complete rooted flag terminating at that d-face. If t>=n-1 every full n-edge path qualifies, yielding all of sd(Q_n). The filtration is immediate.

**Theorem 2 (antipodal one-switch topological index).** Suppose n>=3 and c(bar e)=1-c(e). Then A_1 is invariant under physical cube antipodality. Its free antipodal Z2 cohomological index is at least two, because it contains Y=the cubical 2-skeleton of Q_n, which has an alpha-invariant barycentric triangulation. The double-cover class w of Y/<alpha> has w^2 nonzero. To see this, include Y/<alpha> as the 2-skeleton of the antipodal cell decomposition of boundary(Q_n)/<alpha> homeomorphic to RP^(n-1). The nonzero degree-two class w^2 of RP^(n-1) restricts nontrivially to its 2-skeleton: a class that vanished already there would vanish in the full complex, since the cellular coboundary determining a degree-two class's exactness comes from degree-one cochains and uses only the 2-skeleton. Thus index(A_1)>=2.

**Theorem 3 (correct endpoint criterion).** The full cube center belongs to A_1 iff there exists an antipodal geodesic with at most one edge-color change. Under antipodally odd c, that is equivalent to a monochromatic antipodal geodesic: a one-switch path concatenated with its antipodal color-complement has a monochromatic antipodal length-n segment after cyclically cutting at the change point. Hence center in A_1 iff center in A_0 for such colorings.

**Consequence and exact open step.** Passing from A_0 to the two-color connector thickening A_1 repairs the face-by-face 2-dimensional obstruction: every physical square, including alternating or red-red-blue-blue squares, is entirely filled in A_1. The resulting alpha-free complex has index>=2 if center is absent. This does NOT yet force center for n>=4: the global boundary sphere has index n-1, and the proved index is only two; nor does absence of a full one-switch geodesic automatically exclude (n-1)-dimensional one-switch PREFIX simplices. A dimension-independent proof must raise index from 2 to n-1 using the color-dependent higher-dimensional flag gluing rules, or obtain a stronger dimension bound.

This is a strictly same-line extension: face barycenters continue to encode actual path witnesses, and the one-switch allowance thickens the SAME barycentric reachable-target carrier.

## Two principal-filter theorem for maximum-length color-free reachability

Let an arbitrary binary UNDIRECTED edge coloring of Q_n be given (antipodal oddness is NOT required). Let m<n be the largest length of any monochromatic geodesic anywhere in the cube. For root x and edge color q∈{0,1}, write
\[
I_q(x)=\{i\in[n]:c(\{x,x\oplus e_i\})=q\}.
\]
Thus I_0(x) and I_1(x) partition the n coordinate directions. Define the UNCOLORED rank-m reachability family
\[
\mathcal S_m(x)=\{S\in\binom{[n]}m:x\oplus S\in R(x)\}.
\]

**Theorem (maximal reachability lies in two principal filters).** If P is ANY monochromatic length-m geodesic starting at x, of color q and support S, then
\[
\boxed{I_q(x)\subseteq S.}
\]
Consequently
\[
\boxed{\mathcal S_m(x)\subseteq
\{S\in\binom{[n]}m:I_0(x)\subseteq S\}
\ \cup\
\{S\in\binom{[n]}m:I_1(x)\subseteq S\}.}
\]
This describes a constraint on the COLOR-FREE reachable-support family: there exists a partition [n]=A disjoint_union B such that every maximum-rank reachable support contains A or contains B. (The witness partition is the local edge-color split, although the definition and subsequent use of \(\mathcal S_m(x)\) need not encode colors.)

**Proof.** Suppose some i∈I_q(x) is absent from S. Traverse the q-colored edge x⊕e_i → x, then follow P from x to x⊕S. The resulting path uses direction i followed by the m distinct directions of S, so all m+1 coordinates are distinct. Every edge has color q, yielding a monochromatic geodesic of length m+1 and contradicting global maximality. This proves I_q(x)⊆S, and taking the union over the two possible witness colors proves the family inclusion. QED.

**Further consequences.**
1. A q-colored length-m geodesic can start at x only if |I_q(x)|≤m; in particular, if m<n/2, there can be terminal maximum-rank paths from x in AT MOST ONE color, necessarily a strictly minority incident-edge color.
2. For each color q represented by any maximum-rank geodesic from x, the entire family of q-witnessed rank-m supports has common intersection containing the nonempty star set I_q(x). This strengthens pairwise omitted-coordinate rigidity to a TOTAL intersection property.
3. Choose one direction i_q∈I_q(x) for each represented witness color q. Then \(\{i_0,i_1\}\) (omitting absent choices) intersects EVERY S∈\mathcal S_m(x). Thus the uncolored family \(\mathcal S_m(x)\) has transversal number at most TWO.
4. The size of \(\mathcal S_m(x)\) obeys
\[
|\mathcal S_m(x)|
\le \binom{n-|I_0(x)|}{m-|I_0(x)|}
+\binom{n-|I_1(x)|}{m-|I_1(x)|},
\]
with binomial coefficients of negative lower index defined as 0. A bound depending solely on n,m from the two-element transversal is
\[
|\mathcal S_m(x)|\le\binom nm-\binom{n-2}m
\]
when both colors occur; if only one witness color occurs, a one-element transversal gives the sharper bound \(\binom{n-1}{m-1}\). In particular there is no issue if one I_q(x) is empty, since no q-colored path of positive length can originate at x.
5. Under antipodal oddness, \(\mathcal S_m(\bar x)=\mathcal S_m(x)\) and \(I_q(\bar x)=I_{1-q}(x)\), giving the exact equivariance of this color-free filter structure.

**Topological program.** Rather than label roots with their entire exponentially large families \(\mathcal S_m(x)\), one may label each root with a minimal transversal of size 0,1,or2 of these supports, choosing it antipodally consistently. The missing step is to force an actual antipodal reachability overlap or an incompatible terminal-blocker incidence from this very small coordinate-label space. Abstract antipodal consistency of arbitrary two-element transversals is insufficient; the principal-filter and root-to-root extension constraints must be used.

## At least a 1/5 density of monochromatic four-edge geodesics and terminal-tail support labels

Let n>=5 and let c be ANY binary coloring of ordered physical three-faces of Q_n, without antipodal-reversal assumptions. A directed four-edge geodesic is **monochromatic** when its two consecutive ordered-three-face windows have equal colors.

**Theorem (20-percent universal path density).** At least ONE FIFTH of all directed length-four cube geodesics are monochromatic:
\[
\boxed{\#\{\text{mono directed 4-geodesics}\}\ \ge\
\frac15\,2^n\,n(n-1)(n-2)(n-3).}
\]
The assertion holds separately for each fixed reference vertex r as SECOND vertex of the directed geodesic: at least one fifth of all ordered four-direction words with a path entering r on the first edge produce two equal window colors.

**Proof.** Fix r and a 5-element direction set D. There are 5!=120 ordered lists of four distinct elements of D, each specifying one directed 4-geodesic starting at r⊕e_{p_1} and entering r on its first edge. Partition these lists into 24 cyclic classes: a class is specified by a cyclic ordering of all five members of D, taken modulo rotation, and consists of the five length-four consecutive cyclic words of that cyclic order. For each class, consider the five ordered three-face colors at physical faces through r with consecutive cyclic direction triples. Since the cyclic word of five binary colors has at least one pair of adjacent equal colors, at least one of the five associated directed four-geodesics is monochromatic. Therefore at least 24 of the 120 paths associated with (r,D) are monochromatic.

For n>5, every ordered four-direction word is contained in exactly n-4 different five-element sets D. Summing the 24-per-D bound over all C(n,5) choices of D gives at least
\[
\frac{24\binom n5}{n-4}=\frac15\,n(n-1)(n-2)(n-3)
\]
monochromatic directed four-geodesics with second vertex r. Sum over the 2^n possible second vertices; every directed four-geodesic has exactly one second vertex. QED.

**Terminal two-tail color-free density.** For an ordered pair J=(a,b), x∈Q_n, and D_J=[n]\{a,b}, let \(\mathcal R_J^{(2)}(x)\) be the color-free family of two-element supports U for which there is a monochromatic directed four-geodesic from x with direction word (some order of U, a,b). Each reachable triple (x,J,U) accounts for at most 2!=2 distinct ordered four-geodesics, whereas each possible triple corresponds to exactly two candidate four-geodesics. Thus the same 1/5 lower density holds:
\[
\boxed{\sum_{x\in Q_n}\sum_{J\in[n]_{\ne}^2}|\mathcal R_J^{(2)}(x)|
\ \ge\ \frac15\,2^n n(n-1)\binom{n-2}{2}.}
\]
Here J ranges over all n(n-1) ordered direction pairs. This establishes an unconditional positive-density constraint for the EXACT color-free reachability regions in the NORI complementary-tail closure theorem.

**General uniform-k version.** Let k>=1 and m be the least odd integer ≥k+1, with n>=m. Every binary ordered-k-face coloring of Q_n has at least a 1/m fraction of its directed length-(k+1) geodesics monochromatic. The same cyclic m-order partition argument proves it: with a fixed reference second vertex r and m-set D, every cyclic order has m distinct (k+1)-direction subwords; at least one has two equal consecutive k-face colors. Every ordered (k+1)-word from D belongs to exactly the same number of cyclic m-classes (indeed one if m is k+1 or k+2), and the subsequent average over D preserves the 1/m bound. For k=3, m=5.

**Grand closure status.** The lower bound of 1/5 on rank-two tail reachability is BELOW the 1/2 middle-rank upper bound obtained assuming no grand NORI witness in n=6. Thus density alone does not yet close the conjecture. The exact next objective is an amplification or transfer inequality driving reachability from low ranks toward complementary higher ranks without introducing unwanted ordered-face seam windows.

The support-fiber bounds control the distribution of reachable paths but do not certify a single order extending all compatible pieces. The missing ingredient is a joint choice of terminal memory and complementary supports.

## Topological reachability spaces and extraction

# Topological reachability spaces and extraction

This section separates exact discrete geodesic extraction from the topology of its continuous carriers. The underlying objects are initially antipodally odd physical edge colorings, with c(bar e)=1-c(e). The ordered-three-face problem requires additional ordered terminal-memory data because joining two monochromatic branches creates two new three-face windows.

## The doubled root–endpoint cube

For x,y in Q_n, put S(x,y)={i:x_i≠y_i} and rank rho(x,y)=|S(x,y)|. A state (x,y) represents the endpoints of a path using precisely S. For any i outside S one may replace (x,y) by (x xor e_i,y) or by (x,y xor e_i). The respective covers prepend or append the corresponding genuine edge, and raise the rank by one. If a chain begins at (z,z) and all covers have color q, it constructs a monochromatic q-geodesic: each coordinate is used once. Conversely any monochromatic geodesic is encoded by appending its edges. A chain to rank n yields an antipodal geodesic.

For each coordinate, the four endpoint-bit states form a height-one poset whose order complex is the square boundary S^1. Their product has an order-complex triangulation of (S^1)^n, the n-torus. Thus the 2n endpoint bits give an n-dimensional topological carrier with exact cover-chain path meaning. Its topology alone has limited antipodal index, so a forcing argument must use the colored reachable part and its actual incidence data.

## The root–support reachability recursion

For q∈{0,1}, define E_q(x,S) to mean that some q-monochromatic geodesic begins at x and uses exactly S, ending at x xor 1_S; include S=empty. For nonempty S,

E_q(x,S) iff there exists a∈S such that c({x,x xor e_a})=q and E_q(x xor e_a,S\{a}).

This follows by deleting the first edge, and the converse follows by prepending it. Reversal gives E_q(x,S)=E_q(x xor 1_S,S). Antipodal reversal gives E_q(bar x,S)=E_(1-q)(x,S). Root movement can also prepend an unused q-edge while retaining the terminal vertex. These are genuine geometrical covers, rather than formal implications among labels.

Let E=E_0∪E_1. Define sigma(x,S)=(x,[n]\S). There is a one-switch antipodal edge-geodesic iff E meets sigma(E). Indeed a collision yields monochromatic branches from x to x xor 1_S and from x to x xor 1_([n]\S), with disjoint direction supports. Reverse the first branch and concatenate at x to obtain an antipodal geodesic with at most one color change. Antipodally odd edge colors also permit the standard rotation argument to turn this existential one-switch witness into a monochromatic antipodal witness. Equivalently there exists x whose color-free monochromatic reachable set R(x) contains both z and bar z. The same condition may be written as a common endpoint reachable monochromatically from x and bar x.

## Honest Freudenthal carriers and midpoint extraction

Fix x. A monochromatic geodesic with nested prefix supports S_0⊂...⊂S_k determines a simplex of the usual cubical triangulation of the support cube. Let K_q(x) be the union of simplices witnessed by actual q-monochromatic geodesics from x. The face center associated with D={i:x_i≠y_i} lies in K_q(x) precisely when some q-monochromatic geodesic joins x to y.

For the forward implication, the simplex of the witness contains the empty and D prefix vertices, hence their midpoint. Conversely, if the center of the D-face lies in one witnessed chain simplex, all coordinates outside D vanish and all coordinates in D equal 1/2. Nestedness forces the extremal supports represented by positive barycentric coefficients to be empty and D: otherwise some D-coordinate stays 0 or stays 1, or some outside coordinate remains positive. Thus the same witness path reaches D. This midpoint criterion faithfully encodes target reachability without creating paths from merely convex combinations of unrelated witnesses.

The candidate global argument seeks a topologically forced intersection between antipodally related honest carriers or labels. A zero of a continuous extension in the ambient 2n-cube need not belong to a discrete witnessed simplex, so an additional boundary or incidence theorem is indispensable.

## Terminal profiles and equivariant nerves in NORI

For active ordered-three-face colorings, fix an ordered terminal pair J=(a,b) and let D_J=[n]\{a,b}. Denote by R_J(x) the supports U⊂D_J of q-monochromatic physical geodesics from x ending in ordered directions (a,b), with color q existentially quantified. The reversed-tail splice theorem requires complementary supports U and D_J\U at the *same root*, with terminal orders J and rev J.

Form signed profiles L_x of true pairs (J,U) and their formal reversed-complement profiles tau L_x. The nerve of these signed sets has all positive vertices spanning one simplex and all negative vertices spanning another: every three-edge path has just one ordered-face window and hence supplies a monochromatic singleton-support label from every root. A mixed edge between (x,+) and (y,-) witnesses compatible labels at potentially different roots. When x=y it supplies the desired reversed-tail splice. When x≠y, antipodal symmetry supplies the mirrored mixed edge; along with the two universal same-shore edges these give a genuine equivariant four-cycle, whose two same-root mixed diagonals are precisely the missing grand-closure certificates. Therefore the nerve's nontrivial low-dimensional topology can survive under hypothetical grand failure.

This distinguishes the two forcing tasks. In the edge case, an antipodal collision in one uncolored R(x) is the exact extraction condition. In NORI, a collision must additionally preserve the physical terminal orders and same-root complementary supports. The present reachability carriers and signed-root nerves provide exact encodings and identifiable boundary configurations; a global coincidence theorem enforcing that strengthened compatibility remains open.

### Root-endpoint state torus and geodesic connectors

# Root-endpoint state torus and geodesic connectors

Root and endpoint are independent state variables. A two-ended geodesic may extend on its initial or terminal side without repeating a cube coordinate, provided the current support and the two-window terminal memory are retained. The root-endpoint torus is the simplest geometric carrier for these extensions, but its antipodal index remains small. The following proofs establish the exact extension geometry and identify the earliest loss of physical compatibility under naïve reachability coincidence.

This develops the user's proposed n root bits plus n current-position bits in the ordinary antipodally odd edge-colored cube. Let c be a binary coloring of undirected edges of Q_n, n>=2, satisfying c(bar e)=1-c(e). A monochromatic antipodal geodesic has n edges.

**State poset.** Use states (x,y) in {0,1}^n x {0,1}^n, recording the two endpoints of the currently constructed geodesic. Its used-coordinate set is S(x,y)={i:x_i!=y_i}, and rank is rho(x,y)=|S(x,y)|. For any unused direction i, there are two covers:
(x,y) -> (x XOR e_i,y), colored c({x,x XOR e_i});
(x,y) -> (x,y XOR e_i), colored c({y,y XOR e_i}).
All covers increase rank by one. Root extension is permitted only in an unused direction, just as current-end extension is.

**Exact geodesic extraction.** Every monochromatic directed chain starting at a diagonal state (z,z) constructs a monochromatic geodesic between its current endpoints. A root cover prepends the indicated edge, and a current-end cover appends it. Its direction is unused, so no coordinate repeats. The resulting path has length rho and is therefore geodesic. A chain reaching rank n produces a monochromatic antipodal geodesic. Conversely, any monochromatic geodesic between x and y is represented by a chain of current-end covers from (x,x) to (x,y). Consequently directed monochromatic reachability from the diagonal is exactly monochromatic geodesic reachability between the two endpoint labels, even when root moves are allowed.

**Geometry theorem.** The order complex of this state poset triangulates the n-torus
T_n=(boundary[0,1]^2)^n.
In particular, it is n-dimensional, although its vertices carry 2n bits. The cubical one-skeleton is Q_{2n}; the order-complex triangulation adds diagonals. Colored directed chains throughout this item use cover edges, rather than arbitrary diagonals of the triangulation.

Proof. For one coordinate the two unused states 00,11 are minimal, the two used states 01,10 are maximal, and every minimum is covered by every maximum. Its order complex is the four-edge square boundary S^1. The n-coordinate poset is the product of these one-coordinate posets. A comparable chain uses, in each factor, at most one source-to-sink edge; hence it belongs to a product of square-boundary edges and vertices. On each product cell, its chains give the standard monotone triangulation of that cell. These triangulations agree on common faces and cover the product of the n square boundaries. Thus the order complex is a triangulated n-torus. The rank extends affinely on these simplices.

A fixed root x gives an n-cube chart: y ranges freely and covers change y_i away from x_i. The torus adds root-extension cells to these charts, and those transitions have an exact geodesic meaning. Filling the entire geometric 2n-cube would add cells beyond this state complex.

**Symmetries.** Endpoint exchange sigma(x,y)=(y,x) preserves rank and cover colors. Simultaneous antipodality alpha(x,y)=(bar x,bar y) preserves rank and complements cover colors. The involutions commute. Their product tau(x,y)=(bar y,bar x) also preserves rank and complements cover colors. In the product-square geometry:
Fix(sigma)=D={(x,x)};
Fix(tau)=A={(x,bar x)}.
These statements hold on the full torus, since a square boundary meets its diagonal only at 00,11 and its antidiagonal only at 01,10. Alpha acts freely as a half-turn in each circle factor. The two different reflection fixed sets D and A are precisely the geodesic start and target states.

**Top-rank extension lemma.** Every monochromatic geodesic of length n-1 in an antipodally odd edge coloring extends, at one of its two endpoints, to a monochromatic antipodal geodesic.

Proof. Its endpoints x,y agree in exactly one unused coordinate i. The edges {x,x XOR e_i} and {y,y XOR e_i} are antipodal, since bar x=y XOR e_i and overline(x XOR e_i)=y. Their colors are opposite. One therefore has the color of the existing path, and extending at that endpoint uses the final unused direction. QED.

Thus forcing a monochromatic directed chain to rank n-1 already suffices.

**Reachability labels with exact recursion.** Let r_q(x,y) be 1 precisely when a monochromatic q-geodesic joins x to y. Then r_q(x,x)=1. For x!=y,
r_q(x,y)=OR over i in S(x,y) of
[c({x,x XOR e_i})=q AND r_q(x XOR e_i,y)]
OR
[c({y,y XOR e_i})=q AND r_q(x,y XOR e_i)].
The two alternatives remove an edge from the corresponding endpoint and decrease rank by one. Therefore this recursion has no cyclic dependency and is exact. Moreover
r_q(y,x)=r_q(x,y),
r_q(bar x,bar y)=r_{1-q}(x,y),
r_q(bar y,bar x)=r_{1-q}(x,y).
A hypothetical failure has reachability label (r_0,r_1)=(0,0) at every rank n-1 and rank n state. At D the label is (1,1). Every q-colored cover preserves q-reachability forward.

**Equivalent connector formulation at a common vertex.** For an actual cube vertex v, let R_q(v) be the set of roots x admitting a monochromatic q-geodesic x->v. A monochromatic antipodal geodesic exists if and only if R_0(v) intersects R_0(bar v) for some v. If x lies in this intersection, the coordinate sets used from x to v and from x to bar v are complementary and disjoint. Concatenating the two red paths at x gives a red antipodal geodesic v->bar v. Conversely, a red antipodal geodesic itself witnesses the intersection. Any blue antipodal geodesic has a red antipodal image, so red alone suffices.

More directly matching the user's two-root proposal, if roots x and bar x admit monochromatic geodesics to the same v, with either color on either branch, their two direction sets are complementary. Concatenation is an antipodal geodesic with at most one change. In an odd edge coloring that one-change geodesic rotates to a monochromatic one: if x->v has color q and v->bar x has color 1-q, append the antipodal image of x->v after bar x. The suffix v->bar x followed by that image is a monochromatic n-geodesic from v to bar v. If the two branches have the same color, the original concatenation is monochromatic.

**Precise topological obligation.** A connector theorem on this state complex must produce a directed monochromatic chain from D to rank n-1 (or A), or produce the exact complementary-root meeting just described. Once it does, geodesic extraction is automatic. The outstanding claim is the existence of that chain. Undirected connectivity in the state graph does not preserve the used-direction constraint; arbitrary barycentric label averages do not by themselves give a directed chain.

The geometry and the reachability recursion are established. A topological forcing theorem remains open. Symmetry and the labels at D and A alone cannot supply it: the continuous pair (1-rho/n,1-rho/n) has the same exchange symmetries and endpoint values (1,1) at D and (0,0) at A. The colored-cover propagation and edge-color consistency must enter any obstruction argument.

**NORI applicability.** This construction currently concerns one-coordinate windows, namely ordinary edge colors. For ordered-three-face NORI, a state must additionally retain the last two directions (and potentially the first two when extending at the root) so that extension determines the newly formed ordered-three-face window. No edge-case topological conclusion is being silently transferred to three-face colors.

**Additional verification.** The two-end recursion was compared with ordinary fixed-root monotone geodesic reachability for both colors in all 64 antipodally odd edge colorings of Q_3; every endpoint pair agreed.

## Antipodal endpoint links are high-index spheres with canonical monochromatic entrance sectors

Continue the rooted two-end state torus T_n=(S^1)^n of ordered pairs (u,v) in Q_n^2, with rank d_H(u,v), endpoint exchange sigma(u,v)=(v,u), simultaneous antipodality alpha(u,v)=(bar u,bar v), and tau=alpha sigma. Each coordinate circle is the square 00--01--11--10--00, with angles 0,pi/2,pi,3pi/2.

**Theorem 1 (local antipodal link).** For n>=2, every top-rank state a_x=(x,bar x) is an isolated fixed point of tau, and a sufficiently small link L_x around a_x is an (n-1)-sphere on which tau acts as ordinary antipodality. Its natural crosspolytope cell decomposition has 2n signed vertices (two inward rank-decreasing choices for each coordinate), and its 2^n orthant facets are indexed by all possible common connector vertices z in Q_n. Opposite orthants correspond to z and bar z.

*Proof.* In angular coordinates, tau(theta)=pi-theta coordinatewise. At a_x each theta_i is pi/2 or 3pi/2. In a sufficiently small local chart delta around a_x, tau(delta)=-delta. A small Euclidean ball is tau-invariant, and its boundary is the stated antipodal sphere. The 2n inward directions are the two arcs in each coordinate circle from a_x toward the two diagonal states 00 and 11. Choosing one arc per coordinate gives precisely a product n-cube from the diagonal state (z,z) to a_x, with z_i the chosen diagonal bit. The sector's directed chains are geodesics built by extending either endpoint at each unused direction. Tau sends the diagonal root (z,z) to (bar z,bar z), proving the opposite-sector claim.

**Theorem 2 (canonical entrance-sector selectors).** Let c be an antipodally odd coloring of the undirected edges of Q_n. Write c_i(x)=c({x,x XOR e_i}), and define a cube vertex z_q(x), q in {0,1}, by
(z_q(x))_i = x_i XOR 1 XOR c_i(x) XOR q.
For each antipodal endpoint state a_x=(x,bar x), the q-colored incoming cover edges at a_x select exactly one of the two inward signs in each coordinate. These n signs together specify the unique orthant sector whose *all n immediate final edges into a_x* have color q, and its diagonal root is z_q(x). Moreover
z_1(x)=bar z_0(x),
z_q(bar x)=z_q(x).

*Proof.* The two inward covers in coordinate i add either the edge incident with x of color c_i(x) or its antipodal edge incident with bar x of color 1-c_i(x). The first cover belongs to the sector with diagonal coordinate z_i=bar x_i; the second to z_i=x_i. Thus the sector whose incoming cover has color q has z_i=bar x_i when c_i(x)=q and z_i=x_i when c_i(x)!=q, exactly z_i=x_i XOR 1 XOR c_i(x) XOR q. Each coordinate's two incoming colors are complementary, so the sector is unique. The first displayed relation is immediate, and the second follows from c_i(bar x)=1-c_i(x).

**Precise topological opportunity and extraction warning.** The simultaneous-antipodality action alpha on the entire T_n has equivariant cohomological index only one, but the tau action on each punctured neighborhood of a target a_x has link S^(n-1) with full local antipodal index n-1. The selected z_0(x) and z_1(x) are complementary labels encoding the last-edge color data, precisely matching the proposed antipodal-coordinate labels. Nevertheless color agreement of all n last edges does **not** imply a monochromatic directed chain from the corresponding diagonal root to a_x: interior covers can obstruct, and a successful chain could also enter through a sector whose other last edges have different colors. A Hartman/Tucker/Sperner argument would have to label each local sector by jointly realizable *directed reachability* and prove the required boundary/incidence relations; the local high index and final-edge selectors alone do not settle the edge conjecture or ordered-three-face NORI.

## Three-unused-direction flap dichotomy in ordered-three-face NORI

Fix n>=6, a color-q geodesic P of length m=n-3 from x to y, with direction sequence p=(p_1,...,p_m), and the three unused coordinates W={a,b,c}. Thus the ordered-three-face word inside P consists of m-2>=1 copies of q. For any ordering t=(a,b,c) of W, consider two *full antipodal* geodesics:
H_front: starting at x XOR W, flip a,b,c to reach x, then follow P to y;
H_back: follow P from x to y, then flip c,b,a to finish at y XOR W=bar x.

Let u=c(F_x,(a,b,c)), the color of the ordered missing-coordinate face at x (its exterior coordinates equal x outside W). Since F_y=bar F_x and antipodal reversal reverses coordinate order, the last ordered face of H_back has color 1-u.

Introduce the exact four bridge colors
A(b,c)=color of the (b,c,p_1) window in H_front,
B(c)=color of the (c,p_1,p_2) window in H_front,
C(c)=color of the (p_{m-1},p_m,c) window in H_back,
D(c,b)=color of the (p_m,c,b) window in H_back.
(The displayed dependencies on b,c are justified because ordered-three-face colors ignore the three free coordinate bits, so the removed first missing coordinate does not affect A/B, and the terminal unflipped missing coordinate does not affect C/D.)

The two full color words are EXACTLY
H_front: (u,A(b,c),B(c),q,...,q),
H_back: (q,...,q,C(c),D(c,b),1-u).

**Theorem (forced anti-switch flaps).** If the NORI grand conjecture fails for this coloring, then for EVERY length-(n-3) monochromatic q-geodesic P and EVERY ordering (a,b,c) of the three unused coordinates the following holds:
- if u=q, then (C(c),D(c,b))=(1-q,q), and at least one of A(b,c),B(c) differs from q;
- if u=1-q, then (A(b,c),B(c))=(q,1-q), and at least one of C(c),D(c,b) differs from q.

*Proof.* If u=q, H_back begins with q and ends with 1-q. The complete four-block word q,C,D,1-q has at most one color change precisely when (C,D) is qq, q(1-q), or (1-q)(1-q). Under counterexample all such completions fail, so the sole remaining pair is ((1-q),q). The matching-front outer color and the P interior color are both q; it fails only if at least one of A,B differs from q. If u=1-q, the same argument with the two completions interchanged gives (A,B)=(q,1-q) and a defect in at least one of C,D. All four bridge windows are actual ordered-three-faces, and the only oddness relation used is c(bar F,rev pi)=1-c(F,pi). QED.

**General-dimension consequence.** Any proposed NORI counterexample must exhibit an explicitly prescribed *alternating two-seam obstruction* on one of two opposite three-direction flap completions of every nearly spanning monochromatic core. This is a direct face-local analogue of the one-edge antipodal extension mechanism, now with two unavoidable seam windows. It is not yet a closure theorem: the color on the missing ordered three-face can vary with all six permutations, and the four bridge families do not contradict each other without additional overlapping-core or path-exchange relations.

**Research target.** Derive an exchange or carrier theorem that forces, for at least one such core, one permutation of W whose forced-flap pattern is impossible. Unlike a Q_7 subclass enumeration, this obstruction and its color transport hold for every dimension n>=6.

These results give exact local and conditional constructions. No conclusion here asserts unrestricted high-dimensional grand closure.

### Opposite-corner terminal basins and Freudenthal reachability cones

# Opposite-corner terminal basins and Freudenthal reachability cones

Given a root and a choice of monochromatic color, record precisely the terminal vertices of directed geodesic witnesses, including their ordered terminal-memory state when required. The terminal basin has a natural barycentric or Freudenthal realization, but abstract convexity of that realization is weaker than compatible monochromatic path gluing. The proofs below track accessibility, antipodal reversal and genuine cone carriers.

## The root-progress reachability system on 2n bits

Let c be an antipodally odd binary edge coloring of Q_n. Define E_i subset of Q_n(root) x 2^[n](support) by E_i(r,S) iff an i-monochromatic shortest path takes r to r xor 1_S, with empty paths allowed. Put E=E_0 union E_1.

**Theorem (exact recurrence, symmetry, root movement).** For S nonempty:
E_i(r,S) iff OR over a in S of [c({r,r xor e_a})=i AND E_i(r xor e_a,S\{a})].
Root antipodality alpha(r,S)=(bar r,S) exchanges E_0 and E_1. Path reversal rho(r,S)=(r xor 1_S,S) preserves E_i. If a is not in S and c({r,r xor e_a})=i, then E_i(r,S) implies E_i(r xor e_a,S union {a}), preserving the physical endpoint r xor 1_S. This is precisely a legal monochromatic diagonal-square corridor inside the root-progress doubled cube.

**Proof.** Split a nonempty i-monochromatic geodesic after its first edge, of direction a in S. The remaining path is i-monochromatic and uses the other |S|-1 directions; conversely prepend that i-colored edge. Antipodality swaps colors and preserves relative support, giving alpha. Reversing a monochromatic geodesic preserves color and support, giving rho. Finally, prepend the i-colored edge (r xor e_a)->r to an i-geodesic r->r xor 1_S. As a lies outside S the resulting path is geodesic, has support S union {a}, and the same endpoint. QED.

**Exact endpoint-coincidence formulation.** Define sigma(r,S)=(r,[n]\S) and beta(r,S)=(bar r,[n]\S). Existence of an antipodal geodesic with at most one color change is equivalent to a collision E intersect sigma(E). Indeed, two E-states of the form (r,S),(r,[n]\S) encode monochromatic geodesics from one root to complementary endpoints and the exact antipodal splicing theorem applies. Equivalently E intersects beta(E), since E is alpha-invariant. Under beta, the physical endpoint is unchanged: (bar r) xor 1_([n]\S)=r xor 1_S. Thus a beta-collision represents the proposed common monochromatically reachable cube vertex from antipodal roots, and the pair of compatible color blocks can be concatenated with at most one change.

**Topological gap.** The continuous support reflection sigma on the full 2n-dimensional product cube has a fixed midsection at S_j=1/2 for all j; a generic odd-map zero there gives no combinatorial reachable state. A useful Tucker/Borsuk--Ulam construction must use path-coherent cells generated by the recurrence and certified root corridors, with a proved boundary/index condition that forces a collision of E with beta(E) or sigma(E). These conditions are more restrictive than continuous root-progress interpolation, and their existence remains open.

All statements concern the antipodally odd EDGE-colored proving ground; ordered-three-face NORI transfer remains unresolved.

**Full antipodality gives a sharper topological test.** On the continuous doubled cube C=I^n_root x I^n_support, beta(r,s)=(1-r,1-s) is ordinary antipodality: it fixes only (1/2,...,1/2) in 2n coordinates and acts freely on boundary(C), a (2n-1)-sphere. It is therefore potentially stronger than sigma(r,s)=(r,1-s), whose fixed set is the whole root midsection. Nevertheless let M=I^n_root x {(1/2,...,1/2)_support}. On C\M the explicit beta-equivariant map
f(r,s)=(s-(1/2,...,1/2))/||s-(1/2,...,1/2)||
takes values in S^(n-1) with antipodal action; hence a beta-equivariant subspace that avoids M cannot have equivariant index greater than n-1 by a Borsuk--Ulam obstruction. In a putative counterexample, every monochromatic rooted progress complex built from Freudenthal chains avoids M: within any monotone support simplex, the support midpoint belongs to the simplex only if both empty and full supports belong to it (strict nesting forces its coordinates equal only on the long diagonal joining these extremes). Presence of the full support as a witnessed monochromatic chain already proves the desired conjecture. Thus a genuinely 2n-dimensional beta-topological proof must use mixed root-progress cells and prove that their contact with the support midsection yields actual compatible reachable states. Merely placing disjoint rooted Freudenthal charts in one 2n-cube does not raise the usable index.\n\n**Strengthened monochromatic extraction.** In the antipodally odd EDGE case, every antipodal geodesic with at most one color change rotates, along the same 2n-cycle consisting of that path and its antipodal image, to a monochromatic antipodal geodesic. Consequently the conditions E intersect beta(E), E intersect sigma(E), and existence of a monochromatic antipodal geodesic are ALL equivalent. In fact one can restrict to the one-color reachability family R_0: there exists a monochromatic antipodal geodesic iff some x has R_0(x) intersect bar(R_0(x)) nonempty. Forward: if z,bar z are red-geodesically reachable from x, the two red geodesics run x->z and x->bar z and their reversals splice into a red geodesic z->bar z, since their disjoint coordinate supports partition [n]. Reverse: if x->bar x has a monochromatic blue geodesic, its antipodal image has color red, and red reachability from one endpoint includes its antipode. Equivalently R_0(x) intersect R_1(bar x) is nonempty, since R_1(bar x)=bar R_0(x). This gives the precise single-color antipodal-cone collision C_0(x) intersect tau C_0(x), in the all-root K_n, as an exact extraction criterion; here tau(C_0(x))=C_1(bar x) and the intersection of geometric subcomplexes contains an actual common cube vertex. The difficult task remains to force such a collision globally by topology.

THEOREM (EXPLICIT NORI-COMPATIBLE NON-DOWNSET). There exists an antipodal-reversal-odd ordered-three-face coloring of Q_5 with a fixed terminal vertex y=00000 and ordered terminal directions J=(3,4) for which the color-free basin T_J(y) contains root x=11111 (support U={0,1,2} relative to b0=00011), but omits the root x'=11011 (support U'={0,1} subset U). Thus the existing geodesic-root-accessibility theorem for terminal basins CANNOT be strengthened to closure under arbitrary subsets; a Sperner/barycentric argument must retain actual witness-chain compatibility rather than assuming every lower support is present.
CONSTRUCTION. Coordinates numbered 0,1,2,3,4. For root x=11111, require the ordered three-face colors along the directed path with direction word (0,1,2,3,4) to be 0,0,0. Its successive ordered faces have triples (0,1,2), (1,2,3), (2,3,4), and physical exterior bit strings respectively (x3,x4)=(1,1), (after flipping 0: x0,x4)=(0,1), and (after flipping 0,1: x0,x1)=(0,0).
At root x'=11011, the two possible directed paths to y ending (3,4) have words (0,1,3,4) and (1,0,3,4). Give their FIRST ordered three-face windows color 0 and their SECOND windows color 1. Specifically set c(F,(0,1,3))=0 and c(F,(1,0,3))=0 on the same physical 3-face whose exterior coordinates (2,4) equal (0,1). Set color 1 on the face through y free {1,3,4} with order (1,3,4), and on the face through y free {0,3,4} with order (0,3,4). Neither four-edge path is monochromatic.
The displayed seven assignments involve ordered faces on five distinct free-coordinate triples {0,1,2}, {1,2,3}, {2,3,4}, {0,1,3}, {1,3,4}, {0,3,4} (six distinct triples; two orders on {0,1,3}). No two of the chosen assignments are related by the active involution (F,pi)->(bar F,reverse pi), because that involution preserves the free-coordinate SET. Therefore extend these prescriptions independently to the six antipodal-reversal orbits, and arbitrarily to all remaining orbits with complementary values. This creates an honest globally valid NORI coloring. The prescribed five-edge path is monochromatic, whereas both possible four-edge terminal-J paths from x' fail, as claimed. QED.
TOPOLOGICAL CONSEQUENCE. A terminal basin is rooted-accessible by trimming the FIRST coordinate from an actual monochromatic witness. It need not contain all coordinate-subsets beneath a witnessed support. In particular, the hypothesis of a complete face-respecting barycentric support chart in a naive application of Sperner B5 or cubical Tucker C8 is genuinely stronger than actual NORI monochromatic reachability and cannot be silently assumed.

FOUR-DIRECTION ORDERED-TRIPLE LEMMA (EXACT, NO ANTIPODAL AXIOM). Let A={a,b,c,d} be four distinct directions. Give each of the 24 ordered triples of distinct elements of A an arbitrary bit f(u,v,w). Assume that for EVERY ordered permutation (u,v,w,s) of A, the two overlapping ordered triples are NOT both color1:
  NOT[f(u,v,w)=f(v,w,s)=1].
Then there are four pairwise distinct directions u,v,w,s with
  f(u,v,w)=f(s,v,u)=0.
Thus the lack of a mono-color1 consecutive ordered-window pair forces two color0 ordered triples sharing the same MIDDLE direction v and with the second outer direction of the first reversed to the third position of the second. No physical face reversibility or NORI antipodal oddness is needed.
SELF-CONTAINED CONTRADICTION PROOF. Relabel A={0,1,2,3}. Assume there is NO requested 0-pair, i.e. whenever f(u,v,w)=0, the paired f(s,v,u)=1 for the unique fourth direction s. We show both f(0,1,2)=1 and f(0,1,2)=0. (I) If f012=0, the forbidden 0-pair forces f310=1; the adjacent-overlap restriction on word 2310 forces f231=0; the forbidden 0-pair forces f130=1; adjacent restriction on 2130 forces f213=0; the forbidden 0-pair forces f012=1, contradiction. Therefore f012=1. (II) From f012=1, the overlap restriction on 0123 gives f123=0; 0-pair exclusion gives f021=1; overlap restriction on 0213 gives f213=0; 0-pair exclusion gives f310=1; overlap restriction on 3102 gives f102=0; 0-pair exclusion gives f301=1; overlap restriction on 3012 gives f012=0, contradiction. Thus the requested 0-pair exists. QED.
PHYSICAL NORI APPLICATION. Suppose a physical cube hub z has a four-element direction class A of color0 square-certified incident directions in the local UNIQUE-COLOR edge-shadow branch (no physical edge at z has certificates of both colors). Then no centered 4-geodesic using only A directions can be monochromatic color1: such a path would certify a color1 middle square on two edges at z already certified color0. Thus the abstract lemma applies to the ACTUAL physical ordered-three-face labels through z restricted to A. It produces two literal color0 faces with the special reversed-terminal ordered-pair pattern, furnishing two distinct centered one-switch 6-geodesic seeds after combining with any two color1 directions B={r,s} via the proved mixed-middle selector (orders (u,v,w,r,s,d) and (d,v,u,r,s,w), with d the fourth A direction). Their roots differ by exactly two cube directions, and their corresponding endpoints likewise differ by two. The full six-edge words are (0,0,1,1) for both seeds.
The conclusion does not claim the two rank-two root shifts are automatically a global one-switch NORI witness; their outside terminal-memory supports require an additional root-compatible antipodal splice.

The attainable conclusion is a conditional obstruction involving intersecting physically compatible terminal basins. Individual basin contractibility, antipodal symmetry or a large volume does not independently guarantee a full good path.

### Barycentric reachability carriers and antipodal boundary maps

# Barycentric reachability carriers and antipodal boundary maps

The Boolean cube admits a barycentric realization in which each directed geodesic appears as a chain of nested coordinate supports. Reachability simplices are honest only when their vertices share a single actual monochromatic path witness. This framework compares terminal labels, canonical midpoints, convex relaxations and antipodal boundary maps.

## Canonical face centers recognize every monochromatically reachable target exactly

In the n-dimensional diagonal-fiber cross X_n, let z,z' be any two physical vertices, and D={i:z_i neq z'_i}. Their affine fibers F_z and F_z' intersect in the coordinate constraints r_i=s_i=1/2 for i in D and s_j=(r_j XOR z_j) in the continuous affine sense for j outside D. Define the CANONICAL midpoint point
m(z,z')=(r,s), where
r_i=(z_i+z'_i)/2 and s_i=1/2 for i in D;
r_j=z_j=z'_j and s_j=0 for j outside D.
It satisfies m(z,z')=m(z',z) and belongs to F_z intersect F_z'. In the coordinate chart F_z, this is exactly the center of the |D|-dimensional face with supports S subseteq D, incident with the empty-support apex.

**Theorem (exact partial-target midpoint test).** For any q in {0,1},
m(z,z') belongs to K_q(z) iff there exists a monochromatic q-GEODESIC z->z'.
Consequently m(z,z') in K_q(z) iff it belongs to K_q(z'), and both hold precisely when z,z' are joined by a q-monochromatic geodesic. Thus the colored edge carriers are just the distance-one instances of an exact midpoint-overlap principle at EVERY distance.

*Proof.* A q-monochromatic geodesic z->z' has support exactly D. Its full prefix simplex in F_z contains the empty vertex and the D vertex, so it contains their midpoint m(z,z'). Reversing the geodesic gives the same midpoint in K_q(z').
Conversely suppose m(z,z') lies in one witnessed prefix simplex of K_q(z), corresponding to a chain of actual supports S_0 subset ... subset S_k. Since each s_j=0 outside D, any vertex of this chain contributing with positive barycentric weight has no directions outside D. Since each s_i=1/2 inside D, no contributing supports can all omit any such i or all contain any such i. By nestedness, a positive-weight minimal contributing support must be empty (otherwise some coordinate remains one in the entire positive support), and the maximal positive-weight support must be D (otherwise some coordinate remains zero). The witnessed monochromatic path therefore contains empty and full D support along its own order, yielding a monochromatic geodesic z->z'. More formally, the faces of a Freudenthal chain intersect the relative cube center only if the chain includes both its minimum and maximum support. QED.

**Corollary (face-barycenter labels).** For fixed z, all candidate reachable vertices z' are represented by the 2^n barycenters m(z,z') of cube faces containing the root apex in F_z. The full antipodal conjecture asks whether the barycenter m(z,bar z)=o of the ENTIRE fiber appears in some K_q(z). If z,z' differ by k coordinates, q-reachability to z' is literally the inclusion of the associated k-face barycenter in the witnessed path complex. These barycenter labels avoid false intersections of convex averages: each particular canonical midpoint has an exact shortest-path extraction theorem.

**Root-color symmetry.** Under physical antipodality alpha(r,s)=(1-r,s), one has alpha(m(z,z'))=m(bar z,bar z'); oddness sends K_q(z) to K_(1-q)(bar z). Both the midpoint representation and its witness test are fully antipodally equivariant.

**Limit.** Other points of F_z intersect F_z' may lie in K_q(z) and K_r(z') without monochromatic shortest paths between z,z'. The theorem singles out canonical midpoint points as the faithful labels; a general topological intersection theorem must force one of these certified points, rather than an arbitrary geometric crossing. For full antipodal targets, F_z intersect F_bar z={o}, so every intersection is automatically canonical.

## A color-free 2n-bit reachability holonomy graph: odd signed cycles force closure

Let c be an antipodally odd binary UNDIRECTED edge coloring of Q_n. Define the uncolored monochromatic-geodesic reachability relation
\[
\mathcal E=\{(x,S):x\in Q_n,\ \varnothing\ne S\subseteq[n],\ x\oplus S\in R(x)\}.
\]
These are exactly ROOT–SUPPORT states with n root bits plus n support bits. They are defined solely by the COLOR-FREE sets R(x). Associate a signed graph H_R to the states with THREE types of (undirected) edges:

(A) **Antipodal root flip**, sign 1:
\[
(x,S)\longleftrightarrow(\bar x,S).
\]
(B) **Endpoint reversal/root swap**, sign 0:
\[
(x,S)\longleftrightarrow(x\oplus S,S).
\]
(C) **Near-complementary supports at the same root**, sign 1:
\[
(x,S)\longleftrightarrow(x,T)
\quad\text{if } S\cap T=\varnothing,\ S\cup T=[n]\setminus\{i\}\text{ for some i}.
\]
All endpoints of all these edges are in \(\mathcal E\): (A) by odd coloring, (B) by undirected path reversal, and (C) by definition. Retain edge types if parallel edges arise.

**Theorem (odd-holonomy extraction).** If H_R contains a closed walk whose edge-sign sum is odd and that traverses at least one (C) edge, then c has a MONOCHROMATIC FULL ANTIPODAL GEODESIC. Conversely, in any hypothetical counterexample, every connected component of H_R containing a (C) edge carries a unique consistent binary vertex potential q such that
\[
q(\bar x,S)=q(x,S)\oplus1,\quad
q(x\oplus S,S)=q(x,S),\quad
q(x,T)=q(x,S)\oplus1
\]
on the corresponding edge types. Thus such a component has zero signed holonomy around every closed walk.

**Proof.** For a state (x,S), define \(C(x,S)\subseteq\mathbb F_2\) to be the NONEMPTY set of colors of all monochromatic geodesics joining x to x⊕S. This auxiliary witness-color set is used ONLY IN THE PROOF; it is absent from the state graph and reachability-label definition. Under (A), the antipodal copy complements edge colors exactly, giving C(bar x,S)=1-C(x,S). Under (B), reversal of an undirected edge path preserves each edge color, giving C(x⊕S,S)=C(x,S). At a (C) edge, if C(x,S) and C(x,T) shared any color q, their two q-geodesics would have disjoint coordinate supports covering n-1 coordinates. Their concatenation is a q-colored length-(n-1) geodesic. Its two end-extension edges are antipodal with opposite colors, so one completes it to a full q-geodesic. Therefore, in the absence of a full monochromatic antipodal geodesic, C(x,S) and C(x,T) are disjoint nonempty subsets of the two-element color set. They must be complementary SINGLETONS. The bijections in (A),(B) preserve singleton cardinality, so every state in a connected component containing a (C) edge has a unique witness color. The displayed potential q is then its unique element. Along any closed walk q must return to itself, requiring an even number of sign-1 edges. Hence an odd-signed closed walk implies closure. QED.

**No premature role for the colors.** The graph H_R and the existence of an odd signed cycle depend only on R(x), the cube's root/coordinate geometry, and the sign of three structural operations. The two color indices appear only inside the extraction proof to establish the obstruction. This is exactly an 'antipodal-label coincidence implies actual monochromatic witness' certificate with explicit extraction.

**Relation to odd-dimensional Kneser cycles.** Restrict to a single root x and the (C) edges. This recovers the near-complement graph \(\Gamma_x\). For n odd, middle-layer Kneser odd cycles give odd holonomy immediately. For n even, \(\Gamma_x\) is bipartite by support-cardinality parity, but root antipodality (A) and endpoint exchange (B) can create new cross-root signed cycles. This gives a unified dimension-independent target: force a NONTRIVIAL Z_2-holonomy cycle in the root-coupled reachable state graph.

**Scope and challenge.** A signed frustrated cycle is a SUFFICIENT condition, not asserted to exist for every coloring. Proving its existence from antipodal-odd edge incidence would establish the edge-geodesic conjecture. The graph may be balanced for some colorings that already have a monochromatic antipodal geodesic; the theorem is not an equivalence. One can also treat any reachable support S=[n] as immediate closure, independently of holonomy. Its value is a precise, color-free, topologically meaningful inconsistency criterion, with no small-dimension classification.

## Exact NORI grand closure as intersection of two antipodally corner-rooted geodesically accessible basins

Let c be the ACTIVE antipodal-reversal-odd binary ordered-three-face coloring on Q_n, n>=4. Fix distinct coordinates a,b and let J=(a,b), D=[n]\{a,b}. Fix any cube vertex y and define y^D=y⊕D, the complement in D directions ONLY (its a,b bits unchanged). Define the **COLOR-FREE monochromatic terminal basin**
\[
T_J(y)=\bigl\{x\in Q_n:\ \exists\text{ a directed MONOCHROMATIC ordered-three-face-window geodesic }x\to y
\text{ ending in ordered directions }(a,b)\bigr\}.
\]
Either monochromatic color is permitted, without recording it. Paths of length two with no three-face window are included vacuously; this makes the basin contain its natural base corner. All roots x lie in the (n-2)-dimensional physical facet
\[
H_y^{a,b}=\{x:x_a=1-y_a,\ x_b=1-y_b\}.
\]
Let
\[
b_0=y\oplus\{a,b\}\in H_y^{a,b},\qquad
b_1=b_0\oplus D\in H_y^{a,b}.
\]
These are antipodal vertices WITHIN the facet H_y^{a,b}. The second basin \(T_{\operatorname{rev}J}(y^D)\) lies in the SAME facet H_y^{a,b} and has natural base corner b_1.

**THEOREM 1 (exact two-basin intersection equivalence).** The grand NORI conjecture in Q_n holds if and only if there exist y and ordered tail J=(a,b) such that
\[
\boxed{T_{(a,b)}(y)\cap T_{(b,a)}(y^D)\ne\varnothing.}
\]
The regions are UNCOLORED monochromatic-geodesic reachability labels, and the intersection automatically splices into a full antipodal geodesic with at most one ordered-three-face color change; the colors of the two branch witnesses may agree or differ.

**Proof.** Suppose x is in the intersection. A directed monochromatic x-to-y geodesic A has terminal directions (a,b), and a directed monochromatic x-to-y^D geodesic B has terminal directions (b,a). Since x_a=1-y_a and x_b=1-y_b, both paths traverse a,b and their remaining direction supports are respectively
\[
U=\{i\in D:x_i\ne y_i\},\qquad
V=\{i\in D:x_i\ne (y^D)_i\}=D\setminus U.
\]
Thus their full supports intersect in exactly {a,b}, and their non-tail supports complement in D. Apply the previously proved exact reversed-two-tail splice theorem: truncate A before a,b, append the global antipodal reversal of B, and get a full antipodal geodesic with its first |U| windows of one monochromatic color and last |V| windows of the opposite of B's color. When both U,V are nonempty this is exactly the proof. In the boundary cases U or V empty, one of A/B is a FULL monochromatic n-edge geodesic because it traverses all n coordinates, which itself establishes closure. Conversely any full one-switch antipodal geodesic decomposes by the exact reversed-two-tail theorem into two such monochromatic branches from some common root x ending in opposite facet-antipodal vertices y and y^D with reversed ordered tails J and revJ, so x belongs to the intersection. QED.

**THEOREM 2 (strong rooted accessibility).** Each \(T_J(y)\subseteq H_y^{a,b}\) contains the base corner b_0 and ALL its d=n-2 neighbors inside the facet. More strongly, for EVERY x∈T_J(y), there exists a full Hamming-shortest path INSIDE \(T_J(y)\) from x to b_0; in particular T_J(y) induces a connected subgraph and is geodesically rooted at b_0. The second basin T_revJ(y^D) has the same properties with root b_1.

**Proof.** The length-two path from b_0 to y with direction word (a,b) has no three-face windows and is included by convention. For any i∈D, the three-edge path from b_0⊕e_i to y with word (i,a,b) has exactly one ordered-three-face window and is therefore automatically monochromatic: all d neighbors are included. For general x∈T_J(y), choose a monochromatic witnessing geodesic
\[
x\ \xrightarrow{u_1,\ldots,u_s,a,b}\ y,
\quad\{u_1,\ldots,u_s\}=\{i\in D:x_i\ne(b_0)_i\}.
\]
Trimming its first direction u_1 produces the suffix geodesic from x⊕e_{u_1} to y, with ordered terminal pair (a,b) and a subsequence of the original monochromatic windows. Thus x⊕e_{u_1} lies in T_J(y). Repeat through u_2,...,u_s to b_0. These vertices form a shortest path within the root facet H_y, since each step removes one disagreement coordinate with b_0. The analogous proof applies to revJ at the antipodal corner b_1. QED.

**Exact topological problem.** The grand NORI conjecture is equivalent to the impossibility of TWO DISJOINT geodesically corner-rooted terminal basins T_J(y) and T_revJ(y^D) for EVERY choice of y,a,b. This is a precise two-shore Hex/Hartman connector formulation:
- the opposite base corners b_0 and b_1 lie in a physical d-cube H;
- each basin contains its entire radius-1 star and is geodesically connected to its base;
- basin membership means ACTUAL monochromatic ordered-face-window geodesic reachability and records NO color;
- an intersection yields one genuine full good geodesic with no uncontrolled seam windows.

Importantly, two arbitrary rooted connected radius-one neighborhoods of opposite corners CAN be disjoint for d>=3; topology must use the coupling among basin families for different tails J and terminal vertices y. The next research goal is a simultaneous Sperner/KKM/Hex argument enforcing intersection across the collection of all such coupled accessible basins, not a false pointwise Helly assertion for a single pair.

The topology of an abstract target carrier cannot be used to infer a path unless its simplices satisfy the literal geodesic-certification rule. Several counterexamples here delimit that rule sharply.

### Root-profile nerves and signed mixed-branch interfaces

# Root-profile nerves and signed mixed-branch interfaces

Label each cube root by its genuine monochromatic terminal-support possibilities, retaining the reversed terminal two-direction order used for NORI splicing. The profile nerve has opposite sign shores under antipodal reversal. Individual shores may be large simplices, but the mixed interface is controlled by the existence of paths long enough to support both complementary branches.

## Universal two-shore simplices in the exact signed-root reachability nerve and a canonical equivariant square

Let n>=5, d=n−2>=3, Ω={(J,U): J=(a,b) ordered distinct, ∅≠U⊊D_J=[n]\{a,b}}, with fixed-point-free involution τ(J,U)=(rev J,D_J\U). For each cube root x define the **actual color-free terminal memory profile**
L_x={(J,U) in Ω: U in R_J(x)},
where R_J(x) consists of supports witnessed by a MONOCHROMATIC directed physical ordered-three-face geodesic rooted at x and ending in ordered directions J. Let S_(x,+)=L_x and S_(x,−)=τ L_x. Define N as the nerve on signed roots (x,±) whose simplices are families of S_(x,±) with common label. This is the exact fixed-point carrier of item nori_reversed_tail_root_profile_nerve_tucker_label_reduction_20261008: an antipodal edge (x,+)(x,−) is equivalent to active NORI grand closure.

**Theorem 1 (unconditional two full shores).** All positive signed-root vertices together span a simplex Δ_+, and all negative signed-root vertices together span a simplex Δ_−, *independent of the coloring*. Indeed fix any ordered tail J and coordinate i∈D_J. The three-edge direction word (i,a,b) has exactly one ordered-three-face window, hence is automatically monochromatic, from EVERY starting cube root x. Therefore (J,{i}) belongs to L_x for ALL x. This one label witnesses the whole Δ_+. Its involution τ(J,{i}) witnesses the whole Δ_−.

**Theorem 2 (mixed edge and forced equivariant square).** A mixed edge (x,+)(y,−) exists iff some actual support U satisfies U∈R_J(x) and D_J\U∈R_revJ(y). If x=y this is grand closure. If x≠y, its τ partner (y,+)(x,−) also exists. Together with the universal shore edges (x,+)(y,+), (x,−)(y,−), these four vertices form a τ-invariant **induced four-cycle** in the no-closure hypothesis, namely
(x,+) -- (y,+) -- (x,−) -- (y,−) -- (x,+).
No other edges can occur inside this four-vertex set in a no-closure configuration, because the two missing diagonals are precisely the forbidden opposite-signed same-root pairs. Every triple of the four vertices contains one forbidden opposite pair, so no 2-simplex fills this square using only these four vertices. The induced cycle is an equivariant copy of the circle with antipodal involution. It follows that the free-Z2 cohomological index of N is >=1 whenever any cross-root mixed edge exists under no closure. This does **not** imply that the square is nonzero in the H_1 of all of N: other vertices and simplices could fill it.

**Theorem 3 (only genuinely long supports can couple the shores in a counterexample).** If the grand conjecture fails, no root has an admissible support U of size d−1 in ANY tail family: the complementary size-one label with reversed tail is automatically present at that same root and would give closure. Consequently every mixed signed-root nerve edge in a counterexample must be witnessed by a pair of support sizes s and d−s with BOTH s>=2 and d−s>=2. In particular, for d<=3 (n<=5) no mixed edge exists under the no-closure hypothesis, and the abstract hypothetical nerve is exactly Δ_+ disjoint union Δ_−. For n>=6 every mixed edge records genuinely longer path data not forced by one-window tautologies.

**Application and limit.** The signed root-profile nerve has a structural "two full shores plus constrained mixed faces" form. It is therefore especially amenable to Tucker/Bier-type equivariant arguments if one can control mixed high-dimensional simplices by genuine common witnessed labels. The unrestricted full shore simplices alone have equivariant index zero (their disjoint union is equivariantly S^0); a single cross-root mixed edge creates an invariant S^1 subcomplex, but no general high-index bound follows. Proving that a sufficiently high-index mixed-face configuration MUST appear (or an opposite edge occurs) remains the exact unsolved topological step.

## Color-preserving path carriers have trivial antipodal cover class

Inputs: nori_window_shift_monochromatic_edges_universal_cohomology_class_20261008 and literature_fixed_point_theorems. This gives a precise transport constraint for the new window parity class.

## 1. The monochromatic-shift subgraph splits the double cover
Let H be the graph of actual ordered three-face windows, with shifts realized by genuine four-edge geodesics. Let tau(F,pi)=(bar F,rev pi), and let c(tau v)=1-c(v). Let H_mono be the spanning subgraph retaining exactly edges uv with c(u)=c(v).

Then c:|H_mono| -> {0,1} is continuous and equivariant (tau exchanges 0 and 1). The two color subgraphs are exchanged by tau. The quotient double cover
 H_mono -> H_mono/tau
is TRIVIAL: each quotient vertex and edge has a unique color-zero lift, and this defines a global continuous section. Thus its cover class w_mono vanishes, and all its positive powers vanish.

This holds even when the monochromatic shift graph has odd cycles and nonzero ordinary first cohomology.

## 2. The connector parity class is distinct from antipodal index
In the full quotient B=H/tau, the established classes satisfy
 alpha=[hbar]=[1_B]+w,
where hbar records same-color edges. Restrict to B_mono=H_mono/tau. Then
 w|B_mono=0,
 alpha|B_mono=[1_(B_mono)].
Hence an odd monochromatic cycle may detect alpha while detecting zero antipodal cover class.

The conclusion follows directly from the section in part 1 and the fact that hbar is one on every retained edge. In particular, the coloring-independent nonzero connector class provides genuine parity information; transporting it into a high-index carrier additionally requires the carrier's color-forgetting identifications or suitable edges between different colors.

## 3. General colored-state carrier theorem
Let Z be a finite simplicial complex whose vertices represent monochromatic path states, each with an actual binary witness color q(v). Suppose q is constant on every simplex and tau acts simplicially with q(tau v)=1-q(v). Then q extends to a continuous equivariant map |Z| -> S^0. Its quotient double cover has a global color-zero section. Consequently every positive power of its cover class vanishes.

Proof. Every simplex lies in one color class; the two resulting subcomplexes are disjoint and exchanged. The constant affine extension of q is continuous, and the section follows as above.

For r such carriers, their equivariant join maps to
 (S^0)^(join r)=S^(r-1),
by joining their color maps. Their product with the diagonal involution maps to S^0 by projecting to the first factor and then using its color map. Thus joins or products of separate color-preserving connector carriers have the stated index upper bounds, regardless of other ordinary cohomology classes.

## 4. Consequence for NORI's exact color-free carriers
The mixed root-profile interface and the initial/terminal physical witness-cone complexes forget witness color. Their points may identify states backed by distinct colored paths. Such identifications remove the hypothesis of part 3 and can carry nontrivial antipodal topology.

A proposed high-index construction should specify these identifications and verify that a face still retains a valid root/terminal-memory extraction. Keeping every monochromatic witness in a permanently separate colored component gives the explicit S^0 map above. The exact reversed-tail splice theorem allows either branch color, so color-free profile intersections are the appropriate extraction target.

No assertion of nonzero higher cover powers for the actual color-free interface is made here. Establishing such powers, or acyclicity of the interface, remains a forcing task toward grand closure.


## Sparse monochromatic reachability without large-volume guarantees

**Theorem (exact reachability count for an antipodally odd edge-colored family).** Let \(n=2m\) and partition the \(n\) directions into \(m\) ordered pairs \((a_t,b_t)\). Give each undirected edge in direction \(a_t\) the color of its fixed \(b_t\)-bit, and each edge in direction \(b_t\) the color of its fixed \(a_t\)-bit:
\[
c(\{z,z\oplus e_{a_t}\})=z_{b_t},\qquad
c(\{z,z\oplus e_{b_t}\})=z_{a_t}.
\]
This is a well-defined antipodally odd two-edge-coloring of \(Q_{2m}\): the partner bit remains fixed across its associated edge and toggles under antipodal complementation.

For root \(x\), let \(A,B,H\) be the numbers of coordinate pairs with starting bits \(00,11,\) and mixed \(01/10\), respectively; \(A+B+H=m\). Let \(R_i(x)\) be the vertices reachable from \(x\) by an edge-color-\(i\) monochromatic *geodesic*, including the zero-length path. Let \(R(x)=R_0(x)\cup R_1(x)\). Then
\[
|R_0(x)|=3^{A+H},\quad
|R_1(x)|=3^{B+H},\quad
|R_0(x)\cap R_1(x)|=2^H,
\]
and therefore
\[
\boxed{|R(x)|=3^{A+H}+3^{B+H}-2^H.}
\]
The maximum over roots is
\[
\boxed{\max_x |R(x)|=2\cdot3^m-2^m,}
\]
and the average over all \(2^{2m}\) roots is \(2(5/2)^m-(3/2)^m\).

For every \(m\ge5\), **no** starting vertex has a monochromatic reachability set comprising more than half the cube:
\[
|R(x)|\le2\cdot3^m-2^m<2^{2m-1}.
\]
Nevertheless, the coloring admits a full **monochromatic antipodal geodesic**.

**Proof.** A geodesic changes each coordinate at most once. In a starting \(00\) pair, an edge-color-0 geodesic may traverse neither coordinate or exactly one of the pair (three choices) but cannot traverse both, since the second move would see partner bit 1; edge-color-1 traversal permits only the empty support. For a starting \(11\) pair the roles of the colors reverse. In a mixed pair \(01/10\), each color separately permits exactly three supports: the empty support, one of the two singleton supports, and the two-coordinate support. The two color-specific local support sets intersect precisely in the empty and full-pair supports (two choices).

Coloring interactions between distinct pairs are independent: colors within a pair depend only on that pair's coordinates, so every selection of independently realizable per-pair support witnesses can be concatenated to a globally monochromatic geodesic of the same selected color. Counting the possible global supports, which correspond bijectively to endpoints, gives the two powers of 3; the intersection has one support choice in each homogeneous pair and two in each mixed pair, giving \(2^H\). Inclusion-exclusion yields the formula.

Converting one homogeneous pair to a mixed pair strictly increases the union size: for \(00\to\text{mixed}\), \(3^{A+H}\) stays fixed, \(3^{B+H}\) is tripled and \(2^H\) doubled, so the net increment is \(2\cdot3^{B+H}-2^H>0\); the \(11\to\text{mixed}\) case is symmetric. Thus the maximum occurs when \(A=B=0,H=m\), giving \(2\cdot3^m-2^m\). For a uniformly random root, pairs are independently \(00,11,01,10\) with probability \(1/4\) each. Taking expectations of \(3^{A+H}\), \(3^{B+H}\), and \(2^H\) gives the stated average by multiplying the respective per-pair expectations \(5/2,5/2,3/2\).

For \(m=5\), \(2\cdot3^5-2^5=454<512=2^{9}\). The ratio \((2\cdot3^m-2^m)/2^{2m-1}=4(3/4)^m-2(1/2)^m\) decreases with \(m\ge5\), proving the strict half-volume inequality for all later \(m\).

For the full antipodal geodesic, take a root whose bits in every pair are mixed. For each pair choose the order of its two moves so that both edges have a preselected common color 0 (or analogously color 1); this is possible because one order traverses both directions in color 0 and the other in color 1. Concatenate the resulting monochromatic two-move paths across all pairs. Each direction is used exactly once, yielding a full monochromatic antipodal geodesic. \(\square\)

**Verified checks.** A direct monotone-subset dynamic program enumerated *all roots* in \(n=2,4,6,8\), with no discrepancies between computed monochromatic reachable-endpoint counts and the formula. The independent \(Q_4\) square-face obstruction example in Item \`nori_edge_reachability_nerve_square_face_nonfilling_and_support_symmetries_20261008\` uses the same family.

**Implication for topological NORI strategy.** A proposed proof based solely on universal largeness \(|R(x)|>2^{n-1}\) (and therefore pigeonhole overlap with its antipode) cannot work. The goal must use geometry, support structure, local face incidence, or equivariant topology of the *actual certified reachability family*, rather than a large-volume bound. This theorem is about the simpler edge-colored proving ground; it is NOT by itself a proof or disproof of ordered-three-face NORI.

### Elevation pass I: antipodal invariance at vanishing density

For a root \(x\) with **all \(m\) coordinate pairs mixed** (one 0 and one 1 in each pair), the same family satisfies the stronger identity
\[
\overline{R(x)}=R(x),
\]
even though
\[
\frac{|R(x)|}{|Q_{2m}|}=\frac{2\cdot3^m-2^m}{4^m}\longrightarrow0
\]
exponentially. Indeed, within a mixed pair the color-0 supports are exactly \(\varnothing,\{b\},\{a,b\}\) after a suitable naming of the directions, whereas the color-1 supports are \(\varnothing,\{a\},\{a,b\}\). Complementation of that two-element coordinate support interchanges these lists. Since distinct pairs contribute independent choices, global support complementation interchanges the full color-0 and color-1 reachable families. Thus every endpoint \(x\oplus S\) monochromatically reachable from this particular root has its physical antipode \(x\oplus(V\setminus S)\) monochromatically reachable as well. This demonstrates a much sharper limitation on purely volumetric fixed-point methods: **complete antipodal closure of a reachable set can coexist with arbitrarily small density**. Its arrangement and certified support involution, not its size, contain the relevant obstruction.


A topological coincidence in this nerve implies grand closure only when it realizes complementary supports with compatible endpoint memories at the same root. The interface, not the separate large shores, is the active topological target.

## Terminal memory and branch splicing

# Terminal-memory reachability and physical seam extraction

Let c be a binary coloring of ordered physical three-faces of Q_n satisfying c(bar F,rev pi)=1-c(F,pi). Every direction-distinct path of length k has an ordered color word of k-2 windows. Reversing the path at the antipodal root complements and reverses this word.

## Accessible supports and their limits

For an undirected edge coloring of Q_n, fix x and let R(x) be endpoints reachable from x by a monochromatic geodesic of either color. Its direction-support family A_x consists of S for which x xor 1_S belongs to R(x). Each nonempty S in A_x admits i in S with S without {i} in A_x: delete the final edge of an actual monochromatic witness. All prefixes of one witness give an entire nested support chain. The family need not contain every subset of S, since a different subset need not admit a monochromatic order.

## Reversed-two-tail terminal profiles

For ordered-three-face NORI, fix an ordered terminal pair J=(a,b), and put D=[n] without {a,b}. Record U subset D when a monochromatic geodesic begins at x, uses directions U and finally (a,b), with all windows referring to their actual physical faces. A second monochromatic witness from x ending in (b,a) and using the complementary support D without U is precisely the input of the proved reversed-two-tail splice criterion. The two witness colors may differ. The same physical root, complementary supports and reversed terminal order are essential: they certify the two newly formed three-face windows after rearrangement.

These data define a signed profile nerve by retaining witness labels and exchanging J,U with rev J,D without U. Each sign shore is a full simplex: every three-edge path, with its single ordered-face window, is monochromatic from every root. Mixed intersections at two different roots are genuine compatibility information but are not yet same-root splice certificates. A diagonal mixed intersection gives the intended antipodal extraction.

## Boundary-memory states

For a genuine k-edge path P, record its endpoints, first and last two directions, terminal window colors and switch count truncated at two. Its endpoint difference records the used direction support. This state is sufficient to check admissibility of endpoint extensions only after the new physical seam windows have been evaluated. The rank-six braid construction identifies distinct histories with one reduced boundary state and thereby exhibits nontrivial incidence hidden by state compression. The corresponding physical square has to be certified with its actual paths, rather than filled combinatorially by the mere equality of state labels.

A topological extraction theorem must therefore produce a profile coincidence with one common root and complementary reversed tails, and provide a physical lift of any quotient-level path. Accessibility and the braid construction supply exact constraints on this missing theorem.

### Two-ended path memory, six-direction braids, and seam repairs

# Two-ended path memory, six-direction braids, and seam repairs

A full one-switch path decomposes at one transition into two monochromatic branches, but its seam contributes two ordered three-face windows. The terminal two-direction memory is therefore essential for both a precise reachability statement and legal concatenation. At rank six, two distinct traversal histories can first meet in the same reduced memory state, producing a braid whose links encode the missing exchange information.

## Exact boundary-memory quotient first identifies genuinely different geodesics at rank six

For ordered-three-face NORI, let B(P) be the EXACT two-ended boundary memory state of a directed k-edge geodesic P as previously established: oriented endpoints (x,y), its first two direction entries and last two direction entries (truncated when k<2), first and last three-window colors when k>=3, and total number of color changes clipped at 2. Endpoint XOR determines the unordered set S of its k used directions. Two directed segments are identified only if these memory states agree.

**Theorem 1 (injective through rank five).** For every coloring (and independently of NORI oddness), the map P->B(P) is INJECTIVE on segments of lengths k<=5. Proof: for k<=4 the first and last two direction entries jointly list the entire direction order; for k=5 they reveal p1,p2,p4,p5, while the sole missing entry p3 is the unique coordinate in S minus those four. The starting endpoint x then determines the directed segment uniquely. Shorter lengths have the evident truncated convention.

**Theorem 2 (actual ambiguity at rank six).** For n>=6, there exists a valid antipodal-reversal-odd ordered-three-face coloring and two DISTINCT directed rank-six segments P,P' with B(P)=B(P'). Take common starting root x=0^n and the direction orders
P=(1,2,3,4,5,6),
P'=(1,2,4,3,5,6).
They have the same endpoints and support S={1,...,6}, head=(1,2), tail=(5,6), but differ by a middle adjacent transposition. Assign color zero to all four ordered-three-face windows of P and to all four of P'. They then have equal first/last colors 0 and clipped change count 0, hence identical memory states. These finitely many ordered-face objects belong to distinct orbits of the NORI involution (F,pi)->(bar F,rev pi): where a free unordered triple is shared, the two displayed internal ordered triples are neither identical nor reversals on antipodal faces, and the other triples have different free coordinate sets. Thus all eight prescribed zeros are simultaneously consistent; extend to a full NORI coloring by choosing arbitrary colors on the remaining involution orbits and complementary colors on their mates. The two underlying paths remain distinct.

**Theorem 3 (exact finite-memory directed chains).** The predecessor/successor transitions by prepending or appending one unused direction are Markov on B(P): the new ordered three-window is computed solely from the relevant endpoint and the first/last two direction memories; changes and boundary colors update exactly. Therefore every sequence of legal boundary-state cover transitions from a realizable rank-zero state is represented by an ACTUAL chain of nested geodesic segments, even when several full histories have been merged into one state. This is proved by induction on the sequence length, using that every representative of a state admits the same named legal extension with the same resulting state. The involution Theta on states exchanges left and right transitions, reverses the two direction memories, and complements/swaps first and last colors; for n>=3 it remains free on the state vertices.

**Topological implication.** The full-history contiguous-segment order complex has equivariant index exactly one for EVERY hereditary admissibility rule: each higher segment has a contractible lower link and the whole complex collapses to its directed-edge graph. The exact boundary-memory quotient agrees with that full-history complex through rank five. Starting at rank six it can GLUE distinct histories with common continuation rules, so the former contractible-link collapse argument no longer automatically applies. This supplies a concrete place for higher-dimensional topology to appear while retaining actual geodesic-reachability labels.

This does NOT prove that the quotient has index>1, nor that its quotient-induced order complex has no spurious simplices. To avoid phantom witness chains, define the finite-memory path complex with simplices consisting of states along actual Markov extension chains (or use the exact transition DAG's reachability-path realization), and exploit the inductive chain-lifting property above. The next genuinely new obligation is to determine whether the rank-six braid identifications create nontrivial equivariant relative homology or a Tucker-type carrier intersection that forces an accepting full-rank state.

## Rank-six braid-link circle detects and fills an actual physical square cycle

Keep n=6 and the same valid NORI coloring and accepted monochromatic memory state b merging
P=(1,2,3,4,5,6), P'=(1,2,4,3,5,6)
from root 000000. Let C_<6 be the order complex of all admitted directed geodesic segments of rank<=5, ordered by oriented contiguous inclusion. Because boundary-memory states are unique through rank five, this is also the exact memory quotient subcomplex below b. Let L_b subset C_<6 be the rank-six merged state's lower link, previously proved homotopy equivalent to S^1.

**Theorem 1 (canonical start-point map to the physical edge graph).** For ANY hereditary directed-segment complex, there is a continuous map
f_start:|C| -> |Q_n^(1)|
sending a segment P to its first physical vertex and each simplex of nested contiguous segments to the corresponding piecewise-linear physical path of starting vertices along its maximal segment.

Proof. On a chain P_0<...<P_m, write the start of each P_j as vertex v_(a_j) of P_m=(v_0,...,v_k), so k>=a_0>=a_1>=...>=a_m=0. Send a point with barycentric coefficients lambda_j to the point at continuous arclength t=sum_j lambda_j a_j along the edgewise linear path v_0->...->v_k in the abstract cube edge graph. The coefficients a_j decrease along chains, so this is continuous on the simplex and maps to the physical edge-graph path. If a face of the simplex removes its maximal element, all retained segments lie in the new maximal subsegment; replacing the original indices by indices relative to this subsegment merely translates their arclength origin, preserving the same physical point. Thus the simplex maps agree on overlaps and define a continuous global map. QED.

**Theorem 2 (the circular link survives in preattachment H_1).** Choose the two common lower-link components represented by the common two-edge PREFIX A=P[0,2]=P'[0,2] and common two-edge SUFFIX Z=P[4,6]=P'[4,6]. In the lower link L_P of P there is a path
A < P[0,5] > P[1,5] < P[1,6] > Z.
In L_P' there is the analogous path with P' in place of P. They share their endpoints A,Z, and their union represents the generator of H_1(L_b;F2).

Under f_start, the first path follows the physical route from vertex 000000 through directions 1,2,3,4 to the common physical vertex v_4={1,2,3,4}, while the second path follows directions 1,2,4,3 to the same v_4. Their difference is the closed FOUR-EDGE physical square at base v_2={1,2}, with free directions 3,4:
v_2 -> v_2 XOR e_3 -> v_2 XOR{3,4} -> v_2 XOR e_4 -> v_2.
This square cycle represents a nonzero class in H_1(|Q_6^(1)|;F2), since the target is a graph and its edges appear exactly once in the cycle. Consequently the generator of H_1(L_b;F2) maps NONTRIVIALLY into H_1(C_<6;F2). In particular it is not already killed by any lower-rank path-state simplices.

**Theorem 3 (real rank-six relative filling).** Adjoining the accepted memory-state vertex b and all its incident nested-chain simplices attaches the cone b*L_b to C_<6. The relative homology of the attachment contains
H_2(b*L_b,L_b;F2) ~= H_1(L_b;F2) = F2.
The boundary of this relative class is the NONZERO preexisting physical square-cycle class described in Theorem 2. Thus this actual rank-six braid identification KILLS a genuine H_1 class of the lower-rank reachability complex by attaching a two-dimensional filling; it is not a homotopically trivial cone over a contractible link.

Under complemented reversal Theta, b has a distinct partner state Theta(b), whose link is another circle. Its physical square under the corresponding start-point map is the ANTIPODAL {3,4}-square: originally exterior bits outside directions3,4 are (1,2)=(1,1),(5,6)=(0,0), while the reversed-complemented paths swap 3,4 after directions (6,5), giving exterior bits (1,2)=(0,0),(5,6)=(1,1). Hence the two homological fillings occur in an antipodally paired fashion.

**Research interpretation.** This is an explicit, genuinely higher-dimensional, COLOR-COMPATIBLE topological repair mechanism within the honest reachable-target construction. The canonical segment-poset complex alone collapses to a graph, but exact memory-state merging creates antipodally paired square fillings corresponding to reordering internal coordinates. A global proof would have to show that the necessary system of such fillings (and higher braid analogues) cannot be completed without at least one accepting full antipodal state. The theorem itself is an example for a valid coloring, not universal existence of such a state and not a proof of NORI grand closure.

## Exact common-middle root square of a two-window NORI geodesic splice

Let c be ANY physical ordered-three-face coloring, and fix a genuine full direction-distinct geodesic word p=(p1,...,pn) with a cut after \ell directions, where 2<=\ell<=n−2. Write the two last prefix directions u=p_(ell−1),v=p_ell and the first two suffix directions w=p_(ell+1),t=p_(ell+2), all pairwise distinct. For any cube root x, set S={p1,...,p_ell}, y=x XOR S, and define its TWO physical crossing-window faces
  L_x=( F(y;{u,v,w}), (u,v,w) ),
  R_x=( F(y;{v,w,t}), (v,w,t) ).
These are exactly the ordered faces of the two windows straddling the cut in the full geodesic rooted at x.

**THEOREM (literal two-seam cubical flatness, and sharp dimension).** For ANY translation mask A⊆{v,w} and x'=x XOR A, the two ordered physical faces are literally IDENTICAL:
  L_(x')=L_x, R_(x')=R_x.
Consequently their ordered colors are identical for all FOUR physical roots x, x XOR v, x XOR w, x XOR v XOR w. In other words the two-seam color pair is constant on the full physical 2-cube whose free coordinate directions are exactly {v,w}, for ANY NORI coloring and even without antipodal oddness.

Conversely, suppose A⊆[n] is such that translating x by each individual direction a∈A leaves BOTH ordered physical face OBJECTS unchanged (not merely their colors, which may coincidentally be constant). Then A⊆{v,w}. Thus the two-dimensional root square above is the MAXIMAL full physical coordinate face on which BOTH crossing window objects stay literally fixed. This is sharp in every dimension and every direction order.

**Proof.** A physical ordered face F(y;U) is the cube face with free directions U and all other coordinate bits fixed to y outside U. Translating the starting root x by direction a changes the cut vertex y by the same direction a, so F(y;U) is unchanged iff a∈U. For the left and right crossing faces their free direction sets are U_L={u,v,w} and U_R={v,w,t}. Their intersection is EXACTLY {v,w}, since p has pairwise distinct directions. Hence BOTH faces remain unchanged precisely under flips in span{v,w}; in particular all four root-square vertices have the same two physical objects and colors. Any additional direction lies outside at least one free set, so changing its root bit changes that ordered physical face object, establishing sharpness. QED.

**JOINT CONNECTION WITH MULTIROOT TUCKER.** The root-square near-midpoint Tucker theorem nori_multiroot_near_midpoint_tucker_common_cut_root_square_20261008 supplies, for ANY preassigned physical two-coordinate root square, two packets of eight total actual full endpoint-opposed paths with a common near-middle support cut S (n>=11). To take advantage of THIS theorem's exact two-seam flatness, one must show that some packet's selected cross-splice has the two shared middle seam directions (v,w) EQUAL TO the two free directions of the preassigned root square. That self-consistent alignment is NOT supplied by Tucker merely from common S. More generally, the eight packet paths can have different last prefix and first suffix directions, so their two seam objects need not be identical across the square. Establishing this boundary-memory/root-square alignment, and then synchronizing monochromatic branches or reducing the switch count, is a precisely formulated missing combinatorial forcing lemma.

**STATUS.** This is a genuine physical cubical flatness theorem of the two crossing windows, not an unrestricted NORI closure theorem. It sharply identifies the maximal root-square dimension available for *literal* simultaneous seam invariance (two), explaining why a four-root packet is natural in ordered-three-face NORI.

The braid and root-square calculations demonstrate why pure endpoint reachability loses the needed geometry. A successful global repair must remember the two overlapping physical windows at each concatenation.

### Antipodal root-profile paths and deleted-product extraction

# Antipodal root-profile paths and deleted-product extraction

An antipodal root-profile construction seeks a path in a mixed-sign interface between complementary monochromatic support labels. Reachable support families need not form Boolean downsets, and the root-bit fiber of a partial path may have nontrivial dimension. The following propositions state the exact topological and combinatorial conditions under which a profile coincidence is extractable.

## Geodesic reachability regions are accessible but NOT Boolean downsets, even with antipodal oddness

Let Q_n be an UNDIRECTED binary edge-colored cube satisfying c(bar e)=1−c(e). As usual let R(x) consist of endpoints of monochromatic geodesics from x, allowing either color, including x. For each root x define the reachable coordinate-support family
\[
\mathcal R_x=\{S⊆[n]:x⊕S∈R(x)\}.
\]

**THEOREM 1 (accessibility).** For every nonempty S∈\mathcal R_x, there exists at least one i∈S with S\{i}∈\mathcal R_x. In fact a witness monochromatic shortest path for S certifies every prefix of its specific direction order.

**Proof.** A shortest x→x⊕S path changes every coordinate of S once. Deleting its last edge leaves a monochromatic geodesic from x to x⊕(S\{i}) for the last direction i. Repeat for prefixes. QED.

**THEOREM 2 (explicit counterexample to full downward closure under active edge oddness).** On Q_3 choose the following binary colors for the 12 UNDIRECTED physical edges, written in the convention with coordinate bits (x_1,x_2,x_3) and the displayed bitstrings interpreted as subsets of coordinates, so '100' means e_1:
\[
\begin{array}{c|c}
\text{edge endpoints}&\text{color}\\\hline
000-100&0\\
001-101&0\\
010-110&1\\
011-111&1\\
000-010&0\\
001-011&1\\
100-110&0\\
101-111&1\\
000-001&1\\
010-011&0\\
100-101&1\\
110-111&0
\end{array}
\]
Each physical edge paired with its coordinatewise antipodal image has exactly complementary color, so the coloring is valid.

There is a monochromatic color-0 geodesic
\[
000\to100\to110\to111,
\]
so \(\{1,2,3\}\in\mathcal R_{000}\). But \(101\notin R(000)\): its only two geodesics from 000 are
\(000\to100\to101\), colored (0,1), and \(000\to001\to101\), colored (1,0), neither monochromatic. Thus \(\{1,3\}\notin\mathcal R_{000}\), despite being a subset of \(\{1,2,3\}\).

**CONSEQUENCE.** Even in the simpler edge-colored proving ground, antipodally odd monochromatic-geodesic reachability need NOT be an order ideal of the Boolean lattice. A proof using full downward closure, the ordinary face-KKM covering property for ALL lower-dimensional coordinate faces, or intersections of arbitrary reachable support subsets is INVALID without additional arguments. The TRUE invariant is *geodesic accessibility along SOME prefix chain*, not inclusion of every sub-support. This sharp distinction is essential when trying to extend the proven special parity-root chart connectivity to unrestricted NORI via a general topological reachability theorem.

## EXACT second-index criterion for a two-shore carrier with one contractible shore: an antipodal path IN THE OVERLAP

Let X be a finite simplicial or regular CW complex with a free cellular involution τ and a decomposition X=A∪τA by subcomplexes. Put C=A∩τA and assume A is NONEMPTY and CONTRACTIBLE (as an ordinary space). If C is empty, put index0. Otherwise the following conditions are EQUIVALENT:

(i) The first Stiefel–Whitney class w=w1(X→X/τ) has NONZERO square w²≠0 in H²(X/τ;F2), i.e. the cohomological antipodal index of X is AT LEAST TWO.

(ii) Some connected component C0 of the overlap C is invariant under τ: τ(C0)=C0.

(iii) The ONE-SKELETON of C contains a physical/abstract vertex u and a finite edge path from u to its involution mate τu.

(iv) There exists a continuous τ-equivariant map g:S¹→C (with antipodal half-turn on S¹).

**Proof (i→ii).** This is the previously proved general upper-index two-shore theorem nori_index_two_forces_antipodal_path_in_bichromatic_edge_overlap_20261008: if all C components occur in τ-exchanged pairs, assign ±1 to the two partners, producing an equivariant map C→S⁰; extend it over A to one closed semicircle and by τ over τA to the opposite semicircle, giving X→S¹. Such a map forces w²=0. Contraposition yields (i→ii).

**Proof (ii→iii).** Since C is a finite CW complex, its connected components are path-connected. Choose any vertex u in the τ-invariant component C0. Its mate τu is a vertex of the SAME component. A path in a CW complex can be homotoped into the 1-skeleton without altering endpoint vertices; cells of dimension>=2 do not join different components of the 1-skeleton. Hence u and τu are connected by an edge path entirely in C.

**Proof (iii→iv).** Parametrize an edge path γ:[0,1]→C from u to τu. Define g on the circle R/(2Z) by
  g(t)=γ(t), for 0<=t<=1;
  g(t)=τγ(t−1), for 1<=t<=2.
The two formulas match at t=1, because γ(1)=τu=τγ(0); they match at the identified endpoints t=0 and2 because τγ(1)=u. They also obey g(t+1)=τg(t), so g is a continuous equivariant S¹→C map.

**Proof (iv→i).** Since A is contractible, the composite g:S¹→C⊂A is ordinary nullhomotopic and extends to a disk G:D²→A. Apply the team's proved equivariant equator-capping theorem nori_equivariant_witness_equator_capping_raises_antipodal_index_20261008: glue G on the upper hemisphere of S² to τG on the lower hemisphere. This produces an equivariant map S²→X. The induced quotient RP²→X/τ pulls w back to the nonzero generator a∈H¹(RP²;F2), so w² pulls back to a²≠0. Thus w²≠0. QED.

**Exact NORI mixed-root PROFILE application (under the hypothetical absence of grand closure).** Let Ω be the ordered-terminal-pair/support label alphabet with involution τ(J,U)=(reverse J, D_J\U). For every physical root x, let L_x⊆Ω be the labels of ACTUAL either-color MONOCHROMATIC geodesic branches from x with terminal ordered pair J and preterminal support U. Let
  A=⋃_x Δ(L_x),
  K=A∪τA,
  C=A∩τA = ⋃_(x,y) Δ(L_x∩τL_y).
The universal one-coordinate 3-edge monochromatic branches give a common singleton-support apex to EVERY Δ(L_x), making A a CONE, hence contractible. The active grand conjecture is equivalent to C containing an edge {u,τu}, in which case the midpoint is fixed; so under a hypothetical no-closure assumption K carries a FREE τ-action. The exact criterion above yields:

  w1(K/τ)²≠0
  **IF AND ONLY IF**
  there exist label u∈Ω and a finite graph path
       u=u0—u1—...—um=τu
  in the 1-skeleton of the GENUINE mixed root-profile interface C.

Each edge ui—u_(i+1) of this graph lies in some simplex Δ(L_x∩τL_y), and thus has an explicit pair of physical-root witnesses certifying BOTH of its labels as monochromatically reachable from one root x and their complemented reversed-tail labels as reachable from a possibly other root y. The graph path need not retain a SINGLE common root along its successive edges; hence it does NOT automatically give a grand witness, nor is its endpoint u,τu necessarily an edge of C. The distinction between a τ-CONNECTING PATH and the desired τ-PAIR EDGE is the exact remaining combinatorial/topological shortening problem.

**Topological significance.** The second-index condition for the exact K carrier has become a FINITE GRAPH REACHABILITY question over real certified labels, not a mysterious abstract cup product. Higher w powers still require higher-dimensional overlap information; the equivalence established here is SPECIFICALLY for the nontrivial square w². No unconditional existence of an interface connecting path is claimed.

## Exact witness-root fiber dimension and the correct antipodal-reversal action in 2n-bit root/support geometry

Fix 1<=r<=k<=n, a direction-distinct k-edge cube geodesic with starting root x∈F2^n and ordered direction word pi=(p1,...,pk), and an arbitrary coloring of the PHYSICAL ORDERED r-faces. Its (k−r+1) ordered-r-face windows have free-coordinate sets
  W_j={p_j,p_(j+1),...,p_(j+r−1)} for j=1,...,k−r+1.
Define
  M(pi)=intersection_{j=1}^{k−r+1} W_j
       ={p_(k−r+1),...,p_r} if k<=2r−1,
       =empty if k>=2r.
Then |M(pi)|=max(2r−k,0).

**THEOREM 1 (exact physical-face root-fiber).** For a root translation vector h∈F2^n, the SAME ordered direction word pi, now starting at x+h, has EXACTLY THE SAME physical ordered r-face windows in ALL positions as pi rooted at x IF AND ONLY IF supp(h)⊆M(pi). Thus the set of starting roots realizing a given fixed COMPLETE sequence of ordered physical window faces and orders is exactly one coordinate affine cube
  x+span{e_i : i∈M(pi)}
of dimension max(2r−k,0). Every arbitrary binary color-word predicate (monochromatic, at most one switch, prescribed pattern, etc.) is constant on this actual face-certified root fiber.

**Proof.** The physical face of window j along pi is fixed by the cube bits OUTSIDE W_j. Translating the original starting root by h changes that face's exterior bit assignment precisely on supp(h)\W_j, regardless of prefix flips (the same fixed prefix appears for both roots). Therefore that window's physical face remains unchanged iff supp(h)⊆W_j. This must hold for ALL windows, i.e. supp(h)⊆intersection_j W_j=M(pi). Sliding equal-length consecutive windows have common positions [k−r+1,r] when this interval is nonempty, yielding |M|=2r−k; otherwise the intersection is empty. QED.

**THEOREM 2 (EXACT physical antipodal reversal in root/support coordinates).** Let U={p1,...,pk} be the USED coordinate support, D=[n]\U its UNUSED complement, and let bar denote bitwise complementation of physical cube vertices. Applying physical antipodal complementation and reversing the vertex sequence of the directed k-geodesic sends
  (root x, direction order pi)
    --> (root x XOR D, direction order rev pi).
Indeed the original endpoint is y=x XOR U, so the reversed-complemented geodesic root is bar y=x XOR U XOR [n]=x XOR D. The USED support is PRESERVED, NOT COMPLEMENTED, whereas the UNUSED root bits in D are all complemented.

For an ACTIVE ordered-r-face NORI-type coloring satisfying
  c(bar F,rev sigma)=1−c(F,sigma),
the color word of the transformed path is the reverse and bitwise complement of the original color word, preserving the exact number of switches.

This action is an involution on the full finite ordered-path state set; for k>=2 it is FIXED-POINT-FREE because the ordered direction word cannot equal its reverse when all directions are distinct. For k=n, D is empty and the ROOT is fixed, so antipodal path reversal acts purely by reversing direction order—important for any supposed root-bit topological Tucker labeling. For k<n, it complements precisely the unused root-coordinate bits and not the used support bits.

**COROLLARY 3 (critical ordered-three-face ranks).** For r=3 the exact fixed-path root-fiber dimensions are
  k=3:3, k=4:2, k=5:1, and k>=6:0.
Thus each genuine mono4 witness carries an entire 2D square of equally certified root states; mono5 carries a single rooted edge; mono6 carries no nontrivial coordinate root translation preserving ALL of its physical window faces. This geometric rank collapse is independent of coloring complexity.

**COROLLARY 4 (proper anti-symmetry of root-square carriers).** For fixed pi with 3<=k<=5 and used support U, the antipodal-reversal map sends the physical root-fiber cube
  x+span(M(pi))
to
  (x XOR D)+span(M(pi))
paired with the reversed direction word rev(pi) and complementary reversed window colors. The middle root-coordinate set is unchanged by order reversal, M(rev pi)=M(pi). This gives a rigorously defined free equivariant pairing of SAME-DIMENSION witness-root cubes.

**TOPOLOGICAL RESEARCH CONSEQUENCE.** The natural geometrical "2n bits" consist of an n-bit root and an n-bit progress/used-support coordinate; physical antipodal reversal of an actual short path has the support-preserving but EXTERIOR-complementing form above. Tucker's required FULL sign-vector anticomplementarity must be attached to genuinely reversed EXTERIOR root coordinates (or a proven alternative involution), not casually to USED support. Building a high-index path carrier beyond k=6 therefore requires genuine *coordinate-order exchanges, root slides between different path certificates, or memory-compatible support insertions*; one cannot infer high-dimensional filling from a single fixed geodesic's root-face cube, because its exact physical fiber is a point at k>=6. This is a proved geometry/cubical-fiber statement, not grand closure.

Deleted-product or equivariant index information becomes a closure theorem only after establishing that the selected simplex represents two physically compatible monochromatic tails. The converse obstruction examples explain the necessary hypotheses.
