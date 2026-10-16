# Every weak-majority edge extends to a monochromatic antipodal geodesic

- Stable ID: note_nori_weak_majority_edge_extension_20261015
- Author: unspecified; session provenance retained
- Primary home: subsection:gauge_critical_switches_and_clustered_witnesses_on_full_paths
- Labels: extremal, geodesic-extension, proof
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r9623_1
- Updated session: session_nori_r9623_1
- Disposition: none
- Successor: none

## Related references

- None

## Research note

**Theorem (every weak-majority edge extends).** Let n>=3 and a_i>=0 not all zero. Put Phi(x)=sum_i a_i(-1)^(x_i), and give a direction-i edge e the color zero when its midpoint potential H(e)=(Phi(u)+Phi(v))/2 is positive, color one when H(e) is negative, and any antipodally odd tie color when H(e)=0. Then every zero edge lies on a monochromatic-zero full antipodal geodesic; likewise every one edge lies on a monochromatic-one full antipodal geodesic.

*Proof.* Start from a zero edge e of direction i, whose midpoint potential is nonnegative, and regard it as a path with used dimensions S={i}. Its endpoints u,v agree on all unused bits. Define H_S=(Phi(u)+Phi(v))/2=sum_(j notin S)a_j epsilon_j, where epsilon_j is their common bit sign. For any unused j, adding its edge at u or v gives midpoint potentials Phi(u)-a_j epsilon_j and Phi(v)-a_j epsilon_j, whose maximum is at least H_S-a_j epsilon_j. After the extension the new endpoint-average potential is H_S-a_j epsilon_j.

Choose a reserved unused dimension for the last extension: one with positive a_j epsilon_j if possible, otherwise one of weight zero if possible, otherwise any. Extend all other unused dimensions in this order: negative a_j epsilon_j, zero a_j, then positive a_j epsilon_j. During negative steps H_S>=0 and the maximal candidate midpoint exceeds H_S; removing negative signed weights makes H_S increase. During zero steps the maximal candidate midpoint is at least H_S, which is positive unless all unprocessed signed weights are zero. In the latter case H_S=0 implies all weights other than a_i were zero from the start; as the weights are not all zero, a_i>0 and the two endpoint potentials are +a_i and -a_i, so one zero-step candidate still has positive midpoint. During positive steps before the reserved final direction, H_S is the sum of remaining positive weights, including at least one other positive weight, and the best midpoint is strictly positive. Thus all nonfinal edges can be chosen color zero. When only one direction j remains, the two candidate j-edges at the path endpoints are antipodal mates, and one is color zero. Adding it yields a zero full geodesic through e. Antipodal complementation proves the color-one statement. QED.

**Corollary (single-direction tolerance).** Flipping any fewer than 2^(n-2) antipodal edge pairs contained in one direction preserves a monochromatic full antipodal geodesic: choose one of the 2^(n-2) unflipped zero edges in that direction, extend it as above, and note that the resulting path uses that direction only once.

**Corollary (unrestricted necessary frustration).** In any hypothetical bad odd coloring c with nonzero signed facet-imbalance vector B, let h_p=s_p sum_(j ne dir p)B_j(-1)^(x_j) be the alignment of each antipodal edge-pair sign with its B-weighted field, and put F={p:h_p<0}. Then F meets at least two directions, or |F|>=2^(n-2). In particular |F|>=2. Proof: reverse all strictly misaligned pairs to obtain an antipodally odd weak weighted-majority coloring with weights |B_j| and the same tie colors. If the reversal set lay within one direction with size less than 2^(n-2), the tolerance corollary would make the original c good, contradiction. The previously proved positive-spanning lemma guarantees F nonempty whenever c is bad and B!=0. QED.

The edge-extension property covers all edges of both colors, not merely one constructed full geodesic. The final corollary imposes an unrestricted necessary condition on every counterexample with B!=0; no restricted coloring hypothesis is imposed on c.
