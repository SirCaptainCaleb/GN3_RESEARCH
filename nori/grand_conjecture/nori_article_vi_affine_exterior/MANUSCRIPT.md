# Article VI - Affine exterior methods

## Article setting and orientation

The affine exterior-parity manuscripts prove exact starting-root solution counts and develop affine change-vector syndrome methods. Other surviving results provide endpoint-deletion inequalities, six-window root control, controlled nonlinear fault tolerance, and local physical exterior-chart interpolation. These are positive mathematical statements for their stated structural hypotheses; no unrestricted NORI3 existence theorem follows.

The six-path forcing-certificate lifting obstruction is a separate rigorous, method-specific negative result. Its signed exterior-bit holonomy calculation and complete original proof now reside in a linked research note, not in a standalone Subsection. This classification does not prohibit lifting under a different globally compatible forcing network. Any transfer to the unrestricted NORI1 or ordinary boundary-tournament objectives must preserve actual physical faces and coordinate simplicity.

*Full Article composition: [source manuscript](../nori_article_vi_affine_exterior.md).*

## Affine colorings, exterior-bit control, and lifting obstructions

For an ordered three-face \((F,\pi)\), its exterior-bit vector consists of the coordinates fixed outside the free triple \(\pi\). This section isolates classes in which the dependence on those bits can be controlled algebraically, and explains why local lifting arguments must preserve their actual physical positions. The strongest general method is an explicit root-solving recurrence, which works even without antipodal oddness.

*Full Section composition: [source manuscript](nori_affine_exterior_colorings.md).*

### Exterior parity colorings admit monochromatic geodesics

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

### Endpoint deletion and affine obstruction rigidity

# Endpoint truncation and affine influence restrictions

Let \(V\) be a set of \(n\ge5\) cube coordinates. A full geodesic \(P=(x;p_1,\ldots,p_n)\) has ordered-three-face color word \(w(P)=w_1\cdots w_{n-2}\), with \(w_i\in\mathbb F_2\). Put \(\delta_i=w_i+w_{i+1}\in\mathbb F_2\), interpreted as an integer in \(\{0,1\}\) when counting changes. The coloring is of *physical ordered three-faces*: a window color depends on the exterior fixed cube coordinates and the order of its three free directions, and is independent of the corner at which the window is traversed.

## 1. A two-ended deletion lemma

**Lemma.** Suppose that both paths obtained from \(P\) by deleting its first edge and by deleting its last edge have at most one change in their respective window words. If \(P\) has at least two changes, its window word has precisely the shape
\[
0\,1^{\,n-4}0\quad\text{or}\quad1\,0^{\,n-4}1.
\]

**Proof.** Deletion of the last edge gives \(\sum_{i=1}^{n-4}\delta_i\le1\), while deletion of the first gives \(\sum_{i=2}^{n-3}\delta_i\le1\). An interior change \(\delta_i=1\), \(2\le i\le n-4\), would use the entire allowance of both truncated paths, excluding changes at all other positions and contradicting the assumption that \(P\) has at least two changes. Therefore all interior \(\delta_i\) vanish. The assumed two changes must be exactly \(\delta_1=\delta_{n-3}=1\), yielding the displayed words. \(\square\)

This is a word-theoretic lemma, applicable to arbitrary binary ordered-face colorings. It isolates the sole way two individually good truncations can fail to fit into a full good path: the two terminal seams change and the interior stays constant.

## 2. Affine starting-root images

Fix a direction permutation \(p\). Suppose every window color \(w_i(x,p)\) is an affine function of the starting vertex \(x\in\mathbb F_2^n\), as holds if the ordered-face colors are affine in their exterior bits. Define
\[
\Delta_p(x)=\bigl(w_1+w_2,\ldots,w_{n-3}+w_{n-2}\bigr)
             \in\mathbb F_2^{n-3}.
\]
This is an affine map; its Hamming weight is the number of changes of the corresponding full path.

**Proposition (codimension-one criterion).** If the linear part of \(\Delta_p\) has rank at least \(n-4\), some start \(x\) makes the fixed order \(p\) good. Consequently a fixed order that is bad for every root in dimension six has change-map rank at most one.

**Proof.** Put \(r=n-3\). The nonempty affine image of \(\Delta_p\) has codimension at most one in \(\mathbb F_2^r\). A full image contains \(0\). An affine hyperplane is of the form \(\{z:\lambda\cdot z=b\}\), with \(\lambda\ne0\). When \(b=0\) it contains \(0\), and when \(b=1\) it contains \(e_j\) for any \(j\) with \(\lambda_j=1\). Either way the image contains a vector of weight at most one, as required. \(\square\)

Thus, in the affine subclass, failure for a given order is accompanied by a strong and explicitly testable rank deficiency; no antipodal-reversal condition was needed.

## 3. Complementary-triple influence in dimension six

Now let \(n=6\) and impose the actual NORI condition
\[
c(\bar F,\operatorname{rev}\pi)=1+c(F,\pi).
\]
For a free triple \(T\subset V\) and its designated middle direction \(b\in T\), define \(I(T,b)\subset V\setminus T\) to be the exterior directions that influence the color of an ordered face of type \(T\), for some assignment of its other exterior bits. Reversing the first and third directions leaves this influence set unchanged: antipodal reversal carries the Boolean exterior function to its complemented-input, complemented-output version, preserving each coordinate's Boolean sensitivity.

**Proposition (opposite influence sparsity).** Let \(U=V\setminus T\). If \(d\in I(T,b)\), then \(I(U,e)\subseteq\{b\}\) for every \(e\in U\setminus\{d\}\), under the assumption that no full geodesic has at most one change. If \(|I(T,b)|\ge2\), then \(I(U,e)\subseteq\{b\}\) for all \(e\in U\).

**Proof.** Write \(T=\{a,b,c\}\), \(U=\{d,e,f\}\) and take the order \((a,b,c,d,e,f)\). The four three-face colors are \(A,B,C,D\). Both middle windows have \(c,d\) free and hence are independent of the starting bits \(x_c,x_d\). By hypothesis on \(d\), the first window's color \(A\) can be chosen by varying \(x_d\), holding its other exterior bits fixed. If the last-window color \(D\) were sensitive to \(x_c\), it could be chosen by varying \(x_c\), holding its own other exterior bits fixed. The two exterior choices are independent: \(A\) does not depend on \(x_c\) and \(D\) does not depend on \(x_d\). Choose \(x_d\) to enforce \(A=B\) and \(x_c\) to enforce \(D=C\); the resulting word \((B,B,C,C)\) is good, a contradiction. Therefore the ordered \(U\)-face with middle \(e\) is insensitive to \(c\). Reversing the order of \(T\) preserves sensitivity in \(d\) and similarly excludes sensitivity in \(a\). The only potentially influential coordinate of \(T\) is \(b\). Exchanging \(e\) and \(f\) gives the same conclusion for the other middle direction of \(U\). Finally, if \(d,d'\in I(T,b)\) are distinct, each \(e\in U\) differs from at least one of them, so the first statement applies to all three choices. \(\square\)

The three results expose complementary restrictions on a hypothetical bad coloring: terminal truncation confines switches to two seams, affine dependence forces low change-map rank, and two exterior influences on one triple suppress almost all influences on its complementary triple. The affine and dimension-six statements are conditional structural constraints; neither independently establishes the arbitrary-dimensional NORI conjecture.

