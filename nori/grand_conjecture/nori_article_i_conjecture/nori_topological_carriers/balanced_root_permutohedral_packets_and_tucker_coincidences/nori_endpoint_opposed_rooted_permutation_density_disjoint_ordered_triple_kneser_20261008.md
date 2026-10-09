# At every NORI root a positive fraction of full geodesics have opposite endpoint colors, via disjoint ordered-triple pigeonhole

# Endpoint-opposed NORI geodesics have positive density at every root

Let n>=7 and c be ANY active reversal-antipodally odd binary coloring of actual PHYSICAL ORDERED three-faces of Q_n. Fix EVERY full-geodesic root x.

For each ordered triple \(\alpha=(a,b,c)\) of DISTINCT coordinate directions, define its genuine physical root-face color
\[
h_x(\alpha)=c(F(x;\{a,b,c\}), (a,b,c)).
\]

**EXACT ENDPOINT IDENTIFICATION.** Let p=(p_1,...,p_n) be any direction permutation of a full antipodal geodesic from x, and let w_1,...,w_{n-2} be its actual ordered-three-face color word. Then
\[
w_1=h_x(p_1,p_2,p_3),\quad
w_{n-2}=1-h_x(p_n,p_{n-1},p_{n-2}).
\]
Proof: the last physical three-face has free directions the final three p coordinates; its fixed exterior coordinates are precisely the initial root bits complemented in every other direction. It is the ANTIPODAL physical face of F(x;final three). The active NORI law complements its color when its order is reversed. Thus first and last actual window colors are OPPOSITE exactly when the two ROOT-FACE triple colors shown on the right AGREE. Notice the triples are disjoint as n>=6. This reduction is root-specific but completely independent of intermediate face colors.

Let \(t=\lfloor n/3\rfloor\) and, when t>=3, put
\[
\delta_t=
\frac{\binom{\lfloor t/2\rfloor}{2}+\binom{\lceil t/2\rceil}{2}}{\binom t2}.
\]

**THEOREM 1 (positive density for n>=9).** For EVERY root x of EVERY active NORI coloring with n>=9, at least a fraction \delta_t of the n! genuine full rooted antipodal geodesics have OPPOSITE first and last window colors. In particular this fraction is >=1/3 for every n>=9 and tends to 1/2 as n tends to infinity.

**Proof.** Uniformly choose t disjoint triples from [n], order their members independently and uniformly, and regard them as t distinct *ordered* 3-direction blocks A_1,...,A_t. Set bits b_i=h_x(A_i). Among t binary bits, the number of equal-colored unordered block pairs is at least C(floor(t/2),2)+C(ceil(t/2),2), attained by as equal a split of bit classes as possible. Thus a uniformly random pair of distinct sampled blocks agrees in color with probability at least \delta_t, regardless of the sample.

By permutation invariance of this random disjoint ordered-block sampling, its selected pair is distributed UNIFORMLY over all ordered pairs of DISJOINT ordered triples of coordinate directions. For a uniformly random full n-permutation p, the ordered first triple (p1,p2,p3) and the reverse-ordered last triple (pn,p_(n-1),p_(n-2)) have exactly the same joint uniform distribution over disjoint ordered triples. Therefore the endpoint-identification formula shows that at least a fraction \delta_t of the n! actual full geodesics have opposite first and last window colors. \(\square\)

**THEOREM 2 (the same property exists quantitatively for n=7,8).** For n=7 or 8, at least 1/7 of all full antipodal direction permutations at EVERY root have opposite endpoint window colors.

**Proof.** For any 7 distinct directions in a random order p1,...,p7, define a seven-cycle in the Kneser graph KG(7,3) of 3-sets:
\[
S_0=\{p_2,p_4,p_6\},\qquad
S_j=([7]\setminus S_{j-1})\setminus\{p_j\},\quad1\le j\le7,
\]
so S_7=S_0, and the seven S_0,...,S_6 are distinct with consecutive members DISJOINT. Independently give each S_j a uniformly random ORDER of its three directions, and color that ordered triple by h_x. Every binary coloring of the seven vertices of an odd cycle has at least one edge whose endpoints have the SAME color; hence at least one of the seven sampled oriented disjoint pairs agrees. Average over the random underlying seven-direction permutation and the random orientations. By complete permutation symmetry, the distribution on each cycle edge is uniform over oriented disjoint ordered triple pairs within the chosen 7-set, hence over all disjoint ordered triple pairs in [n] if the 7-set is itself uniformly random. The total probability of an agreeing pair is at least 1/7. Apply the exact endpoint identification as above. \(\square\)

**STRONG CHAMBER BUNDLE CONSEQUENCE.** For any disjoint ordered triples A,B through x of the SAME root-face color q, EVERY full direction permutation p beginning with A and ending with \operatorname{rev}B has opposite endpoint colors, INDEPENDENT of its middle (n−6) direction order. Therefore each such same-color oriented Kneser edge gives an ACTUAL bundle of exactly (n−6)! endpoint-opposed full geodesics. Combinatorially this is the vertex set of a genuine (n−7)-dimensional permutohedral face (for n>=7) of the full permutohedron of rooted direction orders. Antipodal reversal exchanges this face with the corresponding face having first triple B and last triple rev A.

