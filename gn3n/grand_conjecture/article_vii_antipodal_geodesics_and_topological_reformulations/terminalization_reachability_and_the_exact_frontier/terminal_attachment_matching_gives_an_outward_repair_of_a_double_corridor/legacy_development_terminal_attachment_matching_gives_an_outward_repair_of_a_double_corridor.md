# Terminal attachment matching gives an outward repair of a double corridor — preserved pre-item development

## Composition

(none yet)

## Development

Let a protected positive span-two double have reflected starts a<b and full determining span J=[a,b+4]. Decompose its corridor into tight paths P=(p_1,...,p_s) and Q=(q_1,...,q_t), each of order at least two, and let x=v_a,y=v_{b+4} be the two exterior vertices, as in [[complete_positive_span_two_double_corridor_classification]].

Form a bipartite graph with left vertices P,Q and right vertices x,y. Put an edge Te precisely when h(t_{last-1},t_last,e)=1. If this graph has a perfect matching, append the matched exterior vertex to each corridor path. The two resulting paths partition J, so their order (P,e_P,e_Q,Q^{rev}) is a two-cover order on J. This permits a global reorder of J: the exterior vertices move from the old ends to the new cut. It does not preserve the old tail pairs.

The internal status word of this repaired order is 1^{s-1} A B 0^{t-1}, where A,B are the two unrestricted junction statuses. Each of the four choices of A,B avoids 001,011,0101. Alternatively this follows directly from the two tight paths. Every positive determining window at depth at most the selected reflected span-two edge lies in J: span-two starts in [a,b], and alternating starts at such depths have their six-vertex windows within [a,b+4]. Thus replacing J by this two-cover order produces an outward chamber; any newly changed window crossing a boundary of J belongs to a farther-out edge.

This is a sufficient repair criterion, not an assertion that a perfect matching always exists. Explicitly it holds if either
h(p_{s-1},p_s,x)=h(q_{t-1},q_t,y)=1
or
h(p_{s-1},p_s,y)=h(q_{t-1},q_t,x)=1.
Failure leaves the elementary Hall alternatives: one path has no terminal attachment to either exterior vertex, or both paths have attachments only to the same exterior vertex. The reversed initial hooks impose no immediate constraint on these terminal triples.

The obstruction in [[protected_mixed_doubles_can_forbid_simultaneous_preservation_of_both_tail_pairs]] is repaired by this criterion: its construction has h(u,v,e)=1 for all distinct u,v in the corridor and e in {x,y}, so its terminal attachment graph is complete. In fact (P,x) and (Q,y) are an explicit spanning two-cover of that construction. The counterexample therefore defeats simultaneous preservation of both old tail pairs, while exhibiting exactly why moving the exterior vertices to the terminal ends succeeds.

For protected face carriers, this repair can be frozen on the whole interval J and combined with an inherited mask of exterior components disjoint from J, as in [[frozen_window_carriers_and_separator_relabeling_require_precise_invariants]]. The resulting product face is protected and contractible on a fixed ambient source face. Since J may be unbounded, this does not restore a bounded-rank interaction claim. Nor does it supply compatible choices of matching, cut, or repaired order across distinct ambient zero faces. Those obligations remain open.
