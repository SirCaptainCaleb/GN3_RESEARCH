# Window-slide roots form a forest and adjacent walls have one transverse direction

## Composition

For an order pi of n coordinates and arity r>=2, the window-slide vectors e_{v_i}-e_{v_{i+r}} form r disjoint coordinate paths. They are a forest basis of rank n-r, and their span consists of vectors with zero sum on each position-residue class. Thus distinct actual window certificates in one order are independent even with arbitrary signs. An adjacent swap of a,b changes each affected slide vector by plus or minus e_a-e_b; modulo the old span this is the sole possible new direction. If at least one swapped vertex has an incident slide edge, the two chamber spans have union rank n-r+1 and intersection rank n-r-1. This gives an explicit endpoint-incidence and sign test for transverse certificates at cut-changing carrier walls. It does not prove a usable bad-window certificate exists at every such wall or yield termination without actual order-changing surgery.

## Development

## Window-slide roots form a forest, and an adjacent chamber wall has one transverse direction

Let pi=(v_1,...,v_n) be an order of distinct coordinates and let r>=2 be the coordinate arity, with n>=r+1. Consecutive r-windows have dropped/entering-coordinate vectors
f_i=e_{v_i}-e_{v_{i+r}}, 1<=i<=n-r.
This statement concerns actual window-slide vectors, not omitted-coordinate exchange labels.

### Theorem 1: fixed-order independence
The n-r vectors f_i are linearly independent. Any subset, with arbitrary nonzero signs, is independent.

Proof. The coordinate graph joins positions i and i+r. It is the disjoint union of r paths, one for each position residue modulo r. Its incidence vectors form a forest basis. More explicitly, a linear dependence can be read from the first vertex in each path; its incident coefficient is zero, and successive leaf removal annihilates all coefficients. Hence all coefficients vanish.

Let C_t={v_j:j=t mod r}, t=1,...,r, with residue r denoting zero. The span W_pi is exactly
{z in R^V : sum_{v in C_t} z_v=0 for every t}.
Its dimension is n-r.

Consequences. No collection of distinct protected window roots from one fixed order admits a signed dependence, much less a positive dependence. Repeating one barrier certificate does not supply a new graphic circuit. The root-rank alternative in the current barrier process therefore needs an actual transition to another order before it can add information. This is stronger than the mere common-halfspace obstruction.

### Theorem 2: one transverse direction at an adjacent wall
Let pi' be obtained by swapping adjacent coordinates a=v_j and b=v_{j+1}, and put u=e_a-e_b. Then
W_pi' subset W_pi + span(u).
Every changed window-slide vector is its old counterpart plus u or minus u; unchanged vectors agree.

Proof. An affected f_i has a or b as one endpoint. Since its endpoints have rank distance r>=2, they cannot both be the two adjacent swapped positions. Replacing that endpoint changes f_i by plus or minus u. The inclusion follows.

The two adjacent positions have different residues modulo r. Thus u is not in W_pi: its sums on those two residue classes are +1 and -1. If at least one of a,b has an incident old window-slide edge (equivalently, at least one of their residue paths has more than one vertex), a changed f_i exists. Then its counterpart belongs to W_pi' and its old value belongs to W_pi, so u belongs to W_pi+W_pi'. Consequently
W_pi+W_pi'=W_pi+span(u),
dim(W_pi+W_pi')=n-r+1,
dim(W_pi intersection W_pi')=n-r-1.
If both residue paths are singleton vertices, no slide edge changes and W_pi'=W_pi.

### Certified quotient labels at a carrier wall
For a particular actual window-slide certificate rho' in pi', its image modulo W_pi is either zero or plus/minus [e_a-e_b]. The nonzero case can be decided directly: the slide must use exactly one of the swapped coordinates as an endpoint. Thus an adjacent chamber wall introduces at most one new root-space direction, and that direction is the physical swap itself.

This supplies a concrete compatibility check for a proposed protected-root carrier. List the actual before/after bad windows. Identify their roots f_i with the color-dependent signs required by the chosen labeling. Then compute the coefficient of [e_a-e_b]. A transverse root cannot be inferred merely from an omitted-coordinate exchange cycle or from an abstract positive dependence.

If a wall also exchanges cut membership of a and b, its nonzero quotient direction matches the cut-changing exchange direction up to a sign whose value must be checked. This narrows the first-ejection extraction problem of root subsection 20 to an explicit local certificate test. It does not show that every such wall carries a usable bad window or that its sign is the one needed for surgery.

### Closure obligation
A complete barrier process still needs a legal move after a full barrier, preservation of the allowed threshold/provenance state, and sign-compatible extraction from roots spanning multiple orders. The present lemmas establish independence within each order and identify the sole new direction at a single wall; they do not turn root accumulation alone into termination.
