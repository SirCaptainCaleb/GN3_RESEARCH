# Use longest-path displacement profiles as a nonlocal secondary defect potential

## Statement

Proposal: replace local failed-insertion sign words in the well-founded defect-window route by displacement profiles measured against a globally longest path. Among deletion-cover states that preserve the longest-path order and tie on the primary deletion-side normalization, compare the displacement sequences i-p_i of surviving longest-path vertices in the relevant path component. By the positional-lag bound, and on consecutive surviving runs by monotonicity, these profiles lie in a finite bounded ordered set; any failure of order preservation already exposes an order-disagreement witness.

## Body

The existing defect-window assessment shows that its primary distance is only the minimum deletion-side parameter and that local failed-insertion signs can alternate arbitrarily. The certified positional-lag theorem 8f2c6a91d4e7 gives a genuinely nonlocal replacement: in an order-preserving path C of order lambda-d, every surviving longest-path vertex a_i occurs at p_i in [i-d,i]. The sibling insertion-slot development further gives monotonicity of i-p_i on consecutive surviving runs. Proposed route: use the resulting bounded displacement word as a secondary lexicographic potential, and analyze deletion/replacement moves that preserve the primary side size. The exact missing obligation is to prove that every bounded obstruction at a displacement-minimal state either yields a two-cover/order-disagreement consumer or admits a legal move that strictly improves this profile. This avoids relying on unconstrained local sign regularity.
