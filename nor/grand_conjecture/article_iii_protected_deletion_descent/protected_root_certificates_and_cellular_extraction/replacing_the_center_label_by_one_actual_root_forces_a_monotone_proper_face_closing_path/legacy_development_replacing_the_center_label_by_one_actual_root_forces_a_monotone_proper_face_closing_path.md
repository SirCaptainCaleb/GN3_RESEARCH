# Replacing the center label by one actual root forces a monotone proper-face closing path — preserved pre-item development

## Development

Let P be the centered permutahedron in the type-A space W, and work in a minimum-coordinate ternary counterexample.

By root 139, the all-refinements actual-10-root carrier H is nonzero on the entire boundary of P. On every proper face its vectors lie strictly in the inward face-normal halfspace, and the normalized boundary map has the nonzero degree of the inward radial map.

The standard barycentric extension labels the top-face barycenter by zero and therefore puts all degree at the tautological center. Replace only that interior label.

Choose any genuine actual 10 root
r_0=e_s-e_t
from any full coordinate order of the counterexample. Since every bad binary word has at least two changes, such a 10 descent exists. Label the barycenter o of the top face P by r_0 rather than zero. Keep every proper-face barycentric label exactly as in H, and extend affinely over the cone decomposition
sd(P)=o * sd(partial P).

Call the resulting PL map F:P->W.

Its boundary restriction is exactly H, so F cannot be zero-free: otherwise F/||F|| would extend the nonzero-degree normalized boundary map over the ball P. Therefore F has a zero.

No zero lies on partial P because H is boundary-zero-free, and the apex value r_0 is nonzero. Hence any zero lies in a cone simplex with strictly positive apex coefficient. Let its minimal supporting simplex have proper-face chain
F_0<...<F_k
and positive coefficients
lambda_0 for r_0 and lambda_i for the proper-face barycentric root averages g_{F_i}.
Then
lambda_0 r_0 + sum_i lambda_i g_{F_i}=0,
with lambda_0>0 and some lambda_i>0.

Expand every g_{F_i} into its defining positive average of actual 10 roots. All those actual roots are carried by orders refining the largest proper face
G=F_k.
Thus one obtains a positive physical-root dependence
lambda_0 r_0 + sum_j mu_j rho_j=0,
mu_j>0,
where every rho_j is an actual 10 root from a refinement of ONE proper permutahedron face G.

Let
G=B_1|...|B_m
and let phi be the strictly increasing block-rank functional from root 139. Every rho_j has
phi(rho_j)>=0.
Moreover the barycentric label g_G occurs with positive coefficient in the minimal simplex and satisfies
phi(g_G)>0.
Hence
phi(r_0)<0.

Therefore the source s of r_0 lies in a strictly LATER block of G than its target t.

Interpret the roots as directed graph edges: e_a-e_b is the directed edge a->b. The boundary roots rho_j are weakly monotone forward in the ordered block quotient, whereas r_0 is a single backward edge s->t.

The dependence equation says that the positive boundary-root flow has net divergence
-lambda_0 r_0=lambda_0(e_t-e_s).
By standard flow decomposition, it contains a directed path
t=x_0 -> x_1 -> ... -> x_l=s
using actual descent roots rho_j. Every step is weakly forward in the G-block order, and at least one step crosses a block boundary. Together with the single backward actual root
s->t=r_0,
this forms a positive directed physical-root cycle.

Thus the nonzero boundary degree has a non-tautological combinatorial extraction:

For EVERY chosen actual 10 root r_0, there exists a proper permutahedron face G and a monotone directed path of actual 10 roots carried by refinements of G that closes r_0.

This construction requires no odd interior extension and has no fixed-center zero. It uses topology only through the certified nonzero degree on the proper boundary.

Remaining provenance issue: the path roots are actual descents in possibly different refinements of G; the theorem does not yet make consecutive path edges occur in compatible witness states. The next extraction problem is therefore a monotone common-face path gluing problem, substantially narrower than arbitrary root cancellation.