### Exact change-vector fibers and affine obstruction certificates

Let \(Q_n=\{0,1\}^n\). Each ordered three-face \((F,\pi)\) has a binary color depending on its free-coordinate order \(\pi\) and the fixed exterior coordinate bits. For a coordinate order \(p=(p_1,\ldots,p_n)\) and an initial vertex \(x\), write \(w_1(x),\ldots,w_{n-2}(x)\) for the consecutive ordered-three-face colors and \(d_i(x)=w_i(x)\oplus w_{i+1}(x)\) for \(1\le i\le n-3\). A good antipodal geodesic is exactly one with Hamming weight \(|d(x)|\le1\).

**Theorem 1 (exact universal-flipper fiber law).** Partition the coordinate set as \(V=A\sqcup B\), with \(|A|=r\) and \(|B|=m\ge3\). Suppose that whenever an \(a\in A\) is fixed outside an ordered three-face, complementing its fixed bit complements the face color. Fix arbitrary coordinate orders \(\sigma\) of \(A\), \(\tau\) of \(B\), and an arbitrary starting vertex \(y\) in the \(B\)-coordinates. As the \(r\) initial \(A\)-bits vary, the complete change vectors on the full direction order \(\sigma\tau\) are **exactly**
\[
\bigl\{(u,\delta(\tau,y)):u\in\mathbb F_2^r\bigr\},
\]
each occurring exactly once. Here \(\delta(\tau,y)\in\mathbb F_2^{m-3}\) is the change vector along the induced \(B\)-geodesic, with \(A\)-bits omitted (their common fixed parity does not affect changes).

**Proof.** Write \(A=(a_1,\ldots,a_r)\), and let \(z_i\) be the initial bit at \(a_i\). The universal-flipper hypothesis implies
\[
 c(F,\pi)=\bigoplus_{a\in A\setminus\mathrm{free}(F)}x_a(F)\ \oplus\ g(\pi,x_{B\setminus\mathrm{free}(F)})
\]
for a function \(g\) independent of every fixed \(A\)-bit. The \(g\)-contribution \(G_i\) to window \(i\) is therefore determined by \(\sigma,\tau,y\) and independent of \(z\). For \(1\le i\le r\), shifting the three-coordinate window one position to the right fixes the departing \(a_i\) at its already toggled value \(1\oplus z_i\), and removes the untoggled arriving \(a_{i+3}\) if \(i+3\le r\). Consequently
\[
 d_i=G_i\oplus G_{i+1}\oplus 1\oplus z_i
 \oplus\mathbf1_{i+3\le r}z_{i+3}.
\]
For prescribed \(d_1,\ldots,d_r\), solve successively for \(z_r,z_{r-1},\ldots,z_1\). Each equation has coefficient one at the currently solved variable and only uses previously solved higher-index \(A\)-bits. The correspondence \(z\mapsto(d_1,\ldots,d_r)\) is bijective. For \(i>r\), both windows lie within \(B\); all \(A\)-bits have been toggled and contribute the same common parity to both colors. Thus \((d_{r+1},\ldots,d_{r+m-3})=\delta(\tau,y)\). This proves the claim. \(\square\)

**Corollary 1 (exact lifting count).** Put \(q=|\delta(\tau,y)|\). The number of choices of initial \(A\)-bits giving a full geodesic with at most one change is exactly \(r+1\) when \(q=0\), exactly \(1\) when \(q=1\), and \(0\) when \(q\ge2\). Thus a monochromatic residual geodesic admits \(r+1\) distinct good lifts, and a one-change residual geodesic admits one canonical good lift.

**Corollary 2 (complete equidistribution).** If \(m\le3\), then for every prescribed full change vector \(d\in\mathbb F_2^{n-3}\) and fixed coordinate order with \(A\) first, **exactly eight** of the \(2^n\) starting vertices realize \(d\). For \(m=3\), apply Theorem 1 and vary the eight \(B\)-starts. For \(m<3\), the same descending equations freely prescribe all \(n-3\) changes; the remaining \(3-m\) unused \(A\)-bits and the \(m\) \(B\)-bits supply exactly \(2^{3-m+m}=8\) starts. In particular there are exactly \(8(n-2)\) good starts and eight monochromatic starts per such order. The exterior-parity theorem is the special case \(A=V\).

**Theorem 2 (exact affine syndrome criterion).** More generally, suppose the ordered-face colors are affine Boolean functions of their fixed exterior bits. For each fixed direction order \(p\), write its change map as \(d(x)=Mx\oplus b\in\mathbb F_2^s\), where \(s=n-3\) and \(M\) has rank \(\rho\). Let \(H\) be any \((s-\rho)\times s\) matrix of full row rank with \(HM=0\), so \(\ker H=\mathrm{im}M\). Then a good geodesic with this direction order exists **if and only if**
\[
 Hb\in\{0,He_1,\ldots,He_s\}.
\]
Its number of good starting vertices is exactly
\[
 2^{n-\rho}\Bigl|\{0,e_1,\ldots,e_s\}\cap(b+\mathrm{im}M)\Bigr|.
\]
**Proof.** An attainable change vector is precisely an element of the affine coset \(b+\mathrm{im}M=\{v:Hv=Hb\}\), and every such vector has \(2^{n-\rho}\) preimages. The words of Hamming weight at most one are exactly \(0,e_1,\ldots,e_s\). \(\square\)

The syndrome test proves the codimension-at-most-one affine criterion immediately: when \(s-\rho\le1\), the syndromes of zero and the unit vectors cover the entire syndrome space. In dimension six, an affine coloring failing every antipodal geodesic must therefore have \(\mathrm{rank}(M_p)\le1\) for **every** direction order \(p\), an explicit rank-rigidity condition. For larger codimension, the missing syndrome \(Hb\) is the exact linear obstruction for a specified order.

All assertions here are unconditional on antipodal oddness. They concern the stated subclasses and per-order certificates; the grand ordered-three-face conjecture remains unresolved.

## Recent consequences and compatibility conditions

# Reduction of the odd-flipper frontier to seven dimensions

Suppose \(c\) is an antipodal-reversal-odd ordered-three-face coloring of \(Q_n\) and all but exactly six coordinates are universal exterior flippers. Write the six remaining coordinates \(B\), and \(r=n-6\). If \(r\) is even, the earlier parity-six closure theorem applies.

