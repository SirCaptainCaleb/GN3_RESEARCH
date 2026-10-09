# Global geodesic density and cyclic root-transport bounds

# Global geodesic density and cyclic root-transport bounds

Local monochromatic connectors arise from cyclic five-window parity, while global geodesic switch bounds arise by averaging changes along complete coordinate orders and roots. These are distinct but complementary counting arguments: one supplies abundant short seeds, the other supplies at least one long path with controlled defect.

## COLOR-FREE reachability odd-cycle obstruction and the middle Kneser graph

Let c be an antipodally odd binary UNDIRECTED edge coloring of Q_n. For root x write
\[
\mathcal R_x=\{S\subseteq[n]:x\oplus S\in R(x)\},
\]
where R(x) is the color-FREE set of endpoints of monochromatic geodesics starting at x, of EITHER color. Define a graph \(\Gamma_x\) on \(\mathcal R_x\) by joining distinct supports S,T exactly when
\[
S\cap T=\varnothing,\qquad S\cup T=[n]\setminus\{i\}
\]
for some i. Thus two adjacent supports are disjoint and cover n-1 of the n coordinate directions.

**Theorem (odd-cycle reachability certificate).** If \(\Gamma_x\) is nonbipartite for any root x, then c has a MONOCHROMATIC FULL ANTIPODAL GEODESIC. Equivalently, in every hypothetical counterexample, \(\Gamma_x\) is bipartite for EVERY x. This condition is expressed entirely in the uncolored reachability set R(x); it requires no colors in the definition or the topological labeling.

**Proof.** Let S--T be an edge of \(\Gamma_x\). Any two actual monochromatic geodesics from x to x⊕S and x⊕T with the SAME color concatenate in reverse/forward order to a monochromatic (n-1)-edge geodesic, omitting the sole direction i. Its two possible endpoint-extension edges are antipodes and therefore have opposite colors; one has the path color and produces a full monochromatic antipodal geodesic. Consequently, under the hypothesis of NO full monochromatic antipodal geodesic, two reachable supports joined by an edge must have OPPOSITE witness colors. Furthermore, a support incident to any edge must admit a UNIQUE possible monochromatic witness color, since availability of both colors would allow a same-color match with its neighbor. These unique witness colors give a proper binary vertex coloring of all nonisolated vertices of \(\Gamma_x\). Isolated vertices can be colored arbitrarily. Hence \(\Gamma_x\) is bipartite. Contraposition proves the theorem. \(\square\)

**Odd dimensions and the Kneser graph.** For n=2k+1, restrict \(\Gamma_x\) to reachable supports of size k. Two k-subsets are joined exactly when they are disjoint, so this is the subgraph of the Kneser graph KG(2k+1,k) induced by the reachable middle-layer supports. The full KG(2k+1,k) contains an explicit (2k+1)-cycle. For any order p_1,...,p_n, set S_0={p_2,p_4,...,p_{2k}} and iteratively
\[
S_t=S_{t-1}\mathbin{\triangle}([n]\setminus\{p_t\}),\quad 1\le t\le n.
\]
Because p_t has bit 0 in S_{t-1}, S_{t-1} and S_t are disjoint k-subsets whose union omits exactly p_t. Each step toggles 2k bits, preserving cardinality k. The n steps return to S_0 because each coordinate is toggled n-1 times, an even number. The S_t for 0<=t<n are distinct (any shorter nonempty consecutive product of distinct toggle masks is nonzero). Hence they form an odd n-cycle. If ALL these S_t lie in \(\mathcal R_x\), closure follows.

**Quantitative obstruction.** For every hypothetical counterexample, at least one vertex of each such middle-layer n-cycle is absent from \(\mathcal R_x\). Averaging the n cyclic supports over uniformly random permutations p, each position is uniformly distributed among k-subsets. Therefore every root x has at least
\[
\frac1n\binom nk
\]
unreachable k-subsets. For n=3, k=1, all singletons are reachable from every root, contradicting this condition, giving an immediate proof of the edge-geodesic conjecture in n=3.

**Parity limitation.** For even n, every edge of \(\Gamma_x\) joins a set of even size to a set of odd size, because |S|+|T|=n-1 is odd. Thus \(\Gamma_x\) is automatically bipartite in even dimension; the odd-cycle criterion provides information only for odd n (or after a further higher-order construction).

**Research direction.** The theorem changes topological extraction from a single 'balanced ridge is good' assertion to a global statement: seek topological / Kneser / Tucker forcing of a nonbipartite near-complementary-support graph \(\Gamma_x\) for SOME root x. This is a precise COLOR-FREE reachability-label coincidence: the desired odd-cycle vertices are actual reachable supports, and the edge-color witness consistency is derived only in the extraction proof. The existence of such a root for all odd-colorings remains an unsolved forcing obligation; the theorem itself is an exact sufficient condition.

## Quadratic-exponent random NORI closure via a greedy orbit-disjoint FULL-GEODESIC PACKING

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

## Universal full antipodal geodesic switch bound from local odd-cycle physical root transport

Let r>=2 and n>=2r-1. Color all physical ordered r-faces of Q_n by arbitrary binary values (NO antipodal oddness assumption). For a rooted full n-coordinate geodesic (x,p) with direction word p=(p1,...,pn), its actual consecutive ordered-r-face colors form a word of length n-r+1, with exactly m=n-r potentially switching adjacent pairs. Let D(x,p) count their total number of switches.

