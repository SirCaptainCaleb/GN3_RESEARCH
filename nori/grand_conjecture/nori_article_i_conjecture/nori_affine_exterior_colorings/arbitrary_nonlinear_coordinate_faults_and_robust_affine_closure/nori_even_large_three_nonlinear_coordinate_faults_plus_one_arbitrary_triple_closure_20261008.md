# Even-dimensional NORI closure with three arbitrary nonlinear coordinates plus linearly many arbitrary nonlinear triple types

# NEW GRAND-CLOSURE SUBCLASS: three arbitrary nonlinear coordinates PLUS one arbitrary nonlinear disjoint ordered-face triple

**THEOREM (robust three-fault root-chart closure with one additional exceptional free triple).** Let n>=18 be EVEN, let K⊂[n] contain three coordinate directions, put D=[n]\K with odd m=n−3>=15, and fix ANY distinct three-coordinate subset T⊂D. Let C be ANY active NORI ordered-three-face binary coloring satisfying C(bar F,rev π)=1−C(F,π). Assume that for every ordered physical three-face whose three free directions lie entirely in D and whose free-direction SET is NOT T, one has the uniform exterior-parity formula
\[
C(F,\pi)=\bigoplus_{j\notin\operatorname{free}(F)}z_j(F).
\]
On ALL ordered three-faces whose free triple MEETS K, AND on ALL ordered three-faces whose free-direction set equals T (all SIX orientations, every exterior root assignment), impose NO restriction whatever beyond the NORI axiom. The exceptions can be completely arbitrary and NONLINEAR. Then C admits a full antipodal n-geodesic with at most ONE ordered-three-face color change.

The conclusion remains valid if the regular exterior-parity formula is replaced by
\[
q\oplus\eta_i\oplus\eta_j\oplus\eta_k\oplus\bigoplus_{s\notin\{i,j,k\}}z_s
\]
for arbitrary fixed bits q,η_i, using root-translation gauge covariance.

**PROOF.** Suppose no full one-switch NORI geodesic exists. Put D=[n]\K, m=|D| odd. Call a direction order p of D **admissible** if NO consecutive 3-direction window of p has unordered direction set T. Along any admissible p, all m−2 ordered-three-face windows of the D-prefix agree with the uniform exterior-parity reference, regardless of physical root exterior bits, since they avoid both exceptional types.

For any admissible p let G_p be its 8-member outside-root code determined by a constant color on all m−2 D-prefix windows. Its root equations are the six-periodic equalities
\[
s_{p_{j+3}}=1-s_{p_j}\quad(1\le j\le m-3).
\]
The already proved six-exceptional-order synchronization lemma applies verbatim to all x with x_D∈G_p and all SIX permutations of K as final directions: under hypothetical no-closure, all three exceptional terminal windows must have the synchronized alternating word
\[
(t(S),1-t(S),t(S)).
\]
The final ordered K-face is physical, independent of the D-prefix order, so the bit t(S) is WELL DEFINED whenever S belongs to any admissible G_p. It is independent of x_K, and physical antipodal reversal gives
\[
t(\bar S)=1-t(S).
\]
The admissible code union is invariant under outside root complementation, since each G_p is.

