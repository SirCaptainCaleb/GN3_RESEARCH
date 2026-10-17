# Universal profiles, saturation, and nonbinary rooted delta-matroids

- Stable ID: note_nori_common_diagonal_odd_reader_cycles_20261016_r11254
- Author: session_nori_r11401_1
- Primary home: subsection:full_geodesic_color_profiles_span_the_entire_binary_space
- Labels: NORI1, saturation, delta-matroid, nonbinary, unary-reader, symmetric-exchange, dimension-uniform
- Lifecycle: active
- Epistemic status: proved
- Current version: 8
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11254_2
- Updated session: session_nori_r11401_1
- Disposition: none
- Successor: none

## Related references

- note:note_nori_profile_integrability_three_local_laws_20261016_r11254
- note:note_nori_cyclic_profile_hall_countermodel_20261016_r11254

## Research note

# Odd reader cycles obstruct common root-profile translations

Let W_x(c) be the attainable full-geodesic direction-color profiles from x, and put D(c)=intersection_(x in Q_n)(x+W_x(c)). A signature z in D(c) gives a perfect root-profile matching x -> x+z and hence implies NORI1.

**Theorem (complete criterion for unary reader rules).** Suppose c_i(x)=alpha_i+x_(r(i)), with r(i)!=i, for each direction. Form the directed reader graph i -> r(i). Then D(c) is nonempty if and only if all directed reader cycles have even length. In that case D(c) consists of all z satisfying
sum_(i in C)(z_i+alpha_i)=1
for every directed reader cycle C, with unrestricted bits outside the cycles.

*Proof.* For a direction order pi the color recorded in direction i is w_i=alpha_i+x_(r(i))+t_i, where t_i=1 precisely when r(i) precedes i. Prescribing w=x+z forces
t_i=z_i+alpha_i+x_i+x_(r(i)).                                  (1)
These prescribed precedence inequalities admit a common total order if and only if they have no directed cycle. Each weak component of the reader graph has one cycle, including a doubled edge in a reader 2-cycle; the remaining edges belong to trees. The precedence graph has a directed cycle precisely when, on one reader cycle C, every t_i=0 or every t_i=1.

For a reader cycle C of length ell, as x varies, the vector b_i=x_i+x_(r(i)) ranges through the even-parity subspace of F_2^ell: its sum vanishes and the cyclic linear difference map has rank ell-1. Therefore t restricted to C ranges through the parity class of z_C+alpha_C.

If ell is odd, that parity class contains one of 0^ell and 1^ell, so some root prohibits a total order. Therefore D(c) is empty if an odd reader cycle exists. If ell is even, the two constant vectors have even parity. A cycle with sum_(i in C)(z_i+alpha_i)=0 has a root for which t=0^ell, making z inadmissible. With sum one, t has odd parity at every root and cannot be constant; this cycle is then always orderable. Conditions on disjoint reader cycles are independent, and trees add no cycles. Topological sorting of the required precedence graph proves the converse and the full description of D(c).

**Sharp dimension-three counterexample.** Let c_0=x_1, c_1=x_2, c_2=x_0 on Q_3. The reader graph is a 3-cycle, hence D(c)=empty. Every root realizes six of the eight complete profiles, and every candidate translation fails at two antipodal roots. Nevertheless for any fixed permutation pi the map x -> w(x,pi) is bijective, being (x_1,x_2,x_0) plus a fixed vector. Thus a perfect root-profile matching can exist even when there is no common diagonal translation. The obstruction persists for every n>3 by adjoining reader directions c_j=x_0: projection of any full profile onto directions 0,1,2 remains a profile of the three-dimensional example. In Q_2 the only reader cycle has length two, so a common translation always exists.

This is an explicit all-dimensional obstruction to translation-based forcing, distinct from the formal Hall countermodel: the displayed coloring is legal and already possesses a perfect root-profile matching.

