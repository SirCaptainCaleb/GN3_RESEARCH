# Almost every unrestricted NORI coloring is good: exponential bound via independent geodesic words

# Almost all GENERAL (nonlinear) active NORI colorings have good geodesics: an explicit exponentially strong bound

Fix n>=7. Let the sample space consist of ALL valid active NORI colorings of physical ORDERED three-faces of Q_n, independently/uniformly coloring each orbit of the fixed-point-free involution
  (F,(i,j,k)) -> (bar F,(k,j,i))
with one fair bit and giving its partner the complementary bit. This is the **FULL UNRESTRICTED coloring space**, with no affine, parity, Fourier-degree, or other restriction. Every coloring in this sample space satisfies the exact NORI axiom.

Let k=ceil(log2 n). Choose pairwise distinct tags v_1,...,v_n∈F2^k. Define the linear root code
  C={x∈F2^n : sum_i x_i=0, sum_i x_i v_i=0 }.
Then |C|>=2^(n-k-1) and every two distinct x,y∈C have Hamming distance at least 4. Proof: the two sets of equations have rank at most k+1; nonzero vectors of weight1 or3 fail even parity, and a vector of weight2 on {i,j} would require v_i=v_j, impossible. This is an explicit algebraic independent-root certificate, not an existential packing estimate.

Let t=1+floor((n−1)/6). By the independently proved triple-window support packing theorem (the elementary random-permutation/union-bound argument), choose t full direction orders pi^(1),...,pi^(t) whose unordered consecutive 3-direction windows are pairwise disjoint.

**Theorem 1 (mutually independent full geodesic color words).** For EVERY choice of root x∈C and packed direction order pi^(s), look at the ACTUAL full antipodal physical geodesic from x with direction order pi^(s), and its ordered three-face window-color word of length L=n−2. Across ALL t|C| chosen geodesics, these L-tuples of binary colors are independent and individually UNIFORM on {0,1}^L.

Proof. Within one direction order, distinct window positions have distinct unordered free coordinate triples, so their ordered-face objects belong to distinct antipodal-reversal orbits. Across different packed direction orders, unordered free-coordinate triples are disjoint, so their sampled face objects again lie in distinct orbits. For the SAME direction order/window position and two roots x!=y in C, their physical face exterior assignments differ because d_H(x,y)>=4 exceeds the three free directions: the root-progress prefix toggles are the same, and x,y cannot differ only within the three free coordinates. Thus these also correspond to distinct physical ordered-face objects. Could two sampled ordered faces nevertheless lie in the SAME NORI involution orbit? An orbit mate always reverses its ordered triple and complements the physical face, while for a fixed unordered triple, our packed family contains exactly one window position and exactly ONE chosen ordered direction triple. Because no sampled window has the reversed ordered triple, none of the selected objects are orbit mates. Therefore all sampled colors are distinct independent fair orbit bits. Grouping them by path establishes the full independence/uniformity.

**Theorem 2 (explicit nonlinear random grand-closure bound).** Let
  p_n = 2(n−2)/2^(n−2) = (n−2)/2^(n−3),
the exact fraction of binary words of length n−2 with AT MOST ONE color change (there are 2 choices of initial color and n−2 choices for the switch boundary, including no change). Then
 P(random NORI coloring has NO good full antipodal geodesic)
 <= (1−p_n)^(t|C|)
 <= exp(−p_n t 2^(n−k−1))
 = exp(−4(n−2)t/2^k).

Since 2^k<2n, this is STRICTLY less than
   exp(−[2(n−2)/n] (1+floor((n−1)/6))).
Thus the proportion of UNRESTRICTED active NORI colorings violating the grand conjecture tends to zero exponentially fast with n. Indeed the probability of NO MONOCHROMATIC full antipodal geodesic also decreases exponentially: a random length-(n−2) word is monochromatic with probability 2/2^(n−2)=2^(3−n), so
 P(no monochromatic full antipodal geodesic)
 <= exp(−t|C| 2^(3−n))
 <= exp(−4t/2^k)
which decays at best to a nonzero constant with this linear packing; the proved exponential vanishing concerns the AT-MOST-ONE-CHANGE grand conclusion.

**Theorem 3 (independent binomial witness count).** Among the selected t|C| actual directed full geodesics, the number having <=1 change is Binomial(t|C|,p_n). Thus its expected value is
  t|C| (n−2)/2^(n−3) >= 4(n−2)t/2^k,
and the exact zero-witness probability is (1−p_n)^(t|C|). Standard elementary binomial concentration can quantify linear-in-n many independent good witnesses with high probability.

**Why this is strictly stronger than the affine random result.** The sample space is the entire class of valid NORI ordered-face colorings. The proof depends ONLY on identifying disjoint antipodal-reversal orbits of the face objects queried by the selected paths. No linearity or algebraic rank for the coloring is used. The Hamming-distance-four code and window-disjoint permutation packing serve as an explicit independent set in the dependency graph of full geodesic color words.

**Scope.** This does NOT prove grand closure for EVERY coloring: it proves the fraction of possible counterexamples under the uniform distribution is exponentially small. An adversarial deterministic coloring could conspire to make all the selected (or all possible) geodesics bad. To obtain grand closure from this approach one needs an additional deterministic incidence/degree/parity or local-repair argument which excludes the remaining exceptional assignments. The result supplies a rigorous asymptotic strengthening and a useful witness-packing structure.
