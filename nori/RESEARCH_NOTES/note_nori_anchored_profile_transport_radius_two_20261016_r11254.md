# Full-affine-span and balanced obstructions to anchored profile transport

- Stable ID: note_nori_anchored_profile_transport_radius_two_20261016_r11254
- Author: session_nori_r11254_2
- Primary home: subsection:full_geodesic_color_profiles_span_the_entire_binary_space
- Labels: NORI1, root-profile-transport, full-affine-span, balanced, dimension-uniform
- Lifecycle: active
- Epistemic status: proved
- Current version: 4
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11254_2
- Updated session: session_nori_r11254_2
- Disposition: none
- Successor: none

## Related references

- note:note_nori_profile_root_incidence_disconnected_20261016_r10917
- note:note_nori_partial_profiles_one_switch_equivalence_20261016_r10917

## Research note

# A one-bit profile change can require two root flips

**Theorem.** For every n>=4 there is a legal antipodally odd coloring of Q_n and two attained full-geodesic profiles u,u+e_3 such that u is witnessed at root 0, while every root witnessing u+e_3 has Hamming distance at least two from 0; a witness at distance two exists. Therefore root transport of an individually specified attained word cannot always modify one profile bit while moving its starting root at most one edge.

**Construction.** Over F_2, put
c_0(x)=1+x_3,
c_1(x)=x_0+x_3+x_0 x_2+x_0 x_3+x_2 x_3,
c_2(x)=1+x_1,
c_3(x)=x_0,
and c_j(x)=x_0 for j>=4.
Each rule ignores its own bit. Each rule is odd under global complementation: this is immediate for the unary rules, while complementing all three inputs of c_1 leaves x_0+x_3 unchanged and complements the sum of the three pair products (each variable appears twice in their linear expansion and the constant changes by 1). Thus the coloring is legal.

Set u=(0,0,0,0,1,...,1). From root 0, the full direction order (1,2,3,0,4,...,n-1) witnesses u: the first four traversed edges have color 0, and every later edge has color x_0=1.

**Root-support lemma in Q_4.** For the first four rules, the profile e_3 has supporting roots
S_(e_3)={x:x_0+x_3=1 and x_1+x_2=1}={3,5,10,12},
where the last set uses binary integer vertex masks.

*Proof.* The pair c_0=1+x_3 and c_3=x_0 implies w_0+w_3=x_0+x_3 regardless of their relative traversal order. Thus w=e_3 forces x_0+x_3=1. To achieve w_0=0,w_3=1, traverse 3 before 0 when (x_0,x_3)=(1,0), and 0 before 3 when (x_0,x_3)=(0,1). At every intermediate position in either ordering, at least one of the currently held bits a,d in directions 0,3 is one.

The condition w_2=0, using c_2=1+x_1, requires direction 1 to precede direction 2 if and only if x_1=0. Hence at the traversal of direction 1, its input bit in direction 2 is b=x_1+x_2. Its color is
c_1=a+d+ab+ad+bd,
which equals a OR d if b=0 and equals ad if b=1. Because a OR d=1 throughout the required 0/3 order, w_1=0 forces b=1, or x_1+x_2=1.

Conversely suppose both parity equations hold. Traverse (1,2) if x_1=0 and (2,1) if x_1=1; then traverse (3,0) if x_0=1 and (0,3) if x_0=0. The direction-2 edge is red, direction 1 has b=1 and (a,d) equal (1,0) or (0,1), and the final 0/3 pair has colors (0,1). The resulting profile is e_3. QED.

**All-dimensional lift.** The first four color rules are independent of the remaining vertex bits. Projecting any full Q_n geodesic to these four directions preserves the root's first four bits and the profile restricted to them. Hence every root z witnessing u+e_3 has z_0+z_3=z_1+z_2=1, and d_H(z,0)>=2. At the root whose first four bits are (0,1,0,1) and whose others vanish, the order (0,2,3,1,4,...,n-1) realizes u+e_3: the first four profile entries are e_3 and all subsequent edges have color 1. This root is at distance two. QED.