If S,S' arise from admissible p,p' sharing the same last ordered direction pair (u,v) and agree on D\{u,v}, their first exceptional physical ordered face with free (u,v,a) for any a∈K is IDENTICAL, so t(S)=t(S'). This is the exact certified root-chart equality used in the previous three-fault closure proof.

It remains to prove that these admissible-chart equalities connect S to bar S. The existing six-periodic template theorem supplies a connected antipodally invariant carrier H comprising:
- two adjacent central Hamming layers of Q_m when m≡5 or 1 (mod6);
- four consecutive central Hamming layers when m≡3 (mod6).
More precisely, for EVERY cube edge SS' between the relevant consecutive layers, it supplies an ordered tail pair (u,v), with S and S' differing at u, and compatible 6-periodic binary templates p,p' ending in (u,v), such that S∈G_p, S'∈G_p'. One may choose v freely in a specified opposite-bit class (a 1-bit coordinate in the two-layer cases; a 0- or 1-bit coordinate depending on the layer in the four-layer case). This follows by the explicit m=5,7,9 template tables already proved in Item nori_even_dimension_three_arbitrary_nonlinear_coordinate_faults_full_grand_closure_20261008, repeated by six-periodic blocks.

**NEW LEMMA (safe tail and random template realization).** For EACH such middle-layer cube edge SS' and each fixed extra exceptional triple T, choose the tail partner v in its required root-bit class OUTSIDE T; this is possible because each central layer contains at least (m−3)/2>=6 occurrences of the required bit while |T|=3. The flipped direction u may belong to T. For each of the two root states S,S', separately fix a compatible 6-periodic binary template of length m with tail (u,v). The first m−2 positions contain at least
\[
k=(m-3)/2\ge6
\]
zeros and at least k ones (true from the exact central-layer ranks and selected tail bits). Independently and uniformly assign each prefix coordinate of D\{u,v} to positions matching its 0/1 root bit. The resulting random p satisfies the desired periodic prefix equations, has the prescribed physical root S and tail (u,v), and all such assignments are equiprobable within each bit class.

Bound the probability that p contains ANY consecutive unordered triple equal to T. Because v∉T, an occurrence must either lie wholly in the prefix of length m−2 or contain the penultimate tail direction u but NOT the final v.

For any fixed ordered permutation of the THREE distinct T-directions and any three prescribed consecutive prefix slots, the probability that the chosen directions occupy those slots is at most
\[
\frac1{k(k-1)(k-2)}
\]
(the denominator counts available labeled directions in their respective bit classes, and is minimized when all three come from the same class). There are at most 6 ordered permutations of T and m−4 consecutive three-slot blocks wholly inside the prefix. Hence the probability of a forbidden triple entirely in the prefix is at most \(6(m-4)/[k(k-1)(k-2)]\).

If u∈T, the ONLY possible forbidden block involving the tail is the triple of positions (m−3,m−2,m−1) ending at u; the other two members of T can occupy those two prefix positions in at most two possible orders, each with probability at most \(1/[k(k-1)]\). Thus altogether
\[
\Pr[p\text{ not admissible}]
\le \frac{6(m-4)}{k(k-1)(k-2)}
+\frac{2}{k(k-1)}
=\frac{14k-10}{k(k-1)(k-2)}
<1
\quad(k\ge6).
\]
The final equality uses m=2k+3. For k=6 the right side is 74/120<1, and it decreases thereafter. Therefore at least ONE admissible order p exists for S, and INDEPENDENTLY at least one admissible order p' exists for S', both sharing the selected last ordered pair (u,v). Their first exceptional physical faces coincide and hence t(S)=t(S').

This proves that EVERY cube edge of the middle-layer carrier H is certified as a root-chart equality even after arbitrary nonlinear corruption on T. Since H is connected and antipodally invariant, choose any S∈H and join it to bar S along H. Then t(S)=t(bar S), contradicting t(bar S)=1−t(S). Grand closure follows. QED.

**What was improved.** The previously proved even-dimensional three-arbitrary-coordinate theorem required exterior parity on EVERY ordered physical face whose free directions were wholly outside K. The present theorem allows, in addition, arbitrary nonlinear recoloring of ALL physical ordered faces with ONE WHOLE unordered free triple T⊂D (including all six orientations and 2^(n-3) exterior assignments), with no constraints on their values except active NORI reversal oddness. This is an exact, robust reachability-chart extension in ALL EVEN dimensions n>=18, not a small-order enumeration.

**Scope and frontier.** The unrestricted NORI conjecture remains OPEN. This proof shows the antipodal chart connectivity is robust under a genuine arbitrary out-of-class physical face-direction triple defect, using a probabilistic existence lemma only for selecting actual compatible coordinate orders. Extending from one exceptional T to a sparse FAMILY of exceptional unordered triples is a natural next step; the same union bound can handle bounded-size families with additional care in choosing safe tail partners.

## ELEVATION: a LINEAR-SIZE FAMILY of arbitrary nonlinear free-triple faults

The preceding theorem extends from ONE unordered exceptional triple T to ANY FAMILY \(\mathscr T=\{T_1,\ldots,T_r\}\) of at most r distinct unordered three-coordinate subsets of D, with all SIX orientations and ALL exterior-bit color functions per set completely arbitrary subject only to active NORI oddness.

**STRONGER THEOREM.** Fix an integer r>=1. Suppose EVEN n satisfies
\[
\boxed{n\ge \max\{18,\,6r+8\}.}
\]
Choose ANY K⊆[n] with |K|=3, put D=[n]\K, and choose ANY family of at most r three-element subsets of D. Let C be any active NORI coloring agreeing with uniform full-exterior parity, optionally with a separable intercept q+η_i+η_j+η_k, on every ordered physical three-face whose direction triple lies entirely in D but is not a member of \(\mathscr T\). Allow COMPLETELY ARBITRARY NONLINEAR colors on ALL ordered faces meeting K and ALL ordered faces with free-direction set in \(\mathscr T\), subject solely to NORI antipodal-reversal oddness. Then C has a full antipodal geodesic with at most ONE color change.

**Proof of strengthened avoidance step.** Let m=n−3 odd and k=(m−3)/2=(n−6)/2. The displayed dimension hypothesis implies k>=6 AND k>3r. Let W=union_{T∈mathscr T} T, so |W|<=3r<k.

In each middle-layer cube edge SS' from the six-periodic carrier H, the old root-template table prescribes a tail pair (u,v), with u the flipped direction and v allowed to be ANY coordinate in a specified 0-bit or 1-bit class of S. That required class has AT LEAST k elements at every applicable central layer. Since |W|<k, choose v in the required bit class OUTSIDE W. This works simultaneously for EVERY forbidden T∈mathscr T. Fix a compatible six-periodic template with the shared tail (u,v) for S or for S'. Its prefix has at least k zeros and at least k ones.

Choose a uniformly random assignment of the actual prefix coordinate names to the template's positions, matching their prescribed root bits. For each individual T∈mathscr T, the previous single-triple argument applies because v∉T, yielding
\[
\Pr[\text{some 3-consecutive directions have unordered set }T]
\le B(k):=\frac{14k-10}{k(k-1)(k-2)}.
\]
By the union bound,
\[
\Pr[p\text{ has any forbidden triple type}]
\le rB(k).
\]
We check \(rB(k)<1\) from k>=6 and k>3r. If k=6, then r<=1 and \(B(6)=74/120<1\). For k>=7, r<k/3, so
\[
rB(k)<\frac{14k-10}{3(k-1)(k-2)}.
\]
For all k>=7 the denominator 3(k−1)(k−2) exceeds 14k−10 because
\(3(k−1)(k−2)-(14k−10)=3k^2−23k+16\),
which is negative at k=7 (147−161+16=2>0), positive and increasing for k>=7. Thus indeed rB(k)<1 for all k>=7. [At k=7 it is 2>0.] Hence there exists an admissible actual order p for S and independently p' for S', both sharing the prescribed tail (u,v) and avoiding ALL triples in mathscr T.

Every witness prefix now sees only the untouched full-parity faces; the six-order NORI terminal suffix synchronization and actual first-exceptional-face equality arguments are exactly unchanged. Thus EVERY edge of the connected antipodally invariant middle-layer carrier H still forces \(t(S)=t(S')\), while full NORI antipodal-reversal oddness forces \(t(\bar S)=1-t(S)\). Contradiction. QED.

**Quantitative novelty.** For n>=18 even, choose any
\[
1\le r\le\left\lfloor\frac{n-8}{6}\right\rfloor.
\]
This permits a number of arbitrary nonlinear exceptional unordered free-three-direction TYPES growing LINEARLY with n, IN ADDITION to all face types meeting the fixed exceptional three-coordinate set K. Each exceptional type contains all \(6\cdot 2^{n-3}\) physical ordered face objects (prior to antipodal-orbit pairing), each of which can be chosen nonlinearly and independently up to the NORI law. The theorem is all-dimensional and genuinely robust to extensive nonlinear coloring perturbations; it does NOT prove the unrestricted grand conjecture.