**Uniform incidence and perfect matching theorem for unary reader rules.** Let C_1,...,C_s be the directed reader cycles, with lengths ell_j>=2, and put m=n-sum_j ell_j. For every root x, the number of distinct attainable complete profiles is
d=2^m product_(j=1)^s (2^(ell_j)-2).
Every complete profile w is supported by d roots. Hence the bipartite root-profile incidence graph is d-regular and admits a perfect matching.

*Proof.* For a specified root x, the map from precedence bits t in (1) to profile w is a bijection. Such a t is feasible if and only if on each reader cycle C_j its entries are not all equal. There are 2^(ell_j)-2 choices on C_j and two unrestricted choices on each tree direction, giving d. For a specified word w, the cyclic reader map x_(r(i)) permutes the ell_j vertex bits on a reader cycle. The condition that t=w+alpha+x_r is nonconstant excludes two of its 2^(ell_j) assignments, leaving 2^(ell_j)-2 choices for x on that cycle. All m tree-root bits are unrestricted, giving d roots. A finite regular bipartite graph with equal side sizes has a perfect matching by Hall's inequality, as counting edges from any root set gives d|A|<=d|N(A)|. This concludes the proof.

In the three-cycle example d=6: a single fixed direction order even induces a permutation of the eight roots onto the eight profiles. The absence of a common signature thus does not interfere with the matching theorem. This regularity mechanism relies on the unary dependence and makes no claim about arbitrary nonlinear colorings.

**Theorem (delta-matroid structure of all rooted unary-reader profiles).** For every starting root x, the complete profile family W_x of a unary legal coloring c_i(x)=alpha_i+x_(r(i)), with r(i)!=i, is a delta-matroid feasible-set family, interpreted as subsets of the direction set via binary incidence vectors. More precisely, if T denotes the noncycle vertices of the functional reader graph and C_1,...,C_s its directed cycles, then W_x is a binary translate of
F_2^T times product_(j=1)^s (F_2^(C_j) \ {0^(C_j),1^(C_j)}).

*Proof.* Given a root x, define t_i=w_i+alpha_i+x_(r(i)). This equals one if reader r(i) precedes i. Prescribing t defines one precedence inequality per direction. These can be simultaneously satisfied if and only if each directed reader cycle has neither all its inequalities clockwise nor all counterclockwise: equivalently t restricted to each cycle is neither identically zero nor identically one. Every tree edge can be oriented as its t_i prescribes without introducing a directed cycle. Topological sorting then realizes any such t. This gives the product representation.

It remains to prove symmetric exchange for D_l=F_2^l\{0^l,1^l} for l>=2. Let u,v be feasible and i lie in their symmetric difference. If u+e_i is feasible, choose the exchange partner j=i. Otherwise u+e_i is constant, so u is either e_i or 1+e_i. In the former case v_i=0; since v is nonconstant there is j!=i with v_j=1, so j differs between u and v, and u+e_i+e_j=e_j is feasible. In the latter case v_i=1; since v is nonconstant there is j!=i with v_j=0, and u+e_i+e_j=1+e_j is feasible. Hence D_l satisfies symmetric exchange. Full binary cubes do as well. Translates and Cartesian products of delta-matroid feasible families preserve symmetric exchange, proving the theorem.

**Theorem (sharp universal rooted profile bound).** Let c be ANY legal NORI1 coloring and let s(x)=(c_i(x)) be the vector of colors incident to root x. Then s(x) and 1+s(x) are both absent from W_x. Thus |W_x|<=2^n-2 in every dimension n>=2. Equality is achieved for every n>=2 by a unary cyclic reader system with r a single n-cycle; moreover such systems are the only unary reader graphs attaining equality for n>=3.

