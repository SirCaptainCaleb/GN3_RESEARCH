# Full NORI one-switch closure for every even dimension under three arbitrary nonlinear exceptional coordinate directions

# GRAND-CLOSURE SUBCLASS: three arbitrary nonlinear coordinate faults of exterior parity in every EVEN dimension

**THEOREM.** Let n>=8 be EVEN. Fix ANY three-element set K={a,b,c} of cube coordinate directions and put D=[n]\K, with odd m=|D|=n-3>=5. Let C be an arbitrary binary coloring of PHYSICAL ORDERED three-faces of Q_n satisfying the active NORI reversal-odd law
\[
C(\bar F,\operatorname{rev}\pi)=1-C(F,\pi).
\]
Assume ONLY that for every ordered triple π entirely contained in D, its color is the UNIFORM EXTERIOR-PARITY value
\[
C(F,\pi)=\bigoplus_{j\notin\operatorname{free}(F)} z_j(F).
\tag{1}
\]
For ordered triples that MEET K, there is NO RESTRICTION WHATSOEVER on dependence on the exterior bits or on the ordered direction list, beyond the NORI oddness law. Then C HAS a full antipodal cube geodesic with at most ONE ordered-three-face color change. Thus the active NORI conjecture is proved for this broad arbitrary nonlinear three-coordinate perturbation class, uniformly in every even n>=8.

The reference (1) is itself active-NORI-valid because n−3=m is odd, so complementing its m exterior bits flips the parity, and reversing π does not affect the parity. The result generalizes the previously proved two-coordinate arbitrary nonlinear exception theorem by ONE WHOLE EXCEPTIONAL COORDINATE.

**Proof by contradictory root-sheet connectivity.** Suppose NO full NORI one-switch geodesic exists. Fix any permutation p=(p1,...,pm) of D. For full direction orders (p,σ) with σ any of the SIX orders of K, all first m−2 three-face windows are the uniform parity baseline. Write S=x_D for the outside D starting bits. Those m−2 window colors are constant precisely when their m−3 successive change indicators vanish:
\[
S_{p_{j+3}}=1-S_{p_j}\qquad(1\le j\le m-3).
\tag{2}
\]
These constraints have exactly EIGHT solutions S∈Q_D for each p, determined by the first three bits S_{p1},S_{p2},S_{p3}. Denote the union of solutions as p varies by \(\mathcal G\subseteq Q_D\). It is invariant under outside complement S↦\bar S, since (2) is invariant.

**Step A: 6-order suffix synchronization.** Apply the previously proved precise theorem
nori_three_nonlinear_coordinate_faults_six_order_antipodal_suffix_sync_20261008,
whose general hypotheses hold here with h=0. It establishes, under our hypothetical failure, a well-defined binary function t:\mathcal G→F2 such that for ANY p witnessing S∈\mathcal G and ANY full initial root x with x_D=S:
- all SIX choices of K order σ produce the SAME final three-window word (t(S),1−t(S),t(S));
- t(S) is independent of the three root bits x_K;
- the first exceptional ordered three-face window, for ANY first exceptional coordinate a∈K, has color t(S);
- antipodal reversal of the terminal ordered K-faces gives
\[
t(\bar S)=1-t(S).\tag{3}
\]
The last equality is independent of p because the same physical ordered K-face is reached after traversing all D, and t(S) is its order-independent color. Thus it is a global odd function on \mathcal G.

