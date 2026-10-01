# Each triple-deletion state has a unique possible re-extension component

## Statement

Let G be a boundary tournament in which the ordered tight triple T=(a,b,c) is mandatory in every spanning two-cover. Fix x in {a,b,c}, and let F_x=P|Q be any two-cover of G-x. If one component, say P, can be enlarged by x to a Hamiltonian induced subtournament G[V(P) union {x}], then P contains the other two vertices of T, and every Hamilton path on V(P) union {x} contains T consecutively. Consequently, if the other two vertices of T lie in different components of F_x, then x Hamiltonizes neither component; if they lie together in P, then Q union {x} is non-Hamiltonian.

## Body

Suppose G[P union {x}] is Hamiltonian and choose any Hamilton path R on that support. Together with the displayed Hamilton path Q, R|Q is a spanning two-cover of G.

Since T is mandatory, one of these two components must contain T consecutively. The Q-component does not contain x, so it cannot contain T. Therefore R must contain all three vertices of T consecutively. In particular P contains the other two vertices T-{x}.

Moreover R was arbitrary. Hence every Hamilton path on P union {x} must contain T consecutively; otherwise that path together with Q would be a spanning two-cover avoiding T.

If the two surviving vertices of T lie in different components P,Q, neither component contains both of them, so neither can be Hamiltonized after adjoining x. If they lie together in P, then Q lacks both surviving T-vertices, so Q union {x} cannot be Hamiltonian by the same argument. ∎
