# Exterior-assisted packet absorption gives an outward repair — preserved pre-item development

## One exterior vertex can turn a packet bridge into an enlarged-window outward repair

Let \(J\) be the full determining interval of a protected positive reflected double at witness depth \(r\). Let \(z\notin J\) be the immediately adjacent source-order vertex on either side of \(J\), and put
\[
J^+=J\cup\{z\},
\]
so \(J^+\) is again one contiguous interval.

Assume
\[
J=S\sqcup V(T)\sqcup V(U),
\]
where \(|S|=6\) and \(T,U\) are tight paths of order at least two.

Call \(v\in S\) a \(z\)-assisted connector if one of the displayed orders
\[
(T,v,z,U),\quad (T,z,v,U),\quad (U,v,z,T),\quad (U,z,v,T)
\]
is a tight path.

**Lemma (exterior-assisted packet absorption).** If \(v\) is a \(z\)-assisted connector and \(S-v\) is Hamiltonian, then \(H[J^+]\) has a two-cover. Consequently replacing the order on the enlarged interval \(J^+\) by a two-cover order is a strictly outward repair for the original depth-\(r\) witness.

**Proof.** The assisted connector path uses \(z\), \(v\), and all vertices of the two tails. Its complement inside \(J^+\) is exactly \(S-v\), which is Hamiltonian by hypothesis. These two disjoint tight paths therefore cover \(J^+\).

A two-cover order has status word avoiding the positive language
\[
\mathcal W_+=\{001,011,0101\}.
\]
Hence the reordered \(J^+\) contains no internal positive witness at any depth. Every positive window of depth at most \(r\) that could be changed by the surgery was already contained in the original determining interval \(J\), while windows crossing the new boundary of \(J^+\) lie strictly farther outward. Thus the enlarged-window replacement is outward at depth \(r\). \(\square\)

By four-of-six, at least four labels \(v\in S\) have \(S-v\) Hamiltonian. Therefore:

**Corollary.** Three distinct \(z\)-assisted connector labels suffice for an outward repair. More sharply, any one assisted connector outside the at-most-two bad-deletion set
\[
B(S)=\{v\in S:S-v\text{ is non-Hamiltonian}\}
\]
suffices.

This is the exterior analogue of the internal six-packet bridge lemma, but its conclusion is stronger for the terminalization problem: it yields an actual outward move even when \(H[J]\) itself has \(\kappa_2=2\), because the mutable support has been enlarged beyond \(J\).

Failure has a precise bounded form. If neither adjacent exterior vertex yields an outward repair by this mechanism, then for each such \(z\) every \(z\)-assisted connector label lies in the same bad-deletion set \(B(S)\), of order at most two. Thus all good deletion labels are forbidden from every four assisted join orientations. Whenever three of the four required triples of one assisted order are already forced, the fourth must fail and boundary antisymmetry produces an explicit reverse triple involving \(z\). This converts failed exterior absorption into rooted information at the next outward layer.

The lemma does not prove that an adjacent exterior vertex supplies an assisted connector. In particular one may not infer such a connector from the internal four-end reversals alone. The remaining gluing theorem may now target the following dichotomy: an adjacent exterior vertex produces a good assisted connector and hence an outward repair, or the forced reverse triples from all failed assisted connectors assemble into a strictly farther positive witness.
