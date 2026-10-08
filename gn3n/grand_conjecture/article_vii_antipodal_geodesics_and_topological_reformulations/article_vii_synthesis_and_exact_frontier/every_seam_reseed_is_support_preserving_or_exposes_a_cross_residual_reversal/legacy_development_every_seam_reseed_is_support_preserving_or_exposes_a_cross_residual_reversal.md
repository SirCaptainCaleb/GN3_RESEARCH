# Every seam reseed is support-preserving or exposes a cross-residual reversal — preserved pre-item development

## Composition

(none yet)

## Development

## Every seam reseed is support-preserving or exposes a cross-residual reversal

Let \(H\) be a no-two-cover boundary tournament and let
\[
S\mid P\mid Q
\]
be a displayed spanning three-cover. Let \(K\subseteq V(H)-S\) be a Hamiltonian seam support with
\[
\operatorname{pc}(H-K)\le2.
\]

Because \(K\) is cut from exposed endpoint segments of the displayed complementary paths, deleting \(K\) leaves at most two inherited contiguous residual paths. Write them
\[
C_1,\qquad C_2,
\]
omitting an empty interval. Thus
\[
H-K=S\mid C_1\mid C_2
\]
is an inherited three-cover whenever both residual intervals are nonempty.

We prove that the reseed branch always reduces to a support-preserving reseed or an explicit boundary reversal between the two residual paths.

### Empty residual interval

If one of \(C_1,C_2\) is empty, then immediately
\[
H-K=S\mid C
\]
for the other residual path \(C\). This is the support-preserving reseed of [[support_preserving_seam_reseeds_immediately_create_a_short_rail_state]].

Hence assume both \(C_1,C_2\) are nonempty.

### Try to concatenate the two residual paths

Write
\[
C_1=(a_1,\ldots,a_r),\qquad
C_2=(b_1,\ldots,b_s).
\]

If the displayed concatenation
\[
C_1C_2=(a_1,\ldots,a_r,b_1,\ldots,b_s)
\]
is tight, then
\[
\boxed{H-K=S\mid(C_1C_2)}
\]
is a support-preserving two-cover.

Likewise, if
\[
C_2C_1
\]
is tight, then
\[
\boxed{H-K=S\mid(C_2C_1)}
\]
is support-preserving.

Suppose neither concatenation is tight.

For \(C_1C_2\), every consecutive triple is inherited except the one or two junction triples
\[
(a_{r-1},a_r,b_1)\quad(r\ge2),
\qquad
(a_r,b_1,b_2)\quad(s\ge2).
\]
At least one existing junction triple is non-tight. Boundary antisymmetry therefore gives at least one tight reverse
\[
\boxed{(b_1,a_r,a_{r-1})}
\qquad\text{or}\qquad
\boxed{(b_2,b_1,a_r)}.
\]
Thus an exposed endpoint of one residual path reverses an exposed end edge of the other.

Applying the same argument to \(C_2C_1\) gives the opposite-orientation analogue
\[
\boxed{(a_1,b_s,b_{s-1})}
\qquad\text{or}\qquad
\boxed{(a_2,a_1,b_s)}.
\]

If one residual path is a singleton, the same conclusion holds whenever concatenation fails: the unique new junction triple is non-tight and its literal boundary reverse is tight. If both are singletons, their two-vertex concatenation is tight vacuously, so the support-preserving branch holds.

Therefore:

> **Reseed-to-reversal theorem.** Every seam support \(K\) with two-coverable complement yields either
> 1. a support-preserving reseed
>    \[
>    H-K=S\mid R,
>    \]
>    or
> 2. an explicit tight triple in which an endpoint of one inherited residual path reverses an exposed end edge of the other. If neither concatenation order works, such reversal certificates occur from both oriented residual seams.

Consequently the distinction between support-preserving and support-splitting *chosen* two-covers of \(H-K\) is not a genuine frontier. Even when a particular reseed cover splits \(S\), the inherited residual geometry itself either supplies a support-preserving reseed or an immediate positioned reversal.

Combined with [[support_preserving_seam_reseeds_immediately_create_a_short_rail_state]], seam reseeding reduces entirely to the short-rail regime or the already-established reversal/disturbance interface.

No minimum-counterexample hypothesis, cyclic rotation, path reversal, or finite computation is used.
