# The full permutahedron carries a canonical odd descent-root map with a forced zero — preserved pre-item development

## Development


Let h be a reversal-odd binary label on ordered r-tuples, and assume the full instance is a counterexample to one-change NOR.

Let P_V be the centered type-A permutahedron on the physical coordinates V. Its vertices are full coordinate orders

pi=(pi_1,...,pi_n),

and central inversion sends pi to pi^rev.

For pi write its sliding r-window word as

c_1,...,c_m,
m=n-r+1.

Since pi is not one-change, the binary word has at least two changes and therefore has at least one adjacent descent 10.

For every descent position i with

c_i=1,
c_{i+1}=0,

the two consecutive r-windows differ by dropping pi_i and entering pi_{i+r}. Associate the physical root

rho_i(pi)=e_{pi_i}-e_{pi_{i+r}}.

Define the canonical total descent-root label

R(pi)=sum_{i: c_i c_{i+1}=10} rho_i(pi)
in W_V={x in R^V: sum_v x_v=0}.

### Vertex labels are nonzero

For a fixed order pi define the linear functional

L_pi(e_{pi_j})=-j

(up to adding a constant, so it descends to W_V).

Every descent root satisfies

L_pi(e_{pi_i}-e_{pi_{i+r}})=r>0.

Hence

L_pi(R(pi))=r times #(10 descents)>0.

Therefore R(pi) is nonzero at every permutation vertex.

No tie-breaking among descents is used.

### Exact reversal oddness

Reversal oddness gives

c'_j=1-c_{m+1-j}

for pi^rev.

A 10 descent at i in pi becomes a 10 descent at the reversed adjacent position in pi^rev. Its dropped and entering physical coordinates are exchanged. Therefore

rho(pi^rev)=-rho(pi)

term by term, and hence

R(pi^rev)=-R(pi).

Thus R is an odd vertex labeling of the centrally symmetric permutahedron by the type-A root space W_V, whose dimension equals dim P_V=n-1.

### Canonical piecewise-affine extension

Take the barycentric subdivision of the face lattice of P_V.

For every nonempty face F define the label at its barycenter by the average of the labels of its permutation vertices:

R(F)=|Vert(F)|^{-1} sum_{pi in Vert(F)} R(pi).

For the opposite face -F, reversal pairs its permutation vertices with those of F, so

R(-F)=-R(F).

Extend linearly over every barycentric simplex.

This produces a continuous odd piecewise-affine map

R_tilde:P_V -> W_V.

### Forced zero

Suppose R_tilde avoided zero.

Then its restriction to the boundary could be normalized to an antipodal map

partial P_V ~= S^{n-2} -> S(W_V) ~= S^{n-2}.

Because R_tilde is defined on the whole permutahedral (n-1)-ball and avoids zero, this normalized boundary map extends over the ball.

But every antipodal self-map of S^{n-2} has odd degree, whereas a map extending over a ball has degree zero. Contradiction.

Therefore

0 belongs to R_tilde(P_V).

### The zero is a positive dependence of genuine protected roots in one face

Let a zero lie in a barycentric simplex corresponding to a chain of faces

F_0 subset ... subset F_k.

Each barycentric label R(F_j) is a positive average of R(pi) for permutation chambers pi refining F_j, hence refining the largest face F_k.

Each R(pi) is itself a positive sum of genuine physical descent roots e_a-e_c arising from actual consecutive 10 windows of pi.

Expanding the affine zero therefore gives a positive dependence

sum lambda_s (e_{a_s}-e_{c_s})=0,
lambda_s>0,

among genuine protected window-slide roots carried by chambers refining the single permutohedral face F_k.

The existing circulation theorem and Coxeter-block localization now apply: the positive dependence decomposes into directed physical-coordinate cycles, and each such cycle lies in one tied Coxeter block of F_k; all coordinates outside that block have fixed relative order.

### Significance

This supplies the previously missing global finite antipodal carrier/root map without selecting one descent, without choosing deletion witnesses coherently, and without a switch-prism triangulation.

The remaining extraction problem is purely local inside one Coxeter block:

given a support-minimal positive circuit of actual 10-descent roots carried by chambers of one block, produce a one-change order or perform a zero-removing surgery.

For ternary coboundary-flat NOR the two smallest circuits are exactly the already analyzed antipodal pair and directed A2 triangle.
