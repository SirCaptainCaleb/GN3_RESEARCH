# A perfect blocker has exactly one flat tetrahedron in its curvature tube

## Metadata

- ID: a_perfect_blocker_has_exactly_one_flat_tetrahedron_in_its_curvature_tube
- Parent Section: directed_nor_union_closed_bridge
- Position: 180
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development


Work in a minimum coboundary-flat pure-orientation ternary counterexample. Let

O=(v_1,...,v_m)

be a one-change deletion carrier with word

w=0^p1^q,

and let x be its omitted perfect blocker with scan

s=1^{p+1}0^q.

For each i let

Q_i={x,v_i,v_{i+1},v_{i+2}}.

The existing tube theorem proves Q_i fully curved for every i except possibly i=p+1.

The exceptional tetrahedron is in fact flat.

Indeed, in the ordering

(x,v_{p+1},v_{p+2},v_{p+3})

its two consecutive statuses are

alpha(x,v_{p+1},v_{p+2})=s_{p+1}=1,

alpha(v_{p+1},v_{p+2},v_{p+3})=w_{p+1}=1.

A fully-curved tetrahedron is a universal switch gadget: every ordering of its four vertices has opposite consecutive statuses. Therefore Q_{p+1} cannot be fully curved.

In the coboundary-flat sector every tetrahedron is either flat or fully curved. Hence Q_{p+1} is flat.

Consequently the perfect-blocker curvature tube is exact:

Q_1,...,Q_p are fully curved,
Q_{p+1} is flat,
Q_{p+2},...,Q_{p+q} are fully curved.

Thus all nontrivial curvature of the blocker scan is concentrated into one distinguished flat tetrahedron at the phase crossing. Any protected endpoint-defect surgery may use the full tubes on both sides and needs to solve only the passage through this unique flat center.


## Frontier

- Development version when composed: None
- Development version now: 1
