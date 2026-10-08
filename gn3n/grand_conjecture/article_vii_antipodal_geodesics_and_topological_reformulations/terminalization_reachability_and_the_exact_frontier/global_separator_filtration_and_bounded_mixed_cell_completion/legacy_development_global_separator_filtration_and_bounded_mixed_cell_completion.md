# Global separator filtration and bounded mixed-cell completion — preserved pre-item development


### Global separator filtration

Order the fixed witness-path edges from the center outward as
\[
e_1,\ldots,e_r,\qquad r=m-2.
\]
Work on the antipodal Coxeter/Freudenthal chamber sphere \(K\cong S^m\). Every chamber of a counterexample has a selected nonzero local-witness label \(\pm e_j\).

For \(1\le i\le r+1\), let \(K_i\) be the invariant chamber subcomplex obtained by retaining the chambers whose selected witness edge belongs to \(\{e_i,\ldots,e_r\}\). Thus \(K_1=K\), while \(K_{r+1}\) has no chambers in a counterexample. Inside \(K_i\), chambers not belonging to \(K_{i+1}\) have label \(+e_i\) or \(-e_i\).

**Separator-index lemma.** Let \(X\) be a finite free \(\mathbb Z_2\)-complex and let \(S\subseteq X\) be closed and invariant. Suppose
\[
X\setminus S=U^+\sqcup U^-,
\qquad \tau U^+=U^-,
\]
with \(U^\pm\) open-and-closed in \(X\setminus S\). Then the Krasnoselskii genus satisfies
\[
\gamma(S)\ge \gamma(X)-1.
\]
Indeed \(X\setminus S\) has an equivariant map to \(S^0\), hence genus at most one. Taking an invariant regular neighborhood of \(S\) and using genus subadditivity gives \(\gamma(X)\le\gamma(S)+1\).

Consequently, if at every witness edge \(e_i\) the \(e_i\)-free locus separates the two orientation regions, then
\[
\gamma(K_{r+1})\ge \gamma(K_1)-r=(m+1)-(m-2)=3,
\]
contradicting that \(K_{r+1}\) has no chambers. Therefore some stage necessarily fails separation.

### Exact meaning of separator failure

Separator failure is local: some mixed \(e_i\)-cell lets \(+e_i\) and \(-e_i\) incident chambers communicate without an outward-labeled separator. The existing protected-band and terminal-block arguments apply precisely there. If the reflected determining windows separate across a face-block boundary, blockwise splicing gives an \(e_i\)-free chamber. Otherwise the finite terminal classification bounds the determining support by ten vertices.

Thus the global problem reduces to one bounded strengthening of the finite terminal theorem.

**Bounded mixed-cell separator-completion lemma (remaining local obligation).** Let \(F\) be a mixed cell at stage \(e_i\): both orientations occur, no earlier witness occurs in the protected band, and ordinary blockwise outward splicing is unavailable. Then either \(H\) already has a spanning two-cover, or the bounded terminal determining interval can be reordered so that no witness edge \(e_j\) with \(j\le i\) occurs. Any new witness created at an endpoint of the reordered interval is strictly farther outward.

### Why the boundary issue is bounded

Every terminal determining support is a contiguous central interval of at most ten vertices. A two-cover of the induced support gives an ordering \(P,Q^{\rm rev}\) whose internal status word has no forbidden witness. Replacing the old order on that interval changes only status windows meeting one of the two ends outside the support. Those windows lie outside the selected innermost determining windows, so they cannot create a witness strictly closer to the center than \(e_i\). The only unresolved point is whether they can recreate \(e_i\) itself at an endpoint. This is a finite boundary-compatibility question involving at most two crossing status windows at each end.

This compresses the former global carrier-terminalization problem to a finite endpoint-compatibility statement on the already bounded terminal supports, without minimum-counterexample or disturbance arguments.