*Proof.* The first edge of every rooted full geodesic has color c_i(x), ruling out the all-complemented target 1+s(x). Its last edge in direction j is at vertex bar x+e_j and has color c_j(bar x+e_j)=c_j(bar x)=1+c_j(x), ruling out s(x). For a cyclic unary reader graph with one cycle covering all n directions, the product formula above shows W_x is a translate of F_2^n\{0,1}, giving equality. Conversely if a reader graph has a cycle of length l<n, then its rooted profile count 2^T product_j(2^|C_j|-2) is at most 2^n(1-2^(1-l))<2^n-2. The same strict inequality holds when there is more than one cycle. Thus equality among unary graphs requires one spanning cycle.

**Computational audit, beyond legal matrices.** For every zero-diagonal 5x5 binary matrix A, the rooted affine permutation-profile family B(A)={b(pi):pi in S_5}, b_i(pi)=sum_(j before i)A_ij, satisfies symmetric exchange. This is an exhaustive test of 2^20=1,048,576 matrices, including 32,768 legal matrices. Independent random tests extend to higher dimensions, but the general affine delta-matroid assertion remains unproved. The unary theorem above supplies a dimension-uniform proved subclass; its proof does not rely on the finite test.

**Unrestricted one-root saturation theorem.** For an arbitrary legal antipodally odd coloring c of Q_n, let s(x)=(c_i(x)) be its incident-edge color vector. If some root x satisfies |W_x|=2^n-2, then the GLOBAL attainable profile set W(c) equals F_2^n; consequently the coloring has a monochromatic antipodal full geodesic. More precisely, each of the two words s(x) and 1+s(x), which are absent from W_x, occurs at every Hamming neighbor x+e_i of x.

*Proof.* The first and last edge constraints prove s(x),1+s(x) are absent from W_x, so saturation gives W_x=F_2^n\{s(x),1+s(x)}. For each direction i, profile s(x)+e_i is supported at x. In any realizing order its last direction must be i, since the last direction j has color 1+s_j(x), while the proposed word agrees with s_j(x) at all j!=i. Moving that final direction to the beginning by inverse cyclic geodesic rotation moves the root from x to x+e_i and changes only profile bit i, producing s(x). Similarly, 1+s(x)+e_i is supported at x, and its first direction must be i because the first direction j has color s_j(x). Forward cyclic rotation starts at x+e_i and changes profile bit i, producing 1+s(x). All other profiles are already realized at x, proving the theorem.

**Unrestricted Hall theorem at maximal rooted profile degree.** If |W_x|=2^n-2 for every root x of a legal coloring, then its bipartite root-profile incidence graph has a perfect matching, in any dimension n>=2.

*Proof.* Rooted profile sets are invariant under taking the antipodal root and under complementing every profile bit. Therefore quotient the incidence graph by antipodal root pairs and antipodal profile pairs. Each left vertex in this quotient is adjacent to every one of its M=2^(n-1) right vertices except the unique pair {s(x),1+s(x)}. By the one-root saturation theorem, every right vertex has at least one neighbor. The quotient satisfies Hall: a singleton left set has M-1>=1 neighbors; a set of two or more left vertices with differing forbidden right vertices sees all M right vertices; and a set with common forbidden right vertex sees M-1 neighbors, while it cannot have all M left vertices because each right vertex has a neighbor. Hence every left subset has at least its cardinality of neighbors. A quotient perfect matching lifts to a perfect matching of the original graph because each allowed pair of antipodal pairs forms K_(2,2). QED.

The hypothesis in the first statement requires saturation at only one root, whereas the Hall assertion assumes saturation at every root. Rooted profile cardinalities need not be root-independent in nonlinear legal colorings; the stronger assumption in the Hall statement is essential to the argument.

## Universal profile half-spaces and failure of incidence transpose duality

**Theorem (dimension-uniform universal profiles).** For every n>=4 there exists a legal antipodally odd coloring c of Q_n whose universal profile set U(c)=intersection_(x in Q_n) W_x(c) has 2^(n-1) members, while every root supports only 7*2^(n-3) profiles. The coloring has full rooted affine profile span and connected root-profile incidence. For every even n>=8 it can also be made vertex-balanced while preserving these statistics. In all examples a universal profile has 2^n supporting roots, and every non-universal profile has 3*2^(n-2) supporting roots.

