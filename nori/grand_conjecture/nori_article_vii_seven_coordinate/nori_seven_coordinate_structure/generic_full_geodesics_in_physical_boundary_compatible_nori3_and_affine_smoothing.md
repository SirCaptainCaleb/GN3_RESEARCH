# Generic full geodesics in physical boundary-compatible NORI3 and affine smoothing

# Generic full monochromatic geodesics in physical boundary-compatible NORI3

## Statement and distinction from the deterministic conjecture

A boundary-compatible NORI3 coloring on physical ordered 3-faces of Q_n satisfies BOTH
\[
c(F,(w,v,u))=1-c(F,(u,v,w)),\qquad c(\bar F,(u,v,w))=c(F,(u,v,w)).
\tag{BC}
\]
These imply the ordinary antipodal-reversal NORI law; colors are functions of genuine physical exterior fixed bits, independent of traversing corners.

**Theorem A (uniform nonlinear model).** Sample uniformly from ALL legal boundary-compatible physical ordered-three-face colorings (BC): for each unordered free triple T, each of its three reversal pairs of orders, and each antipodal pair of exterior bit assignments, choose one independent fair bit, extending by BC. For n>=20 and every FIXED prescribed binary word w of length n-2,
\[
\Pr[\exists\text{ full antipodal geodesic of window word }w]\ge1-2^{-\varphi(n)/2}.
\tag{A1}
\]
A stronger bound, where \(D_n=\binom n1+\binom n2+\binom n3\), is
\[
\Pr[\text{no full geodesic has word }w]
\le\exp\{-\varphi(n)[1-\tfrac14D_n2^{6-n}]\}.
\tag{A2}
\]
Thus a uniformly random legal boundary-compatible physical coloring has a COMPLETELY MONOCHROMATIC FULL geodesic with probability 1-o(1), allowing arbitrary nonlinear dependence on every exterior coordinate.

**Corollary A3 (all-word universality for prime n).** For prime n tending to infinity, a uniformly random legal boundary-compatible physical coloring, with probability \(1-o(1)\), realizes EVERY one of the \(2^{n-2}\) possible binary window words on full antipodal geodesics. The realizing direction order and starting root may depend on the word.

**Theorem B (adversarial-base affine smoothing).** Fix ANY direction-only boundary 3-tournament \(b(u,v,w)=1-b(w,v,u)\). For every unordered direction triple T and reversal pair of orders choose independently a uniform even-parity vector \(A_{T,\mathrm{orbit}}\) supported on exterior coordinates \(V\setminus T\), using the same vector on reversed orders. Define the real physical face color
\[
c(F,\pi)=b(\pi)\oplus\langle A_{T,\mathrm{orbit}(\pi)},z(F)\rangle.
\tag{B1}
\]
This is legal BC for every choice of the vectors. For n>=15, with probability at least \(1-(0.55)^{\varphi(n)/2}\), there exists ONE complete direction order p such that as the initial cube root x varies, its actual ordered three-face word attains every one of the \(2^{n-2}\) binary words, each by EXACTLY FOUR initial vertices (two antipodal root pairs). This remains true for every adversarial choice of the base boundary tournament b.

No theorem here claims the deterministic square-root lower bound for EVERY exterior-dependent boundary-compatible coloring. The Devine–Milans terminal-pair snake guarantees the square-root bound for ordinary direction-only boundary tournaments; our new results establish that generic exterior dependence, however global, is not itself an obstruction.

## Lemma: independent arithmetic-progression full direction orders

Let n>=5, and for each unit a of Z/nZ set
\[
p^{(a)}=(0,a,2a,\ldots,(n-1)a)\pmod n.
\]
This is a permutation of ALL n cube coordinate directions. Its n-2 consecutive unordered triple windows are three-term arithmetic progressions \(\{j a,(j+1)a,(j+2)a\}\), whose common step is \(\pm a\). Such a three-element set has a UNIQUE middle vertex for a unit a: if a second vertex were its arithmetic midpoint, then \(3a=0\pmod n\), impossible for n>3 when a is a unit. Thus progressions arising from \(p^{(a)}\) and \(p^{(b)}\) can coincide as unordered triples only when \(a=\pm b\pmod n\). Choose one representative a from each pair \(\{a,-a\}\) of units. We obtain \(K=\varphi(n)/2\) FULL direction orders whose unordered consecutive-triple sets are PAIRWISE DISJOINT. In either of our random models, events depending on the face data of these respective orders are consequently independent.

