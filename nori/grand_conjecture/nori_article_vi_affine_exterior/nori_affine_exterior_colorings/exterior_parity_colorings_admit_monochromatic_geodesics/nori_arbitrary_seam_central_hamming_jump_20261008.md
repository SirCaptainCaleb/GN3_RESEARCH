# Arbitrary central Hamming jumps cancel a prescribed ordered-triple color change

ARBITRARY-SEAM CENTRAL JUMP AND EXACT FIBER MULTIPLICITY (proved).
Let n>=4 be EVEN and k=(n-4)/2. Fix a direction order p=(p1,...,pn); identify starting coordinates with bits x1,...,xn in this order. The exterior Hamming weight of its i-th ordered-three-face window is K_i = sum_(r<i)(1-x_r) + sum_(r>i+2)x_r. Therefore K_(i+1)-K_i=1-x_i-x_(i+3).

THEOREM. For EVERY seam j in {1,...,n-3}, precisely 2 or 4 starts satisfy K_i=k for i<=j, and K_i=k+1 for i>j.

PROOF. The prescribed differences require x_j=x_(j+3)=0 and x_(i+3)=1-x_i at all i different from j. The n-3 exterior indices 4,...,n form three residue-class chains C_r=(r+3,r+6,...) (r=1,2,3), of lengths L1,L2,L3 summing to n-3=2k+1. Every unbroken chain is alternating, with either floor(L_r/2) or ceil(L_r/2) ones, selectable by its free first bit. Each EVEN unbroken chain admits two assignments with the same count; each ODD unbroken chain admits one assignment for either count. The chain containing j is uniquely determined. If j<=3 it begins with 0 and contributes floor(L_r/2) ones. If j>3, let q be the position of x_j in that exterior chain, so positions q,q+1 are both zero. This chain contributes floor(L_r/2) ones except when L_r is even and q is odd, when it contributes floor(L_r/2)-1. (This follows by alternating outward on either side of the forced 00 pair.)

Exactly one or three of L1,L2,L3 are odd. Put B=sum_r floor(L_r/2). If exactly one length is odd, B=k. If all three are odd, B=k-1.
If the exceptional chain has the lower usual contribution, then:
- for one odd chain, choose lower on each free odd chain, giving K_1=k;
- for three odd chains, raise exactly one of the two free odd chains, giving K_1=k.
If the exceptional chain loses one additional 1, its length is even and exactly one free chain is odd. Raise that free odd chain, restoring K_1=k. Thus the prescribed full K-profile is always attained. Counting the allowed choices on the two free chains yields exactly 2 or 4 starts (the possibilities are two free odd chains with one raised =2; one free odd and one free even =2; or two free even chains =4). QED.

COMPLEMENT. Complementing every starting bit sends K_i to (n-3)-K_i = (2k+1)-K_i, and hence supplies the corresponding central DOWNWARD jump at any chosen seam.

SEAM-CANCELLATION THEOREM. Let h be any binary coloring of ordered coordinate triples and f:{0,...,n-3}->F_2 any function satisfying f(k+1)=1+f(k). Define c(F,pi)=h(pi)+f(K(F)) (sums in F_2). For any coordinate order p whose h-window word has r>=1 color changes and any chosen change seam j, each start realizing the upward central jump at j yields a c-word with EXACTLY r-1 changes: its f-word is constant on each side of j and flips once at j. In particular, if any coordinate order has <=2 h-changes, c admits an at-most-one-change antipodal geodesic; if an order has exactly one h-change, c admits a monochromatic antipodal geodesic.

When h is reversal-even and f(n-3-t)=1+f(t) for every t, then c obeys NORI antipodal-reversal oddness. For even n the latter identity automatically implies f(k+1)=1+f(k). Thus every reversal-even coordinate-only h with some <=2-change order gives NORI closure for ALL its antipodally antisymmetric Hamming-layer twists. The previously studied two-mark obstruction has an explicit 2-change order, so all its such twists satisfy NORI.

SCOPE. This is an all-even-dimensional radial family, not a proof for arbitrary face-dependent NORI. Multiple seam prescriptions can impose incompatible starting-bit constraints and require a separate global mechanism.
