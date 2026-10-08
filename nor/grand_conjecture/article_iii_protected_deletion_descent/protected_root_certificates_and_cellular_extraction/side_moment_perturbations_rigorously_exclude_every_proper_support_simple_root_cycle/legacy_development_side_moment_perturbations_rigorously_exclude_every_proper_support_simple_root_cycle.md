# Side-moment perturbations rigorously exclude every proper-support simple root cycle — preserved pre-item development

## Side-moment perturbations rigorously exclude every proper-support simple root cycle

This repairs the proper-support part of the invalid irrational-separation argument in root §55. No rationality assumption on topological zero weights is used.

Fix normalized cut size p and put t=p/n<1/2. Use only the side-moment perturbation from root §47,

Psi_epsilon(rho,C,s)=rho+epsilon s M(C,rho),

with epsilon>0.

Suppose a positive zero is supported on a simple directed physical cycle

rho_i=e_{v_i}-e_{v_{i+1}},
i=1,...,k,

with positive coefficients lambda_i, side signs s_i in {+1,-1}, and k<n. Thus there is at least one physical coordinate w outside the cycle support.

Write

S_lambda=sum_i lambda_i s_i.

For every cycle edge, the side moment has coordinate -1/n at w. The physical roots vanish at w. Therefore the w-coordinate of

sum_i lambda_i Psi_epsilon(rho_i,C_i,s_i)=0

gives

S_lambda=0.

Now inspect the coordinate v_i. The physical roots contribute

lambda_i-lambda_{i-1}.

For a valid crossing root, root §47 gives side-moment value
1-t-1/n at its source,
t-1/n at its target,
and -1/n elsewhere.

Using S_lambda=0, the v_i equation becomes

lambda_i-lambda_{i-1}
+epsilon[lambda_i s_i(1-t)+lambda_{i-1}s_{i-1}t]
=0.

Equivalently,

lambda_i[1+epsilon s_i(1-t)]
=
lambda_{i-1}[1-epsilon s_{i-1}t].

Choose epsilon<1/(1-t), so all factors are positive. Multiplying around the cycle yields the necessary condition

product_i [1+epsilon s_i(1-t)]
=
product_i [1-epsilon s_i t].

Let a be the number of positive side signs and b the number of negative side signs.

If a=b, the equality becomes

[1-epsilon^2(1-t)^2]^a
=
[1-epsilon^2 t^2]^a,

impossible for every epsilon>0 because 1-t>t.

If a!=b, take logarithms. The difference between the two sides has derivative a-b at epsilon=0, hence is nonzero for all sufficiently small positive epsilon. Since for fixed n and p there are only finitely many pairs (a,b) with a+b<=n, one may choose one uniform epsilon_0(n,p)>0 such that the equality is impossible for every 0<epsilon<epsilon_0 and every unequal pair.

Therefore:

### Theorem

For every normalized p<n/2 there exists epsilon_0>0 such that, for 0<epsilon<epsilon_0, no positive zero of the side-moment perturbed labels can be supported on a single simple physical root cycle using fewer than n coordinates.

Thus every single-cycle perturbed zero is Hamiltonian.

### Significance

This conclusion is valid for arbitrary real positive zero weights. It salvages the strongest robust part of root §55 without irrational moment separation.

It does not classify Hamiltonian cycles, because there is no exterior coordinate forcing S_lambda=0 when the cycle uses all n coordinates. Nor does it exclude a minimal zero whose physical support decomposes into several coupled cycles. Those remain the honest frontier.