## Proof of Theorem A: complete physical-face second moment and Janson bound

Fix one full direction order p and one target word w of m=n-2 bits. Starting at a cube vertex x and traversing the n distinct directions in p order gives a true full antipodal geodesic. Because of BC antipodal invariance, starts x and \(\bar x\) give IDENTICAL window words in the same order p. Select one representative x from each of the \(M=2^{n-1}\) antipodal root pairs.

For each such x, let \(I_x\) indicate that its full geodesic has word w. Distinct window positions use distinct unordered triples, so their sampled physical face-orbit bits are independent. Therefore
\[
\Pr(I_x=1)=2^{-m},\qquad Z=\sum_xI_x,\qquad \mathbb EZ=M2^{-m}=2.
\tag{A4}
\]
For two different root orbits x,y, write \(\delta=x\oplus y\). At window T_i, both roots query the SAME independent underlying face-orbit bit exactly when their exterior assignments agree or are complementary:
\[
\operatorname{supp}(\delta)\subseteq T_i
\quad\text{or}\quad
\operatorname{supp}(\bar\delta)\subseteq T_i.
\tag{A5}
\]
Let t(delta) count such windows. Since the two roots request the same prescribed word w, all shared requirements agree. Independence over distinct free triples yields
\[
\Pr(I_x=I_y=1)=2^{-2m+t(\delta)}.
\tag{A6}
\]
For distinct antipodal root pairs neither delta nor its complement is empty. If both supports have size >=4, t=0; otherwise only triple windows containing the support of at most three directions can match. Any one, two, or three fixed distinct coordinate directions belong together to at most three, two, or one sliding triple windows, respectively. Hence t<=3. For any x, there are at most \(D_n=\sum_{j=1}^{3}\binom nj\) other antipodal root pairs with t>0.

Thus
\[
\mathbb EZ^2
\le2+M(M-1)2^{-2m}+7MD_n2^{-2m}
<6+7D_n2^{3-n}<8\quad(n\ge20).
\tag{A7}
\]
By the second-moment inequality \(\Pr(Z>0)\ge(\mathbb EZ)^2/\mathbb EZ^2\ge1/2\). For each of the K arithmetic-progression orders above, this event uses an entirely disjoint collection of independent random triple variables. The K success events are independent, giving
\[
\Pr[\text{word w not realized by any of them}]\le(1/2)^K,
\]
proving (A1).

For the stronger bound, for this fixed order p and target w, recode each orbit bit as a Bernoulli SUCCESS variable for receiving the corresponding target w_i. This is well defined because each unordered triple appears at only one window, and different orbit bits are independent. The root event \(I_x\) is the increasing event that a specified subset of m independent fair success variables are ALL 1. Apply the standard Janson inequality for increasing subgraph/cylinder events: \(\Pr(Z=0)\le\exp(-\mu+\Delta/2)\), where \(\mu=\mathbb EZ=2\) and \(\Delta\) is the sum over ordered distinct dependent root pairs of their joint probabilities. Using (A5)–(A6), the at-most-D_n dependencies per root pair and t<=3 give
\[
\Delta\le M D_n2^{-2m+3}=D_n2^{6-n}.
\tag{A8}
\]
Consequently
\[
\Pr(Z=0)\le\exp[-2+\tfrac12D_n2^{6-n}].
\]
Raise this bound to the K independent full-order trials to obtain (A2). If n is prime, \(\varphi(n)=n-1\). The union bound over ALL \(2^{n-2}\) prescribed words gives
\[
\Pr[\exists\text{ unrealized word}]
\le 2^{n-2}\exp[-(n-1)(1-o(1))]
=\exp[-(1-\ln2-o(1))n]\to0,
\]
proving Corollary A3. All root and face comparisons here use ACTUAL physical exterior assignments and their precise antipodal identifications; the paths always use n distinct coordinates.

## Proof of Theorem B: root-map surjectivity and generic affine row rank

For each ordered face, reversing its free tuple flips the boundary-tournament base bit b but preserves the affine coefficient vector, and complementing its exterior bits leaves the affine correction unchanged because the vector has even parity. Hence (B1) satisfies BC on every physical ordered face.