**THEOREM (universal all-dimensional linear full-switch bound).** Under these completely arbitrary colorings,
\[
\boxed{\mathbb E_{X\in Q_n,\ P\in S_n}D(X,P)\ \le\ \frac{2r-2}{2r-1}(n-r).}
\]
Consequently there exists an ACTUAL full antipodal n-edge geodesic with
\[
\boxed{D(x,p)\ \le\ \left\lfloor \frac{2r-2}{2r-1}(n-r)\right\rfloor.}
\]
More quantitatively, for every integer q>=0 with q+1>(2r-2)(n-r)/(2r-1), the fraction of all 2^n n! rooted full antipodal geodesics having at most q switches is at least
\[
\boxed{1-\frac{(2r-2)(n-r)}{(2r-1)(q+1)}.}
\]
All three statements hold without any reversal-odd coloring assumption.

**PROOF.** The team's proved ordered-r odd-cycle root-transport theorem nori_ordered_r_face_odd_cycle_root_transport_two_r_minus_one_seed_20261008 says: fix any q0=2r-1 distinct coordinate directions B and any physical reference root z. Among the (q0)! orders of B, at least (q0-1)! have the first TWO actual r-face windows EQUAL on the rooted q0-edge geodesic that starts at z XOR its first direction, uses that direction order, and passes through z after its first step. The equality follows from odd-cycle alternation of the q0 genuine ordered r-face colors THROUGH z. Indeed an odd cycle of binary vertex colors must have two adjacent equal colors, and each such equal pair is an actual root-neighbor transported (2r-1)-edge witness. The map (z,pi)->(x=z XOR first(pi),pi) is a BIJECTION for each fixed B. Summing over z therefore proves that for a uniformly random starting root X and uniformly random permutation of B, the first TWO actual ordered-r-face window colors of that (2r-1)-edge path agree with probability AT LEAST 1/(2r-1).

Now choose a uniformly random full n-coordinate direction permutation P and independent uniform full-cube root X. Fix any switch location j∈{1,...,n-r}. Consider the consecutive block of r+1 distinct directions (P_j,...,P_(j+r)), and the true physical root Y of this block, reached after the first j-1 directions from X. The joint law of Y and this ordered direction block is uniform over all physical cube roots and all ordered (r+1)-tuples of distinct coordinates: conditioned on P, XOR with the preceding used-support is a bijection on the uniform cube roots. For any ordered (r+1)-tuple, extend it by q0-(r+1)=r-2 distinct unused coordinate directions to an ordered (2r-1)-tuple, chosen uniformly and independently of Y. This is possible because n>=2r-1. The equality of the first TWO r-face windows depends ONLY on Y and the first r+1 ordered directions; it is unaffected by the auxiliary appended r-2 directions. Sampling the entire q0-block uniformly (via a random B and its random order) has exactly the same initial (Y,ordered r+1 tuple) distribution. Therefore the root-transport theorem forces
\[
\Pr[w_j(X,P)=w_{j+1}(X,P)]\ge\frac1{2r-1},
\qquad
\Pr[w_j\ne w_{j+1}]\le\frac{2r-2}{2r-1}
\]
for EVERY j.

Sum over all m=n-r adjacent switch indicators and apply linearity of expectation. Some genuine full rooted path attains at most the integer floor of the expectation bound. Finally apply Markov to the nonnegative integer random variable D:
\[
\Pr[D\ge q+1]\le \frac{\mathbb E D}{q+1}\le
\frac{(2r-2)(n-r)}{(2r-1)(q+1)},
\]
which yields the stated quantitative fraction. QED.

**ACTIVE NORI CASE r=3.** Every binary physical ORDERED three-face coloring of Q_n, n>=5, with or WITHOUT antipodal-reversal oddness, has SOME full n-edge antipodal geodesic with at most
\[
\boxed{\left\lfloor\tfrac45(n-3)\right\rfloor}
\]
three-face window-color changes. In particular for n=5, \(\lfloor\frac45\cdot2\rfloor=1\), immediately reproving the UNRESTRICTED dimension-five NORI theorem from physical root-transport parity + averaging. The result is nontrivial in all dimensions and supplies a positive fraction of moderately low-defect FULL paths, but does not give a ONE-switch full path for n>=6.

**NEAR-OPTIMAL INTERPRETATION AND NEXT TOPOLOGICAL TASK.** This elementary proof demonstrates that literal five-cycle physical root transports can be integrated along the ENTIRE n-coordinate permutation distribution WITHOUT assuming independent local repairs or splicing separately shifted short paths. It gives a correctly glued GLOBAL expectation statement, unlike naive concatenation of independently repaired five-blocks. However a high-index topological proof of grand NORI closure would need to leverage DEPENDENCES between the m switch indicators more strongly than this separate-marginal bound. The odd pentagon identity supplies a universal degree-one cohomological certificate; the missing step is to build a genuine high-dimensional overlapping-pentagon carrier whose nonzero cup product forces sufficiently many ZERO switches in the SAME full direction order, or to force one-switch via the reversed two-tail exact reachability splice. This theorem does not close unrestricted NORI.

Probabilistic abundance and averaged switch bounds narrow the obstruction class without closing the universal theorem. The final one-switch conclusion requires coherence of several short certificates on one full physical path.
