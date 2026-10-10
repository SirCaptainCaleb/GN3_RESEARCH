# General central-layer signed path-square model, linear-time extraction, and reversal-rigidity bound

# Arbitrary central-layer ordered-triple tables as an exact signed triangular-strip optimization

Let n=2m≥6 and k=m−2. Consider any LEGAL NORI coloring that, on the two central exterior-Hamming layers, depends only on the ordered free triple π and the layer (it may behave arbitrarily on all other layers). Write
c(F,π)=a(π) if the exterior weight is k;
c(F,π)=1+a(reverse π) if the exterior weight is k+1.
This is the GENERAL legal relation between the two central tables; a need not be reversal-invariant. Fix a full direction order p and put a_i=a(p_i,p_(i+1),p_(i+2)), a_i^R=a(p_(i+2),p_(i+1),p_i), 1≤i≤2m−2.

Use actual paired starting vertices x_(2j−1)=1−b_j,x_(2j)=b_j. Define φ(2j−1)=j+1 and φ(2j)=j, for 1≤j≤m−1. Every physical ordered-three-face window stays at one of the two central layers, and its color is EXACTLY
g_i(b)=a_i+(1+a_i+a_i^R)b_(φ(i)) mod 2.

**THEOREM 1 (exact path-square model).** For EVERY legal central two-layer table and EVERY prescribed direction order p, the minimum number of color switches among all paired physical starting roots is the minimum over b∈F2^m of the explicit binary energy
E_p(b)=Σ_(i=1)^(2m−3) [g_i(b)≠g_(i+1)(b)].
The interaction graph of E_p on variables b_1,...,b_m is a SUBGRAPH of P_m^2, the graph joining indices at distances 1 or 2. The 2m−3 seams correspond bijectively to the edges of P_m^2, each carrying a cost of at most two variables; costs may ignore one or both endpoint variables. Consequently the exact optimum and an attaining physical antipodal geodesic can be found by a four-state forward dynamic program in O(m) arithmetic operations and O(m) storage (two remembered consecutive b values suffice). This is an exact polynomial-time fixed-order extraction test in every even dimension.

**Proof.** The paired-coordinate exterior weights and displayed window formula follow by counting complete flipped/unflipped pairs and the remaining single exterior bit, just as in the previously proved paired-root chart. The sequence of φ-indices in window order is 2,1,3,2,4,3,5,4,...,m,m−1. Hence its consecutive unordered pairs enumerate the edges of P_m^2 exactly once, for example (1,2),(1,3),(2,3),(2,4),(3,4),(3,5),...,(m−2,m),(m−1,m). Some of these terms may be constant or unary. Each seam cost depends only on the variables at the endpoints of the corresponding edge. Process b_1,...,b_m; after choosing b_j retain (b_(j−1),b_j), and on introducing b_(j+1) score the two edges ending at j+1 (when they exist). This is a four-state dynamic program; backtracking reconstructs b. All constructed cube paths are genuine full antipodal geodesics. QED.

Define the reversal-asymmetric (RIGID) window set R_p={i:a_i≠a_i^R}. If i∈R_p, the factor 1+a_i+a_i^R vanishes and g_i(b)=a_i is independent of the paired root. If i∉R_p, g_i(b)=a_i+b_(φ(i)), which is a gauge-flexible window. Define δ_j=a_(2j−1)+a_(2j+2), and let μ(δ) be the sum of ceil(r/2) over all maximal one-runs of δ.

**THEOREM 2 (quantitative asymmetric-intercept stability).** For every prescribed order p there are two antipodal paired starting roots, each giving at most
min(2m−3, μ(δ)+2|R_p|)
switches in the actual central-two-layer coloring. In particular, if R_p=∅, the exact optimum is μ(δ), even when a is reversal-asymmetric on OTHER triples outside this order.

**Proof.** First temporarily assign each window its flexible proxy bit g_i^*(b)=a_i+b_(φ(i)). The triangle-frustration theorem constructs antipodal b,1−b with μ(δ) proxy switches. For any b, actual g differs from g^* only at indices i∈R_p, since the rigid windows lose the b term. Altering one word position changes at most its two incident seams, so the actual number of switches increases by at most 2|R_p|, for each of the two companion roots separately. The obvious maximum is 2m−3. When R_p=∅ the two words coincide, and the previous exact minimum applies. QED.

**Precise global frontier.** The intrinsic coordinate-only reversal-odd subcase a(reverse π)=1+a(π) has R_p equal to ALL window positions. Then all g_i are independent of b, and the exact path-square reduction is the original ordered-triple sequencing problem. Arbitrary exterior-face dependence also destroys the one-bit-per-window function g_i(b) unless an additional face-fiber invariance is established. Thus the triangular strip isolates two genuine obstructions: reversal-asymmetric rigid triples and physical exterior-bit sensitivity. Both must be addressed by root/order coupling to settle unrestricted NORI.
