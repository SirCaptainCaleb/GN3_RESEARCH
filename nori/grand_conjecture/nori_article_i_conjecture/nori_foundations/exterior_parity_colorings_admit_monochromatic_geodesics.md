# Exterior parity colorings admit monochromatic geodesics

**Theorem (exterior-parity twist, arbitrary window length).** Fix integers 1≤k≤n, a coordinate order p=(p_1,…,p_n), and any binary function f of ordered k-tuples of distinct coordinates. For each ordered k-face (F,σ), let
c(F,σ)=f(σ) ⊕ (⊕_{u∉free(F)} b_u(F)),
where b_u(F) is the constant bit of coordinate u on F and ⊕ denotes addition in F_2. Then **exactly 2^k starting vertices** yield a monochromatic sequence of all n−k+1 ordered k-face windows along the antipodal geodesic with direction order p. In particular, for k=3 exactly eight starts work for **every fixed permutation**, for all n≥3, regardless of f.

**Proof.** Identify starting vertex bits in p-order by x_1,…,x_n and let X=⊕_{j=1}^n x_j. At window i, the first i−1 directions have been toggled. Its color is
w_i=f(p_i,…,p_{i+k−1}) ⊕ X ⊕ (⊕_{j=i}^{i+k−1}x_j) ⊕ ((i−1) mod 2).
We seek w_i=t for a single t∈F_2. Put q=X⊕t. Choose q and x_1,…,x_{k−1} freely, and successively define
x_{i+k−1}=f(p_i,…,p_{i+k−1}) ⊕ ((i−1) mod2) ⊕ q ⊕ (⊕_{j=i}^{i+k−2}x_j)
for i=1,…,n−k+1. Every x_k,…,x_n is determined, and setting t=X⊕q verifies w_i=t at every window. Conversely, any monochromatic starting vertex has its unique t and q=X⊕t and therefore appears exactly once in this construction. The choices are injective, since the first k−1 bits are freely specified and x_k determines q. Hence exactly 2^k starting vertices work. □

**Antipodal compatibility.** The coloring satisfies c(bar F,rev σ)=1⊕c(F,σ) exactly when f(rev σ)=f(σ)⊕(1+(n−k) mod2). Thus for k=3 this supplies a substantial NORI subclass, with reversal-even f in even n and reversal-odd f in odd n. The theorem also works without antipodal symmetry.

**Affine rank criterion (generalization).** Suppose more generally every ordered k-face color is affine over F_2 in the outside face bits. For a fixed coordinate order p the n−k+1 window colors form w(x)=A_p x⊕b_p. If the augmented matrix [A_p | 1] has full row rank n−k+1, a monochromatic window sequence exists: solve A_px⊕t1=b_p. The exterior-parity theorem above gives a constructive proof of this rank criterion for its special coefficient matrix, and proves the stronger exact count 2^k.

**Scope.** General Boolean dependence on outside face bits, and rank-deficient affine colorings, remain untreated. The grand NORI conjecture remains open.

---

Eight constant exterior-Hamming-layer starts and nonlinear weight lifting

Fix any dimension \(n\ge3\) and any order \(p=(p_1,\ldots,p_n)\) of the coordinates. If the starting bits in this order are \(x_1,\ldots,x_n\), let \(K_i\) be the number of 1-bits fixed outside the consecutive three-face with free directions \(p_i,p_{i+1},p_{i+2}\), after the first \(i-1\) directions have been traversed. Then
\[
K_i=\sum_{j<i}(1-x_j)+\sum_{j>i+2}x_j,\qquad
K_{i+1}-K_i=1-x_i-x_{i+3}.
\]

**Theorem (eight constant-layer starts).** For every fixed direction order \(p\), precisely eight starting vertices make the entire sequence \(K_1,\ldots,K_{n-2}\) constant: freely choose \(x_1,x_2,x_3\), and recursively set
\[
x_{i+3}=1-x_i \quad(1\le i\le n-3).
\]
The successive exterior fixed-bit configurations may differ, but their Hamming weights are identical. This holds independently of any coloring.

