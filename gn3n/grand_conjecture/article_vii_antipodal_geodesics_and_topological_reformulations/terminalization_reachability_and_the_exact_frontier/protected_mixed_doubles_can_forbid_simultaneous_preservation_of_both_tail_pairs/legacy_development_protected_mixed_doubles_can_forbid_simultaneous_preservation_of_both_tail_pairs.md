# Protected mixed doubles can forbid simultaneous preservation of both tail pairs — preserved pre-item development

The two-tail interface target must permit more than independent prefix absorption.

Construction. Take disjoint sets U=P union Q and E={x,y}, with displayed paths P=(p_1,...,p_s), Q=(q_1,...,q_t), s,t>=4. Prescribe their displayed internal triples tight. For every e in E and every ordered pair of distinct u,v in U, set h(u,v,e)=1, and hence h(e,v,u)=0. Equivalently every triple with an exterior vertex first and two corridor vertices next is non-tight. These prescriptions are consistent: all their boundary reversals have an exterior vertex first, and the original prescriptions have one last. The middle-exterior pairs can be completed arbitrarily.

For three-sets entirely in U, retain the path prescriptions and choose the two junction statuses in the order C=(P,Q^{rev}) to be zero. These junction triples meet both P and Q, so neither is a prescribed internal path triple or its boundary reversal. Complete all remaining reversal pairs arbitrarily.

The spanning order omega=(x,P,Q^{rev},y) has status word
0 1^{s-2} 0^t 1.
Its only positive forbidden occurrences are 011 at start 1 and 001 at start m-2, where m=s+t. They are reflected since 1+(m-2)=m-1. Every strictly inward positive witness is absent. This is precisely the protected mixed reflected-double configuration with two substantial tight paths, including all their actual first tight triples. It has the required reversed endpoint relations
h(p_2,p_1,x)=h(q_2,q_1,y)=1.
Its determining span has order s+t+2, which is unbounded.

Nevertheless no tight path ending in two vertices of U can contain x or y. To prove this, suppose such a path contains a vertex of E, and choose the last occurrence e of a vertex of E. Because the terminal two vertices lie in U, at least two U vertices follow e. Its next triple therefore has the form (e,u,v), and is non-tight by construction, a contradiction.

Consequently there is no spanning two-path cover in which both paths end in ordered pairs drawn entirely from U. This excludes, in particular, simultaneous preservation of the original terminal pairs of P and Q. It also excludes a bounded-prefix replacement which produces two fragments ending in the prescribed pairs for reattachment to two nonempty untouched tails: after the tails are attached, both complete paths end in U, so neither can contain either exterior vertex.

The obstruction is stronger than failure to preserve one particular ordered pair: no choices of two terminal pairs wholly inside the old corridor can work. It is still a local counterexample to an attachment requirement, not to the unrestricted two-cover conjecture. A possible repair may concatenate or repartition the two tails into one final path, let another path end at an exterior vertex, move or reorder part of a tail, or use additional hypotheses unavailable from the protected status word alone.

Thus [[span_two_doubles_are_exactly_a_two_cover_corridor_plus_two_reversed_endpoints]] gives a correct corridor decomposition (with all endpoint cases supplied by [[complete_positive_span_two_double_corridor_classification]]), but its suggested universal two-fragment repair preserving both ordered tail attachments cannot be the next theorem. The bounded-prefix target must explicitly permit a change in how the tails are assigned to the final paths. The protected outward-carrier and global compatibility checks then remain separate obligations.
