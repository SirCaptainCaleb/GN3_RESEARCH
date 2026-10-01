# Vertex-minimal equality does not by itself give outside packet expansion

## Statement

The packet-expansion conclusion in 7a55fc8cb587 is not justified by vertex-minimality of an equality-layer counterexample alone. From a nonempty S outside a preserved nonspecial witness and |N(S)|<=d|S|, one may infer that H-S has density at least d and retains the nonspecial edge, but H-S can have minimum degree at most d because deleting S may lower degrees of surviving vertices. In that case H-S satisfies, rather than violates, the equality-layer assertion. Thus no contradiction to minimality follows without a separate minimum-degree-preservation or strengthened inductive hypothesis.

## Body

The proof of 7a55fc8cb587 fixes a nonspecial witness P, takes S disjoint from P, and observes correctly that if |N(S)|<=d|S| then
|E(H-S)|>=d|V(H-S)|
and the nonspecial edge e with witness P survives.

The next step claims that H-S is therefore a smaller counterexample to the equality-layer assertion. This does not follow.

The equality-layer assertion E_ell says that an exact-density P_ell-free graph containing a nonspecial edge must HAVE a vertex of degree at most d. Its negation requires, in addition to density/nonspeciality, minimum degree at least d+1.

Deleting S may reduce the degrees of surviving vertices. Linearity only limits the loss from a single deleted vertex at a surviving vertex to one; a packet S may lower a surviving degree by several units through distinct edges. Hence H-S may have a vertex of degree at most d. If so, it is not a smaller counterexample to E_ell.

Even strengthening the density premise from equality to >=d|V| does not fix this unless the strengthened statement is itself assumed/proved to conclude low degree and minimality is taken among counterexamples with minimum degree>d. The mere facts 'density at least d' and 'nonspecial edge survives' are insufficient.

Therefore the Hall consequence assigning d incidence-disjoint source edges per outside vertex, and the cycle-packet corollary derived from it, should not be used until an additional argument ensures that every such deletion preserves minimum degree>d or otherwise converts the resulting low-degree vertex back into progress in H.