**Step B: physically identical first-exceptional faces force t-equivalences.** Suppose S,S'∈\mathcal G are witnessed by outside orders p,p' with the SAME last ordered pair (u,v)=(p_{m−1},p_m)=(p'_{m−1},p'_m), and S,S' agree on all outside coordinates in D\{u,v}. Fix the SAME three K root bits for their full roots. Their first exceptional window is the ordered physical three-face with free directions (u,v,a), for any fixed a∈K. Before this window the path has traversed EXACTLY D\{u,v}, regardless of its internal order. Hence its exterior coordinate bits are 1−S_i=1−S'_i on D\{u,v} and the same K\{a} starting bits. The two physical ordered faces are IDENTICAL, so their actual C-colors coincide. By Step A those values are t(S),t(S'). Therefore
\[
t(S)=t(S').\tag{4}
\]
Crucially this is a genuine physical-face equality; no convexification, abstract-label equality, or same-color assumption was introduced.

**Step C: a six-periodic template lemma forces a full connected middle-layer equality graph.** Fix a permutation p and write the constrained bits in its order:
\[
s_1s_2\cdots s_m
=
(\alpha,\beta,\gamma,\ 1-\alpha,1-\beta,1-\gamma,\ \alpha,\beta,\gamma,\ldots),
\tag{5}
\]
for some initial \(\alpha,\beta,\gamma\in\{0,1\}\). This word is 6-PERIODIC, with exactly THREE ones in every full block of six entries. Define \(\mathcal T_m(k)\subseteq\{00,01,10,11\}\) to be the set of terminal bit pairs (s_{m−1},s_m) of these eight templates whose first m−2 bits have exactly k ones. These finite sets can be calculated directly from the eight choices of \(\alpha,\beta,\gamma\). Since each six-block contains three ones and (5) repeats, the exact recurrence is
\[
\mathcal T_{m+6}(k+3)=\mathcal T_m(k).
\tag{6}
\]
For odd m>=5, it therefore suffices to list three base cases:

\[
\begin{array}{c|l}
m & \text{nonempty }\mathcal T_m(k)\\\hline
5 & k=0:\{11\},\ k=1:\{01,10,11\},\ k=2:\{00,01,10\},\ k=3:\{00\};\\
7 & k=2:\{10,11\},\ k=3:\{00,01\};\\
9 & k=3:\{00,01,10,11\},\ k=4:\{00,01,10,11\}.
\end{array}
\tag{7}
\]

Because p can be ANY permutation of outside coordinate DIRECTIONS, a cube bitstring S can realize one of these templates with any FIXED ordered last pair (u,v) iff its outside remaining m−2 bits have k ones and its bit values at u,v form one of the listed patterns in \mathcal T_m(k). The earlier m−2 directions may be permuted arbitrarily to match a template prefix with the same number of ones; no other constraints remain.

Now consider three residue cases; below, equalities across listed neighboring S,S' follow from (4) with a shared tail pair (u,v).

CASE 1: m=6r+5. Put w=(m−1)/2=3r+2. The union \mathcal G is EXACTLY the two middle Hamming layers w,w+1. For ANY weight-w S and ANY zero-bit coordinate u that we wish to flip, choose v with S_v=1. The remaining outside m−2 bits have w−1=3r+1 ones. By the 5-row of (7) shifted r times, terminal pairs (S_u,S_v)=01 and (S'_u,S'_v)=11 are BOTH realizable with the SAME ordered tail (u,v), where S'=S⊕u has weight w+1. Hence EVERY cube edge between the weight-w and weight-(w+1) layers enforces t(S)=t(S'). These adjacent middle layers form a CONNECTED subgraph of Q_m.

CASE 2: m=6r+7. Put w=(m−1)/2=3r+3. Again \mathcal G is EXACTLY the middle layers w,w+1. For ANY weight-w S and ANY zero-bit coordinate v, choose u with S_u=1. The remaining bits have w−1=3r+2 ones. The 7-row of (7) has both terminal patterns 10 and 11 at this prefix count. Flip v from 0 to1 and apply (4). Thus EVERY cube edge between these two middle layers enforces equality, and the graph is CONNECTED.

CASE 3: m=6r+9. Put w=(m−3)/2=3r+3. The union \mathcal G is EXACTLY the FOUR consecutive central Hamming layers w,w+1,w+2,w+3. By the 9-row of (7), shifted r times, ALL FOUR terminal patterns occur when the remaining m−2 bits have either w or w+1 ones. For EVERY edge S→S' obtained by changing a zero to one between consecutive layers:
- from weight w to w+1, select the second terminal coordinate v with S_v=0, giving prefix weight w and tail transition 00→10;
- from weight w+1 to w+2, select v with S_v=1, giving prefix weight w and tail transition 01→11;
- from weight w+2 to w+3, select v with S_v=1, giving prefix weight w+1 and transition 01→11.
Each is a valid identical-physical-face comparison, so (4) gives equality along EVERY such cube edge. The induced graph on four consecutive central layers is CONNECTED.

For any two consecutive nonempty Hamming layers of Q_m, the induced graph is connected: all vertices of the lower layer can be joined through 2-step swaps of a 1 and 0 via the upper layer, and every upper vertex has a lower neighbor. A longer interval of consecutive middle layers is likewise connected. Consequently in ALL THREE cases, the equalities (4) force t to be CONSTANT on all of \mathcal G. Yet \mathcal G is nonempty and closed under complement S↦\bar S, and (3) demands t(\bar S)=1−t(S). Contradiction. Hence the assumed grand-NORI failure cannot occur. QED.

**What is solved and what remains.** This is a COMPLETE, all-even-dimension theorem about a large, genuinely NONLINEAR class of active NORI colorings: absolutely every ordered face involving one of three arbitrary exceptional coordinates may be recolored independently (subject to active NORI parity), with no bound on its Hamming distance from the parity reference. It uses the exact color-free reachability philosophy at a physical-face level: six differently oriented terminal reachability witnesses generate a common antipodally odd endpoint-label t, and certified adjacent root charts force a connected label carrier. Unlike the earlier 2-coordinate terminal-fault result, the proof uses multiple coordinate orders, the NORI oddness law, and a nontrivial connectedness theorem for a cyclic 3-chain root-code.

The unrestricted NORI grand conjecture for arbitrary face colorings is STILL OPEN. Extending the argument requires a replacement for the parity 3-chain root-code connectivity under arbitrary colors outside K, or a way to choose such a coordinate split K after a normalization/exchange.

## Corollary: arbitrary separable orientation-intercepts on the untouched triples

The theorem is not restricted to zero intercept h. For ANY bit vector η∈F2^D and any bit q, suppose the untouched ordered triples entirely in D satisfy
\[
C(F,(i,j,k))=
q+\eta_i+\eta_j+\eta_k+
\bigoplus_{s\notin\{i,j,k\}}z_s(F).
\]
All triples intersecting K remain ARBITRARY nonlinear subject only to NORI oddness. Then grand closure still holds for every even n>=8.

**Proof.** For each outside order p, its early consecutive color-change bit is
\[
\delta_j=1+x_{p_j}+x_{p_{j+3}}+\eta_{p_j}+\eta_{p_{j+3}}.
\]
This follows because adjacent ordered triples share their two middle coordinate directions and their intercept sums cancel there, leaving η_{p_j}+η_{p_{j+3}}. Set S'_i=x_i+η_i for every i∈D. The good-prefix root equations become precisely the 6-periodic equations \(S'_{p_{j+3}}=1-S'_{p_j}\) of the proved h=0 case. The translation S↦S+η preserves agreement outside a fixed terminal pair (u,v), so it carries the physical chart equality graph bijectively to the original 6-periodic graph. It also COMMUTES with global complement S↦bar S. Therefore the proved connectedness and antipodal self-connection survive the translation, and the exact chart-extraction theorem gives grand closure. QED.

This strengthens the result to a family of 2^(n−3) distinct coordinate-separable orientation-intercepts (plus a uniform bit q) on the nonexceptional triples, while exceptional triples may still be arbitrarily nonlinear.
