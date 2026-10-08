# Minimum-hole concatenations are exact minimum-deficiency faces — preserved pre-item development

## Development

## Minimum-hole concatenations attain the deletion distance exactly

Let X be a minimum two-cover deletion set in a boundary tournament H, with |X|=k, and fix a displayed two-cover
H-X=P|Q,
where |P|=r and |Q|=s. For an arbitrary ordering x_1,...,x_k of X, form the spanning order
pi=(P,x_1,...,x_k,Q^rev).

The deletion-distance proof gives
d_2(pi)<=k.
Since k=kappa_2(H)=min_sigma d_2(sigma), every spanning order has d_2 at least k. Hence
d_2(pi)=k.

The inequalities used in the construction are
p(pi)>=r-1
and
q(pi)<=r+k.
Because q-p-1=d_2(pi)=k, both inequalities are equalities:
p(pi)=r-1,
q(pi)=r+k.

Writing m=|V(H)|-2=r+s+k-2 and c(pi)=m+1-q(pi), one obtains
c(pi)=s-1.

Therefore every permutation of the minimum hole X in the concatenation (P,X,Q^rev) has the same exact deficiency and the same exact root:
d_2(pi)=k,
psi(pi)=e_{r-1}-e_{s-1}.

Equivalently, the whole ordered-partition face obtained by freely permuting X is a minimum-deficiency face with constant root. It is a zero-root face exactly when the complementary two-cover is balanced:
|P|=|Q|.

For k=2 and |P|=|Q|=r, every hole order has
p=c=r-1,
q=r+2,
and the four central status positions have the form
0 a b 1.
Thus a symmetric genuine two-deletion state is already an exact minimum-deficiency zero-root state; no second topological passage is needed to obtain equality of the deletion block with kappa_2.

This is a direct sharpening of the deletion-distance identity and uses only minimality of the deletion set, not minimum-counterexample calculus.
