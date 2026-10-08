# Endpoint barriers force a rank-two protected root cycle with unit cut defects — preserved pre-item development

## Composition

(none yet)

## Development

Work in a minimum ternary counterexample in the coboundary-flat alternating sector, in the endpoint regime where the standard normalized deletion witness has both phases nonempty and the canonical endpoint tetrahedron is fully curved.

For every coordinate x choose one good order of V minus {x} and normalize it as
O_x=(a_x,b_x,c_x,...) with word 0^{p_x}1^{q_x}.
Prepending x gives the endpoint-defect word 1,0^{p_x},1^{q_x}. The first transition is supported on
(x,a_x,b_x,c_x).
The endpoint full-curvature theorem therefore supplies the actual protected slide root
rho_x=e_x-e_{c_x}.

By the central-cut theorem, this root carries the rank-two cut
C_x={x,a_x},
and its forced Johnson successor is
C_x^+={a_x,c_x}.

Define f(x)=c_x. Since all coordinates in the deletion order are distinct and x is omitted, f(x) is never x. Thus f is a self-map of the finite coordinate set without fixed points and its functional digraph contains a directed cycle
x_0 -> x_1 -> ... -> x_{k-1} -> x_0,
where x_{i+1}=f(x_i).

The associated actual endpoint barrier roots satisfy
rho_i=e_{x_i}-e_{x_{i+1}},
so
sum_i rho_i=0.
Hence minimum-counterexample endpoint geometry already forces a positive physical protected-root cycle; no topological zero theorem is needed merely to obtain physical root cancellation.

The cut provenance of this cycle is particularly simple. Write
C_i={x_i,a_i}.
The forced successor of C_i along rho_i is
C_i^+={x_{i+1},a_i},
while the next attained endpoint cut is
C_{i+1}={x_{i+1},a_{i+1}}.
Therefore the cut-defect vector is
D_i=1_{C_{i+1}}-1_{C_i^+}=e_{a_{i+1}}-e_{a_i}.
Consequently
sum_i D_i=0
automatically, and every nonzero defect has Johnson distance one. The secondary cut-defect circulation is exactly the coordinate walk of the partner sequence
a_0,a_1,...,a_{k-1},a_0.

Thus the endpoint-induced root cycle has rank-two cut provenance and unit local defects. Zero defect at step i is equivalent to a_{i+1}=a_i. If all partners are equal, the attained cuts concatenate exactly as the one-token Johnson cycle with common core {a}. If the partners vary, the entire incompatibility is encoded by a second ordinary coordinate circulation rather than by arbitrary multi-token Johnson defects.

This gives a new closure target: choose the endpoint witnesses so that a functional-cycle component minimizes the number of partner changes. Either the partner is constant and one obtains an exact realized Johnson cycle, or the partner-defect circulation supplies a strictly simpler secondary object whose relation to endpoint witnesses can be attacked directly.

The theorem concerns the flat alternating minimum-counterexample sector where the endpoint full-curvature root is established. It does not assert the same functional map for unrestricted basepoint-dependent colorings.