**Corollary (arbitrary nonlinear exterior-weight colorings).** Let \(f:\{0,1,\ldots,n-3\}\to\{0,1\}\) be arbitrary, and color every ordered three-face by \(c(F,\pi)=f(K(F))\), where \(K(F)\) is the number of exterior coordinates fixed at 1. Every direction order has at least eight monochromatic antipodal geodesics, namely the starting vertices from the theorem. No antipodal-oddness or linearity of \(f\) is needed.

**Transference corollary.** More generally, let \(h\) be any binary function of ordered triples of distinct coordinates and define
\[
c(F,\pi)=h(\pi)\oplus f(K(F)).
\]
For the eight starts above, the entire sequence of window-color differences is **exactly** the change sequence of \(h(p_i,p_{i+1},p_{i+2})\): the \(f(K_i)\)-term is constant. Thus every one-change direction order for the coordinate-only coloring \(h\) yields at least eight one-change based antipodal geodesics for \(c\). This transfer holds for any \(f\), even when \(c\) does not satisfy antipodal oddness.

**Antipodal compatibility.** Setting \(m=n-3\), this class satisfies \(c(\bar F,\operatorname{rev}\pi)=1\oplus c(F,\pi)\) precisely when
\[
h(\operatorname{rev}\pi)\oplus h(\pi)
 \oplus f(m-k)\oplus f(k)=1
\]
for every ordered triple \(\pi\) and all \(0\le k\le m\). For example, reversal-odd \(h\) with any complement-symmetric weight function \(f(m-k)=f(k)\) is a valid NORI coloring, and the transference result applies. Exterior-weight-only colorings with reversal-even \(h\) are antipodally odd exactly when \(f(m-k)=1\oplus f(k)\), possible for odd \(m\).

*Proof.* When the window shifts right by one direction, the departing coordinate \(p_i\) enters the fixed exterior at its toggled bit \(1-x_i\), and the arriving direction \(p_{i+3}\) leaves the fixed exterior, removing \(x_{i+3}\). This proves the difference formula. Its vanishing for every \(i\) is equivalent to the displayed recurrence. Three freely chosen initial bits determine all later bits uniquely, giving exactly eight starts. Under these starts \(f(K_i)\) is constant, so it changes no adjacent color differences. The antipodal condition follows because complementation sends \(K\) to \(m-K\) and reverses the ordered free directions. \(\square\)

**Scope.** This proves a genuinely nonlinear face-dependent subclass of NORI but does not resolve arbitrary face-position dependence or arbitrary reversal-odd coordinate-only \(h\).

**Statement**

For every coordinate order there are exactly eight starts with constant exterior Hamming weight across all three-face windows; this yields monochromatic geodesics for any color depending only on that weight, and transfers all one-change coordinate-only orders through arbitrary additive weight perturbations.

---

Central exterior-weight jump repairs odd nonlinear two-mark twists

Let n=2r>=6, k=(n-4)/2, and write x_i for the start bits in an arbitrary coordinate order p. Let K_i be the number of exterior one-bits in its i-th three-face window. Then K_(i+1)-K_i=1-x_i-x_(i+3).

CENTRAL JUMP LEMMA. There is a start with (K_1,...,K_(n-2))=(k,k,k+1,...,k+1).

PROOF. Impose x_2=x_5=0, x_4=1-x_1, and x_(i+3)=1-x_i for all i>=3. The displayed K-profile follows once K_1=k. Its initial exterior positions 4,...,n split into the three modulo-three chains C0=(6,9,...), C1=(4,7,...), C2=(5,8,...), of lengths L0,L1,L2 with sum 2k+1. The bits on C0 and C1 alternate with independent initial choices x_3,x_1, so each chain can contribute either floor(L_j/2) or ceil(L_j/2) ones. Chain C2 alternates beginning with zero, contributing floor(L2/2). An odd number of L0,L1,L2 is odd. If exactly one is odd, the lower choices give k ones. If all three are odd, the lower choices give k-1 ones and increasing either adjustable chain gives k. Thus K_1=k. QED.

SPIKE-REPAIR THEOREM. Let c(F,pi)=h(pi) XOR f(K(F)), where h is an arbitrary coordinate-triple label and f(k+1)=1 XOR f(k). If some order p has h-word (q,1 XOR q,q,...,q), then c has a full antipodal geodesic with exactly one change.

