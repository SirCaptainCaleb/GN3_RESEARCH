# Transverse curvature oscillation along near-spanning monochromatic geodesics

# Endpoint residual barriers and corrected transverse oscillation

This subsection records the endpoint consequences of complementary monochromatic arms. An earlier version applied the residual-face gluing theorem at the common root of the arms. Its residual face is instead based at an arm endpoint. The assertions of a barrier at every interior corridor vertex, the resulting corridor-wide ordinary-curvature oscillation, and the associated one-sided exchange-defect profile are withdrawn.

Let c be an antipodally odd coloring of Q_n, and suppose it has no monochromatic full antipodal geodesic. Let P=(v_0,...,v_m) be a red dimension-simple path, and let M be its unused directions.

## Theorem 1 (endpoint residual-face barriers)

Every full path through the M-face based at v_0, starting at v_0, contains a descent 10. The same holds at v_m. If m>0 and |M|>=2, the two disjoint endpoint faces together contain at least 2|M|(|M|-1) descending directed two-edge turns.

*Proof.* At v_0 take the empty red arm and the whole path P as the other arm. The residual-face gluing theorem then has its starting corner v_0. Repeat from v_m with reversed P. The two faces are disjoint when m>0. Apply the sharp residual-face turn bound separately. Splitting P at an interior vertex produces arms ending at v_0 and v_m, so it gives these same endpoint faces, rather than an additional face at the splitting vertex. QED.

For |M|=1 the endpoint barrier is impossible, recovering the full-geodesic extension principle for a monochromatic path of length n-1.

## Theorem 2 (translated color oscillation in codimension two)

Let M={a,b}. At each endpoint u in {v_0,v_m}, the residual square is a gate:
\[
c_a(u)=c_b(u)=1,\qquad c_b(u+a)=c_a(u+b)=0.
\]
For h in {a,b}, let w_j^(h) be the color of the j-th edge of P+h. Then the word w^(h) contains both 01 and 10.

*Proof.* Both residual square routes must descend, giving the displayed gates. For k the other unused direction, the path consisting of the h-edge at v_0, then P+h, then the k-edge to the antipode of v_0 has word 1 w^(h) 0. It uses every direction once. If w^(h) had no 01, this full word would have at most one switch, which yields a monochromatic full path by root sliding. Reversing P gives 1 rev(w^(h)) 0, forcing 10 as well. Only the two endpoint gates are used. QED.

In particular, a hypothetical bad coloring cannot contain a monochromatic (n-2)-path when n<=4, since its translated word is too short to have both transitions.

## The strip formula and its scope

Put h_j=c_h(v_j), let d_j be the j-th direction of P, and put
\[
\kappa_j^{(h)}=\kappa(F_{\{h,d_j\}}(v_{j-1})).
\]
Since P is red,
\[
w_j^{(h)}=\kappa_j^{(h)}+h_{j-1}+h_j\pmod2.
\]
Consequently the corrected curvature word on the right has both transitions. Endpoint gates give h_0=h_m=1 and hence
\[
\sum_j\kappa_j^{(h)}=\sum_jw_j^{(h)}\pmod2.
\]
They do not force the interior h_j to equal one. Ordinary curvature need not coincide termwise with the translated color word by this argument. Likewise, the earlier corner-independent one-sided Freudenthal defect formula requires blue transverse edges at both ends of each individual side square; that condition has only been established for a side square when its two transverse edges are separately known to be blue.

At either endpoint, a full monochromatic face path supplies both ordinary monotone orientations. The adjacent parallel face roots at that endpoint are empty by the two-step lift. This proves at least two empty roots in each adjacent face when m>=1. It does not prove the former 2m bound. Interior seams and transverse edge colors remain part of the unrestricted closure problem.
