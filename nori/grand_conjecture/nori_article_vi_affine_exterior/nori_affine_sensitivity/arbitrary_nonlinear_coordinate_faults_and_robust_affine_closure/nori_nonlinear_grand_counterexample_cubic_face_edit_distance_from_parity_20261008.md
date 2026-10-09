# Any NORI counterexample is cubic Hamming distance from every full-parity face coloring

# Deterministic Hamming-distance barrier: a NORI counterexample must differ from EVERY full-parity reference on Ω(n³) ordered physical faces

Let n>=5 and let c0 be ANY active antipodal-reversal-odd ordered-three-face coloring of the full-parity exterior form
  c0(F,(i,j,k))=h(i,j,k)+Σ_(t notin{i,j,k}) z_t  (mod2),
where h is arbitrary subject to the reversal compatibility equation h(k,j,i)+h(i,j,k)=1+(n−3 mod2). Such h exist by independent assignment on each ordered-triple reversal pair. Every full direction permutation has exactly 8(n−2) good (at most one switch) starting roots under c0, by the three-residue-chain theorem.

Let c be ANY other valid active NORI coloring, with arbitrary NONLINEAR face-bit behavior. Let E be the set of actual PHYSICAL ORDERED THREE-FACE OBJECTS (F,pi3) on which c and c0 disagree. The NORI axiom implies E is a union of full two-element antipodal-reversal involution orbits.

**Theorem (global edit-distance necessary condition).** If c has NO antipodal full geodesic with at most one ordered-three-face color change, then
  |E| >= n(n−1)(n−2).
Equivalently, c differs from c0 on at least
  n(n−1)(n−2)/2
INDEPENDENT ANTIPODAL-REVERSAL FACE-COLOR ORBITS.

**Proof: double-counting good reference paths.** Reference c0 has exactly B=8(n−2)n! distinct DIRECTED full antipodal good paths (root plus permutation). Every one of these B paths must query at least one c/c0-disagreeing face object; otherwise its entire color word in c is unchanged and remains good.

For a FIXED ordered physical 3-face object (F,(i,j,k)), count how many full directed antipodal geodesics include it as a consecutive 3-edge window. The permutation must have the ordered directions (i,j,k) as one consecutive block; there are (n−2)! such full permutations. In each such permutation, all n−3 exterior root bits are uniquely determined by demanding the physical window face equal F; its 3 free root bits are arbitrary, giving exactly 2³=8 full rooted geodesics. Thus the object occurs on precisely 8(n−2)! full directed antipodal geodesics, and on at most that many of the B reference GOOD paths.

Hence B <= |E|·8(n−2)!, giving
  |E| >= 8(n−2)n!/[8(n−2)!] = n(n−1)(n−2).
Because E is stable under the free antipodal-reversal orbit involution, the count in independent orbit variables is half. QED.

**Interpretation.** The full-parity solution is not a fragile isolated model: any hypothetical NORI counterexample lies at least CUBIC distance from EVERY valid full-parity reference in the natural Hamming metric on actual ordered-face coloring objects. This provides a global error/repair budget across every root and coordinate permutation, not merely a bound along one preselected path. The bound is necessary, not sufficient: the total number of ordered physical 3-face objects is n(n−1)(n−2)·2^(n−3), and this lower bound by itself does not exclude a counterexample.

**Complementary positional blocker bound.** Define the set E_type of ordered triples for which c and c0 disagree on AT LEAST ONE exterior-face assignment. The robust one-arbitrary-window theorem says that in any counterexample EVERY full direction permutation must have at least TWO successive ordered triple types from E_type among its n−2 windows. A uniformly random permutation contains a fixed prescribed ORDERED triple consecutively with probability 1/[n(n−1)]. Averaging its >=2 bad windows over all permutations gives the necessary condition
  |E_type| >=2n(n−1).
This O(n²) type-level bound is logically different from the Ω(n³) physical-face edit bound above; neither implies the other directly.

Both conclusions require no affine hypothesis on c itself, only comparison against an affine full-parity reference c0 whose witness count is already proved.