PROOF. Take the central-jump start. The f-word is (a,a,1 XOR a,...,1 XOR a), where a=f(k). Its XOR with the h-word is (q XOR a,1 XOR q XOR a,1 XOR q XOR a,...), with exactly one change. QED.

COROLLARY. For n even, partition directions A union M, |M|=2, and set h(a,b,d)=1 precisely if b lies in A and at least one of a,d lies in M. If f(n-3-t)=1 XOR f(t), then c(F,pi)=h(pi) XOR f(K(F)) is antipodal-reversal odd and has a one-change antipodal geodesic. Indeed h is reversal-even and antipodal complementation sends K to n-3-K; the order with both M directions first has h-word (0,1,0,...,0). Apply the theorem. This proves closure for every nonlinear antisymmetric exterior-Hamming-weight twist of the sharp two-mark unrestricted obstruction.

---

Arbitrary central Hamming jumps cancel a prescribed ordered-triple color change

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

---

Central two-layer normal form for arbitrary nonlinear radial NORI

CENTRAL TWO-LAYER NORMAL FORM FOR ORDERED-FACE HAMMING-RADIAL NORI.

Let n>=4. An ordered-three-face coloring is Hamming-radial when its value depends only on its ordered free triple pi and the number K of exterior coordinates equal to 1: c(F,pi)=g_pi(K), where 0<=K<=m=n-3. The NORI oddness condition is EXACTLY
 g_rev(pi)(m-t)=1+g_pi(t)
for every ordered triple pi and every t, where + is mod 2.

ODD DIMENSIONS. If m=2k, define a(pi)=g_pi(k). The NORI identity at t=k yields a(rev pi)=1+a(pi), so a is a reversal-odd coordinate-only coloring. For every fixed coordinate order p there exists a starting root with K_i=k for EVERY consecutive window; indeed impose x_(i+3)=1-x_i, which makes K constant, and select the three free initial chain bits to obtain K1=k. Consequently any one-change order for a yields a one-change NORI geodesic for c. This is an unconditional dimension-preserving reduction from Hamming-radial odd-dimensional NORI to coordinate-only reversal-odd NOR. The latter is also a subclass (take g_pi constant), so the universal conjectures for the two classes are equivalent in each odd dimension.

EVEN DIMENSIONS. Write m=2k+1 and define for each ordered triple pi two bits
 a(pi)=g_pi(k), epsilon(pi)=g_pi(k)+g_pi(k+1).
The NORI identity is EQUIVALENT ON THE TWO CENTRAL LAYERS to
 epsilon(rev pi)=epsilon(pi),
 a(rev pi)=1+a(pi)+epsilon(pi).
Thus switch flags epsilon are reversal-even. At epsilon=0 the lower central color a is reversal-odd; at epsilon=1 it is reversal-even.

Let pi_i=(p_i,p_(i+1),p_(i+2)) be the consecutive triples of a coordinate order p. Constant-central starts K_i=k exist, yielding color word a(pi_i). By the arbitrary-seam jump theorem, for every j=1,...,n-3 there are exactly 2 or 4 roots realizing K_i=k on windows i<=j and K_i=k+1 on windows i>j. At these roots the complete color word is EXACTLY
 W_i(p,j)=a(pi_i)+epsilon(pi_i)*1_(i>j).
The complementary roots realize the downward central jump and produce
 Wdown_i(p,j)=a(pi_i)+epsilon(pi_i)*1_(i<=j).
These formulas depend only on the two central layers, and remain true when the profiles g_pi(t) are nonlinear and completely unrelated away from those layers.

ALL-SWITCHER COROLLARY. If epsilon(pi)=1 for every ordered triple, then a is reversal-even. For every order whose a-word has r>=1 changes, choose any one of those change seams j: W(p,j) has exactly r-1 changes. In particular, existence of an a-order with at most two changes implies a one-change NORI geodesic; existence of an a-order with exactly one change implies a monochromatic NORI geodesic. Here the profile g_pi may vary ARBITRARILY with pi, subject only to its NORI pair identities and the central switch flag. This strictly enlarges the common additive Hamming-function family h(pi)+f(K).

