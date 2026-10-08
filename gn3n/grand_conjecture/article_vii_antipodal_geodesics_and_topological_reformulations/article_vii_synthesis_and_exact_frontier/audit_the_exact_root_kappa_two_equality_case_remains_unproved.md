# Correction: exact-root deletion distance at least two does force a zero root

## Composition

### Correction: deletion distance at least two forces a zero exact root

The bounded central classification proves the following stronger statement:
\[
\boxed{\kappa_2(H)\ge2
\Longrightarrow
\text{every positively balanced exact-root carrier contains a chamber with }p=c.}
\]
The length-two nonzero configurations have deficiency at most one. In the sole four-vertex residual configuration, the distinguished-vertex structure supplies a chamber with both root coordinates at least \(s+1\), while the global deficiency lower bound forces equality \(p=c=s+1\). Hence there is no genuine nonzero \(k=2\) equality branch. The load-bearing exact-root state is the symmetric partial cover \(P\mid X\mid Q\) with \(|P|=|Q|\).

## Development

## Correction: the exact-root \(k\ge2\) zero-root theorem is proved

An earlier version of this audit incorrectly stated that [[exact_root_compression_and_bounded_central_structure_subsection_a]] asserted, without proof, that
\[
\kappa_2(H)\ge2
\]
forces a zero exact root on every positive exact-root carrier.

That reading stopped too early in the long source subsection. The proof appears later, after the strengthened four-central-vertices classification and the distinguished-vertex analysis.

### The actual argument

Assume a positively balanced exact-root carrier \(F\) has no zero root and put
\[
s=\min_{\pi\in F}\min\{p(\pi),c(\pi)\},
\qquad
L=m-2s.
\]
The strengthened central classification leaves exactly three nonzero configurations:
\[
(\ell,r,|B|,L)
=
(s+1,s+1,2,2),
\]
\[
(s+1,s+1,4,4),
\]
or, up to left-right symmetry,
\[
(s+1,s,3,2).
\]

If \(L=2\), any chamber with \(p=s\) has
\[
\delta\le L-1=1,
\]
contradicting the global bound
\[
\delta\ge\kappa_2(H)\ge2.
\]

Thus only
\[
\ell=r=s+1,\qquad |B|=L=4
\]
remains. The distinguished-vertex theorem supplies \(z\in B\) such that every \(p=s\) witness begins \(B\) with \(z\), while every \(c=s\) witness ends \(B\) with \(z\).

Choose a chamber whose first and last vertices of \(B\) are both different from \(z\). Then
\[
p,c\ge s+1.
\]
Since
\[
m=2s+4
\]
and every chamber has
\[
\delta=m-p-c\ge2,
\]
we obtain
\[
2\le\delta\le (2s+4)-2(s+1)=2.
\]
Hence
\[
p=c=s+1,
\]
contradicting the assumption that the carrier has no zero root.

Therefore the stronger theorem is established:
\[
\boxed{
\kappa_2(H)\ge2
\Longrightarrow
\text{every positively balanced exact-root carrier contains a chamber with }p=c.
}
\]

### Elevation consequence

The later role-anchor surplus theorem
\[
\text{nonzero augmented carrier}\Longrightarrow \kappa_2\le2
\]
is still useful as an independent dimensional argument, but it is weaker on the unaugmented exact-root carrier than the proved zero-root theorem above.

Accordingly the exact-root route should be elevated further:

> For every hypothetical counterexample with \(\kappa_2(H)\ge2\), exact-root topology reaches the symmetric zero-root branch immediately. There is no genuine nonzero \(k=2\) equality branch to analyze.

The load-bearing problem is therefore entirely the balanced canonical partial cover
\[
P_\pi\mid X_\pi\mid Q_\pi,
\qquad
|P_\pi|=|Q_\pi|,
\qquad
|X_\pi|=\delta(\pi)\ge\kappa_2(H),
\]
and, ideally, forcing such a zero-root chamber with
\[
|X_\pi|=\kappa_2(H).
\]

This correction supersedes the previous audit text and removes the proposed four-anchor \(k=2\) equality problem.