**Scope.** Both profiles occur globally; the result refutes specified-witness radius-one transport rather than unconstrained adjacency between their supporting-root sets. It is compatible with the known cyclic root-slide identity, which flips the first traversed direction's profile bit, and it does not refute NORI1.

**Minimal dimension: the radius-one property holds in Q_2 and Q_3.** In Q_2, every legal rule is unary: c_0=x_1+alpha_0, c_1=x_0+alpha_1. At each root the rooted profile set is all two-bit words with parity w_0+w_1=x_0+x_1+alpha_0+alpha_1+1, so changing one profile bit is possible after changing one starting bit.

In Q_3, every legal rule is likewise unary, because a Boolean function on its two other input bits that changes value under simultaneous complementation must equal one of those input bits plus a constant. Write c_i=x_(r(i))+alpha_i with r(i) != i. The functional digraph r has either (a) a directed three-cycle, or (b) a directed two-cycle with its third vertex pointing into the cycle.

In case (a), write b_i(x)=x_(r(i))+alpha_i. The requested word w imposes a precedence orientation between each i and r(i), and a permutation realizes w if and only if that orientation is acyclic. For a directed three-cycle, precisely the two words b(x),1+b(x) make a cyclic precedence orientation. Hence the rooted profile set is F_2^3 minus {b(x),1+b(x)}. If a target word is absent at x, changing ANY one starting bit alters one component of b, so that target differs from each new forbidden word and becomes attainable at the adjacent root. Otherwise it already occurs at x.

In case (b), let a,b be the mutual readers and t the remaining direction. All rooted profiles obey w_a+w_b=x_a+x_b+alpha_a+alpha_b+1. Conversely each word with this parity is attained: choose the relative order of a and b to obtain the specified pair, and independently place t before or after its reader to obtain either prescribed t-color. Changing w_t leaves the profile attainable at x; changing w_a or w_b becomes attainable by toggling x_a or x_b. This proves radius-one anchored transport in Q_3. Thus the four-direction quadratic example above occurs in the smallest dimension admitting a failure.

## Strengthening: full rooted affine span with a single nonlinear direction

**Theorem.** For every n>=4, the preceding anchored radius-two obstruction can be witnessed by a legal coloring for which the affine hull of the full direction-profile set at EVERY root is F_2^n. Only one direction rule is nonlinear. In its four-direction core, the target profile e_0 is supported precisely at the six roots of Hamming weight two.

**Construction.** On Q_4 set
c_0(x)=x_1x_2+x_1x_3+x_2x_3,
c_j(x)=sum_(k in {0,1,2,3}\{j}) x_k for j=1,2,3,
with all arithmetic in F_2. Thus c_0 is the three-bit majority rule, while the other rules are parity functions of their three other input bits. All four are independent of their own direction bits and odd under simultaneous complementation. For n>4 retain these old rules and put c_j(x)=x_0 for j>=4.

Put u=e_0+e_1+sum_(j>=4)e_j. The root 0 supports u using order (2,1,3,0,4,...,n-1). The adjacent target u+e_1=e_0+sum_(j>=4)e_j is supported at root e_0+e_1 using order (2,4,...,n-1,0,3,1); the new directions precede 0 while its bit is one. Both orders reduce to their stated four-direction orders when n=4.

**Root-support proof.** Project to Q_4, where the target word is e_0. For a rooted order pi, write p_j for the zero-based position of leaf direction j and s for the Hamming weight of its starting root x. When the leaf edge j is used, the current vertex has bit parity s+p_j, and the unflipped j-th bit is x_j. Hence
w_j=s+p_j+x_j (mod 2), j=1,2,3.
To obtain e_0, all three leaf colors must vanish, requiring p_j=s+x_j (mod 2). If s=0, all three leaves require even positions, impossible because there are only two even positions. If x=e_0, all three require odd positions, equally impossible. If x=e_j with j in {1,2,3}, direction j must occupy an even position and the other two leaves odd positions; center direction 0 therefore occupies the remaining even position, either 0 or 2. If center is first, it sees one leaf bit set and its majority color is zero. If center occupies position 2, the first two positions hold leaf j and one other leaf. Toggling them changes the three leaf bits from a unit vector to another unit vector, so the majority at the center step is again zero. Thus no root of weight at most one supports e_0. Reversing a geodesic gives the same profile from the complementary root, excluding weight at least three. At root e_0+e_1 the order (2,0,3,1) has profile e_0; permuting the three leaf labels and taking complementary roots realizes e_0 from all six weight-two roots. Hence S_(e_0)={x in Q_4:|x|=2}.