MIXED-FLAG CERTIFICATE. More generally, for arbitrary epsilon, if there exist p and j for which the explicit word W(p,j) or Wdown(p,j) has at most one adjacent change, the arbitrary Hamming-radial NORI coloring admits the desired geodesic. This reduces the central-witness construction to a finite two-bit reversal-constrained ordered-triple problem. It is a sufficient certificate, not a proof that a good p,j always exists. In particular the all-zero flags include the open reversal-odd coordinate-only NOR case, and arbitrary face-position dependence is beyond the radial hypothesis.

CONSTANT-LAYER START JUSTIFICATION. Let L1,L2,L3 be the lengths of exterior index chains (4,7,...),(5,8,...),(6,9,...), summing to m. In an alternating chain of length L, its number of ones is either floor(L/2) or ceil(L/2). If m even, exactly zero or two chain lengths are odd, so k=m/2 is attainable. If m odd, exactly one or three lengths are odd, so floor(m/2) is attainable. This proves the constant-central start claim for both parity cases.

---

Exact three-chain generating polynomial for all exterior-weight profiles

EXACT THREE-CHAIN SOLUTION OF PRESCRIBED EXTERIOR-WEIGHT PROFILES.

Let p=(p1,...,pn) be a fixed permutation of the n coordinate directions, x_i the initial bit at p_i, and K_i=sum_(t<i)(1-x_t)+sum_(t>i+2)x_t the exterior Hamming weight at the i-th three-direction window. As usual
 K_(i+1)-K_i=1-x_i-x_(i+3)
for 1<=i<=n-3.

THEOREM (exact generating-function characterization). Fix ANY prescribed signed increment vector delta=(delta_1,...,delta_(n-3)) in {-1,0,+1}^(n-3). Partition coordinate positions 1,...,n into the three chains (r,r+3,r+6,...), r=1,2,3. On each chain, interpret each seam relation between x_i and x_(i+3) as follows:
 delta_i=0 requires (x_i,x_(i+3)) in {(0,1),(1,0)};
 delta_i=+1 requires (0,0);
 delta_i=-1 requires (1,1).
If a chain's edge requirements are inconsistent, the profile has no root. Otherwise:
(A) a chain containing at least one nonzero delta_i has EXACTLY ONE binary labeling of its coordinates; denote the number of 1-bits among its exterior positions (indices >=4) by a_r.
(B) a chain with all zero delta_i has exactly TWO alternating binary labelings; if it has L_r exterior positions, the two possible numbers of exterior ones are floor(L_r/2) and ceil(L_r/2), counting multiplicity if L_r is even.
Define the polynomial
 P_delta(z)=product_(r=1)^3 P_r(z),
where P_r(z)=z^(a_r) in case A, and P_r(z)=z^floor(L_r/2)+z^ceil(L_r/2) in case B. If any chain is inconsistent set P_delta=0. Then for EVERY integer q, the coefficient [z^q]P_delta is EXACTLY the number of roots x for which K_1=q and K_(i+1)-K_i=delta_i for all i. In particular the unconstrained initial-weight fiber size is 2^(number of chains with no nonzero seam), and every exact fiber has size at most 8.

PROOF. Each difference equation is equivalent to its displayed allowed bit-pair condition. Relations on distinct residue classes modulo 3 share no variables. On one chain with all delta=0, the first bit may be chosen arbitrarily and all later bits alternate, giving two solutions with the stated exterior weights. On a chain with some nonzero delta, that edge fixes both endpoint bits, and the remaining relations propagate uniquely to both ends (or contradict another fixed edge). Therefore valid assignments multiply across the three chains. The exponent of the corresponding monomial records the contribution to K_1 from each chain. Polynomial multiplication counts exactly the assignments with a given total exterior weight q. QED.

TWO-JUMP COMPATIBILITY. Let n be even and k=(n-4)/2. To prescribe the central profile k before seam j, k+1 between seams j<l, and k thereafter, put delta_j=+1, delta_l=-1, other deltas0 and test [z^k]P_delta>0. Whenever j,l lie on the same residue chain, chain compatibility REQUIRES (l-j)/3 even (equivalently 6 divides l-j). If they lie on distinct chains, the chain equations are automatically consistent, though the weight coefficient can still vanish. Reversing the jump signs gives the complementary high/low/high profile with K_1=k+1 and is equivalent by complementing all root bits.

