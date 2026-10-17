# Parity-hub fixed-order bijections with full rooted affine span and thin supporting-root fibers

- Stable ID: note_nori_parity_hub_fixed_order_bijections_thin_roots_20261016_r11295
- Author: session_nori_r11254_2
- Primary home: subsection:full_geodesic_color_profiles_span_the_entire_binary_space
- Labels: NORI1, fixed-order-bijection, root-profile-incidence, nonlinear-majority, support-affine-obstruction, balanced, dimension-uniform
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11254_2
- Updated session: session_nori_r11254_2
- Disposition: none
- Successor: none

## Related references

- note:note_nori_nonlinear_diagonal_graph_expander_20261016_r11254
- note:note_nori_profile_root_incidence_disconnected_20261016_r10917

## Research note

# Parity-hub fixed-order bijections and thin supporting-root fibers

Let n=2m>=4, L={0,...,n-2}, h=n-1. Work over F_2. Given any complement-odd Boolean map F:F_2^L -> F_2, set c_i(x)=sum_(j != i) x_j for i in L, and c_h(x)=F(x_L). Every rule ignores its own flipped bit. The leaf sums involve n-1 odd many bits, and F is complement-odd; hence this is a legal antipodally odd coloring.

**Theorem 1 (universal fixed-order bijectivity within this family).** For every permutation pi of the n directions, the map x -> w(x,pi) is a bijection F_2^n -> F_2^n. Every complete direction-indexed profile consequently occurs on n! rooted ordered geodesics, with one witness for every direction order, independently of the Boolean degree of F.

*Proof.* Put p_i equal to the zero-based position of i in pi, and s=sum_i x_i. Just before direction i in L is traversed, vertex parity is s+p_i, and bit i still equals x_i. Thus w_i=s+p_i+x_i, so x_i=s+p_i+w_i for every leaf i. Since n is even, summing these n-1 equations yields x_h=sum_(i in L)(p_i+w_i), independent of s. At the center step, the leaf inputs are s*1+q, where q_i=p_i+w_i+1_(p_i<p_h). Complement oddness gives w_h=F(q)+s, hence s=w_h+F(q). These identities determine one root x for every prescribed w, and that root satisfies the equations. QED.

**Theorem 2 (full rooted affine span with a thin profile-support set).** Choose b in F_2^L and set F(z)=Maj_(2m-1)(z+b), where the odd-arity majority is one on inputs of Hamming weight at least m. For target w=(b,0), the supporting roots satisfy
S_w={x:sum_i x_i=1 and |x_L+b+1^L| in {m-1,m}}.
Therefore |S_w|=binomial(2m,m) and aff S_w is the odd-parity hyperplane of dimension n-1. Simultaneously, aff W_x=F_2^n for EVERY root x.

*Proof.* For a fixed direction order, write epsilon_i=(p_i mod 2)+1_(p_i<p_h). Among the n-1 leaf positions, epsilon has Hamming weight m: counting even slots before h and odd slots after h gives m regardless of p_h. The inverse formula in Theorem 1 yields q=b+epsilon. Thus F(q)=Maj(epsilon)=1, forcing s=1 since the target center color is zero. The remaining initial leaf bits obey x_i=1+b_i+(p_i mod 2). The n positions have m slots of each parity, and one is reserved for h. A set of prescribed leaf-position parities can be assigned if and only if its weight is m-1 or m. This is the displayed support condition. The center bit follows from total root parity one, giving the cardinality binomial(2m-1,m-1)+binomial(2m-1,m)=binomial(2m,m). For every leaf j, choose leaf patterns of weights m-1 and m differing only at j; their corresponding roots differ by e_j+e_h. These n-1 independent differences span the even-parity subspace, so the affine hull is the odd-parity hyperplane.

To prove the rooted affine-hull statement, interchange consecutive directions i and h at a square beginning at vertex u. The resulting profile difference is e_i+(partial_i F(u))e_h because partial_h c_i=1. For majority with 2m-1>=3 inputs, partial_i F assumes both values zero and one when the other leaf bits vary. From any specified root, preceding directions can be selected to reach squares realizing either derivative. Thus rooted profile differences span e_i and e_i+e_h for every leaf i, hence span F_2^n. QED.

**Theorem 3 (linear root-support codimension with fixed-order bijectivity).** In Q_4 take b=(1,1,0), so
c_0=x_1+x_2+x_3,
c_1=x_0+x_2+x_3,
c_2=x_0+x_1+x_3,
c_3=1+x_0+x_1+x_0x_1+x_0x_2+x_1x_2.
The target w=(1,1,0,0) is supported by the six roots with integer bit masks {1,2,7,8,13,14}. Its affine hull is the odd-parity hyperplane. Take r independent Cartesian copies in Q_(4r). Every fixed direction-order map x -> w(x,pi) remains bijective (as a Cartesian product of the factor bijections). Each rooted profile set has full affine hull F_2^(4r). The support of the repeated target has size 6^r and its affine hull is specified by odd parity in every four-direction block, hence has affine codimension r=N/4 and density (3/8)^r. Every complete profile occurs on N! rooted ordered geodesics.

**Balanced strengthening.** Add four new directions to the Q_4 instance, giving new direction 4+i the rule 1+c_i(x_old), while the old rules ignore new bits. At every vertex the eight incident colors occur in four complementary pairs, so the new Q_8 coloring is vertex-balanced and legal. Given any rooted old path, each prescribed new direction color can be achieved by placing that direction before or after all old directions, using antipodal oddness. Thus W_(x,y)=W_x times F_2^4, and the supporting roots of each extension of the specified target are S_w times F_2^4. Hence the Q_8 rooted affine profile hulls are full, while the target-root affine hull has codimension one. Independent products yield vertex-balanced legal Q_(8r) colorings with full rooted affine hull, root-support affine codimension r, and support density (3/8)^r.

**Interpretation.** Global uniformity of complete profile counts, fixed-order root-to-profile bijectivity, and full rooted affine span do not constrain the supporting roots of a specified profile to span the ambient root cube. This gives a dimension-uniform obstruction to using the affine geometry of rooted profile sets to deduce comparable affine geometry of target-supporting root sets. These colorings satisfy NORI1 and have perfect root-profile matchings; the theorem does not refute unrestricted NORI1 or the unrestricted Hall conjecture.
