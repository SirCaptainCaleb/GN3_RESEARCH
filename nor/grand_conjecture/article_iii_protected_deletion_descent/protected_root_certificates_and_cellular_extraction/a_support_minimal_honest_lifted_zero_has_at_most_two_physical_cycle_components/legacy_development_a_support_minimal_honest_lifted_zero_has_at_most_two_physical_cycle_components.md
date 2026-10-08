# A support-minimal honest lifted zero has at most two physical cycle components — preserved pre-item development

## A support-minimal honest lifted zero has at most two physical cycle components

Work in the honest switch-prism target

W direct-sum R

with state labels (rho,s), where rho is a type-A physical window root and s in {+1,-1}.

Let

sum_e lambda_e (rho_e,s_e)=0,
lambda_e>0,

be a support-minimal positive lifted dependence.

### Physical flow decomposition

The physical equation

sum_e lambda_e rho_e=0

is a positive circulation. Decompose it into directed simple physical cycles:

lambda = sum_C mu_C chi_C,
mu_C>0,

where chi_C assigns one common positive unit flow to every directed edge of C.

For a directed cycle C define its signed side imbalance

S(C)=sum_{e in C} s_e.

The lifted scalar equation becomes

sum_C mu_C S(C)=0.

If some cycle has S(C)=0, then its own labels satisfy

sum_{e in C} (rho_e,s_e)=(0,0),

giving a positive lifted subdependence. By support minimality this is possible only when the whole support is that one cycle.

Therefore in a genuinely multi-cycle support-minimal zero, every cycle in every positive cycle decomposition has nonzero side imbalance.

Since the weighted sum of these nonzero imbalances is zero, at least one cycle has positive imbalance and at least one has negative imbalance.

Take one C_+ with S(C_+)>0 and one C_- with S(C_-)<0. Then

(-S(C_-)) sum_{e in C_+}(rho_e,s_e)
+
S(C_+) sum_{e in C_-}(rho_e,s_e)
=0,

because each physical cycle sum is zero and the scalar coordinates cancel.

This is itself a positive lifted dependence supported only on C_+ union C_-.

By support minimality, the entire original support must equal that union.

### Theorem

Every support-minimal honest lifted zero is of exactly one of the following forms:

1. one directed simple physical cycle whose side sum is zero;
2. the union of exactly two directed simple physical cycles with opposite nonzero side sums.

No genuinely minimal lifted zero needs three physical cycle components.

### Intersection bound

The target W direct-sum R has dimension n. Hence a support-minimal positive circuit contains at most n+1 labels.

Let A,B be the physical vertex sets of the two simple cycles in case 2. Their edge counts equal |A| and |B|, so

|A|+|B| <= n+1.

If A union B is all n physical coordinates, then

|A cap B|
=
|A|+|B|-n
<=1.

Thus a full-support two-cycle lifted circuit consists of either:

- two vertex-disjoint directed cycles partitioning V; or
- two directed cycles meeting in exactly one physical coordinate.

This is the complete combinatorial shape of the remaining multi-cycle lifted obstruction before using carrier provenance.