TWO-SEAM COLOR CANCELLATION. Suppose c(F,pi)=h(pi)+f(K(F)), where n is even and f(k+1)=1+f(k). Fix an order p and two distinct color-change seams j<l of its coordinate-only h-word. If [z^k]P_delta>0 for delta_j=+1, delta_l=-1, delta_i=0 otherwise, the corresponding central-profile root toggles the f-color exactly at j and l and cancels BOTH chosen changes, leaving exactly r-2 changes when the h-word has r changes. For r<=3 this yields a full one-change NORI geodesic (assuming the original coloring satisfies NORI oddness). The criterion applies to ANY two change seams; it does not require they be consecutive within the list of changes.

SCOPE. This completely determines which arbitrary signed exterior-weight profiles are realizable, and strengthens the earlier single central jump by an exact multiple-jump test. A two-jump pattern may fail even when its seams are on distinct residue chains because the total initial exterior weight cannot be the central value. Such failures show the limit of root-only central-weight cancellation, and motivate exchanging the direction order p.

---

Every ordered k-window has a central jump with exact binomial witness count

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

---

Two homogeneous central layers force closure despite arbitrary off-layer face dependence

CENTRAL-LAYER HOMOGENEITY SUFFICES; ALL OTHER FACE DEPENDENCE IS FREE.

Let n be even, n>=4, k=(n-4)/2. Let c be an arbitrary binary coloring of ordered three-faces of Q_n satisfying NORI oddness c(bar F,rev pi)=1+c(F,pi). Assume ONLY the following central-layer homogeneity: for each ordered free triple pi there exist bits a(pi),epsilon(pi) such that
 c(F,pi)=a(pi) for EVERY face F whose exterior Hamming weight K(F)=k;
 c(F,pi)=a(pi)+epsilon(pi) for EVERY face F with K(F)=k+1.
The colors of faces at all other exterior Hamming weights may depend arbitrarily on the entire exterior bitstring and on pi, subject only to NORI oddness.

THEOREM (genuinely face-dependent central two-layer reduction). The NORI involution forces epsilon(rev pi)=epsilon(pi) and a(rev pi)=1+a(pi)+epsilon(pi). For every coordinate order p, the constant-central starts and the prescribed central-jump roots of the three-chain theorem yield exactly the same color words as in the radial normal form:
 W_i(p,j)=a(pi_i)+epsilon(pi_i)*1_(i>j),
 Wdown_i(p,j)=a(pi_i)+epsilon(pi_i)*1_(i<=j).
Thus any p,j for which either explicit word has at most one change certifies full NORI closure for this coloring. In particular, if epsilon=1 on all ordered triples and there is an order whose a-word has at most two color changes, then a full one-change antipodal geodesic exists. If epsilon=1 and some a-word has exactly one change, a monochromatic geodesic exists.

PROOF. The antipodal of a k-layer ordered face is a (k+1)-layer face because n-3=2k+1, with free order reversed. Evaluating NORI oddness on the two central weights yields the stated relations. All constructed roots have K_i entirely within {k,k+1}; hence their face colors are determined exactly by (a,epsilon), regardless of the values assigned on every other face. Substitute their weight profiles into the two displayed homogeneous-layer formulas. The resulting binary words are precisely W and Wdown, and the color-change conclusions follow. QED.

ODD-DIMENSION ANALOGUE. If n is odd and m=n-3 is even, impose homogeneity only on the unique self-complementary middle layer K=m/2. NORI then makes the induced coordinate-only triple label a(pi) reversal-odd. A constant-middle-layer start exists for every direction order. Consequently every one-change a-order transfers to a full NORI one-change geodesic, with arbitrary face-dependent values away from the middle layer.

SIGNIFICANCE. Global Hamming-radial dependence is UNNECESSARY: one or two middle layers alone suffice. This is an exact enlargement to true nonlinear and nonradial ordered-face colorings. The unresolved general NORI case is the presence of arbitrary variation WITHIN the central Hamming layers; proving exchange/coherence across their exterior bitstrings is now the precise additional task.