Fix a full direction permutation \(p_1,\ldots,p_n\), with m=n-2 windows. Let \(T_i=\{p_i,p_{i+1},p_{i+2}\}\). Extend the random exterior coefficient vector for its ordered window by zero coordinates on T_i and call it \(A_i\in\mathbb F_2^n\). Its physical face exterior at step i is \(x\oplus1_{\{p_1,\ldots,p_{i-1}\}}\) outside T_i, when starting at cube root x. Therefore the COMPLETE actual ordered-face word equals
\[
W_p(x)=Ax\oplus\gamma,\quad A=(A_1;\ldots;A_m),\quad
\gamma_i=b(p_i,p_{i+1},p_{i+2})\oplus\langle A_i,1_{\{p_1,\ldots,p_{i-1}\}}\rangle.
\tag{B2}
\]
If A has row rank m, the map \(x\mapsto W_p(x)\) is surjective onto \(\mathbb F_2^m\), so EVERY target word is obtained at exactly \(2^{n-m}=4\) roots. Since A has even-weight rows, those roots form two antipodal pairs. This property does not depend on the chosen base tournament b.

For fixed p, the m independent rows \(A_i\) are uniform on subspaces
\[
H_i=\{u\in\mathbb F_2^n:u|_{T_i}=0,\ \sum_j u_j=0\},\quad\dim H_i=n-4.
\]
Let E be the even-parity hyperplane, \(\dim E=n-1\). For \(|i-j|\ge3\), the sliding triples T_i,T_j are disjoint, and for n>=7 a coordinate remains outside their union. Duality yields \(H_i+H_j=E\): indeed \(H_i^\perp=\operatorname{span}(1,e_{p_i},e_{p_{i+1}},e_{p_{i+2}})\), and the orthogonal spaces for two disjoint triples intersect precisely in \(\operatorname{span}(1)\).

For nonempty J⊆{1,...,m}, the XOR \(\bigoplus_{i\in J}A_i\) is uniform on \(\sum_{i\in J}H_i\). If J has two indices distance >=3, the sum is uniform on E, so the probability of zero is \(2^{-(n-1)}\). Otherwise J lies in some three consecutive index positions; there are at most 4m such J, and their probability of zero is at most \(2^{-(n-4)}\) since at least one \(H_i\) is present. Taking a union bound over all possible nontrivial row dependencies gives
\[
\Pr(\operatorname{rank}A<m)
\le2^m2^{-(n-1)}+4m2^{-(n-4)}
=\tfrac12+4(n-2)2^{-(n-4)}<0.55\quad(n\ge15).
\tag{B3}
\]
So the full-rank probability for ANY fixed full direction order is greater than 0.45. The K=φ(n)/2 arithmetic-progression orders above use disjoint unordered triples and hence independent coefficient vectors. Their row-full-rank events are independent. All fail with probability less than \(0.55^K\). On the complementary event, at least one order realizes ALL window words with exactly four roots each by (B2). This proves Theorem B.

## Relation to established work and open frontier

The deterministic affine change-vector and syndrome framework, including exact root counts and a corank-at-most-one guarantee for one-switch words, already appears in the earlier NORI Subsection *Exact change-vector fibers and affine obstruction certificates*. It is NOT claimed as an original theorem here. This manuscript's distinct contributions are the independent arithmetic-progression full-order packing, the physical antipodal-orbit second moment/Janson results for arbitrary nonlinear BC colorings, and the quantitative adversarial-base random-affine smoothing theorem.

Devine–Milans (supplied *Scrapbook*, “Antisymmetric Tournaments”) proves EVERY ordinary direction-only boundary 3-tournament has a simple positive tight path of order at least \(1+\sqrt{(n-1)/2}\). The fully exterior-dependent physical BC class is larger, and its universal deterministic square-root guarantee is not established by the present results. In particular, random full-geodesic existence does NOT imply existence in adversarial colorings. The theorems show that generic independent global exterior variation promotes rather than obstructs long paths, so any deterministic counterexample must rely on globally correlated exterior behavior.

**Verification.** Independent GF(2) rank simulations verified the order-packing triple disjointness and generic full-row-rank rates on n=9,11,13,15,17,19,21,25 (300 trials each). Independent face-orbit sampling checked the full physical nonlinear model in n=7,8,9,10 (500 trials each). A further exhaustive-root linear-algebra implementation verified the previously known corank-to-switch consequence for 500 random face-affine matrices in every n=5,...,11. These tests supplement, rather than replace, the exact proofs above.