*Four-dimensional construction and proof.* Work over F_2. Put c_0(x)=1+x_2, c_1(x)=x_0+x_2+x_3, c_2(x)=1+x_1, and c_3(x)=x_2. Each rule ignores its direction bit and depends on an odd number of input bits, hence is legal. Let s(x)=(c_i(x)) be the star-color word. For a direction order pi, write [i<j] for the precedence indicator. Its profile is
w_0=1+x_2+[2<0],
w_3=x_2+[2<3],
w_2=1+x_1+[1<2],
w_1=x_0+x_2+x_3+#[j in {0,2,3}:j<1] mod 2.

Given any x and any target w with w_0=w_3, place the triple {0,2,3} in order (0,2,3) if the common target bit is 1+x_2, or in order (3,2,0) if it is x_2. This fixes w_0,w_3. Insert direction 1 into one of the four slots. There are two slots before direction 2 and two after; choosing the side fixes w_2, while the parity of the number of triple directions preceding 1 varies between the two slots on that side, allowing either w_1. Therefore every w with w_0=w_3 is attainable from every root.

Conversely s_0(x)=1+s_3(x). Every word w with w_0!=w_3 occurs as a star word s(x): set x_2=w_3, x_1=1+w_2, x_0=0, x_3=w_1+w_3. Such w cannot occur from that root, since the last direction i of any full geodesic has color 1+s_i(x). Hence the universal set is the 8-word affine hyperplane U_4={w:w_0=w_3}.

More strongly, each rooted profile set is W_x=F_2^4\{s(x),1+s(x)}. To see this, when direction 2 is outside the interval between 0 and 3, the recorded bits w_0,w_3 are unequal. The two possible sides for direction 2 and the four slots for inserting direction 1 generate three of the four combinations of (w_1,w_2) for each fixed unequal pair (w_0,w_3). The missing combinations are s(x) and 1+s(x). The eight equal-bit profiles were already constructed. The map x->s(x) takes the eight unequal-bit words, each at two starting roots. Hence each unequal-bit profile is absent from precisely four roots (those satisfying s(x)=w or s(x)=1+w), and is supported at twelve; equal-bit profiles are supported at all sixteen. All rooted sets have fourteen profiles and full affine span; the incidence is connected because all roots share universal profiles.

*Dimension and balance extensions.* For n>4 retain these four rules and append reader rules c_j=x_0 for directions j>=4. Reader steps do not affect the old rules and may be placed independently before or after all old directions, giving either desired reader color. Thus W_(x,y)=W_x^(4) times F_2^(n-4). Universal profiles are precisely those with w_0=w_3, their count is 2^(n-1), rooted degree is 7*2^(n-3), and the two supporting-root counts are 2^n and 3*2^(n-2).

For even n>=8, instead append four new directions 4+i colored 1+c_i(old), i=0,1,2,3, then any required additional complementary reader pairs x_0 and 1+x_0. Each old-new or extra reader pair has opposite incident colors, proving vertex balance. All these rules depend only on old bits, and every new direction can be placed before or after the old full path to realize its requested color. The same product identity, rooted support, universal half-space, full rooted affine span and incidence connectivity hold.

**Corollary (incidence transpose non-realizability).** The class of bipartite root-profile incidence relations of legal colorings is not closed under transposition, for every n>=4, even when restricted to vertex-balanced colorings in even n>=8. Indeed, the last-edge and first-edge constraints forbid s(x) and 1+s(x) from W_x in every legal coloring, so no legal incidence matrix has a full root row. The constructed matrices have full profile columns because half their profiles are attained from every root. Their transposes therefore have full rows and cannot be legal incidence matrices, even up to independent relabeling of each bipartition.

