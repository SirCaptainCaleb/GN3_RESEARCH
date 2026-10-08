# Exact-root surplus forces deletion distance at most five — preserved pre-item development

## Exact-root surplus forces deletion distance at most five

Let
\[
k=\kappa_2(H)\ge1,qquad m=n-2.
\]
For every spanning order \(\pi\), write
\[
p=p(\pi),\qquad c=c(\pi)=m+1-q(\pi).
\]
By the deletion-distance identity,
\[
d_2(\pi)=m-p-c\ge k
\]
for every chamber of a counterexample. Hence
\[
p+c\le m-k.
\]
Since \(p,c\ge1\), every coordinate occurring in an exact root
\[
\psi(\pi)=e_p-e_c
\]
belongs to
\[
\{1,\ldots,m-k-1\}.
\]
Therefore the exact-root image lies in the type-A root space on at most \(m-k-1\) coordinates, of dimension at most
\[
m-k-2.
\]

Now prescribe any set
\[
S\subseteq V(H),qquad |S|=k+2.
\]
For each \(z\in S\), let
\[
\rho_z(\pi)\in\{+1,0,-1\}
\]
record whether \(z\) lies in the canonical left path, deletion hole, or canonical right path associated with \(\pi\). Reversal exchanges the two path roles and fixes the hole role, so
\[
\rho_z(\pi^{\rm rev})=-\rho_z(\pi).
\]

Augment the exact-root map by these \(k+2\) role coordinates. Its target dimension is at most
\[
(m-k-2)+(k+2)=m.
\]
The domain is the antipodal permutation sphere \(S^m\). Borsuk--Ulam therefore supplies a zero. Taking the minimal barycentric carrier face \(F\) of such a zero gives strictly positive chamber weights with

1. exact-root balance; and
2. zero weighted role average for every \(z\in S\).

Assume first that \(F\) has no zero exact root. Apply the bounded-central-block theorem from [[topological_recurrence_to_local_gn3_structure_subsection_e]]. It gives one central face block \(B\) with
\[
|B|\le7,
\]
while the numbers \(\ell,r\) of positions before and after \(B\) satisfy
\[
\ell,r\in\{s,s+1\},qquad
s=\min_{\pi\in\mathcal V(F)}\min\{p(\pi),c(\pi)\}.
\]

Every vertex in a block strictly before \(B\) is uniformly in the canonical left path throughout \(F\): indeed every chamber has \(p\ge s\), so every position at most \(s+1\), and hence every position before \(B\), lies in the left path. Symmetrically every vertex strictly after \(B\) is uniformly in the canonical right path.

Consequently an anchor \(z\in S\) cannot lie outside \(B\), because its role would then be constantly \(+1\) or constantly \(-1\), contradicting its zero weighted role average. Thus
\[
S\subseteq B.
\]
Since \(|S|=k+2\) and \(|B|\le7\),
\[
k+2\le7.
\]
Therefore
\[
\boxed{\kappa_2(H)\le5}
\]
unless the augmented zero carrier already contains a zero exact-root chamber.

The zero-root alternative is not a failure of the reduction. A zero root has
\[
p=c,
\]
so it is a symmetric canonical deletion cover whose hole has order
\[
d_2(\pi)=m-2p.
\]
Thus the grand conjecture is reduced to two bounded fronts:

- a nonzero exact-root carrier with \(\kappa_2(H)\le5\); or
- a symmetric zero-root deletion cover, again with minimum deletion distance at most five once the above argument is applied at minimum \(k\).

This route uses one consistent order-relative predicate throughout and does not invoke dual-polarity witness protection or terminal two-cover surgery. It therefore bypasses the polarity mismatch identified in [[audit_terminal_surgery_and_compression_use_different_witness_polarities]].

### Sharpening at the top value

If \(k=5\) and the carrier has no zero root, then the central-block parameters are forced. Positive deficiency gives
\[
L=m-2s\ge k+1=6.
\]
The anchor condition gives \(|B|\ge7\), so \(|B|=7\). The mixed \((\alpha,\beta)=(1,2),(2,1)\) cases are impossible by the table in the bounded-central-block theorem, and the \((2,2)\) case would require \(L=5\), contradicting \(L\ge6\). Hence necessarily
\[
\alpha=\beta=1,qquad L=|B|=7,qquad \ell=r=s+1.
\]
Moreover every root satisfies, after translating \(p=s+a,c=s+b\),
\[
a+b\le L-k=2.
\]
Thus any remaining nonzero \(k=5\) carrier is confined to the four root types
\[
(0,1),(1,0),(0,2),(2,0),
\]
while \((1,1)\) is exactly the zero-root branch. This is a finite seven-block interface for the next repair step.