If \(r\) is odd, choose one flipper \(g\in A\) and put \(A'=A\setminus\{g\}\), so \(|A'|=r-1\) is even. Restrict to the seven-dimensional subcube with directions \(B\cup\{g\}\), fixing all \(A'\)-coordinates to zero, to define \(c'\). By the universal-flipper identity and even parity of \(|A'|\), the induced \(c'\) is antipodal-reversal-odd: reversing within the seven-dimensional subcube and complementing all fixed \(A'\)-bits changes the color by \(1\oplus |A'|=1\). The direction \(g\) remains a universal exterior flipper in \(c'\).

Apply the exact flipper lifting lemma to the set \(A'\): any one-change antipodal geodesic in \(c'\) lifts to a one-change antipodal geodesic in \(c\).

**Seven-dimensional bottleneck theorem.** To prove NORI for every coloring in every dimension having at most six nonflipper coordinates, it suffices to prove NORI for the class of \(Q_7\) colorings with *one universal exterior flipper*. Combined with the already proved even-flipper and five-nonflipper theorems, this is the sole outstanding configuration for that entire structured class.

The restriction is a sufficient reduction; it does not assert that arbitrary NORI counterexamples possess any universal flipper.

For every n>=7 there is a NORI antipodal-reversal-odd ordered-three-face coloring with pointwise reversal-evenness, affine single-exterior-bit color on each face, and a coordinate order for which EVERY starting vertex produces at least two color changes.

Construction: On ordered free triples (1,2,3), (2,3,4), (3,4,5), (4,5,6), and (i,i+1,i+2) for i>=5, assign face colors respectively y_n, 1+y_1, y_1, y_n, y_1 (sum mod 2; y is the physical exterior-bit assignment). Along order (1,...,n) from x, the color word is (x_n,x_1,1+x_1,x_n,1+x_1,...,1+x_1). Its first five bits are 00101, 01000, 10111, or 11010 according to (x_1,x_n)=(0,0),(1,0),(0,1),(1,1); each has at least two switches, and the remaining bits repeat its fifth bit. Give reversed ordered triples the same function on their common face. Fill all other reversal-pairs using an arbitrary single exterior bit y_r (possible since n>=7). Each function changes under exterior-bit complement, so c(bar F,rev pi)=1+c(F,pi) globally. This proves the claim.

Research consequence: oddness plus exact face-locality does not force a good root for any fixed coordinate order. A grand-closure argument must exchange direction orders as well as roots. This is a proof obstruction to root-only Hamming-layer or fixed-permutation surjectivity arguments, not a counterexample to the grand conjecture.

### Affine change syndromes and exact root-count phenomena

# Affine change syndromes and exact root-count phenomena

Fix a coordinate order and vary the starting vertex in an affine coloring of physical ordered faces. The successive color changes are affine functions of the root bits; good paths correspond to syndrome vectors of Hamming weight at most one. This linear-algebraic translation gives exact fiber counts, quantitative generic success and sharp rank-deficient obstructions.

## A valid antipodally odd affine edge coloring with reachability nerve chi=2, Lefschetz=0

On Q_4={0,1}^4, define the color of direction-i edges by
\[
c_1(x)=x_3,\qquad c_2(x)=x_4,\qquad
c_3(x)=x_4,\qquad c_4(x)=x_3,
\]
where c_i is independent of x_i as required for an undirected edge coloring. Every c_i depends on exactly one *exterior* bit, so complementing all cube bits flips every edge color: c_i(bar x)=1-c_i(x). Hence the original antipodal-odd edge axiom holds.

For the COLOR-FREE monochromatic geodesic reachability nerve K_R on 16 cube-vertex labels, the exact simplicial face counts are
\[
(f_0,\ldots,f_{15})=
(16,120,560,1820,4368,8008,11440,12870,11440,7992,4320,1752,504,92,8,0).
\]
Therefore
\[
\boxed{\chi(K_R)=\sum_{k=0}^{15}(-1)^k f_k=2.}
\]
The counts of τ-invariant simplices supported on respectively r antipodal vertex pairs, r=1,...,8, are
\[
(a_1,\ldots,a_8)=(8,28,56,70,52,22,4,0).
\]
An invariant simplex with r antipodal pairs has 2r vertices and τ acts as r disjoint vertex transpositions; its contribution to the antipodal Lefschetz number is \((-1)^{(2r-1)}(-1)^r=(-1)^{r+1}\). Hence
\[
\boxed{L(\tau)=\sum_{r=1}^8(-1)^{r+1}a_r=0.}
\]
Nevertheless ALL eight antipodal edges {x,bar x} belong to K_R: R(x)∩R(bar x) is nonempty for every x.

**Exact reproducibility without black-box search.** For each root x, define dynamic Boolean arrays r_q(x,S) on coordinate subsets S⊆[4]:
\[
r_q(x,\varnothing)=1,\qquad
r_q(x,S)=\bigvee_{i\in S}\bigl[
r_q(x,S\setminus\{i\})\ \land\
(c_i(x\oplus(S\setminus\{i\}))=q)
\bigr].
\]
Then R(x) consists exactly of x⊕S for which r_0(x,S)∨r_1(x,S)=1. Enumerating x in binary order 0000 through 1111 and encoding R(x) as a 16-bit mask with target z at bit position z gives
\[
(0fff,0fff,0fff,0fff,\ ff7f,ffbf,ffdf,ffef,\
f7ff,fbff,fdff,feff,\ fff0,fff0,fff0,fff0).
\]
The nerve simplex test is the direct formula
\[
\sigma\in K_R\ \Longleftrightarrow\
\exists z\in Q_4:\ \sigma\subseteq R(z),
\]
using symmetry R(z) as the set of roots that can reach z. Counting nonempty bitmask subsets of the displayed region masks produces exactly the face counts above. Counting masks closed under z→15⊕z produces a_r.

**Implication.** The raw reachability nerve does not universally have odd Euler characteristic, and the antipodal involution need not have nonzero Lefschetz number, EVEN when every antipodal pair has an intersection certificate. Consequently neither invariant alone can prove the grand edge conjecture on this nerve. This is a precise, fully specified counterexample to an overly strong topological forcing hypothesis; it does NOT refute the edge conjecture or the exact fixed-point equivalence. A refined nerve, local carrier condition, or higher-order reachability incidence theorem is necessary.

## Random affine NORI: most colorings are full-rank at EVERY chosen permutation with a quantitative constant bound

Consider the affine-exterior ordered-three-face family
 c(F,(i,j,k))=h(i,j,k)+sum_(t notin{i,j,k}) a_(i,j,k),t z_t,
where all bits are mod2. Impose active NORI antipodal-reversal oddness by choosing the coefficient vector and intercept freely and uniformly for one ordered-triple in each reversal pair, and defining the reversed triple on the antipodal face by the complementary rule. In particular, for any FIXED full direction permutation pi, the exterior coefficient vectors L_1,...,L_(n−2) associated with its consecutive ordered triples are independent and uniformly random on the coordinate subspaces outside their respective free triples: none of these ordered triples is the reverse of another since pi uses distinct directions.

Let m=n−3 and form the affine full-geodesic change vector D_pi(x)=b+M x∈F2^m, where the slope of its jth row is L_j+L_(j+1). The random intercepts do not affect rank.

**Theorem (explicit rank failure probability).** For EVERY fixed direction order pi and all n>=4,
 P(rank M < m)
 <= 1/8 + (4n−14)/2^n.
In particular this bound is <=5/16 for all n>=4 (with its maximum at n=5), so
  P(rank M=n−3) >= 11/16
for every n>=4; the probability lower bound tends to 7/8 as n→∞.

Whenever rank M=n−3, for EVERY binary change pattern y∈F2^m exactly eight starting roots produce D_pi(x)=y. Hence at least 11/16 of the randomly sampled valid AFFINE NORI colorings have exactly eight fully monochromatic antipodal pi-geodesics for this SINGLE user-prescribed order and exactly 8(n−2) good <=1-switch pi-geodesics.

**Proof (first moment of the left kernel).** Write the (m+1)×n matrix L with rows L_1,...,L_(m+1), and the m×(m+1) successive-difference matrix ∂, so M=∂L. For any nonzero row vector t∈F2^m, put w=t∂∈F2^(m+1). The map t→w bijects F2^m with the EVEN-parity subspace of F2^(m+1), so w is nonzero of even Hamming weight at least two. The random row combination tM=wL is uniform on exactly the union of the EXTERIOR coordinate supports of windows j with w_j=1: for a coordinate i, it is the XOR of independent uniform coefficients from the selected rows whose free triples omit i, and random bits from different coordinates i are independent. If the intersection of the selected windows' free triple sets has size a, this union has size n−a, so
   P(tM=0)=2^(−(n−a)).
For two selected windows a distance1 apart, a=2; a distance2, a=1; distance>=3, a=0. For FOUR or more distinct selected windows, a=0 because any coordinate belongs to at most three consecutive length-three windows. There are exactly m weight-two supports at distance1 and m−1 at distance2; all remaining 2^m−1−(2m−1) nonzero even supports have exterior union size n.

Thus the EXPECTED number of nonzero vectors in ker(M^T) is exactly
 E(|ker(M^T)|−1)
  = m*2^(−(n−2)) + (m−1)*2^(−(n−1)) + (2^m−1−(2m−1))*2^(−n)
  = 1/8+(4n−14)/2^n.
If M is rank-deficient, its left kernel has at least one nonzero vector. Markov's inequality (or union bound) yields P(rank M<m) <= this expectation. The sequence is <=5/16 for n>=4, with equality of the BOUND at n=5 (directly check n=4 and n=5 and that (4n−14)/2^n decreases thereafter). QED.

**Scope.** This shows affine NORI counterexamples, if any, are not remotely generic: even a PRESCRIBED direction order has probability bounded far above one half of admitting a monochromatic full antipodal geodesic, uniformly in dimension, and tending to at least 7/8. This is a probability statement about a well-defined uniform ensemble of valid affine-exterior colorings, NOT proof that every coloring or every affine coloring has a good path. The full NORI grand conjecture is still open.

## Global sparse-slope stability around the full exterior-parity affine coloring

Let n>=4. Consider ANY binary coloring c of physical ordered three-faces of Q_n that is affine in the exterior cube bits, with arbitrary orientation-dependent intercepts. For each ordered triple \(\pi=(a,b,c)\) of distinct coordinates, write its exterior coefficient vector \(A_\pi=(a_{\pi,t})_{t\notin\operatorname{set}\pi}\). Let \(P_\pi\) be the full exterior-parity coefficient vector with ALL entries 1. Let
\[
\mathcal E=\{\pi:A_\pi\ne P_\pi\},\qquad M=|\mathcal E|\le n(n-1)(n-2).
\]
The intercept bits on all triples are unrestricted. Active NORI antipodal-reversal oddness may hold but is NOT REQUIRED for this result.

**Theorem (sparse affine perturbation closure).** There exists a full antipodal directed cube geodesic whose ordered-three-face window colors change at most
\[
\boxed{\left\lfloor\frac{M}{n(n-1)}\right\rfloor}
\]
times (with the trivial cap n-3 if desired). In particular:
- If M<n(n-1), there exists a FULL MONOCHROMATIC antipodal geodesic.
- If M<2n(n-1), there exists a full antipodal geodesic with AT MOST ONE window-color change, proving the active NORI conclusion for this affine class even without imposing its oddness axiom.

**Proof.** Choose a uniformly random permutation p=(p_1,...,p_n). A fixed ordered triple \pi appears as one of its n-2 consecutive three-direction windows with probability
\[
\frac{n-2}{n(n-1)(n-2)}=\frac1{n(n-1)}.
\]
Let K(p) count the windows whose ordered triples belong to \mathcal E. By linearity of expectation,
\[
\mathbb E K(p)=\frac{M}{n(n-1)}.
\]
Therefore SOME order p satisfies K(p)≤floor(M/[n(n-1)]).

For a fixed such p, write the n-2 ordered window colors as the affine vector C_p(x)=h_p+L_p x over F2, where x is the starting root. Let L_0 be the coefficient matrix for the parity-baseline coloring with slope 1 on every exterior coordinate (but the same arbitrary intercepts); L_p-L_0 has nonzero rows at no more than K(p) exceptional windows, so rank(L_p-L_0)≤K(p). Apply consecutive difference operator \partial to obtain the (n-3)×n change matrices M_p=\partial L_p and M_0=\partial L_0. The rows of M_0 are EXACTLY
\[
e_{p_i}+e_{p_{i+3}},\quad 1\le i\le n-3,
\]
because consecutive three-face exterior masks differ only in the exiting direction p_i and entering direction p_{i+3}. These rows form the edge-incidence vectors of three disjoint paths on the coordinate positions modulo 3 and are linearly independent; hence rank M_0=n-3.

By rank perturbation,
\[
\operatorname{rank}M_p\ge n-3-K(p).
\]
The affine syndrome theorem (also proven independently: for any affine map F2^n→F2^{n-3} with rank r, its affine image contains a vector of Hamming weight at most n-3-r) yields a root x for which the full p-geodesic has at most K(p) changes. Combined with the expectation bound, this proves the claimed floor(M/[n(n-1)]) bound and its two threshold corollaries. QED.

**Interpretation.** This is a structural all-dimension closure theorem: an affine NORI coloring may perturb an arbitrary set of up to roughly \(2n^2\) orientation-triple exterior slopes away from the uniform parity baseline and still MUST have a full one-switch antipodal geodesic. The proof has TWO independent ingredients: permutation averaging to avoid most exceptional ordered triples, and a full-rank three-residue incidence matrix on the remaining windows. It is a genuine subclass result, not a proof for arbitrary nonlinear or dense exceptional-slope NORI colorings.

These results solve broad affine and near-affine subclasses and quantify the exceptional linear ranks. They do not assert the unrestricted NORI theorem, where the exterior-bit dependence need not be affine.

## Nonlinear faults, exterior sensitivity and holonomy

For a six-direction word (a,b,c,d,e,f), the four window colors under two selected root-bit changes have the exact form (A(u), B, C, D(v)). The endpoint-control theorem specifies when these four symbols can be made to have at most one change. Separate affine change-map and nonlinear-tail theorems show how controlled exterior sensitivities yield genuine monochromatic or one-switch geodesics for the stated structured families.

The Fourier/exterior-chart Subsection develops local root interpolation, physical gluing and explicitly restricted computer-assisted results, without asserting unrestricted NORI3 closure. The signed exterior-bit holonomy obstruction to naively embedding a particular six-path forcing certificate has been migrated to a research note, where its complete certificate and exact scope remain available.

*Full Section composition: [source manuscript](nori_affine_sensitivity.md).*

### Six-move endpoint control and exterior-sensitivity rigidity

**Six-move endpoint square.** Let p=(a,b,c,d,e,f) be six distinct coordinate directions in Q_n (n≥6), and fix all starting bits other than those in directions c,d. The four consecutive ordered-three-face window colors have the form
(A(u), B, C, D(v)),
where u=x_d, v=x_c. Indeed the first window (a,b,c) ignores x_c, the last (d,e,f) ignores x_d, and the two middle windows (b,c,d) and (c,d,e) ignore both. This holds for arbitrary Boolean ordered-three-face colorings and arbitrary fixed coordinates outside the six-move block.

**Exact square criterion.** Put R_A={A(0),A(1)} and R_D={D(0),D(1)}. If B≠C, a choice of u,v has at most one color change precisely when B∈R_A and C∈R_D. If B=C, a choice has at most one change precisely when B∈R_A or C∈R_D. In particular, if both endpoint functions are nonconstant, independently choose A(u)=B and D(v)=C to produce (B,B,C,C), a one-change block.

**Theorem (dimension-six crossed sensitivity).** For n=6 fix any coordinate order (a,b,c,d,e,f). Assume the color of the ordered face (a,b,c) changes with its exterior coordinate d for at least one assignment of the other two exterior coordinates e,f, and the color of (d,e,f) changes with its exterior coordinate c for at least one assignment of its other two exterior coordinates a,b. Then a successful antipodal geodesic exists with exactly this order and at most one change. Proof: first sensitivity depends only on (x_e,x_f) and second only on (x_a,x_b); choose these disjoint sets of bits to witness both sensitivities simultaneously. The endpoint-square criterion supplies x_d and x_c. □

**Rigidity under fixed-order failure (n=6).** Write A=A(x_d,x_e,x_f), B=B(x_a,x_e,x_f), C=C(x_a,x_b,x_f), D=D(x_a,x_b,x_c). Suppose no choice of starting vertex works with order (a,b,c,d,e,f). Assume A(0,e_0,f_0)≠A(1,e_0,f_0) for some (e_0,f_0). For every x_a,x_b,x_c choose x_d so A=B. Failure of the resulting word (B,B,C,D) forces B≠C and D≠C, hence B=D=1⊕C. Holding e=e_0 and f=f_0 yields
B(x_a,e_0,f_0)=D(x_a,x_b,x_c)=1⊕C(x_a,x_b,f_0)
for every x_a,x_b,x_c. Since B ignores x_b and x_c, D is independent of x_b,x_c and C(.,.,f_0) is independent of x_b. In particular D cannot be sensitive in x_c. The mirror statement follows by reversing the four windows. This is a necessary structural restriction for any hypothetical dimension-six counterexample.

**Scope.** Crossed sensitivities provide local six-move control in larger dimensions, but concatenation into a full n-move geodesic requires compatible window colors outside the controlled block. Coordinate-only colorings have no exterior sensitivities and are not addressed by this argument.

## Recent consequences and compatibility conditions

Statement:
For an antipodally odd ordered-three-face coloring of Q_6, if there is an ordered coordinate triple (a,b,c) whose color is sensitive to each of the three fixed exterior coordinates d,e,f (sensitivity may occur at different exterior-bit assignments), then a good antipodal geodesic exists. Equivalently, in every counterexample each ordered triple has exterior Boolean-sensitivity support of size at most two. If a triple has sensitivity to two exterior coordinates, every orientation of its complementary free triple is face-independent.

Proof:
Assume every six-direction geodesic has at least two changes. Apply the antipodal endpoint-collapse theorem to sensitivity of (a,b,c) in d. There is K_d with c(def)=c(dfe)=K_d and c(fed)=c(efd)=1−K_d, all face-independent. Sensitivity in e yields K_e with c(edf)=c(efd)=K_e and c(fde)=c(dfe)=1−K_e; the overlap forces K_e=1−K_d, and the two conclusions together fix all six orientations of free set {d,e,f}. Consequently c(fde)=K_d while c(fed)=1−K_d. Sensitivity in f, however, would force c(fde)=c(fed) by the same endpoint-collapse theorem. Contradiction. The same argument applies under any relabeling and reversal; the witnesses to three sensitivities need not share the same outside-bit assignment.

Statement:
Assume an antipodal-reversal-odd coloring of Q_6 has no one-change antipodal geodesic. Let d,e,a,b,c,f be the six coordinates. If the ordered-triple color C_{abc} is sensitive to both fixed exterior bits d,e, then the four ordered triples (a,b,c), (f,a,b), (c,f,a), (b,c,f) are all independent of the remaining exterior bit in {a,b,c,f}, and, as functions of the two fixed bits d,e, their colors are respectively F, 1-F, F, 1-F for one Boolean function F(d,e) genuinely depending on both variables.

Proof:
By the two-junta theorem C_{abc}=F(x_d,x_e) is independent of x_f. The complementary ordered triples (d,e,f) and (e,d,f) are face-independent and opposite-colored, because the color on the complementary triple is determined by which of d,e comes first. Compare full six-step orders (d,e,f,a,b,c) and (e,d,f,a,b,c), starting at the same cube vertex. Their first window colors are opposite; their third window has identical ordered free axes (f,a,b) and the same exterior fixed bits (d and e have both been traversed), and their fourth window is also identical (a,b,c) with the same exterior bits. Write the two words as (0,B,C,D) and (1,B',C,D), after possibly exchanging 0 and 1. If C=D, whichever order has first color 1-C gives a word (1-C,*,C,C), which necessarily has at most one change. Therefore global failure forces C≠D at every starting vertex. The third window is C_{fab}, depending on exterior coordinates {c,d,e}; the fourth is C_{abc}, depending on {d,e,f}. Their d,e exterior bits agree after traversing the common initial block {d,e,f}, whereas their remaining exterior bits x_c and x_f range independently. Hence C_{fab}(z_d,z_e,z_c)=1-C_{abc}(z_d,z_e,z_f) for every choice of these bits. Both color functions are independent of their respective leftover exterior coordinate and F_{fab}=1-F_{abc} on d,e. Thus C_{fab} is also sensitive in both d and e. Apply the same argument to C_{fab}, whose fourth coordinate among {a,b,c,f} is c, to conclude C_{cfa}=1-C_{fab}=F_{abc}; then apply it to C_{cfa} with fourth coordinate b to conclude C_{bcf}=1-C_{cfa}=1-F_{abc}. This yields the alternating four-cycle.

### Arbitrary nonlinear-coordinate faults and robust affine closure

# Arbitrary nonlinear-coordinate faults and robust affine closure

Begin with the exterior-parity coloring, where the root recurrence yields many monochromatic full paths for any chosen direction order. Modify the coloring arbitrarily on ordered three-faces involving a small exceptional coordinate set, while maintaining the antipodal-reversal axiom. The essential point is that clean directions remain controllable and terminal fault windows can sometimes be polarized using spare root bits.

THEOREM (TWO ARBITRARY NONLINEAR TERMINAL WINDOWS). Let r>=2 and n>=r+2. Fix a coordinate permutation p=(p1,...,pn). Let c0 be a coloring of ordered physical r-faces whose n-r consecutive change bits along p are an affine SURJECTION of the starting root x∈F2^n; e.g. the common exterior-parity coloring c0(F,pi)=h(pi)+sum_(i outside pi) z_i (mod2). Assume also that flipping the root bit p_(n-1) complements EVERY ONE of the first L-2 baseline window colors, where L=n-r+1 is the full window-word length (true for that common all-one exterior-parity coloring).

Let c be ANY other ordered physical r-face coloring, with arbitrary NONLINEAR exterior dependence, agreeing with c0 on the FIRST L-2 ordered-window types along p, for all exterior assignments. Its LAST TWO window types are completely unrestricted. Then AT LEAST 2^(r+1) starting roots produce full antipodal p-geodesics of c having at most ONE color change. For active NORI (r=3) this is AT LEAST SIXTEEN good full geodesics from distinct roots along the same order.

PROOF. Onto-ness of the baseline change map means precisely 2^(r+2) roots x have the first L-2 baseline window colors all equal (vanishing first L-3 differences). Call this set G. Their corresponding actual c prefix colors are q(x) repeated L-2 times. Let T(x)=x xor e_(p_(n-1)). This direction is absent from ALL the first L-2 free-coordinate r-tuples (they end at p_(n-2)), so in the all-one exterior-parity baseline it complements all early window colors. Thus T(G)=G and q(Tx)=1-q(x). By contrast p_(n-1) is among the free directions of BOTH LAST TWO ordered r-windows: their direction position intervals are [n-r,n-1] and [n-r+1,n]. Flipping its root bit therefore NEVER changes either of their actual physical face colors, irrespective of how nonlinearly those colors depend on the OTHER exterior bits. Write their common colors as u,v for both x and Tx.

The two actual full window words are q^(L-2),u,v and (1-q)^(L-2),u,v. If u=v both have <=1 change. If u!=v, choose the root whose prefix bit equals u; then only the final transition u->v changes. Therefore each fixed-point-free T-pair in G includes a good root, establishing 2^(r+1) good roots. QED.

COROLLARY (TWO UNCONTROLLED COORDINATES). For any designated coordinate pair {a,b}, an arbitrary nonlinear change to ALL ordered physical three-face colors whose free direction triple intersects {a,b} cannot defeat the one-switch grand NORI conclusion if the coloring retains a common all-one exterior-parity form on every triple avoiding {a,b}. Put a,b as the FINAL TWO directions; only the final two consecutive ordered-three-face windows can deviate from the parity reference. The proof yields at least16 good roots. A NORI antipodal-reversal-odd choice of the arbitrary exceptions is allowed.

GENERALITY: The first assumption is onto-ness of the reference change map and a fresh-coordinate flip symmetry, not affine behavior of the two exceptional window colors. This advances the previous single arbitrary-window fault theorem to TWO consecutive terminal faults; the same argument does not control three arbitrary trailing windows, which may themselves have two color changes. It is a dimension-independent scoped closure theorem, not a universal proof of the grand conjecture.

## An exact root-chart connectivity extraction theorem for three arbitrary nonlinear NORI fault directions

Fix n>=8, an active NORI coloring C, and a three-element direction set K⊂[n]; write D=[n]\K, m=|D|>=5. Assume the ordered-three-face colors whose free coordinate triples lie ENTIRELY in D agree on every exterior assignment with some full exterior-parity AFFINE reference
\[
C(F,(i,j,k))=h(i,j,k)+\bigoplus_{s\notin\{i,j,k\}} z_s(F),
\quad i,j,k\in D.
\]
The intercept h on ordered triples in D may be arbitrary, subject to h(k,j,i)=h(i,j,k)+1+(n-3 mod2) in order to preserve the active NORI oddness law. The coloring on all ordered triples MEETING K is completely arbitrary nonlinear, subject only to the active NORI condition.

For each outside order p=(p_1,...,p_m), let G_p⊆F2^D be the 8-element affine root-code cut out by the zero early-window changes
\[
S_{p_{j+3}}=S_{p_j}\oplus1\oplus h(p_j,p_{j+1},p_{j+2})
\oplus h(p_{j+1},p_{j+2},p_{j+3}),
\quad j=1,...,m-3.
\]
Let G=union_p G_p. Every G_p and hence G is invariant under complement S↦bar S.

Define the entirely explicit **physical first-exceptional-face chart graph** Z_h on vertex set G, connecting S,S' if there exist outside permutations p,p' with S∈G_p, S'∈G_p', such that
- their last ordered coordinate pairs (p_{m−1},p_m)=(p'_{m−1},p'_m)=(u,v) agree, and
- S,S' agree on every outside coordinate outside {u,v}.
These conditions exactly say that the first exceptional physical ordered-three-face with free directions (u,v,a) after the outside prefix is IDENTICAL for S and S', for any fixed a∈K and any common K-root bits.

**THEOREM (antipodal chart connection forces GRAND NORI closure).** If ANY connected component of Z_h contains both S and bar S, then the full active NORI grand conjecture holds for C: a full antipodal one-switch geodesic exists. In particular, if Z_h is connected and nonempty, closure holds.

**PROOF.** Suppose no full good antipodal geodesic exists. On each G_p, the existing exact three-terminal-window obstruction, compared across all SIX permutations of K and then under the active antipodal reversal, implies the existence of a UNIQUE bit t(S), independent of p, the initial K-bits and the ordered terminal K-permutation, such that the last three full-window colors are (t(S),1−t(S),t(S)). The value t(S) is the common color of every orientation of the final physical K-face, whose exterior D-coordinate bits are bar S. This makes t globally well-defined on G, independent of which p witnesses S. Physical reversal-oddness gives t(bar S)=1−t(S). For every chart edge SS', the relevant FIRST exceptional physical ordered face is literally the same, so its color t(S) must equal its color t(S'). Consequently t is constant on each connected component of Z_h. A component containing S and bar S would require t(S)=t(bar S)=1−t(S), impossible. Therefore any such chart self-connection forces grand closure. QED.

**Nature of the remaining forcing theorem.** The result converts a whole **NONLINEAR** active NORI subclass into a purely finite graph-connectivity problem Z_h depending ONLY on the AFFINE REFERENCE intercept h on the unexceptional ordered triples. Colors of all exceptional ordered three-faces do NOT affect this graph. This is a concrete realization of the user's original reachability-label strategy: actual monochromatic-prefix root charts are glued only where their physical last-two-direction face certificates agree, and a topologically forced antipodal self-connection yields the full one-switch witness via an exact extraction theorem.

**Known closure instance.** When n is even and h≡0 (more generally h≡constant or h(i,j,k)=q+η_i+η_j+η_k), the cyclic-three-chain template yields an antipodally connected chart graph in every dimension n>=8. This has been fully proved separately in Item nori_even_dimension_three_arbitrary_nonlinear_coordinate_faults_full_grand_closure_20261008. Empirical finite checks are NOT a proof of chart connectivity for arbitrary allowed h; no such universal assertion is made here. The unrestricted grand conjecture remains open.

## A sharp structural obstruction to completing NORI by sparse-fault clean-prefix charts alone

Fix a distinguished three-coordinate set K⊂[n], let D=[n]\K of size m=n−3>=3, and let \mathscr T be the set of unordered triples of directions inside D on which a proposed clean full-exterior-parity reference MAY fail. The recent robust-root-chart closure results construct actual monochromatic-prefix witness charts ONLY from direction permutations p of D whose every consecutive 3-direction window avoids \mathscr T.

**THEOREM (one-coordinate star destroys every clean full prefix).** Fix ANY direction t∈D, and put
\[
\mathscr T_t=\{T\in\binom D3:t\in T\}.
\]
Then \(|\mathscr T_t|=\binom{m-1}{2}=\Theta(m^2)\). EVERY permutation p=(p_1,...,p_m) of D contains AT LEAST ONE consecutive 3-direction window whose unordered direction set belongs to \mathscr T_t. Consequently there are NO admissible clean-prefix order charts if one insists on avoiding all triples in \mathscr T_t, regardless of the color values, physical faces, or NORI antipodal-reversal law.

**Proof.** The distinguished direction t appears at some position j of the permutation. Because m>=3, at least one consecutive block of three positions contains j (choose the first block if j<=3, the last block if j>=m−2, and any containing block otherwise). That consecutive three-direction set contains t, and so belongs to \mathscr T_t. Since every p has such a window, no clean avoiding permutation exists. The number of forbidden unordered triples is exactly \binom{m-1}{2}. QED.

**THEOREM (single-root-bit polarization stops at exactly r exceptional terminal windows).** More generally, in the ordered-r-face model, appending k exceptional coordinate directions to a clean prefix gives k exceptional r-windows. One of those exceptional directions belongs to ALL k free coordinate sets IF AND ONLY IF k<=r. For k>=r+1 the first and last exceptional windows have DISJOINT exceptional-direction sets. For active NORI r=3, toggling one exceptional root bit can preserve every exceptional suffix window at once when k<=3, but not k>=4. This is the already proved terminal-common-free-coordinate theorem nori_suffix_polarization_terminal_r_window_common_free_direction_sharp_threshold_20261008.

**CONCLUSION (method barrier, NOT conjecture counterexample).** These two elementary facts show why the recent O(n²) arbitrary-fault robustness cannot be promoted to unrestricted NORI merely by tightening the random-order avoidance bound: an explicit O(n²)-size forbidden family blocks ALL clean order witnesses. Furthermore, folding that fourth problematic direction into K and attempting the same single-root-bit suffix-polarization proof fails at exactly four exceptional windows. The *grand conjecture itself* is not contradicted. But unrestricted closure needs genuinely NEW machinery: (i) actual reachability/terminal-memory charts that traverse non-reference windows rather than avoiding them, (ii) a multi-bit or root-mobile polarization allowing four or more exceptional windows, or (iii) a direct topological forcing theorem for exact complementary reversed-tail label intersections with no parity normal form.

**Research priority.** Treat 'extend quadratic r' and 'remove parity reference' as qualitatively different problems. The first cannot logically settle the second. Aim instead at the general NORI exact color-free reversed-tail reachability sets R_J(x), preserving ordered two-direction memory, and force R_(a,b)(x) ∩ complement_D(R_(b,a)(x)) nonempty for some root x.

The rigorous closure theorems apply to the stated number and location of arbitrary faults; sharp obstruction constructions show why the same argument cannot simply be iterated to cover unrestricted colorings.

### Exterior face charts and Fourier transport

# Exterior-face charts: exact root repair and its limits

In a legal physical ordered-three-face coloring, fixed exterior coordinates cannot be suppressed without proof. This subsection combines a general Boolean root-interpolation lemma, a seam triangularization mechanism, and a deliberately restricted computer-assisted higher-dimensional test. The restricted theorem is not claimed for arbitrary exterior dependence.

## Acyclic pivotal matching and root interpolation

Theorem (acyclic Boolean pivot matching). Fix any dimension n>=4, order p, rooted window colors w_i(x), and seam bits d_i=w_i+w_(i+1), i in [m], m=n-3. For a Boolean function f write Delta_j f(x)=f(x)+f(x+e_j). Select a set I of seam indices and injectively assign distinct root coordinates rho(i) to i in I. Assume Delta_(rho(i)) d_i = 1 at every root. Form a directed graph on I with arc j to i (j!=i) whenever d_i depends on x_(rho(j)); equivalently Delta_(rho(j))d_i is not identically zero. If this graph is acyclic, then for ANY target seam values t_i at i in I, exactly 2^(n-|I|) roots realize d_i=t_i simultaneously. In particular, min_root switches <= m-|I|. If |I|>=m-1, a full one-switch antipodal geodesic exists.

Proof. Choose the n-|I| unused root bits arbitrarily. Process seam indices in topological order of the directed graph. On processing i, every other pivotal coordinate influencing d_i has already been assigned, because a missing arc means the corresponding Boolean derivative vanishes identically. The pivotal coordinate rho(i) toggles d_i for every choice of other bits, hence there is exactly one value making d_i=t_i. Later choices preserve previous equations. Counting the free root bits gives 2^(n-|I|) roots.

Feedback-set corollary. If removing B from the pivotal dependency graph makes it acyclic, the same reasoning on I\B gives exactly 2^(n-|I|+|B|) roots satisfying all retained seam equations and at most m-|I|+|B| changes. Define alpha(p) as the maximum number of seams admitting an acyclic pivotal matching. Any putative NORI counterexample must obey alpha(p)<=n-5 for every full direction order p. The physical-face condition guarantees w_i are true faces; the proof needs no oddness assumption.

Extension: right-triangular seam interpolation (Item nori_order_local_boolean_seam_triangularization_dimension_independent_20261009) is the case rho(i)=p_(i+3), whose dependency arcs point forward. This result allows arbitrary pivotal coordinates and arbitrary nonlinear lower-order dependencies.

Abstract sharpness example: d_1=u+v and d_2=1+u+v have global unit derivatives in each variable. Assigning distinct pivots yields a directed two-cycle, and the equations d_1=d_2=0 are inconsistent; exactly one of them can vanish. This example is a statement about arbitrary Boolean seam systems and makes no claim of NORI realizability.

Open obligation: Find an all-but-one acyclic pivotal matching (or a fiberwise nonlinear substitute) in at least one genuine full direction order of each legal coloring.

## Local seam triangularization

# Dimension-independent nonlinear seam triangularization and exact root multiplicity

Let n>=4 and c be ANY binary coloring of physical ordered three-faces of Q_n (the NORI antipodal law may additionally hold). Fix a full direction order p=(p_1,...,p_n). Let w_i(x) denote its actual physical ordered-three-face color at starting cube root x, for 1<=i<=n-2. Put d_i(x)=w_i(x)+w_(i+1)(x) over F_2 for 1<=i<=m=n-3. For any Boolean function f of cube-root bits, define its Boolean difference Δ_j f(x)=f(x)+f(x+e_j).

Call seam i RIGHT-TRIANGULAR when BOTH identities hold at every cube root:
(1) Δ_(p_(i+3)) d_i ≡ 1;
(2) Δ_(p_j) d_i ≡ 0 for all j>i+3.
These hypotheses are physical-face local: (1) is exactly Δ_(p_(i+3)) w_i≡1, since p_(i+3) belongs to the second free triple; (2) says that the two adjacent actual faces have identical exterior-bit derivatives in every still-future direction p_j, j>i+3. Those common derivatives may be arbitrary nonlinear functions of other root coordinates.

THEOREM (nonlinear seam-defect bound and exact multiplicity). Let B be ANY set of seam indices containing every seam that is not right-triangular. For every assignment of the first three root bits and every requested t_i∈F_2 for i∉B, there are EXACTLY 2^|B| completions of the remaining root bits satisfying d_i(x)=t_i at every i∉B. Consequently an actual antipodal full geodesic of direction order p exists with at most |B| changes. More precisely, among the 2^n possible initial roots, exactly 2^(3+|B|) satisfy d_i=0 for all i∉B. If B=∅, every seam word in F_2^(n-3) occurs at exactly eight roots and there are eight monochromatic full geodesics of this fixed direction order. If |B|=1, at least sixteen starting roots yield a full one-change geodesic.

PROOF. Choose x_(p_1),x_(p_2),x_(p_3) arbitrarily, and process i=1,...,m. If i∈B, choose x_(p_(i+3)) freely. If i∉B, condition (2) says d_i is independent of every as-yet-unassigned bit x_(p_j), j>i+3. Condition (1) says toggling the current bit x_(p_(i+3)) toggles d_i, for every setting of already fixed bits. Exactly one choice attains d_i=t_i. Subsequent choices cannot modify a previously solved nonexceptional seam by (2). Conversely each permissible assignment must choose these same forced pivot bits. Hence there are precisely 2^|B| completions per initial triple and 2^(3+|B|) total. Setting all prescribed t_i=0 leaves changes only at seams in B. QED.

COROLLARY (counterexample obstruction). Any counterexample to full NORI must have at least TWO non-right-triangular seams for EVERY full direction order p. Thus every order must encounter at least two failures of pointwise entering-direction flip or two-face future-derivative agreement, counted jointly.

NONLINEAR, NO-GLOBAL-FLIPPER EXAMPLES. For an arbitrary order p and arbitrary Boolean maps G_i on i-1 variables, prescribe on ordered triple (p_i,p_(i+1),p_(i+2)) the face color c_i(z)=Σ_(j=i+3)^n z_(p_j)+G_i(z_(p_1),...,z_(p_(i-1))), with z denoting its fixed exterior coordinates. Prescribe reversed triples by the antipodal-reversal-odd law, and all other ordered triple types arbitrarily subject to that law. Along the genuine rooted full path of order p, the prefix exterior coordinates have been toggled and the suffix exterior coordinates have not; therefore w_i(x)=Σ_(j=i+3)^n x_(p_j)+G_i(1+x_(p_1),...,1+x_(p_(i-1))). It follows that d_i(x)=x_(p_(i+3))+G_i(prefix_(i-1))+G_(i+1)(prefix_i). Every seam is right-triangular regardless of the Boolean degrees of G_i. For n>=7, the unused triple types can be colored independently of a selected exterior coordinate for each direction, so this family can be chosen with NO universal exterior flipper. The result therefore supplies an all-dimensional, genuinely nonlinear, order-local root-control criterion strictly broader than relying on globally uniform exterior flippers.

LIMIT. The right-triangular hypotheses are sufficient local certificates, not consequences of antipodal oddness. The unrestricted grand conjecture remains open. The new closure target is to force an order with at most one defective seam, or find a weaker global replacement for the pointwise future-derivative agreement.

## Exact Q8 one-sentinel physical-face theorem (computer-assisted)

THEOREM (complete Q8 closure with one genuine exterior coordinate; computer-assisted). Let c color the PHYSICAL ORDERED three-faces of Q8, obeying c(bar F,reverse pi)=1-c(F,pi). Fix one distinguished direction t. Assume that for each ordered free triple pi the face color depends on its exterior fixed bits only through the bit x_t when t is NOT in pi; when t is free, its color depends on no exterior bit. Then some full antipodal eight-geodesic has a window-color word with at most one change. The assumption allows genuine face-position dependence, so this strictly extends coordinate-only Q8 closure.

MATHEMATICAL REDUCTION. Relabel t=7 and V={0,...,6}. For all ordered triples pi on V let H(pi)=c(F,pi) at t-exterior bit 0 (the other exterior bits are immaterial). The antipodal-reversal law forces color at t-bit 1 to equal 1-H(reverse pi). H is an ARBITRARY 210-bit ordered-triple coloring; NO reversal-oddness of H is assumed. For ordered triples pi containing 7, denote their position-independent labels by G(pi); then G(reverse pi)=1-G(pi), contributing exactly 63 Boolean variables. There are 210+63=273 independent Boolean variables.

For a full eight-direction order p and a starting sentinel bit b, let j=position of 7 in p. For window index i with ordered triple pi=p[i:i+3]: if 7 lies inside pi its color is G(pi); otherwise its color is H(pi) for b XOR [j<i]=0, and 1-H(reverse pi) for b XOR [j<i]=1. Every other starting-root bit is immaterial. The full window word has six bits. Forbid each of the twelve binary words with zero or one color change by one six-literal clause OR_i(window_i != target_i). Reversing p at the SAME root sends its word to the complement of the reversed word by the physical NORI law; hence it suffices to inspect half of all 8-permutations, for both sentinel-root bits, giving (8!/2)*2*12=483840 clauses.

A DICHOTOMY ON THE CHART H is exhaustive.
Case I. H has a monochromatic tight directed five-path on five distinct vertices of V. By relabeling V and globally flipping all colors, normalize H(012)=H(123)=H(234)=0. Add these three unit clauses. The full 273-variable CNF with the 483840 badness clauses is UNSAT (libz3.so.4).
Case II. H has NO monochromatic tight directed five-path. For each ordered five-tuple q in V, forbid both H(q0q1q2)=H(q1q2q3)=H(q2q3q4)=0 and the analogous all-1 assignment. These are 2*7P5=5040 three-literal clauses. With the same full 483840 badness clauses the 273-variable CNF is UNSAT (libz3.so.4).
Thus a hypothetical coloring with no good full Q8 geodesic lies in neither exhaustive case; contradiction.

REPRODUCIBLE REFERENCE CHECKER (Python 3 with z3-solver):
from itertools import permutations
from z3 import Bool,Not,Or,Solver,unsat
V=range(8); t=7; W=list(permutations(V,3))
H={q:Bool('H'+''.join(map(str,q))) for q in W if t not in q}
G={}
for q in W:
    if t in q and q not in G:
        a=Bool('G'+''.join(map(str,q)))
        G[q]=a; G[q[::-1]]=Not(a)
assert len(H)==210 and len(G)==126
def h(q,b):
    if t in q:return G[q]
    return H[q] if b==0 else Not(H[q[::-1]])
good={tuple([a]*j+[1-a]*(6-j)) for a in (0,1) for j in range(7)}
assert len(good)==12
for case in (0,1):
    S=Solver()
    if case==0:
        for i in range(3):S.add(Not(H[tuple(range(i,i+3))]))
    else:
        for q in permutations(range(7),5):
            w=[H[q[i:i+3]] for i in range(3)]
            S.add(Or(*w));S.add(Or(*(Not(a) for a in w)))
    for p in permutations(V):
        if p>p[::-1]:continue
        loc=p.index(t)
        for b in (0,1):
            w=[h(p[i:i+3],b^(loc<i)) for i in range(6)]
            for g in good:
                S.add(Or(*(w[i] if g[i]==0 else Not(w[i]) for i in range(6))))
    assert S.check()==unsat
Executed with direct ctypes calls to the system Z3 C library on 2026-10-09: Case I UNSAT in 9.84 s; Case II UNSAT in 7.87 s, each with 273 variables and 483840 six-literal no-good clauses. A separate SAT tactic independently rechecked Case I UNSAT (~10.35 s).

IMPORTANT SCOPE. The theorem is a special FACE-DEPENDENT rank-eight case and therefore a strictly stronger bridge than coordinate-only Q8. It does not establish full physical Q8 or all-dimensional NORI, because a generic ordered-face color can depend on five independent exterior bits. Any all-dimension upgrade must control multiple exterior coordinates simultaneously. A two-sentinel extension was formulated with 438 variables and 967680 no-good clauses; initial SAT solving did not finish. This identifies a natural next bridge between coordinate-only combinatorics and the full physical geometry. Request independent certificate audit before elevating to a publication composition.

## Interpretation and remaining obligation

The Boolean matching and seam arguments permit local control where their exact pivot and support hypotheses hold. The Q8 SAT statement assumes a single globally distinguished exterior coordinate; it is **not** unrestricted dimension-eight closure and supplies no induction by itself. Extending these constructions would require a dimension-uniform choice of compatible physical roots and seam windows despite general nonlinear dependence on all exterior coordinates.
