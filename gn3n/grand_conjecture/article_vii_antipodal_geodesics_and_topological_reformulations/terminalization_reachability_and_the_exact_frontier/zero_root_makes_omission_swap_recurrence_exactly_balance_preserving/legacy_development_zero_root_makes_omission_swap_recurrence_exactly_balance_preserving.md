# Zero root makes omission-swap recurrence exactly balance-preserving — preserved pre-item development

## Composition

(none yet)

## Development

Let H be a minimum counterexample on n=2r+1 vertices and let F_x=P|Q be a balanced deletion cover of H-x, |P|=|Q|=r, supplied by the zero exact-root theorem. For each label v choose a deletion cover F_v of H-v minimizing the two-component quadratic potential, and choose F_x to be the balanced one.

The singleton lift F_x|{x} has
Phi=2r^2+1.
This is the absolute minimum possible value of Phi among ALL singleton lifts on n vertices: every deletion cover has component orders a,2r-a, and a^2+(2r-a)^2 is minimized uniquely at a=r.

Consequently, in [[balanced_omission_swap_gives_descent_or_selected_singleton_recurrence]], the strict-descent alternative is impossible for any omission swap reachable from F_x|{x} without first increasing Phi. Every selected singleton lift reached on that Phi level must again have deletion component orders r|r.

Thus the zero-root state defines a balance-preserving omission-swap component: every hole label reachable by neutral omission swaps has a selected balanced deletion cover, and all such singleton lifts lie at the common absolute minimum 2r^2+1.

In particular any neutral recurrence starting from the zero root can be studied entirely inside the uniform-size support graph whose vertices are r-sets and whose selected cover edges join disjoint r-sets with one omitted label. Containment alternatives disappear in this component. The remaining exits are genuine two-cover, order/reversal disturbance, bounded Hamiltonian support with two-coverable complement, or escape to a new balanced omitted label.
