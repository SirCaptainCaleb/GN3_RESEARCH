# Causal rounding, ordered derivative blockers and cross-path flux integrability

- Stable ID: note_nori_xvi_budgeted_bigon_partition_exchange_20261017_r11435
- Author: Independent NORI1 mathematician
- Primary home: subsection:paired_direction_involutions_and_geodesic_endpoint_matchings
- Labels: NORI1, budgeted-geodesic-bigon, Eulerian, holonomy, partition-transfer, square-commutators, global-reconfiguration, influence-cone, verified
- Lifecycle: active
- Epistemic status: proved
- Current version: 19
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11435_1
- Updated session: session_nori_r11739_1
- Disposition: none
- Successor: none

## Related references

- note:note_c944daa4c653527d2f6bf61e
- note:note_63844857c6223f15944d26f9
- note:note_f45cc9ea86406fa362616dde
- note:note_6cf2c03748d63e9b6efde8f3
- article:nori_article_xvi_obstruction_compatibility_and_closure
- note:note_nori_xvi_walk_pumping_shortest_repair_20261018

## Research note

# Budget-preserving partition transfers and global reconfiguration of antipodal geodesic bigons

## Scope correction for intrinsic walk energies — 19 October 2026

The proved walk-pumping theorem in `note_nori_xvi_walk_pumping_shortest_repair_20261018`, v3, applies to the intrinsic uniform odd-occurrence Gibbs energy and to the hybrid and causal-coupled policies below that contain it. Write \(A_0^{\rm conn}(c)\) for roots joined to their antipodes by a red walk, and
\[
D_0(c)=\min_{x\in A_0^{\rm conn}(c),\,\pi}
\#\{\text{blue edges of the full geodesic }(x,\pi)\}.
\]
For every fixed \(\beta>0\), the corresponding unrestricted-walk infima equal \(D_0(c)\).

For the lower bound, every rounded word is a full geodesic from its red-antipodally connected starting root, so its blue count is at least \(D_0(c)\). For the upper bound, start at a minimizing root and choose a red antipodal path. For each direction, a closed red excursion can visit a red edge in that direction and return. Append such excursions in the desired direction order before the antipodal path, and repeat the designated red edge back and forth sufficiently often in each excursion. Uniform odd-occurrence selection then chooses the designated excursions in the desired order with probability tending to one. The Gibbs survival tends to \(\exp(-\beta D_0(c))\). Hybrid and coupled policy classes containing this independent policy inherit the same infimum.

The pathwise rounding identities and explicit certificates below retain their proved scope. Their unrestricted-walk minimizations therefore provide reformulations of \(D_0\). A proposed new global bound must address this quantity or restrict the walk family with justification. The pumping proof does not assert the same collapse for every first/last-only functional.

The globally shortest red antipodal path restriction in the cited note avoids these inserted excursions and retains the established product law. Its required uniform sublinear bound remains open. More generally, a certificate statistic dominating the global minority defect needs only a uniform sublinear upper bound for the tensor-amplification implication; additivity of that auxiliary statistic is optional.


Let c be any legal antipodally odd red/blue coloring of the undirected edges of Q_n. For each direction i, let U_i swap endpoints of red i-edges and fix endpoints of blue i-edges. Thus U_i is an involution. For a word w=(w_1,...,w_l) write H(w)=U_(w_l)...U_(w_1).

Fix a direction permutation pi=(i_1,...,i_n) and A subseteq [n] containing the last direction i_n and omitting the first i_1. Write B=[n]\A and W(pi,A)=(pi|A) pi (pi|B), with induced orders. Each direction appears twice. The underlying cube walk traces a simple 2n-cycle with two disjoint full geodesic sides: see the established simple-bigon normal form note_c944daa4c653527d2f6bf61e. A red fiber lift of some W(pi,A) sending its initial fiber state x to bar x is equivalent to a monochromatic full antipodal geodesic for c.

THEOREM 1 (partition-changing exchange formula). Suppose j belongs to B and is neither the first nor last direction of pi. Put
P=pi|{a in A:a precedes j}; Q=pi|{a in A:j precedes a};
R=pi|{b in B:b precedes j}; S=pi|{b in B:j precedes b};
X=Q pi R.
Then W(pi,A)=P X j S and W(pi,A union {j})=P j X S. Their holonomies H,H' satisfy
    H'H^(-1)=H(S) H(X) U_j H(X)^(-1) U_j H(S)^(-1).
Both words remain eligible, simple, and use every direction twice. The quotient is a product of at most |X|-1 <= 2n-2 conjugates of elementary square commutators (U_j U_k)^2, omitting factors with k=j.

PROOF. Direct concatenation of the pi-restrictions gives the two word identities. Their return permutations are H(S) U_j H(X) H(P) and H(S) H(X) U_j H(P), respectively; cancel H(P) and use U_j^(-1)=U_j. Expand the commutator of U_j with H(X), by the standard commutator-of-products identity, into the commutators with its individual involutive factors. X contains one occurrence of j, whose commutator factor is trivial. Since the letters of Q and R are disjoint from j and from one another, |X|<=2n-1. QED.

