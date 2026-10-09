# Odd block-cyclic affine edge colorings of every rank realize all direction-color patterns by cyclic parity-padding

# Arbitrary-rank cyclic BLOCK-dependence odd affine edge colorings realize all direction-color words

**Definition.** Let n>=2 and partition the n distinct coordinate directions into m>=2 nonempty blocks B_1,...,B_m. Let sigma be a FIXED-POINT-FREE permutation of [m] (a disjoint union of directed cycles of length >=2). In every block B_j choose a nonempty ODD-cardinality subset M_j⊆B_j of marked coordinate directions. Fix arbitrary bits b_v∈F2 for all directions v. Color each physical cube edge of direction v∈B_i by
   c_v(x)=b_v + Σ_{u∈M_(sigma(i))} x_u  mod 2.
Every direction-v edge color depends on a distinct block B_(sigma(i)) and hence is INDEPENDENT of x_v. Since |M_(sigma(i))| is odd, c_v(bar x)=1+c_v(x). These therefore form a valid class of antipodally odd UNDIRECTED EDGE colorings of the original k=1 conjecture, with potentially high dependence arity and arbitrarily large nullity.

**THEOREM (all full direction-indexed color patterns, any number of cycles).** For EVERY such block-cyclic coloring and EVERY prescribed direction-indexed target T=(T_v)_v∈F2^n, there exist an actual cube root x and a permutation p of all n coordinate directions for which the complete n-edge antipodal geodesic P(x,p) has color T_v on its unique direction-v physical edge, simultaneously for ALL v. Therefore EVERY coloring in the class admits a monochromatic full antipodal geodesic, of either prescribed constant color.

**Lemma (cyclic-odd parity-padding interleaving).** Let sigma be ANY fixed-point-free permutation on m block labels, and let p_i be any POSITIVE ODD counts. For a word of these block labels with p_i occurrences of label i, set
  a_i = #{occurrences of i preceded by an EVEN number of occurrences of sigma(i)}.
Fix ANY word w0 containing each block label EXACTLY ONCE, and let eps_i∈{0,1} be its corresponding a_i. Then for EVERY target integer vector (a_i) with 0<=a_i<=p_i and a_i≡eps_i (mod 2), there is an actual interleaving word with these statistics.

*Proof.* Start with w0, where each block occurs once and realizes eps_i. Grow the counts p_i by increments of TWO. Suppose a word currently contains an odd number q_i of each block and achieves the relevant intermediate statistics. To add TWO new occurrences of block i:
- Prepend the two i letters at the VERY BEGINNING to increase a_i by 2: both see zero preceding sigma(i) letters.
- Append the two i letters at the VERY END to leave a_i unchanged: both see the current positive ODD total q_(sigma(i)) of sigma(i) letters, so contribute zero.
For every other label j≠i, its statistic a_j is unchanged: only the number of preceding occurrences of i changes, by zero or two, and this does not change any parity. This also holds when sigma(j)=i. To realize arbitrary prescribed a_i with parity eps_i, inductively choose the append operation if a_i <= p_i−2, and prepend operation if a_i>=2, after applying the smaller-count induction to a_i or a_i−2 respectively. The two ranges cover 0<=a_i<=p_i for every p_i>=3, with the p_i=1 base value forced by eps_i. Since each adjustment affects only the count and statistic of its own block, the operations for different i can be interleaved in any order. QED.

**Proof of the theorem.**
1. Put q_v=b_v+T_v. At a chosen starting root x define independently choosable initial block parity registers
   alpha_i=Σ_{u∈M_(sigma(i))} x_u.
   The m sets M_(sigma(i)) are pairwise disjoint and nonempty because sigma is a permutation and the B_j are disjoint. Thus for ANY alpha∈F2^m there is an actual x realizing all alpha_i (set one designated input bit per marked set accordingly).
2. For v∈B_i, after traversing earlier directions in the full order the true physical direction-v edge has color
   C_v=b_v+alpha_i+ #(M_(sigma(i)) directions PRECEDING v) mod 2.
   Hence target C_v=T_v requires that v be traversed at a moment when the parity of already-used M_(sigma(i)) directions equals alpha_i+q_v.
3. Consider only the MARKED directions in M_i, with p_i=|M_i| odd. Fix any base permutation w0 of the m block labels, one each, with epsilon statistics from the lemma. For each block i, choose alpha_i to ensure
   a_i:=#{v∈M_i : q_v=alpha_i} ≡ eps_i (mod 2).
   Because p_i is odd, changing alpha_i to 1+alpha_i replaces the count a_i by p_i−a_i and flips its parity; thus the desired parity choice is always possible independently for every block.
4. Apply the cyclic-odd interleaving lemma to obtain a word of MARKED block labels with precisely a_i occurrences of block i appearing at EVEN preceding M_(sigma(i)) parity. Assign the actual named directions v∈M_i with q_v=alpha_i to exactly these even-parity i slots, and those with q_v=1+alpha_i to the odd-parity i slots. Since the numbers coincide, this bijection always exists. All marked direction-edge colors are now the prescribed T_v.
5. Insert the remaining UNMARKED coordinate directions v∈B_i\M_i, if any. Each unmarked direction belongs to none of the marked support sets M_j, so its traversal changes NO parity register. Since the marked set M_(sigma(i)) has positive odd size, the interleaving word has actual gaps with parity of already-used M_(sigma(i)) directions equal to 0 and gaps with parity 1 (before its first occurrence and after its first occurrence). Insert every unmarked v∈B_i in any such gap realizing the required parity alpha_i+q_v. All insertions preserve every previous parity check, regardless of their order.
6. Finally choose the root x with the initial register values alpha_i from Step 1. The resulting full permutation p and root x have C_v=T_v for every direction v. Since every coordinate direction is used exactly once, P(x,p) is a genuine full n-edge antipodal geodesic. QED.

**Corollaries and strength.**
- For m=2 with sigma interchanging the two blocks, this gives an alternative full proof of the previously established rank-two odd-affine theorem nori_k1_affine_rank_two_all_direction_color_patterns_odd_odd_interleaving_20261009. In fact EVERY valid rank-two odd affine matrix has exactly that two-block form, so the older result is complete for that rank.
- For m=3 with sigma a 3-cycle, we obtain a NEW solved family of RANK THREE odd affine matrices, with potentially arbitrary nullity n−3, using odd-sized marked subsets on successive groups. This goes beyond the known rank>=n−2 theorem whenever n>=6, and beyond 2-junta when a marked support has >=3 coordinates.
- More generally any number m of block types and any disjoint union of cyclic successor graphs is permitted. The m row types are supported on pairwise disjoint nonempty sets and therefore linearly independent; the resulting affine matrix has EXACT rank m. Thus this simultaneously solves genuine intermediate-rank cases for arbitrarily large n.
- The proof is CONSTRUCTIVE and polynomial-time. The parity-padding operations and assignments require no enumeration of full permutations or cube roots.

**Boundary.** General odd affine matrices may have row supports spread across MULTIPLE input blocks, giving coupled parity-register effects. General nonlinear three-input majority edge colorings likewise do not have this linear block transport law. Unrestricted edge-color geodesic closure is still open. The block-cyclic proof shows that the odd-odd interleaving technique is not a rank-two accident; it can be extended to arbitrarily many parity dimensions PROVIDED the row-support dependency graph is a permutation of independent blocks.
