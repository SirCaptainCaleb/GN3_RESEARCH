# The consecutive-change defect is a local transition-root sum with only endpoint correction — preserved pre-item development

## Composition

(none yet)

## Development

## The consecutive-change defect is a local transition-root sum with only endpoint correction

Let a ternary coordinate order

pi=(v_1,...,v_n)

have change positions

p_1<...<p_k,

k>=2.

Root §155 defines the consecutive-change defect

C(pi)=sum_{j=1}^{k-1}(e_{v_{p_j}}-e_{v_{p_{j+1}+3}}).

For each actual transition at p_j define its physical slide root

rho_j=e_{v_{p_j}}-e_{v_{p_j+3}}.

Then there is the exact identity

C(pi)
=
sum_{j=1}^k rho_j
+
e_{v_{p_1+3}}
-
e_{v_{p_k}}.

### Proof

The positive terms of C(pi) are

e_{v_{p_1}}+...+e_{v_{p_{k-1}}},

while the negative terms are

-e_{v_{p_2+3}}-...-e_{v_{p_k+3}}.

On the other hand

sum_j rho_j
=
(e_{v_{p_1}}+...+e_{v_{p_k}})
-
(e_{v_{p_1+3}}+...+e_{v_{p_k+3}}).

Subtracting gives exactly

C(pi)-sum_j rho_j
=
e_{v_{p_1+3}}-e_{v_{p_k}}.

### Block-locality consequence

Use the global good-order selector of root §163. Let two codimension-one face witnesses be

pi=P · U · Q,
pi'=P · U' · Q,

where U and U' are two orders of the same merged proper block B and the outside prefix P and suffix Q are identical.

Changing U to U' can alter only:
- ternary windows entirely inside B;
- the two ternary splice layers meeting the left boundary of B;
- the two ternary splice layers meeting the right boundary of B.

Hence every transition root rho_j that differs between pi and pi' is supported on B together with at most the two adjacent outside coordinates on each side.

All transition roots farther away occur in both sums with identical physical endpoints and cancel in

C(pi)-C(pi').

The endpoint correction
e_{v_{p_1+3}}-e_{v_{p_k}}
also cancels whenever the global first/last changes are unaffected. If an extreme change is affected, that change itself lies in the same bounded splice neighborhood, so the altered correction is still supported there.

Therefore:

### Theorem

For canonical nested-face witnesses differing only in one merged proper block B,

C(pi)-C(pi')

is supported entirely on B plus a bounded ternary boundary collar (at most two outside coordinates on each side).

Thus the consecutive-change Sperner label is genuinely LOCAL along every edge of the canonical barycentric face flag, despite its original definition using long consecutive-change macro roots.

### Topological consequence

The one-band Sperner carrier can be viewed as a PL field whose edge increments are proper-block local. A zero simplex therefore assembles from a chain of local proper-subinstance replacement increments, not from unrelated global witness orders.

Combined with the flag-local witness theorem §163, the remaining gluing problem becomes a relative repair problem on one proper block with fixed two-sided boundary memory. No long-range label interaction survives along a face edge.
