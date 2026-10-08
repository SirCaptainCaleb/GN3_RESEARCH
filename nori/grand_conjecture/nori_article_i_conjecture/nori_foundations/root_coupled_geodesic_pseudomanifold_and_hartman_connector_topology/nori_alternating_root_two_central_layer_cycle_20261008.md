# Alternating roots yield a two-central-layer closed root-slide cycle

UNIVERSAL TWO-CENTRAL-LAYER ROOT-SLIDE CYCLE.

Let n>=4 be even, k=(n-4)/2, and p=(p1,...,pn) any coordinate order. Take the starting root whose p-ordered bits are x_i=0 for odd i and x_i=1 for even i. Traverse directions p1,...,pn twice, obtaining a closed cubical walk of length 2n. It consists exactly of the successive forward root slides of the n-edge antipodal geodesic (x,p), returning to the initial rooted order after 2n slides. For t=1,...,2n, let K_t be the number of fixed exterior one-bits of the ordered three-face window beginning at step t along this closed walk, interpreted cyclically.

THEOREM (explicit central-layer cycle). Every K_t belongs to {k,k+1}. More precisely, writing U=k+1 and L=k, the full cyclic weight word is
 K_1,...,K_(n-2) = U,...,U (n-2 copies);
 K_(n-1)=L, K_n=U;
 K_(n+1),...,K_(2n-2) = L,...,L (n-2 copies);
 K_(2n-1)=U, K_(2n)=L.
In particular K_(t+n)=2k+1-K_t for every t, so opposite points on the root-slide cycle lie in complementary central layers. The weight word has exactly six transitions around the 2n-cycle (including the closing transition from K_(2n)=L to K_1=U).

PROOF. Initially K1=sum_(i=4)^n x_i is the number of even indices in {4,...,n}, equal to n/2-1=k+1=U. For the first n-3 seam shifts the recurrence K_(i+1)-K_i=1-x_i-x_(i+3) gives zero, since x_(i+3)=1-x_i by alternation. Thus K_1,...,K_(n-2)=U. In the three seam shifts that cross the boundary between the two copies of p, the arriving coordinate has already been flipped once and its current bit is 1-x_(i+3-n). Therefore the differences are x_(i+3-n)-x_i. For i=n-2,n-1,n, the indices i and i+3-n have opposite parity (since n is even), yielding the alternating differences -1,+1,-1. Hence K_(n-1)=L, K_n=U, K_(n+1)=L. At step n+1 the initial root has been complemented, whose ordered bits again alternate, now beginning with 1 instead of 0. The next n-3 differences vanish, giving K_(n+1),...,K_(2n-2)=L. By complementary symmetry of the two halves, the final three boundary differences are +1,-1,+1, returning from K_(2n-2)=L through U,L to the initial U. These are precisely the displayed weights. QED.

COLOR TRANSPORT. Every consecutive n-edge segment of this 2n-cycle is an actual full antipodal geodesic, and each forward shift is a root slide preserving n-3 of the n-2 ordered face-window objects. Therefore this cycle supplies 2n compatible full geodesics whose entire window families lie on the TWO CENTRAL EXTERIOR-WEIGHT LAYERS. For Hamming-radial NORI c(F,pi)=g_pi(K), all 2n path color words are computed solely from the two-bit central data (a(pi),epsilon(pi)); arbitrary profile values outside the central layers play no role. For unrestricted face-dependent NORI, the same cycle exists geometrically and constrains the location and overlaps of its actual ordered faces, although their color values need not depend only on the exterior weight.

RESEARCH IMPLICATION. The earlier central one-jump fibers live as chambers on a genuine root-slide corridor within an antipodally paired 2n-cycle. A Hartman/connector proof could use these compatible cyclic carriers instead of attempting to transport isolated roots under incompatible permutation charts. Pure anti-periodicity of a binary word is insufficient to force a one-change segment: an alternating word can still have many switches. The missing obligation is an overlap or witness-exchange theorem exploiting the joint face incidence across DISTINCT cyclic orders.
