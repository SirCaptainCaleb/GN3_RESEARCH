# Elevation: four-vertex exact-root compression sharpens the surplus bound to two — preserved pre-item development

## Elevation: the four-vertex central theorem sharpens the exact-root surplus bound

Let
\[
k=\kappa_2(H)\ge1,\qquad m=|V(H)|-2.
\]
For every spanning order \(\pi\), the deletion-distance identity gives
\[
d_2(\pi)=m-p(\pi)-c(\pi)\ge k.
\]
Hence every coordinate occurring in the exact root
\[
\psi(\pi)=e_{p(\pi)}-e_{c(\pi)}
\]
lies in
\[
\{1,\ldots,m-k-1\},
\]
so the exact-root image has dimension at most
\[
m-k-2.
\]

Choose any prescribed set
\[
S\subseteq V(H),\qquad |S|=k+2,
\]
and augment the exact-root map by the \(k+2\) canonical role coordinates
\[
\rho_z\in\{+1,0,-1\}\qquad(z\in S),
\]
recording left-path, hole, and right-path membership. Reversal negates all these coordinates. The total target dimension is at most
\[
(m-k-2)+(k+2)=m,
\]
equal to the dimension of the antipodal permutation sphere. Therefore Borsuk--Ulam supplies a positive carrier face \(F\) with exact-root balance and zero weighted role average for every \(z\in S\).

Assume \(F\) contains no zero exact-root chamber. The later strengthened exact-root compression theorem in [[exact_root_compression_and_bounded_central_structure]] improves the central block bound used in [[exact_root_surplus_forces_deletion_distance_at_most_five]] from seven to four:
\[
|B|\le4.
\]
Every face block strictly before \(B\) lies uniformly in the canonical left path throughout \(F\), and every face block strictly after \(B\) lies uniformly in the canonical right path. Hence no anchored vertex \(z\in S\) can lie outside \(B\), since its role coordinate would then be constantly \(+1\) or constantly \(-1\), contradicting its zero positive average. Thus
\[
S\subseteq B.
\]
Consequently
\[
k+2=|S|\le |B|\le4,
\]
and therefore
\[
\boxed{k\le2.}
\]

Equivalently:

> If \(\kappa_2(H)\ge3\), every positive carrier of the augmented exact-root/role map contains a zero exact-root chamber.

This is a strict strengthening of [[exact_root_surplus_forces_deletion_distance_at_most_five]], whose numerical bound \(k\le5\) came from the older \(|B|\le7\) compression.

### Strategic consequence

The exact-root route now separates the grand theorem into only two layers:

1. the nonzero recurrent branch can occur only at deletion distance \(k\le2\);
2. for every hypothetical counterexample with \(k\ge3\), topology necessarily enters the symmetric zero-root branch.

Thus there is no reason to spend further effort on high-deletion-distance nonzero root cycles. The load-bearing target is the zero-root chamber
\[
p=c,
\]
i.e. the balanced canonical partial cover \(P\mid X\mid Q\) with \(|P|=|Q|\), together with the already-small \(k=1,2\) nonzero residues.

No minimum-counterexample or disturbance hypothesis is used; this is only the old surplus argument recomposed with the newer four-vertex central compression.
