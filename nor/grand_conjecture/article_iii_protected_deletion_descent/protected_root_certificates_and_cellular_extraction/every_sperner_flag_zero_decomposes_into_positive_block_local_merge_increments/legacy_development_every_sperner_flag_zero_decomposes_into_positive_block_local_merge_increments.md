# Every Sperner flag zero decomposes into positive block-local merge increments — preserved pre-item development

## Every Sperner flag zero decomposes into positive block-local merge increments

Use the canonical consecutive-change defect labels

L(F)=C(pi_F)

from roots §§155,163-164.

Suppose the center-replacement/Sperner carrier has a zero supported on a nested proper-face flag

F_1<...<F_k

together with the apex label r_0:

lambda_0 r_0 + sum_{i=1}^k lambda_i L(F_i)=0,

with every displayed lambda positive.

Put

Lambda=sum_{i=1}^k lambda_i

and for j=1,...,k-1 define the positive tail weights

T_j=sum_{i=j+1}^k lambda_i.

Then the discrete Abel identity gives

sum_{i=1}^k lambda_i L(F_i)
=
Lambda L(F_1)
+
sum_{j=1}^{k-1}
T_j [L(F_{j+1})-L(F_j)].

Indeed each increment L(F_{j+1})-L(F_j) contributes to exactly the labels with index greater than j.

Hence every Sperner zero has the equivalent form

lambda_0 r_0
+
Lambda L(F_1)
+
sum_{j=1}^{k-1} T_j Delta_j
=0,

where

Delta_j=L(F_{j+1})-L(F_j)

and every coefficient Lambda,T_j is strictly positive.

### Refining a skipped face step

If F_j<F_{j+1} is not codimension one, insert any saturated chain

F_j=H_0<H_1<...<H_m=F_{j+1}.

Then

Delta_j
=
sum_{ell=0}^{m-1}
[L(H_{ell+1})-L(H_ell)].

The SAME positive coefficient T_j multiplies every inserted codimension-one increment.

Therefore one may refine the flag all the way to codimension-one block merges without changing signs or introducing arbitrary coefficients.

### Locality

By root §164, each codimension-one increment

L(H_{ell+1})-L(H_ell)

is supported in the single proper block merged at that step together with its bounded ternary boundary collar.

Thus a global topological zero decomposes into:

1. the apex isolated-band label r_0;
2. one boundary defect label L(F_1);
3. a positive combination of block-local merge increments, one for each merge in a saturated refinement of the supporting face flag.

No global face-witness mismatch remains hidden in the convex coefficients.

### Consequence

The Sperner extraction problem can be attacked inductively on the merged block size. A failure of compatible realization at a coarse face must already appear in one codimension-one proper-block merge increment. Distant merge increments cannot create a new nonlocal obstruction by themselves; any cancellation between them must pass through overlapping boundary collars or nested blocks.

This gives a precise algebraic interface between boundary degree and the desired relative block-splice theorem.
