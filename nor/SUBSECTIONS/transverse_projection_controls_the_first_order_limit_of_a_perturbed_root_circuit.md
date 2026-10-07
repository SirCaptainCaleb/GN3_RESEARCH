# Transverse projection controls the first-order limit of a perturbed root circuit

## Metadata

- ID: transverse_projection_controls_the_first_order_limit_of_a_perturbed_root_circuit
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 75
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

For a perturbed simple physical cycle, normalize the zero coefficients to sum one. Projection onto the old root span determines a unique analytic positive coefficient adjustment near equal weights. A zero exists exactly when the remaining transverse moment equation vanishes. Hence the necessary first-order condition is the projection of the averaged moments onto the orthogonal complement of the old span; moments inside the span are absorbed by coefficient changes. For Hamiltonian support the old span is all W, the transverse equation disappears, and all small in-space perturbations retain a positive zero. Irrational separation can at most separate rational transverse limiting equations, not arbitrary finite-epsilon weights.

## Development

## Transverse projection controls the first-order limit of a perturbed root circuit

This develops the correct coefficient-sensitive replacement for equal-weight moment separation. It complements the arbitrary-perturbation stability theorem in root §68 and the audit in root §65.

Let
\[
\rho_i=e_{v_i}-e_{v_{i+1}},\qquad i=1,\ldots,k
\]
be one simple directed physical coordinate cycle, with distinct v_i and cyclic indexing. Put
\[
U=\operatorname{span}\{\rho_i\}\subseteq W,
\]
so dim U=k-1. Fix arbitrary moment vectors m_i in W and consider perturbed columns
\[
q_i(\epsilon)=\rho_i+\epsilon m_i.
\]
A normalized positive dependence has coefficients lambda_i>0, sum lambda_i=1. Let R and M denote the linear maps with columns rho_i and m_i, respectively, and let lambda^0=(1/k,...,1/k).

### Theorem

There is a unique analytic coefficient vector lambda(epsilon), for sufficiently small epsilon, satisfying
\[
\sum_i\lambda_i(\epsilon)=1,\qquad
P_U\big(R\lambda(\epsilon)+\epsilon M\lambda(\epsilon)\big)=0,
\]
with lambda(0)=lambda^0. Its entries remain positive.

A positive zero of all the perturbed columns exists for a sufficiently small nonzero epsilon if and only if this coefficient vector also satisfies
\[
P_{U^\perp}M\lambda(\epsilon)=0.
\]
In particular, if positive zeros occur for a sequence epsilon_j -> 0, then the necessary FIRST-ORDER condition is
\[
P_{U^\perp}\sum_i m_i=0.
\]
There is no necessary condition that the unprojected sum of moments vanish.

When k=n, U=W and the transverse equation is empty. Thus every sufficiently small perturbation has a positive dependence, independently of all provenance moments.

### Proof

Let
\[
A=\{a\in\mathbb R^k:\sum_i a_i=0\}.
\]
R restricted to A is an isomorphism A -> U: R has one-dimensional kernel spanned by the all-ones vector, and A intersects that kernel only at zero.

Write lambda=lambda^0+a. The projected equation becomes
\[
R_A a+\epsilon P_U M(\lambda^0+a)=0.
\]
For small epsilon, R_A+epsilon P_U M|_A remains invertible. Hence
\[
a(\epsilon)=
-\epsilon\big(R_A+\epsilon P_U M|_A\big)^{-1}P_U M\lambda^0.
\]
This is analytic near zero and tends to zero, establishing uniqueness and positivity.

Any normalized zero of the perturbed columns must solve this projected equation, hence must use exactly lambda(epsilon). Since the unperturbed columns lie in U, the remaining equation is epsilon P_{U^\perp}M lambda(epsilon)=0. This proves the equivalence.

Taking a sequence of zeros and passing to epsilon=0 gives
\[
P_{U^\perp}M\lambda^0=0,
\]
which is the claimed projected sum condition.

### First derivative and its meaning

The coefficient adjustment is
\[
\lambda'(0)=-R_A^{-1}P_U M\lambda^0.
\]
Thus the component of the averaged moment lying inside U is absorbed by a first-order change of the positive coefficients. Only its transverse component is a genuine first-order obstruction.

Vanishing of the first-order transverse component need not suffice: subsequent Taylor coefficients of P_{U^\perp}M lambda(epsilon) may obstruct exact zeros. These higher terms must be checked rather than replaced by equal-coefficient equations.

### Irrational moments: what can legitimately be separated

Suppose m_i=s_i(A_i+theta B_i), where A_i,B_i have rational coordinates, s_i are discrete signs, and theta is irrational. For a type-A coordinate cycle, the orthogonal projection onto U^\perp has rational entries. Therefore the limiting first-order equation may separate as
\[
P_{U^\perp}\sum_i s_i A_i=0,\qquad
P_{U^\perp}\sum_i s_i B_i=0.
\]
This uses the rational EQUAL limiting coefficients, not a claim that the finite-epsilon zero coefficients are rational.

It separates only the transverse equations. For a Hamiltonian cycle U=W both projections are zero, so irrationality imposes no moment restriction at all. In particular it cannot force uniform side labels or a regular cut-incidence design from an arbitrary Hamiltonian perturbed zero.

For coupled physical cycles the limiting kernel can have dimension greater than one and its positive weights need not be rational. Even this restricted irrational separation then needs additional justification.

### Consequence for carrier design

Provenance recorded inside the old root span can change zero weights without eliminating the zero. To enforce a new balance one must use transverse directions, a genuine lift, or constraints in the domain/cut state itself. The graphic rank filtration is therefore relevant to perturbation limits: rank saturation at U=W removes every transverse algebraic constraint, while unsaturated circuits admit a quotient-space obstruction. None of these algebraic equations automatically realizes a Johnson exchange or preserves outside order.
