# Root slides transport central weight profiles through one-seam corridors

ROOT-SLIDE TRANSPORT OF THE EXTERIOR-HAMMING-WEIGHT PROFILE.

Fix n>=4 and a full antipodal geodesic P starting at x with coordinate order p=(p1,...,pn). Let x_i denote the initial bit at direction p_i, and K_i the number of exterior 1-bits at the i-th ordered-three-face window. Let P+ be the forward root slide: start at x+e_(p1) and use direction order (p2,...,pn,p1). Denote its window exterior weights by K'_i.

THEOREM (exact transport). We have
 (K'_1,...,K'_(n-2)) = (K_2,...,K_(n-2), K_(n-2)+x_1-x_(n-2)).
In particular a root slide preserves the physical ordered faces and colors of all n-3 overlapping windows, and its one new ordered face has exterior Hamming weight shifted from the old last window by an amount in {-1,0,1}.

PROOF. The vertex sequence for P+ is obtained by dropping the first vertex of P and adding the antipode of its new first vertex to the end. Thus its first n-3 ordered-three-face windows are literally the second through last windows of P, proving the first n-3 equalities. The old last face has free directions (p_(n-2),p_(n-1),p_n), with exterior bits 1-x_1,...,1-x_(n-3), giving weight K_(n-2)=sum_(i=1)^(n-3)(1-x_i). The new last face has free directions (p_(n-1),p_n,p1), with exterior bits 1-x_2,...,1-x_(n-2), giving weight K'_(n-2)=sum_(i=2)^(n-2)(1-x_i). Subtract to obtain x1-x_(n-2). QED.

COROLLARY (one-jump corridors are forced at n divisible by 6). Suppose n is divisible by 6 and P is a constant-exterior-layer geodesic with K_i=k=(n-4)/2 for every i. The constant-weight recurrence x_(i+3)=1-x_i has n-3 an ODD multiple of 3, so x_(n-2)=1-x_1. Therefore its forward root slide has weight profile
 (k,...,k,k+2x_1-1).
It always leaves the constant-weight chamber class through an EXACTLY ONE-SEAM boundary jump. When x1=1 the new last layer is k+1, the upper central layer; when x1=0 it is k-1. Hence the central single-jump configurations are geometrically natural root-slide corridors between rooted Freudenthal chambers. They need not all stay in the two central layers.

TOPOLOGICAL ROLE. The all-root Freudenthal/pseudomanifold chamber graph admits endpoint root slides as genuine ridge adjacencies. The displayed weight-transport law gives an exact discrete boundary coordinate for such a ridge move. Any proposed Hartman least-unreachable-face argument using central Hamming-layer paths must allow single-seam weight defects: in dimensions n divisible by 6, the constant central layer alone has no root-slide edges. This result applies independent of coloring and is fully compatible with arbitrary face dependence. It does not itself force a low-switch colored geodesic.
