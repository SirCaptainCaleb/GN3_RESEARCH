# Audit: same Hall transfer polarity is not excluded by boundary antisymmetry — preserved pre-item development

## Composition

(none yet)

## Development

## Audit: same Hall transfer polarity is not excluded by boundary antisymmetry

The argument in [[isolated_hall_blocks_force_opposite_transfer_polarity_or_strict_potential_descent]] contains an invalid cyclic-rotation step, and [[opposite_hall_polarity_repairs_strong_imbalance_quadratic_descent]] therefore does not yet repair the directional gap.

In the notation
\[
A=(\ldots,u,v),\qquad B_j=(a_j,b_j,\ldots),
\]
with
\[
x_j=h(u,v,a_j),\qquad y_j=h(v,a_j,b_j),
\]
the branch \(x_1=x_2=0\) gives, by the boundary flip and only by the boundary flip,
\[
h(a_1,v,u)=h(a_2,v,u)=1.
\]
It does **not** imply
\[
h(v,u,a_2)=1.
\]
A boundary tournament distinguishes an ordered triple only from its boundary flip, obtained by exchanging the first and last entries; cyclic rotations are not equivalent orientations.

Consequently the displayed four-path
\[
(a_1,v,u,a_2)
\]
is not certified: its second triple \(h(v,u,a_2)\) is undetermined. Thus the proof does not exclude the possibility that both failed concatenations have the same \(x=0,y=1\) polarity.

The other same-polarity branch \(y_1=y_2=0\) is validly excluded by the common-reverser lemma, since then the common carrier \(v\) reverses the two disjoint initial edges \(a_1b_1\) and \(a_2b_2\).

Therefore the currently justified isolated-block conclusion is asymmetric:
- the \(y_1=y_2=0\) same-polarity pattern forces a Hamiltonian four-support;
- the \(x_1=x_2=0\) same-polarity pattern remains possible absent a separate argument;
- mixed polarities remain possible.

In particular, for a strongly imbalanced three-cover, the Hall obstruction does not yet force a transfer out of the dominant component. The claimed strict quadratic descent remains conditional on eliminating the surviving \(x_1=x_2=0\) polarity by a valid boundary-tournament argument.

This audit concerns only the polarity/directional claim. The basic four-path Hall obstruction theorem and the potential calculation for a transfer whose direction is already known remain valid.