THEOREM 2 (forward influence-cone confinement). Place a directed influence arc a -> b whenever the b-th edge-color function depends on vertex bit a. Let C(j) be the set reachable from j in this directed graph, including j. Then for every root x the two exchanged return endpoints satisfy
    supp(H'(x) xor H(x)) subseteq C(j).
The statement holds for arbitrary nonlinear legal colorings.

PROOF. No color rule outside C(j) reads any input bit inside C(j), by forward closure. The projection of each red-swap U_i to the complement of C(j) is therefore well-defined; U_i for i in C(j) induces the identity there. In the exchange identity of Theorem 1, U_j projects to the identity, so the entire conjugated commutator projects to the identity. Thus H' and H agree off C(j) at every root. QED.

THEOREM 3 (all-eligible-bigon connectedness). For every n>=3 form the finite graph whose vertices are all eligible pairs (pi,A). Allow (i) a single interior label membership toggle j in A while pi is fixed, and (ii) an adjacent transposition of letters of pi that preserves first-in-B and last-in-A with A fixed. This graph is connected. Every intermediate state retains the simple-bigon condition and the two-use-per-direction budget. Cross-part adjacent swaps have the one-transported-square correction from the archived median-shuffle theorem note_63844857c6223f15944d26f9; same-part adjacent swaps change only two copies and yield a product of at most two transported-square corrections.

PROOF. For fixed pi, the n-2 interior A-memberships can be toggled arbitrarily, so its fiber is the full Boolean (n-2)-cube. Adjacent transpositions generate all permutations. Before transposing letters outside the final two positions, choose A to consist solely of the final letter; then both swapped letters belong to B and the transposition is permitted. Before transposing the final two letters, choose A to contain precisely those two letters; neither is the first, since n>=3, and swapping them preserves eligibility. Restore a canonical singleton-final A after each transposition, then toggle the interior memberships to reach the chosen terminal A. All steps are admissible. The holonomy claims follow because each adjacent transposition changes only the middle pair and, when the swapped labels are in one part, an additional exterior pair, with each replacement introducing one conjugated square commutator. QED.

INDEPENDENT FINITE VERIFICATION. Standard-library Python verifier nori_xvi_budgeted_bigon_partition_exchange_verify.py: generate legal colorings from independent antipodal edge-orbit bits; for every eligible tested triple (pi,A,j), form the chronological correction word
    S[::-1] + (j,) + X[::-1] + (j,) + X + S
and apply it to H(W(pi,A))(x) for every cube root x; assert equality with H(W(pi,A union {j}))(x). Compute the influence digraph by Boolean derivatives and verify the endpoint difference is supported within C(j). Build the eligible-pair move graph and exhaust its connected component. Results:
    Q3: 64 legal samples, 384 transfer checks, 12 eligible states, connected;
    Q4: 60 legal samples, 5760 transfer checks, 96 eligible states, connected;
    Q5: 8 legal samples with 40 orders each, 3840 transfer checks, 960 eligible states, connected.
The verifier and proof were rerun in the continuing research session. For local provenance the verifier SHA256 is 01950b1782eb4d66eb36cd4ff514292f12c0aa631f430450c3c3518a423e76b5 and manuscript SHA256 is f0b007b0049037cd70b26bedc3d4515c837e2baac3de1af82d6829a9bb1501fc.

SCOPE AND PRIOR WORK. The one-partition median shuffle lattice, simple-bigon normal form, chord-crossing curvature factorization, and normal-generation results are established in notes note_63844857c6223f15944d26f9, note_c944daa4c653527d2f6bf61e, note_f45cc9ea86406fa362616dde and note_6cf2c03748d63e9b6efde8f3. The partition-changing holonomy formula and global connectedness of the full admissible parameter space extend these statements. These theorems supply a budget-preserving move calculus; they do not prove the existence of a return with H(W)(x)=bar x. A closure argument would need a jointly rooted augmentation or a cubically forced dual certificate beyond connectedness. NORI1 remains open.

## New extension: tensorized return energy
For every direction permutation pi and every subset A, let W_pi(A)=(pi|A) pi (pi|A^c) and eps_pi(c)=min_(A,x) d_H(H_W(x),bar x). The adaptive eta(c)=min_pi eps_pi(c) satisfies eta(c box d)=eta(c)+eta(d) for all legal colorings on disjoint direction sets: each global doubled word projects to the same kind of doubled word in each factor, and concatenating factor optima proves the converse inequality. Every successful doubled return produces a red full geodesic because each direction occurs twice and must execute one red swap to reverse its bit. Therefore eta(c)=0 iff c has a monochromatic full geodesic, and the proposed universal bound eta(c)=o(n) would prove NORI1 by Cartesian amplification. Full mathematical proof and certificate: /mnt/data/nori_xvi_tensor_order_radius_and_q5_certificate.md.


## Central-order exchange radius, its product law, and a five-dimensional certificate

Define r_pi(c) as the minimum Kendall adjacent-swap distance from pi to a central order sigma with some successful doubled return H_(W_sigma(A))(x)=bar x; put r_pi(c)=infinity when no such return exists. For all legal c,d and concatenated reference orders pi+rho, the two product laws hold:
eps_(pi+rho)(c box d)=eps_pi(c)+eps_rho(d);
r_(pi+rho)(c box d)=r_pi(c)+r_rho(d).
Proof: factor projections of W_sigma(A) retain the partition-complete doubled-word form, and the endpoint Hamming deficit splits as the sum of the factor deficits. For r, the Kendall distance from pi+rho to a successful global sigma equals the sum of its two within-factor distances plus nonnegative cross-factor inversions. Concatenating minimizing successful factor orders gives equality in both cases. This proof does not assume that restrictions to factors satisfy simple-bigon eligibility.

FINITE Q5 CERTIFICATE. Specify legal edge colors c_i by 16-bit hexadecimal truth tables over the other four vertex bits, sorted in ascending direction order, the least significant table bit representing all-zero input:
c_0=0x9716; c_1=0x3173; c_2=0x9D46; c_3=0x2F0B; c_4=0xE718.
Own-direction independence is immediate, and each table complements under bitwise antipodality, proving legality. The 40 antipodal edge-orbit bits have the alternative mask 0x180B467316 using direction-first and smallest-representative order.

For the prescribed central order pi0=(0,1,2,3,4), exhaustive enumeration of all 32 subsets A and all 32 roots gives endpoint-defect histogram: distance1=62, distance2=221, distance3=430, distance4=215, distance5=96. Therefore eps_pi0=1, and there are NO successful doubled returns even allowing noneligible A. The eight eligible A choices alone give histogram distance1=11, distance2=61, distance3=98, distance4=63, distance5=23.

One adjacent central swap gives pi1=(0,1,2,4,3), eligible A={2,3} (integer mask12), root x=17 and chronological word W=(2,3,0,1,2,4,3,0,1,4). Its red swap endpoint is 14=bar 17, and its nonstationary red steps give the red full geodesic direction word (2,1,4,3,0). Thus r_pi0=1. Independently enumerating all 32 roots and 120 direction orders gives 140 red full geodesics. The example is NOT a counterexample to NORI1.

THEOREM (linear radius and fixed-order defect). Taking k Cartesian copies of the seed on Q_(5k), with reference order Pi_k concatenating k copies of pi0, gives eps_(Pi_k)=k and r_(Pi_k)=k by the two tensor laws. These colorings all have monochromatic full geodesics. Every successful doubled return must change the central order inside each 5-direction block, so at least k adjacent central-order swaps are indispensable, regardless of roots and partition transfers. k swaps attain the bound by concatenating pi1 and its eligible A/root in every block; the global resulting bigon is eligible as well. A parameter-graph route maintaining eligibility uses k central swaps and one final partition toggle: initially include the globally last direction in the eventual A, perform all swaps, then remove that direction.

The all-dimensions statements use algebraic proof. Finite verification is reproducible with /mnt/data/nori_xvi_order_radius_tensor_verify.py and the accompanying complete manuscript /mnt/data/nori_xvi_tensor_order_radius_and_q5_certificate.md. The 65536 legal Q4 colorings were independently enumerated and all admit at least one doubled return at a prescribed central order; the displayed Q5 certificate is the first failure across dimensions 2 to 5.

## Balanced Eulerian lifting of linear order radius
From the displayed Q5 seed define B on Q10 by B_i(x,y)=c_i(x) and B_(5+i)(x,y)=1+c_i(x) mod2 for i=0,...,4. The rules are legal and every vertex has five red and five blue incident edges. Dummy red swaps change only y. With reference central order (0,1,2,3,4,5,6,7,8,9), every return projects on old x bits to an obstructed Q5 fixed-order return, so its deficiency is at least one. Checking all 1024 partitions and 32 old roots (new-bit initial states do not change the deficiency) confirms eps_identity(B)=1. The one-adjacent-swap order (0,1,2,4,3,5,6,7,8,9), eligible A={2,3,5,8,9} (mask812), and starting root (17,0) have antipodal return. Thus r_identity(B)=1. Tensor powers give balanced legal colorings on Q_(10k) with eps_identity=k and r_identity=k although each coloring admits monochromatic full geodesics. This establishes that central-order exchange may require linearly many adjacent swaps even in a balanced Eulerian instance.

## New positive theorem: one-error doubled return gives a short monochromatic antipodal path
Let c be any legal coloring, W any word with each direction appearing twice, and U_i the red edge-swap involutions. If a root x has endpoint y=H_W(x) differing from its antipode bar x in at most one bit, then there is a red antipodal path of length at most n+2. If there is no error, delete stationary swaps to obtain a red full geodesic.

When the sole deficient direction is j, y=bar x+e_j. Deleting all stationary swaps produces a red walk P from x to y: every i!=j moves once, while j moves either zero or two times. Its length is n-1 or n+1. By undirectedness and antipodal oddness, c_j(y)=c_j(bar x+e_j)=c_j(bar x)=1-c_j(x). Thus one endpoint's j-edge is red. If c_j(x)=0, prepend x+e_j -> x to P; the new endpoints x+e_j and y are antipodal. Otherwise append y -> bar x; the endpoints x and bar x are antipodal. The resulting red walk has length n or n+2. Erase any closed subwalk to obtain a simple red antipodal path no longer than n+2. In the zero-j-execution case it has length n, so is a red full geodesic.

A hypothetical NORI1 counterexample with a one-error doubled return must therefore execute the deficient direction twice. It has a red antipodal n+2 path. Combined with the established Article XI one-detour result this forces an antipodal full geodesic with at most floor((n-1)/3) blue edges. Thus a bad coloring with shortest red antipodal path at least n+4 must satisfy adaptive return energy eta>=2. No universal eta<=1 bound is asserted.

Independent verifier /mnt/data/nori_xvi_oneerror_balanced_verify.py confirms legality and all one-error extensions for the Q5 tables previously archived: of 62 one-error partition/root returns, 17 execute the missing direction zero times and 45 execute it twice. The same verifier checks balanced Q10 legality, 32768 partition/old-root cases, minimum central-identity defect one, and the eligible single-swap return at root 17 and partition mask812. Full proof /mnt/data/nori_xvi_oneerror_extraction_and_face_interface.md.

Prospective higher-error completion must preserve simultaneous red and blue direction-simple path information on the face spanned by deficient dimensions, not merely one missing-edge color per dimension. This is a proposed research target, not a solved general forcing theorem.

## Arbitrary-shuffle return-energy tensor theorem and neutral-order plateaus

Let eps_c(pi)=min_(A,x) d_H(H_(W_pi(A))(x),bar x), with W_pi(A)=(pi|A) pi (pi|A^c), and ANY exterior subset A. For legal independent factors c,d with disjoint direction sets I,J, for EVERY global central order pi (including arbitrary interleavings),
 eps_(c box d)(pi)=eps_c(pi|I)+eps_d(pi|J).
Proof: restrict each doubled word to a factor; the resulting factor word still has the partition-complete W form. Independent-factor swaps commute and act on disjoint vertex bits, so Hamming return deficiencies add. Minimize factor roots and partitions independently.

Consequence: an adjacent transposition of directions from DIFFERENT product factors leaves eps unchanged. Let c be the certified Q5 coloring with tables (9716,3173,9D46,2F0B,E718), whose identity central order has eps=1 and whose last-two-swapped order has eps=0. Take k independent copies and interleave their central order by direction rank, listing each factor's direction 0, then every factor's direction 1, ..., through direction 4. The product return energy equals k, and EVERY immediately adjacent transposition is energy-neutral. No same-factor directions begin closer than k positions; at least k-1 neutral cross-factor swaps are necessary before any same-factor swap can change the energy. The k-th swap CAN lower energy by one: first move a factor's direction 4 across the intervening k-1 others until adjacent to its direction 3, then swap that final pair. Therefore the minimum adjacent-exchange distance to a strictly smaller energy is precisely k. The paired balanced Q10 lift gives the same statement in the vertex-balanced Eulerian regime of dimensions 10k. This is a uniform obstruction only to a STRICT one-step descent claim, not to the adaptive energy approach.

Formal manuscript and certificate: /mnt/data/nori_xvi_plateau_safe_tensor_descent.md and /mnt/data/nori_xvi_plateau_tensor_example_verify.py.

## Tensor-stable weak descent: a specified OPEN forcing principle

Let WD(c) mean that every central direction order pi with positive eps_c(pi) admits a finite path of adjacent central swaps along which eps never increases and whose final value is strictly smaller. Neutral moves are allowed.

THEOREM. If legal independent factors c,d each satisfy WD, then their Cartesian product also satisfies WD. By the arbitrary-shuffle product identity, cross-factor adjacent swaps preserve eps. For any pi whose product energy is positive, choose a factor of positive restricted energy. Group that factor's directions by cross-factor adjacent swaps, all energy-neutral, and execute the factor's WD descent path inside the contiguous block. The product energy does not increase and eventually decreases strictly.

CONDITIONAL CLOSURE. If WD holds for all legal colorings in all dimensions, NORI1 holds: starting at any pi, repeat the non-increasing improvement paths. The nonnegative integer eps decreases at the end of each stage until it reaches zero, yielding a red full antipodal geodesic. No unrestricted proof of WD is claimed.

Finite stress test: flip every subset of at most five of the 40 antipodal edge-orbit bits of the certified Q5 coloring (rules 9716,3173,9D46,2F0B,E718). This produces 760099 legal colorings. At the central identity order, each was checked over 1024 root/partition pairs. Precisely 165 had positive eps; all 165 had a strictly improving adjacent central swap among the four possibilities. This is selected finite evidence, not exhaustive Q5 or proof of WD. Verifier source /mnt/data/nori_xvi_permutohedron_descent_radius5.cpp.

The earlier note_nori_antipodal_two_direction_square_connector_20261017 already handles the two-missing-direction square interface and the opposed-core completion theorem; those are prior work, not claimed anew. Full plateau-safe analysis /mnt/data/nori_xvi_plateau_safe_tensor_descent.md.


## Cyclic root-slide derivative transport and an unrestricted positive corridor theorem
For a legal coloring let U_i swap red direction-i edges and fix blue edges, let W=(i,V), x root, y=H_W(x), and let E=x XOR y XOR 1_n be the return-error mask. Rotate W to W'=(V,i) and transport the endpoints to x'=U_i(x), y'=U_i(y). Then H_(W')(x')=y' and
 E_(W')(x')=E XOR (1 XOR Delta_E c_i(x))*e_i,
where Delta_E c_i(x)=c_i(x) XOR c_i(x XOR E). PROOF: H_(V,i)=U_i H_(i,V) U_i; the change of error in bit i is c_i(x) XOR c_i(y) = 1 XOR Delta_E c_i(x) by y=bar x XOR E and antipodal oddness. All other error bits are invariant under this rotation.

POSITIVE FORCING LEMMA. Suppose W uses every direction twice, and its return-error mask is {j}. Fix an occurrence of j in W. If the root-transported cyclic shifts preceding that occurrence all satisfy Delta_j c_i(x_t)=1 for their shifted directions i!=j, then the return error stays {j} until j reaches the first position. Sliding j then eliminates the error because c_j ignores its own bit. Removing stationary red swaps from the resulting doubled word yields a red full antipodal geodesic. The same holds immediately if the deficient letter occurs at the first or last word position. In a hypothetical bad coloring every such one-error corridor must be blocked by some inactive derivative; compatibility of these blockers across roots and exchanged orders remains OPEN.

REVERSAL SYMMETRY. reverse(W_pi(A))=W_(reverse pi)(A^c), and red swaps are involutive. The substitution x=H_W(z) yields d_H(H_W^(-1)x,bar x)=d_H(H_W z,bar z). Therefore all rootwise defect histograms agree for reversed/complemented word pairs and eps_c(pi)=eps_c(reverse pi). The number of successful central orders is even for n>=2.

VERIFICATION. /mnt/data/nori_xvi_cyclic_error_transport_verify.py tested 30000 random legal cyclic-return identities in dimensions 3-7 and 300 complete reversal histograms. For the established Q5 seed (9716,3173,9D46,2F0B,E718), 62 rooted partition-complete doubled returns have one error; 19 admit zero-error cyclic shifts, all via the active corridor; 43 do not admit such shifts. Full proofs: /mnt/data/nori_xvi_cyclic_root_transport_and_influence_corridor.md. These are conditional repair criteria, not NORI1 closure.


FULL PERMUTOHEDRON FINITE AUDIT (strengthening the previously saved local Q5 test). For the 165 legal Q5 colorings with positive return energy at the identity order among the 760099 colorings within five antipodal edge-orbit flips of the seed, compute eps_c(pi) for ALL 120 central permutations, using all 32 roots and 32 exterior subsets for each. For every order pi with eps_c(pi)>0, at least one of its four adjacent-transposition neighbors has strictly smaller energy. No positive local minima or blocked plateau exits occur anywhere in these 165 complete 120-vertex energy landscapes. This is a finite targeted result, NOT a theorem for arbitrary legal Q5 colorings or for unbounded n. Reproducible optimized C++ verifier: /mnt/data/nori_wd_full_q5.cpp; output positive_at_identity=165, local_positive_count=0, WD_bad=0 in 2.97s on the recorded run. Separately the Q5 seed has positive energy at only two of its 120 central permutations, namely the identity and its reversal; the remaining 118 have zero energy. This explains why selected small-dimensional stress tests can be less adversarial than the all-dimensional product plateaus.


## Curvature-controlled flat-strip repair: unrestricted quantitative forcing theorem

For a legal antipodally odd two-coloring and any doubled direction word W, suppose its red-swap return from x has one deficient antipodal direction j, so y=H_W(x)=bar x XOR e_j. Every other direction executes once; j executes zero or two times. In the zero-execution case, an appropriate red endpoint j-edge completes a red full geodesic.

THEOREM. In the two-execution case, write the executed red walk as P=R j S j T, with R,S,T using every non-j direction once. Let z_t be the starting state of the red S-step in direction i_t and put
K(P,j)=sum_(i_t in S) Delta_j c_(i_t)(z_t),
where Delta_j c_i(z)=c_i(z) XOR c_i(z XOR e_j) is zero or one. Then there exists a full antipodal geodesic with precisely K(P,j) blue edges, so the unrestricted minority defect delta(c)<=K(P,j).

PROOF. Remove both j steps. The R and T edges retain their previous red colors, while each edge of S is translated in direction j and acquires color Delta_j c_(i_t)(z_t). The shortened direction word RST has length n-1 and runs from x to bar x XOR e_j. Own-direction independence and antipodal oddness imply c_j(bar x XOR e_j)=1 XOR c_j(x). Thus one can insert a red j-edge at an endpoint: prepend x XOR e_j -> x if c_j(x)=0 (changing the root accordingly), or append (bar x XOR e_j) -> bar x if c_j(x)=1. The result uses all n directions once and has K blue edges.

THEOREM (incoming flux and square-curvature parity). On that same S strip,
 XOR_(i_t in S) Delta_(i_t)c_j(z_t)=0.
Consequently, writing kappa_(j,i)(z)=Delta_j c_i(z) XOR Delta_i c_j(z) for the cubical square curvature,
 K(P,j) mod2 = XOR_(i_t in S) kappa_(j,i_t)(z_t).
PROOF. Let a be the state just before the first red j step and s the sum of S direction bits. Both j steps are red, so c_j(a)=c_j(a XOR s)=0, since c_j ignores its own bit. Telescoping the j-color along S proves zero incoming-flux parity. Expanding each curvature identity proves the outgoing-flux parity statement.

POSITIVE CONSEQUENCES. A one-error return whose strip has no active outgoing derivative produces a red geodesic. If all strip squares are flat, K is even; a hypothetical bad coloring possessing such a return must have at least two active outgoing derivatives. If the entire j-influence column is zero, flat-strip repair always works; if it is one on all other directions, the previously proved active-influence cyclic corridor works. The mixed derivative case remains unresolved. These constraints use the same color variables across rooted paths and squares, as demanded by Article XVI.

INDEPENDENT VERIFICATION. /mnt/data/nori_xvi_flat_strip_defect_verify.py, with proof /mnt/data/nori_xvi_flat_strip_flux_and_curvature.md, checks 600 legal colorings and 60000 rooted partition-complete return words in dimensions 3 through 8. It verifies all 7224 one-error cases, the constructed full geodesic, its blue-edge count, incoming-flux parity and curvature parity. For the earlier nonlinear Q5 seed with tables (9716,3173,9D46,2F0B,E718), the 62 one-error returns at central identity order consist of 17 zero-execution returns and 45 two-execution returns. Among the latter, strip flux K has frequency K0:29, K1:12, K2:4. Thus 46 of the 62 return cases provide a red geodesic by direct cancellation, although no root/partition gives a zero return for that prescribed central order. A separate exhaustive census of the 760099 legal Q5 perturbations within five antipodal edge-orbit flips shows that all 165 cases with positive identity-order return energy admit a zero-flux two-execution return; 161 additionally admit zero-execution returns. C++ verifier /mnt/data/nori_xvi_flatstrip_neighborhood_census.cpp. These are finite tests, not a universal one-error existence theorem.

SCOPE. The derivative/curvature inequality is proved for arbitrary legal colorings whenever a one-error doubled return exists. A dimension-uniform sublinear bound on minimum strip flux, or a universal zero-flux witness, remains OPEN. This is a constructive bridge between Article XVI budgeted holonomy and square integrability, not NORI1 closure.


## Influence-outdegree compression of any monochromatic antipodal n+2 path

UNRESTRICTED THEOREM. Let c be ANY undirected two-coloring of Q_n, and let P be a red antipodal path of length n+2. It has direction word R j A j B j T, where j is traversed thrice and each other direction once. For every edge i_t in A or B starting at state z_t along the original red path, put d_t=Delta_j c_(i_t)(z_t)=c_(i_t)(z_t) XOR c_(i_t)(z_t XOR e_j). Let K_A=sum_A d_t and K_B=sum_B d_t. Let dplus(j) be the number of other directions i for which c_i depends somewhere on vertex bit j. Then
 delta(c)<=min(K_A,K_B)<=floor(dplus(j)/2),
where delta is the minimum number of minority-colored edges on a full antipodal geodesic.

PROOF. Removing the first two j-steps leaves a full antipodal geodesic. Its edges outside A retain their red color, and each A edge is translated by e_j and takes color d_t, so it has K_A blue edges. Similarly deleting the final two j-steps gives a full antipodal geodesic with K_B blue edges. Since A and B use disjoint direction sets, each active derivative on either strip uses a distinct outward influence neighbor of j. Thus K_A+K_B<=dplus(j), proving the estimate. Deleting the first and last j-steps gives a third full geodesic with K_A+K_B blue edges. No antipodal oddness assumption is required for these conclusions.

CURVATURE FLUX. The red j-edge at each end of either strip implies that incoming derivatives to j have zero sum modulo two along that strip, using own-direction independence. Therefore K_A mod2 is the XOR of square curvatures kappa_(j,i_t)(z_t) over A, and likewise for K_B over B. This couples the two quantitative defects to disjoint square-curvature regions in the same path.

Combining with the archived one-detour three-repair theorem yields
 delta(c)<=min(floor((n-1)/3),floor(dplus(j)/2)).
Thus any legal coloring with a red antipodal n+2 path repeated in a direction of outgoing influence degree at most one contains a monochromatic full antipodal geodesic. Conversely a hypothetical NORI1 counterexample with an n+2 monochromatic path must repeat a direction with outgoing influence degree at least two. Existence of an n+2 monochromatic path in every legal coloring is NOT asserted.

PROOF AND TESTS. /mnt/data/nori_xvi_flat_strip_flux_and_curvature.md and /mnt/data/nori_xvi_three_occurrence_flux_verify.py. The independent verifier conditioned legal odd colorings on 640 simple red antipodal n+2 paths, 80 paths per dimension n=4,...,11, and checked all three induced geodesics, their blue-edge counts, the curvature parities, legality and the influence-degree bound. All checks passed. The theorem itself has a dimension-uniform combinatorial proof.

This advances Article XVI Programme B and the path-length/minority-defect bridge with a direct quantitative influence-sensitive inequality; unrestricted NORI1 remains OPEN.


## Causal first-last rounding and product-additive influence exposure for arbitrary red antipodal walks

Let P=(x;w_1,...,w_L) be any red walk from x to bar x in an undirected two-colored Q_n. Every direction occurs an odd number of times. Write f_i,l_i for its first and last positions, R for the repeated directions, and v_t for the starting vertex at time t. In the directed influence graph put j->i when c_i changes under toggling vertex bit j somewhere. Define J_i(t)={j in R excluding i: j->i, f_j<t<l_j}, r_i(t)=|J_i(t)| and the nonnegative causal exposure
 Lambda_c(P)= (1/2) sum_i [2-2^(-r_i(f_i))-2^(-r_i(l_i))].

THEOREM (all-length rounding). Independently retain for each direction either its first or last occurrence, discarding all others. Every retained direction word is a full antipodal geodesic. For an original red step i at time t, let h_i(t)=2^(-r_i(t))sum_(S subseteq J_i(t))c_i(v_t XOR e_S). The expected blue-edge count of the random rounded geodesic is
 (1/2)sum_i [h_i(f_i)+h_i(l_i)] <= Lambda_c(P).
Consequently some full geodesic has at most floor(Lambda_c(P)) blue edges. This holds for arbitrary undirected colorings and arbitrary walk length.

PROOF. Conditional on choosing i's occurrence t, the new edge starting vertex differs from v_t by the parity of discarded preceding occurrences. For any j!=i that parity is zero if t lies outside the first-to-last j interval, because the total number of j occurrences is odd. If f_j<t<l_j, the fair choice between retaining j first or last makes that shift bit independent uniform. Shifts in nonreader directions and direction i itself do not alter c_i. Thus the retained i-edge color averages uniformly over the Boolean subcube generated by J_i(t), giving h_i(t). This subcube contains the original red edge, hence h_i(t)<=1-2^(-r_i(t)). Summing proves the theorem.

COROLLARY (influence-neighborhood control). Let r=|R| and Nplus(R)={i:some j in R influences i}. The blue minority defect delta(c) for legal odd colorings satisfies
 delta(c)<=floor[(1-2^(-r))*|Nplus(R) outside R|+(1-2^(-(r-1)))*|Nplus(R) intersect R|].
For r=0 the original walk is a red geodesic. For r=1 this becomes delta(c)<=floor(dplus(j)/2) for the sole repeated direction j, INDEPENDENT of how often j occurs. The prior half-outdegree theorem required a walk of length n+2. If each i has a first or last occurrence outside all influencing repeated-direction intervals, choosing those safe occurrences produces a red geodesic directly.

THEOREM (arbitrary-shuffle tensor identity). For two independent legal colorings c,d, any red antipodal product walk P projects to factor red antipodal walks P_c,P_d. Foreign directions have no influence arcs, and within-factor first/last relative orders are preserved under projection. Hence
 Lambda_(c box d)(P)=Lambda_c(P_c)+Lambda_d(P_d)
for EVERY interleaving. The color-sensitive mean-blue expression above is also additive.

Define Phi(c) as the infimum of Lambda_c(P) over finite red antipodal WALKS. It is finite for legal odd c by the Wu-Yang monochromatic antipodal-path theorem and antipodal red/blue reversal. Projection and concatenation give Phi(c box d)=Phi(c)+Phi(d). The rounding theorem yields delta(c)<=Phi(c). Every strictly positive Lambda_c(P) is at least 1/4, so Phi(c)=0 iff some walk has zero score and hence a red geodesic; the converse follows from taking a red geodesic as P. A universal estimate sup_(c legal Q_n)Phi(c)=o(n) would PROVE NORI1 by the established Cartesian amplification, but that estimate remains OPEN. This creates a causal interval-overlap target for arbitrary monochromatic walks without presupposing small path-length excess.

INDEPENDENT VERIFICATION. Full proof /mnt/data/nori_xvi_causal_interval_rounding.md. Python nori_xvi_causal_first_last_rounding_verify.py constructed 880 legal odd colorings with red antipodal walks in dimensions 4-9, exhausting all first/last choices and checking the complete subcube-averaging formula and causal upper bounds. nori_xvi_causal_tensor_audit.py checked 40 independent product colorings (4+4,4+5) with arbitrarily interleaved red paths and verified both tensor formulas. These tests are finite audits, not NORI1 closure.


## Spectral survival and the optimal temporal rounding law

For an arbitrary red antipodal walk P=(x;w_1,...,w_L), every direction i appears an odd number of times. Let O_i be its occurrence positions and independently select one T_i in O_i with distribution mu_i. Deleting unselected occurrences yields a full antipodal geodesic. Let v_t be the old starting vertex and k_j(t) the number of j-steps before t. Put F_j(t)=Pr(T_j<t) and q_j(t)=F_j(t) if k_j(t) is even, else 1-F_j(t).

THEOREM (full independent-occurrence expectation). Conditional on choosing T_i=t, the change to the starting vertex of its i-edge in each other bit j is an independent Bernoulli(q_j(t)). Thus the conditional blue probability equals the independent-product average of c_i(v_t XOR e_S) over subsets S of [n] excluding i, with bit inclusion probabilities q_j(t). Summing with weights mu_i(t) gives the expected blue count. No antipodal oddness is required.

PROOF. The j-bit shift equals k_j(t) mod2 XOR 1_(T_j<t), by comparing counts of previously executed j-steps in the old and shortened paths. Independence is inherited from the independently chosen retained occurrences. Since c_i ignores bit i, the i-bit shift is immaterial. Summing the resulting blue indicators proves the identity. Every old edge at v_t is red, so the conditional blue probability is at most one minus the probability that every relevant bit remains unchanged.

THEOREM (unique temporal minimax). Suppose direction j appears m>=3 odd times. Over all one-occurrence selection laws mu_j, the smallest possible maximum parity-disturbance probability among the m-1 gaps between its consecutive occurrences is 1/2. It is attained uniquely by giving probability 1/2 to the first and last occurrences and zero to every interior occurrence.

PROOF. The two outermost interior gaps have disturbance probabilities 1-mu_j(first) and 1-mu_j(last). Their maximum is at least 1-(mu_j(first)+mu_j(last))/2 >=1/2. Equality forces the endpoint probabilities to be 1/2 each and all other probabilities zero. That choice makes every intermediate disturbance probability 1/2. This proves that the earlier fair first-last rounding is minimax among color-blind independent single-occurrence policies; color-sensitive data are needed for further strengthening.

FOURIER SURVIVAL THEOREM (legal odd colorings). Put g_i(v)=(-1)^(c_i(v)), chi_S(v)=(-1)^(sum_(j in S)v_j), and its normalized Walsh coefficient ghat_i(S)=2^(-n) sum_(v in Q_n)g_i(v)chi_S(v). Own-bit independence eliminates supports containing i, while antipodal oddness eliminates EVEN-cardinality supports. Under independent occurrence choices the conditional blue probability at original i-edge starting v_t is
  (1/2)[1 - sum_(S not containing i, |S| odd) ghat_i(S)chi_S(v_t) product_(j in S)(1-2q_j(t))].
For fair first-last rounding, every q_j(t) is zero outside its first-to-last open interval and 1/2 inside. Therefore the product multiplier removes every Walsh support meeting the causally exposed set J_i(t); only odd supports S contained in the unexposed directions T_i(t) survive. Writing Theta_c(P) for the expected blue count under fair first-last rounding,
  Theta_c(P)=n/2-(1/4) sum_i sum_(t in {f_i,l_i}) sum_(S subseteq T_i(t), |S| odd) ghat_i(S)chi_S(v_t).
This is the coloring-sensitive sharpening of the influence-only score Lambda_c(P), and obeys delta(c)<=Theta_c(P)<=Lambda_c(P). A residual Fourier sum strictly greater than 2n-4 forces Theta_c(P)<1 and hence a red full antipodal geodesic.

EXPLICIT Q5 POSITIVE CERTIFICATE. Define legal edge rules c_i(v) as bit v of the 32-bit tables, with vertex bit v indexed from zero:
 c_0=0x0C0CCFCF, c_1=0x0F55550F, c_2=0x55BB2255, c_3=0xCECE8C8C, c_4=0x2F0B2F0B.
They ignore bit i and reverse under vertex complementation. Starting at x=11, the direction word W=(1,3,2,1,4,1,3,0,4,3,4) is a SIMPLE RED antipodal path. Its repeated directions are 1,3,4. The eight first-last rounded geodesics have blue counts (0,0,2,1,1,1,0,0). The coarse causal influence exposure is Lambda=5/2, while the Fourier-filtered mean is Theta=5/8<1. Consequently Fourier survival CERTIFIES a red full geodesic where the influence-only bound cannot. One witness has word (1,3,2,4,0), vertices 11,9,1,5,21,20=bar 11.

TENSOR THEOREM AND CLOSURE TARGET. Define the intrinsic color-sensitive walk energy Psi(c)=inf_(P red antipodal walk) Theta_c(P). It is finite for legal odd colorings by Wu-Yang monochromatic antipodal paths and antipodal color interchange. Under any interleaving of independent Cartesian factor walks, first-last random rounding and its expected blue count split into independent factor contributions; projection and concatenation show
  Psi(c box d)=Psi(c)+Psi(d).
The earlier energies satisfy delta(c)<=Psi(c)<=Phi(c). If c has no red geodesic, every rounded geodesic has at least one blue edge, so Psi(c)>=1. If it has a red geodesic, Psi(c)=0. Thus proving the unrestricted uniform estimate sup_(c legal Q_n)Psi(c)=o(n) would prove NORI1 by Cartesian amplification. This is a strictly sharper and spectral-sensitive target than Phi=o(n); the estimate is OPEN, and no proof of NORI1 is claimed.

VERIFICATION. Complete self-contained manuscript: /mnt/data/nori_xvi_spectral_survival_and_temporal_minimax.md. Independent standard-library verifier /mnt/data/nori_xvi_spectral_survival_verify.py checks the explicit legal Q5 tables, their simple red antipodal word, all eight rounded geodesics and their colors, 250 additional legal conditioned red paths in Q4-Q8, 480 Fourier endpoint identities, full choice-ensemble equality for random nonuniform occurrence laws, and the minimax bound on rational policies for repeated occurrences 3,5,7. All checks passed. This continues Article XVI's unrestricted causal interval programme by sharpening the original rounding mechanism, rather than introducing another restricted coloring class.


## Joint-moment causal forcing and tensorized Gibbs survival

Let P be any red antipodal walk in a legal odd coloring. For each repeated direction j choose its first or last occurrence independently and fairly, deleting every other occurrence; obtain a full antipodal geodesic. Let B be its total number of blue edges, and b_i its direction-i blue indicator. Define K_i=({i} intersect R) union {j in repeated directions excluding i: c_i depends on input bit j, and f_j<t<l_j for some t in {f_i,l_i}}. Every b_i depends only on the independent choices in K_i. Thus b_i,b_k are independent when K_i and K_k are disjoint, and
  mu=EB=sum_i p_i,
  Var(B)=sum_i p_i(1-p_i)+2sum_(i<k)(p_ik-p_i*p_k),
where p_i=E b_i and p_ik=E(b_i b_k). The choice-cube Walsh expansion of B has support only in subsets of the K_i. Its variance is the sum of squared nonconstant Walsh coefficients.

THEOREM (correlation-forced red geodesic). If B takes values in [0,M], with 1<=M<=n, then
 Pr(B=0)>= [EB^2-(M+1)mu+M]/M
          = [Var(B)-(mu-1)(M-mu)]/M.
Proof: the quadratic polynomial (b-1)(b-M)/M equals one at b=0 and is nonpositive for all integers b in [1,M]. Average this pointwise minorization of the zero indicator. In particular a one-walk variance satisfying Var(B)>(mu-1)(M-mu) FORCES a red full antipodal geodesic, including when mu>=1, where the previous first-moment method cannot certify one.

Q4 CERTIFICATE. Define each edge rule c_i(v) by bit v of the 16-bit tables c_0=0x033F, c_1=0xA55A, c_2=0xBB22, c_3=0x2B2B. These satisfy own-direction independence and antipodal oddness. Starting at root 3, W=(2,3,0,3,2,1,2,3) visits 3,7,15,14,6,2,0,4,12=bar3 with all edges red. The two repeated directions 2,3 have four fair first-last choices, with blue counts B=(0,1,3,1). Thus mu=5/4, EB^2=11/4, Var(B)=19/16, and the quadratic theorem guarantees Pr(B=0)>=1/8 (the true value is 1/4), whereas the mean test fails.

SOFT-MINIMUM THEOREM. For beta>0 define Z_beta(P)=E exp(-beta B), F_beta(P)=-(1/beta)log Z_beta(P). Since min B<=F_beta(P)<=EB by elementary bounds and Jensen, the condition F_beta(P)<1 guarantees an all-red rounded geodesic. In the Q4 certificate, beta=log 2 gives Z_beta=17/32>1/2 and F_beta=log_2(32/17)=0.912537159...<1, forcing a red geodesic from the SAME walk of mean 5/4.

TENSOR LAW. For arbitrary interleavings of independent red antipodal factor walks P,Q, the rounded blue counts add as independent random variables. Hence Z_beta(P interleave Q)=Z_beta(P)Z_beta(Q), F_beta(P interleave Q)=F_beta(P)+F_beta(Q), and both the means and variances add. Let E_beta(c)=inf_(P red antipodal walk) F_beta(P) for legal odd c. The red path set is nonempty by Wu-Yang and antipodal color reversal. Projection and concatenation yield E_beta(c box d)=E_beta(c)+E_beta(d), with delta(c)<=E_beta(c)<=Psi(c), where delta is global minority-geodesic defect and Psi is the earlier color-sensitive first-moment energy. Consequently an ALL-colorings upper bound sup_(legal Q_n c)E_beta(c)=o(n) for any fixed beta>0 would prove unrestricted NORI1 by the existing tensor-amplification argument. No such estimate is established.

GIBBS VARIATIONAL IDENTITY. For uniform measure u on first-last choice bits, F_beta(P)=min_nu[E_nu B+(1/beta)KL(nu||u)]. Since each b_i depends only on K_i, Z_beta(P)=2^(-|R|)sum_epsilon product_i exp(-beta b_i(epsilon restricted to K_i)). This packages the shared legal color rules, temporal interval overlap, and all-order joint correlations in a causal factor-graph partition function. The remaining open forcing step is an unrestricted lower bound on some such survival partition function; NORI1 is not solved.

FULL PROOF /mnt/data/nori_xvi_correlated_rounding_gibbs_softmin.md. Standalone independent verification /mnt/data/nori_xvi_softmin_causal_gibbs_verify.py checks legal Q4 tables and red path, all four rounded geodesics, second moments, causal supports, choice-cube Walsh variance, rational Z=17/32, arbitrary-interleaved Q4xQ4 tensor additivity, and 250 further independent legal red antipodal walks in Q4-Q8. All passed.


## Interior-occurrence causal flux cut: a strict strengthening of first-last Gibbs survival

UNRESTRICTED THEOREM. Suppose an arbitrary red antipodal walk P in a two-colored Q_n repeats only one direction j, precisely 2k+1 times. Write its word R j S_1 j S_2 j ... j S_(2k) j T, and let
 K_l=sum_(red i-edge at original start v in S_l) Delta_j c_i(v),
 Delta_j c_i(v)=c_i(v) XOR c_i(v XOR e_j).
Retaining only the r-th occurrence of j makes a full antipodal geodesic with
 B_r=sum_(l<r,l odd)K_l+sum_(l>=r,l even)K_l
blue edges. In particular B_(2t)=B_(2t-1)+K_(2t-1)=B_(2t+1)+K_(2t), so every even occurrence is weakly dominated by both neighboring odd occurrences. The optimal blue count is a one-dimensional minimum cut:
 min_r B_r = min_(0<=t<=k)[sum_(s<=t)K_(2s-1)+sum_(s>t)K_(2s)]
         = sum_(s=1)^k K_(2s)+min_(0<=t<=k)sum_(s<=t)(K_(2s-1)-K_(2s)).
Compute it in O(length P) operations by scanning the signed-flux partial sums. If all selected left odd strips and right even strips have zero flux, the retained interior occurrence gives a red full geodesic.

PROOF. Strip S_l has experienced l original j steps but experiences zero after deletion when l<r and one otherwise. Translation parity therefore changes only on odd l<r and even l>=r. Every original strip edge was red; translation by j changes it to blue precisely when its Boolean derivative is one. This proves the formula and all corollaries without needing antipodal oddness.

SIMPLE UNARY Q6 WITNESS. With vertex bits x_0,...,x_5, prescribe c_0=x_4, c_1=1+x_3, c_2=x_3, c_3=x_4, c_4=x_0, c_5=x_4. All are legal unary odd rules. Root x=16 and word (4,3,5,3,2,3,1,3,0,3) give a simple red antipodal path. The unique repeated direction j=3 appears five times. The four derivative strips, in directions (5,2,1,0), have K=(0,1,1,0). The five possible retained-occurrence geodesics have blue counts (1,1,0,1,1). Retaining the third occurrence gives a fully red geodesic with word (4,5,2,3,1,0), while first-last selection always incurs one blue edge.

PRODUCT-COMPATIBLE HYBRID GIBBS THEOREM. For ANY red antipodal walk, each direction occurs oddly often. Independently for each direction choose one of two distributions: FL chooses its first/last occurrences fairly; ODD chooses uniformly among its odd-ordinal occurrences 1,3,...,2k+1. For policy vector tau and beta>0, put
 Zstar_beta(P)=max_tau E_tau exp(-beta B), Fstar_beta(P)=-(1/beta)log Zstar_beta(P).
Here B is the rounded geodesic's blue count. Always Fstar_beta(P)<=F_FL_beta(P), and Fstar_beta(P)<1 forces a red full geodesic. For the unary Q6 path at beta=log2, FL survival is 1/2 while ODD survival is 2/3, forcing success.

For any interleaving of red antipodal walks P and Q from independent factors c,d, the occurrence-ordinal choices and blue counts project into independent factor contributions. Hence Zstar_beta(P shuffle Q)=Zstar_beta(P)Zstar_beta(Q) and Fstar_beta(P shuffle Q)=Fstar_beta(P)+Fstar_beta(Q). Minimizing over all red antipodal walks yields an intrinsic energy Gstar_beta satisfying Gstar_beta(c box d)=Gstar_beta(c)+Gstar_beta(d), and delta(c)<=Gstar_beta(c)<=the earlier first-last Gibbs energy. A universal upper bound Gstar_beta(c)=o(n) over all legal n-dimensional c would prove NORI1 via tensor amplification. No such estimate has been established.

VERIFICATION. Full proof manuscript /mnt/data/nori_xvi_odd_occurrence_cut_and_hybrid_survival.md; independent verifier /mnt/data/nori_xvi_odd_occurrence_min_cut_verify.py checks the unary certificate, all five geodesics and the K-cut formula, 480 additional compatible legal red paths in Q5-Q8, and odd-occurrence Gibbs tensor factorization in an interleaved Q6xQ6 product. All pass. These are unrestricted implications and a stricter causal rounding technique, not a proof of universal monochromatic geodesic existence.


## Causal optimal-transport coupling of repeated-direction choices

SETUP. Let P be any red antipodal walk of a legal antipodally odd coloring c, and let R be its repeated directions. For j in R let T_j select one of its occurrences. Keeping only these choices produces a full antipodal geodesic, with blue indicators b_i(T) and total B(T)=sum_i b_i(T). For every direction i define potential causal choice-support S_i=({i} intersect R) union {j in R outside i: c_i depends on vertex bit j somewhere}. Each b_i depends only on T restricted to S_i. Let C range over the connected components of the hypergraph on R having the sets S_i as hyperedges. Then B(T)=B_const+sum_C B_C(T_C).

TWO-DIRECTION THEOREM (marginal-preserving optimal transport). Suppose two repeated directions have m occurrences each, and B(r,s) denotes the blue geodesic count when retaining their r-th and s-th occurrences. For q=exp(-beta) in (0,1), the largest Gibbs survival among ALL couplings with both occurrence marginals uniform on [m] is
  max_(permutations sigma) (1/m)sum_(r=1)^m q^(B(r,sigma(r))).
PROOF. Couplings form a scaled doubly stochastic matrix polytope. Its vertices are scaled permutation matrices by Birkhoff-von Neumann; maximizing the linear Gibbs expectation therefore attains a maximum-weight assignment. For unequal or other prescribed marginals one obtains the standard transportation linear program.

FAIR FIRST-LAST CORRELATED FORCING. For two fair binary first-last variables, the only extreme couplings are aligned and crossed. Writing B_ab for the four rounded blue costs (a,b in {0,1}),
 Z_coupled=max{[q^(B_00)+q^(B_11)]/2,[q^(B_01)+q^(B_10)]/2},
 Z_coupled-Z_independent=(1/4)*abs(q^(B_00)+q^(B_11)-q^(B_01)-q^(B_10)).
Thus the improvement is governed by the mixed Gibbs difference across the four outcome choices, which is invisible to independent rounding.

LEGAL Q5 CERTIFICATE. Define c_i(v) as bit v of these 32-bit tables for i=0,...,4:
 (0xCFC33C0C, 0xF50F0F50, 0xDDBB2244, 0x75755151, 0xA0FAA0FA).
The tables ignore their own bit and satisfy c_i(bar v)=1 XOR c_i(v). Starting at x=27, the word P=(3,0,4,3,2,0,3,1,0) is a simple red antipodal walk with visited vertices
 (27,19,18,2,10,14,15,7,5,4).
Directions 3 and 0 occur three times, giving the complete blue-cost matrix
 B=[[2,2,1],[3,1,0],[3,2,0]].
At q=1/2 the four independent policies built from fair first-last or all-occurrence uniform marginals have survival (15/32,19/48,1/2,4/9), none strictly above 1/2. Correlated uniform-all marginal matching has optimum 7/12. Correlating the ORIGINAL fair first-last marginals by choosing their first or their last occurrences together yields the even stronger survival
 Z=(q^2+q^0)/2=5/8>1/2.
Therefore this single red walk has a red full geodesic forced by causal coupling, although the previous independent Gibbs tests at q=1/2 cannot certify it. The winning choice retains last occurrences of both repeated directions and gives the red geodesic word (4,2,3,1,0) from the same root.

PRODUCT-COMPATIBLE CAUSAL-COUPLING THEOREM. For every j in R permit marginal distributions from {fair first-last, uniform odd-ordinal, uniform all-occurrence}. Within each causal component C permit any JOINT law with one of those marginals for each variable; require independence across different components. Let
 Zcorr_beta(P)=max_(such laws) E exp(-beta B), Fcorr_beta(P)=-(1/beta)log Zcorr_beta(P).
This includes the previous independent fair first-last and odd-ordinal policies. In independent Cartesian factor colorings c box d, the causal hypergraph of ANY interleaved red product walk is a disjoint union of the two factor hypergraphs, because neither factor's edge rules reads the other's bits. Factor projections preserve occurrence ordinals and all allowed marginals. Thus the admissible distributions factor into independent component laws and the blue count splits, proving
 Zcorr_beta(P shuffle Q)=Zcorr_beta(P)*Zcorr_beta(Q),
 Fcorr_beta(P shuffle Q)=Fcorr_beta(P)+Fcorr_beta(Q).
Allowing arbitrary coupling ACROSS independent causal components would invalidate this tensor identity, so the causal restriction is logically essential.

Let Hcorr_beta(c)=inf_(red antipodal walks P)Fcorr_beta(P). The Wu-Yang red-antipodal path theorem and antipodal color exchange make this energy finite for legal odd colorings. Projection and concatenation prove Hcorr_beta(c box d)=Hcorr_beta(c)+Hcorr_beta(d). It obeys delta(c)<=Hcorr_beta(c)<=the previous independent first-last/odd Gibbs energy. A universal estimate sup_(legal Q_n colorings c)Hcorr_beta(c)=o(n) for a fixed beta>0 would imply NORI1 by tensor amplification; NO such estimate is claimed or proved here.

VERIFICATION. Standalone /mnt/data/nori_xvi_causal_coupling_matching_verify.py checks all legal Q5 edge rules, red walk edges, 9 rounded geodesics, rational survival values and the causal dependence of both repeated choices. /mnt/data/nori_xvi_correlated_matching_tensor_verify.py additionally checks an arbitrary interleaving of two Q5 copies, giving survival (7/12)^2=49/144 for the matched uniform-all policy, and 375 independent conditioned legal red antipodal walks in Q5-Q7 (all matchings at least the independent uniform survival, with 361 strict gains). The full self-contained manuscript is /mnt/data/nori_xvi_causal_transport_coupling.md. This is a positive all-dimensional correlation mechanism that keeps the tensor closure bridge; unrestricted NORI1 remains OPEN.

## Entropy localization and complete ordered-derivative blocking pairs

THEOREM (two-point coupling bound). For a red antipodal walk P, let B(epsilon) be the number of blue edges after fair first-last rounding, m=min_epsilon B, beta>0, q=exp(-beta), and let Z maximize E q^B over ALL couplings with each first-last choice fair. A minimizing assignment epsilon_star and its bitwise complement form a valid fair-marginal two-point law. Therefore
  m <= -(1/beta)log Z < m+(log 2)/beta
whenever any direction repeats. For q<=1/2, Z>q iff some rounded geodesic is fully red. PROOF: Z<=q^m. The antipodal two-point law yields Z>q^m/2. If m>=1, Z<=q; if m=0, Z>1/2>=q. This shows that liberal coupling already nearly recovers deterministic rounding, rather than supplying an independent existence mechanism.

COMPONENT LOCALIZATION. If the causal repeated-choice hypergraph has h nonempty components and couplings are independent between components, the analogous Gibbs energy F obeys
  m <= F < m + h*(log 2)/beta.
The greatest possible probability of a specified rounding is 2^(-h), attained by complementary assignment pairs independently in each component. The number of causal components, not the number of repeats, controls the Gibbs entropy penalty.

TENSOR WARNING. The previously verified legal Q5 two-repeated-direction red walk has fair first-last blue-cost outcomes (2,3,1,0) and optimal q=1/2 coupling survival 5/8. Two independent copies with causal-component independence yield 25/64. Unrestricted cross-factor coupling instead pairs the global zero-cost assignment with its complement and attains 17/32; an independent transport LP confirms this is optimal. Therefore unconstrained correlation breaks tensor additivity. However additivity of a proposed upper-bound energy is not required for the NORI1 amplification implication: domination of the global geodesic defect and a uniform o(n) bound already suffice.

THEOREM (ordered two-witness obstruction). If only j repeats in a red antipodal walk, 2k+1 times, with outgoing derivative fluxes K_1,...,K_(2k) in the strips between successive j moves, retaining odd occurrence 2t+1 yields
 D_t=sum_(s<=t)K_(2s-1)+sum_(s>t)K_(2s).
All rounded geodesics have a blue edge IF AND ONLY IF there exist s<=t with K_(2s-1)>0 and K_(2t)>0. PROOF: all cuts fail precisely when the earliest active odd strip lies no later than the latest active even strip; otherwise a cut between the two groups has zero flux. Even-numbered retained occurrences cannot improve on adjacent odd ones. Thus the full obstruction to compressing an arbitrarily long one-repeat red walk is witnessed by TWO temporally ordered positive outgoing square derivatives.

MULTIPLE REPEATS. When every rounded edge's blue indicator depends on at most one repeated-direction choice variable, its total blue cost separates into independent one-direction ordered-flux costs. A red full geodesic exists among the rounded words iff no repeated direction possesses the positive odd/even blocking pair just described. The condition is PATH-SPECIFIC, and the optimal rounded geodesic is constructible by scanning its strips.

CHECKS. Detailed mathematical proofs /mnt/data/nori_xvi_entropy_localization_and_ordered_blockers.md. Independent /mnt/data/nori_xvi_entropy_and_ordered_flux_verify.py passed 350 random fair-marginal transportation LPs; all flux assignments from {0,1,2} with up to six strip pairs; the rational Q5 product example; and a legal Q6 red antipodal walk repeating two causally separated directions (root 5, word 0,3,3,2,3,4,5,0,0,1). This new local forcing/obstruction dichotomy is proved, but no unrestricted cross-path incompatibility is yet established. NORI1 remains open.


## Shared-edge transverse-flux transport across two red antipodal paths

THEOREM (transverse square exchange). Fix distinct cube directions i,h,j and vertex v. Let D_j c_i(v)=c_i(v) XOR c_i(v XOR e_j), and define square curvature kappa_(i,h)(v)=D_i c_h(v) XOR D_h c_i(v). Consider a two-edge red path segment i,h across a square with all four edges red, so its exchanged segment h,i is also red. The parity of outgoing j-derivative flux on the two routes is
 K_ih = D_j c_i(v) XOR D_j c_h(v XOR e_i),
 K_hi = D_j c_h(v) XOR D_j c_i(v XOR e_h).
Then
  K_ih XOR K_hi = D_j kappa_(i,h)(v) = kappa_(i,h)(v XOR e_j).
The first equality is valid for ANY edge coloring, even without the red-square condition; the second uses curvature zero on the original all-red square.

PROOF. XOR the four derivatives and factor out D_j. The remaining Boolean expression is c_i(v) XOR c_h(v XOR e_i) XOR c_h(v) XOR c_i(v XOR e_h), which is the square curvature. On the original red square this curvature is zero. The neighboring path segment outside the exchanged square is unchanged, so the identity couples outgoing causal-strip fluxes on TWO DIFFERENT red paths in one legal coloring.

INTEGER IMPROVEMENT. Because all four edges of the original square are red, translating the two alternative routes by e_j makes their outgoing derivative flux COUNTS equal to the numbers of blue edges along the two edge-disjoint routes in the j-shifted square. These counts partition its four edges, hence
 min(flux_ih,flux_hi) <= floor(number_of_blue_edges_in_shifted_square/2).
If the shifted square has at most one blue edge, one available red route has zero outgoing j-flux. This is a constructive local improvement in the derivative-compression programme.

THREE-CUBE INTEGRABILITY. The transverse changes in three perpendicular exchange directions are linked by the cubical identity
 D_j kappa_(i,h) XOR D_i kappa_(h,j) XOR D_h kappa_(j,i)=0,
because each second Boolean derivative in the expression appears twice. Free unrelated flux assignments across red paths need not obey this constraint. This is an instance of d(d c)=0, now connected directly to the ordered flux-pair blockers of the preceding section.

EXPLICIT Q4 CERTIFICATE. Rules c_i(v), encoded by 16-bit tables indexed by vertex v, are (0x3F03,0x0F0F,0x3333,0x7171), all legal odd rules. The square based at v=4 with directions i=0,h=1 is all red. For j=2 the two outgoing path fluxes are 0 and 1; the shifted-square curvature is one, witnessing a nontrivial shared-edge transport.

INDEPENDENT CHECKS. /mnt/data/nori_xvi_transverse_flux_exchange_verify.py checked 100 random legal colorings in each Q3-Q6, over one million ordered triple/base-vertex Bianchi identities, the transverse-flux formula on every all-red square, and the integer blue-count partition. All tests passed. Manuscript /mnt/data/nori_xvi_entropy_localization_and_ordered_blockers.md, Section 6. These theorems prove an all-dimensional CROSS-PATH compatibility identity, not a contradiction ruling out every possible globally consistent blocking assignment. NORI1 remains OPEN.
