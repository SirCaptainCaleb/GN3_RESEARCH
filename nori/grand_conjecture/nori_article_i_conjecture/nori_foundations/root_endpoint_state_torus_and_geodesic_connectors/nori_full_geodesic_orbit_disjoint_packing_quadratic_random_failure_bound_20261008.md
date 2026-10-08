# Orbit-disjoint antipodal geodesic packing: random unrestricted NORI failure at most exp(-n(n-1)/2)

# Quadratic-exponent random NORI closure via a greedy orbit-disjoint FULL-GEODESIC PACKING

Consider the COMPLETE UNRESTRICTED binary coloring space for ordered physical 3-faces of Q_n, n>=4, obeying active antipodal reversal oddness:
  c(bar F,(k,j,i)) = 1 - c(F,(i,j,k)).
Sample a color independently and fairly on every pair-orbit of this free involution and give the paired reversed-complemented ordered face the opposite bit. The coloring need NOT be affine, parity-based, coordinate-only, or otherwise structured.

**Theorem 1 (large family of mutually disjoint genuine window-orbits).** In Q_n there exists a family P of DIRECTED FULL antipodal geodesics (specified by starting vertex x and ordered permutation of ALL n directions) such that NO TWO chosen paths visit any shared antipodal-reversal ORBIT of an actual ordered physical 3-face, and
    |P| >= ceil( 2^n n(n-1) / [16(n-2)] ).
In particular |P| is of order n*2^n, greatly exceeding the previous distance-four-root-code packing combined with O(n) disjoint direction orders.

**Proof.** There are exactly N=2^n n! directed full geodesics. Each carries L=n-2 consecutive ordered physical three-face windows, whose unordered free-coordinate 3-sets are all distinct; hence the L window objects lie in L distinct antipodal-reversal face orbits.

Fix ONE actual ordered face object (F,(i,j,k)), with pairwise distinct free directions. Exactly (n-2)! ordered full direction permutations contain the ordered triple (i,j,k) as consecutive entries: collapse the triple into a block among n-2 permuted objects. For each such direction permutation, the requirement that its physical consecutive window equals F fixes all n-3 exterior starting-root bits and leaves 3 free starting-root bits, hence exactly 2³=8 possible roots. So precisely 8(n-2)! full geodesics contain this single oriented physical face object. The antipodal-reversal orbit also contains exactly one second object (bar F,(k,j,i)), likewise on 8(n-2)! geodesics. A full geodesic cannot contain both orbit objects, since they have the same free-coordinate support but each ordered full direction permutation visits any unordered triple support at most once. Thus EVERY face orbit lies in exactly
   D = 16(n-2)!
directed full geodesics.

Greedily select a remaining full geodesic P and discard ALL remaining geodesics sharing at least one of its L orbits. At each selection, at most LD paths are discarded (by the union bound; overlaps can only reduce this count). To discard all N original paths requires at least N/(LD) selections. Therefore
  |P| >= ceil(2^n n! / [16(n-2)(n-2)!])
      = ceil(2^n n(n-1) / [16(n-2)]).
QED.

**Theorem 2 (quadratic-exponent UNRESTRICTED grand-success probability).** In the uniform active NORI coloring space, each chosen path P∈P has an INDEPENDENT uniformly random binary color word of length L=n-2. A word of length L is fully monochromatic with probability p_mono=2/2^L=2^(3-n). A word has at most ONE color change with probability
  p_good=2L/2^L=(n-2)2^(3-n)
(because there are two choices of initial bit and L possible switch positions, including no switch).

Therefore
  Pr(there is NO one-switch full antipodal geodesic ANYWHERE in Q_n)
   <= (1-p_good)^|P|
   <= exp(-n(n-1)/2).
And, substantially stronger than prior NORI random results,
  Pr(there is NO fully MONOCHROMATIC full antipodal geodesic ANYWHERE in Q_n)
   <= (1-p_mono)^|P|
   <= exp(-n(n-1)/[2(n-2)]).
The first bound tends to zero as exp(-Theta(n²)); the second tends to zero as exp(-n/2), for the FULL unrestricted space of valid antipodal-reversal-odd physical ordered-three-face colorings. Every selected color word is genuinely independent of the others because the paths query pairwise disjoint involution-orbit variables. No dependence approximation or local lemma is used.

**Theorem 3 (certified independent witness counts).** Let X_good and X_mono denote the number of good and monochromatic full paths among the explicitly selected orbit-disjoint family P. Then
  X_good ~ Binomial(|P|, p_good),
  X_mono ~ Binomial(|P|, p_mono).
Their expected values obey
  E X_good >= n(n-1)/2,
  E X_mono >= n(n-1)/[2(n-2)].
Consequently standard binomial tail bounds give concentrations around quadratically many good witnesses and linearly many fully monochromatic witnesses with exponentially small failure probabilities in n. These are LOWER BOUNDS on counts in the full family of ALL antipodal geodesics.

**General ordered-r-face extension (r>=2).** For binary ordered physical r-faces under an antipodal reversal-odd free involution, each ordered face object belongs to 2^r (n-r+1)! full geodesics, and each face orbit belongs to
  D_r=2^(r+1)(n-r+1)!
full directed geodesics. Each full geodesic contains L=n-r+1 distinct face orbits. The same greedy method packs at least
  ceil[ 2^n n! / (L 2^(r+1)(n-r+1)!) ]
pairwise orbit-disjoint full antipodal paths. Their binary window words are independent fair words of length L, giving analogous explicit probabilistic lower bounds for mono and <=1-change full paths. No antipodal oddness beyond independent coloring of free reversal orbits is needed to count the paths.

**Significance and limits.** This strictly strengthens both nori_unrestricted_random_coloring_one_switch_exponential_success_code_packing_20261008 (whose exponent was only Omega(n)) and the affine-ensemble results: for arbitrary random valid NORI coloring, the chance of a hypothetical counterexample is bounded above by exp(-n(n-1)/2), and failure of the STRONGER monochromatic variant has exponentially small probability exp(-Omega(n)). This does NOT prove that the counterexample set is empty. An adversarial coloring could make ALL selected words bad; to obtain universal grand closure from this packing one needs a deterministic parity/topological consistency obstruction among the remaining overlapping paths not retained in the independent family.
