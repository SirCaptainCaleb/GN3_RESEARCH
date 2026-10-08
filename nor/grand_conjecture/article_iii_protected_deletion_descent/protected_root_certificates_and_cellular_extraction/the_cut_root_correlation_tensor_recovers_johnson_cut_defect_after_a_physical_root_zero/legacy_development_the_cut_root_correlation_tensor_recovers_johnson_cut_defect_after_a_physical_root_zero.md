# The cut root correlation tensor recovers Johnson cut defect after a physical root zero — preserved pre-item development

Let a legitimate cut-crossing protected state consist of a physical cut C and root rho=e_a-e_d with a in C and d outside C. Put
u_C=1_C-(1/2)1
and define the cut-root correlation tensor
T(C,rho)=u_C rho^T.

Then
tr T(C,rho)=<u_C,rho>=1.
Under complement-reversal,
(C,rho)->(C^c,-rho),
so u_C->-u_C and therefore
T(C^c,-rho)=T(C,rho).
Thus T is an EVEN provenance observable: it descends to the antipodal quotient rather than serving as another odd root coordinate.

Now suppose a positive physical root zero has been reduced to one simple directed coordinate cycle
rho_i=e_{x_{i+1}}-e_{x_i}, i mod k.
The unique positive dependence on this simple type-A cycle has equal coefficients, so normalize them to 1/k. Let C_i be the actual protected cut carried by rho_i, with x_{i+1} in C_i and x_i outside C_i. Define
H=(1/k) sum_i T(C_i,rho_i).

Because sum_i rho_i=0, the centering term cancels and
H=(1/k) sum_i 1_{C_i} rho_i^T.

Inspect the column indexed by x_i. Only rho_{i-1} contributes positively there and rho_i negatively there. Hence
k H e_{x_i}=1_{C_{i-1}}-1_{C_i}.

Let
D_i=1_{C_{i-1}}-1_{C_i}+rho_i
be the canonical cut-defect vector. Therefore
D_i = k H e_{x_i}+rho_i.

So the entire Johnson cut-defect circulation of a simple physical root cycle is encoded linearly in the columns of the even tensor H. In particular,
D_i=0 iff H e_{x_i}=-(1/k)rho_i.

Further:
- tr H=1;
- H 1=0 because every rho_i lies in the type-A space;
- if all C_i have one fixed rank, then 1^T H=0 as well, so H acts on W;
- the tensor construction uses the actual cuts and is valid for arbitrary real topological zero weights before cycle extraction; after support-minimal cycle extraction the equal coefficients are forced by the graphic circuit and no irrational-weight argument is needed.

Interpretation. Odd fixed-point topology should force the PHYSICAL root zero. Cut provenance should then be read as a secondary even observable on that zero set, not inserted as a small W-valued perturbation. For a support-minimal root cycle the observable H is exactly a linear encoding of the cut-defect vectors. This avoids the perturbation-stability obstruction for Hamiltonian cycles and the irrational-coefficient audit: H is not asked to destroy the root zero; it diagnoses whether its cuts concatenate.

The next extraction problem can therefore be stated as a zero-set problem: force or choose a physical root zero for which the even tensor H has a column satisfying the zero-defect relation, or prove that nonzero defect columns give a terminating cut-space improvement.
