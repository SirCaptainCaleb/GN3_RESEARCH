# Even-dimensional NORI closure under three arbitrary nonlinear coordinates plus quadratically many arbitrary nonlinear triple types

# QUADRATIC NONLINEAR-FAULT ROBUSTNESS: root-chart NORI closure with arbitrary exceptional unordered triple types

**THEOREM (quadratically many arbitrary nonlinear ordered-three-face direction types).** Fix EVEN n>=18. Set m=n−3 (odd) and k=(m−3)/2=(n−6)/2>=6. Choose any THREE exceptional coordinate directions K⊂[n], set D=[n]\K, and any family \mathscr T of r DISTINCT unordered 3-subsets of D satisfying
\[
\boxed{r\,B_{\!*}(k)<1,\qquad
B_{\!*}(k)=
\frac{6(2k-1)}{k(k-1)(k-2)}
+\frac{2}{k(k-1)}+\frac{2}{k^2}.}
\]
Let C be ANY active NORI reversal-antipodally odd binary physical ordered-three-face coloring. Suppose that on every physical ordered three-face whose free triple lies ENTIRELY in D and whose UNORDERED free triple is NOT in \mathscr T, C equals full exterior parity
\[
C(F,(i,j,\ell))=\bigoplus_{t\notin\{i,j,\ell\}}z_t(F),
\]
optionally plus a fixed separable intercept q+η_i+η_j+η_\ell. On every other ordered face—ALL orientations of ALL triples meeting K, and ALL six orientations of the r triples in \mathscr T, at every physical exterior assignment—allow COMPLETELY ARBITRARY NONLINEAR colors, constrained only by the active NORI axiom. Then C HAS a full antipodal n-edge geodesic with at most ONE ordered-three-face color change.

This is an all-even-dimension robust NORI closure theorem permitting \(r=\Theta(n^2)\) unordered physical triple TYPES of unrestricted nonlinear faults, in addition to ALL faces involving the chosen three exceptional coordinate directions. The theorem does not assert universal NORI closure for arbitrary colors.

**PROOF: period-template chart connection surviving sparse hypergraph faults.** Work first with q=η=0. Suppose there is NO full NORI one-switch geodesic. Define the six-periodic parity-prefix code \(G_p\) for a direction order p of D by the equations
\[
S_{p_{j+3}}=1-S_{p_j}\quad(1\le j\le m-3).
\]
Call p *admissible* when NO THREE consecutive directions of p form an unordered triple belonging to \mathscr T. All ordered face colors used by its D-only consecutive windows are then exactly the baseline full parity reference. As proved by the six-order suffix synchronization theorem, at every S∈G_p for such admissible p, hypothetical no-closure forces a uniform alternating three-window exceptional K-suffix (t(S),1−t(S),t(S)), with t(S) independent of the choice/order of K and of x_K. The final physical K-face, with exterior D-bits bar S, shows t(S) is also independent of the admissible p witnessing S, and the NORI reversal-odd law gives t(bar S)=1−t(S). Thus t is a well-defined antipodally ODD label on the union of all admissible G_p.

The proved six-periodic template lemma of Item nori_even_dimension_three_arbitrary_nonlinear_coordinate_faults_full_grand_closure_20261008 gives a CONNECTED ANTIPODALLY INVARIANT carrier H in the middle Hamming layers of Q_D: two adjacent middle layers for m≡1 or5 (mod6), four central layers for m≡3 (mod6). For EVERY directed cube edge S→S' in H (one 0-to-1 coordinate flip u), the template table supplies an allowed terminal partner v in a prescribed equal-bit class B⊆D\{u}, with |B|>=k, and compatible six-periodic D-words at S and S' ending in the SAME ordered terminal pair (u,v) or (v,u), as dictated by the table. All such partner choices work because the templates fix only the two terminal BITS of the last ordered pair; its coordinate NAMES are arbitrary within their bit classes.

**IMPROVED TAIL PARTNER LEMMA.** Regard \mathscr T as a three-uniform hypergraph on D. Write d_\mathscr T(u,v)=#{T∈\mathscr T:{u,v}⊆T}. For a fixed flipped direction u,
\[
\sum_{v\in B} d_\mathscr T(u,v)\le 2d_\mathscr T(u)\le 2r.
\]
Thus SOME allowable tail partner v∈B satisfies
\[
\boxed{d_\mathscr T(u,v)\le 2r/k.}
\]
Unlike the previous proof, v need NOT avoid the union of exceptional triples. This is the critical improvement that permits r of quadratic size.

