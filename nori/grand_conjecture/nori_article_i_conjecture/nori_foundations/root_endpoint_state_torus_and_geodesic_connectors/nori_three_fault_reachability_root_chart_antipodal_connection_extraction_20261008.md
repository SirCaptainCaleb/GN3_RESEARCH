# Three nonlinear fault directions: an antipodal root-chart connector theorem with exact NORI extraction

# An exact root-chart connectivity extraction theorem for three arbitrary nonlinear NORI fault directions

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
