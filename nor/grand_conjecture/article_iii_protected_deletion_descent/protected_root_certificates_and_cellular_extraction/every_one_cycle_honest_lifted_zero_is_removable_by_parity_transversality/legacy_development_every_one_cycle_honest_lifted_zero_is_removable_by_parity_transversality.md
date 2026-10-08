# Every one-cycle honest lifted zero is removable by parity transversality — preserved pre-item development

Work with the honest switch-prism lifted labels
(rho,s) in W direct-sum R,
with s in {+1,-1}.

Let a support-minimal positive lifted zero have physical support equal to one directed simple cycle
rho_i=e_{x_i}-e_{x_{i+1}},
i mod k.
The physical cycle has a unique positive dependence, so after normalization all coefficients are equal. The lifted scalar equation therefore gives
sum_i s_i=0.

Let S={x_0,...,x_{k-1}}. Because the cycle roots occur in refinements of one ordered-partition carrier cell, block monotonicity around the directed cycle forces all x_i into one tied Coxeter block B.

The lifted cycle labels span a (k-1)-dimensional subspace H whose projection to W_S is an isomorphism. Hence H is the graph of a unique linear functional
f:W_S->R
with f(rho_i)=s_i.

Now choose a chamber refining the same carrier cell in which the cycle vertices occur consecutively inside B in directed cycle order
x_0,x_1,...,x_{k-1}.
All other coordinates of B may be placed before or after this consecutive segment, and all other face blocks remain in their fixed order.

Choose any cut-state vertex of the same product carrier cell. The ambient instance is a counterexample, so the state is bad and the honest labeling selects a violating ternary window with lifted label
(sigma,t),
t in {+1,-1}.

If either endpoint of sigma lies outside S, then sigma is not in W_S and the lifted label is immediately transverse to H.

Otherwise both endpoints lie in S. Because the S coordinates are consecutive in the chamber, the entire ternary window lies inside the S segment and has the form
(x_i,x_{i+1},x_{i+2})
for some linear index i. Thus
sigma=e_{x_i}-e_{x_{i+2}}=rho_i+rho_{i+1}.
Therefore
f(sigma)=s_i+s_{i+1},
which belongs to {-2,0,2}.
But the honest side coordinate t is +/-1. Hence
t != f(sigma),
so (sigma,t) is again transverse to H.

Thus EVERY honest violating-window label available on this cycle-ordered chamber is transverse to the lifted cycle span.

Cone the boundary of the support-minimal zero simplex to any such genuine transverse state label. Projection to (W direct-sum R)/H shows every new cone simplex is zero-free, while every proper old face is zero-free by support minimality. The one-cycle lifted zero is locally removable.

Therefore every support-minimal honest lifted zero supported on a single physical cycle is removable, whether or not that physical cycle is Hamiltonian.

Combined with root 188, the only remaining support-minimal lifted obstruction is the union of exactly two directed simple physical cycles with opposite nonzero side imbalances.
