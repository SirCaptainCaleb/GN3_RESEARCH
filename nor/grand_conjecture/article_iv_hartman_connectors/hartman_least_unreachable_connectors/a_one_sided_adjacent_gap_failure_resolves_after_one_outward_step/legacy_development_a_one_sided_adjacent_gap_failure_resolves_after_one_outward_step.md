# A one-sided adjacent-gap failure resolves after one outward step — preserved pre-item development

Work in path-normalized square-path gauge with consecutive connector vertices
H,P,L,M,R,S.
Let a be insertable at L|M and b at M|R, and assume the bad mutual orientation b->a.

The insertion collar for b says
L->b, M->b, b->R, b->S.
Encode the incidence word of b by r_T=1 when T->b. Thus on L,M,R,S the word is 1100.

Suppose the two-for-one exchange fails only on the left, so P->b fails; equivalently r_P=0, while the right outer condition a->S holds.

Section 25 shows that a genuine unresolved adjacent-gap obstruction has no legal insertion gap for b anywhere strictly to the left of its original gap.

Now inspect the preceding vertex H. If H->b also failed, then r_H=0, and the four consecutive incidence bits on H,P,L,M would be
0011.
By the exact insertion criterion, this would make b directly insertable at the earlier gap P|L, contradicting the one-sided blocker-tail theorem.

Therefore H->b is forced.

But the one-sided exchange calculation of §14 then becomes an actual legal square-path exchange:
delete P and M and insert b,a, replacing
H,P,L,M,R,S
by
H,L,b,a,R,S.
All consecutive and distance-two edges are certified; H->b is the only formerly unchecked left distance-two edge and a->S is the assumed right edge.

Hence a left-only failure cannot propagate beyond one connector step. It always has a legal support-preserving exchange. The symmetric statement holds for a right-only failure.

Consequently the conditional multi-step outward transport of §14 is unnecessary in the genuinely unresolved adjacent-gap setting: after excluding alternative insertion gaps as in §25, every one-sided outer failure resolves by one legal exchange. The only remaining rank-two obstruction is the case in which both outer incidences fail simultaneously.

Unification audit: the blocker-tail argument correctly forces H→b, and the replacement H,L,b,a,R,S is internally a square-path under the stated right-edge condition. Its first pair changes from H,P to H,L. If G precedes H, the additional external distance-two edge G→L is required in the same path-normalized gauge. The source argument does not certify it. At a released left endpoint no such exterior edge exists, while fixed-representative endpoint compatibility remains a separate target. The support cardinality is preserved by deleting P,M and inserting b,a; this exchanges two holes and does not realize the support union of the two original absorptions. Retain the internal step and its extra collar obligation instead of unconditional global resolution.

Additional gauge audit: the inference H→b from forbidding the earlier 0011 insertion uses the neighboring-gap implication in §25. That implication requires the new internal a,b orientation, which flips when b's insertion gauge changes from 1100 to 0011. Thus H→b is an independent condition for the proposed exchange, not a forced edge from the stated hypotheses. With H→b, a→S, and the outside collar G→L when present, the square-path replacement is valid internally and externally. The two-hole support exchange remains distinct from a support-union filler.
