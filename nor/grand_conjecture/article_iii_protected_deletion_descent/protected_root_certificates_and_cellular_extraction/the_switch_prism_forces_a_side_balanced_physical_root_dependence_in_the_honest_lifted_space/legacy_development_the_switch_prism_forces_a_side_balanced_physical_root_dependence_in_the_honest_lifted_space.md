# The switch prism forces a side-balanced physical root dependence in the honest lifted space — preserved pre-item development

## Composition

(none yet)

## Development

## The switch prism forces a side-balanced physical root dependence in the honest lifted space

Let h be a reversal-odd ordered-r-tuple coloring on n physical coordinates and assume counterexamplehood: every full coordinate order has at least two color changes.

Use the switch prism

X=P_V x I,

where P_V is the centered type-A permutahedron and I parametrizes threshold cuts. X is an n-dimensional ball. Its boundary has the free involution

(x,t) -> (-x,-t),

corresponding to order reversal and complementary cut level.

At every discrete bad switch state z=(pi,k), select a violating r-window by any reversal-equivariant rule. If the selected window is

(v_i,...,v_{i+r-1}),

define its physical window root

rho(z)=e_{v_i}-e_{v_{i+r-1}} in W,

and define the side sign

s(z)=+1 if the violating window lies on the pre-switch side,
s(z)=-1 if it lies on the post-switch side.

Under reversal the selected window reverses and changes side, so

rho(-z)=-rho(z),
s(-z)=-s(z).

Thus the lifted label

Lambda(z)=(rho(z),s(z)) in W direct-sum R

is exactly odd.

### Degree theorem

Choose a centrally symmetric triangulation refining the switch-prism product structure. Extend labels to subdivision vertices by reversal-compatible convex averaging over incident state labels and extend affinely over every simplex. This gives a continuous map

F:X -> W direct-sum R,

whose boundary restriction is odd.

Since dim X=n and dim(W direct-sum R)=n, F must vanish.

Indeed, if F were zero-free, normalization would give a continuous map

F/||F||: X -> S^{n-1}.

Its boundary restriction is antipodal. Every antipodal self-map of S^{n-1} has odd degree, while any sphere map extending over the n-ball has degree zero, a contradiction.

Therefore some simplex of the refined switch prism carries a positive dependence of genuine state labels

sum_j lambda_j rho_j=0,
sum_j lambda_j s_j=0,
lambda_j>0.

So topology forces a SIDE-BALANCED physical root circulation, not merely a raw physical root zero.

### Localization

The block-rank halfspace argument from the root-only switch-prism theorem applies to the physical component unchanged. If the largest permutahedron face supporting the zero has every Coxeter block of size at most r-1, one linear functional is strictly one-signed on every rho_j, contradicting the physical zero.

Hence a lifted zero localizes to a face containing a block of size at least r.

For ternary arity, the first possible local carrier is therefore an A2 block, though a minimal zero may still require a larger block if side balance prevents cancellation in every A2 subcarrier.

### Why this is stronger than dimension-preserving provenance perturbation

The side coordinate is genuine and transverse to W. It is not a small perturbation that a Hamiltonian physical cycle can absorb by changing its positive coefficients. Any zero must satisfy exact weighted side balance.

This uses the extra interval dimension of the switch prism, which is precisely why the target W direct-sum R has the correct dimension for a degree obstruction.

### Remaining extraction problem

The lifted zero uses roots of violating WINDOWS, not automatically canonical deletion roots or terminal barrier roots. Closure therefore requires a local bridge from a support-minimal side-balanced violation-root dependence to one of:

- a switch-crossing endpoint repair;
- strict threshold-defect improvement;
- a protected deletion/root state already handled by Article III.

The set-valued cellular Tucker theorem and its arbitrary-cell repair theorem supply exactly this kind of local information for signed middle-coordinate labels. A useful next step is to combine the two carriers so that a minimal lifted-root zero inherits the controlled Tucker repair event.
