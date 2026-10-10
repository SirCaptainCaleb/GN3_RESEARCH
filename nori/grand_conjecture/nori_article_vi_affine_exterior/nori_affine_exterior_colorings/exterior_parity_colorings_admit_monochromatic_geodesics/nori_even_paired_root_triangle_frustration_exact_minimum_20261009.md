# Exact triangle-frustration minimum and quarter-linear switch bound on paired roots

# Exact all-dimensional paired-root minimum for genuine NORI geodesics

Let n=2m≥6, k=m−2. Assume a legal ordered-three-face coloring has c(F,π)=a(π) on exterior-one layer k and c(F,π)=1+a(π) on layer k+1, where a(π)=a(reverse π), as required by antipodal oddness. Other layers are arbitrary. Fix ANY full order p and put a_i=a(p_i,p_(i+1),p_(i+2)), 1≤i≤2m−2. Let δ_j=a_(2j−1)+a_(2j+2) over F2 for 1≤j≤m−2. Let μ(δ)=Σ_runs ceil(length(run)/2), summing over maximal 1-runs of δ.

**THEOREM.** Among the 2^m actual paired-root full geodesics x_(2j−1)=1−b_j,x_(2j)=b_j, the EXACT minimum number of ordered-three-face color changes is μ(δ). At least two antipodal paired roots attain the minimum. For every prescribed order p there are consequently at least two antipodal full geodesics with ≤ceil((m−2)/2)=ceil((n−4)/4) changes. This fixed-order bound is sharp within the stated coloring class. A one-switch paired root exists exactly when the support of δ is empty, a singleton, or an adjacent pair.

**Proof.** On paired roots the physical central-layer selector t satisfies t_(2j−1)=b_(j+1),t_(2j)=b_j (1≤j≤m−1), and every binary t satisfying t_(2j−1)=t_(2j+2) (1≤j≤m−2) comes from a UNIQUE b. The color word g=a+t therefore ranges precisely over words satisfying g_(2j−1)+g_(2j+2)=δ_j. Write s_i=g_i+g_(i+1) (mod 2), where s_i=1 is a color switch. Telescoping gives δ_j=s_(2j−1)+s_(2j)+s_(2j+1).

A switch affects at most two δ equations and, if two, their indices are adjacent. Every maximal run of r ones in δ therefore needs at least ceil(r/2) switches touching it. Switches touching distinct runs are disjoint because the runs are separated by a zero position. Hence #switches≥μ(δ).

For the matching upper bound, partition every 1-run into successive adjacent pairs and at most one singleton. Generate the pair (j,j+1) with the single switch s_(2j+1)=1, contributing e_j+e_(j+1) to δ. Generate the singleton j with s_(2j)=1, contributing e_j. Put all other s_i=0. This realizes δ with exactly μ(δ) switches. Integrate s from g_1=0, then use the proved bijection g↔b; integrating from g_1=1 gives the complementary word and the antipodal root x+1^n. Pairing the δ indices shows μ(δ)≤ceil((m−2)/2). For sharpness of the universal fixed-order bound, prescribe all δ_j=1; the compared triples along fixed p are distinct and can have their a-values assigned independently, respecting a(π)=a(reverse π). The exact formula then gives ceil((m−2)/2). QED.

**Geometric interpretation.** In the window sequence, variable indices are φ(2j−1)=j+1 and φ(2j)=j, and consecutive window seams are exactly the edges of the path-square graph P_m^2 (a triangulated strip). The parity δ_j is the gauge-invariant curvature around the jth interior triangle. Minimizing changes is a minimum-support edge representative of the prescribed triangle curvature, equivalently a unit-cost dual T-join. The run formula solves this problem in closed form.

**Consequences.** The paired-root sparse-defect criterion established previously is also NECESSARY within this chart. In n=8 every prescribed direction order admits a one-change paired-root solution. In n=10 any direction order with δ_1=0 admits a one-change paired-root solution.

**Scope.** This is a quantitative full-geodesic theorem for central-two-layer reversal-even intercepts. Arbitrary exterior-face dependence and reversal-asymmetric intercepts remain separate global obligations.
