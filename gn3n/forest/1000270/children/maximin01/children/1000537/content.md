# Global minimum-side deletion states normalize to an endpoint carrying both large-side barriers

## Statement

Let H be a minimum counterexample and let mu be the minimum smaller-component order among all exact two-path covers of all one-vertex deletions. Then either deletion-cover dynamics already exposes an explicit support crossing or relative-order disagreement, or there is a globally extremal deletion state H-y=R|Q with |R|=mu<=|Q| and an endpoint z of R such that, for Q=(q_0,...,q_s), both (q_1,q_0,z) and (z,q_s,q_{s-1}) are tight. The proof begins with a minimum-side transfer dichotomy: any extremal H-x=P|Q has either a two-end barrier vertex of P or a tight bridge (q_0,p_{k+1},p_k,q_s) through a reversed P-edge. A clean deletion-state swap converts the reversed-edge branch into a globally extremal barrier state, and a second minimal-distance argument transports the barrier vertex to an endpoint unless an explicit disagreement occurs.

## Body

# Global minimum-side deletion states normalize to an endpoint carrying both large-side barriers

Let H be a minimum counterexample. Define mu to be the minimum, over all vertices x and all exact two-path covers of H-x, of the order of the smaller component.

The result below packages the full minimum-side normalization: an extremal deletion state either already yields an explicit crossing/order-disagreement witness, or it can be normalized so that an endpoint of the small component simultaneously carries the reversed barriers at both ends of the large component.

## The minimum-side transfer dichotomy

First fix x and choose an exact cover
H-x=P|Q
whose smaller component P has minimum possible order among exact covers of H-x. Write
P=(p_0,...,p_{r-1}),
Q=(q_0,...,q_s),
with r<=|Q|.

Both components have order at least three. If one had order at most two, adjoining x to it gives a set of order at most three, hence a Hamiltonian set; replacing that component by a Hamilton path on the enlarged set would two-cover H.

For 1<=k<=r-1 define
A_k : (q_0,p_k,p_{k-1}) is tight,
and for 0<=k<=r-1 define
B_k : (q_1,q_0,p_k) is tight,
C_k : (p_k,q_s,q_{s-1}) is tight.
For 0<=k<=r-2 define
D_k : (p_{k+1},p_k,q_s) is tight.

Consider
W_k=(p_0,...,p_k,q_0,...,q_s).
If k<r-1 and W_k were tight, then
W_k | (p_{k+1},...,p_{r-1})
would be an exact cover of H-x with smaller component of order r-k-1<r. If k=r-1, W_k would Hamiltonize H-x and W_k|(x) would two-cover H. Hence W_k is never tight.

For k=0, failure of the only new triple gives B_0 by boundary antisymmetry. For k>=1, one of
(p_{k-1},p_k,q_0),
(p_k,q_0,q_1)
fails, so A_k or B_k holds.

Dually, consider
Z_k=(q_0,...,q_s,p_k,...,p_{r-1}).
The same minimality argument shows Z_k is never tight. Thus C_{r-1} holds, and for k<=r-2 at least one of C_k,D_k holds.

If some k has both B_k and C_k, then p_k is a two-end barrier vertex:
(q_1,q_0,p_k)
and
(p_k,q_s,q_{s-1})
are tight.

Otherwise, if some k has both D_k and A_{k+1}, then
(q_0,p_{k+1},p_k,q_s)
is a tight four-vertex path, traversing an ordinary edge of P in reverse between the two endpoints of Q.

These two outcomes are exhaustive. Indeed, assume neither occurs. Starting from B_0, absence of the barrier branch gives not C_0, hence D_0; absence of the reversed-edge branch then gives not A_1, hence B_1. Iterating
B_k => not C_k => D_k => not A_{k+1} => B_{k+1}
forces B_{r-1}, and absence of a barrier at p_{r-1} contradicts C_{r-1}.

Thus every minimum-side deletion state has either a two-end barrier vertex or a reversed-edge bridge.

## Global minimum-side normalization

Now choose globally extremal
H-x=P|Q
with |P|=mu.

If the transfer dichotomy gives a two-end barrier vertex, we already have a globally extremal barrier state. Suppose instead it gives
(q_0,p_{k+1},p_k,q_s)
tight, and put u=p_{k+1}.

Compare the inherited deletion state with an arbitrary exact cover of H-u. If u is internal in P, apply the internal-deletion trichotomy; if u is the endpoint p_{r-1}, apply the endpoint-state trichotomy. Any crossing, bridge disagreement, or relative-order disagreement is an explicit useful output of deletion-cover dynamics.

Otherwise the clean branch replaces u by the old omitted vertex x while leaving Q unchanged:
H-u=R|Q,
with |R|=mu.
Since mu is globally minimal, this is again globally extremal.

In the original state H-x=P|Q, x cannot be prepended or appended to Q, since either extension together with P would two-cover H. Boundary antisymmetry therefore gives
(q_1,q_0,x)
and
(x,q_s,q_{s-1})
tight.
After the clean swap, x belongs to the new small component R, so x is a two-end barrier vertex in the new globally extremal state.

Consequently, unless an explicit deletion-state disagreement has already appeared, a globally minimum-side cover can be chosen in two-end barrier normal form.

## Transporting the barrier to an endpoint

Among all globally extremal barrier states
H-y=R|Q
with |R|=mu, choose one in which the distance along the displayed path R from a barrier vertex z to its nearer endpoint is minimal. Let that distance be d.

Assume d>0. Choose an endpoint of R at distance d from z and let w be the path neighbor of z lying one step toward that endpoint.

If w is internal in R, apply the internal-deletion trichotomy to w. If w is itself the endpoint, which occurs when d=1, apply the endpoint-state trichotomy. Again, any crossing, relative-order disagreement, internal-restoration crossing, or bridge disagreement is already the explicit first outcome.

In the clean branch, w is replaced by the old omitted vertex y, Q remains unchanged, and the new small component still has order mu. Hence the new deletion state is globally extremal.

As before, y could not have been prepended or appended to Q in the old state, or H would have a spanning two-cover. Thus
(q_1,q_0,y)
and
(y,q_s,q_{s-1})
are tight.
After the clean swap, y occupies the former position of w and is therefore a new two-end barrier vertex at distance d-1 from the chosen endpoint. This contradicts minimality of d.

Hence d=0.

Therefore at least one of the following holds:

1. deletion-cover dynamics exposes an explicit support crossing or relative-order disagreement; or
2. there is a globally extremal deletion state
   H-y=R|Q,
   |R|=mu<=|Q|,
   in which an endpoint z of R simultaneously satisfies
   (q_1,q_0,z)
   and
   (z,q_s,q_{s-1})
   tight.

This is the endpoint barrier normal form needed by the defect-compression bridge.