By toggling one direction rule by a constant, the universal half-space becomes {w:w_0!=w_3}, which contains neither monochromatic word. Thus universal support of many arbitrary profiles does not by itself give a universal monochromatic profile.

**Independent audits.** Exhaustive order enumeration for n=4,5,6 and the balanced n=8 construction checked 384,3840,46080,10321920 rooted full geodesics respectively, with zero discrepancies in rooted profiles or support counts. An exhaustive census over all 65536 legal Q4 colorings found numbers of universally supported profiles 0,2,4,8 only, attained by 60352,3072,1536,576 colorings respectively. This establishes the computational maximum eight in Q4; no higher-dimensional universal upper bound is asserted.

The theorem concerns the asymmetry of the incidence representation and does not disprove NORI1 or the perfect-matching conjecture. The displayed families possess perfect matchings and monochromatic antipodal geodesics.

**Universal-profile symmetric exchange fails in Q4 (sharp dimension).** For a legal coloring c put U(c)=intersection_(x in Q_n) W_x(c). There is a legal Q4 coloring with U(c)={1,14} in integer direction-mask notation. It is an affine line, yet violates delta-matroid symmetric exchange: with u=1, v=14, and selected differing direction i=0, the permitted exchanges from u give masks 0,2,4,8, none belonging to U(c). Every rooted profile family of this coloring has at least ten words and full affine span F2^4; its root-profile incidence graph is connected. Reader lifts preserve the failure in every dimension n>=4, and complementary reader lifts give vertex-balanced examples in every even dimension n>=8.

*Explicit coloring.* Over F2 take
c_0=x_1x_2+x_1x_3+x_2x_3;
c_1=x_0+x_2+x_3;
c_2=x_0+x_0x_1+x_3+x_0x_3+x_1x_3;
c_3=x_2.
Each rule ignores its own direction bit and toggles under complementing its three remaining arguments, so c is legal.

*Finite proof certificate.* For each root x enumerate the 24 direction orders and accumulate its complete profile mask M_x=sum_(w in W_x)2^w. The rooted masks for x=0,1,...,7 are respectively
5ffa, fdbf, 5ffa, cff3, fa5f, eff7, f66f, f81f
in hexadecimal notation. Antipodal reversal gives M_(15-x)=M_x. The bitwise intersection of these eight masks is 4002, whose set bits are 1 and 14. Their minimum population is ten, exceeding the maximum eight points of an affine hyperplane of F2^4. Hence every rooted affine span is full. Any two rooted profile sets intersect since 10+10>16, so incidence is connected. A separate direct-permutation verifier checks every one of the 384 rooted paths.

*Lifts and minimal dimension.* For any n>4 append reader directions c_j=x_0. Their colors can be independently selected by putting each reader before or after the four old steps, giving W_(x,y)=W_x times F2^(n-4), and hence U_n={1,14} times F2^(n-4). The symmetric-exchange witness survives by taking equal new-direction entries. For even n>=8, instead append four complementary rules c_(4+i)=1+c_i, and further complementary reader pairs x_0,1+x_0 if needed. These give vertex balance and the same profile factorization.

For n=2 or3, every complement-odd rule on the other n-1<=2 inputs has form c_i=a_i+x_(r(i)) with r(i)!=i. The functional reader graph contains a directed cycle C. Given any candidate universal word w, choose root bits x_(r(i))=w_i+a_i along C. Every path with profile w would require i to precede r(i) around the entire cycle, which is impossible. Thus U(c)=empty for every legal coloring in dimensions two and three. Dimension four is the first with a nonempty universal-profile family violating symmetric exchange.

*Full Q4 census.* All 65536 legal four-dimensional colorings were enumerated using their 16 independent antipodal edge-orbit bits. The universal-profile cardinalities 0,2,4,8 occur for 60352,3072,1536,576 colorings respectively. Every nonempty U is affine, but precisely the 3072 two-word universal families fail symmetric exchange. This distinguishes universal affineness from the exchange axiom.

