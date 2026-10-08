# Facet antipodal duality preserves one change and endpoint mismatch

# Exact antipodal pairing of facet one-change geodesics

Let c be an antipodal-reversal-odd ordered-three-face coloring of Q_(n+1), and let H_0,H_1 be opposite n-facets normal to direction g. If a full n-edge geodesic P inside H_0 has direction order p=(p_1,...,p_n) and ordered-three-face color word w=(w_1,...,w_(n-2)), its antipodal reversal J(P) in H_1 has direction order rev(p) and color word
J(w)=(1-w_(n-2),...,1-w_1).
This is immediate from the defining NORI oddness involution, applied to each ordered face.

In particular, if w=0^r 1^s has one change then J(w)=0^s 1^r still has one change (the change orientation remains 0-to-1); likewise if w=1^r 0^s, the dual is 1^s 0^r. Hence antipodal face symmetry by itself preserves the number of changes; it does NOT turn a one-change facet geodesic into a monochromatic geodesic in the opposite facet.

EXACT ENDPOINT EXTENSION CRITERION. Suppose P has exactly one change and appending the as-yet-unused direction g produces a full (n+1)-edge geodesic P*g. Let beta be the color of its one new ordered-three-face window (p_(n-1),p_n,g), taken at the actual face. Then P*g is one-change if and only if beta=w_(n-2), the terminal old-window color. Otherwise it has exactly two changes. The antipodal reversal J(P*g), which begins with g and follows J(P), has exactly the same number of changes: its word is the reversed complement of (w,beta). Therefore passing to the antipodal partner duplicates this endpoint match/mismatch without resolving it.

This identifies a concrete induction invariant: seek one-change facet geodesics with *terminal extension compatibility* for at least one omitted direction g, or prove a witness-exchange operation forcing compatibility among candidate paths. Pairing a single path with its antipodal dual is insufficient. Any stronger argument must compare genuinely different facet geodesics, change their endpoints, or exploit additional face overlaps.

The result is elementary, requires no information about colorings outside the chosen path and its dual, and applies to any n>=4 for which two or more face windows occur.
