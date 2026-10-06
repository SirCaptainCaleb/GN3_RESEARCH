# Direct failed-restoration reversals are impossible at an equitable global minimum

## Metadata

- ID: direct_failed_restoration_reversals_are_impossible_at_an_equitable_global_minimum
- Parent Section: article_vii_synthesis_and_exact_frontier
- Position: 124
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## The direct failed-restoration reversal cannot recur at an equitable global \(\Phi\)-minimum

Let
\[
T=C\mid D\mid\{z\}
\]
be a globally \(\Phi\)-minimal spanning three-cover of a no-two-cover boundary tournament, in the direct-mixing setup of [[path_disturbance_endpoint_reversal_descent_or_an_omission_swap]].

Assume the surviving vertices of the distinguished path
\[
R=(z,r_1,\ldots,r_m)
\]
form one inherited-order terminal block
\[
B=(r_1,\ldots,r_m)
\]
of \(C\), and that the theorem reaches its direct endpoint-reversal branch. Thus
\[
C=L,B
\]
with \(L\ne\varnothing\), writing \(w\) for the last vertex of \(L\), and
\[
(w,z,r_1)
\]
is non-tight. Hence
\[
(r_1,z,w)
\]
is tight and reverses the initial edge \(zr_1\) of \(R\).

Put
\[
\ell=|L|,\qquad b=|B|=m,\qquad d=|D|.
\]
Besides the comparison three-cover
\[
C\mid D\mid\{z\},
\]
there is an immediate spanning three-cover
\[
R\mid L\mid D.
\]
Indeed \(R=(z,B)\) is the original tight path, \(L\) is an inherited initial subpath of \(C\), and \(D\) is unchanged.

Its potential difference is
\[
\begin{aligned}
\Delta\Phi
&=(b+1)^2+\ell^2+d^2-\bigl((b+\ell)^2+d^2+1\bigr)\\
&=2b(1-\ell).
\end{aligned}
\]

Since \(b\ge1\) and the original cover is globally \(\Phi\)-minimal,
\[
\Delta\Phi\ge0.
\]
Therefore
\[
\boxed{\ell=1}.
\]
Consequently the alternative cover
\[
R\mid\{w\}\mid D
\]
has the same global minimum potential.

Now assume, as in the unresolved branch of [[longest_paths_and_reversal_structure_reversals_are_unavoidable_subsection_c]], that every global \(\Phi\)-minimum has one of the near-equitable profiles
\[
(r,r,r),\qquad(r,r,r+1),\qquad(r,r+1,r+1).
\]
A global minimum containing a singleton component therefore has all three component orders at most two. Hence the whole tournament has order at most six.

Thus, in any tournament of order greater than six satisfying the near-equitable global-minimum conclusion,

> the direct failed-restoration endpoint-reversal branch of the disturbance theorem is impossible at a global \(\Phi\)-minimum.

Equivalently, once the marked-reversal reduction has reached an equitable global minimum, a direct mixed-edge comparison cannot regenerate the external-reversal interface through the theorem's terminal failed-restoration case. It must instead yield a split/leave-and-return disturbance, a two-cover, strict descent, or a neutral omission swap; the neutral branch is already absorbed by the later omission-swap lemmas.

This gives a genuine monotonicity improvement in the external-reversal recurrence: one entire mechanism by which a mixed comparison returned to an external reversal is eliminated at global minimum.