*Correction to the prior Q5 calculation.* The previously verified U={2,4,6,13,18,25,27,29} is nonaffine and ALSO violates symmetric exchange. For u=2,v=13,i=0 its four candidate exchanges are 3,1,7,11; all are absent. Hence universal symmetric exchange already fails in Q4, while nonaffineness of universal families first appears in Q5. Neither construction refutes NORI1 or the still-unproved exchange conjecture for rooted profiles of affine legal colorings.

**Affine universal-profile nonaffineness under complete rooted saturation.** For every odd n>=5 there is a legal affine coloring with |W_x|=2^n-2 at EVERY root but with a nonaffine universal-profile set U(c) of cardinality 2^n-8. Specifically take
c_0=x_1,  c_1=sum_(j=2)^(n-1)x_j,  c_j=x_0 for 2<=j<n.
The middle rule reads n-2 odd many input bits, so all rules ignore their own direction bit and are complement-odd. Define s(x)=(x_1,sum_(j>=2)x_j,x_0,...,x_0). Then
W_x=F2^n\{s(x),1+s(x)}
for every root x.

*Proof.* Fix x,w and let t_j=w_j+x_0 for the leaf directions j>=2. Then t_j=1 iff direction 0 precedes j in the order. Likewise b=w_0+x_1=1 iff direction 1 precedes 0. Put p=sum_(j>=2)x_j and q=w_1+p; q must equal the parity of the leaves preceding direction 1. If t has both a zero and a one, at least one leaf lies on either side of direction 0. Whether direction 1 is before or after direction 0, one can insert it on its prescribed side before or after a leaf, realizing either q parity. If all t_j=0, every leaf precedes 0: when b=1 the parity q is arbitrary, while when b=0 it is forced to 1 because all n-2 odd many leaves precede 1. Thus the sole forbidden word of this type is b=q=0, namely s(x). If all t_j=1, every leaf follows 0: when b=0 the parity q is arbitrary, while b=1 forces q=0. The sole forbidden word of this type is b=q=1, namely 1+s(x). This proves the rooted saturation identity.

The image of the incident-color map x->s(x) is the eight-word affine subspace E={w:w_2=...=w_(n-1)}: the three bits x_1, sum_(j>=2)x_j, x_0 vary independently. Since E is closed under complementing every bit, the universal profile family is
U(c)=F2^n\E=F2^{\{0,1\}} times (F2^{n-2}\{0,1}).
Its size 2^n-8 is not a power of two, so it is nonaffine. Every member of U(c) has all 2^n supporting roots; each of the eight profiles in E has 3*2^(n-2) supporting roots, because each excluded star-vector value has 2^(n-3) root preimages. Every root has degree 2^n-2, so the previously proved universal saturation Hall theorem supplies a perfect matching. The family U(c) does satisfy symmetric exchange, since the nonconstant-vector factor does, despite failing affine closure.

For even N>=6, append one direction with reader rule x_0 to the N-1-dimensional odd example. Its profile sets factor with F2 in the new direction, giving |U|=2^N-16 and nonaffineness. Thus legal affine examples with nonaffine universal profile sets occur in every dimension n>=5, improving the previous nonlinear Q5 construction. For any even N>=10, choose odd m>=5 with N=2m or N=2m+2, append complementary reader directions 1+c_i to all m old directions, and add an extra complementary pair x_0,1+x_0 if necessary. The resulting coloring is legal and vertex-balanced; profiles factor, so U remains nonaffine and the universal-profile density tends to one.

A standalone verifier enumerates every root and direction order in dimensions n=5 and n=7, respectively 3840 and 645120 paths, and confirms legality, rooted saturation, and the U formula. The affine rooted symmetric-exchange conjecture remains open, as does unrestricted NORI1.

## Rooted saturation produces nonbinary delta-matroids