Fix the common ordered last pair (u,v), or (v,u) in the m≡1 mod6 case, with this selected partner v. For EACH of S,S', fix a valid six-periodic binary template realizing its prescribed terminal bits, whose first m−2 slots contain at least k zeros AND at least k ones; this is guaranteed by the explicit m=5,7,9 template table repeated in six-bit blocks, and the chosen middle-layer ranks. Independently and UNIFORMLY assign the named prefix coordinates D\{u,v} to their prescribed 0/1 template positions. The result is a uniformly random compatible actual direction order p for S (and independently p' for S') with its last two directions fixed. Its good-prefix equations remain exact.

**RIGOROUS BAD-WINDOW UNION BOUND.** There are m−2=2k+1 prefix positions and two tail positions. Every forbidden consecutive unordered triple T∈\mathscr T must occur in one of exactly three kinds of consecutive windows:
1. Wholly inside the first m−2 positions: there are m−4=2k−1 possible blocks. For each fixed T and block, there are at most 3!=6 ways to arrange its three distinct named coordinates in those positions. The probability of any one specified arrangement is at most 1/[k(k−1)(k−2)], because every prescribed bit class has at least k available named coordinates. Union over all r exceptional triples gives probability at most
\[
\frac{6r(2k-1)}{k(k-1)(k-2)}.
\]
2. The unique block containing the PENULTIMATE tail coordinate but NOT the final tail coordinate: this is (p_{m-3},p_{m-2},p_{m-1}). The penultimate tail coordinate w is either u or v. Each exceptional T containing w contributes at most two ordered assignments of its other two coordinates to the prescribed prefix slots; each such event has probability at most 1/[k(k−1)]. Because d_\mathscr T(w)≤r, their total probability is at most
\[
\frac{2r}{k(k-1)}.
\]
3. The unique block containing BOTH tail coordinates: (p_{m-2},p_{m-1},p_m). The exceptional T must contain both u,v; each such T specifies at most one remaining prefix direction, whose probability of landing in position m−2 is at most 1/k. By the low-codegree partner selection, their total probability is at most
\[
\frac{d_\mathscr T(u,v)}k\le\frac{2r}{k^2}.
\]
These cases exhaust all m−2 ordered-three-face windows in the D-prefix. Therefore
\[
\Pr[p\text{ is NOT admissible}]
\le r B_{\!*}(k)<1.
\]
So an ACTUAL admissible compatible order p exists for S, and independently an admissible order p' exists for S'. Both end with the same ordered tail pair and both have physical first-exceptional ordered face through (tail_1,tail_2,a) for any a∈K. Since S,S' agree outside the flipped coordinate u, and u belongs to the tail free set, their two first-exceptional physical faces are IDENTICAL (the other differing coordinates, if any, also belong to this same free set). Thus their forced alternating-suffix bits obey t(S)=t(S').

As EVERY edge of H admits this certified actual equality, t is constant throughout the connected antipodally invariant H. But t(bar S)=1−t(S) for every S∈H, contradicting the existence of an antipodal pair in H. Hence the assumed grand NORI failure is impossible. This proves closure.

For the optional separable intercept q+η_i+η_j+η_\ell, translate D-root bits by η as in the proved gauge-covariance theorem; the same six-periodic root charts and the same bad-window probabilities are obtained. \(\square\)

**ASYMPTOTIC STRENGTH.** Since
\[
B_{\!*}(k)=\frac{16+O(k^{-1})}{k^2},
\]
the sufficient bound allows r < (1+o(1))k²/16 = (1+o(1))n²/64 exceptional UNORDERED triple types, beyond all triples meeting K. The previous linear-size theorem only handled r<=floor((n−8)/6). For instance at n=28, k=11 one may take r<=6, versus r<=3 in the linear theorem. This proof does NOT require the union of exceptional triple types to leave even one direction unused.

**FOLLOW-UP TARGET.** Remove the assumption of a known parity reference on the untouched D-direction face triples. The proof uses that reference specifically to construct an antipodally connected large code of *actually monochromatic* prefix root charts; the color-free physical-face extraction itself does not rely on affine structure. Alternatively, find a similar connectivity argument for arbitrary reversal-compatible orientation intercept h, independent of a separable gauge. Neither is proved here.

## ELEVATION II: exact binary-pattern counting improves the quadratic constant from 1/64 to 1/40

