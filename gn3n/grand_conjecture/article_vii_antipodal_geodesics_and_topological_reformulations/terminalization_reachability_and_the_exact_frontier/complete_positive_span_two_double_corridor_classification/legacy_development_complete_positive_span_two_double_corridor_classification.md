# Complete positive span-two double corridor classification — preserved pre-item development

## Development

Work only with positive witness words W+={001,011,0101}. Let a<b be reflected starts of two positive span-two occurrences in one protected chamber, with d=b-a>=5 so their five-vertex determining windows are disjoint. Put x=v_a, y=v_{b+4}, and C=(v_{a+1},...,v_{b+3}). The internal status word t of C is epsilon_{a+1}...epsilon_{b+1}, of length M=d+1. Every positive forbidden occurrence wholly inside this interval is strictly inward of the selected span-two edge: span-two starts lie from a+1 through b-1, and alternating starts from a+1 through b-2. Therefore t avoids W+.

For completeness, a W+-free binary word has the form 1^u0^v or 1^u010^v, with nonnegative exponents, allowing the empty endpoint portions. One proof uses p=first zero and q=last one: absence of W+ is equivalent to q<=p+1. If q<p the word is monotone; if q=p+1 the only rising pair is the adjacent 01 between a prefix of ones and a suffix of zeros. This uses no negative forbidden word.

There are four endpoint cases, and protection gives their complete status classification:
(i) left 001, right 001: t=01 0^{d-1}.
(ii) left 011, right 011: t=1^{d-1}01.
(iii) left 001, right 011: impossible for d>=5.
(iv) left 011, right 001: t=1^u0^v with u,v>=2 and u+v=M, or t=1^u010^v with u,v>=2 and u+v+2=M.

Indeed the left occurrence supplies the first pair 01 or 11 of t, and the right supplies its last pair 00 or 01. In case (i), its first zero is at 1 and its first one at 2; q<=p+1 forces all later statuses to be zero. Case (ii) is the reverse-complement case. Case (iii) would have p=1 and q=M>2. The first and last pairs in case (iv) give exactly the displayed exponent restrictions.

Choose a cut j of C with q<=j<=p+1, and let P be its first j vertices in displayed order, Q its remaining vertices in reverse displayed order. Then P,Q are tight paths. In all four cases which can occur, the cut can be chosen with 2<=j<=M, so both paths have at least two vertices. For (i), j=2 is forced; for (ii), j=M is forced; in (iv), the endpoint pairs imply p>=3 and q<=M-2, so a cut in [2,M] exists.

Write P=(p_1,p_2,...), Q=(q_1,q_2,...). Irrespective of which positive words occur,
h(p_2,p_1,x)=1 and h(q_2,q_1,y)=1.
The first identity is the boundary reversal of epsilon_a=0; the second is epsilon_{b+2}=1, since q_2=v_{b+2},q_1=v_{b+3}. Thus the exact two-exterior-vertex formulation in [[span_two_doubles_are_exactly_a_two_cover_corridor_plus_two_reversed_endpoints]] holds without its unnecessary choice of left 011/right 001. Reversal exchanges (i) and (ii), while each mixed case is preserved; reversal alone cannot turn a same-word pair into case (iv).

There is a further immediate simplification. In case (i), P has exactly two vertices, so replace it by the tight three-vertex path (p_2,p_1,x). This absorbs x without changing Q. The full determining span is now partitioned into this tight three-path, the long tight path Q, and the remaining vertex y, with h(q_2,q_1,y)=1. Case (ii) symmetrically absorbs y into (q_2,q_1,y), leaving P and x. These are genuine three-path covers of the span, not two-path covers: absorption of the remaining endpoint or a compatible repartition is still needed.

In case (iv), both P and Q have order at least three. It is the only disjoint double type which retains two substantial tails and both reversed endpoint attachments. Consequently the remaining local repair separates into (a) the tight three-path plus one long path plus one reversed endpoint, and (b) two long tight paths plus two reversed endpoints. Neither follows merely from the unrooted finite two-cover theorem. Any eventual protected surgery must also check all boundary-crossing positive windows and global compatibility of its carriers.
