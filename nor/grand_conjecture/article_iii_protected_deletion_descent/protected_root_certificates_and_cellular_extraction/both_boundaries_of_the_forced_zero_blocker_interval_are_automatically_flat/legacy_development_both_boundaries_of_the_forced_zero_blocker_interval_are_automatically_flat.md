# Both boundaries of the forced-zero blocker interval are automatically flat — preserved pre-item development

## Both boundaries of the forced-zero blocker interval are automatically flat

Continue with §360.

Let
\[
Q=(q_1,\ldots,q_m)
\]
be a monochromatic zero connector containing the consecutive edge \(x,z\), and let \(a\in A\setminus V(Q)\) fail every direct insertion.

Write
\[
s_i=\alpha(a,q_i,q_{i+1}).
\]
Let
\[
s_\ell=s_{\ell+1}=\cdots=s_r=0
\]
be the maximal zero-run containing the distinguished \(xz\)-edge.

Because the failed scan starts and ends with \(1\),
\[
s_{\ell-1}=1,\qquad s_{r+1}=1
\]
whenever both boundaries are interior.

We show that both blocker boundaries are flat tetrahedra.

### Left boundary

Consider the ordered four-set
\[
(a,q_{\ell-1},q_\ell,q_{\ell+1}).
\]
Its consecutive statuses are
\[
\alpha(a,q_{\ell-1},q_\ell)=s_{\ell-1}=1,
\]
and
\[
\alpha(q_{\ell-1},q_\ell,q_{\ell+1})=0
\]
because \(Q\) is monochromatic zero.

Thus this is a \(1\to0\) transition.

One off-face is
\[
\alpha(a,q_\ell,q_{\ell+1})=s_\ell=0.
\]
Coboundary flatness on the four-set gives the other off-face:
\[
1\oplus0\oplus
\alpha(a,q_{\ell-1},q_{\ell+1})
\oplus0
=0,
\]
hence
\[
\alpha(a,q_{\ell-1},q_{\ell+1})=1.
\]

So the off-face pair is
\[
(1,0),
\]
which is the FLAT pattern for a \(1\to0\) transition.

### Right boundary

Consider
\[
(q_r,q_{r+1},q_{r+2},a).
\]
Its consecutive statuses are
\[
\alpha(q_r,q_{r+1},q_{r+2})=0
\]
and, by cyclic invariance,
\[
\alpha(q_{r+1},q_{r+2},a)=s_{r+1}=1.
\]
Thus this is a \(0\to1\) transition.

One off-face is
\[
\alpha(q_r,q_{r+1},a)=s_r=0.
\]
The tetrahedral parity identity forces the other to be \(1\). Hence the off-face pair is
\[
(0,1),
\]
the FLAT pattern for a \(0\to1\) transition.

Therefore
\[
\boxed{\text{both boundaries of the distinguished blocker interval are flat}.}
\]

### Consequence

A first failure of direct vertex absorption into a compatible zero connector cannot terminate in local full curvature.

Instead it creates a genuine two-sided flat repair corridor surrounding the forced \(xz\)-zero.

Thus the connector-growth problem has a reversible local state space:

- the central \(xz\)-edge remains a forced zero;
- the left and right blockers are movable flat boundaries;
- any terminal obstruction must arise only after a finite sequence of boundary transports, not at the first failed insertion.

This supplies the missing local reversibility required by the Hartman least-unreachable program. The next target is component invariance: show that transporting either flat blocker cannot destroy reachability of the opposite blocker or the protected \(xz\)-edge.
