# A minimum-order one-backward witness has three common deletion-cover states

## Statement

Assume H is a minimum-order boundary tournament with path-cover number three and that a normalized Astra-010 witness for H has exactly one backward comparison alpha between the incident edges ab and bc. Let G be obtained by reversing alpha, so T=(a,b,c) is mandatory in every spanning two-cover of G. Then for each x in {a,b,c}, H-x=G-x, and this common deletion has path-cover number exactly two and is non-Hamiltonian.

## Body

Deleting any x in {a,b,c} removes at least one of the two incident ordinary edges ab,bc whose comparison was reversed. Therefore the changed comparison alpha is absent from the induced subtournament, so H-x and G-x are identical.

Because H has minimum order among counterexamples with path-cover number three, every proper induced subtournament has path-cover number at most two. Hence pc(H-x)<=2.

On the other hand, G has a spanning two-cover and every spanning two-cover of G contains the mandatory ordered triple T. Choose the endpoint-minimal cover A|B carrying T. By 6bf7cd56cda1, deleting any one vertex of T leaves a non-Hamiltonian subtournament of G. Thus G-x is non-Hamiltonian for x in {a,b,c}.

Since H-x=G-x is non-Hamiltonian but has path-cover number at most two, its path-cover number is exactly two. ∎