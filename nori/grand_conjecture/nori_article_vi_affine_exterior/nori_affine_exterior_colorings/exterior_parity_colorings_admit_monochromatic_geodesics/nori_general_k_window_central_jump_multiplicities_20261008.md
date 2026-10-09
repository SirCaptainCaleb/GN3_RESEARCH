# Every ordered k-window has a central jump with exact binomial witness count

GENERAL k-WINDOW CENTRAL-JUMP THEOREM WITH EXACT MULTIPLICITY.

Let 1<=k<n and suppose m=n-k=2q+1 is odd. Fix a coordinate order p=(p1,...,pn) and a starting vertex with p-ordered bits x1,...,xn. The exterior Hamming weight of its i-th ordered k-face window, for i=1,...,m+1, is
 K_i=sum_(a<i)(1-x_a)+sum_(a>i+k-1)x_a.
Consequently K_(i+1)-K_i=1-x_i-x_(i+k) for 1<=i<=m.

THEOREM. For every prescribed seam j in {1,...,m}, there is a starting vertex with
 K_i=q for i<=j, and K_i=q+1 for i>j.
Indeed there are an explicit positive number of such starts, depending only on n,k, and the residue class of j modulo k.

PROOF. Force x_j=x_(j+k)=0, and x_(i+k)=1-x_i for all other seam indices i. Partition the m exterior bit positions k+1,...,n into the k residue-class chains C_r=(r+k,r+2k,...) indexed by r=1,...,k, with lengths L_r. These lengths sum to 2q+1, so the number t of odd lengths is odd. Every chain other than the exceptional one containing seam j alternates and has two independently selectable patterns, contributing floor(L_r/2) or ceil(L_r/2) ones in its exterior positions (the two patterns contribute equal counts when L_r is even).

In the exceptional chain, if j<=k, the first exterior bit is forced zero and the chain has floor(L_e/2) ones. If j>k, an interior adjacent pair in the exterior chain is forced 00; all remaining bits alternate outward. This yields floor(L_e/2) ones except when L_e is even and the initial 00 occurs at an odd exterior position, when it yields floor(L_e/2)-1.

Let B=sum_r floor(L_r/2)=(m-t)/2. We need K1=q=(m-1)/2, or an increment of (t-1)/2 above B.
If the exceptional chain is odd, it supplies its baseline floor(L_e/2), and the other t-1 odd chains can freely supply the required (t-1)/2 extra ones. The number of roots realizing the profile is
 2^(k-t) * binomial(t-1,(t-1)/2).
If the exceptional chain is even, the other t odd chains can supply either (t-1)/2 extra ones (when there is no exceptional deficit) or (t+1)/2 (when the exceptional chain loses an extra one). These two binomial coefficients agree because t is odd. The number of roots is
 2^(k-t-1) * binomial(t,(t-1)/2).
Both numbers are strictly positive. The remaining even free chains each contribute a factor 2, giving the displayed exact multiplicities. QED.

SINGLE-SEAM CANCELLATION COROLLARY. Let h be an arbitrary binary label of ordered k-tuples and let f:{0,...,n-k}->F2 satisfy f(q+1)=1+f(q). Color every ordered k-face by c(F,pi)=h(pi)+f(K(F)). If a coordinate order has r>=1 changes in its h-window word, choose the central jump at any of its change seams. The resulting ordered k-face geodesic has exactly r-1 changes. If h is reversal-even and f(m-s)=1+f(s) for every s, this is an antipodal-reversal-odd ordered k-face coloring. The result therefore generalizes the NORI k=3 central-jump lemma and includes k=1 edge-face colorings under the same exterior-radial structure.

In the NORI case k=3 the number t of odd chain lengths is either 1 or 3, and the formulas specialize to exactly 2 or 4 roots per upward central jump. For an arbitrary k, the number of roots is a positive explicit binomial coefficient times a power of two.

SCOPE. The theorem proves existence and multiplicities of a central Hamming-layer jump for every even-dimensional k=odd case (and more generally whenever n-k is odd). It does not supply coherence of ordered-face colors on exterior assignments having the same Hamming weight.