Identify each profile with its support subset of E=[n]. For a symmetric binary matrix S indexed by E let D(S)={X subset E:det S[X]=1}, where det of the empty matrix is one. A binary-representable delta-matroid is a twist D(S) triangle T for some T subset E; its feasible sets are {X triangle T:X in D(S)}.

**Theorem (dimension-uniform failure of binary representability).** Let n>=3. The delta-matroid D_n=2^E\{empty,E} is not binary-representable. Consequently, if ANY legal antipodally odd coloring attains the maximal rooted profile count |W_x|=2^n-2 at a root, that rooted profile family is a nonbinary delta-matroid. Such saturated legal affine colorings exist in every dimension n>=3, for example the directed unary reader cycle c_i(x)=x_(i-1 mod n).

*Delta-matroid property.* Let u,v be nonconstant binary words and i a differing bit. If u+e_i is nonconstant, symmetric exchange holds with partner i. Otherwise u+e_i is constant. If u=e_i, then v_i=0 and v has a one in some other position j, yielding u+e_i+e_j=e_j, which is nonconstant. If u=1+e_i, then v_i=1 and v has a zero in another position j, yielding u+e_i+e_j=1+e_j, also nonconstant. Hence D_n obeys symmetric exchange.

*Three-direction obstruction.* Suppose D_3=D(S) triangle T, with S symmetric. The empty set is feasible for D(S), so T is feasible for D_3: T must be a nonempty proper subset of E. Since the two excluded subsets of D_3 are complementary, we may replace T with its complement and relabel so that T={a}. Then D(S) is all subsets except {a} and {b,c}. In particular S_aa=0, S_bb=S_cc=1. Nonsingularity of principal pairs {a,b} and {a,c} gives S_ab=S_ac=1; singularity of principal pair {b,c} gives S_bc=1. The rows b and c of S are therefore identical, making det S[E]=0. But E must be feasible in D(S), a contradiction.

*All higher dimensions.* The three-element family H=2^[3]\{empty} is also nonbinary. Indeed if H=D(S) triangle T then T is nonempty and D(S) is missing only T. If T is a singleton a, all other diagonal entries are one; requiring all principal pairs nonsingular forces S_ab=S_ac=1 and S_bc=0, making the principal triple singular. If T is a pair {a,b}, every diagonal is one; all other principal pairs nonsingular force S_ab=1 and S_ac=S_bc=0, again making the triple singular. If T=E, all singleton and pair minors are nonsingular, so S=I and det S[E]=1, contradicting the missing triple.

For n>3, restrict D_n to a three-element subset Q by fixing every profile bit outside Q to zero. Since the complement-excluded word E has a one outside Q, this restriction is H. Binary-representable delta-matroids are closed under such nonempty restrictions: twist by one feasible word in the restriction, use the principal-pivot determinant identity to represent the twisted family by a symmetric matrix with empty feasible, and delete the outside indices by passing to its principal submatrix. Therefore D_n cannot be binary-representable.

*Application to arbitrary legal colorings.* The first and last edge restrictions imply that the incident-color word s(x) and its complement are absent from W_x. If |W_x|=2^n-2, then W_x=s(x)+D_n. Twists preserve binary representability, so W_x is nonbinary for n>=3. The directed n-cycle reader coloring has W_x equal to a translate of D_n because specifying a profile fixes each directed cyclic precedence inequality, which is orderable precisely when those inequalities are not all equal. Thus saturated nonbinary rooted profile systems occur in legal affine colorings at every n>=3. In dimension n=2 the family D_2 is binary-representable, as the twist of the feasible minors {empty,E} of the alternating matrix with off-diagonal ones.

This does not refute the affine symmetric-exchange conjecture: D_n itself obeys symmetric exchange. It proves that arguments relying on binary symmetric-matrix representations cannot cover all legal affine or unrestricted rooted profile families, including the saturated systems used in the one-root NORI1 forcing theorem.
