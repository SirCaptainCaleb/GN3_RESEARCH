# Power-of-two universal oriented tournament Hamilton paths imply marked-center monochromatic NORI in infinitely many dimensions

THEOREM (power-of-two oriented Hamilton-path parity; marked-tournament three-window closure in infinitely many dimensions).

(A) Let T be any tournament on r=2^k vertices (k>=0). For EVERY prescribed binary orientation pattern epsilon=(epsilon_1,...,epsilon_(r-1)), the number of permutations p satisfying t(p_i,p_(i+1))=epsilon_i for every i is ODD. Here t(a,b)=1+t(b,a) over F_2 encodes the tournament orientation.

Proof of A. Use Redei's standard odd-Hamilton-path theorem: every nonempty induced tournament has an odd number of permutations whose consecutive arc labels t are all 1 (equivalently all 0, by reversing orders). For fixed epsilon, expand over F_2
 F(epsilon)=sum_(p in S_r) product_(i=1)^(r-1) [1+t(p_i,p_(i+1))+epsilon_i].
For a chosen subset I of indices at which the product contributes the tournament variable t, the selected adjacencies partition positions 1,...,r into kappa>=1 maximal consecutive blocks, of lengths l_1,...,l_kappa. The sum over p of product_(i in I) t(p_i,p_(i+1)) factors, after choosing the ordered vertex subsets of those block sizes, into a product of directed-Hamilton-path counts, each odd by Redei. Its parity is therefore the multinomial r!/(l_1!...l_kappa!). When I is all positions this is 1. When I is proper, kappa>=2; every mixed multinomial coefficient of total degree r=2^k is even, by (X_1+...+X_kappa)^(2^k)=sum_j X_j^(2^k) over F_2. Hence every proper-I term vanishes and F(epsilon)=1. This identity counts exactly the permutations with t along the path equal to epsilon. QED.

(B) Let n=2r-1 or n=2r with r a power of two and n>=3. Let t be ANY tournament on n directions and s:[n]->F_2 an ARBITRARY marking of all center directions. Then there is a full direction permutation p for which ALL n-2 ordered-triple labels h(p_i,p_(i+1),p_(i+2))=t(p_i,p_(i+2))+s(p_(i+1)) are equal. Thus the marked-center tournament subclass has fully MONOCHROMATIC spanning geodesics in every dimension n=3,4,7,8,15,16,31,32,63,64,...

Proof of B. Choose alpha∈F_2 occurring at least r times among the n values s(v), and choose a set O of exactly r vertices marked alpha. Put E=[n] without O, of size r-1 or r. By Redei's Hamilton path theorem, order E as e_1,...,e_|E| with t(e_j,e_(j+1))=0 throughout. By A, order O as o_1,...,o_r with the ARBITRARY prescribed orientation pattern
 t(o_j,o_(j+1))=alpha+s(e_j)  for j=1,...,r-1.
Interleave p=(o_1,e_1,o_2,e_2,...), ending with o_r in odd n or e_r in even n. Every odd-position triple compares consecutive O vertices and has center e_j, hence color (alpha+s(e_j))+s(e_j)=alpha. Every even-position triple compares consecutive E vertices and has center o_j marked alpha, hence color 0+alpha=alpha. Thus the entire three-window word is constant. QED.

(C) PHYSICAL NORI consequence. If an ordered physical three-face coloring of Q_n with n in these dimensions restricts on ONE CENTRAL exterior-Hamming layer |S|=floor((n-3)/2) or ceil((n-3)/2) to the marked tournament form h(a,b,c)=t(a,c)+s(b), independent of the identity of exterior one-set S, then it has a monochromatic full antipodal cube geodesic. The colors at every other exterior-weight layer may be arbitrary, nonlinear, and face-dependent. Indeed choose p as in B, and an alternating starting cube vertex in p order which keeps every genuine three-window on the chosen central exterior-weight layer (established alternating-root lemma).

All results here are exact and all-dimensional along the indicated infinite subsequence. The proof of A uses only Redei's classical odd-Hamilton-path theorem and multinomial parity. A fully unrestricted NORI coloring and dimensions outside this subsequence remain open; the factorized central-layer hypothesis is essential in C.

ADDITIONAL GENERAL PARITY FORMULA. For arbitrary tournament T on r vertices and arbitrary prescribed arc pattern epsilon, the parity of its number of realizations equals the parity for the transitive tournament, with explicit formula
 F(epsilon)=sum_(I subseteq [r-1]) [product_(i notin I)(1+epsilon_i)] * multinomial(r; block_sizes(I))  (mod 2).
Consequently for r with exactly two 1-bits in its binary expansion, say r=2^a+2^b with a>b, the parity equals 1+epsilon_(2^a)+epsilon_(2^b). In particular, for r=5 the prescribed 4-edge pattern is realized an odd number of times whenever its first and fourth arc signs are equal, independently of tournament orientation. This provides a concrete general-dimension parity test for the next frontier.
