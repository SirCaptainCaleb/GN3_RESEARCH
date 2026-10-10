# Q12 two-layer switching closure: four-triple partition parity forces additive structure

# Complete Q12 closure for two-layer switching via parity of four-triple partitions

Let c be an antipodal-reversal-odd binary coloring of physical ordered three-faces of Q_12. For each ordered triple π assume all faces of exterior Hamming weight 4 have color a(π), and all faces of exterior Hamming weight 5 have color 1−a(π). On all other exterior layers c is arbitrary subject to NORI oddness. Then a(rev π)=a(π).

**THEOREM.** Every such coloring admits a full antipodal twelve-edge geodesic whose ten consecutive ordered-face colors change at most once. In fact one can choose a direction order with at least TWO distinct physical central starting vertices yielding good full geodesics.

**Lemma 1 (exact algebraic central-root four-block certificate).** Let p be a direction order, and put a_i=a(p_i,p_(i+1),p_(i+2)) for i=1,...,10. If a_1=a_4 and a_7=a_10, then p admits at least TWO distinct physical starting roots whose full antipodal twelve-geodesics are good.

**Proof.** Choose six bits B,A,C,D,E,F and assign the twelve root bits in direction order as
 (1−B,B,1−A,A,1−C,C,1−D,D,1−E,E,1−F,F).
Direct counting of fixed exterior ones in the genuine ordered three-faces shows that all ten windows lie in layers 4 or 5, and their layer-offset profile is exactly
 t=(A,B,C,A,D,C,E,D,F,E).
In particular, **every** binary t with t_1=t_4, t_3=t_6, t_5=t_8, t_7=t_10 has an explicit genuine root.

Define two defect bits d_2=a_3+a_6 and d_3=a_5+a_8 (sums mod2). Choose one of the following four at-most-one-change 10-bit words g by their respective defect pair (d_2,d_3):
  00 → 0000000000,
  10 → 0000111111,
  11 → 0000011111,
  01 → 0000001111.
Every listed word satisfies g_1=g_4 and g_7=g_10. By construction, t=a+g satisfies all four indicated Hamming-profile equalities. Choose A,B,C,D,E,F to realize that t in the explicit paired-root formula. Every actual window color equals a_i+t_i=g_i, which has at most one change. Replacing all six parameters by their complements changes t by the all-ones word, supplying a second distinct root with color word 1−g. QED.

This analytical certificate is a special case of the all-even paired-root subspace and sparse-defect theorem Item nori_all_even_paired_root_linear_subspace_sparse_defect_two_start_geodesics_20261009.

**Lemma 2 (rigidity of universally odd four-block partitions).** Suppose a binary map a on ORDERED distinct triples of twelve coordinate names satisfies
 Σ_(j=1)^4 a(π_j)=1 mod 2
for EVERY partition of the twelve names into four ordered triples π_1,...,π_4. Then a is independent of the internal ordering of each triple, and
 a(i,j,k)=d+w_i+w_j+w_k mod 2
for some bits w_i,d with Σ_i w_i=1.

Proof: Holding a triple's underlying 3-set and the other three triples fixed while permuting that triple leaves the total parity 1, so a is symmetric in its arguments; let h(U) be its value on a 3-set U. Fix distinct names r,s. For any two disjoint 2-sets U,V outside {r,s}, compare the two full four-triple partitions
 (U+r),(V+s),C,D
and
 (U+s),(V+r),C,D,
where C,D partition the six other names. Their odd-parity equalities yield
 h(U+r)+h(U+s)=h(V+r)+h(V+s).
The graph of disjoint 2-sets on the other ten names is connected (the Kneser graph KG(10,2)), so the difference δ_rs=h(U+r)+h(U+s) is independent of U. For any distinct r,s,t, choose U disjoint from all three; then δ_rs+δ_st=δ_rt. Choose reference name z, let w_z=0, w_r=δ_rz. Thus δ_rs=w_r+w_s. The function h(A)+Σ_(j∈A)w_j is invariant under a one-element replacement in a 3-set A, and the Johnson graph J(12,3) is connected. Hence it is a constant d, proving the additive form. Summing over any four-block partition gives Σ_i w_i+4d=1 mod 2, so Σ_i w_i=1.

**Lemma 3 (all odd vertex weights have a one-switch triple order).** Suppose a(i,j,k)=d+w_i+w_j+w_k where Σ_i w_i is odd. Arrange the twelve directions so their w-bits, in direction order, are one of these sequences, according to the number m of ones:
  m=1: 000000000001, triple-parity word 0000000001;
  m=3: 000001001001, triple-parity word 0001111111;
  m=5: 001001001011, triple-parity word 1111111100;
  m=7,9,11: bitwise complements of the m=5,3,1 sequences, respectively.
Each has at most one color change across its ten consecutive triples; adding d preserves change positions. Every word with the prescribed number of ones can be realized by assigning the directions of each w-class to the indicated positions. Since actual central-face colors may flip when K=5, choose a root with K_i=4 for every i (in direction-order bits, the THREE explicit distinct roots 011100011100, 101010101010, and 110001110001 each have K_i=4 for all 1≤i≤10); therefore at least three actual roots have precisely this one-switch color word.

**Proof of the theorem.** Consider all partitions of the twelve coordinates into four ordered triples.
Case A: Some partition has an EVEN number of a-color-1 blocks. Then arrange its four triples so the first two block colors agree and the last two agree: the block-color word is one of 0000,0011,1100,1111. Concatenate these four ordered triples as p. Its intercept colors a_1,a_4,a_7,a_10 satisfy Lemma 1; take one of its two good actual central roots.
Case B: Every partition has ODD color parity. Lemma 2 gives additive vertex-parity a with odd Σw, and Lemma 3 supplies a full direction order with a good constant-layer physical root. The antipodal geodesic is genuine, and its window word is one-switch.

This is a face-dependent, two-central-layer hypothesis; the unrestricted Q12 and all-dimensional NORI conjecture remain open. The proof is a new cross-support partition-parity rigidity mechanism, rather than enumeration of NORI colorings or a fixed direction-order criterion.
