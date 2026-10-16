# Forward influence-cone obstruction for doubled-direction holonomy

- Stable ID: note_87aec5ba5386ea640f6aecb0
- Author: unspecified; session provenance retained
- Primary home: subsection:paired_direction_involutions_and_geodesic_endpoint_matchings
- Labels: holonomy, influence-graph, crossing-commutators, source-SCC
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r10487_3
- Updated session: session_nori_r10487_3
- Disposition: none
- Successor: none

## Related references

- None

## Research note

### Directed influence cones of interlacement curvature

Continue with the doubled-direction word \(w\), red swaps \(U_i\), its set \(C(w)\) of directions appearing in a noncommuting interlacement pair, and the directed influence graph \(D(c)\), whose arc \(i\to j\) means that the rule \(c_j\) reads bit \(i\). Define the forward influence closure \(A=\operatorname{Reach}^+_{D(c)}(C(w))\).

**Theorem (influence-cone necessary condition).** For every starting fiber state \(x\in Q_n\), the red return map \(U_w\) preserves every bit outside \(A\):
\[
\boxed{\pi_{[n]\setminus A}U_w(x)=\pi_{[n]\setminus A}(x).}
\tag{IC1}
\]
Consequently any doubled-direction word with antipodal return \(U_w(x)=\bar x\) must satisfy
\[
\boxed{\operatorname{Reach}^+_{D(c)}(C(w))=[n].}
\tag{IC2}
\]

*Proof.* By the crossing-commutator factorization, \(U_w\) is a product of conjugates of commutators \(K_{ij}=(U_jU_i)^2\), each with both \(i,j\in C(w)\subseteq A\). Write \(T=[n]\setminus A\). As \(A\) is forward-closed under directed influence, no rule indexed by \(T\) reads a vertex bit belonging to \(A\). Therefore projection onto \(T\) intertwines every full red swap \(U_k\) with the corresponding swap on \(Q_T\) when \(k\in T\), and with the identity when \(k\in A\). This property extends to their inverses, products and conjugates. In particular each square commutator \(K_{ij}\) with \(i,j\in A\) and every conjugate of it acts trivially after projection onto \(T\). So does their product \(U_w\). This proves (IC1), and (IC2) follows because an antipodal displacement changes every vertex bit. \(\square\)

**Theorem (source-component curvature requirement).** Let \(S_1,\ldots,S_h\) be the source strongly connected components of \(D(c)\). If \(U_w(x)=\bar x\), then for every \(a\), the chord diagram \(J(w)\) has a crossing edge \(\{i,j\}\) lying entirely in \(S_a\) and satisfying \(U_iU_j\ne U_jU_i\). Consequently
\[
\boxed{r_c(w)\ge h.}
\tag{IC3}
\]

*Proof.* A source SCC \(S_a\) receives no influence arcs from outside, so each rule indexed in \(S_a\) depends only on its own SCC bits. Projecting the red swap sequence onto \(S_a\) deletes all letters outside \(S_a\) and preserves the original action on its bits. The projected double-occurrence word must send the projected start state to its bitwise complement. If it had no noncommuting interlacement pair, the crossing factorization theorem would make its return the identity, a contradiction. Different source SCCs are disjoint, and crossing status of pairs within one SCC is not affected by deleting the other labels. Thus the required crossings are distinct, proving (IC3). \(\square\)

**Sharpness.** The direct product of \(h\) legal reciprocal-reader two-cubes in (CW4) has \(h\) source SCCs and admits an antipodal doubled-direction return with \(h\) crossing pairs. Thus (IC3) is tight for arbitrarily large \(n=2h\), and the standard paired lift gives balanced examples on \(Q_{4h}\).

This improves the earlier weak-component lower bound to the source-SCC count and gives a geometric necessary coverage criterion (IC2). It is compatible with a strongly connected influence graph having a single interlacement-curvature seed; such a seed being sufficient is not claimed.
