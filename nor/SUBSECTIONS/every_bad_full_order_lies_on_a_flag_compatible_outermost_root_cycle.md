# Every bad full order lies on a flag-compatible outermost-root cycle

## Metadata

- ID: every_bad_full_order_lies_on_a_flag_compatible_outermost_root_cycle
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 244
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Every bad full order lies on a flag-compatible outermost-root cycle

Assume the outermost-change boundary carrier D from the preceding subsection and suppose the ambient instance is a counterexample.

Fix an arbitrary bad full order pi_* and write
rho_*=D(pi_*).

Triangulate the boundary of the permutahedron by its barycentric subdivision. At the barycenter of each proper face F use the concrete proper-face witness pi_F and label it by D(pi_F). By the face-normal argument, the resulting piecewise-linear boundary map is zero-free and has nonzero degree after radial normalization.

Now cone the entire boundary triangulation to one interior vertex o. Give o the label rho_*, and extend affinely over every cone simplex.

If this coned map were zero-free, radial normalization would extend the nonzero-degree boundary map across the ball, impossible. Therefore some cone simplex contains a zero.

Such a cone simplex has vertices
o, F_0, ..., F_t
where F_0<...<F_t is one flag of proper faces. Hence there are nonnegative coefficients, with the coefficient of o positive, such that
lambda_* rho_* + sum_i lambda_i D(pi_{F_i}) = 0.
The center coefficient is positive because every boundary simplex is already zero-free.

All nonzero labels here are type-A roots e_x-e_y.

### Minimal root dependence

Take a support-minimal positive subdependence that still contains rho_*.
A positive dependence among directed type-A roots is a balanced directed flow on the physical coordinates. Support minimality forces its directed support to be one simple directed cycle: if a balanced positive flow had more than one directed cycle, subtracting a positive multiple of one cycle would leave a smaller positive dependence. Along a simple directed cycle all coefficients are equal by flow conservation at each cycle vertex.

Therefore there exist distinct physical coordinates
x_0,x_1,...,x_{m-1}
such that, after cyclic indexing,
rho_*=e_{x_0}-e_{x_1}
and every remaining cycle edge
e_{x_i}-e_{x_{i+1}}
is the outermost-change root of a proper-face witness pi_{F_j} from the SAME nested face flag.

### Consequence

For every chosen bad full order, its outermost defect root belongs to a directed physical cycle completed entirely by proper-subinstance witnesses carried by one compatible flag.

This is substantially stronger than an arbitrary positive dependence. The proper-face witnesses in the return path are mutually flag-compatible, and their outside block orders come from the fixed selector g(S). Thus the remaining realization problem can be stated as a flag-cycle splice theorem:

Given a bad full order whose outermost root is x_0->x_1 and a nested-face return path
x_1->x_2->...->x_0
of outermost roots from canonical proper-face witnesses, produce a spanning NOR-good order or a strict admissible witness improvement.

No averaged-label provenance or arbitrary circuit-cell realization is needed for this reduction.

## Frontier

- Development version when composed: None
- Development version now: 1