**NORI consequence under hypothetical grand failure.** Every endpoint-opposed full direction permutation has an ODD number of color changes (the parity of the number of switches equals w_first xor w_last=1). If no one-change full geodesic exists, each of at least \delta_t n! rooted full paths has >=3 changes. Thus the high-index permutohedral endpoint-zero hypersurface intersects a DENSE and honest union of actual zero-labeled permutohedral faces, not merely virtually interpolated zeros.

**Precise limitation.** Endpoint-opposed paths can have 3,5,... switches; the positive density theorem and chamber bundles DO NOT themselves force a one-switch path. The missing step is an equivariant/local exchange theorem reducing at least one of the abundant odd-switch paths to a single switch.

## Root-mobile positive-density common-prefix-support carrier

**Corollary (a single support cut shared by exponentially many actual roots).** Retain n>=9 and \delta_t as in Theorem 1. Fix ANY cut rank \ell∈{1,...,n−1}. Then there exists a coordinate subset S⊂[n] of size |S|=\ell such that at least
\[
\boxed{\delta_t\,2^n}
\]
DISTINCT physical roots x admit at least ONE ACTUAL full antipodal geodesic P(x,\pi) with
(a) opposite initial and final ordered three-face colors and
(b) exactly S as its used-coordinate support after the first \ell directions. Equivalently, these at least \delta_t 2^n rooted paths all visit the intermediate physical vertex x⊕S at time \ell, i.e. the identical translation S of their starting-root set. For n=7,8 use the positive lower density \delta=1/7.

**Proof.** For every fixed root x and cut rank \ell, take a uniformly random full direction permutation \pi. Its initial \ell support S_\pi is uniformly distributed among C(n,\ell) subsets of size \ell. By Theorems1-2 the probability that \pi is endpoint-opposed is at least \delta. For each S define p_x(S)=fraction of full direction permutations with initial support S that are endpoint-opposed. Then
\[
\frac1{\binom n\ell}\sum_{S:|S|=\ell}p_x(S)\ge\delta
\]
for every x. Average again over all 2^n roots: SOME fixed support S obeys \(\sum_x p_x(S)\ge\delta\,2^n\). Since each p_x(S)≤1, at least \delta2^n distinct roots have p_x(S)>0 and thus possess actual endpoint-opposed order witnesses with the SAME initial support S. All these genuine paths pass at time \ell through the translated root set \{x⊕S\}, as claimed. QED.

**Topological significance.** This is an ENTIRE EXPONENTIALLY LARGE MOBILE ROOT-CHART support packet in EVERY middle cut dimension, in contrast with the Borsuk–Ulam arbitrary-root packet theorem which supplies a common support cut for any <=n-2 PRESCRIBED roots. The density result instead selects a good common cut S and then guarantees many actual roots at once. Neither statement implies those paths have monochromatic branches or compatible reverse-tail support complements; that remains the grand extraction gap.

## Stronger every-root / every-rank genuine corridor density

**THEOREM.** Let \delta be the preceding lower bound (\delta_t for n>=9; 1/7 for n=7,8). Then for EVERY individual physical root x and EVERY Hamming rank \ell∈{1,...,n−1}, the set
\[
B_{x,\ell}=\bigl\{S\in\binom{[n]}\ell:\exists\text{ an ACTUAL endpoint-opposed full n-geodesic from x whose FIRST }\ell\text{ used directions have support }S\bigr\}
\]
satisfies
\[
\boxed{|B_{x,\ell}|\ge \delta\binom n\ell.}
\]
Equivalently at least a \delta-fraction of every exact Hamming sphere centered at x consists of PHYSICAL intermediate vertices lying on a genuine full antipodal geodesic from x with opposite first/last three-face colors. The root x and rank ell are COMPLETELY arbitrary.

**Proof.** Sample a uniformly random full coordinate order \pi. Its initial ell-set S is uniformly distributed over all C(n,ell) supports. If \pi is endpoint-opposed, S is necessarily in B_{x,ell}. Thus
\[
\delta\le\Pr[\pi\text{ endpoint-opposed}]
\le\Pr[S\in B_{x,\ell}]
=|B_{x,\ell}|/\binom n\ell.
\]
This proves the bound, without any independence assumption between path goodness and its intermediate support. \(\square\)

**Important limit.** These are endpoint-opposed full geodesics, not necessarily monochromatic or one-switch geodesics. Dense intermediate physical vertices alone do NOT force complementarily reachable monochromatic tails or intersection with the separately constructed bichromatic hub separator. The theorem provides a quantitatively rich root-mobile true-path carrier for future topological intersection forcing.
