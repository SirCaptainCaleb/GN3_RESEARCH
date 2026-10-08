# Correction: exact violations, fixed centers, and positive windows — preserved pre-item development

## Correction: absolute positive windows and auxiliary radii coincide only at fixed center

The first lemma below remains valid chamberwise, but the former large-radius same-face theorem was too strong because it silently treated radius coordinates as fixed absolute positions across a face.

Write an auxiliary chamber as
\[
\pi=(\ldots,r,\ldots)
\]
and let \(x_d,y_d\) be the established equal-radius violation bits.

**Lemma (ordinary nearest violations produce positive endpoint words).**
For one fixed chamber, if \(d\ge2\) is its nearest violating radius, then
\[
(x_d,y_d)=(1,0)
\]
produces a left positive word \(011\), while
\[
(x_d,y_d)=(0,1)
\]
produces a right positive word \(001\). In that chamber the two corresponding absolute start positions, when both are considered, are separated by \(2d\).

The proof is unchanged: all smaller left statuses are \(1\), all smaller right statuses are \(0\), and at radius two the innermost statuses are the forced auxiliary statuses ending at and beginning at \(r\).

What fails is transporting those absolute windows from one chamber of a face to another when \(r\) belongs to a non-singleton face block. Swapping \(r\) with an original vertex changes which absolute old triple is called radius \(d\). As shown explicitly in [[moving_the_auxiliary_center_can_reverse_arbitrary_large_nearest_radii_without_same_face_escape]], a two-chamber face can have ordinary nearest labels \(+d\) and \(-d\) for arbitrarily large \(d\), while the same absolute left \(011\) and right \(001\) occurrences persist in both chambers. The separated-window theorem then returns its persistent-orientation alternative, not an outward chamber.

Therefore the former claim
\[
\text{opposite ordinary labels at }d\ge4
\Longrightarrow
\text{same-face greater-radius chamber}
\]
is false without a fixed-center hypothesis.

**Fixed-center version.**
If the position of \(r\) is fixed throughout a protected face—for example \(r\) is a singleton face block—then the radius-\(d\) determining windows occupy fixed absolute positions. In that situation, for \(d\ge4\), ordinary left-only and right-only radius-\(d\) chambers give the two opposite fixed positive occurrences with start separation \(2d\ge8\). The theorem [[separated_protected_determining_windows_force_a_persistent_witness_or_same_face_escape]] then does give a chamber with neither radius-\(d\) occurrence.

This fixed-center statement is valid but is not by itself the strategic closure, because singleton-\(r\) zero carriers are already closed by the singleton carrier conversion theorem.

The useful surviving elevation is instead twofold:

1. [[bounded_radius_auxiliary_neighborhoods_have_exact_outward_replacements]] gives a center-preserving explicit replacement for every nearest radius \(d\le3\);
2. large-radius cancellations caused only by moving \(r\) should be treated as **fiber motion of the auxiliary center**, not as new absolute positive-witness geometry.

Thus the next exact-violation attack should quotient or control the \(r\)-motion fibers, while the fixed-position positive-witness separator machinery handles genuine changes of absolute determining windows.