The preceding probability bound is valid but uses the crude six-permutations-at-every-slot estimate for forbidden three-coordinate sets wholly inside the prefix. The six-periodic templates have a powerful additional property: the prefix of length \(m-2=2k+1\) contains EXACTLY k zeros and k+1 ones, in some order. (Its two bit-class populations are at least k by the middle-layer template theorem, and sum to 2k+1.)

**STRONGER THEOREM.** Retain all hypotheses and conclusions of the main theorem, but replace the sufficient fault bound by
\[
\boxed{r\,B_{\rm new}(k)<1,\quad
B_{\rm new}(k)=\frac8{k(k-1)}+\frac2{k^2}.}
\]
This is a STRICTLY stronger bound than the preceding B_*(k) for every k>=6. It allows \(r<(1+o(1))k^2/10=(1+o(1))n^2/40\) arbitrarily corrupted unordered triple direction types, in addition to the three completely arbitrary nonlinear exceptional directions K.

**Proof (exactly two binary-types for a triple).** Fix one exceptional unordered triple T={i,j,l} and one compatible periodic binary template for a root S and chosen common tail pair. Let N_0,N_1∈{k,k+1} denote the prefix-position counts of binary values. The randomly named prefix order is a uniformly random assignment within each bit class; the bits S_i,S_j,S_l are FIXED.

First count forbidden appearances of T entirely in the prefix:

CASE A: all three coordinates of T have the SAME bit value b. A consecutive three-slot block can host T only if all three slots have bit b. The number of such all-b consecutive blocks is at most N_b-2, because a run of N_b b's contains N_b-2 triples and breaking into several runs cannot increase this count. Given a particular eligible block, the probability its THREE positions contain exactly the names of T in any of their 3!=6 orders is
\[
\frac{6}{N_b(N_b-1)(N_b-2)}.
\]
Consequently the union-bound probability over all eligible consecutive blocks is at most
\[
\frac{6(N_b-2)}{N_b(N_b-1)(N_b-2)}
=\frac6{N_b(N_b-1)}\le\frac6{k(k-1)}.
\]
This argument is exact for the distribution within a bit class.

CASE B: the three coordinates of T have two of one bit value b and one of the other bit value 1-b. A block has a compatible bit pattern only when its three template slots contain those same bit counts. There are at most 2k-1 consecutive prefix blocks total. For any eligible block the probability of receiving the THREE specified named coordinates is
\[
\frac{2}{N_b(N_b-1)N_{1-b}}
\le\frac2{k^2(k-1)},
\]
since the two same-bit names admit 2! orders and the different-bit name is forced into the remaining slot. Therefore the total probability of a wholly-prefix forbidden occurrence is at most
\[
\frac{2(2k-1)}{k^2(k-1)}
\le\frac6{k(k-1)}.
\]
The latter inequality is immediate from 2(2k−1)≤6k.

In both cases, for each T,
\[
\Pr[T\text{ occurs wholly inside the prefix}]\le \frac6{k(k-1)}.
\]
Summing over r exceptions gives at most 6r/[k(k-1)].

The two boundary cases proved previously require NO change: the one-tail-coordinate window contributes <=2r/[k(k-1)], while choosing a common tail partner v of pair-codegree d_\mathscr T(u,v)<=2r/k makes the both-tail-coordinate window contribute <=2r/k². Thus
\[
\Pr[\text{ANY exceptional triple occurs as a D-prefix window}]
\le r\left(\frac6{k(k-1)}+\frac2{k(k-1)}+\frac2{k^2}\right)
=r B_{\rm new}(k)<1.
\]
Genuine compatible admissible parity-root prefix orders exist at BOTH endpoints of EVERY root-chart edge in the connected antipodally invariant middle-layer carrier. The same actual-physical-face coincidence and antipodal-reversal contradiction finish the proof, exactly as in the main theorem. QED.

**Quantitative examples.** For k=6 (n=18), B_new=8/30+2/36<1/3, so r=3 is permitted; for k=7 (n=20), B_new=8/42+2/49<1/4, so r=4 is permitted. At n=100 (k=47), the bound permits r<=217, improving the preceding quadratic theorem's r<=132 and the original linear theorem's r<=15.

**Scope.** This is a refined NONLINEAR SUBCLASS CLOSURE theorem, not universal NORI grand closure. The dependence on a clean full-exterior-parity reference outside K and the exceptional triple family remains essential to this particular proof.
