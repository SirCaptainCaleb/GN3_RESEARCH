# Arbitrary nonlinear-coordinate faults and robust affine closure

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



*Exact scoped proof in note* note_clean_prefix_sparse_fault_chart_obstruction.