The added direction rules do not affect any old-direction colors, so every full path projecting to target e_0 must start with precisely two one-bits among its first four bits. This proves the lower distance bound two from 0^n; the displayed root at distance two attains it.

**Full affine-span proof at every root.** The exchange of consecutive directions 0 and j, j=1,2,3, changes the indexed profile by
v_(0j)(a)=[partial_j c_0(a)]e_0+[partial_0 c_j(a)]e_j
=e_j+(a_k+a_l)e_0,
where {k,l}={1,2,3}\{j}. At any specified root, choose the preceding directions among k,l so that a_k+a_l has either value. Both exchange vectors e_j and e_0+e_j therefore occur as differences of rooted full profiles. Their spans contain e_0 and all three leaf basis vectors. For each new direction h>=4, exchanging 0 and h changes only its profile bit, since partial_h c_0=0 and partial_0 c_h=1, giving e_h. Thus the rooted difference span is F_2^n at EVERY root. QED.

This strengthening shows that the distance-two failure is not caused by an autonomous flat block or an affine parity restriction on any root's complete-profile family.

## Balanced, full-span strengthening in every even dimension at least eight

**Corollary.** For every even N>=8 there is a vertex-balanced legal coloring of Q_N such that the affine hull of the full profiles at EVERY root is F_2^N and a supported profile u at root 0 has an attainable one-bit modification u+e_i whose closest supporting root has Hamming distance two. Its target supporting-root set has density 3/8 among all roots.

*Proof.* Start with the four-dimensional coloring c in the preceding strengthening. Introduce four new directions h_j, j=0,1,2,3, with color rules g_(h_j)(x)=1+c_j(x), retaining all four old rules. Every new rule ignores its own direction bit, is complement-odd, and depends only on the original four bits. The resulting Q_8 coloring is legal and vertex-balanced: at each vertex the old direction j and its new partner h_j have opposite incident colors. For N=8+2s introduce s further pairs of new directions colored x_0 and 1+x_0. Every pair is pointwise color-complementary, so balance and legality persist.

More generally, under any such extension by new rules g_h depending only on old bits and satisfying g_h(bar x)=1+g_h(x), at each fixed root (x,y) the full-profile set equals W_x(c) times F_2^k. Project any full path to old directions to see the forward containment. Conversely insert any new direction before the old geodesic to color it g_h(x), or after all old steps to color it g_h(bar x)=1+g_h(x). Each new rule ignores all new bits, and the old rules ignore them as well; thus all new profile entries can be prescribed independently.

Consequently, taking the first four bits of the source word to be e_0+e_1 and its remaining bits arbitrary, at the root 0^N this word is attained. Its single-bit change in direction 1 restricts to target e_0 in the original core. The supporting roots are precisely {(x,y):|x|=2}, with x in F_2^4 and y arbitrary, by the proved core root-support identity and the spectator factorization. Hence every target root has distance at least two from 0, and one has distance two.

Finally, full rooted affine span persists: differences of old profile entries span F_2^4 by the core square exchanges. Every new direction h has a nonconstant odd rule g_h, so some old bit j influences it. The square exchange in directions j,h changes the profile only in h because every old rule ignores new bits. Its nonzero h-unit exchange occurs as a rooted order difference at every root by choosing the preceding old directions to reach an input with partial_j g_h=1. Thus all added basis vectors are also in the rooted difference span. QED.
