# Alternating geodesic index vanishes despite red success in arbitrarily high dimensions

- Stable ID: note_nori_signed_geodesic_index_tensor_cancellation_r11984
- Author: unspecified; session provenance retained
- Primary home: subsection:gauge_critical_switches_and_clustered_witnesses_on_full_paths
- Labels: 
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11984_1
- Updated session: session_nori_r11984_1
- Disposition: none
- Successor: none

## Related references

- None

## Research note

Define Sigma_c(x) to be the signed sum over red full antipodal geodesics rooted at x, sign determined by the permutation of original direction labels.

TENSOR THEOREM. For independent legal paired-flat colorings c on Q_(2m) and h on Q_(2k), Sigma_(c box h)(x,y)=binom(m+k,m) Sigma_c(x)Sigma_h(y).
Proof: Every red full path in the product is a shuffle of red full paths in its factors. The sign of its original-direction permutation is the product of the two factor signs and the shuffle sign. Pair adjacent shuffle slots (1,2),(3,4), etc. Swapping the first mixed pair cancels signed shuffles having any mixed pair. The remaining shuffles have homogeneous pairs and are counted by binom(m+k,m), each with positive sign.

Q6 SEED. Let direction pairs be (0,1),(2,3),(4,5), and let f0(x)=f1(x)=x4 while f2 is any odd Boolean gate independent of bits 4,5. Then Sigma_c(x)=0 for EVERY root x.
Proof: Each of the pair0 and pair1 occurrences must straddle the one traversal of original direction4, since both selectors read x4 and the two red directions within a pair must differ. Each side of direction4 consequently contains one pair0 move and one pair1 move. The only remaining move, original direction5, can separate them on at most one side. Choose the side before direction4 when its 0,1 moves are adjacent; otherwise choose the side after direction4. Swapping those two adjacent moves preserves every red step because f0 and f1 both depend only on x4 and their steps change distinct bits. It reverses the permutation sign and keeps the selected side invariant. This is a fixed-point-free involution on successful rooted red full paths.

Take f2=x0. Root 1 with direction word (2,5,0,4,1,3) is a red full geodesic. Independent direct enumeration finds 192 rooted red full geodesics, but zero signed sum at all 64 roots.

PRODUCT OBSTRUCTION. Tensor this Q6 seed with arbitrarily many successful paired-flat Q4 blocks. The result is red-successful in arbitrarily large even dimensions, while Sigma vanishes at every root by the tensor theorem. Independent signed subset dynamic programming confirms the Q6 and Q10 cases, the latter at all 1024 roots.

This closes the proposed universal nonvanishing of antisymmetrized red full-geodesic counts as a forcing principle. It does not solve NORI1 or weaken the unsigned two-geodesic orbit-support criterion.

STRONG NONCOMMUTING CHECK. A distinct Q6 paired-flat instance with eight-bit odd exterior-gate masks (0xca,0xf0,0x3f) has 224 rooted red full geodesics across 40 successful roots, but Sigma_c(x)=0 for all 64 roots. Its q-dependency digraph is strongly connected: the nontrivial source-to-target arcs are 0->2, 1->0, 1->2, and 2->1. None of the three red pair matchings commute globally with another. Independent full enumeration of 64 roots and 720 original-direction orders yields the zero signed sums and a red witness with root 10, direction word (0,2,1,4,3,5). Thus rootwise vanishing of the alternating index is not confined to models with commuting pair matchings or weak q-dependency. This finite strengthening does not prove a dimension-uniform theorem for strongly connected dependency, but the earlier product construction already proves arbitrarily high dimension vanishing without that restriction.
