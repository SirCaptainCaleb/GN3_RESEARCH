# Balanced three-nonlinear two-internal-reader closure through a paired residual reader

- Stable ID: note_95362730bed6abbdc8b02eac
- Author: unspecified; session provenance retained
- Primary home: subsection:paired_direction_involutions_and_geodesic_endpoint_matchings
- Labels: NORI1, three-nonlinear, balanced, closure, paired-reader, eight-pivot
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r10003_3
- Updated session: session_nori_r10003_3
- Disposition: none
- Successor: none

## Related references

- None

## Research note

THEOREM. Let c be a vertex-balanced antipodally odd cube edge coloring with precisely three exceptional nonunary directions a,b,c and every other direction unary. Suppose the signed exceptional sum is s_a+s_b+s_c=X_a+X_b+X_p, with X_j=epsilon_j*(-1)^x_j, p outside {a,b,c}. Cancel opposite unary rules sharing a reader. Let the three unmatched unary directions u_a,u_b,u_p have signed rules -X_a,-X_b,-X_p. Assume p belongs to a remaining complementary unary pair {p,p'} whose common reader is a or b. Then the coloring admits a zero full antipodal geodesic in every dimension, regardless of its nonlinear exceptional rules and all remaining unary reader cycles.

PROOF. Normalize bit signs so X_a,X_b,X_p act as independent signed bit characters. The pair p,p' has rules s_p=delta*X_r and s_p'=-delta*X_r, with r=a or b and delta=+1 or -1. Take the eight-direction core T={a,b,c,u_a,u_b,u_p,p,p'}. Fix arbitrary exterior bits. Balance gives s_a+s_b+s_c=X_a+X_b+X_p at every core vertex. If X_a=X_b=X_p=+1, all three exceptional signed rules are +1. Since s_a ignores its own bit a, its sign is therefore + whenever X_b=X_p=+; similarly s_b is + whenever X_a=X_p=+. The c edge is + whenever all three characters are +. These are selector-independent forcing rules.

By symmetry suppose r=a. If delta=+1, choose initial (X_a,X_b,X_p)=(-1,+1,+1) and traverse directions (u_a,p',a,c,b,u_b,p,u_p). The first two steps are red because s_(u_a)=-X_a and s_p'=-X_a. Direction a is red because X_b=X_p=+; afterward X_a=+. Then c is red since all three X signs are +. Direction b is red because X_a=X_p=+; afterward X_b=-. Direction u_b is red because s_(u_b)=-X_b. Direction p is red because s_p=X_a=+; afterward X_p=-. Finally u_p is red because s_(u_p)=-X_p.

If delta=-1, choose initial (X_a,X_b,X_p)=(+1,-1,+1) and traverse (u_b,b,c,p',a,u_a,p,u_p). Direction u_b is red because X_b=-. Direction b is red since X_a=X_p=+, making X_b=+. Direction c is now red at the all-positive sign state. Direction p' has signed value X_a=+. Direction a is red since X_b=X_p=+, leaving X_a=-. Direction u_a is then red. Direction p has signed value -X_a=+, leaving X_p=-, after which u_p is red. For r=b swap a and b and their unmatched partners in these constructions. All eight directions occur once; neither construction uses any information about the exceptional selector or the frozen exterior bits. Hence every frozen core T has a zero full antipodal geodesic. Apply the established uniform frozen-core absorption theorem to the remaining unary directions, including cyclic components. QED.

An independent exhaustive subset-reachability check on the eight-bit core confirms a selector-robust path for each of the four (reader r, sign delta) cases. This closes another dimension-uniform three-nonunary subbranch beyond the earlier result where p equals one of the unmatched unary directions u_a,u_b.
